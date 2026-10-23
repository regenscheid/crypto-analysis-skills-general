---
name: analyze-paper
description: Work out whether a paper proves what it claims — separate the informal claim from the theorem, name the notion and the model, run the mismatch checklist, carry the reduction's loss into the concrete parameters, and say which claims are worth settling. Use when asked to audit whether a paper or security argument supports its claims. Reading or applying a published result alone does not assign this audit.
license: Apache-2.0
---

# Does the paper prove what it claims?

Use [the environment guide](../investigate/reference/environment.md) to read
related instructions through a native loader, files, or supplied text. Tool names
and Python record-keeping examples below apply only when those capabilities are
available. Without them, analyze the inspected evidence and keep a text record;
label missing source retrieval, computation, or independent checks explicitly.


Two statements about the same paper, both honest, that a review has to keep apart:

> **What the abstract says.** "We give an attack on X."
> **What the theorem says.** Under GRH, for `p → ∞`, an algorithm running in
> `p^{1/3+o(1)}` where the `o(1)` is not quantified and the constant is
> `(B + log p)^{O(1)}`, unevaluated.

The distance between those two is where this skill works. It is not a hunt for
errors — most papers are correct and still support a weaker claim than the one
that gets repeated about them. **The commonest real finding is not a wrong proof;
it is a right proof of a different statement.**

Read [paper use and verification](../investigate/reference/paper-use-and-verification.md)
when distinguishing this audit from source interpretation or use of a theorem.
Keep the audit rigorous within its assigned scope; an inspected source alone
establishes an attribution, not its mathematical correctness.

## Which skill this is

- **`analyze-paper`** — does the argument support the claims? Paper-level.
- **`verify-claim`** — takes one claim and settles it. Use it on what §5 hands out.
- **`derive-cost`** — the target has no published cost and you need one. There a
  reduction is a *route to a number*; here it is an *argument to be audited*.
- **`analyze-scheme`** — the object is a scheme and its parameters, not a document.

## Plan when the task needs it

For multi-stage work, use the current host's plan interface or a short written
plan and begin the authorized analysis. A bounded check may need no formal plan.
Independent work can run sequentially; delegation is optional and subject to the
host's capabilities and permissions. Follow
[the environment guide](../investigate/reference/environment.md).

## Step 0 — Read what is already known

Follow [workbench-knowledge's project setup](../workbench-knowledge/SKILL.md#read-it-first)
to import its helpers and resolve the stable `project_dir` before reading or
writing research records.

```python
from knowledge import read_all
print(read_all(project_dir=project_dir))  # knowledge, gaps, and lessons for this project
```

```
nist-mcp_search_csrc            is the scheme already broken? round reports
firecrawl-mcp_firecrawl_search  the forum post or comment that is not a paper
```

A recorded gap describes the scope and outcome of an earlier attempt. A search
miss or unavailable tool is not a mathematical obstruction; reconsider it when
the source, model, or capability changes. The round reports and a web search
can be relevant because **a
large share of competition cryptanalysis was never a paper** — it was a
`pqc-forum` post or an official comment, and `e-print-mcp_search_eprint` will not
find it.

## Step 1 — Read the body, then write down what is claimed

```
e-print-mcp_eprint_fulltext(paper_id, query)    the BODY, from a local cache
nist-mcp_csrc_fulltext(ref, query)           the same, for standards
```

An abstract identifies a result; it rarely states one precisely enough to audit.
A reduction remembered rather than read is the failure this workbench is built
against — this project once derived a cost model from an abstract, got the
reduction one equation wrong, and found out only when a human handed over the
PDF. Discover the available retrieval capability; historical fetch timings are
not guarantees for the current host.

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
  "0–5 bits of advantage at NIST-I". If it needs a cost, that is `derive-cost`.
- **Check the crossover.** An asymptotically better algorithm can be worse at
  every parameter anyone uses. Find where it actually wins.

## Step 5 — Say what would change the conclusion

Close with two lists, both short.

**Claims worth settling** — the discrete ones, each stated precisely enough that
someone could settle it without re-reading the paper. These are what you hand to
`verify-claim`; a claim it cannot act on was not stated finely enough here.

**What would change the answer** — the specific evidence, not a hedge. "If the
independence assumption in Lemma 3 fails, the bound is vacuous." "If the
unevaluated constant is below 2^10, the crossover lands inside NIST-I." This is
the most valuable paragraph in the report, because it converts a verdict into a
research plan and it is the one an author can argue with.

**Check the bibliography, do not recall it.** The pilot found a real citation
defect this way — Corollary 1.2 cited a GRH-conditional reduction where an
unconditional one exists, in a paper the article already cites. That was found by
opening the bibliography.

## Write back

Use the same `project_dir` resolved at Step 0.

```python
from knowledge import add_entry, add_gap
add_entry(statement="…", kind="notion",
          evidence=[{"kind": "paper", "ref": "…", "note": "theorem 3, ROM"}],
          project_dir=project_dir)
add_gap(question="…", looked_in=["ePrint", "NIST", "firecrawl", "web"],
        finding="…", project_dir=project_dir)
```

These **append** — never rewrite those files, and never reach for `edit_file` to
add a record: concurrent writers lose entries that way (measured, 1193 of 1200).
`looked_in` is a list of **channels**, not a mood.

A mismatch found is worth recording as an entry. So is a mismatch looked for and
absent — that is what licenses the next reader to skip the check.

## What this deliberately does not do

- **It does not settle the claims it finds.** That is `verify-claim`, and keeping
  them apart is what stops a paper audit turning into an unbounded verification
  run.
- **It does not decide whether the scheme is secure.** A paper is one input.
  `analyze-scheme` owns the scheme.
- **It reports the scope actually checked.** Source reading establishes what was
  stated; a proof audit or exact finite check can establish more within its
  scope. Do not label a whole paper verified after a bounded checklist. Use
  [evidence interpretation](../investigate/reference/evidence-interpretation.md).
- **It does not treat a correct proof as a strong result.** Correct and weak is
  the normal case, and saying so is the deliverable.
