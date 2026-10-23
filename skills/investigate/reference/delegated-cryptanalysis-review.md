# Orchestrator research judgment after delegation

Apply this reference when independent workers are available and authorized.
Without them, use the same synthesis questions across sequential work and label
self-checks accurately. The optional board requires persistent Python storage.

Delegation supplies research inputs; it does not outsource the main agent's
research judgment. The main agent must assess what delegated cryptanalysis
missed, stopped short of, or undervalued. This applies across research proposals,
source work, modeling, computations, mathematical development, and assessments.
It matters especially when the orchestrator has a more capable model or broader
context than its subagents. Do not assume those capabilities from role names.

A dedicated reviewer can check whether submitted work is correct. A favorable
review does not establish that the right questions were asked, important
possibilities were considered, or the significance of the findings was understood.
The orchestrator's primary contribution here is intellectual synthesis and
judgment about depth, omissions, and significance.

## Look beyond the submitted answers

Read the substantive work and its limits, then form your own view of how it
addresses the user's research question. Do not let the subagent's framing,
familiar technique list, or stopping point define the boundaries of that view.
Use the broader investigation context to assess:

- **Omissions:** Which material questions in the assignment were left unexamined,
  or answered only through a narrower special case?
- **Premature dismissal:** Was a direction set aside because of a demonstrated
  obstruction, or merely because the subagent lacked time, context, tools, or a
  useful idea? Failure of one approach does not settle the wider question.
- **Connections:** Do separate findings bear on the same assumption, expose a
  tension, or jointly change an interpretation that neither subagent recognized?
  State the connecting inference; shared terminology alone is not a connection.
- **Significance:** Does a modest or routine finding change a standards-relevant
  assumption, parameter assessment, or understanding of a construction? Lack of
  a novel method is not a reason to omit an important implication.
- **Depth:** Did the work resolve the requested question, advance its unresolved
  reasoning, or stop at a summary or outline that leaves the substantive work undone?

These are judgments about the work, not a checklist to fill with invented gaps.
The union of subagent outputs is not evidence of exhaustive creative coverage.
When a material omission or implication is identified, explain it concretely
and incorporate it into the synthesis or a focused continuation within the
assignment. A request to the same subagent to “think harder” does not substitute
for the orchestrator supplying its own reasoning about what was missed and why
it matters. Report when that assessment remains incomplete.

## Use the reviewer without repeating its job

Use the dedicated reviewer's findings and compatible checked inputs. Reopen a
correctness question for a specific gap, changed dependency, conflicting evidence,
or an explicit verification assignment, under [paper use](paper-use-and-verification.md).
Do not repeat every baseline calculation or proof as the default response to a
research-depth concern.

New inferences introduced during synthesis still need checking proportionate to
the claim. Distinguish the submitted result, reviewer verdict, and the
orchestrator's additional interpretation or argument. Preserve conditional
premises, model and version boundaries, and unexamined scope. A main-agent pass
is not automatically independent verification; use
[evidence interpretation](evidence-interpretation.md) to describe its actual support.

## Preserve significance without inflating originality

Apply [contribution assessment](contribution-assessment.md) to both the subagent's
finding and the orchestrator's synthesis. Identify the known ingredients, their
application or deduction, and any substantive additional step. An important
consequence can remain a routine application or elementary corollary. Conversely,
a subagent's “routine” label does not establish that the finding is unimportant.
Recognizing a routine deduction does not require an exhaustive literature survey.

## Batch critic for a project research board

For a sustained DISCOVER pass, review the whole batch of raw delegated
outcomes before the orchestrator changes idea states. Read the project-wide
[research board](../../workbench-knowledge/reference/research-board.md),
the relevant per-idea notebooks, the fixed target and assumptions, all
returns from the pass, and the published SOTA rows. Do not edit the raw
`outcome` events. Produce `critique-<pass>.md` with a decision for every
idea and an explicit reason for any unchanged open state.

Classify each proposed dismissal by its stated reason class. Confirm a
`demonstrated_obstruction` only if the evidence addresses the exact lane
and its hypotheses; one failed representation, a famous target, missing
tools, or elapsed time cannot close a wider lane. Requeue every soft
dismissal. Cross-check whether findings from different frames conflict or
jointly imply a new consequence. Compare empirical and quantitative claims
with the published SOTA rows without treating agent results as catalog
records. For a claimed speedup, include the work and memory added by the
new transform, representation, or preprocessing; an eliminated guess or
lower-dimensional subproblem is not by itself a net improvement.

If frames disagree about a potentially useful mechanism, identify the
smallest precise disputed step and obtain a focused independent check before
closing it. Retain the original reports, including an early dismissal that a
later frame contests. Reconciliation may be a new delegated frame or a root
agent check; direct child-to-child messaging is not required.

For every lemma proposal, check its hypotheses, target applicability,
known failures, exact literature locator when sourced from a paper, and
`restates` links. Detect when one proposed lemma follows from another or
restates a known result. Resolve `lemma_proposal_conflicts` before treating an
ID as one result. A new derived lemma requires an independent check
of the fixed candidate before promotion to project `knowledge.md`; a
fresh explanation by the same author is not independent. Record the
checker and exact artifact in the promotion evidence. Keep both the original
`derivation` and the `independent-check` evidence items. Before adding the
lemma to `knowledge.md`, inspect `entry_id_for_claim(lemma_id,
project_dir=project_dir)`, then call `add_entry_once(...,
claim=lemma_id, project_dir=project_dir)` and retain its returned ID. The
helper serializes the lookup and append across cooperating sessions. Check
that any reused entry states the same result and evidence. The later board
`promote` event must carry that `knowledge_id`; the event alone does not
write durable knowledge.

After the critique is saved, the orchestrator appends one `critique` event
with its artifact reference, pass ID, summary, and every reviewed idea ID,
including open ideas. On later passes, triage reads those critique references
with the idea notebooks and passes relevant objections to the next frame.
The orchestrator then appends the critic-approved
`promote` and `close_lane` events with the critique reference and the exact
excluded scope for each closed lane. For an accepted split, it must append
full child `idea` events with `title` and `builds_on` before assigning those
children to new frames. The split event creates open placeholders, not
complete research questions. The critic may recommend those events; it does
not rewrite earlier board lines or silently convert a child-reported state
into a terminal state.

At a meaningful synthesis boundary, explain the material omissions, connections,
or implications identified, and how they changed the research conclusion or
remaining question. If none were justified, say so without manufacturing novelty
or claiming that no possibilities remain. Use the host's artifacts and resource
controls, and the project research board for sustained discovery.
