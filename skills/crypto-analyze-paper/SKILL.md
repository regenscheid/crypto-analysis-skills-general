---
name: crypto-analyze-paper
description: Work out whether a paper proves what it claims — separate the informal claim from the theorem, name the notion and the model, run the mismatch checklist, carry the reduction's loss into the concrete parameters, and say which claims are worth settling. Use when asked to audit whether a paper or security argument supports its claims. Reading or applying a published result alone does not assign this audit.
license: Apache-2.0
---

# Does the paper prove what it claims?

Use [the environment guide](../crypto-investigate/reference/environment.md) to read
related instructions through a native loader, files, or supplied text, and
[the retrieval reference](../crypto-investigate/reference/tools.md) for sources.
Without retrieval or execution, analyze the inspected evidence and label missing
source retrieval, computation, or independent checks explicitly.


Two statements about the same paper, both honest, that a review has to keep apart:

> **What the abstract says.** "We give an attack on X."
> **What the theorem says.** Under GRH, for `p → ∞`, an algorithm running in
> `p^{1/3+o(1)}` where the `o(1)` is not quantified and the constant is
> `(B + log p)^{O(1)}`, unevaluated.

The distance between those two is where this skill works. It is not a hunt for
errors — most papers are correct and still support a weaker claim than the one
that gets repeated about them. **The commonest real finding is not a wrong proof;
it is a right proof of a different statement.**

Read [paper use and verification](../crypto-investigate/reference/paper-use-and-verification.md)
when distinguishing this audit from source interpretation or use of a theorem.
Keep the audit rigorous within its assigned scope; an inspected source alone
establishes an attribution, not its mathematical correctness.

## Which skill this is

- **`crypto-analyze-paper`** — does the argument support the claims? Paper-level.
- **`crypto-verify-claim`** — takes one claim and settles it. Use it on what §5 hands out.
- **`crypto-derive-cost`** — the target has no published cost and you need one. There a
  reduction is a *route to a number*; here it is an *argument to be audited*.
- **`crypto-analyze-scheme`** — the object is a scheme and its parameters, not a document.

## Plan when the task needs it

For multi-stage work, use the current host's plan interface or a short written
plan and begin the authorized analysis. A bounded check may need no formal plan.
Independent work can run sequentially; delegation is optional and subject to the
host's capabilities and permissions. Follow
[the environment guide](../crypto-investigate/reference/environment.md).

## Step 0 — Check what is already established

Look first for earlier audits of this paper, checked claims, and recorded dead
ends. Use the host's own record of results if it has one; otherwise follow
`crypto-workbench-knowledge` (without durable storage, a handoff in the
conversation). A recorded
gap describes the scope and outcome of an earlier attempt. A search miss or
unavailable tool is not a mathematical obstruction; reconsider it when the
source, model, or capability changes.

Then ask whether the scheme the paper is about is already broken: the official
round-status reports and a web search, as
[the retrieval reference](../crypto-investigate/reference/tools.md#cover-the-open-web-gap)
describes. **A large share of competition cryptanalysis was never a paper** — it
was a `pqc-forum` post or an official comment, and a preprint search will not
find it.

## Step 1 — Read the body, then write down what is claimed

Open the paper's body (for standards, the exact edition) through the
[retrieval order](../crypto-investigate/reference/tools.md#look-in-this-order),
and note the page of every statement you will rely on.

An abstract identifies a result; it rarely states one precisely enough to audit.
A reduction remembered rather than read is the failure to guard against: a cost
model derived from an abstract once had its reduction one equation wrong, found
only when someone opened the PDF.

Write the informal claims down verbatim, from the abstract, the introduction, and
any conclusion. These are the sentences that will be quoted about this paper.
Keep them separate from what you find in §2 — the whole method depends on not
merging the two.

## Step 2 — Write down what is actually proved

For each theorem, corollary and lemma that carries weight:

- **The statement.** Quantifiers included. `∀ p` and `for p → ∞` are different papers.
- **The notion.** Name it. `reference/` splits the definitions by primitive so you
  load only what you need — see the table below.
- **The model.** Standard, ROM, QROM, ideal cipher, generic group. "IND-CCA2"
  alone is incomplete; **"IND-CCA2 in the ROM" and "IND-CCA2 in the standard
  model" are different claims with different strengths.**
- **The assumptions.** Every one, including the ones stated once in §1 and never
  repeated — GRH, heuristic regularity, an independence assumption between two
  distributions, a random-oracle instantiation.
- **What is left unquantified.** An `o(1)`, an `O(1)` constant, a "for sufficiently
  large", a polynomial factor named but not evaluated. These are where the
  distance in the opening lives, and the author often flags them honestly.

| reference file | covers |
|---|---|
| `reference/conventions.md` | advantage conventions, concrete vs asymptotic, query budgets, standard/ROM/QROM. **Read with any of the others.** |
| `reference/pke-kem.md` | IND-CPA, IND-CCA1/CCA2, KEM IND-CCA, non-malleability |
| `reference/signatures.md` | EUF-CMA, SUF-CMA, the state-reuse obligation |
| `reference/hash.md` | the seven Rogaway–Shrimpton notions and their implications |
| `reference/symmetric-aead.md` | IND-CPA, INT-PTXT/INT-CTXT, generic composition |
| `reference/nist-categories.md` | categories I–V and the four traps in claiming one |
| `reference/mismatches.md` | the twelve-row checklist §3 runs |

Each notion there is written as **Game → Obligations → Operational break**, and
the obligations are checkboxes on purpose. The measured failure mode is not
ignorance of a definition; it is **asserting a definition is satisfied without
evaluating it**. A glossary does not help with that; a list of obligations that
must each be discharged does.

## Step 3 — Run the mismatch checklist

`reference/mismatches.md`, twelve rows, each a recurring real finding. Work it as
a checklist rather than reading it as prose — the top row alone (proof gives
IND-CPA, claim says IND-CCA2) is the commonest finding in the file.

For each mismatch found, record three things: the claimed notion, the proved
notion, and **whether the gap is closable**. "The proof is for IND-CPA" is an
observation; "the scheme is re-randomisable so SUF does not follow, and here is
the mauling" is a finding.

## Step 4 — Carry the loss into the concrete claim

An asymptotic theorem plus a parameter set is not a security level. This is the
step papers most often skip and reviews most often skip checking.

- **Instantiate the bound.** Put the actual `q_H`, `q_S`, `q_D` and the actual
  parameters in. A bound whose query budgets are missing is not concrete.
- **Carry the reduction's loss.** A factor of `q_H` or a rewinding square root
  moves the claimed level. If the paper claims 128 bits from a reduction losing
  `q_H = 2^64`, say what is left.
- **Evaluate what the author left unevaluated**, or say you could not. Pricing an
  unevaluated constant is exactly how the pilot turned "an attack on X" into
  "0–5 bits of advantage at NIST-I". If it needs a cost, that is `crypto-derive-cost`.
- **Check the crossover.** An asymptotically better algorithm can be worse at
  every parameter anyone uses. Find where it actually wins.

## Step 5 — Say what would change the conclusion

Close with two lists, both short.

**Claims worth settling** — the discrete ones, each stated precisely enough that
someone could settle it without re-reading the paper. These are what you hand to
`crypto-verify-claim`; a claim it cannot act on was not stated finely enough here.

**What would change the answer** — the specific evidence, not a hedge. "If the
independence assumption in Lemma 3 fails, the bound is vacuous." "If the
unevaluated constant is below 2^10, the crossover lands inside NIST-I." This is
the most valuable paragraph in the report, because it converts a verdict into a
research plan and it is the one an author can argue with.

**Check the bibliography, do not recall it.** The pilot found a real citation
defect this way — Corollary 1.2 cited a GRH-conditional reduction where an
unconditional one exists, in a paper the article already cites. That was found by
opening the bibliography.

## Record the result

Use the host's own record of results if it has one; otherwise follow
`crypto-workbench-knowledge` (without durable storage, a handoff in the
conversation). For each finding give the
statement, its evidence with locators (for example "theorem 3, ROM, p. 12"), its
limits, and what was not checked. For a question left open, record the channels
searched — "ePrint, NIST, web" is a different finding from "ePrint" — and what
was found.

A mismatch found is worth recording. So is a mismatch looked for and absent —
that is what licenses the next reader to skip the check. Extend an existing
record rather than rewriting it.

## What this deliberately does not do

- **It does not settle the claims it finds.** That is `crypto-verify-claim`, and keeping
  them apart is what stops a paper audit turning into an unbounded verification
  run.
- **It does not decide whether the scheme is secure.** A paper is one input.
  `crypto-analyze-scheme` owns the scheme.
- **It reports the scope actually checked.** Source reading establishes what was
  stated; a proof audit or exact finite check can establish more within its
  scope. Do not label a whole paper verified after a bounded checklist. Use
  [evidence interpretation](../crypto-investigate/reference/evidence-interpretation.md).
- **It does not treat a correct proof as a strong result.** Correct and weak is
  the normal case, and saying so is the deliverable.
