---
name: workbench-knowledge
description: Read and extend project research notes, evidence, gaps, and lessons across cryptographic investigations. Use when prior work should be reused or a result should be retained. Python file helpers and an append-only research board are optional; without persistent storage, return a text handoff.
license: Apache-2.0
---

# Project research notes

Read relevant prior notes when they are accessible. Keep established results,
search gaps, process lessons, and open conjectures distinct. A retrieved note is
provenance; inspect whether its evidence covers the current claim and version.
A search gap is scoped to its queries, sources, and date, not proof of impossibility.

## Choose a record that the session can retain

With no execution or durable writable storage, use the conversation. Return a
handoff with the target and version, assumptions, inspected sources and locators,
findings and evidence, unchecked candidates, gaps, and next decisive work. State
that the user must retain or re-supply it; do not claim cross-session memory.

When Python on a POSIX-compatible filesystem with `fcntl` locking (for example,
macOS, Linux, or WSL) and suitable storage are available, the bundled helpers maintain
`knowledge.md`, `gaps.md`, and `lessons.md` under one project directory. The
optional board records in-flight ideas. Use the host's supported file interface
or a confirmed writable path; temporary analysis storage may not survive a
session. No home path or host-specific permission UI is guaranteed.

## Read it first

Resolve this skill's actual directory through the host's loader or file listing.
Set `CRYPTO_SKILLS` explicitly to its scripts directory; do not probe private
application paths. `CRYPTO_FILES` is an optional absolute storage parent. The
helper's local default is `~/crypto-workbench-files`; override it in a sandbox.
Choose a stable path-safe project ID once and retain it with the research record.

```python
import os, sys
from pathlib import Path
script_dir = Path(os.environ['CRYPTO_SKILLS']).expanduser().resolve()
sys.path.insert(0, str(script_dir))
from board import project_dir_for_id, board_snapshot
from knowledge import read_all, add_entry, add_entry_once, add_gap, add_lesson
project_dir = project_dir_for_id('your-stable-project-id')
print(read_all(project_dir=project_dir))
print(board_snapshot(project_dir))
```

`CRYPTO_FILES/projects/<project-id>/` is the project directory. Never mix unrelated
projects or create a fresh project ID on every continuation. If workers are used,
pass their project and session IDs and the absolute path only after confirming
that they share access; otherwise hand off the relevant content explicitly.

## Evidence and updates

```python
add_entry(statement, kind='measurement',
          evidence=[{'kind': 'computation', 'ref': '<script and output>',
                     'note': '<exact inputs, versions, and scope>'}],
          project_dir=project_dir)
add_gap(question, looked_in=['ePrint', 'official comments'],
        finding='<queries, date, exclusions, and result>', project_dir=project_dir)
add_lesson('<observed process issue, with environment and version>',
           project_dir=project_dir)
```

Each evidence item has `kind`, `ref`, and `note`. Supported kinds are `assertion`,
`derivation`, `independent-check`, `computation`, `paper`, `spec`, and `human`.
An assertion alone records a belief, not established knowledge. A new derivation
stays a candidate until a separate check covers the fixed argument. The helper
requires `independent-check` alongside `derivation` when promoting it into
`knowledge.md`; name the exact route and candidate. If independent checking is
unavailable, retain the derivation in the conversation or board as unchecked.

Use `add_entry_once(..., claim='<stable-claim-id>', project_dir=project_dir)` for
idempotent promotion. If it reuses an entry, inspect that entry for matching
statement, scope, and evidence. Record corrections by appending what they
supersede. Reuse prior checks only when their premises and versions still match.

## Append and confirm

Use the helpers rather than read-modify-write on the authoritative record.
They require POSIX `fcntl` locking and append bounded entries while preserving
concurrent cooperating writes on supported local filesystems. On unsupported
systems, use host documents or text notes rather than importing these helpers. Do not assume those semantics on remote document
stores or every network filesystem. For a host document interface, use its
supported revision and merge behavior, or one writer.

A failed write is not a saved record. `GrantMissing` identifies a failed knowledge
write; `BoardWriteError` means the ledger may be partially written, so inspect it
before retrying. `NotebookMaterializationError` means the board event was saved:
repair the filesystem issue and rebuild the notebook without duplicating the
outcome. If storage remains unavailable, return the unsaved record in chat.

For sustained research where a board is useful, read
[the optional research-board procedure](reference/research-board.md). It supports
sequential phases as well as authorized workers. The board is not a scheduler or
execution engine. Keep work within the requested scope and current session limits.

```sh
python3 skills/workbench-knowledge/scripts/knowledge.py --selftest
python3 skills/workbench-knowledge/scripts/board.py --selftest
```
