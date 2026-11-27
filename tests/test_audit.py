"""The pack's guard: the faults the 2026-11 audit found cannot return."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from audit_skills import (audit, load_terms, validate_host_notes, validate_links,
                          validate_route_budget, validate_skill_mentions, validate_terms)


def skill(root: Path, name: str, body: str = "", description: str | None = None) -> Path:
    path = root / "skills" / name / "SKILL.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    description = description or f"Use this demonstration skill when testing the audit of {name}."
    path.write_text(f"---\nname: {name}\ndescription: {description}\n---\n\n{body}\n")
    return path


class GuardTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "config").mkdir()
        shutil.copy(ROOT / "config/audit-terms.json", self.root / "config")
        (self.root / "config/skill-migrations.json").write_text('{"renames": [{"from": "old-name", "to": "demo"}]}')
        self.terms = load_terms(self.root)

    def test_repository_passes_its_own_audit(self):
        with tempfile.TemporaryDirectory() as out:
            result = subprocess.run(
                [sys.executable, str(ROOT / "tools/audit_skills.py"),
                 "--output", str(Path(out) / "inventory.json"),
                 "--registry-output", str(Path(out) / "registry.json")],
                capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            registry = json.loads((Path(out) / "registry.json").read_text())
            self.assertEqual(registry, json.loads((ROOT / "config/skill-registry.json").read_text()),
                             "config/skill-registry.json is stale; run tools/audit_skills.py")

    def test_retired_tool_names_are_rejected(self):
        for text in ("Use nist-mcp_search_csrc first.", "Call portal_list_servers.",
                     "e-print-mcp_eprint_fulltext(paper_id, query)"):
            with self.subTest(text=text):
                skill(self.root, "demo", text)
                self.assertTrue(validate_terms(self.root, self.terms))
        skill(self.root, "demo", "search_eprint_fulltext(paper_id, query) then eprint_fulltext(paper_id, start_page, page_count)")
        self.assertEqual(validate_terms(self.root, self.terms), [])

    def test_first_product_names_fields_and_paths_are_rejected(self):
        for text in ("Built for Claude Science.", "Pass child_frame_id.", "Set context_summary.",
                     "Read structured_output.", "Raises GrantMissing.", "Use edit_file.",
                     "Files under ~/crypto-workbench-files.", "In this workbench we",
                     "Ask the dedicated reviewer.", "## Optional CryptoSkills cross-references"):
            with self.subTest(text=text):
                skill(self.root, "demo", text)
                failures = validate_terms(self.root, self.terms)
                self.assertTrue(failures)
                self.assertIn("skills/demo/SKILL.md:", failures[0])

    def test_alias_reading_is_allowed_only_where_listed(self):
        board = self.root / "skills/crypto-workbench-knowledge/scripts/board.py"
        board.parent.mkdir(parents=True)
        board.write_text('provenance.get("child_frame_id")\n')
        self.assertEqual(validate_terms(self.root, self.terms), [])
        other = self.root / "skills/other/scripts/x.py"
        other.parent.mkdir(parents=True)
        other.write_text('child_frame_id = 1\n')
        self.assertEqual(len(validate_terms(self.root, self.terms)), 1)

    def test_unknown_backticked_skill_name_is_rejected(self):
        skill(self.root, "demo", "Use `demo`, `old-name` and `official-manual`.")
        self.assertEqual(validate_skill_mentions(self.root, {"demo"}, self.terms), [])
        skill(self.root, "demo", "Use `decryption-failure-correctness-and-reaction-analysis`.")
        self.assertEqual(len(validate_skill_mentions(self.root, {"demo"}, self.terms)), 1)

    def test_broken_link_and_anchor_are_rejected(self):
        skill(self.root, "demo", "## Real heading\n\nSee [here](#real-heading) and [other](../other/SKILL.md).")
        skill(self.root, "other", "## Section")
        (self.root / "README.md").write_text("[demo](skills/demo/SKILL.md#real-heading)\n")
        (self.root / "START_HERE.md").write_text("start\n")
        self.assertEqual(validate_links(self.root), [])
        skill(self.root, "demo", "See [gone](../missing/SKILL.md) and [x](../other/SKILL.md#nope).")
        failures = validate_links(self.root)
        # the missing skill, the missing anchor, and README's anchor now gone
        self.assertEqual(len(failures), 3)
        self.assertTrue(any("broken anchor" in item for item in failures))

    def test_name_and_description_limits(self):
        skill(self.root, "demo", description="x " * 151)
        _, errors, _ = audit(self.root / "skills")
        self.assertTrue(any("over 300" in error for error in errors))
        long_name = "a" * 65
        skill(self.root, long_name)
        _, errors, _ = audit(self.root / "skills")
        self.assertTrue(any("exceeds 64" in error for error in errors))

    def test_host_note_names_only_its_documented_tools(self):
        note = self.root / "skills/demo/reference/hosts/demo-host.md"
        note.parent.mkdir(parents=True)
        note.write_text("---\nhost: demo\ntools: [plan_create]\nterms: [CRYPTO_FILES]\n---\n\n"
                        "Use `plan_create` with `CRYPTO_FILES`.\n")
        self.assertEqual(validate_host_notes(self.root), [])
        note.write_text(note.read_text() + "Then `invented_tool`.\n")
        self.assertEqual(len(validate_host_notes(self.root)), 1)
        note.write_text("# no front matter, `plan_create`\n")
        self.assertIn("lacks a tools list", validate_host_notes(self.root)[0])

    def test_route_over_budget_is_rejected(self):
        skill(self.root, "demo", "x" * 500)
        budget = {"load_cap": 100000, "target_max": 100, "routes": [
            {"name": "demo route", "host": "atlas", "files": ["demo/SKILL.md"]}]}
        (self.root / "config/route-budget.json").write_text(json.dumps(budget))
        self.assertIn("over 100", validate_route_budget(self.root)[0])
        budget["target_max"] = 10000
        (self.root / "config/route-budget.json").write_text(json.dumps(budget))
        self.assertEqual(validate_route_budget(self.root), [])


if __name__ == "__main__":
    unittest.main()
