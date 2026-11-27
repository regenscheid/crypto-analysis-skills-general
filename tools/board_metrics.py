#!/usr/bin/env python3
"""Validate offline, normalized research-board evidence (optional note-keeping aid).

This belongs with the optional `crypto-workbench-knowledge` aid and its board:
it is an evaluation input contract, not a host API or proof of trace
authenticity. See tests/board-metrics-contract.md. Normalized traces written
with the older field names (``child_frame_id``, ``context_summary``,
``structured_output``) are read as ``worker_id``, ``worker_context`` and
``structured_return``.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
import re
from pathlib import Path

from trace_evidence import _load_trace


BOARD_EVENT_TYPES = (
    "idea", "outcome", "finding", "dismissal", "lemma_proposal",
    "critique", "promote", "close_lane", "sota_row",
)
SOFT_DISMISSAL_REASONS = frozenset({
    "lacked_idea", "lacked_time", "lacked_tools", "lacked_context",
})
CAPTURE_CHANNELS = (
    "board_reads", "board_appends", "delegations", "delegation_returns",
)
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}\Z")
FIELD_ALIASES = {
    "child_frame_id": "worker_id",
    "context_summary": "worker_context",
    "structured_output": "structured_return",
}


def _read_aliases(event: object) -> object:
    """Map the older normalized field names to the current ones."""
    if not isinstance(event, dict):
        return event
    event = dict(event)
    for old, new in FIELD_ALIASES.items():
        if old in event:
            value = event.pop(old)
            if new in event and event[new] != value:
                raise ValueError(f"{old} and {new} disagree")
            event.setdefault(new, value)
    return event


def _nonempty(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a nonempty string")
    return value


def _safe_id(value: object, label: str) -> str:
    value = _nonempty(value, label)
    if not _SAFE_ID.fullmatch(value) or value in {".", ".."}:
        raise ValueError(f"{label} must be a path-safe identifier")
    return value


def _id_list(value: object, label: str) -> list[str]:
    if not isinstance(value, list):
        raise ValueError(f"{label} must be an array")
    ids = [_safe_id(item, f"{label} item") for item in value]
    if len(ids) != len(set(ids)):
        raise ValueError(f"{label} has duplicate IDs")
    return ids


def _text_list(value: object, label: str) -> list[str]:
    if not isinstance(value, list):
        raise ValueError(f"{label} must be an array")
    return [_nonempty(item, f"{label} item") for item in value]


def _valid_id(value: object) -> bool:
    return isinstance(value, str) and value not in {".", ".."} and bool(_SAFE_ID.fullmatch(value))


def _valid_text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _valid_lemma(value: object) -> bool:
    if not isinstance(value, dict) or not _valid_id(value.get("lemma_id")):
        return False
    if not isinstance(value.get("source"), str) or value["source"] not in {"derived", "literature"}:
        return False
    if value["source"] == "literature" and not _valid_text(value.get("locator")):
        return False
    applies_to = value.get("applies_to")
    return (isinstance(value.get("hypotheses"), list)
            and isinstance(applies_to, dict)
            and _valid_text(applies_to.get("target"))
            and bool(applies_to.get("evidence"))
            and isinstance(value.get("known_failures"), list)
            and isinstance(value.get("restates"), list))


def _board_outcome(value: object) -> bool:
    """Validate the required ``board_append(..., 'outcome', payload)`` shape."""
    if not isinstance(value, dict) or not all(
            _valid_id(value.get(key)) for key in ("delegation_id", "idea_id")):
        return False
    if not isinstance(value.get("state"), str) or value["state"] not in {
            "open", "resolved", "obstructed", "split"}:
        return False
    if not all(isinstance(value.get(key), list)
               for key in ("findings", "dismissals", "lemma_proposals")):
        return False
    if not isinstance(value.get("notebook_append"), str):
        return False
    if value["state"] == "split":
        children = value.get("child_idea_ids")
        if (not isinstance(children, list) or not children
                or not all(_valid_id(child) for child in children)
                or len(children) != len(set(children))
                or value["idea_id"] in children):
            return False
        if "child_ideas" in value:
            described = value["child_ideas"]
            if (not isinstance(described, list)
                    or len(described) != len(children)
                    or any(not isinstance(item, dict)
                           or not _valid_id(item.get("idea_id"))
                           or not _valid_text(item.get("title"))
                           or not isinstance(item.get("builds_on"), list)
                           or not all(_valid_id(lemma_id) for lemma_id in item["builds_on"])
                           or len(item["builds_on"]) != len(set(item["builds_on"]))
                           or item.get("state", "open") != "open"
                           for item in described)
                    or {item["idea_id"] for item in described} != set(children)):
                return False
    for finding in value["findings"]:
        if not isinstance(finding, dict) or finding.get("idea_id", value["idea_id"]) != value["idea_id"]:
            return False
        if "dominated_by" not in finding or not _valid_text(finding.get("sota_delta")):
            return False
        if finding["dominated_by"] is None:
            if not _valid_text(finding.get("domination_justification")):
                return False
        elif not _valid_id(finding["dominated_by"]):
            return False
    for dismissal in value["dismissals"]:
        if not isinstance(dismissal, dict) or dismissal.get("idea_id", value["idea_id"]) != value["idea_id"]:
            return False
        reason = dismissal.get("reason_class")
        if not isinstance(reason, str) or reason not in SOFT_DISMISSAL_REASONS | {"demonstrated_obstruction"}:
            return False
        if not _valid_text(dismissal.get("attempted")):
            return False
    return all(_valid_lemma(lemma) for lemma in value["lemma_proposals"])


def _proposal_payloads(event: dict) -> list[dict]:
    payload = event["payload"]
    if event["event_type"] == "lemma_proposal":
        return [payload]
    if event["event_type"] == "outcome":
        proposals = payload.get("lemma_proposals", [])
        if not isinstance(proposals, list) or any(not isinstance(p, dict) for p in proposals):
            raise ValueError("outcome.lemma_proposals must be an array of objects")
        return proposals
    return []


def _has_board_path(summary: object, board_dir: str) -> bool:
    if not isinstance(summary, str):
        return False
    # The suffix boundary prevents /board-old from satisfying /board.
    return re.search(re.escape(board_dir) + r"(?=$|[/\s`'\".,;:)}\]])", summary) is not None


def board_metrics(path: Path) -> dict:
    """Report project/session board behavior from explicit, normalized events.

    A missing capture channel makes every metric depending on it ``None``.
    In particular, absence of an append is evidence only when board appends and
    terminal worker returns were captured completely and outcome provenance is
    known. Event and coverage claims remain the normalizer's responsibility.
    """
    doc = _load_trace(path)
    doc["events"] = [_read_aliases(event) for event in doc["events"]]
    project_id = _safe_id(doc.get("project_id"), "project_id")
    session_id = _safe_id(doc.get("session_id"), "session_id")
    project_dir = Path(_nonempty(doc.get("project_dir"), "project_dir"))
    if not project_dir.is_absolute() or project_dir.name != project_id or any(
            part in {".", ".."} for part in project_dir.parts):
        raise ValueError("project_dir must be an absolute project-specific path")
    project_dir_text = str(project_dir)
    board_dir = str(project_dir / "board")
    coverage = doc.get("capture_complete")
    if not isinstance(coverage, dict) or set(coverage) != set(CAPTURE_CHANNELS) or any(
            type(coverage[key]) is not bool for key in CAPTURE_CHANNELS):
        raise ValueError(f"capture_complete must give boolean coverage for {CAPTURE_CHANNELS}")

    reads: dict[str, tuple[int, dict]] = {}
    appends: list[tuple[int, dict]] = []
    delegates: dict[tuple[str, str], tuple[int, dict]] = {}
    returns: dict[tuple[str, str], tuple[int, dict]] = {}
    append_ids: set[str] = set()
    append_calls: set[str] = set()
    for index, event in enumerate(doc["events"]):
        if not isinstance(event, dict):
            raise ValueError("each trace event must be an object")
        kind = event.get("kind")
        if kind == "board_read":
            call_id = _nonempty(event.get("call_id"), "board_read.call_id")
            if call_id in reads:
                raise ValueError("duplicate board_read call_id")
            if event.get("project_dir") != project_dir_text:
                raise ValueError("board_read project_dir disagrees with trace")
            if event.get("scope") not in {"project", "session"}:
                raise ValueError("board_read.scope must be project or session")
            if event.get("status") not in {"succeeded", "failed"}:
                raise ValueError("board_read.status must be succeeded or failed")
            if event["status"] == "succeeded":
                snapshot = event.get("snapshot")
                if not isinstance(snapshot, dict):
                    raise ValueError("successful board_read requires snapshot")
                opened = _id_list(snapshot.get("open_idea_ids"), "snapshot.open_idea_ids")
                requeue = _id_list(snapshot.get("requeue_idea_ids"), "snapshot.requeue_idea_ids")
                if not set(requeue) <= set(opened):
                    raise ValueError("snapshot requeue IDs must be open ideas")
                _id_list(snapshot.get("promoted_lemma_ids"), "snapshot.promoted_lemma_ids")
                soft = snapshot.get("soft_dismissals")
                if not isinstance(soft, list):
                    raise ValueError("snapshot.soft_dismissals must be an array")
                soft_ids = set()
                for item in soft:
                    if not isinstance(item, dict):
                        raise ValueError("soft dismissal must be an object")
                    sid = _nonempty(item.get("event_id"), "soft dismissal event_id")
                    ordinal = item.get("dismissal_index")
                    if type(ordinal) is not int or ordinal < 0:
                        raise ValueError("soft dismissal needs a nonnegative dismissal_index")
                    _safe_id(item.get("idea_id"), "soft dismissal idea_id")
                    if item.get("reason_class") not in SOFT_DISMISSAL_REASONS:
                        raise ValueError("soft dismissal reason_class is invalid")
                    if (sid, ordinal) in soft_ids:
                        raise ValueError("duplicate soft dismissal event_id/index")
                    soft_ids.add((sid, ordinal))
            reads[call_id] = (index, event)
        elif kind == "board_append":
            call_id = _nonempty(event.get("call_id"), "board_append.call_id")
            if call_id in append_calls:
                raise ValueError("duplicate board_append call_id")
            append_calls.add(call_id)
            eid = _nonempty(event.get("event_id"), "board_append.event_id")
            if eid in append_ids:
                raise ValueError("duplicate board_append event_id")
            append_ids.add(eid)
            if event.get("event_type") not in BOARD_EVENT_TYPES:
                raise ValueError("board_append.event_type is invalid")
            if event.get("session_id") != session_id:
                raise ValueError("board_append session_id disagrees with trace")
            expected_ledger = str(project_dir / "board" / "sessions" / (session_id + ".jsonl"))
            if event.get("ledger_path") != expected_ledger:
                raise ValueError("board_append ledger_path is not this project's session ledger")
            if not isinstance(event.get("payload"), dict):
                raise ValueError("board_append.payload must be an object")
            if event["event_type"] == "idea":
                payload = event["payload"]
                _safe_id(payload.get("idea_id"), "idea payload idea_id")
                _nonempty(payload.get("title"), "idea payload title")
                _id_list(payload.get("builds_on"), "idea payload builds_on")
                if payload.get("state", "open") != "open":
                    raise ValueError("idea payload state must start open")
            if event["event_type"] == "outcome":
                if not _board_outcome(event["payload"]):
                    raise ValueError("board_append outcome payload is invalid")
                source = event.get("capture_source", "unknown")
                if source not in {"delegation_return", "manual", "unknown"}:
                    raise ValueError("outcome capture_source is invalid")
                if source == "delegation_return":
                    delegation_id = _safe_id(event.get("delegation_id"), "outcome delegation_id")
                    _safe_id(event.get("worker_id"), "outcome worker_id")
                    if delegation_id != event["payload"]["delegation_id"]:
                        raise ValueError("outcome payload/provenance delegation_id mismatch")
            if event["event_type"] == "lemma_proposal" and not _valid_lemma(event["payload"]):
                raise ValueError("board_append lemma_proposal payload is invalid")
            appends.append((index, event))
        elif kind == "delegation":
            pair = (_safe_id(event.get("delegation_id"), "delegation_id"),
                    _safe_id(event.get("worker_id"), "worker_id"))
            if pair in delegates:
                raise ValueError("duplicate delegation worker identity")
            if event.get("worker_context") is not None and not isinstance(
                    event["worker_context"], str):
                raise ValueError("worker_context must be a string or null")
            if type(event.get("expects_board_outcome")) is not bool:
                raise ValueError("delegation.expects_board_outcome must be boolean")
            if "idea_id" in event:
                _safe_id(event["idea_id"], "delegation.idea_id")
                _nonempty(event.get("board_read_call_id"), "delegation.board_read_call_id")
            delegates[pair] = (index, event)
        elif kind == "delegation_return":
            pair = (_safe_id(event.get("delegation_id"), "return delegation_id"),
                    _safe_id(event.get("worker_id"), "return worker_id"))
            if pair in returns:
                raise ValueError("duplicate terminal return identity")
            if event.get("status") not in {"completed", "failed", "cancelled"}:
                raise ValueError("delegation_return.status must be terminal")
            output = event.get("structured_return")
            if output is not None and not isinstance(output, dict):
                raise ValueError("structured_return must be an object or null")
            if isinstance(output, dict) and "delegation_id" in output:
                if output["delegation_id"] != pair[0]:
                    raise ValueError("return payload/delegation_id mismatch")
            returns[pair] = (index, event)

    for pair, (_, event) in returns.items():
        if pair in delegates:
            idea_id = delegates[pair][1].get("idea_id")
            output = event.get("structured_return")
            if (idea_id is not None and isinstance(output, dict)
                    and "idea_id" in output and output["idea_id"] != idea_id):
                raise ValueError("return payload/idea_id disagrees with delegation")
    for _, event in appends:
        if event["event_type"] != "outcome" or event.get("capture_source") != "delegation_return":
            continue
        pair = (event["delegation_id"], event["worker_id"])
        if pair in delegates:
            idea_id = delegates[pair][1].get("idea_id")
            if idea_id is not None and event["payload"]["idea_id"] != idea_id:
                raise ValueError("outcome payload/idea_id disagrees with delegation")

    if coverage["board_reads"] and coverage["delegations"]:
        for _, delegation in delegates.values():
            if "idea_id" in delegation:
                ref = delegation["board_read_call_id"]
                if ref not in reads or reads[ref][1]["status"] != "succeeded":
                    raise ValueError("idea delegation lacks a captured successful board read")
    if coverage["delegations"] and coverage["delegation_returns"]:
        if not set(returns) <= set(delegates):
            raise ValueError("delegation return has no captured delegation")
    if len({pair[1] for pair in delegates}) != len(delegates):
        raise ValueError("one worker_id appears in multiple delegations")
    if len({pair[0] for pair in delegates}) != len(delegates):
        raise ValueError("one delegation_id appears in multiple worker requests")
    if coverage["delegations"] and coverage["board_appends"]:
        for _, event in appends:
            if event["event_type"] == "outcome" and event.get("capture_source") == "delegation_return":
                if (event["delegation_id"], event["worker_id"]) not in delegates:
                    raise ValueError("outcome provenance has no captured delegation")

    observed = {
        "board_reads": sum(event["status"] == "succeeded" for _, event in reads.values()),
        "board_appends_by_type": dict(Counter(event["event_type"] for _, event in appends)),
        "delegations": len(delegates),
        "terminal_returns": len(returns),
    }
    result = {"schema_version": 1, "source_trace": doc["source_trace"],
              "project_id": project_id, "session_id": session_id,
              "project_dir": project_dir_text, "capture_complete": coverage,
              "observed": observed, "unverified": []}

    def report(name: str, value: object, channels: tuple[str, ...], verified: bool = True) -> None:
        if verified and all(coverage[channel] for channel in channels):
            result[name] = value
        else:
            result[name] = None
            result["unverified"].append(name)

    report("board_reads", observed["board_reads"], ("board_reads",))
    report("board_appends_by_type", {kind: observed["board_appends_by_type"].get(kind, 0)
                                      for kind in BOARD_EVENT_TYPES}, ("board_appends",))

    classifications = {"carried": set(), "new": set(), "requeued": set()}
    soft_requeued = set()
    unclassified = []
    for index, delegation in delegates.values():
        idea_id = delegation.get("idea_id")
        if idea_id is None:
            continue
        ref = delegation["board_read_call_id"]
        read = reads.get(ref)
        if (read is None or read[1]["status"] != "succeeded"
                or read[1]["scope"] != "project" or read[0] >= index):
            unclassified.append(idea_id)
            continue
        snapshot = read[1]["snapshot"]
        key = (ref, idea_id)
        if idea_id in snapshot["requeue_idea_ids"]:
            classifications["requeued"].add(key)
            soft_requeued.update((item["event_id"], item["dismissal_index"])
                                for item in snapshot["soft_dismissals"]
                                if item["idea_id"] == idea_id)
        elif idea_id in snapshot["open_idea_ids"]:
            classifications["carried"].add(key)
        elif any(read[0] < at < index and event["event_type"] == "idea"
                 and event["payload"]["idea_id"] == idea_id for at, event in appends):
            classifications["new"].add(key)
        else:
            unclassified.append(idea_id)
    idea_verified = not unclassified
    report("ideas_carried", len(classifications["carried"]),
           ("board_reads", "board_appends", "delegations"), idea_verified)
    report("ideas_new", len(classifications["new"]),
           ("board_reads", "board_appends", "delegations"), idea_verified)
    report("ideas_requeued", len(classifications["requeued"]),
           ("board_reads", "board_appends", "delegations"), idea_verified)
    report("soft_dismissals_requeued", len(soft_requeued),
           ("board_reads", "board_appends", "delegations"), idea_verified)
    result["unclassified_idea_ids"] = sorted(set(unclassified))

    rederivations = set()
    unknown_lemma_events = []
    for at, event in appends:
        for proposal in _proposal_payloads(event):
            if proposal.get("source") != "derived":
                continue
            restates = _text_list(proposal.get("restates"), "derived lemma restates")
            _safe_id(proposal.get("lemma_id"), "derived lemma_id")
            prior_reads = [(i, e) for i, e in reads.values()
                           if i < at and e["status"] == "succeeded"
                           and e["scope"] == "project"]
            if not prior_reads:
                unknown_lemma_events.append(event["event_id"])
                continue
            latest_read = max(prior_reads, key=lambda pair: pair[0])[1]
            for prior_id in set(restates) & set(latest_read["snapshot"]["promoted_lemma_ids"]):
                rederivations.add((event["event_id"], proposal["lemma_id"], prior_id))
    report("rederivations_of_existing_lemmas", len(rederivations),
           ("board_reads", "board_appends"), not unknown_lemma_events)
    result["unclassified_lemma_event_ids"] = sorted(set(unknown_lemma_events))

    missing_path = sorted(pair[1] for pair, (_, event) in delegates.items()
                          if not _has_board_path(event.get("worker_context"), board_dir))
    report("delegations_missing_board_path", len(missing_path), ("delegations",))
    result["missing_board_path_worker_ids"] = (
        missing_path if coverage["delegations"] else None)

    appended_returns: dict[tuple[str, str], list[tuple[int, dict]]] = {}
    for at, event in appends:
        if event["event_type"] == "outcome" and event.get("capture_source") == "delegation_return":
            pair = (event["delegation_id"], event["worker_id"])
            appended_returns.setdefault(pair, []).append((at, event))
    ambiguous_outcomes = [event["event_id"] for _, event in appends
                          if event["event_type"] == "outcome"
                          and event.get("capture_source", "unknown") == "unknown"]
    board_returns = {pair: event.get("structured_return") for pair, (_, event) in returns.items()
                     if event["status"] == "completed" and pair in delegates
                     and delegates[pair][1]["expects_board_outcome"]}
    unsatisfied = sorted(pair[1] for pair, payload in board_returns.items()
                         if not _board_outcome(payload))
    unmatched = sorted(pair for pair, payload in board_returns.items()
                       if not _board_outcome(payload) or not any(
                           at > returns[pair][0] and event["payload"] == payload
                           for at, event in appended_returns.get(pair, [])))
    modified = sorted(pair for pair, payload in board_returns.items()
                      if _board_outcome(payload)
                      and any(at > returns[pair][0] for at, _ in appended_returns.get(pair, []))
                      and not any(
                          at > returns[pair][0] and event["payload"] == payload
                          for at, event in appended_returns[pair]))
    duplicate_appends = sorted(pair[1] for pair, events in appended_returns.items()
                               if len(events) > 1)
    report("returns_not_appended", len(unmatched),
           ("board_appends", "delegations", "delegation_returns"),
           not ambiguous_outcomes)
    return_metric_verified = result["returns_not_appended"] is not None
    result["unappended_return_worker_ids"] = (
        [pair[1] for pair in unmatched] if return_metric_verified else None)
    result["modified_return_worker_ids"] = (
        [pair[1] for pair in modified] if return_metric_verified else None)
    result["unsatisfied_board_return_worker_ids"] = (
        unsatisfied if return_metric_verified else None)
    result["duplicate_return_append_worker_ids"] = (
        duplicate_appends if return_metric_verified else None)
    result["unknown_origin_outcome_event_ids"] = sorted(ambiguous_outcomes)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("trace", type=Path)
    args = parser.parse_args()
    try:
        report = board_metrics(args.trace)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
