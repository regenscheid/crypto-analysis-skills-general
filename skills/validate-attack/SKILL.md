---
name: validate-attack
description: Establish whether a claimed attack actually works — state its preconditions, decide whether analysis or an implementation settles the question, then do that one, and report what the result does and does not imply at full parameters. Use when a paper, a post, or an earlier session asserts an attack and the question is whether to believe it.
license: Apache-2.0
---

# Is this attack real?

Use [the environment guide](../investigate/reference/environment.md) to read
related instructions through a native loader, files, or supplied text. Tool names
and Python record-keeping examples below apply only when those capabilities are
available. Without them, analyze the inspected evidence and keep a text record;
label missing source retrieval, computation, or independent checks explicitly.


When invoked directly by “verify,” “check whether,” or equivalent language,
start the answer with `MODE: VALIDATE`. When a DISCOVER investigation hands over
a frozen candidate, preserve `MODE: DISCOVER` and label this work as its bounded
validation subphase. The mode changes who owns the surrounding search; this
skill still checks only the one supplied attack.

An attack claim has two ways of being wrong, and they need different work.

> **It does not apply.** The preconditions are not met by the target, the cost
> model is not the one the comparison uses, or the asymptotic never reaches the
> parameters anyone deploys. **Analysis settles this.** No code.
>
> **It does not run.** The step everyone glosses — "then recover the secret from
> the kernel" — does not do what the sketch says. **Only an implementation
> settles this**, and usually at a scale far below the real one.

Choosing between them is the first real step, and getting it wrong is expensive
in both directions. Writing code to discover a precondition fails is a day spent
on a paragraph. Reasoning confidently about whether a Gröbner basis drops to
degree 3 is how a plausible wrong answer gets published.

## Which skill this is

- **`validate-attack`** — does a *specific claimed attack* hold up?
- **`analyze-scheme`** — is a *scheme* secure, across all attack families?
- **`discover-cryptanalysis`** — generates and maps new candidate attacks; it
  hands this skill one concrete candidate at a time for falsification.
- **`derive-cost`** — nothing has costed this target and you need a number.
- **`analyze-paper`** — the object is a document and its theorems.
- **`verify-claim`** — the object is one stated claim, of any kind.

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
print(read_all(project_dir=project_dir))
```

```
nist-mcp_search_csrc            is it already broken? the round reports say
firecrawl-mcp_firecrawl_search  the forum post or comment that is not a paper
e-print-mcp_search_eprint       the published attack, if there is one
```

If the attack is already published, read it instead of rebuilding it. **For
roughly half of the schemes in a standardization round, the cryptanalysis was
never a paper** — it was a `pqc-forum` post or an official comment, so
`e-print-mcp_search_eprint` will not find it however well you phrase the query.

A miss there is therefore not evidence of no attack. Two channels reach that
material: the NIST round reports, which say why a scheme did not advance
(`nist-mcp_search_csrc`), and a web search for the forum thread itself
(`firecrawl-mcp_firecrawl_search`). Do not fall back on memory for this — it is
the case where recall is least reliable and hardest to check.

## Step 1 — State the attack precisely enough to be wrong

Write it out before deciding anything. If you cannot, that is the finding.

- **What it recovers** — the key, a distinguisher, one bit, a forgery. Say which.
  A distinguisher is not a key recovery, and calling one a break is the single
  most common category error in this domain.
- **Preconditions**, each as a checkbox against the target: parameter ranges,
  structure the attack needs (a subfield, a low-rank matrix, a splitting
  modulus), oracle access, data complexity, whether it needs a weak-key class and
  how large that class is.
- **Claimed cost**, with its **model**. A bare exponent is not a cost. Name the
  model — gate count, RAM operations, field multiplications, and over which
  field — because a figure without one cannot be compared to anything.
- **The source**, opened this session. `e-print-mcp_eprint_fulltext`, not recall. An abstract
  identifies an attack; it rarely states preconditions.

## Step 2 — Choose the route, and say why

**Analysis settles it** when the claim turns on whether the attack *applies*:

- a precondition the target plainly does or does not meet
- a cost model mismatch between the claim and its comparison
- an asymptotic whose crossover is outside every deployed parameter set
- an arithmetic or unit error in the stated complexity
- a notion mismatch — it breaks something other than what is claimed

**Implementation settles it** when the claim turns on whether the attack *runs*:

- a step whose behaviour is an empirical question — does the ideal drop in
  degree, does the lattice actually reduce, does the rank fall where predicted
- a heuristic presented as reliable, with no data behind it
- a success probability justified only heuristically, with no supporting data

A new mathematical claim does not require code merely because it is new. A
complete argument may settle it; an empirical premise needs empirical evidence.
Use [evidence interpretation](../investigate/reference/evidence-interpretation.md)
to choose a route proportionate to the exact claim.

Write the choice down with its reason. A route chosen silently is a route nobody
can challenge, and this step is where the reviewer's leverage is.

## Step 3 — The analysis route

Work the preconditions against the target one at a time, and **cite the target's
actual parameters** rather than the ones the paper assumed. Then:

- Recompute the stated complexity from the stated inputs. Arithmetic errors in
  attack complexities are common and easy to find.
- Put both costs in **one** model before comparing. "The structure costs 60 bits"
  once subtracted a field-multiplication count over `F_8` from a bit-operation
  count over `F_4096`; the difference was meaningless.
- Find the crossover. An asymptotically better attack can lose at every parameter
  in use — the pilot moved one from `log₂p = 79` to **208–262**, which changed
  the verdict from "attack" to "no practical advantage".
- If it needs a number nobody has computed, that is `derive-cost`. Hand it over
  rather than guessing.

An applicability check alone does not establish the claimed behavior. State the
remaining proof or empirical obligation; implementation is required only when
that obligation depends on execution.

## Step 4 — The implementation route

**Time one unit before launching the grid** — `investigate`'s compute route
carries the rule and the two 2026-08-06 failures behind it. The one that
matters here: a script whose docstring said enumeration was "infeasible past
n~32" shipped a default grid running to n=64, and burned 20 minutes on a
computation that could never finish. A bound you know belongs in the code.

**Pick a scale where the answer is checkable.** Reduced parameters, fewer rounds,
a smaller field, a weakened variant with the structure the attack targets planted
deliberately. The point is not to run the real attack; it is to make the claim
falsifiable in minutes.

`reference/sage-idioms.md` carries verified, runnable idioms for the pieces —
planting a low-rank matrix, the degree of regularity from the semi-regular
Hilbert series, q-ary lattice reduction, MILP and SAT skeletons. Use them rather
than re-deriving; every one records its Sage version and its output. For Magma,
see the `magma` skill — an algebraic premise is settled by constructing the
object, not by reasoning about it.

**Then the two runs that make it evidence:**

1. **The positive case.** It succeeds where the claim says it must — on an
   instance with the structure planted, at a scale where you can confirm the
   recovered secret is the real one.
2. **A justified control.** State its expected outcome and why it follows.
   Removing a sufficient precondition does not necessarily force failure. Use
   a known-answer case, an independently checked output, or another comparison
   that addresses a specific failure mode.

When the full-size attack cannot run, build the strongest feasible verification
ladder and label each rung's scope:

1. Check the defining identity or proof step against a separately derived
   argument. This supports that step, not the whole algorithm.
2. Test isolated stages on planted or known-answer inputs, including their
   interfaces. This exposes stage errors but leaves composition open.
3. Exhaustively test small instances where possible, then run scaled end-to-end
   trials on fresh instances. State the sampled key distribution, parameters,
   sample count, and exactly what was recovered or distinguished.
4. Include wrong-key or absent-structure controls and measure false positives
   and verification failures, not only successful runs.
5. If a full-size harness substitutes a secret-dependent value, internal state,
   or unavailable oracle for an attack stage, name the shortcut and report only
   the remaining stage demonstrated. It is not full-size key recovery.

Keep the claimed attacker computation restricted to public data and the stated
oracle access. Secret reads may verify a result in a separate test harness, but
must not feed a supposedly public attack path. Audit the actual code paths using
[crypto-review](../crypto-review/SKILL.md#preconditions-before-cost) and keep
counted full-size cost separate from measured toy-scale runtime.

This is the discipline `scripts/present_milp.py` is built around: it reproduces a
*published* bound — ≥10 active S-boxes over 5 rounds of PRESENT — before its
model is trusted for anything new. A MILP model missing one propagation
constraint returns a clean, confident, entirely wrong answer, and the known-answer
test is what catches it. Reproduce a published result before trusting a model on
an unpublished one.

**Record the failures too.** A run that did not work, with its error, is a
finding. Keep what it said — a status code without its body, an exception without
its message, a non-zero exit without stderr is a diagnosis discarded at the moment
it was free.

## Step 5 — Report what it implies, and what it does not

A toy-scale success is evidence about the toy scale. State the gap explicitly:

- what was run, at what parameters, and how long it took
- what the positive case established, and what the negative control ruled out
- **what does not follow** — scaling behaviour that was assumed rather than
  measured, a constant that grows, a step that is cheap at `n = 20` and dominant
  at `n = 200`
- for a scaling claim, the parameters you *did* run, so the extrapolation is
  visible and arguable rather than implied

Report exactly what the evidence establishes. A checked witness or exhaustive
finite computation can verify its scoped predicate; state the domain, coverage,
and trusted implementation. A non-exhaustive search supports only “no
counterexample found” under the stated parameters and sampling process.

## Write back

Use the same `project_dir` resolved at Step 0.

```python
from knowledge import add_entry, add_gap
add_entry(statement="<attack> requires <precondition>, which <target> does not meet",
          kind="attack",
          evidence=[{"kind": "paper", "ref": "…", "note": "preconditions, §3"},
                    {"kind": "computation", "ref": "…", "note": "toy-scale run"}],
          project_dir=project_dir)
add_gap(question="…", looked_in=["ePrint", "NIST", "firecrawl", "web"],
        finding="…", project_dir=project_dir)
```

These **append** — never rewrite those files, and never reach for `edit_file` to
add a record: concurrent writers lose entries that way (measured, 1193 of 1200).

**A refuted attack is as valuable an entry as a confirmed one**, and cheaper to
record than to rediscover. Say which of the two ways it failed — did not apply,
or did not run.

## What this deliberately does not do

- **It does not search for attacks.** It takes one that is claimed. Breadth is
  `analyze-scheme`; candidate generation and cross-field transfer are
  `discover-cryptanalysis`. Both are different jobs.
- **It does not implement by default.** Reaching for code when analysis settles
  the question is the failure this skill's Step 2 exists to prevent.
- **It does not treat a toy-scale success as a break.** The scale gap is the
  result's main limitation and belongs in the first paragraph of the report.
- **It does not build production attack code.** Everything here is throwaway
  evidence at a scale chosen to be checkable.
