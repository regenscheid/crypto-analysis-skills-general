# Adversary model and proof models

> Part of `crypto-analyze-paper`'s security-definitions reference. The framing that
> governs every file here — including the rule that these are **obligations to
> discharge, not prose to cite** — is in [`README.md`](README.md), and the
> shared advantage/query conventions and proof models are in
> [`conventions.md`](conventions.md). Read those first.

## Adversary model conventions

**Advantage.** For a decision game with a bit *b*, `Adv = |2·Pr[b' = b] − 1|`
equivalently `|Pr[b'=1|b=1] − Pr[b'=1|b=0]|`. For a search/forgery game,
`Adv = Pr[A wins]`. The two decision-game forms above are **identically equal**
when b is uniform: Pr[b'=b] = ½p₁ + ½(1−p₀), so 2·Pr[b'=b] − 1 = p₁ − p₀. The
split that *does* cost a factor of 2 is `|2·Pr[b'=b] − 1|` versus
`|Pr[b'=b] − ½|` — check which is in use before comparing two papers' numbers.
Use the signed form inside hybrid arguments, where terms must telescope; take
absolute values only at the end.

**Concrete vs asymptotic.** A concrete bound is `Adv ≤ f(q, t, ε)` with explicit
q (queries), t (time). An asymptotic claim is "negligible in λ". PQC submissions
are concrete; textbook reductions are often asymptotic. **A concrete claim cannot
be checked against an asymptotic proof**, and this substitution is a real review
finding.

**Query budgets.** Any oracle-access notion is parameterised by how many queries
the adversary may make. A bound that omits q_H, q_D or q_S is incomplete, not
merely terse. Dropping a query factor can change the concrete claim.

---

## Proof models — always state which

| Model | Assumption | What it costs |
|---|---|---|
| **Standard** | none beyond the hardness assumption | strongest; hardest to achieve |
| **ROM** | hash modelled as a random oracle the adversary queries | uninstantiable in general; a ROM proof is heuristic evidence, not a theorem about the deployed scheme |
| **QROM** | as ROM, but the adversary queries **in superposition** | the relevant model for post-quantum claims |

**Why QROM is not a footnote for PQC.** A ROM proof does not transfer to a
quantum adversary: standard ROM technique relies on the reduction *observing*
and *reprogramming* queries, and a superposition query cannot be read without
disturbing it ([2010/428](https://eprint.iacr.org/2010/428), Boneh, Dagdelen,
Fischlin, Lehmann, Schaffner, Zhandry). A post-quantum scheme proved only in the
ROM has an **unremarked gap**, and detecting that is a core `crypto-analyze-paper` job.

**Obligation whenever a ROM/QROM proof appears:**
- [ ] Model stated explicitly, not inferred from context
- [ ] If PQC and ROM-only: is the QROM gap acknowledged, or silently ignored?
- [ ] Reduction loss stated — tightness in the QROM is frequently worse

---
