# What the offline checks establish

`score_routing_response.py` checks report format and expected names. Its legacy
`passed` field means only that those smoke checks (and supplied trace checks)
passed. It does not measure mathematical progress, correctness, novelty, coverage,
or whether cited evidence supports a conclusion. `research_progress` is always
`not_assessed`; compare actual mathematical outputs in a separate review.

`check_skill_probe.py` checks exact body-content adherence. A correct marker
does not by itself prove that a host invoked a skill.

Both tools accept `--trace` as the following **offline normalized JSON**, prepared
from the existing harness trace. No harness instrumentation or API change is
required. Preserve the original trace and map only observed successful skill-body
loads. The normalization must never infer a load from a response, a skill name in
a prompt, an available tool definition, or a failed call.

```json
{
  "schema_version": 1,
  "source_trace": "captured-run.jsonl",
  "events": [
    {
      "kind": "skill_load",
      "skill_id": "skill-load-probe",
      "status": "succeeded",
      "call_id": "original-call-id",
      "body_sha256": "REPLACE_WITH_64_LOWERCASE_HEX_DIGITS_FROM_THE_RETURNED_BODY"
    }
  ]
}
```

Hash the UTF-8 body actually returned, not the description or a local file that
was never loaded. This document records trace evidence; the checker does not
authenticate the original trace or prove that the loaded guidance was followed.
Missing trace evidence stays unassessed. Malformed or name-only traces fail when
supplied; failed calls cannot count as successful loads.

## Project/session research-board metrics

`python tools/trace_evidence.py --board-metrics normalized.json` reports one
recorded session in one project. `board_metrics(path)` returns the
same JSON object for Python callers. This is an **offline normalized event
contract**, not a host API and not proof that the original capture is
authentic. Preserve the original trace, host-call tapes, and board ledgers.

The top-level `project_id` and `session_id` are the project's ID and the session identifier actually recorded by the host or supplied by the researcher. `project_dir` is the absolute
`<CRYPTO_FILES>/projects/<project_id>` path. `capture_complete` has four
boolean channels: `board_reads`, `board_appends`, `delegations`, and
`delegation_returns`. Mark a channel `true` only after covering the entire
session. A missing or partial channel makes dependent metrics `null` and adds
their names to `unverified`; observed counts remain under `observed`. Do not
turn a failed search or inaccessible trace into a zero.

The following shortened example shows the event shapes. The root assigns a
unique `delegation_id` to **each child** before dispatch. A host `delegate`
call also has its own `host_call_id`; one batched host call can spawn several
children, each with a different `delegation_id` and `child_frame_id`. Events
are in observed execution order.

```json
{
  "schema_version": 1,
  "source_trace": "captured-run-with-host-call-tapes",
  "project_id": "proj_example",
  "session_id": "root-frame-id",
  "project_dir": "/absolute/crypto-workbench-files/projects/proj_example",
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
      "project_dir": "/absolute/crypto-workbench-files/projects/proj_example",
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
      "delegation_id": "assigned-child-1",
      "host_call_id": "host-call-7",
      "child_frame_id": "child-frame-id",
      "idea_id": "idea-a",
      "board_read_call_id": "read-cell-1:0",
      "expects_board_outcome": true,
      "context_summary": "Read /absolute/crypto-workbench-files/projects/proj_example/board."
    },
    {
      "kind": "delegation_return",
      "delegation_id": "assigned-child-1",
      "child_frame_id": "child-frame-id",
      "status": "completed",
      "structured_output": {
        "delegation_id": "assigned-child-1", "idea_id": "idea-a", "state": "open", "findings": [],
        "dismissals": [], "lemma_proposals": [], "notebook_append": ""
      }
    },
    {
      "kind": "board_append",
      "call_id": "append-cell-9:0",
      "event_id": "board-event-id",
      "session_id": "root-frame-id",
      "ledger_path": "/absolute/crypto-workbench-files/projects/proj_example/board/sessions/root-frame-id.jsonl",
      "event_type": "outcome",
      "payload": {
        "delegation_id": "assigned-child-1", "idea_id": "idea-a", "state": "open", "findings": [],
        "dismissals": [], "lemma_proposals": [], "notebook_append": ""
      },
      "capture_source": "delegation_return",
      "delegation_id": "assigned-child-1",
      "child_frame_id": "child-frame-id"
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
contains its `delegation_id` and `child_frame_id`, copy those to the normalized
event and set `capture_source: "delegation_return"`. If provenance cannot be
established, set `capture_source: "unknown"`; use `"manual"` only when the
trace explicitly shows a manual outcome. An unknown outcome origin makes the
negative return-to-append metric unverified.

Normalize delegation events only from observed requests and returns. Assign a
unique per-worker `delegation_id`, retain the host's worker ID as `child_frame_id`,
and record the actual task context in `context_summary`. Correlate returned and
persisted payloads by those IDs. Running descriptors are not terminal returns.
Do not invent capture completeness, a child ID, a board read, or a persisted
outcome from prose mentions. A host without worker traces cannot substantiate
these metrics; sequential work need not produce delegation events at all.

## Cross-environment trials

Use `portability-cases.json` for instruction access, absent browsing, absent
execution, partial catalogs, storage, and sequential research. Supply each prompt
and its resource constraints, withholding the review criteria from the model.
Record the actual model, host version, capabilities, resources supplied, and
output. Review whether the result used available evidence accurately and made
useful progress. These cases are manual acceptance criteria, not completed tests
of every assistant or evidence of scientific correctness.

The skill probe checks body-content adherence regardless of whether the body
was obtained natively, through a file read, or in supplied text. Record that
access route separately. For native-load claims, retain the host's actual load
event; a pasted marker or an assistant's statement cannot establish one. If
native tracing is unavailable, leave loading unassessed. Do not fabricate a
normalized trace to make the checker pass.

The routing scorer remains an offline **format smoke check** for complete-catalog
trials. It expects prescribed sections and names; it is not an acceptance gate
for a legitimate partial-catalog or text-only session. It cannot measure whether
a missing method was correctly treated or whether an argument is sound.

## Mathematical development and contribution cases

`mathematical-research-cases.json` contains fourteen manual evaluation cases with
supplied premises and review criteria. They cover routine parameter substitution,
important applications of known methods, invalidated hypotheses, reuse of
established mathematics, sustained block-matrix derivation, and conditional work.
They do not execute cryptanalytic attacks or change the harness.

For a behavioral trial, give the model the prompt and relevant skills, keeping
the review criteria separate until assessment. Inspect the actual reasoning,
source use, and output. Compare the same prompt and supplied context before and
after the skill change; record the model configuration and available resources.
Do not count a case as passed because expected words appeared. These cases have
not been exercised in a live assistant merely by being checked into the repository.


## Comparison protocol

Compare the original skills, the original skills plus the user's ranked-question
prompt, and the revised skills on the same supplied mathematical questions. Keep
model version, sampling settings, available tools, input context, and resource
limits matched. Use more than one run before attributing a difference to wording.
These are evaluations of the existing host, not changes to its execution API.

Review the actual products and, where available, traces. Distinguish source
interpretation from paper verification, and count repeated checking as justified
only when it addresses a changed dependency or the assigned verification task.
Assess mathematical progress by the inference produced, its correctness and
scope, and the unresolved obligations it exposes. Report time or resource use
by activity only when the trace supports that measurement. Do not optimize for
claimed novelty, number of proposed questions, or the absence of negative results.

The added cases cover a false paper claim, use of an established theorem,
post-selection inference, a zero-event confidence limit, a nine-question proposal,
continuation from a partial derivation, and scoped negative results. Their
presence and reference answers do not constitute a live model evaluation.

The elementary-corollary case checks whether a newly named rank inequality is
recognized as a direct consequence of supplied standard facts. The expected
assessment concerns the displayed reasoning, not another literature survey.

Use `reconstructed-ranked-research-prompt.json` for the middle condition. Its
wording is a reconstructed representative prompt authorized by the user, not an
exact historical prompt. The original-skills baseline is commit `098013c`, the
parent of this PR's first commit. Record the full resolved commit IDs and skill
body hashes for every executed condition; do not use an evolving branch name as
the only version identifier.

Use fresh, isolated conversations with identical supplied context, tool access,
model versions, effort, and resource limits. Keep review criteria and prior
condition outputs out of generation context. Verify which skill bodies actually
loaded; merely attaching revised files does not establish that the host used
them. Counterbalance condition order and run at least two repetitions per case
and condition before describing a repeated pattern. Report run-level outcomes,
disagreements, and execution failures; two repetitions alone do not establish
statistical significance or general improvement.

`delegated-cryptanalysis-cases.json` adds three supplemental handoffs covering
an important routine finding undervalued by its author, an unnoticed connection
between accurately reviewed reports, and premature closure after a correct but
narrow examination. A dedicated correctness reviewer has already checked the
supplied findings. Assess what research judgment the orchestrator adds: omitted
implications, meaningful connections, and justified treatment of open questions.
Repeating the supplied correctness checks does not satisfy this objective.
These bounded fixtures do not measure open-ended cryptanalytic creativity.

`delegated-mathematics-cases.json` supplies three further cases with fixed
synthetic subagent handoffs. Review whether the main agent catches a false proof,
continues past an unjustified dismissal, and corrects inflated novelty. These
and the broader cryptanalysis cases isolate the main agent's response to supplied
work; they do not measure real delegation or differences between model
capabilities. A live delegation trial
must also record the primary and child model/effort settings actually used,
subtask prompts, returned artifacts, and what the primary agent checked or added.
Do not infer those settings from UI labels or role names.
