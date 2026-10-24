#!/usr/bin/env python3
"""Audit installed Agent Skills and emit a deterministic inventory."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FIELD_PATTERN = re.compile(r"^(name|description):\s*(.+?)\s*$")
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^]]*]\(([^)]+)\)")


def unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        if value[0] == '"':
            return json.loads(value)
        return value[1:-1].replace("''", "'")
    return value


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening frontmatter delimiter")
    try:
        end = next(index for index in range(1, len(lines)) if lines[index].strip() == "---")
    except StopIteration as error:
        raise ValueError("missing closing frontmatter delimiter") from error
    fields: dict[str, str] = {}
    for line in lines[1:end]:
        match = FIELD_PATTERN.match(line)
        if match:
            fields[match.group(1)] = unquote(match.group(2))
    return fields


def relative_links(path: Path) -> list[str]:
    links = []
    for target in MARKDOWN_LINK_PATTERN.findall(path.read_text(encoding="utf-8")):
        target = target.strip().split("#", 1)[0]
        if not target or target.startswith(("#", "/", "http://", "https://", "mailto:")):
            continue
        if " " in target and not target.startswith("<"):
            continue
        links.append(target.strip("<>"))
    return links


def audit(skills_root: Path) -> tuple[dict[str, object], list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    records: list[dict[str, object]] = []

    for path in sorted(skills_root.glob("*/SKILL.md")):
        directory = path.parent.name
        line_count = len(path.read_text(encoding="utf-8").splitlines())
        try:
            frontmatter = parse_frontmatter(path)
        except ValueError as error:
            errors.append(f"{directory}: {error}")
            continue

        name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")
        if not name:
            errors.append(f"{directory}: missing name")
        elif not NAME_PATTERN.fullmatch(name):
            errors.append(f"{directory}: invalid name {name!r}")
        elif len(name) > 64:
            errors.append(f"{directory}: name exceeds 64 characters")
        if name != directory:
            errors.append(f"{directory}: frontmatter name is {name!r}")
        if not description:
            errors.append(f"{directory}: missing description")
        elif len(description.split()) < 8:
            warnings.append(f"{directory}: description may under-trigger ({len(description.split())} words)")
        elif len(description.split()) > 100:
            warnings.append(f"{directory}: description is long ({len(description.split())} words)")
        if line_count > 500:
            warnings.append(f"{directory}: SKILL.md is {line_count} lines; prefer progressive disclosure")

        missing_links = []
        for markdown in path.parent.rglob("*.md"):
            for link in relative_links(markdown):
                if not (markdown.parent / link).exists():
                    rendered = f"{markdown.relative_to(path.parent)} -> {link}"
                    missing_links.append(rendered)
                    warnings.append(f"{directory}: missing relative link {rendered}")

        records.append(
            {
                "name": name,
                "description": description,
                "description_words": len(description.split()),
                "lines": line_count,
                "missing_relative_links": missing_links,
            }
        )

    counts = Counter(record["name"] for record in records)
    for name, count in sorted(counts.items()):
        if count > 1:
            errors.append(f"duplicate skill name {name!r}: {count} copies")

    report: dict[str, object] = {
        "schema_version": 1,
        "skill_count": len(records),
        "description_words": sum(int(record["description_words"]) for record in records),
        "skill_body_lines": sum(int(record["lines"]) for record in records),
        "warnings": len(warnings),
        "errors": len(errors),
        "skills": records,
    }
    return report, errors, warnings


def validate_routing_cases(path: Path, skill_names: set[str]) -> list[str]:
    failures: list[str] = []
    cases = json.loads(path.read_text(encoding="utf-8"))
    for case in cases["cases"]:
        for name in case["expected_skills"]:
            if name not in skill_names:
                failures.append(f"routing case {case['id']}: unknown skill {name}")
    return failures


def validate_migrations(path: Path, skill_names: set[str]) -> list[str]:
    """A renamed ID must resolve to one current skill without a retired alias."""
    migrations = json.loads(path.read_text(encoding="utf-8"))
    failures = []
    previous_ids = set()
    current_ids = set()
    for rename in migrations["renames"]:
        previous, current = rename["from"], rename["to"]
        if previous in previous_ids or current in current_ids:
            failures.append(f"skill migration: duplicate mapping {previous} -> {current}")
        previous_ids.add(previous)
        current_ids.add(current)
        if current not in skill_names:
            failures.append(f"skill migration: unknown destination {current}")
        if previous in skill_names:
            failures.append(f"skill migration: retired name still installed {previous}")
    return failures


def validate_portability(skills_root: Path) -> list[str]:
    """Reject reintroduction of private deployment APIs in distributed resources."""
    patterns = {
        "private host SDK": re.compile(r"\bhost\.(?:delegate|collect|artifacts|artifact_path|artifact_marker|lineage|submit_output|skills|mcp|send_message|children|stop_child|capabilities)\b"),
        "private workflow API": re.compile(r"\b(?:generate_plan|update_step_status|save_artifacts|compute_submit|compute_result|compute_close|request_host_access)\b"),
        "private installation path": re.compile(r"\.(?:cscience|claude-science)/"),
    }
    failures = []
    for path in sorted(skills_root.rglob("*")):
        if not path.is_file() or path.suffix not in {".md", ".py", ".yaml", ".json"}:
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for label, pattern in patterns.items():
                if pattern.search(line):
                    failures.append(f"{path.relative_to(skills_root)}:{number}: {label}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skills-root", type=Path, default=REPOSITORY_ROOT / "skills")
    parser.add_argument("--output", type=Path, default=REPOSITORY_ROOT / "reports" / "skill-inventory.json")
    parser.add_argument("--registry-output", type=Path, default=REPOSITORY_ROOT / "config" / "skill-registry.json")
    parser.add_argument("--routing-cases", type=Path, default=REPOSITORY_ROOT / "tests" / "routing-cases.json")
    parser.add_argument("--import-manifest", type=Path, default=REPOSITORY_ROOT / "config" / "imported-skills.json")
    parser.add_argument("--skill-migrations", type=Path, default=REPOSITORY_ROOT / "config" / "skill-migrations.json")
    args = parser.parse_args()

    report, errors, warnings = audit(args.skills_root)
    imported = json.loads(args.import_manifest.read_text(encoding="utf-8"))
    domains = {
        record["installed_name"]: record["domain"]
        for record in imported["skills"]
    }
    for record in report["skills"]:
        record["domain"] = domains.get(str(record["name"]), "core")
    report["skills_by_domain"] = dict(
        sorted(Counter(str(record["domain"]) for record in report["skills"]).items())
    )
    skill_names = {str(record["name"]) for record in report["skills"]}
    errors.extend(validate_routing_cases(args.routing_cases, skill_names))
    errors.extend(validate_migrations(args.skill_migrations, skill_names))
    portability_errors = validate_portability(args.skills_root)
    errors.extend(portability_errors)
    report["portability_errors"] = len(portability_errors)
    report["errors"] = len(errors)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    registry = {
        "schema_version": 1,
        "id_contract": "skill_id is exactly the Agent Skill name from SKILL.md frontmatter",
        "skill_count": len(report["skills"]),
        "skills": [
            {
                "skill_id": record["name"],
                "domain": record["domain"],
            }
            for record in report["skills"]
        ],
    }
    args.registry_output.parent.mkdir(parents=True, exist_ok=True)
    args.registry_output.write_text(
        json.dumps(registry, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print(
        f"audited {report['skill_count']} skills: "
        f"{len(errors)} errors, {len(warnings)} warnings"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
