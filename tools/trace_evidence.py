"""Validate offline, normalized skill-load evidence.

This is an evaluation input contract, not a host API or proof of trace authenticity.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def _load_trace(path: Path) -> dict:
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ValueError("trace must be a normalized JSON event document") from exc
    if not isinstance(doc, dict) or type(doc.get("schema_version")) is not int or doc["schema_version"] != 1:
        raise ValueError("trace schema_version must be 1")
    if not isinstance(doc.get("source_trace"), str) or not doc["source_trace"].strip():
        raise ValueError("trace must identify the original captured source_trace")
    if not isinstance(doc.get("events"), list):
        raise ValueError("trace events must be an array")
    return doc


def successful_skill_loads(path: Path) -> set[str]:
    doc = _load_trace(path)
    loaded = set()
    call_ids = set()
    for event in doc["events"]:
        if not isinstance(event, dict):
            raise ValueError("each trace event must be an object")
        if event.get("kind") != "skill_load":
            continue
        if event.get("status") != "succeeded":
            continue
        for key in ("skill_id", "call_id", "body_sha256"):
            if not isinstance(event.get(key), str) or not event[key].strip():
                raise ValueError(f"successful skill_load is missing {key}")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", event["skill_id"]):
            raise ValueError("skill_id must be an exact canonical runtime name")
        if not re.fullmatch(r"[0-9a-f]{64}", event["body_sha256"]):
            raise ValueError("body_sha256 must identify the successfully returned body")
        if event["call_id"] in call_ids:
            raise ValueError("duplicate successful skill-load call_id")
        call_ids.add(event["call_id"])
        loaded.add(event["skill_id"])
    return loaded


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("trace", type=Path)
    args = parser.parse_args()
    try:
        report = sorted(successful_skill_loads(args.trace))
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
