---
name: crypto-verify-claim
description: "Check whether one specified claim in a paper, report or security argument is correct, by auditing its reasoning or reproducing its evidence, and report supported, refuted or unresolved. Use for an assigned claim check; citing or applying a published result does not require one."
license: Apache-2.0
---

# Check one paper claim

Use [the environment guide](../crypto-investigate/reference/environment.md) to read
related instructions through a native loader, files, or supplied text, and
[the retrieval reference](../crypto-investigate/reference/tools.md) for sources.
Without retrieval or execution, analyze the inspected evidence and label missing
source retrieval, computation, or independent checks explicitly.


When asked to check whether a specified claim is correct, start with
`MODE: VALIDATE`. If a larger investigation assigns this bounded check, preserve
its declared mode and identify the verification subtask. Do not infer a paper
audit from a request to understand or use the paper. Read
[paper use and verification](../crypto-investigate/reference/paper-use-and-verification.md)
when deciding which task was assigned.

You are handed a claim and asked whether it holds. **One claim, deliberately** —
working out *which* claims in a body of work are load-bearing is `crypto-analyze-paper`'s
job, and merging the two turns a bounded check into an unbounded one.

Keep these questions distinct:

> **What exactly does the source claim?**
> **Does its argument or evidence establish that claim?**

Finding the statement in a paper establishes its attribution. It does not
establish the statement's correctness. Likewise, a completed command or a
retrieved earlier record is provenance; inspect what that evidence actually
supports. For a correctness verdict, check the argument, the relevant
computation, or a prior independent check that covers the same claim and scope.
An incomplete proof is unresolved unless a valid contradiction refutes the
claim. Conditional lemmas remain useful with their open premises visible.

Reuse prior verification when the claim, source revision, assumptions, and
evidence scope match; identify it as reused. A recorded citation alone cannot
stand in for a prior correctness check. An explicit request for fresh independent
verification still calls for fresh work on the assigned claim.

## Which skill this is

- **`crypto-verify-claim`** — whether one assigned paper or argument claim is correct.
- **`crypto-analyze-paper`** — a whole document, and which of its claims are worth
  settling. It hands work to this skill.
- **`crypto-validate-attack`** — the claim is specifically that an attack works.
- **`crypto-derive-cost`** — nothing has costed the target and a number is needed.
- **`crypto-review`** — review a supplied analysis for reasoning and reporting defects.
- **`mathematical-research-development`** — develop a stated mathematical question
  using published ingredients; invoking this skill does not require this verifier.

## Plan when the task needs it

For multi-stage work, use the current host's plan interface or a short written
plan and begin the authorized analysis. A bounded check may need no formal plan.
Independent work can run sequentially; delegation is optional and subject to the
host's capabilities and permissions. Follow
[the environment guide](../crypto-investigate/reference/environment.md).

## Step 1 — Restate the claim precisely enough to be settled

A claim as received is usually not checkable. "ML-KEM-512 is category 1" has no
truth value until you say under which metric, against which peg, and at which
revision of the peg. **Restating is not a formality — it is where most claims
turn out to be two claims, or none.**

Within the assigned claim, identify the premises on which its conclusion depends.
These often include:

- **numbers** — attack costs, security levels, memory, probabilities, degrees
- **parameter sets** — any `(n, m, q, r)` tuple, any named parameter set
- **attributions** — "X broke Y", "paper Z shows", "the standard says"
- **applicability** — "this attack applies", "the precondition is met"
- **negatives** — "no such paper exists", "the estimator has no model for this",
  "this is not in the corpus"

Negatives are the most frequently wrong of these. See failure mode 5 in
[the failure taxonomy](reference/failure-taxonomy.md).

Then pin down what would make it true or false:

- **the notion and the model**, if it is a security claim — "IND-CCA2" alone is
  incomplete, and ROM and standard-model versions are different claims. The
  `crypto-analyze-paper` skill's `reference/` set states each notion as obligations to
  discharge rather than prose to cite.
- **the cost model and unit**, if it is a cost. A bare exponent is not a claim.
- **the exact parameters** it is asserted about, not the ones nearby.
- **what was searched, and how completely**, if it is a negative.

If the restatement cannot be written, stop and say so. An unstatable claim is a
finding, and it is the cheapest one available.

## Step 2 — Establish how it was obtained

| tag | meaning |
|---|---|
| `[SOURCE]` | an exact source statement was inspected — cite revision and locator, identifying reused inspection when applicable |
| `[TOOL]` | a computation has an identified run and output — cite invocation, inputs, and whether it was rerun here |
| `[RECORD]` | retrieved from this environment's durable record of earlier results — cite its identifier or location |
| `[DERIVATION]` | a new argument was worked this session — cite the candidate artifact and state its assumptions; this is candidate provenance, not independent support |
| `[RECALL]` | asserted from knowledge, with no retrieval and no computation |

These are provenance tags, not correctness verdicts. Resolve unsupported recall
through the relevant source or evidence before relying on it in the verification.

`[DERIVATION]` is not `[RECALL]`: it exposes a checkable chain of reasoning. But
it is not `[TOOL]` merely because some algebra was typed into a notebook. A tool
run supports exactly the finite computation it performed; it does not
independently establish the general argument that selected or interpreted that
computation.

Ground the classification in actual inspected material, recorded runs, or
supplied host evidence. A sentence that claims a tool ran is insufficient.
Previously supplied evidence need not produce a new tool call to remain usable.

## Step 3 — Pick the route that actually settles it

Reproducing a number is one route, not the definition of the work. Match the
route to what the claim rests on:

| the claim rests on | settle it by |
|---|---|
| a computation someone ran | **reproduce or independently reconstruct the relevant calculation** — compare its inputs, model, and output with the published claim |
| what a document says | **open the document** — the body at the relevant page, not the abstract ([retrieval order](../crypto-investigate/reference/tools.md#look-in-this-order)) |
| a definition being met | **discharge the obligations** — the `crypto-analyze-paper` skill's `reference/` set lists them per notion |
| an attack working | **hand it to `crypto-validate-attack`** — which decides whether analysis or code settles it |
| a cost nobody has computed | **hand it to `crypto-derive-cost`** |
| a new theoretical derivation | **check it by an independent route** — independent re-derivation, proof audit, computation, or human review |
| something not existing | **name the channels searched** — a negative is a claim about the search |

When the route *is* reproduction, two checks catch most of what goes wrong:

- **Can the reported calculation be reconstructed?** Missing code makes a result
  unreproduced here; it does not prove it false. A mathematical value may be
  established by an exact derivation. Measured performance needs measurement evidence.
- **Do the inputs match the claim's inputs?** A number computed for one parameter
  set and reported for another is the single most common real defect here.

Choose a route capable of addressing the claimed evidence or suspected error.
Matching one displayed number does not check the proof or all dependent claims.

For a new derivation, make independence concrete. Give the checker the exact
claim, target definitions, assumptions, and candidate artifact, then ask it to
find the shortest refutation or check the argument through a separate route.
Use an available independent checking route. Give a verdict on the fixed
argument; do not silently repair a missing step before judging it. A gap leaves
the claim unresolved unless it supplies a contradiction. A separately requested
repair should identify the changed argument and preserve the original verdict.

Record the original reasoning as `derivation` evidence and the separate result
as `independent-check` evidence. The latter names which route was used and what
was actually checked. Reading the same conclusion twice, or having the author
rephrase it, is not independent. Prior art can support ingredients, but it does
not check a new inference unless it establishes that exact inference under the
same assumptions.

## Step 4 — Work the failure taxonomy

[The failure taxonomy](reference/failure-taxonomy.md) lists eight recurring ways a
claim check goes wrong, each with an observed case and the check that catches
it. Read the rows relevant to the assigned claim; they do not require opening
unrelated sources or rerunning unrelated calculations. The ones that matter
most often:

- **uncited recall of reference data** — every parameter tuple and published
  figure carries `[SOURCE]`;
- **a negative concluded from an incomplete look** — a negative names what was
  searched and how completely (failure mode 5);
- **unit or model mismatch** — every difference of two costs states the unit and
  cost model of both;
- **discarding the diagnostic you already had** — when something fails, keep
  what it said.

## Step 5 — Report

One of three verdicts, and the third is a real answer:

- **supported** — with the route that settled it and the evidence it produced
- **refuted** — with the same
- **unresolved** — with **what would settle it and why that was not done**

State the question to which the verdict applies. “The paper states X” can be
supported while “X is correct” remains unresolved. Name reused evidence, fresh
checks, unchecked dependencies, and the exact conclusion they support.

Do not round `unresolved` to true or false. Forcing uncertainty into a verdict is
how the 19-of-19 refutation happened, and an unresolved claim with a named next
step is more useful than a confident wrong one.

A new theoretical claim carrying only `[DERIVATION]` is `unresolved` as a claim
and remains a candidate in the discovery artifact. It can become `supported`
only after an independent re-derivation, proof audit, computation, or human
review checks the same claim. A failed cheap falsifier may refute it immediately;
independence is a gate for promotion, not a reason to preserve a dead candidate.

Report the restatement alongside the verdict. A claim settled in a form nobody
else would recognise has not been settled for them — and if the restatement
turned one claim into two, say so and give a verdict for each.

When several claims came from one `crypto-analyze-paper` pass, a summary line helps:

```
claims settled       n of N
  supported / refuted / unresolved   n / n / n
  [RECALL] converted to [SOURCE]|[TOOL]   n
```

**The list is the deliverable**, not the rate — a single unsupported parameter set
matters more than a high percentage.

## Step 6 — Record the result

Facts that had to be retrieved once should not be retrieved again from scratch.
Use the host's own record of results if it has one; otherwise follow
`crypto-workbench-knowledge` (without durable storage, a handoff in the
conversation). Record the checked claim under its
stated assumptions, the verdict, the evidence with locators — for a new
derivation both the original argument (`derivation`) and the separate check
(`independent-check`, naming its route and what it checked) — and what was not
checked. For a question not settled, record what was checked and why it remains
open.

Name the **channels** searched for a negative. "Searched ePrint" and "searched
ePrint, the NIST publications, and the web" are different findings, and each
supports only a negative about its stated search scope.

Do not record a derivation-only candidate as an established result. Keep it in
the live plan and the discovery record as a candidate until the
`independent-check` evidence exists. Ordinary sourced facts retain their existing evidence rules; this
extra gate applies when the claimed result is newly derived.

## What this deliberately does not do

- **It does not decide which claims matter.** It takes one. Working out what a
  document's load-bearing claims are is `crypto-analyze-paper`, and keeping them apart is
  what keeps this bounded.
- **It checks reasoning when correctness depends on it.** A well-sourced claim
  can still be false. A broader review of the analysis belongs to `crypto-review`.
- **It does not promote a derivation by repeating it.** New theoretical work
  needs a genuinely separate checking route before it is recorded as established.
- **It distinguishes retrieval from verification.** Retrieval can settle an
  attribution or supply compatible prior verification. A paper's assertion
  alone does not settle an assigned correctness check of its reasoning.
- **It reports the exact evidence scope.** A checked witness or exhaustive finite
  computation can verify a scoped predicate. Random sampling and unsuccessful
  searches do not establish a universal claim. Use
  [evidence interpretation](../crypto-investigate/reference/evidence-interpretation.md).
- **It does not hide anything.** There is no answer key, nothing is scored
  against a secret, and the same work can be audited repeatedly without being
  spent.
