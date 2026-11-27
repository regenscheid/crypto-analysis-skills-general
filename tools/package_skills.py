#!/usr/bin/env python3
"""Build deterministic skill bundles without installing anything.

Without --host: one ZIP per selected skill (one top-level skill folder each),
a text packet `context.md`, and a manifest. With --host, a layout that host
accepts for a whole-pack install:

  atlas        an archive for the platform's `skills import --archive`
  claude-code  a plugin marketplace (`.claude-plugin/marketplace.json`) with one
               plugin whose `skills/` holds the selected skills
  codex        `.agents/skills/<name>/` to copy into a repository or home

Host layouts add every skill that a selected skill links to with `../`, so its
links resolve; the per-skill ZIPs cannot, so the packet carries the linked files
and the manifest names them.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import sys
import tarfile
import zipfile

from audit_skills import parse_frontmatter, relative_links

ROOT = Path(__file__).resolve().parents[1]
PROFILES = ('starter', 'symmetric', 'public-key', 'formal', 'all')
HOSTS = ('atlas', 'claude-code', 'codex')
ENTRY_POINTS = {
    'symmetric-cryptanalysis-orchestrator',
    'public-key-cryptanalysis-orchestrator',
    'formal-methods-router',
    'empirical-statistical-and-heuristic-claim-separation',
}
# Not in the recommended set: a licensed tool's skill, added on need.
STARTER_EXCLUDED = {'crypto-magma'}
# The fallback record; the Atlas platform keeps its own (its ledger).
RECORD_SKILL = 'crypto-workbench-knowledge'
TEXT_SUFFIXES = {'.md', '.txt', '.json', '.yaml', '.yml', '.toml'}
PACK_NAME = 'crypto-analysis-skills-general'
PLUGIN_NAME = 'crypto-analysis-skills'
EPOCH = (1980, 1, 1, 0, 0, 0)


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


def select_skills(catalog: dict, profile: str | None, names: list[str],
                  host: str | None = None) -> list[str]:
    if names:
        unknown = sorted(set(names) - catalog.keys())
        if unknown:
            raise ValueError('unknown skill IDs: ' + ', '.join(unknown))
        return sorted(set(names))
    profile = profile or 'starter'
    if profile == 'all':
        return sorted(catalog)
    starter = {name for name, item in catalog.items()
               if item['domain'] == 'core' and name not in STARTER_EXCLUDED}
    starter |= ENTRY_POINTS & catalog.keys()
    if host == 'atlas':
        starter.discard(RECORD_SKILL)
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


def outside_links(name: str, files: dict[str, bytes]) -> list[str]:
    """Pack paths (skills/<other>/...) that this skill's Markdown links to."""
    found = set()
    for relative, body in files.items():
        if not relative.endswith('.md'):
            continue
        base = PurePosixPath('skills', name, relative).parent
        for link in relative_links(text=body.decode('utf-8')):
            parts = []
            for part in (base / link).parts:
                if part == '..':
                    if parts:
                        parts.pop()
                elif part != '.':
                    parts.append(part)
            target = PurePosixPath(*parts) if parts else None
            if target and len(target.parts) >= 3 and target.parts[0] == 'skills' and target.parts[1] != name:
                found.add(target.as_posix())
    return sorted(found)


def link_closure(root: Path, selected: list[str], catalog: dict) -> tuple[list[str], list[str]]:
    """Selected skills plus every skill they link to, transitively."""
    chosen, queue, added = set(selected), list(selected), []
    while queue:
        name = queue.pop()
        for target in outside_links(name, source_files(root, name)):
            other = target.split('/')[1]
            if other in catalog and other not in chosen:
                chosen.add(other)
                added.append(other)
                queue.append(other)
    return sorted(chosen), sorted(added)


def _zip_entry(name: str) -> zipfile.ZipInfo:
    entry = zipfile.ZipInfo(name, date_time=EPOCH)
    entry.compress_type = zipfile.ZIP_DEFLATED
    entry.create_system = 3
    entry.external_attr = 0o100644 << 16
    return entry


def _write_tree(base: Path, name: str, files: dict[str, bytes]) -> None:
    for relative, body in files.items():
        path = base / name / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(body)


def _tar_bytes(sources: dict[str, dict[str, bytes]]) -> bytes:
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode='w', format=tarfile.PAX_FORMAT) as archive:
        for name in sorted(sources):
            for relative, body in sorted(sources[name].items()):
                info = tarfile.TarInfo(f'{PACK_NAME}/skills/{name}/{relative}')
                info.size = len(body)
                info.mode = 0o755 if body.startswith(b'#!') else 0o644
                info.mtime = 0
                info.uname = info.gname = ''
                archive.addfile(info, io.BytesIO(body))
    import gzip
    out = io.BytesIO()
    with gzip.GzipFile(fileobj=out, mode='wb', mtime=0, filename='') as compressed:
        compressed.write(buffer.getvalue())
    return out.getvalue()


def build_bundle(root: Path, output: Path, profile: str | None = None,
                 names: list[str] | None = None, host: str | None = None) -> dict:
    if host is not None and host not in HOSTS:
        raise ValueError(f'unknown host: {host}')
    catalog = skill_catalog(root)
    selected = select_skills(catalog, profile, names or [], host)
    if not selected:
        raise ValueError('selection contains no skills')
    added: list[str] = []
    if host is not None:
        selected, added = link_closure(root, selected, catalog)
    # Validate and snapshot input before creating any output. Reject symlinks so
    # a resource cannot accidentally include unrelated local files.
    sources = {name: source_files(root, name) for name in selected}
    if output.exists():
        raise ValueError(f'output already exists; choose a new directory: {output}')
    manifest = {'schema_version': 2, 'repository': PACK_NAME,
                'selection': profile or ('explicit' if names else 'starter'),
                'host': host,
                'skills': []}
    output.mkdir(parents=True)
    if host is None:
        manifest['dependency_policy'] = (
            'Only selected skills are archived; files they link to in other skills '
            'are listed per skill and carried in context.md.')
        _per_skill_zips(root, output, selected, sources, catalog, manifest, profile, names)
    else:
        manifest['dependency_policy'] = (
            'Whole-pack layout: every skill a selected skill links to is included '
            'so relative links resolve.')
        manifest['added_for_links'] = added
        for name in selected:
            manifest['skills'].append({
                'skill_id': name, **catalog[name],
                'files': {relative: hashlib.sha256(body).hexdigest()
                          for relative, body in sources[name].items()},
            })
        if host == 'atlas':
            archive = output / f'{PACK_NAME}.tar.gz'
            archive.write_bytes(_tar_bytes(sources))
            manifest['archive'] = archive.name
            manifest['archive_sha256'] = hashlib.sha256(archive.read_bytes()).hexdigest()
            manifest['install'] = (f'sandbox-science-harness skills import --state-dir STATE '
                                   f'--name crypto --archive {archive.name}')
        elif host == 'claude-code':
            plugin = output / 'plugins' / PLUGIN_NAME
            for name in selected:
                _write_tree(plugin / 'skills', name, sources[name])
            (plugin / '.claude-plugin').mkdir(parents=True)
            (plugin / '.claude-plugin' / 'plugin.json').write_text(json.dumps({
                'name': PLUGIN_NAME,
                'description': 'Cryptanalysis and cryptographic formal-methods skills.',
            }, indent=2, sort_keys=True) + '\n', encoding='utf-8')
            (output / '.claude-plugin').mkdir()
            (output / '.claude-plugin' / 'marketplace.json').write_text(json.dumps({
                'name': PACK_NAME,
                'owner': {'name': PACK_NAME + ' maintainers'},
                'plugins': [{'name': PLUGIN_NAME, 'source': f'./plugins/{PLUGIN_NAME}',
                             'description': 'Cryptanalysis and cryptographic formal-methods skills.'}],
            }, indent=2, sort_keys=True) + '\n', encoding='utf-8')
            manifest['install'] = (f'/plugin marketplace add {output}  then  '
                                   f'/plugin install {PLUGIN_NAME}@{PACK_NAME}; or copy '
                                   f'plugins/{PLUGIN_NAME}/skills/* to .claude/skills/')
        elif host == 'codex':
            for name in selected:
                _write_tree(output / '.agents' / 'skills', name, sources[name])
            manifest['install'] = ('copy .agents/skills/* into <repository>/.agents/skills/ '
                                   'or ~/.agents/skills/')
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n',
                                          encoding='utf-8', newline='\n')
    return manifest


def _per_skill_zips(root, output, selected, sources, catalog, manifest, profile, names):
    (output / 'skills').mkdir()
    starter_text = (root / 'START_HERE.md').read_text(encoding='utf-8')
    packet = [
        '# Cryptographic analysis context packet\n',
        'Use only the supplied methods relevant to the question. This packet is '
        'instruction text, not evidence of native skill loading or tool execution. '
        'Resources retain their original paths below. References to other skills '
        'do not imply that those skills are present; files the selected skills link '
        'to are included at the end under their original paths. Scripts and binary '
        'assets are in the corresponding ZIPs and have not been executed.\n',
        'Included skill IDs: ' + ', '.join(selected) + '\n',
        '## File: START_HERE.md\n\n' + starter_text,
    ]
    included = set()
    linked: set[str] = set()
    for name in selected:
        archive_path = output / 'skills' / (name + '.zip')
        files = sources[name]
        with zipfile.ZipFile(archive_path, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
            for relative, body in files.items():
                archive.writestr(_zip_entry(name + '/' + relative), body)
                if Path(relative).suffix in TEXT_SUFFIXES:
                    packet.append(f'## File: skills/{name}/{relative}\n\n' + body.decode('utf-8'))
                    included.add(f'skills/{name}/{relative}')
        links = outside_links(name, files)
        linked.update(links)
        manifest['skills'].append({
            'skill_id': name, **catalog[name],
            'archive': 'skills/' + archive_path.name,
            'archive_sha256': hashlib.sha256(archive_path.read_bytes()).hexdigest(),
            'files': {relative: hashlib.sha256(body).hexdigest() for relative, body in files.items()},
            'links_outside_skill': links,
        })
    extra = sorted(path for path in linked - included if (root / path).is_file())
    if extra:
        packet.append('## Files linked from the selected skills\n\nThese belong to other '
                      'skills and are included so the links can be followed.')
        for path in extra:
            packet.append(f'## File: {path}\n\n' + (root / path).read_text(encoding='utf-8'))
    manifest['linked_files_in_context'] = extra
    context = '\n\n'.join(packet).rstrip() + '\n'
    (output / 'context.md').write_text(context, encoding='utf-8', newline='\n')
    manifest['context_sha256'] = hashlib.sha256(context.encode('utf-8')).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument('--profile', choices=PROFILES)
    selection.add_argument('--skill', action='append', default=[], help='canonical ID; repeat for several skills')
    parser.add_argument('--host', choices=HOSTS, help='write a whole-pack layout for this host')
    parser.add_argument('--output', type=Path, required=True, help='new output directory; existing directories are never overwritten')
    args = parser.parse_args()
    try:
        manifest = build_bundle(ROOT, args.output, args.profile, args.skill, args.host)
    except (ValueError, OSError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    print(f"packaged {len(manifest['skills'])} skills in {args.output.resolve()}")
    if args.host is None:
        print(f"text packet: {(args.output / 'context.md').stat().st_size:,} bytes; select fewer skills if needed")
    else:
        print(f"install: {manifest['install']}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
