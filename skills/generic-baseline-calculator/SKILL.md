---
name: generic-baseline-calculator
description: "Compute exact generic and exhaustive-attack baselines for a symmetric security model so attacks are compared against the right target. Use before calling an attack faster than generic, and again when the model changes; public-key: generic-baseline-and-security-level-calculator."
metadata:
  version: "0.1"
  display-name: "Generic Baseline Calculator"
  tags: "complexity, generic-attacks, baselines, bounds"
  requires: "claim-adversary-matrix, target-parameters"
  produces: "generic-baselines, comparison-table, assumption-log"
---

# Generic Baseline Calculator

## Use this skill when

Before calling an attack non-generic, faster than brute force, practical, or security-reducing. Re-run it when the model, number of users, data allowance, nonce behavior, tag length, or quantum access changes.

## Operating procedure

1. **Select the claim row.** Baselines are property- and model-specific; do not reuse a single “security bits” number for every claim.
2. **Compute exhaustive search.** For key/state recovery, include success probability, number of known/chosen pairs needed for verification, false matches, equivalent keys, weak-key fraction, multi-target effects, and preprocessing amortization.
3. **Compute codebook and query saturation limits.** Check block/domain size, unique-input limits, and whether claimed data exceeds the available codebook or nonce space.
4. **Compute birthday-style baselines.** For collisions, tags, internal state/capacity, random functions/permutations, and multi-user aggregation, identify the relevant domain and range rather than applying a universal square-root rule.
5. **Compute generic forgery baselines.** Include tag length, verification attempts, transcript length, nonce collisions/reuse, multi-user factors, and construction-specific bounds.
6. **Compute preimage and second-preimage baselines.** Distinguish fixed-target, many-target, long-message, memory-assisted, and construction-specific generic attacks.
7. **Compute time-memory(-data) baselines.** State preprocessing, online time, memory, data, coverage, chain merges/collisions, and whether tables are key-, primitive-, or parameter-specific.
8. **Compute quantum baselines only under an explicit model.** Distinguish Q1/Q2, oracle-query count, logical depth, qubits, reversible-circuit cost, parallelization, and verification. Do not report only “half the key bits.”
9. **Normalize units.** Convert time to calls of a named primitive/round where possible; memory to bits/bytes/words plus access pattern; data to unique/adaptive oracle queries; preprocessing to an explicit amortization population.
10. **Compare candidate attacks.** Report whether the attack improves time, data, memory, or success over the relevant generic frontier. An attack that improves one coordinate while making another infeasible should not be reduced to a single exponent.

## Output contract

For each claim/model produce a table with:

- generic attack name and applicability conditions;
- formula and parameter substitution;
- data, time, memory, preprocessing, communication, and success;
- classical/Q1/Q2 status;
- codebook/domain caps and multi-user/multi-target factors;
- sensitivity to parameter changes;
- comparison rule to be used by every attack record.

Flag attacks whose quoted complexity is above a generic baseline, exceeds the domain, ignores verification, or shifts most cost into unreported preprocessing.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `BR-INTRO`
- `RS04-HASH`
- `HELL80-TMTO`
- `BS00-TMDTO`
- `GROVER96`
- `BHT97`
- `GLRS16`
- `NIST-38D`
- `ML15-MULTIKEY`
- `SEL08-SUCCESS`
- `BGT11-SUCCESS`

Full records are bundled in `references/REFERENCES.md`.
