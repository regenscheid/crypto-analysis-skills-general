"""Focused checks for the project research board's storage and reducer."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import uuid


BOARD_SCRIPT = Path(__file__).resolve().parents[1] / "skills" / "crypto-workbench-knowledge" / "scripts"
sys.path.insert(0, str(BOARD_SCRIPT))
from board import (BoardError, board_append, board_snapshot, new_idea_id,
                   new_lemma_id, notebook_path, project_dir_for_id,
                   rebuild_notebook)


class BoardTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.project = project_dir_for_id("proj_test", self.temporary.name)

    def outcome(self, idea_id: str, **changes) -> dict:
        return {"idea_id": idea_id, "delegation_id": "delegation-" + uuid.uuid4().hex,
                "state": "open", "findings": [],
                "dismissals": [], "lemma_proposals": [], "notebook_append": "",
                **changes}

    def idea(self, idea_id: str, title: str = "Test an invariant") -> dict:
        return {"idea_id": idea_id, "title": title, "builds_on": []}

    def test_project_folder_and_identifiers_are_explicit(self) -> None:
        self.assertEqual(self.project, Path(self.temporary.name) / "projects" / "proj_test")
        with self.assertRaises(BoardError):
            project_dir_for_id("../other", self.temporary.name)
        with self.assertRaises(BoardError):
            board_append("relative/project", "session-1", "idea", self.idea("I1"))
        with self.assertRaises(BoardError):
            board_append(self.project, "../other", "idea", self.idea("I1"))
        with self.assertRaises(BoardError):
            board_append(self.project, "session-1", "unknown", {})
        with self.assertRaises(BoardError):
            board_append(self.project, "session-1", "outcome", self.outcome(
                "I1", state="maybe"))

    def test_outcome_is_verbatim_and_only_critic_closes_idea(self) -> None:
        idea_id = new_idea_id()
        board_append(self.project, "session-a", "idea", self.idea(idea_id))
        outcome = self.outcome(idea_id, state="resolved", notebook_append="## First check\n")
        event_id = board_append(self.project, "session-a", "outcome", outcome,
                                provenance={"delegation_id": outcome["delegation_id"],
                                            "child_frame_id": "frame-1"})
        ledger = self.project / "board" / "sessions" / "session-a.jsonl"
        entries = [json.loads(line) for line in ledger.read_text().splitlines()]
        self.assertEqual(entries[-1]["payload"], outcome)
        self.assertEqual(entries[-1]["event_id"], event_id)
        self.assertEqual(entries[-1]["provenance"],
                         {"delegation_id": outcome["delegation_id"],
                          "child_frame_id": "frame-1"})
        self.assertEqual(board_snapshot(self.project)["ideas"][0]["state"], "open")
        self.assertEqual(notebook_path(self.project, "session-a", idea_id).read_text(),
                         "## First check\n")
        board_append(self.project, "session-b", "promote", {
            "kind": "idea_state", "idea_id": idea_id, "state": "resolved",
            "critique_ref": "critique-1.md"})
        self.assertEqual(board_snapshot(self.project)["ideas"][0]["state"], "resolved")
        self.assertEqual(board_snapshot(self.project, "session-a")["ideas"][0]["state"], "open")
        self.assertEqual(board_snapshot(self.project, "session-b")["ideas"][0]["state"], "resolved")

    def test_soft_dismissal_requeues_but_cannot_close_lane(self) -> None:
        idea_id = new_idea_id()
        board_append(self.project, "session-a", "idea", self.idea(idea_id))
        board_append(self.project, "session-a", "outcome", self.outcome(
            idea_id, dismissals=[{"reason_class": "lacked_tools",
                                  "attempted": "Tried the available solver"}]))
        snapshot = board_snapshot(self.project)
        self.assertEqual(snapshot["requeue_idea_ids"], [idea_id])
        self.assertEqual(len(snapshot["soft_dismissals"]), 1)
        with self.assertRaises(BoardError):
            board_append(self.project, "session-a", "close_lane", {
                "lane_id": "lane-1", "reason_class": "lacked_tools",
                "critique_ref": "critique-1.md", "excluded_scope": "solver lane"})
        with self.assertRaises(BoardError):
            board_append(self.project, "session-a", "promote", {
                "kind": "idea_state", "idea_id": idea_id, "state": "obstructed",
                "reason_class": "lacked_tools", "critique_ref": "critique-1.md"})
        board_append(self.project, "session-a", "close_lane", {
            "lane_id": "lane-1", "reason_class": "demonstrated_obstruction",
            "critique_ref": "critique-1.md", "excluded_scope": "solver lane"})
        self.assertEqual(len(board_snapshot(self.project)["closed_lanes"]), 1)

    def test_derived_lemma_promotion_requires_independent_check(self) -> None:
        lemma = {"lemma_id": "L1", "source": "derived", "hypotheses": ["H"],
                 "applies_to": {"target": "T", "evidence": "construction definition"},
                 "known_failures": [], "restates": []}
        board_append(self.project, "session-a", "lemma_proposal", lemma)
        promotion = {"kind": "lemma", "lemma": lemma, "evidence": [
            {"kind": "derivation", "ref": "notebook.md#L1"}],
            "critique_ref": "critique-1.md", "knowledge_id": "K1-abc"}
        with self.assertRaises(BoardError):
            board_append(self.project, "session-a", "promote", promotion)
        promotion["evidence"].append({"kind": "independent-check", "ref": "review.md#L1"})
        board_append(self.project, "session-a", "promote", promotion)
        self.assertEqual(len(board_snapshot(self.project)["lemmas"]), 1)
        with self.assertRaises(BoardError):
            board_append(self.project, "session-a", "lemma_proposal", {
                **lemma, "lemma_id": "L2", "source": "literature"})

    def test_conflicting_lemma_proposals_are_not_hidden(self) -> None:
        lemma_id = new_lemma_id()
        base = {"lemma_id": lemma_id, "source": "derived", "hypotheses": [],
                "applies_to": {"target": "T", "evidence": "construction"},
                "known_failures": [], "restates": []}
        board_append(self.project, "session-a", "lemma_proposal", base)
        board_append(self.project, "session-b", "lemma_proposal",
                     {**base, "hypotheses": ["extra assumption"]})
        snapshot = board_snapshot(self.project)
        self.assertEqual(len(snapshot["lemma_proposals"]), 2)
        self.assertEqual(snapshot["lemma_proposal_conflicts"], [lemma_id])

    def test_open_idea_keeps_critique_reference_across_sessions(self) -> None:
        idea_id = new_idea_id()
        board_append(self.project, "session-a", "idea", self.idea(idea_id))
        board_append(self.project, "session-a", "critique", {
            "pass_id": "pass-1", "critique_ref": "artifact:critique-v1",
            "idea_ids": [idea_id], "summary": "Still open: test the cost of the transform"})
        snapshot = board_snapshot(self.project)
        self.assertEqual(len(snapshot["critiques"]), 1)
        self.assertEqual(snapshot["open_ideas"][0]["critique_refs"],
                         ["artifact:critique-v1"])

    def test_notebook_can_be_rebuilt_from_event_log(self) -> None:
        idea_id = new_idea_id()
        board_append(self.project, "session-a", "outcome", self.outcome(
            idea_id, notebook_append="First line\n"))
        board_append(self.project, "session-a", "outcome", self.outcome(
            idea_id, notebook_append="Second line\n"))
        notebook = notebook_path(self.project, "session-a", idea_id)
        self.assertEqual(notebook.read_text(), "First line\nSecond line\n")
        notebook.unlink()
        rebuild_notebook(self.project, "session-a", idea_id)
        self.assertEqual(notebook.read_text(), "First line\nSecond line\n")

    def test_split_child_enters_persistent_open_queue(self) -> None:
        parent, child = new_idea_id(), new_idea_id()
        board_append(self.project, "session-a", "idea", self.idea(parent))
        board_append(self.project, "session-b", "promote", {
            "kind": "idea_state", "idea_id": parent, "state": "split",
            "child_idea_ids": [child], "critique_ref": "critique-1.md"})
        snapshot = board_snapshot(self.project)
        self.assertEqual({item["idea_id"] for item in snapshot["open_ideas"]}, {child})
        self.assertEqual(snapshot["ready_open_ideas"], [])
        self.assertEqual(next(item for item in snapshot["ideas"]
                              if item["idea_id"] == child)["details"]["parent_idea_id"],
                         parent)
        board_append(self.project, "session-b", "idea", self.idea(child, "Define child"))
        self.assertEqual({item["idea_id"] for item in board_snapshot(self.project)["ready_open_ideas"]},
                         {child})

    def test_split_outcome_checks_child_definitions(self) -> None:
        parent, child = new_idea_id(), new_idea_id()
        valid = self.outcome(parent, state="split", child_idea_ids=[child],
                             child_ideas=[self.idea(child, "Check a quotient")])
        board_append(self.project, "session-a", "outcome", valid)
        with self.assertRaises(BoardError):
            board_append(self.project, "session-a", "outcome", self.outcome(
                parent, state="split", child_idea_ids=[child],
                child_ideas=[self.idea(new_idea_id())]))
        with self.assertRaises(BoardError):
            board_append(self.project, "session-a", "outcome", self.outcome(
                parent, state="split", child_idea_ids=[parent]))

    def test_outcome_provenance_and_required_fields(self) -> None:
        outcome = self.outcome("I1")
        with self.assertRaises(BoardError):
            board_append(self.project, "session-a", "outcome", outcome,
                         provenance={"delegation_id": "different",
                                     "child_frame_id": "frame-1"})
        with self.assertRaises(BoardError):
            board_append(self.project, "session-a", "outcome",
                         {key: value for key, value in outcome.items()
                          if key != "delegation_id"})
        with self.assertRaises(BoardError):
            board_append(self.project, "session-a", "outcome", self.outcome(
                "I1", dismissals=[{"reason_class": "lacked_tools"}]))
        with self.assertRaises(BoardError):
            board_append(self.project, "session-a", "idea",
                         {"idea_id": "I1", "title": "Missing base lemmas"})

    def test_duplicate_idea_id_is_detected_across_sessions(self) -> None:
        board_append(self.project, "session-a", "idea", self.idea("I1"))
        board_append(self.project, "session-b", "idea", self.idea("I1", "Another question"))
        with self.assertRaisesRegex(BoardError, "duplicate idea ID"):
            board_snapshot(self.project)

    def test_concurrent_processes_keep_every_event_and_uuid_unique(self) -> None:
        code = (
            "import sys\n"
            "sys.path.insert(0, sys.argv[1])\n"
            "from board import board_append, new_idea_id\n"
            "for _ in range(50):\n"
            "    board_append(sys.argv[2], 'shared-session', 'idea', "
            "{'idea_id': new_idea_id(), 'title': 'Concurrent idea', "
            "'builds_on': []})\n"
        )
        commands = [[sys.executable, "-c", code, str(BOARD_SCRIPT), str(self.project)]
                    for _ in range(8)]
        processes = [subprocess.Popen(command, stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE) for command in commands]
        for process in processes:
            stdout, stderr = process.communicate(timeout=30)
            self.assertEqual(process.returncode, 0, (stdout + stderr).decode())
        ledger = self.project / "board" / "sessions" / "shared-session.jsonl"
        events = [json.loads(line) for line in ledger.read_text().splitlines()]
        self.assertEqual(len(events), 400)
        self.assertEqual(len({event["event_id"] for event in events}), 400)
        self.assertEqual(len({event["payload"]["idea_id"] for event in events}), 400)
        self.assertEqual(len(board_snapshot(self.project)["open_ideas"]), 400)


if __name__ == "__main__":
    unittest.main()
