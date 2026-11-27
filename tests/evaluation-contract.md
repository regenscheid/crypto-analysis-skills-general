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

## Research-board metrics

The research board belongs to `crypto-workbench-knowledge`, the fallback record
for hosts that keep none of their own. Its offline metrics have their own
contract, [board-metrics-contract.md](board-metrics-contract.md), and tool,
`tools/board_metrics.py`. The methods are evaluated without a board: none of the
checks above requires one.

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
narrow examination. An independent correctness reviewer has already checked the
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
