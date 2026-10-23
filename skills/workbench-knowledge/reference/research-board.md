# Project research board

Use this optional procedure when Python and persistent writable files are
available for sustained DISCOVER work that develops and revisits
cryptanalytic ideas. A single proposal or bounded mathematical question does
not require a board loop. The board is a research record, not a plan, job
queue, or replacement for host artifacts.

## Resolve the shared project and session

`CRYPTO_FILES` names an absolute storage parent (default
`~/crypto-workbench-files`). Give each project one stable, path-safe ID and
use `projects/<project-id>/` beneath that parent. Use the host's project ID
when it exposes one. Otherwise create an opaque ID once, save that ID and
absolute project path in a discoverable project artifact, and reuse them in
later sessions. Never use a title alone or a delegated agent's current
working directory as the identity.

Use the host's root session ID for the session ledger. If the host does not
expose one, generate an opaque ID once per root session and record it in that
session's first artifact. The root agent resolves both IDs, ensures the shared
directory is writable, and passes the absolute project directory, session
ID, and relevant notebook paths to delegates in their task and
a supported context field. Confirm shared access before passing paths. A child
must not invent another project directory. Without workers, perform phases
sequentially; without persistent Python storage, return an equivalent text record.

```python
from board import (project_dir_for_id, board_snapshot, board_append,
                   new_idea_id, new_lemma_id)
from knowledge import read_all, add_entry_once, entry_id_for_claim

project_dir = project_dir_for_id(project_id)
print(read_all(project_dir=project_dir))
snapshot = board_snapshot(project_dir)  # all sessions, not only this session
idea_id = new_idea_id()
board_append(project_dir, session_id, "idea", {
    "idea_id": idea_id,
    "title": "Check the stated invariant",
    "builds_on": [],  # IDs of confirmed lemmas, if any
    "state": "open",
})
```

The authoritative files are
`<project_dir>/board/sessions/<session-id>.jsonl`. Each event is appended
as one JSON line by `board_append`; do not edit or rewrite a ledger. The
helper gives every event a UUID and accepts a maximum 1 MiB event. Notebook
files under `board/notebooks/<session-id>/<idea-id>.md` are generated from
logged `notebook_append` text and can be rebuilt. `knowledge.md`,
`gaps.md`, and `lessons.md` are shared across all sessions of this project.
Use `board_snapshot(project_dir, session_id=<id>)` only when examining one
session's branch of work; triage starts from the project-wide snapshot.

## Event meanings

| Event | Required research content |
|---|---|
| `idea` | Globally unique `idea_id`, nonempty `title`, `builds_on` array of confirmed lemma IDs, initially `open` |
| `outcome` | The delegated structured return exactly as received; its state is a proposal |
| `finding` | `idea_id`, `dominated_by` SOTA row ID or null, `domination_justification` when null, and `sota_delta` |
| `dismissal` | `idea_id`, `reason_class`, and nonempty `attempted` description |
| `lemma_proposal` | Project-unique `lemma_id`, `source`, `hypotheses`, `applies_to`, `known_failures`, `restates`, and `locator` for literature |
| `critique` | `pass_id`, saved `critique_ref`, nonempty `summary`, and distinct `idea_ids` reviewed, including ideas left open |
| `promote` | Critic decision with `kind`, full evidence, and `critique_ref` |
| `close_lane` | `lane_id`, `reason_class=demonstrated_obstruction`, `excluded_scope`, and `critique_ref` |
| `sota_row` | `row_id`, `catalog_record_id`, and `published_ref`; never an agent result |

`dismissal.reason_class` is one of `demonstrated_obstruction`,
`lacked_idea`, `lacked_time`, `lacked_tools`, or `lacked_context`.
Only a critic-accepted demonstrated obstruction may close a lane.
The other four are soft dismissals and remain eligible for requeueing.
An idea stays `open` until a critic promotes it to `resolved` or
`obstructed`, or `split` with child idea IDs. A child's `outcome.state`
alone never changes the board state. Split children enter the open queue.
Before assigning a split child to a delegated frame, append its full `idea`
event with `title` and `builds_on`; the open placeholder made by the split
does not contain a research question. Use `ready_open_ideas` from the snapshot for
dispatch only after that definition exists.

A finding compares its claim to the published bar represented by `sota_row`
events. If no published row dominates it, set `dominated_by` to null and
justify that conclusion. State the actual `sota_delta`; a rediscovered or
weaker result remains recorded without being promoted as a new attack.
For an intermediate mathematical observation that is not yet an attack, say
so in `sota_delta` and name the missing link to an attack. Do not invent a
cost or claim dominance merely to fill the field.
Derived lemma promotion must carry an independent-check evidence item that
names the exact proposal checked. Literature lemmas need an exact source
locator and explicit hypotheses. Record a derived lemma's `restates`
links when it matches known literature.
Generate new lemma IDs with `new_lemma_id()` or an equivalent UUID. The
project snapshot retains every proposal, including multiple proposals with
the same ID, and reports `lemma_proposal_conflicts` and
`promoted_lemma_conflicts`. Resolve conflicting statements or hypotheses
before treating an ID as confirmed knowledge; a reused ID does not mean two
claims agree.

Use these exact nested field names in an `outcome` return:

- Each `findings[]` item has `dominated_by` (a SOTA row ID or `null`) and
  nonempty `sota_delta`; when `dominated_by` is `null`, include nonempty
  `domination_justification`.
- Each `dismissals[]` item has `reason_class` and a nonempty `attempted`
  description. The five allowed reason classes are listed above.
- Each `lemma_proposals[]` item has `lemma_id`, `source` (`derived` or
  `literature`), `hypotheses` (array), `applies_to` with nonempty `target` and
  `evidence`, `known_failures` (array), and `restates` (array). A literature
  proposal also has a nonempty exact `locator`.

The helper supplies the enclosing outcome's `idea_id` to nested findings and
dismissals; if one of those items repeats `idea_id`, it must match. Keep the
arrays empty when there is no item. Record a notebook fragment as the exact
`notebook_append` string; it may be empty.

## Capture child work mechanically

For each delegated frame, include `idea_id`, a unique delegation ID, the
absolute project directory, the relevant notebook path and prior critique
references, the frozen target, and the expected return fields in the task.
Put a concise version in the supported context field; do not assume the child
inherits the conversation. Use structured output when supported, or request the
same fields as JSON text. Do not invent a host schema API.
The child returns `delegation_id`, `idea_id`, `state`, `findings[]`, `dismissals[]`,
`lemma_proposals[]`, and `notebook_append`, plus child idea IDs when split.
The root appends the returned `structured_output` as one `outcome`
**without editing, filtering, or rewriting its fields**. Pass
`provenance={"delegation_id": ..., "child_frame_id": ...}` to
`board_append`; it lives in the event envelope, leaving the child payload
unchanged. The provenance `delegation_id` must match the returned
`delegation_id`. Keep any host `deviations` with the critique/trace evidence;
never silently turn a missing structured return into empty arrays.

Call `board_append` on every collected return before curating it. A
`BoardError` means validation failed before the append; preserve the original
return and mark it unrecorded until repaired. A `BoardWriteError` means the
ledger write failed or may have been partial: inspect the ledger for that
delegation ID and exact payload before retrying. A
`NotebookMaterializationError` means the outcome **was** appended; fix the
filesystem issue and call `rebuild_notebook(project_dir, session_id, idea_id)`
without appending it again. A separate critic pass interprets the raw
returns and emits promotion or lane-closure events. The root writes
`critique-<pass>.md` as a host artifact, appends one `critique` event linking
that artifact to every idea reviewed in the pass, and uses its reference in
any promotion or lane-closure events. This keeps the critic's objections
visible for ideas that remain open. Do not let a child declare its own
obstruction accepted.

```python
board_append(project_dir, session_id, "critique", {
    "pass_id": pass_id,
    "critique_ref": critique_ref,
    "summary": "What was accepted, contested, or left open in this pass",
    "idea_ids": reviewed_idea_ids,
})
```

For a critic-approved derived lemma, inspect
`entry_id_for_claim(lemma_id, project_dir=project_dir)` for an existing entry,
then call `add_entry_once(statement, kind="derived result",
evidence=[derivation, independent_check], claim=lemma_id,
project_dir=project_dir)` and retain the returned knowledge ID. The helper
locks the claim lookup and append across cooperating sessions; when it reuses
an ID, verify the existing entry states the same result and evidence before
promotion. The evidence entries need `kind`, `ref`, and `note`;
the independent check names the exact fixed proposal. Append the
`promote` event with `kind="lemma"`, the full lemma object, both evidence
items, `knowledge_id`, and `critique_ref`. The board promotion records the
critic decision; it does not itself write `knowledge.md`. For a literature
lemma, use its exact locator and hypotheses with the appropriate evidence
before recording promotion. Do not put an unchecked derivation in
`knowledge.md`.

## Triage, ideate, execute, critique

At the start of every pass:

1. Read the three durable project files and the project-wide
   `board_snapshot`. Establish relevant published `sota_row` records with
   exact source, scope, and cost model before judging an improvement; a row
   must never be an agent result.
2. Carry forward every open idea with all its notebook paths and critique
   references. Read relevant prior critiques before dispatch, and include
   those references in the task and `context_summary`. Requeue every soft
   dismissal; lack of time, tools, context, or an idea is not a proof of
   obstruction.
3. Generate new ideas only where that record shows a gap. Supply closed
   lanes as exclusions and name the confirmed lemmas each new idea builds
   on. There is no fixed idea count; the queue persists across sessions.
4. Define every split child with an `idea` event, then execute one focused
   frame per ready open idea. Give it the notebook path in `context_summary`
   and the actual task. Append each return mechanically.
5. Run a batch critic across the pass. Cross-check proposed closures,
   detect conflicting lemma IDs, lemmas implied by other lemmas or already in
   the literature,
   assign terminal idea states, promote checked lemmas, and save the critique.
   Append a `critique` event linking that artifact to every reviewed idea,
   even when its state remains open.
6. Continue within the requested scope and current session limits, or until the
   user stops. Return the next unresolved ideas in the handoff. Preserve the board
   when stopping; a session ending does not itself resolve an idea.

One or two open-brief inventor frames may join a pass. Give them confirmed
lemmas, published SOTA rows, and closed lanes. Ask for an object or invariant
not yet tracked, excluding closed-lane families as their primary lens. They
must state why an object fails before switching. They do not need the entire
board, because their task is deliberately broader than a narrow idea frame.

Keep the user's target fixed. Calling it the “most-studied target” is not an
obstruction. Retarget only with user approval. A proposed stopping reason
must name its reason class and the exact evidence supporting it.
