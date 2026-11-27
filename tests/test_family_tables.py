"""The routers' family tables are generated from the registry and cannot drift."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from family_tables import ROUTERS, outputs, registry, similar_pairs


class FamilyTableTests(unittest.TestCase):
    def test_generated_files_match_the_registry(self):
        stale = [str(path.relative_to(ROOT)) for path, text in outputs(ROOT).items()
                 if not path.exists() or path.read_text(encoding="utf-8") != text]
        self.assertEqual(stale, [], "run python3 tools/family_tables.py")

    def test_every_specialist_skill_is_in_its_router_table(self):
        skills = registry(ROOT)
        for domain, router in ROUTERS.items():
            table = (ROOT / "skills" / router / "references/skill-family.md").read_text()
            for skill in skills:
                if skill["domain"] == domain and skill["skill_id"] != router:
                    self.assertIn(f"`{skill['skill_id']}`", table)

    def test_similar_symmetric_and_public_key_names_are_told_apart(self):
        pairs = similar_pairs(registry(ROOT))
        self.assertEqual(len(pairs), 5)
        for router in ("symmetric-cryptanalysis-orchestrator", "public-key-cryptanalysis-orchestrator"):
            text = (ROOT / "skills" / router / "SKILL.md").read_text()
            for symmetric, public_key in pairs:
                self.assertIn(f"`{symmetric}` (symmetric) / `{public_key}` (public-key)", text)


if __name__ == "__main__":
    unittest.main()
