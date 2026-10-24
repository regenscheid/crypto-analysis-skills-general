#!/usr/bin/env python3
"""Build deterministic per-skill ZIPs and a text packet without installing anything."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import zipfile

from audit_skills import parse_frontmatter

ROOT = Path(__file__).resolve().parents[1]
PROFILES = ('starter', 'symmetric', 'public-key', 'formal', 'all')
ENTRY_POINTS = {
    'symmetric-cryptanalysis-orchestrator',
    'public-key-cryptanalysis-orchestrator',
    'formal-methods-router',
    'empirical-statistical-and-heuristic-claim-separation',
}
TEXT_SUFFIXES = {'.md', '.txt', '.json', '.yaml', '.yml', '.toml'}


def skill_catalog(root: Path) -> dict[str, dict]:
    imported = json.loads((root / 'config/imported-skills.json').read_text(encoding='utf-8'))
    domains = {item['installed_name']: item['domain'] for item in imported['skills']}
    catalog = {}
    for path in sorted((root / 'skills').glob('*/SKILL.md')):
        fields = parse_frontmatter(path)
        name = fields.get('name')
        if name != path.parent.name or not fields.get('description'):
            raise ValueError(f'invalid skill manifest: {path}')
        catalog[name] = {'description': fields['description'],
                         'domain': domains.get(name, 'core')}
    return catalog


def select_skills(catalog: dict, profile: str | None, names: list[str]) -> list[str]:
    if names:
        unknown = sorted(set(names) - catalog.keys())
        if unknown:
            raise ValueError('unknown skill IDs: ' + ', '.join(unknown))
        return sorted(set(names))
    profile = profile or 'starter'
    starter = {name for name, item in catalog.items()
               if item['domain'] == 'core' and name not in {'crypto-magma', 'crypto-workbench-knowledge'}}
    starter |= ENTRY_POINTS & catalog.keys()
    if profile == 'all':
        return sorted(catalog)
    if profile == 'starter':
        return sorted(starter)
    return sorted(starter | {name for name, item in catalog.items()
                             if item['domain'] == profile})


def source_files(root: Path, name: str) -> dict[str, bytes]:
    skill_dir = root / 'skills' / name
    if skill_dir.is_symlink():
        raise ValueError(f'symlinked skill directory: {name}')
    files = {}
    for path in sorted(skill_dir.rglob('*')):
        relative = path.relative_to(skill_dir)
        if '__pycache__' in relative.parts or path.name == '.DS_Store' or path.suffix in {'.pyc', '.pyo'}:
            continue
        if path.is_symlink():
            raise ValueError(f'symlinked resource: {name}/{relative.as_posix()}')
        if path.is_file():
            files[relative.as_posix()] = path.read_bytes()
    if 'SKILL.md' not in files:
        raise ValueError(f'missing SKILL.md: {name}')
    return files


def build_bundle(root: Path, output: Path, profile: str | None = None,
                 names: list[str] | None = None) -> dict:
    catalog = skill_catalog(root)
    selected = select_skills(catalog, profile, names or [])
    # Validate and snapshot input before creating any output. Reject symlinks so
    # a resource cannot accidentally include unrelated local files.
    sources = {name: source_files(root, name) for name in selected}
    starter_text = (root / 'START_HERE.md').read_text(encoding='utf-8')
    if not selected:
        raise ValueError('selection contains no skills')
    if output.exists():
        raise ValueError(f'output already exists; choose a new directory: {output}')
    output.mkdir(parents=True)
    (output / 'skills').mkdir()
    packet = [
        '# Cryptographic analysis context packet\n',
        'Use only the supplied methods relevant to the question. This packet is '
        'instruction text, not evidence of native skill loading or tool execution. '
        'Resources retain their original paths below. References to other skills '
        'do not imply that those skills are present. Scripts and binary assets are '
        'in the corresponding ZIPs and have not been executed.\n',
        'Included skill IDs: ' + ', '.join(selected) + '\n',
        '## File: START_HERE.md\n\n' + starter_text,
    ]
    manifest = {'schema_version': 1, 'repository': 'crypto-analysis-skills-general',
                'selection': profile or ('explicit' if names else 'starter'),
                'dependency_policy': 'Only selected skills are included; cross-skill references are optional.',
                'skills': []}
    for name in selected:
        archive_path = output / 'skills' / (name + '.zip')
        files = sources[name]
        with zipfile.ZipFile(archive_path, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
            for relative, body in files.items():
                entry = zipfile.ZipInfo(name + '/' + relative, date_time=(1980, 1, 1, 0, 0, 0))
                entry.compress_type = zipfile.ZIP_DEFLATED
                entry.create_system = 3
                entry.external_attr = 0o100644 << 16
                archive.writestr(entry, body)
                if Path(relative).suffix in TEXT_SUFFIXES:
                    packet.append(f'## File: skills/{name}/{relative}\n\n' + body.decode('utf-8'))
        manifest['skills'].append({
            'skill_id': name, **catalog[name],
            'archive': 'skills/' + archive_path.name,
            'archive_sha256': hashlib.sha256(archive_path.read_bytes()).hexdigest(),
            'files': {relative: hashlib.sha256(body).hexdigest() for relative, body in files.items()},
        })
    context = '\n\n'.join(packet).rstrip() + '\n'
    (output / 'context.md').write_text(context, encoding='utf-8', newline='\n')
    manifest['context_sha256'] = hashlib.sha256(context.encode('utf-8')).hexdigest()
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n', encoding='utf-8', newline='\n')
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument('--profile', choices=PROFILES)
    selection.add_argument('--skill', action='append', default=[], help='canonical ID; repeat for several skills')
    parser.add_argument('--output', type=Path, required=True, help='new output directory; existing directories are never overwritten')
    args = parser.parse_args()
    try:
        manifest = build_bundle(ROOT, args.output, args.profile, args.skill)
    except (ValueError, OSError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    print(f"packaged {len(manifest['skills'])} skills in {args.output.resolve()}")
    print(f"text packet: {(args.output / 'context.md').stat().st_size:,} bytes; select fewer skills if needed")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
