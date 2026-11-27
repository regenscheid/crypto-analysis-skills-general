---
name: floating-point-and-rounding-error-verification
description: "Builds rigorous models and proofs for floating-point cryptographic computations, rounding modes, approximation error, interval bounds, exceptional behavior, and accumulated numerical effects."
metadata:
  version: "0.1.0"
  display-name: "Floating-Point and Rounding-Error Verification"
  category: "implementation-verification"
  tags: "floating-point, rounding, ieee-754, gappa, flocq, interval"
  requires: "floating-point algorithm, precision and rounding specification, claimed accuracy/safety property"
  produces: "rigorous error bounds, exception and range analysis, reference implementation, replayable numerical proof"
  optional: "true"
  namespace: "formal"
---

# Floating-Point and Rounding-Error Verification

## Purpose

Builds rigorous models and proofs for floating-point cryptographic computations, rounding modes, approximation error, interval bounds, exceptional behavior, and accumulated numerical effects.

## Use this skill when

Use this skill when cryptographic correctness, sampling, decoding, signature generation, rejection behavior, or a security argument depends materially on IEEE-754 operations or other finite-precision approximations.

## Do not invoke automatically

Do not replace empirical high-precision comparison with a theorem unless the complete input domain and operation semantics are covered. Conversely, do not demand formal numerics when ordinary measurement is sufficient for an exploratory correlation study.

## Optional entry contract

**Inputs**
- floating-point algorithm
- precision and rounding specification
- claimed accuracy/safety property

**Expected products**
- rigorous error bounds
- exception and range analysis
- reference implementation
- replayable numerical proof

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Freeze the algorithm, source/compiler settings, target floating-point format, rounding mode, contraction/FMA behavior, excess precision, subnormal handling, exceptions, math-library functions, and permitted nondeterminism.
2. Derive an exact real-number or integer reference specification independent of the floating-point implementation. State the desired property: absolute/relative error, interval containment, sign stability, decision equivalence, distribution distance, or failure bound.
3. Model each operation under IEEE-754 or the actual target semantics. Include ties, signed zero, infinities, NaNs, underflow, overflow, and fused versus unfused evaluation where reachable.
4. Use Flocq for foundational IEEE reasoning, Gappa for automated error/range proofs, MPFR as a correctly rounded high-precision reference, and Arb/ball arithmetic for rigorous interval enclosures. State which parts are formally checked versus trusted computation.
5. Prove or rigorously bound input ranges before error propagation. Partition the domain around discontinuities, rounding thresholds, rejection boundaries, and conditionally executed approximations.
6. Analyze correlated and reused errors separately from independent-error heuristics. For randomized algorithms, connect deterministic numerical bounds to distributional or failure-probability reasoning explicitly.
7. Generate boundary and adversarial test cases with MPFR/interval references and compare across compilers and architectures. Preserve exact inputs causing maximal or unexpected error.
8. When the full domain is infeasible, report a certified subdomain and an empirical remainder rather than extrapolating the proof.
9. Publish mathematical specification, operation semantics, proof scripts/certificates, reference computations, compiler assumptions, and decision-level implications.

## Output contract

- A formal or rigorous numerical model with pinned IEEE/compiler semantics.
- Certified error/range/decision-stability bounds and exceptional-case analysis.
- High-precision boundary test corpus and independent reference outputs.
- A statement separating proved bounds, exhaustive checks, and empirical observations.

## Non-negotiable guardrails

- Do not assume independent or unbiased rounding errors without evidence.
- High precision reduces reference error but is not itself a proof of the entire input domain.
- Compiler reassociation, FMA contraction, fast-math, and extended precision can change the model.
- An error bound must be connected to the cryptographic acceptance/failure/security claim, not reported in isolation.

## Related formal skills

- `exact-probability-counting-and-tail-bound-certification`
- `empirical-statistical-and-heuristic-claim-separation`

## Related cryptanalysis skills in this pack (optional)

- `decryption-failure-and-reaction-analysis`
- `ntru-and-falcon-analysis`

## Associated primary references

- **IEEE754** — [IEEE Standard for Floating-Point Arithmetic](https://standards.ieee.org/ieee/754/6210/) (2019) — IEEE. `standard`.
- **MPFR** — [GNU MPFR](https://www.mpfr.org/) (2026) — GNU MPFR project. `official-project`.
- **GAPPA** — [Gappa](https://gappa.gitlabpages.inria.fr/) (2026) — Inria. `official-project`.
- **FLOCQ** — [Flocq](https://flocq.gitlabpages.inria.fr/) (2026) — Inria. `official-project`.
- **ARB** — [Arb: Arbitrary-Precision Ball Arithmetic](https://arblib.org/) (2026) — Arb project. `official-project`.
- **FLINT** — [FLINT](https://flintlib.org/) (2026) — FLINT project. `official-project`.

Bundled source metadata is in `references/REFERENCES.md`.
