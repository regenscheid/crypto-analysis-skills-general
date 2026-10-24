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
from trace_evidence import board_metrics, successful_skill_loads


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


class BoardMetricTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / "trace.json"
        self.project_dir = Path(self.tmp.name) / "projects" / "proj_demo"
        self.ledger = str(self.project_dir / "board" / "sessions" / "session-1.jsonl")
        self.board_path = str(self.project_dir / "board")

    def trace(self, events, **changes):
        doc = {"schema_version": 1, "source_trace": "original-host-tape.jsonl",
               "project_id": "proj_demo", "session_id": "session-1",
               "project_dir": str(self.project_dir),
               "capture_complete": {"board_reads": True, "board_appends": True,
                                    "delegations": True, "delegation_returns": True},
               "events": events}
        doc.update(changes)
        self.path.write_text(json.dumps(doc), encoding="utf-8")
        return self.path

    def read(self):
        return {"kind": "board_read", "call_id": "read-1", "status": "succeeded",
                "project_dir": str(self.project_dir), "scope": "project",
                "snapshot": {"open_idea_ids": ["carried", "soft"],
                             "requeue_idea_ids": ["soft"],
                             "soft_dismissals": [{"event_id": "dismiss-1",
                                                  "dismissal_index": 0,
                                                  "idea_id": "soft",
                                                  "reason_class": "lacked_tools"}],
                             "promoted_lemma_ids": ["lemma-old"]}}

    def append(self, event_id, event_type, payload, **changes):
        return {"kind": "board_append", "call_id": "append-" + event_id,
                "event_id": event_id, "event_type": event_type,
                "session_id": "session-1", "ledger_path": self.ledger,
                "payload": payload, **changes}

    def delegate(self, idea_id, number, context_summary):
        return {"kind": "delegation", "delegation_id": "delegate-" + number,
                "child_frame_id": "child-" + number, "idea_id": idea_id,
                "board_read_call_id": "read-1", "context_summary": context_summary,
                "expects_board_outcome": True}

    @staticmethod
    def outcome(idea_id, number="1"):
        return {"delegation_id": "delegate-" + number,
                "idea_id": idea_id, "state": "open", "findings": [],
                "dismissals": [], "lemma_proposals": [], "notebook_append": ""}

    def test_report_uses_snapshot_ids_and_exact_return_correlation(self):
        first = self.outcome("carried")
        second = self.outcome("soft", "2")
        events = [
            self.read(),
            self.append("idea-append", "idea", {"idea_id": "new", "title": "New idea",
                                                   "builds_on": []}),
            self.delegate("carried", "1", "Read " + self.board_path + "/sessions/session-1.jsonl"),
            self.delegate("soft", "2", "Read " + self.board_path + "-old"),
            self.delegate("new", "3", "Read " + self.board_path),
            {"kind": "delegation_return", "delegation_id": "delegate-1",
             "child_frame_id": "child-1", "status": "completed", "structured_output": first},
            self.append("outcome-append", "outcome", first,
                        capture_source="delegation_return", delegation_id="delegate-1",
                        child_frame_id="child-1"),
            {"kind": "delegation_return", "delegation_id": "delegate-2",
             "child_frame_id": "child-2", "status": "completed", "structured_output": second},
            self.append("lemma-append", "lemma_proposal",
                        {"lemma_id": "lemma-new", "source": "derived",
                         "hypotheses": [], "applies_to": {"target": "T", "evidence": "E"},
                         "known_failures": [], "restates": ["lemma-old"]}),
        ]
        report = board_metrics(self.trace(events))
        self.assertEqual(report["board_reads"], 1)
        self.assertEqual(report["board_appends_by_type"]["idea"], 1)
        self.assertEqual(report["board_appends_by_type"]["outcome"], 1)
        self.assertEqual(report["board_appends_by_type"]["lemma_proposal"], 1)
        self.assertEqual((report["ideas_carried"], report["ideas_new"],
                          report["ideas_requeued"]), (1, 1, 1))
        self.assertEqual(report["soft_dismissals_requeued"], 1)
        self.assertEqual(report["rederivations_of_existing_lemmas"], 1)
        self.assertEqual(report["delegations_missing_board_path"], 1)
        self.assertEqual(report["missing_board_path_child_frame_ids"], ["child-2"])
        self.assertEqual(report["returns_not_appended"], 1)
        self.assertEqual(report["unappended_return_child_frame_ids"], ["child-2"])
        self.assertEqual(report["unverified"], [])

    def test_incomplete_capture_is_unverified_not_zero(self):
        coverage = {"board_reads": True, "board_appends": False,
                    "delegations": True, "delegation_returns": False}
        events = [self.read(), self.delegate("carried", "1", self.board_path)]
        report = board_metrics(self.trace(events, capture_complete=coverage))
        self.assertEqual(report["board_reads"], 1)
        self.assertIsNone(report["board_appends_by_type"])
        self.assertIsNone(report["ideas_carried"])
        self.assertIsNone(report["returns_not_appended"])
        self.assertEqual(report["delegations_missing_board_path"], 0)
        self.assertIn("returns_not_appended", report["unverified"])

    def test_unknown_outcome_origin_makes_negative_return_metric_unverified(self):
        outcome = self.outcome("carried")
        events = [self.read(), self.delegate("carried", "1", self.board_path),
                  {"kind": "delegation_return", "delegation_id": "delegate-1",
                   "child_frame_id": "child-1", "status": "completed",
                   "structured_output": outcome},
                  self.append("outcome-unknown", "outcome", outcome)]
        report = board_metrics(self.trace(events))
        self.assertIsNone(report["returns_not_appended"])
        self.assertEqual(report["unknown_origin_outcome_event_ids"], ["outcome-unknown"])

    def test_modified_return_is_not_a_verbatim_append(self):
        outcome = self.outcome("carried")
        changed = {**outcome, "state": "resolved"}
        events = [self.read(), self.delegate("carried", "1", self.board_path),
                  {"kind": "delegation_return", "delegation_id": "delegate-1",
                   "child_frame_id": "child-1", "status": "completed",
                   "structured_output": outcome},
                  self.append("outcome-edited", "outcome", changed,
                              capture_source="delegation_return",
                              delegation_id="delegate-1", child_frame_id="child-1")]
        report = board_metrics(self.trace(events))
        self.assertEqual(report["returns_not_appended"], 1)
        self.assertEqual(report["modified_return_child_frame_ids"], ["child-1"])

    def test_expected_board_return_without_schema_fields_is_not_appended(self):
        events = [self.read(), self.delegate("carried", "1", self.board_path),
                  {"kind": "delegation_return", "delegation_id": "delegate-1",
                   "child_frame_id": "child-1", "status": "completed",
                   "structured_output": {"summary": "No board fields"}}]
        report = board_metrics(self.trace(events))
        self.assertEqual(report["returns_not_appended"], 1)
        self.assertEqual(report["unsatisfied_board_return_child_frame_ids"], ["child-1"])

    def test_rejects_cross_project_ledger_and_duplicate_event_ids(self):
        idea = {"idea_id": "new", "title": "New idea", "builds_on": []}
        wrong = self.append("event-1", "idea", idea,
                            ledger_path="/tmp/other/sessions/session-1.jsonl")
        with self.assertRaisesRegex(ValueError, "ledger_path"):
            board_metrics(self.trace([wrong]))
        event = self.append("event-1", "idea", idea)
        with self.assertRaisesRegex(ValueError, "duplicate board_append"):
            board_metrics(self.trace([event, event]))

    def test_session_scoped_read_cannot_verify_project_wide_carry(self):
        read = {**self.read(), "scope": "session"}
        report = board_metrics(self.trace([read, self.delegate("carried", "1", self.board_path)]))
        self.assertEqual(report["board_reads"], 1)
        self.assertIsNone(report["ideas_carried"])
        self.assertEqual(report["unclassified_idea_ids"], ["carried"])

    def test_multiple_soft_dismissals_in_one_outcome_have_distinct_ordinals(self):
        read = self.read()
        read["snapshot"]["soft_dismissals"].append(
            {"event_id": "dismiss-1", "dismissal_index": 1,
             "idea_id": "soft", "reason_class": "lacked_context"})
        report = board_metrics(self.trace([read, self.delegate("soft", "2", self.board_path)]))
        self.assertEqual(report["soft_dismissals_requeued"], 2)
        read["snapshot"]["soft_dismissals"][1]["dismissal_index"] = 0
        with self.assertRaisesRegex(ValueError, "duplicate soft dismissal"):
            board_metrics(self.trace([read]))

    def test_delegation_ids_must_match_return_and_persisted_provenance(self):
        outcome = self.outcome("carried")
        wrong_return = {"kind": "delegation_return", "delegation_id": "delegate-1",
                        "child_frame_id": "child-1", "status": "completed",
                        "structured_output": {**outcome, "delegation_id": "other"}}
        with self.assertRaisesRegex(ValueError, "return payload/delegation_id"):
            board_metrics(self.trace([self.read(), self.delegate("carried", "1", self.board_path),
                                      wrong_return]))
        wrong_append = self.append("outcome-1", "outcome", outcome,
                                   capture_source="delegation_return",
                                   delegation_id="other", child_frame_id="child-1")
        with self.assertRaisesRegex(ValueError, "outcome payload/provenance"):
            board_metrics(self.trace([wrong_append]))
        duplicate = self.delegate("soft", "2", self.board_path)
        duplicate["delegation_id"] = "delegate-1"
        with self.assertRaisesRegex(ValueError, "one delegation_id"):
            board_metrics(self.trace([self.read(), self.delegate("carried", "1", self.board_path),
                                      duplicate]))

    def test_split_return_needs_child_ids(self):
        split = {**self.outcome("carried"), "state": "split"}
        events = [self.read(), self.delegate("carried", "1", self.board_path),
                  {"kind": "delegation_return", "delegation_id": "delegate-1",
                   "child_frame_id": "child-1", "status": "completed",
                   "structured_output": split}]
        report = board_metrics(self.trace(events))
        self.assertEqual(report["unsatisfied_board_return_child_frame_ids"], ["child-1"])
        with self.assertRaisesRegex(ValueError, "outcome payload is invalid"):
            board_metrics(self.trace([self.append("outcome-1", "outcome", split)]))
        split["child_idea_ids"] = ["child-idea"]
        split["child_ideas"] = [{"idea_id": "different", "title": "Explore a quotient",
                                 "builds_on": []}]
        with self.assertRaisesRegex(ValueError, "outcome payload is invalid"):
            board_metrics(self.trace([self.append("outcome-2", "outcome", split)]))

    def test_outcome_dismissal_requires_attempted_text(self):
        outcome = {**self.outcome("carried"),
                   "dismissals": [{"reason_class": "lacked_tools"}]}
        with self.assertRaisesRegex(ValueError, "outcome payload is invalid"):
            board_metrics(self.trace([self.append("outcome-1", "outcome", outcome)]))
        outcome["dismissals"][0]["attempted"] = "Checked the available tools"
        report = board_metrics(self.trace([self.append("outcome-1", "outcome", outcome,
                                                       capture_source="manual")]))
        self.assertEqual(report["board_appends_by_type"]["outcome"], 1)

    def test_return_and_append_idea_ids_must_match_delegation(self):
        outcome = self.outcome("soft")
        ret = {"kind": "delegation_return", "delegation_id": "delegate-1",
               "child_frame_id": "child-1", "status": "completed",
               "structured_output": outcome}
        with self.assertRaisesRegex(ValueError, "return payload/idea_id"):
            board_metrics(self.trace([self.read(), self.delegate("carried", "1", self.board_path),
                                      ret]))
        append = self.append("outcome-1", "outcome", outcome,
                             capture_source="delegation_return",
                             delegation_id="delegate-1", child_frame_id="child-1")
        with self.assertRaisesRegex(ValueError, "outcome payload/idea_id"):
            board_metrics(self.trace([self.read(), self.delegate("carried", "1", self.board_path),
                                      append]))

    def test_append_before_return_does_not_count_as_return_append(self):
        outcome = self.outcome("carried")
        append = self.append("outcome-1", "outcome", outcome,
                             capture_source="delegation_return",
                             delegation_id="delegate-1", child_frame_id="child-1")
        ret = {"kind": "delegation_return", "delegation_id": "delegate-1",
               "child_frame_id": "child-1", "status": "completed",
               "structured_output": outcome}
        report = board_metrics(self.trace([self.read(), self.delegate("carried", "1", self.board_path),
                                           append, ret]))
        self.assertEqual(report["returns_not_appended"], 1)
        self.assertEqual(report["modified_return_child_frame_ids"], [])


if __name__ == "__main__":
    unittest.main()
