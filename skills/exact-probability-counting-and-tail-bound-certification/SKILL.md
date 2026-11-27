---
name: exact-probability-counting-and-tail-bound-certification
description: "Derives and checks exact probabilities, combinatorial counts, statistical distances, tail bounds, union bounds, and failure probabilities without silently replacing dependent structure by independence or floating approximations."
metadata:
  version: "0.1.0"
  display-name: "Exact Probability, Counting, and Tail-Bound Certification"
  category: "certified-computation"
  tags: "probability, counting, tail-bound, statistical-distance, failure-probability"
  requires: "probabilistic claim, sample space/distribution, events and parameter ranges"
  produces: "exact or rigorous bound, derivation/proof, numerical enclosure, assumption report"
  optional: "true"
  namespace: "formal"
---

# Exact Probability, Counting, and Tail-Bound Certification

## Purpose

Derives and checks exact probabilities, combinatorial counts, statistical distances, tail bounds, union bounds, and failure probabilities without silently replacing dependent structure by independence or floating approximations.

## Use this skill when

Use this skill when a cryptographic argument depends on exact combinatorial probability, decryption/signing failure, rejection sampling, collision terms, bad events, data complexity, or a security reduction’s concrete loss.

## Do not invoke automatically

Do not formalize every empirical success rate. Use this when an exact or certified bound changes the conclusion, dependence is subtle, or a claimed exponent must be trusted beyond simulation.

## Optional entry contract

**Inputs**
- probabilistic claim
- sample space/distribution
- events and parameter ranges

**Expected products**
- exact or rigorous bound
- derivation/proof
- numerical enclosure
- assumption report

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Define the probability space, random variables, conditioning, support, independence/dependence assumptions, and exact event in mathematical notation and executable form.
2. Derive exact counts or rational expressions where feasible. Use dynamic programming, generating functions, recurrences, convolution, inclusion–exclusion, or exhaustive enumeration with proved coverage.
3. For inequalities, identify every bound and direction: union, Markov, Chebyshev, Chernoff/Hoeffding, martingale, Gaussian/subgaussian approximation, or problem-specific combinatorial lemma.
4. Treat correlations, reuse, conditioning, rejection, adaptive queries, and key-dependent distributions explicitly. Do not multiply marginal probabilities without justification.
5. Use Lean/Rocq/Isabelle for reusable theorems or exact rationals, and Arb/MPFR for rigorously rounded evaluation of large expressions. Record approximation error and monotonicity.
6. Cross-check reduced parameters by exact enumeration and large parameters by independent implementations. Test boundary parameters and asymptotic-to-concrete transitions.
7. For empirical inputs, propagate confidence intervals or uncertainty rather than inserting point estimates as exact constants.
8. Connect the bound to the final cryptographic claim, including number of users/queries, repetitions, amplification, verification, and failure handling.
9. Publish formulas, proof/certificate, rigorous numerical enclosure, parameter table, and all independence/heuristic assumptions.

## Output contract

- An exact expression or rigorous one-sided interval for each parameter set.
- A derivation or machine-checked theorem for the bound.
- Reduced-instance enumeration and independent numerical cross-checks.
- An assumption and sensitivity report tied to the security/attack conclusion.

## Non-negotiable guardrails

- Independence and identical distribution must be established, not inferred from notation.
- Floating-point exponent output is not a rigorous probability bound without directed error control.
- Union bounds may be valid but too loose; report both validity and usefulness.
- Empirical estimates and exact failure bounds must remain distinct.

## Related formal skills

- `lean-probability-combinatorics-and-bounds`
- `floating-point-and-rounding-error-verification`

## Related cryptanalysis skills in this pack (optional)

- `decryption-failure-and-reaction-analysis`
- `symmetric-attack-complexity-and-success-auditor`

## Associated primary references

- **MATHLIB-DOCS** — [Mathlib 4 Documentation](https://leanprover-community.github.io/mathlib4_docs/) (2026) — Lean community. `official-documentation`.
- **CRYPTHOL** — [CryptHOL](https://isa-afp.org/entries/CryptHOL.html) (2026) — Andreas Lochbihler et al.. `formal-development`.
- **ARB** — [Arb: Arbitrary-Precision Ball Arithmetic](https://arblib.org/) (2026) — Arb project. `official-project`.
- **MPFR** — [GNU MPFR](https://www.mpfr.org/) (2026) — GNU MPFR project. `official-project`.
- **FLOCQ** — [Flocq](https://flocq.gitlabpages.inria.fr/) (2026) — Inria. `official-project`.

Bundled source metadata is in `references/REFERENCES.md`.
