---
name: empirical-statistical-and-heuristic-claim-separation
description: "Interpret empirical, statistical, heuristic, and exact evidence in ordinary mathematical research. Distinguish exploratory observations from confirmation, quantify uncertainty, and preserve model and sampling assumptions. Formal proof work is optional."
metadata:
  version: "0.1.0"
  display-name: "Empirical, Statistical, and Heuristic Claim Separation"
  category: "certified-computation"
  tags: "evidence, statistics, heuristic, experiment, claim-discipline"
  requires: "experimental or estimator result, target claim, sampling/model assumptions"
  produces: "evidence classification, confidence/uncertainty report, formalizable subclaims, appropriate conclusion language"
  optional: "true"
  namespace: "formal"
---

# Empirical, Statistical, and Heuristic Claim Separation

## Purpose

Interpret observations and uncertainty at the strength they support. Read
[research stages](references/research-stages.md) for exploration, selection,
confirmation, zero-event limits, and inconclusive results.

## Use this skill when

Use this skill when a cryptanalysis project mixes simulations, Monte Carlo counts, performance measurements, lattice estimators, random-permutation heuristics, numerical correlations, and formal or exact claims.

## Ordinary research route

Do not use it to obstruct ordinary experimental cryptanalysis. Its purpose is to label evidence accurately and identify small high-value proof obligations, not to demand that every measurement become a theorem.

## Optional entry contract

**Inputs**
- experimental or estimator result
- target claim
- sampling/model assumptions

**Expected products**
- evidence classification
- confidence/uncertainty report
- formalizable subclaims
- appropriate conclusion language

Use this route whenever the statistical question warrants it, without entering
FORMALIZE mode. The historical formal-pack namespace is a packaging label, not
a prerequisite. A request about evidence does not require a proof-assistant plan.

## Operating procedure

1. Write the strongest desired conclusion and list each supporting item as derivation, checked witness, exhaustive computation, certified computation, formal theorem, statistical estimate, benchmark, heuristic model, or expert judgment.
2. For experiments, record population, sampling design, keys/instances, seeds, exclusions, censoring/timeouts, stopping rules, multiple testing, and the exact observed statistic.
3. Compute suitable confidence intervals or posterior/likelihood summaries and report zero-event upper bounds correctly; do not equate no observed failures with probability zero.
4. For performance and attack estimates, separate algorithmic operation counts, implementation measurements, hardware/model assumptions, extrapolation, and asymptotic terms.
5. For lattice, random-permutation, Markov, independence, or Gaussian heuristics, state where each assumption enters and test sensitivity to plausible alternatives.
6. When useful for the requested assurance, identify an optional exact or formal subclaim. Otherwise complete the statistical interpretation without creating a formalization task.
7. Use replication, holdout instances, independent implementations, and adversarial controls to reduce ordinary scientific error.
8. Choose calibrated conclusion language and evidence status. Preserve contradictions and negative results rather than averaging them away.
9. Publish raw/aggregated data provenance, analysis code, uncertainty, assumptions, and optional formal follow-up tasks.

## Output contract

- A claim-to-evidence table with explicit evidence classes.
- Statistical uncertainty and estimator-assumption report.
- Reproducible experiment/benchmark manifest.
- Optional exact or formal subclaims only when they add relevant assurance.

## Non-negotiable guardrails

- No observed event is not impossibility.
- An estimator is not a certified lower bound unless its model and computation are proved.
- Benchmarks are platform- and implementation-specific.
- Do not downplay valuable empirical evidence merely because it is not formal.

## Related formal skills

- `formalization-value-and-scope-triage`
- `exact-probability-counting-and-tail-bound-certification`

## Related cryptanalysis skills in this pack (optional)

- `public-key-evidence-synthesis-and-research-backlog`
- `symmetric-evidence-synthesis-and-research-backlog`

## Associated primary references

- **ARB** — [Arb: Arbitrary-Precision Ball Arithmetic](https://arblib.org/) (2026) — Arb project. `official-project`.
- **MPFR** — [GNU MPFR](https://www.mpfr.org/) (2026) — GNU MPFR project. `official-project`.
- **FPLLL-REPO** — [fplll](https://github.com/fplll/fplll) (2026) — fplll project. `official-repository`.
- **SHANNON26** — [ShannonProver: Towards Automating Formal Cryptographic Proofs](https://arxiv.org/abs/2607.02847) (2026) — Yiping Ma et al.. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
