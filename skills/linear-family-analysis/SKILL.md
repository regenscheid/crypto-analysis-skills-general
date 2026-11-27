---
name: linear-family-analysis
description: "Analyze linear approximations, trails, hulls and multiple or multidimensional linear attacks on symmetric primitives with sign and dependency accounting. Use when operations show biased linear relations, diffusion allows low-weight masks, or published approximations exist."
metadata:
  version: "0.1"
  display-name: "Linear Family Analysis"
  tags: "linear-cryptanalysis, linear-hull, multidimensional, partial-sum"
  requires: "design-assumption-graph, claim-model, round-scope"
  produces: "linear-records, hull-analysis, ranking-model, validation-plan"
---

# Linear Family Analysis

## Use this skill when

The target’s Boolean or word operations exhibit biased linear relations, the diffusion layer permits low-weight masks, or literature provides useful approximations or zero-correlation structure.

## Operating procedure

1. **Define masks and inner products exactly.** State bit ordering, field/word representation, input/output/key masks, and whether approximations include plaintext, ciphertext, tweak, nonce, or round-key terms.
2. **Compute local correlations.** Use S-box LATs or exact component formulas. Track signed correlation rather than only absolute weight; for modular addition and ARX use exact or validated approximations.
3. **Search valid trails.** Model mask propagation, key schedule, constants, and round boundaries. Validate each trail directly and state whether weights are exact or lower bounds.
4. **Analyze linear hulls.** Aggregate trails with the same external masks, including signs, dependencies, and key-dependent effects. Do not infer hull correlation from the single best trail.
5. **Select the statistical method.** Distinguish Matsui-style single approximation, multiple approximations, multidimensional linear cryptanalysis, zero-correlation tests, or capacity-based combination. State the null and right-key distributions.
6. **Design key recovery.** Identify partial encryption/decryption, subkey bits, partial sums, counters, FFT/Walsh transforms, ranking statistic, expected key rank, and verification.
7. **Audit data reuse and dependence.** Samples, approximations, and counters may be correlated. Justify covariance assumptions or estimate them empirically.
8. **Handle signs and key dependence.** Explain whether signs are known, guessed, averaged, key-dependent, or eliminated by squaring/capacity. Test across many keys.
9. **Validate statistically.** Use wrong-key randomization, null masks, multiple keys, predeclared sample sizes, confidence intervals, and rank distributions.
10. **Compare the full frontier.** Include data, time, memory, number of approximations, preprocessing, success probability, and generic exhaustive recovery.

## Output contract

Report:

- exact masks and correlation convention;
- trail list and hull/cluster treatment;
- signed correlations and key dependence;
- statistical distinguisher or key-ranking procedure;
- sample/data derivation and covariance assumptions;
- partial-sum/guess complexity and verification;
- observed versus predicted distributions and key ranks;
- exact model, rounds, and claim impact.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `MAT93-LIN`
- `KR94-MULTILIN`
- `MWGP11-MILP`
- `BLNW12-ZC`
- `BR14-ZC`

Full records are bundled in `references/REFERENCES.md`.
