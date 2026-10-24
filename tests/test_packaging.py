"""Exercise release artifacts, source fidelity, and selection boundaries."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from package_skills import build_bundle, select_skills, skill_catalog
from audit_skills import validate_migrations, validate_portability
from import_skill_packs import rewrite_text


class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.output = Path(self.tmp.name) / 'bundle'

    def test_exact_resources_and_hashes_round_trip(self):
        # This skill has a real executable helper as well as instructions.
        manifest = build_bundle(ROOT, self.output, names=['crypto-verify-claim'])
        self.assertEqual(len(manifest['skills']), 1)
        skill = manifest['skills'][0]
        archive = self.output / skill['archive']
        self.assertEqual(hashlib.sha256(archive.read_bytes()).hexdigest(), skill['archive_sha256'])
        with zipfile.ZipFile(archive) as bundle:
            self.assertIn('crypto-verify-claim/scripts/reproduce.py', bundle.namelist())
            self.assertTrue(all(name.startswith('crypto-verify-claim/') for name in bundle.namelist()))
            for name in bundle.namelist():
                relative = name.removeprefix('crypto-verify-claim/')
                body = bundle.read(name)
                self.assertEqual(body, (ROOT / 'skills/crypto-verify-claim' / relative).read_bytes())
                self.assertEqual(hashlib.sha256(body).hexdigest(), skill['files'][relative])
        packet = (self.output / 'context.md').read_bytes()
        self.assertEqual(hashlib.sha256(packet).hexdigest(), manifest['context_sha256'])
        self.assertIn((ROOT / 'skills/crypto-verify-claim/SKILL.md').read_bytes(), packet)
        self.assertEqual(manifest, json.loads((self.output / 'manifest.json').read_text()))

    def test_deterministic_archives_and_packet(self):
        first = build_bundle(ROOT, self.output, names=['crypto-investigate', 'crypto-verify-claim'])
        second = build_bundle(ROOT, Path(self.tmp.name) / 'second', names=['crypto-verify-claim', 'crypto-investigate'])
        self.assertEqual(first, second)

    def test_existing_output_is_not_overwritten(self):
        self.output.mkdir()
        sentinel = self.output / 'keep.txt'
        sentinel.write_text('retained')
        with self.assertRaisesRegex(ValueError, 'already exists'):
            build_bundle(ROOT, self.output, names=['crypto-verify-claim'])
        self.assertEqual(sentinel.read_text(), 'retained')
        self.assertEqual(list(self.output.iterdir()), [sentinel])

    def test_unknown_or_traversal_selection_creates_nothing(self):
        for name in ['unknown-skill', '../README.md']:
            with self.subTest(name=name), self.assertRaisesRegex(ValueError, 'unknown skill'):
                build_bundle(ROOT, self.output, names=[name])
            self.assertFalse(self.output.exists())

    def test_symlinked_resource_is_rejected_before_output(self):
        fixture = Path(self.tmp.name) / 'source'
        (fixture / 'skills/demo').mkdir(parents=True)
        (fixture / 'config').mkdir()
        (fixture / 'config/imported-skills.json').write_text('{"skills": []}')
        (fixture / 'START_HERE.md').write_text('Start')
        (fixture / 'skills/demo/SKILL.md').write_text('---\nname: demo\ndescription: A test skill with a resource.\n---\n')
        external = Path(self.tmp.name) / 'external.txt'
        external.write_text('outside content')
        (fixture / 'skills/demo/resource.txt').symlink_to(external)
        with self.assertRaisesRegex(ValueError, 'symlinked resource'):
            build_bundle(fixture, self.output, names=['demo'])
        self.assertFalse(self.output.exists())

    def test_domain_profiles_include_core_and_requested_domain(self):
        catalog = skill_catalog(ROOT)
        starter = set(select_skills(catalog, 'starter', []))
        self.assertIn('crypto-investigate', starter)
        self.assertIn('formal-methods-router', starter)
        self.assertNotIn('crypto-workbench-knowledge', starter)
        for domain in ['symmetric', 'public-key', 'formal']:
            selected = set(select_skills(catalog, domain, []))
            self.assertTrue(starter <= selected)
            self.assertTrue({name for name, item in catalog.items() if item['domain'] == domain} <= selected)
            self.assertTrue(all(name in starter or catalog[name]['domain'] == domain for name in selected))
        self.assertEqual(set(select_skills(catalog, 'all', [])), set(catalog))


class SkillMigrationTests(unittest.TestCase):
    def test_pack_refresh_updates_explicit_references_but_preserves_prose(self):
        source = ("Use `investigate` with [environment](../../investigate/reference/environment.md), "
                  "`verify-claim`, and [costs](../derive-cost/SKILL.md). "
                  "Then investigate the claim.\n```sh\nmagma -b job.m\n```\n")
        result = rewrite_text(source, 'symmetric', 'example')
        self.assertIn('`crypto-investigate`', result)
        self.assertIn('../../crypto-investigate/reference/environment.md', result)
        self.assertIn('`crypto-verify-claim`', result)
        self.assertIn('../crypto-derive-cost/SKILL.md', result)
        self.assertIn('Then investigate the claim.', result)
        self.assertIn('magma -b job.m', result)

    def test_registry_and_rename_record_have_no_dangling_or_duplicate_ids(self):
        names = set(skill_catalog(ROOT))
        self.assertEqual(validate_migrations(ROOT / 'config/skill-migrations.json', names), [])

    def test_retired_name_cannot_be_reintroduced_as_an_alias(self):
        names = set(skill_catalog(ROOT)) | {'investigate'}
        failures = validate_migrations(ROOT / 'config/skill-migrations.json', names)
        self.assertIn('skill migration: retired name still installed investigate', failures)


class PortabilityAuditTests(unittest.TestCase):
    def test_private_api_regression_is_rejected_with_locator(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'demo/SKILL.md'
            path.parent.mkdir()
            path.write_text('Use host.delegate for all work.\n')
            failures = validate_portability(Path(tmp))
            self.assertEqual(len(failures), 1)
            self.assertIn('demo/SKILL.md:1:', failures[0])

    def test_portable_host_discussion_is_allowed(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'demo/SKILL.md'
            path.parent.mkdir()
            path.write_text('Use the actual tool inventory of the host.\n')
            self.assertEqual(validate_portability(Path(tmp)), [])


if __name__ == '__main__':
    unittest.main()
