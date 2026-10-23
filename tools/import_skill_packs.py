#!/usr/bin/env python3
"""Import the staged CryptoSkills packs into the repository.

The staging directory is intentionally not part of the repository.  This script
copies only self-contained skill directories, gives globally colliding skills a
domain-qualified name, rewrites skill cross-references to installed names, and
records the result in a deterministic manifest.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STAGING_ROOT = REPOSITORY_ROOT / ".skill-packs"
DEFAULT_SKILLS_ROOT = REPOSITORY_ROOT / "skills"
DEFAULT_MANIFEST = REPOSITORY_ROOT / "config" / "imported-skills.json"


@dataclass(frozen=True)
class Pack:
    domain: str
    source: Path


PACKS = (
    Pack(
        "symmetric",
        Path("symmetric/symmetric-cryptanalysis-skills/skills"),
    ),
    Pack(
        "public-key",
        Path("public key/public-key-cryptanalysis-skills/skills"),
    ),
    Pack(
        "formal",
        Path("theoremprovers/cryptoskills-formal-methods/skills"),
    ),
)


SHARED_NAMES = (
    "attack-complexity-and-success-auditor",
    "attack-hypothesis-generator-and-triage",
    "attack-transfer-and-adaptation",
    "evidence-synthesis-and-research-backlog",
    "literature-attack-extractor",
    "reproduction-and-falsification-planner",
)


RENAMES = {
    (domain, name): f"{domain}-{name}"
    for domain in ("symmetric", "public-key")
    for name in SHARED_NAMES
}


TEXT_SUFFIXES = {".json", ".jsonl", ".md", ".txt", ".yaml", ".yml"}
NAMESPACED_SKILL = re.compile(
    r"(?<![a-z0-9-])(symmetric|public-key|formal):([a-z][a-z0-9-]*)"
)


def installed_name(domain: str, source_name: str) -> str:
    return RENAMES.get((domain, source_name), source_name)


def tree_hash(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        digest.update(path.relative_to(root).as_posix().encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def rewrite_text(text: str, domain: str, source_name: str) -> str:
    for shared_name in SHARED_NAMES:
        text = re.sub(
            rf"(?<![a-z0-9-]){re.escape(shared_name)}(?![a-z0-9-])",
            installed_name(domain, shared_name),
            text,
        )

    def replace_namespaced(match: re.Match[str]) -> str:
        reference_domain, reference_name = match.groups()
        return installed_name(reference_domain, reference_name)

    return NAMESPACED_SKILL.sub(replace_namespaced, text)


def rewrite_tree(root: Path, domain: str, source_name: str) -> None:
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        original = path.read_text(encoding="utf-8")
        rewritten = rewrite_text(original, domain, source_name)
        if rewritten != original:
            path.write_text(rewritten, encoding="utf-8")


def discover(staging_root: Path) -> list[tuple[Pack, Path]]:
    discovered: list[tuple[Pack, Path]] = []
    for pack in PACKS:
        skills_root = staging_root / pack.source
        if not skills_root.is_dir():
            raise FileNotFoundError(f"missing staged pack: {skills_root}")
        for skill_dir in sorted(skills_root.iterdir()):
            if skill_dir.is_dir() and (skill_dir / "SKILL.md").is_file():
                discovered.append((pack, skill_dir))
    return discovered


def import_packs(
    staging_root: Path,
    skills_root: Path,
    manifest_path: Path,
) -> int:
    records: list[dict[str, str]] = []
    destinations: set[str] = set()

    for pack, source in discover(staging_root):
        source_name = source.name
        destination_name = installed_name(pack.domain, source_name)
        destination = skills_root / destination_name

        if destination_name in destinations:
            raise RuntimeError(f"duplicate installed name: {destination_name}")
        destinations.add(destination_name)
        if destination.exists():
            raise FileExistsError(
                f"refusing to overwrite existing skill: {destination}"
            )

        source_hash = tree_hash(source)
        shutil.copytree(source, destination)
        rewrite_tree(destination, pack.domain, source_name)
        records.append(
            {
                "domain": pack.domain,
                "source_name": source_name,
                "installed_name": destination_name,
                "source_sha256": source_hash,
                "installed_sha256": tree_hash(destination),
            }
        )

    manifest = {
        "schema_version": 1,
        "source": ".agents (local staging; not committed)",
        "skill_count": len(records),
        "collision_policy": "qualify the six shared workflow names by domain",
        "skills": records,
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"imported {len(records)} skills into {skills_root}")
    print(f"wrote {manifest_path}")
    return 0


def check_import(skills_root: Path, manifest_path: Path) -> int:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    failures: list[str] = []
    for record in manifest["skills"]:
        destination = skills_root / record["installed_name"]
        if not destination.is_dir():
            failures.append(f"missing: {record['installed_name']}")
            continue
        actual = tree_hash(destination)
        if actual != record["installed_sha256"]:
            failures.append(
                f"changed: {record['installed_name']} "
                f"({actual} != {record['installed_sha256']})"
            )
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"verified {manifest['skill_count']} imported skills")
    return 0


def accept_installed_changes(skills_root: Path, manifest_path: Path) -> int:
    """Record reviewed local changes without altering source provenance hashes."""
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    failures: list[str] = []
    updates: list[tuple[dict[str, str], str]] = []
    for record in manifest["skills"]:
        destination = skills_root / record["installed_name"]
        if not destination.is_dir():
            failures.append(f"missing: {record['installed_name']}")
            continue
        actual = tree_hash(destination)
        if actual != record["installed_sha256"]:
            updates.append((record, actual))
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1

    for record, actual in updates:
        record["installed_sha256"] = actual
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"recorded reviewed changes to {len(updates)} imported skills")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--staging-root", type=Path, default=DEFAULT_STAGING_ROOT)
    parser.add_argument("--skills-root", type=Path, default=DEFAULT_SKILLS_ROOT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--check",
        action="store_true",
        help="verify installed trees against an existing import manifest",
    )
    mode.add_argument(
        "--accept-installed-changes",
        action="store_true",
        help="record reviewed installed-tree hashes while preserving source hashes",
    )
    args = parser.parse_args()
    if args.check:
        return check_import(args.skills_root, args.manifest)
    if args.accept_installed_changes:
        return accept_installed_changes(args.skills_root, args.manifest)
    return import_packs(args.staging_root, args.skills_root, args.manifest)


if __name__ == "__main__":
    raise SystemExit(main())
