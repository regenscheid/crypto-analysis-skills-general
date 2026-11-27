---
name: lean-probability-combinatorics-and-bounds
description: "Formalizes finite probability spaces, counting arguments, expectations, statistical distance, combinatorial identities, and exact or analytic bounds needed by cryptographic correctness and attack analysis."
metadata:
  version: "0.1.0"
  display-name: "Lean Probability, Combinatorics, and Bounds"
  category: "lean"
  tags: "lean, probability, combinatorics, bounds"
  requires: "probabilistic or counting claim, distribution definitions, required precision"
  produces: "formal probability model, counting lemmas, exact or rigorous bound, assumption report"
  optional: "true"
  namespace: "formal"
---

# Lean Probability, Combinatorics, and Bounds

## Purpose

Formalizes finite probability spaces, counting arguments, expectations, statistical distance, combinatorial identities, and exact or analytic bounds needed by cryptographic correctness and attack analysis.

## Use this skill when

Use this skill for finite distributions, collision probabilities, decryption-failure events, success amplification, union bounds, sampling without replacement, binomial/hypergeometric counts, and exact attack success calculations.

## Do not invoke automatically

Do not formalize a simulation-derived frequency as if it were the true probability. First identify whether the result is an exact finite count, analytic inequality, asymptotic estimate, or empirical confidence interval.

## Optional entry contract

**Inputs**
- probabilistic or counting claim
- distribution definitions
- required precision

**Expected products**
- formal probability model
- counting lemmas
- exact or rigorous bound
- assumption report

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Define the probability space and random variables explicitly, including independence, conditioning, support, subdistributions/failure, and adversarial choices. Avoid prose-only “uniform random” assumptions.
2. For finite spaces, prefer exact counting or rational probabilities when feasible. Prove the link from counts to the event probability rather than relying on floating-point summaries.
3. Decompose events into disjoint unions or controlled overlaps and state every union-bound, conditioning, and symmetry step. Check that bad events are measurable and cover the claimed failure.
4. Formalize independence only where justified by the sampling procedure. Key-derived cached values, shared randomness, rejection sampling, and transcript reuse often create dependencies.
5. Use mathlib probability and finite combinatorics libraries where mature; isolate missing analytic facts in reusable lemmas rather than importing informal estimates as axioms.
6. For tail bounds, state the exact hypotheses: boundedness, moment-generating function, sub-Gaussian parameter, martingale structure, or variance. Record whether constants are tight enough for the cryptographic claim.
7. Connect analytic bounds to concrete parameter arithmetic with exact rounding direction. Avoid binary floating-point evaluation in the final inequality unless its error is proved.
8. Validate formulas against exhaustive small cases and high-precision independent computations. Treat those checks as transcription/error detection.
9. Publish both the theorem and the residual modeling assumptions, especially independence, ideal distributions, estimator models, and omitted implementation behavior.

## Output contract

- A formal event/distribution model and exact quantifier scope.
- Counting identities or analytic bounds with hypotheses.
- Concrete parameter instantiations using exact arithmetic.
- A distinction among theorem, rigorous numerical bound, and empirical estimate.

## Non-negotiable guardrails

- Do not infer independence from repeated signatures or samples without analyzing shared state.
- Do not mix statistical distance, failure probability, and adversarial advantage without the appropriate triangle/conditioning argument.
- Do not round a security exponent in the favorable direction.
- If a required probability result is outside current library support, state the gap rather than axiomatizing the desired bound silently.

## Related formal skills

- `exact-probability-counting-and-tail-bound-certification`
- `floating-point-and-rounding-error-verification`

## Related cryptanalysis skills in this pack (optional)

- `decryption-failure-and-reaction-analysis`
- `symmetric-attack-complexity-and-success-auditor`

## Associated primary references

- **MATHLIB-DOCS** — [Mathlib 4 Documentation](https://leanprover-community.github.io/mathlib4_docs/) (2026) — Lean community. `official-documentation`.
- **MATHLIB-REPO** — [Mathlib 4](https://github.com/leanprover-community/mathlib4) (2026) — Lean community. `official-repository`.
- **EASYCRYPT11** — [EasyCrypt: Automated Reasoning for Security Proofs](https://eprint.iacr.org/2011/101) (2011) — Gilles Barthe et al.. `research-paper`.
- **ARB** — [Arb: Arbitrary-Precision Ball Arithmetic](https://arblib.org/) (2026) — Arb project. `official-project`.
- **MPFR** — [GNU MPFR](https://www.mpfr.org/) (2026) — GNU MPFR project. `official-project`.
- **MLKEM-EC24** — [Formally verifying Kyber Episode V: Machine-checked IND-CCA security and correctness of ML-KEM in EasyCrypt](https://eprint.iacr.org/2024/843) (2024) — José Bacelar Almeida et al.. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
