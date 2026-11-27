---
name: distinguisher-to-key-recovery-extension
description: "Extend a symmetric distinguisher or structural property into key or state recovery with explicit round boundaries, filtering, ranking, false positives and verification. Use when a property exists but the claim concerns key recovery or full rounds."
metadata:
  version: "0.1"
  display-name: "Distinguisher to Key/State Recovery Extension"
  tags: "key-recovery, state-recovery, round-extension, filtering"
  requires: "distinguisher-or-property, design-graph, target-model"
  produces: "extension-plan, recovery-attack-record, complexity-derivation"
---

# Distinguisher to Key/State Recovery Extension

## Use this skill when

A differential, linear, integral, zero-correlation, impossible, boomerang, algebraic, or other property exists but the security claim concerns key/state recovery or full-round use.

## Operating procedure

1. **Freeze the core distinguisher.** Record exact input/output conditions, covered rounds/phases, probability/correlation/statistic, data structure, success, and independence assumptions.
2. **Choose extension boundaries.** Enumerate forward and backward extensions separately. Identify which state bits must be computed, which subkey/state bits influence them, and where diffusion makes partial computation impossible or expensive.
3. **Minimize guessed material.** Use partial encryption/decryption, equivalent subkeys, key-schedule relations, partial sums, meet-in-the-middle cuts, early abort, neutral bits, or key bridging. Prove which guessed bits are sufficient.
4. **Design data structures.** Specify pairs, quartets, structures, chosen sets, counters, or linear samples. Account for duplicate data, codebook limits, adaptive selection, and data reuse across key guesses.
5. **Derive filtering and ranking.** For each stage calculate expected right/wrong-key distributions, surviving candidates, false positives, signal-to-noise ratio, and the statistic used to rank candidates.
6. **Account for dependencies.** Key guesses, trails, samples, and counters often share data. Do not multiply probabilities or variances under unjustified independence assumptions.
7. **Include verification.** State how remaining key/state candidates are checked, number of pairs required, equivalent-key issues, and verification cost. A partial subkey rank is not full recovery.
8. **Optimize the attack frontier.** Compare alternative cuts and guess orders across time, data, memory, and success. Do not optimize only the headline time exponent.
9. **Validate progressively.** Use reduced/toy instances, known-key experiments, wrong-key randomization, and end-to-end recovery trials. Report distributions and confidence intervals, not only successful examples.
10. **Check the claimed model.** Verify that the extension’s chosen data, decryption, related keys/tweaks, resets, or Q2 queries are allowed by the claim row.

## Output contract

Produce an extension record containing:

- core distinguisher and exact round placement;
- forward/backward operations and guessed variables;
- data structures and pseudocode;
- per-stage filtering, candidate counts, false-positive model, and ranking statistic;
- key-schedule/state reconstruction and final verification;
- complete data/time/memory/preprocessing/success derivation;
- experimental validation and falsification criteria;
- explicit statement of what is and is not recovered.

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
- `BBS99-IMP`
- `KW02-INTEGRAL`
- `WAG99-BOOM`
- `SHW14-AUTO`

Full records are bundled in `references/REFERENCES.md`.
