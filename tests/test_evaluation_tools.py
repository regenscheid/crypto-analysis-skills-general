"""Regression tests for false-positive evaluation evidence."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from trace_evidence import successful_skill_loads


class TraceEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / "trace.json"

    def trace(self, events):
        self.path.write_text(json.dumps({"schema_version": 1,
                                        "source_trace": "original.jsonl", "events": events}))
        return self.path

    def load_event(self, **changes):
        return {"kind": "skill_load", "skill_id": "crypto-investigate", "call_id": "call-1",
                "status": "succeeded", "body_sha256": hashlib.sha256(b"body").hexdigest(),
                **changes}

    def test_plain_text_names_are_not_events(self):
        self.path.write_text("crypto-investigate skill-load-probe")
        with self.assertRaises(ValueError):
            successful_skill_loads(self.path)

    def test_failure_and_response_mentions_do_not_count(self):
        path = self.trace([self.load_event(status="failed"),
                           {"kind": "response", "text": "Loaded crypto-investigate"}])
        self.assertEqual(successful_skill_loads(path), set())

    def test_success_requires_body_identity_and_call_identity(self):
        event = self.load_event()
        self.assertEqual(successful_skill_loads(self.trace([event])), {"crypto-investigate"})
        for key in ["body_sha256", "call_id"]:
            broken = {k: v for k, v in event.items() if k != key}
            with self.subTest(key=key), self.assertRaises(ValueError):
                successful_skill_loads(self.trace([broken]))

    def test_duplicate_calls_are_rejected(self):
        with self.assertRaises(ValueError):
            successful_skill_loads(self.trace([self.load_event(), self.load_event()]))

    def test_padded_empty_report_does_not_become_research_evidence(self):
        case = json.loads((ROOT / "tests/routing-cases.json").read_text())["cases"][0]
        response = Path(self.tmp.name) / "response.md"
        response.write_text("MODE: DISCOVER\n# Skill trace\n" + ", ".join(case["expected_skills"])
                            + "\n# Source grounding\nNo source READ.\n# Coverage\nDEFERRED. "
                            "No candidate was developed; no falsification was attempted.\n")
        self.path.write_text(" ".join(case["expected_skills"]))
        proc = subprocess.run([sys.executable, str(ROOT / "tools/score_routing_response.py"),
                               case["id"], str(response), "--trace", str(self.path)],
                              text=True, capture_output=True)
        result = json.loads(proc.stdout)
        self.assertEqual(proc.returncode, 1)
        self.assertFalse(result["passed"])
        self.assertEqual(result["trace_evidence"], "invalid")
        self.assertEqual(result["research_progress"], "not_assessed")
        self.assertEqual(result["scientific_correctness"], "not_assessed")


if __name__ == "__main__":
    unittest.main()
