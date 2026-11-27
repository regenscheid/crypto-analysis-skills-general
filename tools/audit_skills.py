#!/usr/bin/env python3
"""Audit installed Agent Skills and emit a deterministic inventory."""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import sys
from collections import Counter
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FIELD_PATTERN = re.compile(r"^(name|description):\s*(.+?)\s*$")
NAME_MAX = 64
DESCRIPTION_MAX = 300
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


def _link_targets(text: str) -> list[str]:
    """Relative Markdown link targets, with any anchor, outside fenced code."""
    text = re.sub(r"(?ms)^```.*?^```", "", text)
    targets = []
    for target in MARKDOWN_LINK_PATTERN.findall(text):
        target = target.strip()
        if not target or target.startswith(("/", "http://", "https://", "mailto:")):
            continue
        if " " in target and not target.startswith("<"):
            continue
        targets.append(target.strip("<>"))
    return targets


def relative_links(path: Path | None = None, *, text: str | None = None) -> list[str]:
    """Relative link paths (anchors dropped) in a Markdown file or text."""
    if text is None:
        text = path.read_text(encoding="utf-8")
    links = []
    for target in _link_targets(text):
        target = target.split("#", 1)[0]
        if target:
            links.append(target)
    return links


def heading_anchors(text: str) -> set[str]:
    """GitHub-style anchors of a Markdown file's headings."""
    anchors = set()
    text = re.sub(r"(?ms)^```.*?^```", "", text)
    for heading in re.findall(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", text):
        slug = re.sub(r"[^\w\- ]", "", heading.strip().lower().replace("`", ""))
        anchors.add(slug.replace(" ", "-"))
    return anchors


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
        elif len(name) > NAME_MAX:
            errors.append(f"{directory}: name exceeds {NAME_MAX} characters")
        if name != directory:
            errors.append(f"{directory}: frontmatter name is {name!r}")
        if not description:
            errors.append(f"{directory}: missing description")
        elif len(description) > DESCRIPTION_MAX:
            errors.append(f"{directory}: description is {len(description)} characters, over {DESCRIPTION_MAX}")
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
                    errors.append(f"{directory}: missing relative link {rendered}")

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


def load_terms(root: Path = REPOSITORY_ROOT) -> dict:
    return json.loads((root / "config" / "audit-terms.json").read_text(encoding="utf-8"))


def _scanned_files(root: Path, terms: dict) -> list[Path]:
    files = set()
    for pattern in terms["scan"]:
        files.update(path for path in root.glob(pattern) if path.is_file())
    excluded = set(terms.get("exclude", []))
    return sorted(path for path in files
                  if path.relative_to(root).as_posix() not in excluded
                  and "__pycache__" not in path.parts
                  and path.suffix in {".md", ".py", ".json", ".jsonl", ".yaml", ".yml", ".txt"})


def validate_terms(root: Path, terms: dict) -> list[str]:
    """Retired tool names and the first product's names, fields and paths."""
    rules = [(entry["pattern"], entry["label"])
             for key in ("retired_tool_names", "first_product") for entry in terms[key]]
    compiled = [(re.compile(pattern), pattern, label) for pattern, label in rules]
    allowed = terms.get("allowed_in", {})
    failures = []
    for path in _scanned_files(root, terms):
        relative = path.relative_to(root).as_posix()
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for number, line in enumerate(lines, 1):
            for regex, pattern, label in compiled:
                if regex.search(line) and not any(
                        fnmatch.fnmatch(relative, allowed_path)
                        for allowed_path in allowed.get(pattern, [])):
                    failures.append(f"{relative}:{number}: {label}")
    return failures


def validate_skill_mentions(root: Path, skill_names: set[str], terms: dict) -> list[str]:
    """A backticked hyphenated name must be a registered skill or a listed non-skill term."""
    migrations = json.loads((root / "config" / "skill-migrations.json").read_text(encoding="utf-8"))
    known = skill_names | {item["from"] for item in migrations["renames"]} | set(terms["not_skill_names"])
    files = sorted((root / "skills").rglob("*.md")) + [root / "README.md", root / "START_HERE.md"]
    failures = []
    for path in files:
        if not path.is_file():
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for token in re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", line):
                if token not in known:
                    failures.append(f"{path.relative_to(root).as_posix()}:{number}: "
                                    f"`{token}` is not a registered skill or a listed term")
    return failures


def validate_links(root: Path) -> list[str]:
    """Every relative link (and #anchor) in the pack's Markdown resolves."""
    files = sorted((root / "skills").rglob("*.md")) + sorted((root / "tests").glob("*.md")) + [
        root / "README.md", root / "START_HERE.md"]
    failures = []
    for path in files:
        if not path.is_file():
            continue
        for target in _link_targets(path.read_text(encoding="utf-8")):
            link, _, anchor = target.partition("#")
            destination = (path.parent / link) if link else path
            where = f"{path.relative_to(root).as_posix()} -> {target}"
            if not destination.exists():
                failures.append(f"broken link {where}")
            elif anchor and destination.suffix == ".md" and anchor not in heading_anchors(
                    destination.read_text(encoding="utf-8")):
                failures.append(f"broken anchor {where}")
    return failures


def _front_matter_lists(text: str) -> dict[str, list[str]]:
    """The inline lists (key: [a, b]) of a Markdown file's front matter."""
    if not text.startswith("---\n"):
        return {}
    block = text[4:].split("\n---", 1)[0]
    lists = {}
    for key, value in re.findall(r"(?m)^([a-z_]+):\s*\[(.*)\]\s*$", block):
        lists[key] = [item.strip() for item in value.split(",") if item.strip()]
    return lists


def validate_host_notes(root: Path) -> list[str]:
    """A host note names only tools in its own documented list (front matter `tools`)."""
    failures = []
    for path in sorted((root / "skills").glob("*/reference/hosts/*.md")):
        text = path.read_text(encoding="utf-8")
        lists = _front_matter_lists(text)
        if "tools" not in lists:
            failures.append(f"{path.relative_to(root).as_posix()}: front matter lacks a tools list")
            continue
        allowed = set(lists["tools"]) | set(lists.get("terms", []))
        body = text.split("\n---", 1)[1] if text.startswith("---\n") else text
        for number, line in enumerate(body.splitlines(), 1):
            for token in re.findall(r"`([A-Za-z_][A-Za-z0-9_]*)`", line):
                if token not in allowed:
                    failures.append(f"{path.relative_to(root).as_posix()}: body line {number}: "
                                    f"`{token}` is not in the note's documented tools")
    return failures


def route_sizes(root: Path) -> list[dict]:
    budget = json.loads((root / "config" / "route-budget.json").read_text(encoding="utf-8"))
    sizes = []
    for route in budget["routes"]:
        size = sum(len((root / "skills" / name).read_text(encoding="utf-8")) for name in route["files"])
        sizes.append({"name": route["name"], "host": route["host"], "characters": size})
    return sizes


def validate_route_budget(root: Path) -> list[str]:
    budget = json.loads((root / "config" / "route-budget.json").read_text(encoding="utf-8"))
    failures = []
    for route in budget["routes"]:
        missing = [name for name in route["files"] if not (root / "skills" / name).is_file()]
        if missing:
            failures.append(f"route {route['name']!r}: missing files {missing}")
    if failures:
        return failures
    return [f"route {item['name']!r} loads {item['characters']:,} characters, "
            f"over {budget['target_max']:,}"
            for item in route_sizes(root) if item["characters"] > budget["target_max"]]


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
    root = args.skills_root.resolve().parent
    if (root / "config" / "audit-terms.json").is_file():
        terms = load_terms(root)
        guard_errors = (validate_terms(root, terms)
                        + validate_skill_mentions(root, skill_names, terms)
                        + validate_links(root)
                        + validate_host_notes(root)
                        + validate_route_budget(root))
        errors.extend(guard_errors)
        report["guard_errors"] = len(guard_errors)
        report["route_characters"] = route_sizes(root)
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
