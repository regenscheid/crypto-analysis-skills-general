---
name: crypto-review
description: Review a supplied cryptographic analysis for cost-model, precondition, security-notion, parameter-provenance, and citation defects. Use for an assigned analysis review; merely citing or applying a paper does not require a fresh citation or paper audit.
license: Apache-2.0
---

# Crypto review

Use [the environment guide](../crypto-investigate/reference/environment.md) to read
related instructions through a native loader, files, or supplied text. Tool names
and Python record-keeping examples below apply only when those capabilities are
available. Without them, analyze the inspected evidence and keep a text record;
label missing source retrieval, computation, or independent checks explicitly.


Cryptographic claims fail in ways that generic review does not catch, because
the *form* of a security statement carries most of its meaning. A well-formed
sentence can be confidently wrong in a way that misleads anyone who acts on it,
and it will read as fluent domain knowledge while doing so.

Two things make this checkable rather than a matter of taste: most of these
errors are visible in the statement itself, and the citations are checkable
against a real corpus.

## Know which of these you can actually do

Assess the reviewer's actual access. With only the supplied analysis, check
statement form, reasoning, assumptions, and internal consistency. With source
retrieval, inspect exact citations. With suitable execution, reproduce material
calculations. Role names do not establish any of these capabilities. Use an
independent worker only when available and authorized; otherwise label the review
as a self-check rather than independent verification.

Never claim to have checked something you had no tool to check. That failure is
worse than the one this skill exists to catch, because it is a fabricated
verification rather than a fabricated fact.

## Check citations against the corpus, not against memory

Use the source routes actually available; supplied text may be the only route.

Use compatible prior inspection with identifiable provenance when the statement,
revision, and scope match. Reopen the affected source for a changed dependency,
conflicting evidence, suspected attribution error, or an explicit fresh audit.
Follow [paper use and verification](../crypto-investigate/reference/paper-use-and-verification.md).
When fresh retrieval is needed, use available source connectors; a cited paper
is a checkable attribution:

Find preprints, standards, exact document revisions, and official comments using
available connectors, web tools, or supplied documents. No particular corpus or
connector size is assumed.

- **Does the reference resolve?** Inspect the returned record. A failed lookup
  leaves the reference unresolved through that route; it does not establish
  fabrication. Check for an identifier error or a coverage/access limit before
  reaching a stronger conclusion.
- **Does it say what is claimed?** Open the exact theorem, algorithm, table, or
  section in the relevant revision. An abstract identifies a topic; it rarely
  establishes the precise assumptions or conclusion of a load-bearing claim.
- **Is the attribution right?** Authors and title come back with the record.

State what you inspected and its locator. A metadata check establishes that the
reference resolves; reading the exact result establishes what that source says.
Keep those findings separate from independent correctness of its argument.

If neither a source nor compatible prior inspection is available, say the
attribution is unverified here. Corpus unavailability does not invalidate an
already inspected source or turn it into recall.

## Every cost figure carries its model, or it means nothing

Priced on the same instance at the same block size:

| model | ML-KEM-512 | 768 | 1024 |
|---|---|---|---|
| `ADPS16` core-SVP, classical | 2^118.6 | 2^182.2 | 2^255.2 |
| `MATZOV` | 2^143.8 | 2^204.9 | 2^275.1 |
| `BDGL16` sieve, gate count | 2^147.9 | 2^212.1 | 2^285.5 |
| `CheNgu12` enumeration | 2^280.8 | 2^485.4 | 2^745.3 |

**25 bits between two defensible sieving models, 160+ across the table.** A bare
`2^143` is not a result. ADPS16 is the conservative convention NIST submissions
quote. CheNgu12 prices a different algorithm family and is not apples-to-apples
with the rest — flag any comparison that treats it as such.

## Preconditions before cost

A cheap attack that does not apply is not a finding, and an estimator will price
it regardless. Before accepting a cost:

- Does the scheme actually have the structure the attack needs?
- Is the parameter regime inside the attack's validity range?
- Is the memory requirement physically plausible? A 2^80-memory attack is not an
  operational break of a 2^128 scheme.
- **A sub-2^64 figure on a standardised parameter set is far more likely a
  misapplied model than a break.** Question it rather than repeating it.

For an empirical attack claim with code, list every code path that reads the
secret key, expanded or round keys, or internal state. Check setup, helper
functions, instrumentation, and success tests as well as the main attack path.
Each such read must be absent from the claimed attacker computation or declared
as a scoped cheat. State what the code demonstrates under that scope; a secret
read used to verify an experiment does not by itself demonstrate key recovery
without that read.

Attack families change which one dominates as parameters move. Measured on a UOV
sweep at q=256, n=round(2.5m), `memory_access=0`: the cheapest family is
DirectAttack up to m=40, WedgeAttack from m=44, and IntersectionAttack from
m=68. So a review of "the attack cost" that considers only the family a paper
happens to discuss can understate by 8–10 bits, growing with parameter size.

The same sweep is also a caution against over-reading a crossover: at m=76–80
the Intersection/Wedge gap is **0.4 and 0.8 bits**, which is a tie, and calling
it a regime change would be reading structure into rounding. It becomes real at
m=84 (4.8 bits).

## Structure, not vocabulary

Attacks transfer along mathematical structure, not name similarity. "Extends to"
requires an argument that the required structure is present.

Both directions of this inference are unsafe:

- A quotient ring `F_q[x]/(f)` with `f` irreducible **is** a field extension and
  admits subfield descent.
- A non-field ring may still **contain** an exploitable field: `M_l(F_q)` embeds
  `F_{q^l}`, and SNOVA is attacked through exactly that (ePrint 2024/1374). So
  "it is a matrix ring, not a field, therefore safe" is a non-sequitur — this
  exact inference was made on this project and later refuted.

Also distinguish a **descent** from a **lift**. LUOV's attack descends to a
pre-existing subfield the designer put there; SNOVA's manufactures an extension
by passing to a splitting field. They imply different design-time checks and
should not be merged into one claim.

## Security notions are not interchangeable

Check quantifier order, the adversary's oracle access, and what the reduction
loses. Flag:

- IND-CPA results stated as IND-CCA.
- A notion asserted without its game.
- A security level quoted as `2^n` where the construction caps it lower —
  Merkle–Damgård gives roughly `2^(n/2)` collision resistance, and message
  length erodes it further. SHA-256 over a 1 GB message is about 232 bits, not
  256.
- Hash-function implications stated as conditional when they are unconditional,
  or the reverse.

## Words that hide the reasoning

"Secure", "verified", "proven", and a bare security parameter with no model, no
attack set and no assumption are not conclusions. The honest form names what was
estimated, under which cost model, against which attack families, assuming what.

## The inference itself may be the defect

Every claim above can be individually true and the conclusion drawn from them
still invalid. Five steps that look like reasoning and are not:

- **"No attack was found, therefore it is secure."** → name the search scope and
  the analytical maturity. A negative is a claim about the search.
- **"The attack reaches most rounds, therefore it is nearly broken."** → compare
  attack model, work factor, target object and scaling. Round count alone says
  nothing.
- **"It has a proof, therefore it is secure."** → state the theorem, assumptions,
  reduction loss and model, and what the proof does not cover.
- **"Fewer published attacks, therefore stronger."** → paper count measures
  attention, not resistance. A scheme nobody studied has no attacks against it.
- **"A distinguisher is a break."** → name the property violated and show a
  consequence for a claimed game before using break vocabulary.

They are listed inline because **the current reviewer may have no way to open a file**, and
these are the rows it most needs. `reference/invalid-inferences.md` carries the
full treatment, why the first one recurs here specifically, and the three rows
deliberately left out as outside this workbench's scope.

## Parameter provenance

Where did `n`, `m`, `q` or the security level come from? Parameters recalled
from memory are wrong often enough to matter, and a wrong tuple silently
invalidates every number computed from it. Parameters presented as a scheme's
official values need a source; parameters explicitly labelled a sweep or
unverified are fine as they stand.

## Classical and quantum are different claims

Check which is being made, and whether a quantum speedup has been applied to an
attack that does not admit one.

## Contribution and originality

Before claiming a new result, use
[contribution assessment](../crypto-investigate/reference/contribution-assessment.md).
State the closest known result, the changed scope, and the additional reasoning
actually supplied. Distinguish routine applications and new evaluations from
substantive extensions or potentially new methods. Keep correctness, originality,
and significance separate; a useful parameter-specific finding need not be novel.

## If you can execute

Inspect the available computational environment and tool versions through
`crypto-investigate/reference/computation.md`. Do not assume SageMath or either estimator
is installed, and do not promise a runtime before measuring a representative
unit of work.

Two cautions from this project's own history. The estimator's runtime **roughly
doubles every +12 in m** for UOV — measured in one parallel sweep, 6 s at m=32
and 317 s at m=80 (solo, without contention, the same points are 4 s and 291 s;
quote one condition or the other, not a mixture) — so sweep in parallel and
longest-job-first, and do not extrapolate from a single small benchmark. And check
that the tool models the attack in question at all: `cryptographic_estimators`
ships DirectAttack, KipnisShamir, CollisionAttack, IntersectionAttack and
WedgeAttack for UOV, and **no subfield-descent model whatsoever**, so a sweep
run to settle a descent question answers an adjacent question instead.

## Reporting

Order findings by whether they change a security conclusion. Distinguish:

- **wrong** — the mathematics is incorrect;
- **unsupported** — may be true, but the stated basis does not establish it;
- **imprecise** — true, but stated in a way a reader would misapply.

Say plainly when a claim is correct. Confirming that an attack genuinely applies,
at a stated cost, under a named model, is a real result — a reviewer that only
ever objects is one nobody can act on.
