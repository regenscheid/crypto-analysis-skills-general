---
name: impossible-differential-and-zero-correlation-analysis
description: "Construct exact impossible differentials and zero-correlation linear properties of symmetric primitives and evaluate elimination and statistical key-recovery attacks. Use when forward and backward propagation may contradict or a hull may have zero correlation."
metadata:
  version: "0.1"
  display-name: "Impossible Differential and Zero-Correlation Analysis"
  tags: "impossible-differential, zero-correlation, miss-in-the-middle, key-elimination"
  requires: "design-assumption-graph, claim-model, round-scope"
  produces: "impossible-or-zero-correlation-records, proof-obligations, recovery-plan"
---

# Impossible Differential and Zero-Correlation Analysis

## Use this skill when

Forward and backward propagation sets may contradict, deterministic diffusion creates unreachable transitions, or a linear hull may have provably zero correlation over a key class.

## Operating procedure

1. **Choose the property type.** Keep impossible differential and zero-correlation linear analysis distinct. The former asserts an input/output difference pair cannot occur; the latter asserts a correlation is exactly zero under stated conditions.
2. **Propagate forward and backward sets.** Use exact or sound set-valued propagation from both boundaries. Record all truncation/relaxation and whether it preserves impossibility.
3. **Identify the contradiction.** State the exact middle variable/property that cannot simultaneously satisfy the forward and backward conditions. A failed solver search is not a proof of impossibility.
4. **Prove scope and key dependence.** Determine whether the property holds for every key, an average, a weak-key subset, independent round keys, or only a simplified schedule.
5. **Search systematically.** Use exact SAT/SMT/CP or validated MILP models, symmetry reductions, and exhaustive small-round checks. For infeasibility retain certificates when available.
6. **Design key elimination for impossible differentials.** Add boundary rounds, derive guessed subkey material, calculate probability a wrong key survives each structure, dependencies across pairs, number of surviving candidates, and final verification.
7. **Design statistical tests for zero correlation.** Select multidimensional/capacity/chi-square-style statistics as appropriate; derive right- and wrong-key distributions, data, degrees of freedom, ranking, and false positives.
8. **Enforce data feasibility.** Count unique chosen inputs, structures, ciphertext requirements, adaptive queries, and codebook limits.
9. **Validate positive and negative cases.** Exhaustively confirm impossibility on reduced instances, test deliberately possible endpoints, and validate key-ranking distributions over multiple keys.
10. **State exactly what is proved.** Separate an exact core property from heuristic boundary extension or statistical assumptions.

## Output contract

For each result include:

- property type and exact endpoints/masks;
- forward/backward propagation sets;
- contradiction or zero-correlation proof;
- key-schedule/key-class scope;
- solver/exhaustive validation and certificate status;
- boundary extension, filtering/ranking, and verification;
- full resources and success;
- exact claim/model impact.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `BBS99-IMP`
- `BLNW12-ZC`
- `BR14-ZC`
- `SHW14-AUTO`
- `MM00-SAT`

Full records are bundled in `references/REFERENCES.md`.
