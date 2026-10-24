---
name: crypto-verify-claim
description: Check whether one specified claim in a paper, report, or security argument is correct. Audit its reasoning or reproduce the relevant evidence and report supported, refuted, or unresolved. Use for an assigned claim-verification task; merely citing or applying a published result does not require auditing that result.
license: Apache-2.0
---

# Check one paper claim

Use [the environment guide](../crypto-investigate/reference/environment.md) to read
related instructions through a native loader, files, or supplied text. Tool names
and Python record-keeping examples below apply only when those capabilities are
available. Without them, analyze the inspected evidence and keep a text record;
label missing source retrieval, computation, or independent checks explicitly.


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
retrieved knowledge entry is provenance; inspect what that evidence actually
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

Negatives are the most frequently wrong of these. See failure mode 5.

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
| `[KB]` | retrieved from the knowledge base or ledger — cite the entry id |
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
| what a document says | **open the document** — `e-print-mcp_eprint_fulltext`, `nist-mcp_csrc_fulltext`, the body not the abstract |
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

These historical examples motivate checks when the corresponding failure mode
is relevant. They do not require opening unrelated sources or rerunning unrelated
calculations for every assigned claim.

**1. Uncited recall of reference data.** Parameter tables, published costs, which
scheme a name refers to. *Observed:* a probe's "fresh" parameters were a
published LUOV set, asserted from memory and never checked; the same class of
error recurred a second time on the same file. **Check:** every parameter tuple
and published figure carries `[SOURCE]`.

**2. Over-correction from a partial source.** Treating one document as exhaustive
and overturning a true statement with it. *Observed:* a correct claim that LUOV
round 2 used prime `r` was "corrected" to composite on the strength of a version
of the paper that omits the table showing both — arriving with more confidence
than the original error. **Check:** before overturning a prior claim, establish
that the new source is *complete* for that question. Prefer the archival version
over a conference version; they differ.

**3. Stale derived numbers after an input change.** *Observed:* changing a
parameter set and recomputing some outputs but not others left a key-recovery
figure 10.2 bits wrong, inside a rubric with a ±0.5 tolerance. **Check:** when an
input changes, identify every affected dependency and recompute those conclusions.
Retain checks whose inputs and assumptions did not change; if dependencies are
uncertain, state which additional review is needed to establish their scope.

**4. Unit or model mismatch in a comparison.** *Observed:* "the structure costs
60 bits" subtracted a field-multiplication count over `F_8` from a bit-operation
count over `F_4096`. **Check:** every difference of two costs states the unit and
the cost model of both. A bare exponent is not a result.

**5. A negative concluded from an incomplete look.** *Observed three times in one
session:* "the repo has no attack references" from a sparse checkout that never
pulled `solution/`; "the paper body is unreachable" from one host's `robots.txt`
when another host served it; "the corpus does not cover this" when the full-text
cache held 9 of 924 documents. **Check:** a negative must name what was searched
and how completely. "Not found in X" is a claim about X.

**6. Discarding the diagnostic you already had.** *Observed:* a fetch returned
HTTP 403 and the script kept the status code and threw away the response body.
The body was the Cloudflare interstitial, which would have said the challenge was
never solved. Instead "403" was reported as a bare fact and written up as a
property of the *publisher* — when it was a property of the script's control
flow. Three further "403" rows in the same table inherited the error.

**Check:** when something fails, keep what it said. A status code without its
body, an exception without its message, a non-zero exit without stderr — each is
a diagnosis discarded at the moment it was free. This is worse than failure mode
5: there the evidence was never gathered; here it was in hand and destroyed.

**7. Verification that repeats the asserter's unchecked premise.** A different
reader or citation does not automatically supply independent evidence. **Check:**
identify the error your route could expose. Independently reconstructing an
argument from the same paper or specification is valid checking. Open another
source when it addresses a specific uncertainty; source novelty is not a gate.

**8. Silent aggregate failure.** *Observed twice:* one estimator family raising
discarded eight valid results, and the failure formatted as a tuple rather than
an error. **Check:** any "cheapest of N" states what was skipped. A minimum over
a reduced set is an upper bound on the minimum over the full set, provided the
retained costs are valid and comparable. State omitted cases; invalid estimates
may support no bound at all.

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

## Step 6 — Write back

Facts that had to be retrieved once should not be retrieved again from scratch.
Follow [crypto-workbench-knowledge's project setup](../crypto-workbench-knowledge/SKILL.md#read-it-first)
to import its helpers and resolve the stable `project_dir` first.

```python
from knowledge import add_entry, add_gap
add_entry(statement="<checked claim under its stated assumptions>", kind="derived result",
          evidence=[
              {"kind": "derivation", "ref": "<discovery artifact>#C2",
               "note": "Original argument, assumptions, and notation map."},
              {"kind": "independent-check", "ref": "<verifier report>",
               "note": "Fresh proof audit checked C2 without repairing it."},
          ], project_dir=project_dir)
add_gap(question="<question not settled>", looked_in=["ePrint", "NIST"],
        finding="<what was checked and why the question remains open>",
        project_dir=project_dir)
```

See `crypto-workbench-knowledge`. These **append** — never rewrite those files, and
never reach for `edit_file` to add a record: concurrent writers lose entries
that way (measured, 1193 of 1200).

`looked_in` is a list of **channels**, not a mood. "Searched ePrint" and "searched
ePrint, the NIST corpus, and the web" are different findings,
and each supports only a negative about its stated search scope.

Do not write a derivation-only candidate to durable knowledge. Keep it in the
live plan and the versioned discovery artifact until the `independent-check`
record exists. Ordinary sourced facts retain their existing evidence rules; this
extra gate applies when the claimed result is newly derived.

## What this deliberately does not do

- **It does not decide which claims matter.** It takes one. Working out what a
  document's load-bearing claims are is `crypto-analyze-paper`, and keeping them apart is
  what keeps this bounded.
- **It checks reasoning when correctness depends on it.** A well-sourced claim
  can still be false. A broader review of the analysis belongs to `crypto-review`.
- **It does not promote a derivation by repeating it.** New theoretical work
  needs a genuinely separate checking route before it becomes durable knowledge.
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
