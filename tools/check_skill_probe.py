#!/usr/bin/env python3
"""Check a captured skill-probe response and optional call trace."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from trace_evidence import successful_skill_loads


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("response", type=Path, help="file containing the raw model response")
    parser.add_argument(
        "--trace",
        type=Path,
        help="offline normalized JSON load events (tests/evaluation-contract.md)",
    )
    parser.add_argument(
        "--cases",
        type=Path,
        default=REPOSITORY_ROOT / "tests" / "skill-load-probe-cases.json",
    )
    args = parser.parse_args()

    expected = json.loads(args.cases.read_text(encoding="utf-8"))["expected"]
    raw_response = args.response.read_text(encoding="utf-8").strip()
    try:
        actual = json.loads(raw_response)
    except json.JSONDecodeError as error:
        print(f"FAIL adherence: response is not exact JSON ({error})", file=sys.stderr)
        return 1

    failures = []
    if actual != expected:
        failures.append("load/adherence: response does not match the body-only record")
    if args.trace:
        try:
            loaded = successful_skill_loads(args.trace)
            if "skill-load-probe" not in loaded:
                failures.append("load evidence: no successful skill-load-probe event")
        except ValueError as exc:
            failures.append(f"load evidence: {exc}")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}", file=sys.stderr)
        return 1

    if args.trace:
        print("PASS exact-response adherence and recorded load-event evidence; trace authenticity not assessed")
    else:
        print("PASS exact-response adherence; skill loading not assessed without trace evidence")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
