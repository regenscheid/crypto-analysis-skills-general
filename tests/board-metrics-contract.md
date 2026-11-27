# Research-board metrics (crypto-workbench-knowledge)

`python3 tools/board_metrics.py normalized.json` reports one
recorded session in one project. `board_metrics(path)` returns the
same JSON object for Python callers. This is an **offline normalized event
contract**, not a host API and not proof that the original capture is
authentic. Preserve the original trace, the host's record of worker calls, and the board ledgers.

The top-level `project_id` and `session_id` are the project's ID and the session identifier actually recorded by the host or supplied by the researcher. `project_dir` is the absolute
`<CRYPTO_FILES>/projects/<project_id>` path. Traces normalized with the older
field names `child_frame_id`, `context_summary` and `structured_output` are read
as `worker_id`, `worker_context` and `structured_return`. `capture_complete` has four
boolean channels: `board_reads`, `board_appends`, `delegations`, and
`delegation_returns`. Mark a channel `true` only after covering the entire
session. A missing or partial channel makes dependent metrics `null` and adds
their names to `unverified`; observed counts remain under `observed`. Do not
turn a failed search or inaccessible trace into a zero.

The following shortened example shows the event shapes. The main agent assigns a
unique `delegation_id` to **each worker** before dispatch. A host's delegation
call also has its own `host_call_id`; one batched host call can start several
workers, each with a different `delegation_id` and `worker_id`. Events
are in observed execution order.

```json
{
  "schema_version": 1,
  "source_trace": "captured-run-with-worker-calls",
  "project_id": "proj_example",
  "session_id": "session-1",
  "project_dir": "/absolute/records/projects/proj_example",
  "capture_complete": {
    "board_reads": true,
    "board_appends": true,
    "delegations": true,
    "delegation_returns": true
  },
  "events": [
    {
      "kind": "board_read",
      "call_id": "read-cell-1:0",
      "status": "succeeded",
      "project_dir": "/absolute/records/projects/proj_example",
      "scope": "project",
      "snapshot": {
        "open_idea_ids": ["idea-a"],
        "requeue_idea_ids": ["idea-a"],
        "soft_dismissals": [
          {"event_id": "prior-dismissal-id", "dismissal_index": 0, "idea_id": "idea-a", "reason_class": "lacked_tools"}
        ],
        "promoted_lemma_ids": ["lemma-prior"]
      }
    },
    {
      "kind": "delegation",
      "delegation_id": "assigned-worker-1",
      "host_call_id": "host-call-7",
      "worker_id": "worker-1",
      "idea_id": "idea-a",
      "board_read_call_id": "read-cell-1:0",
      "expects_board_outcome": true,
      "worker_context": "Read /absolute/records/projects/proj_example/board."
    },
    {
      "kind": "delegation_return",
      "delegation_id": "assigned-worker-1",
      "worker_id": "worker-1",
      "status": "completed",
      "structured_return": {
        "delegation_id": "assigned-worker-1", "idea_id": "idea-a", "state": "open", "findings": [],
        "dismissals": [], "lemma_proposals": [], "notebook_append": ""
      }
    },
    {
      "kind": "board_append",
      "call_id": "append-cell-9:0",
      "event_id": "board-event-id",
      "session_id": "session-1",
      "ledger_path": "/absolute/records/projects/proj_example/board/sessions/session-1.jsonl",
      "event_type": "outcome",
      "payload": {
        "delegation_id": "assigned-worker-1", "idea_id": "idea-a", "state": "open", "findings": [],
        "dismissals": [], "lemma_proposals": [], "notebook_append": ""
      },
      "capture_source": "delegation_return",
      "delegation_id": "assigned-worker-1",
      "worker_id": "worker-1"
    }
  ]
}
```

Normalize a `board_read` only from an observed completed `board_snapshot`
call and its returned snapshot. Record the absolute `project_dir` argument and
`scope: "project"` when `session_id=None` was passed; a session-filtered read
uses `scope: "session"` and cannot prove project-wide carry or re-derivation.
A failed read has `status: "failed"` and no snapshot. Copy the snapshot's
`open_ideas[*].idea_id`, `requeue_idea_ids`,
`soft_dismissals[*].event_id`, `soft_dismissals[*].idea_id`,
`soft_dismissals[*].dismissal.reason_class`, and `lemmas[*].lemma.lemma_id` into
the normalized fields shown above. Deduplicate `promoted_lemma_ids` and omit
IDs listed in the board's `promoted_lemma_conflicts`; a conflicting ID is not
one settled lemma. Add `dismissal_index` as the zero-based
position in the source outcome's `dismissals` array; use `0` for a standalone
`dismissal` event. Resolve each snapshot `event_id` against the project
ledgers to recover this index. The `(event_id, dismissal_index)` pair is
unique even when one outcome produced several soft dismissals. A name in a
prompt or report is not a read.

Normalize `board_append` from an actual line in
`<project_dir>/board/sessions/<session_id>.jsonl`: `event_id`, `session_id`,
`type` as `event_type`, and the verbatim `payload`. Add the absolute
`ledger_path` and a trace `call_id` for the successful append call (use a cell
ID plus ordinal when one cell appends more than once). The helper can store
`provenance` **outside** the verbatim payload for outcomes. When the ledger
contains its `delegation_id` and `worker_id`, copy those to the normalized
event and set `capture_source: "delegation_return"`. If provenance cannot be
established, set `capture_source: "unknown"`; use `"manual"` only when the
trace explicitly shows a manual outcome. An unknown outcome origin makes the
negative return-to-append metric unverified.

Normalize delegation events only from observed requests and returns. Assign a
unique per-worker `delegation_id`, retain the host's identifier for the worker as `worker_id`,
and record the actual task context in `worker_context`. Correlate returned and
persisted payloads by those IDs. Running descriptors are not terminal returns.
Do not invent capture completeness, a worker ID, a board read, or a persisted
outcome from prose mentions. A host without worker traces cannot substantiate
these metrics; sequential work need not produce delegation events at all.
