#!/usr/bin/env python3
"""Append-only, project-scoped research board with per-session event ledgers.

The JSONL files are authoritative. Notebook files are derived from logged
``outcome.notebook_append`` text and can be rebuilt after an interrupted write.
No private host API is needed: the root agent passes one absolute
project directory and the host's session identifier to every delegate.
"""

from __future__ import annotations

import argparse
import fcntl
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import time
import uuid


EVENT_TYPES = frozenset({
    "idea", "outcome", "finding", "dismissal", "lemma_proposal",
    "critique", "promote", "close_lane", "sota_row",
})
IDEA_STATES = frozenset({"open", "resolved", "obstructed", "split"})
TERMINAL_STATES = IDEA_STATES - {"open"}
REASON_CLASSES = frozenset({
    "demonstrated_obstruction", "lacked_idea", "lacked_time",
    "lacked_tools", "lacked_context",
})
LEMMA_SOURCES = frozenset({"derived", "literature"})
SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}\Z")
MAX_EVENT_BYTES = 1024 * 1024


class BoardError(ValueError):
    """Invalid board input or damaged event data."""


class BoardWriteError(OSError):
    """A board write failed; the event may or may not have been saved."""


class NotebookMaterializationError(OSError):
    """The event was saved, but its derived notebook needs rebuilding."""


def _safe_id(value: object, label: str) -> str:
    if not isinstance(value, str) or not SAFE_ID.fullmatch(value) or value in {".", ".."}:
        raise BoardError(f"{label} must be a nonempty path-safe identifier")
    return value


def _project_dir(project_dir: str | os.PathLike[str]) -> Path:
    path = Path(project_dir).expanduser()
    if not path.is_absolute():
        raise BoardError("project_dir must be an absolute path resolved by the root agent")
    return path


def project_dir_for_id(project_id: str, base: str | os.PathLike[str] | None = None) -> Path:
    """Return ``<CRYPTO_FILES>/projects/<project_id>`` without creating it.

    CRYPTO_FILES defaults to the historical ``~/crypto-workbench-files`` base.
    A configured relative base is rejected because children have separate CWDs.
    """
    _safe_id(project_id, "project_id")
    root = Path(base if base is not None else
                (os.environ.get("CRYPTO_FILES") or "~/crypto-workbench-files")).expanduser()
    if not root.is_absolute():
        raise BoardError("CRYPTO_FILES/base must be an absolute path")
    return root / "projects" / project_id


def new_idea_id() -> str:
    """Generate a project-wide idea identifier without coordinating writers."""
    return "idea-" + uuid.uuid4().hex


def new_lemma_id() -> str:
    """Generate a project-wide lemma identifier without coordinating writers."""
    return "lemma-" + uuid.uuid4().hex


def _required_text(payload: dict, key: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value.strip():
        raise BoardError(f"payload.{key} must be a nonempty string")
    return value


def _list(payload: dict, key: str) -> list:
    value = payload.get(key)
    if not isinstance(value, list):
        raise BoardError(f"payload.{key} must be an array")
    return value


def _validate_finding(payload: dict) -> None:
    _safe_id(payload.get("idea_id"), "payload.idea_id")
    if "dominated_by" not in payload:
        raise BoardError("finding requires dominated_by (a SOTA row ID or null)")
    dominated_by = payload["dominated_by"]
    if dominated_by is not None:
        _safe_id(dominated_by, "payload.dominated_by")
    else:
        _required_text(payload, "domination_justification")
    _required_text(payload, "sota_delta")


def _validate_dismissal(payload: dict) -> None:
    _safe_id(payload.get("idea_id"), "payload.idea_id")
    if payload.get("reason_class") not in REASON_CLASSES:
        raise BoardError(f"dismissal.reason_class must be one of {sorted(REASON_CLASSES)}")
    _required_text(payload, "attempted")


def _validate_lemma(payload: dict) -> None:
    _safe_id(payload.get("lemma_id"), "payload.lemma_id")
    if payload.get("source") not in LEMMA_SOURCES:
        raise BoardError("lemma source must be derived or literature")
    if payload["source"] == "literature":
        _required_text(payload, "locator")
    _list(payload, "hypotheses")
    applies_to = payload.get("applies_to")
    if not isinstance(applies_to, dict):
        raise BoardError("lemma applies_to must identify target and evidence")
    _required_text(applies_to, "target")
    if not applies_to.get("evidence"):
        raise BoardError("lemma applies_to.evidence is required")
    _list(payload, "known_failures")
    _list(payload, "restates")


def _validate_event(event_type: str, payload: dict) -> None:
    if event_type not in EVENT_TYPES:
        raise BoardError(f"unknown board event type: {event_type!r}")
    if not isinstance(payload, dict):
        raise BoardError("payload must be an object")
    if event_type == "idea":
        _safe_id(payload.get("idea_id"), "payload.idea_id")
        _required_text(payload, "title")
        builds_on = _list(payload, "builds_on")
        for lemma_id in builds_on:
            _safe_id(lemma_id, "payload.builds_on item")
        if len(builds_on) != len(set(builds_on)):
            raise BoardError("idea.builds_on must not repeat lemma IDs")
        if payload.get("state", "open") != "open":
            raise BoardError("a new idea must start open")
    elif event_type == "outcome":
        _safe_id(payload.get("idea_id"), "payload.idea_id")
        _safe_id(payload.get("delegation_id"), "payload.delegation_id")
        if payload.get("state") not in IDEA_STATES:
            raise BoardError(f"outcome.state must be one of {sorted(IDEA_STATES)}")
        for key in ("findings", "dismissals", "lemma_proposals"):
            if not isinstance(payload.get(key), list):
                raise BoardError(f"outcome.{key} must be an array")
        if not isinstance(payload.get("notebook_append"), str):
            raise BoardError("outcome.notebook_append must be a string")
        if payload["state"] == "split":
            children = _list(payload, "child_idea_ids")
            for child in children:
                _safe_id(child, "payload.child_idea_ids item")
            if not children or len(children) != len(set(children)):
                raise BoardError("split outcome requires distinct child_idea_ids")
            if payload["idea_id"] in children:
                raise BoardError("split child cannot be the parent idea")
            if "child_ideas" in payload:
                child_ideas = _list(payload, "child_ideas")
                described = []
                for child_idea in child_ideas:
                    if not isinstance(child_idea, dict):
                        raise BoardError("outcome.child_ideas items must be objects")
                    _validate_event("idea", child_idea)
                    described.append(child_idea["idea_id"])
                if set(described) != set(children) or len(described) != len(children):
                    raise BoardError("child_ideas must define exactly child_idea_ids")
        for item in payload.get("findings", []):
            if not isinstance(item, dict):
                raise BoardError("outcome.findings items must be objects")
            if "idea_id" in item and item["idea_id"] != payload["idea_id"]:
                raise BoardError("outcome finding idea_id disagrees with outcome.idea_id")
            _validate_finding({**item, "idea_id": payload["idea_id"]})
        for item in payload.get("dismissals", []):
            if not isinstance(item, dict):
                raise BoardError("outcome.dismissals items must be objects")
            if "idea_id" in item and item["idea_id"] != payload["idea_id"]:
                raise BoardError("outcome dismissal idea_id disagrees with outcome.idea_id")
            _validate_dismissal({**item, "idea_id": payload["idea_id"]})
        for item in payload.get("lemma_proposals", []):
            if not isinstance(item, dict):
                raise BoardError("outcome.lemma_proposals items must be objects")
            _validate_lemma(item)
    elif event_type == "finding":
        _validate_finding(payload)
    elif event_type == "dismissal":
        _validate_dismissal(payload)
    elif event_type == "lemma_proposal":
        _validate_lemma(payload)
    elif event_type == "critique":
        _safe_id(payload.get("pass_id"), "payload.pass_id")
        _required_text(payload, "critique_ref")
        _required_text(payload, "summary")
        idea_ids = _list(payload, "idea_ids")
        for idea_id in idea_ids:
            _safe_id(idea_id, "payload.idea_ids item")
        if not idea_ids or len(idea_ids) != len(set(idea_ids)):
            raise BoardError("critique requires distinct nonempty idea_ids")
    elif event_type == "promote":
        kind = payload.get("kind")
        _required_text(payload, "critique_ref")
        if kind == "idea_state":
            _safe_id(payload.get("idea_id"), "payload.idea_id")
            state = payload.get("state")
            if state not in TERMINAL_STATES:
                raise BoardError("idea_state promotion requires resolved, obstructed, or split")
            if state == "obstructed" and payload.get("reason_class") != "demonstrated_obstruction":
                raise BoardError("obstructed requires demonstrated_obstruction")
            if state == "split":
                children = _list(payload, "child_idea_ids")
                for child in children:
                    _safe_id(child, "payload.child_idea_ids item")
                if not children or len(children) != len(set(children)):
                    raise BoardError("split requires distinct child_idea_ids")
                if payload["idea_id"] in children:
                    raise BoardError("split child cannot be the parent idea")
        elif kind == "lemma":
            lemma = payload.get("lemma")
            if not isinstance(lemma, dict):
                raise BoardError("lemma promotion requires a lemma object")
            _validate_lemma(lemma)
            evidence = _list(payload, "evidence")
            if lemma["source"] == "derived":
                for evidence_kind in ("derivation", "independent-check"):
                    if not any(
                        isinstance(item, dict) and item.get("kind") == evidence_kind
                        and isinstance(item.get("ref"), str) and item["ref"].strip()
                        for item in evidence
                    ):
                        raise BoardError(
                            f"derived lemma promotion requires {evidence_kind} evidence")
                _safe_id(payload.get("knowledge_id"), "payload.knowledge_id")
        else:
            raise BoardError("promote.kind must be idea_state or lemma")
    elif event_type == "close_lane":
        _safe_id(payload.get("lane_id"), "payload.lane_id")
        _required_text(payload, "critique_ref")
        _required_text(payload, "excluded_scope")
        if payload.get("reason_class") != "demonstrated_obstruction":
            raise BoardError("only demonstrated_obstruction can close a lane")
    elif event_type == "sota_row":
        _safe_id(payload.get("row_id"), "payload.row_id")
        _required_text(payload, "catalog_record_id")
        _required_text(payload, "published_ref")


def _ledger_path(project_dir: Path, session_id: str) -> Path:
    return project_dir / "board" / "sessions" / (session_id + ".jsonl")


def notebook_path(project_dir: str | os.PathLike[str], session_id: str,
                  idea_id: str) -> Path:
    """Return the derived per-session notebook path for an idea."""
    project = _project_dir(project_dir)
    return project / "board" / "notebooks" / _safe_id(session_id, "session_id") / (
        _safe_id(idea_id, "idea_id") + ".md")


def _write_once(path: Path, data: bytes) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX)
            written = os.write(fd, data)
            if written != len(data):
                raise BoardWriteError(f"short append to {path}: {written}/{len(data)} bytes")
        finally:
            fcntl.flock(fd, fcntl.LOCK_UN)
            os.close(fd)
    except OSError as exc:
        raise BoardWriteError(f"cannot append to {path}: {exc}") from exc


def board_append(project_dir: str | os.PathLike[str], session_id: str,
                 event_type: str, payload: dict,
                 provenance: dict | None = None) -> str:
    """Append one validated JSON event in one OS write and return its UUID.

    The passed payload is stored unchanged. In particular, an ``outcome`` is a
    mechanical record of a child's structured return; a later critic event is
    needed to change idea state or promote a lemma.
    """
    project = _project_dir(project_dir)
    session = _safe_id(session_id, "session_id")
    _validate_event(event_type, payload)
    if provenance is not None:
        if event_type != "outcome" or not isinstance(provenance, dict):
            raise BoardError("provenance is only accepted for an outcome object")
        provenance = {
            "delegation_id": _safe_id(provenance.get("delegation_id"),
                                       "provenance.delegation_id"),
            "child_frame_id": _safe_id(provenance.get("child_frame_id"),
                                        "provenance.child_frame_id"),
        }
        if provenance["delegation_id"] != payload["delegation_id"]:
            raise BoardError("outcome provenance delegation_id must match its payload")
    event_id = str(uuid.uuid4())
    event = {"event_id": event_id, "session_id": session, "type": event_type,
             "at_ns": time.time_ns(), "payload": payload}
    if provenance is not None:
        event["provenance"] = provenance
    try:
        data = (json.dumps(event, ensure_ascii=False, separators=(",", ":"),
                           allow_nan=False) + "\n").encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise BoardError("payload must be finite JSON data") from exc
    if len(data) > MAX_EVENT_BYTES:
        raise BoardError(f"event exceeds {MAX_EVENT_BYTES} bytes; split the return")
    _write_once(_ledger_path(project, session), data)
    if event_type == "outcome" and payload.get("notebook_append"):
        try:
            rebuild_notebook(project, session, payload["idea_id"])
        except OSError as exc:
            raise NotebookMaterializationError(
                f"event {event_id} was appended; rebuild its notebook from the ledger: {exc}") from exc
    return event_id


def _read_ledger(path: Path) -> list[dict]:
    if not path.exists():
        return []
    events = []
    try:
        with path.open("r", encoding="utf-8") as fh:
            fcntl.flock(fh.fileno(), fcntl.LOCK_SH)
            for line_number, line in enumerate(fh, 1):
                try:
                    event = json.loads(line)
                except ValueError as exc:
                    raise BoardError(f"invalid JSON at {path}:{line_number}") from exc
                if not isinstance(event, dict) or event.get("type") not in EVENT_TYPES:
                    raise BoardError(f"invalid event at {path}:{line_number}")
                if event.get("session_id") != path.stem:
                    raise BoardError(f"session mismatch at {path}:{line_number}")
                if not isinstance(event.get("payload"), dict):
                    raise BoardError(f"missing payload at {path}:{line_number}")
                events.append(event)
            fcntl.flock(fh.fileno(), fcntl.LOCK_UN)
    except OSError as exc:
        raise BoardError(f"cannot read board ledger {path}: {exc}") from exc
    return events


def rebuild_notebook(project_dir: str | os.PathLike[str], session_id: str,
                     idea_id: str) -> Path:
    """Materialize one notebook from the authoritative ledger, safely to repeat."""
    project = _project_dir(project_dir)
    session = _safe_id(session_id, "session_id")
    idea = _safe_id(idea_id, "idea_id")
    target = notebook_path(project, session, idea)
    target.parent.mkdir(parents=True, exist_ok=True)
    lock_path = target.with_suffix(".lock")
    with lock_path.open("a") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        chunks = [event["payload"]["notebook_append"]
                  for event in _read_ledger(_ledger_path(project, session))
                  if event["type"] == "outcome"
                  and event["payload"].get("idea_id") == idea
                  and event["payload"].get("notebook_append")]
        fd, temporary = tempfile.mkstemp(prefix=".notebook-", dir=target.parent)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                fh.write("".join(chunks))
            os.replace(temporary, target)
        except BaseException:
            if os.path.exists(temporary):
                os.unlink(temporary)
            raise
    return target


def board_snapshot(project_dir: str | os.PathLike[str],
                   session_id: str | None = None) -> dict:
    """Reduce all project ledgers, or just one session, into the current board."""
    project = _project_dir(project_dir)
    if session_id is not None:
        files = [_ledger_path(project, _safe_id(session_id, "session_id"))]
    else:
        files = sorted((project / "board" / "sessions").glob("*.jsonl"))
    events = [event for path in files for event in _read_ledger(path)]
    events.sort(key=lambda event: (event.get("at_ns", 0), event.get("event_id", "")))
    ideas: dict[str, dict] = {}
    findings: list[dict] = []
    dismissals: list[dict] = []
    lemma_proposals: list[dict] = []
    lemmas: list[dict] = []
    critiques: list[dict] = []
    closed_lanes: dict[str, dict] = {}
    sota_rows: dict[str, dict] = {}

    def idea_record(idea_id: str, session: str) -> dict:
        if idea_id not in ideas:
            ideas[idea_id] = {"idea_id": idea_id, "state": "open",
                              "origin_session_id": session, "details": {},
                              "defined": False,
                              "reported_states": [], "notebook_paths": [],
                              "critique_refs": [],
                              "child_idea_ids": []}
        return ideas[idea_id]

    for event in events:
        kind, payload, session = event["type"], event["payload"], event["session_id"]
        event_ref = {"event_id": event["event_id"], "session_id": session}
        if kind == "idea":
            idea = idea_record(payload["idea_id"], session)
            if idea["defined"]:
                raise BoardError(f"duplicate idea ID {payload['idea_id']} in project board")
            idea["defined"] = True
            idea["origin_session_id"] = session
            idea["details"].update(payload)
        elif kind == "outcome":
            idea = idea_record(payload["idea_id"], session)
            idea["reported_states"].append({**event_ref, "state": payload["state"]})
            if payload.get("notebook_append"):
                notebook = str(notebook_path(project, session, payload["idea_id"]))
                if notebook not in idea["notebook_paths"]:
                    idea["notebook_paths"].append(notebook)
            for item in payload.get("findings", []):
                findings.append({**event_ref, "idea_id": payload["idea_id"], "finding": item})
            for item in payload.get("dismissals", []):
                dismissals.append({**event_ref, "idea_id": payload["idea_id"], "dismissal": item})
            for item in payload.get("lemma_proposals", []):
                lemma_proposals.append({**event_ref, "lemma": item})
        elif kind == "finding":
            findings.append({**event_ref, "idea_id": payload["idea_id"], "finding": payload})
        elif kind == "dismissal":
            dismissals.append({**event_ref, "idea_id": payload["idea_id"], "dismissal": payload})
        elif kind == "lemma_proposal":
            lemma_proposals.append({**event_ref, "lemma": payload})
        elif kind == "critique":
            critiques.append({**event_ref, **payload})
            for idea_id in payload["idea_ids"]:
                idea = idea_record(idea_id, session)
                idea["critique_refs"].append(payload["critique_ref"])
        elif kind == "promote":
            if payload["kind"] == "idea_state":
                idea = idea_record(payload["idea_id"], session)
                idea["state"] = payload["state"]
                idea["critique_ref"] = payload["critique_ref"]
                idea["child_idea_ids"] = payload.get("child_idea_ids", [])
                if payload["state"] == "split":
                    for child_id in payload["child_idea_ids"]:
                        child = idea_record(child_id, session)
                        child["details"].setdefault("parent_idea_id", payload["idea_id"])
            else:
                lemma = payload["lemma"]
                lemmas.append({**event_ref, "lemma": lemma,
                               "evidence": payload["evidence"],
                               "critique_ref": payload["critique_ref"]})
        elif kind == "close_lane":
            closed_lanes[payload["lane_id"]] = {**event_ref, **payload}
        elif kind == "sota_row":
            sota_rows[payload["row_id"]] = {**event_ref, **payload}

    soft_dismissals = [item for item in dismissals
                       if item["dismissal"]["reason_class"] != "demonstrated_obstruction"]
    open_ideas = [idea for idea in ideas.values() if idea["state"] == "open"]
    ready_open_ideas = [idea for idea in open_ideas if idea["defined"]]
    def conflicting_lemma_ids(records: list[dict]) -> list[str]:
        by_id: dict[str, set[str]] = {}
        for record in records:
            lemma = record["lemma"]
            by_id.setdefault(lemma["lemma_id"], set()).add(
                json.dumps(lemma, sort_keys=True, ensure_ascii=False))
        return sorted(lemma_id for lemma_id, versions in by_id.items()
                      if len(versions) > 1)

    return {"project_dir": str(project), "session_id": session_id,
            "event_count": len(events), "ideas": list(ideas.values()),
            "open_ideas": open_ideas, "ready_open_ideas": ready_open_ideas,
            "requeue_idea_ids": sorted({item["idea_id"] for item in soft_dismissals
                                        if item["idea_id"] in ideas
                                        and ideas[item["idea_id"]]["state"] == "open"}),
            "findings": findings, "dismissals": dismissals,
            "soft_dismissals": soft_dismissals,
            "lemma_proposals": lemma_proposals,
            "lemma_proposal_conflicts": conflicting_lemma_ids(lemma_proposals),
            "lemmas": lemmas,
            "promoted_lemma_conflicts": conflicting_lemma_ids(lemmas),
            "critiques": critiques,
            "closed_lanes": list(closed_lanes.values()),
            "sota_rows": list(sota_rows.values())}


def board_selftest() -> bool:
    """Run the focused local regression suite; returns True on success."""
    import unittest
    suite = unittest.defaultTestLoader.discover(
        str(Path(__file__).resolve().parents[3] / "tests"), pattern="test_board.py")
    return unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--snapshot", metavar="PROJECT_DIR")
    parser.add_argument("--session-id", help="filter --snapshot to this session")
    args = parser.parse_args()
    if args.selftest:
        return 0 if board_selftest() else 1
    if args.snapshot:
        print(json.dumps(board_snapshot(args.snapshot, args.session_id), indent=2,
                         ensure_ascii=False))
        return 0
    parser.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
