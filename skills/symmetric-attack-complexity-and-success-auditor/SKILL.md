---
name: symmetric-attack-complexity-and-success-auditor
description: "Recomputes an attack end to end, normalizes resource units, checks success and false positives, and compares it with the correct generic baseline and security claim. Use when: Before accepting, reporting, transferring, or comparing any cryptanalytic complexity. It is especially important for papers or agent outputs that quote one exponent without a complete derivation."
metadata:
  version: "0.1"
  display-name: "Attack Complexity and Success Auditor"
  tags: "complexity, success-probability, audit, reproducibility"
  requires: "attack-record, generic-baselines, claim-adversary-matrix"
  produces: "audited-attack-record, resource-ledger, error-report"
---

# Attack Complexity and Success Auditor

## Use this skill when

Before accepting, reporting, transferring, or comparing any cryptanalytic complexity. It is especially important for papers or agent outputs that quote one exponent without a complete derivation.

## Assigned scope

Apply this procedure to the assigned quantitative or empirical claim. Being
listed as a related skill or citing a published result does not assign a fresh
cost audit or reproduction. Retain rigorous checks when that is the task. Reuse
compatible evidence and identify the changed dependency behind a repeated check;
see [paper use and verification](../crypto-investigate/reference/paper-use-and-verification.md).
A mathematical proposal may state unresolved cost or empirical obligations
without completing this workflow.

## Operating procedure

1. **Reconstruct the attack algorithm.** Convert prose into executable pseudocode or a precise staged algorithm. Identify loops, tables, guesses, filters, repetitions, and verification.
2. **Count data correctly.** Distinguish unique chosen/known inputs, total oracle calls, pairs/quartets derived from a structure, adaptive rounds, rejected samples, and multi-user aggregation. Enforce domain/codebook caps.
3. **Count time in explicit units.** Name the primitive, round, S-box, hash call, solver operation, or memory operation. Convert partial-round work to primitive equivalents with stated assumptions.
4. **Count memory and I/O.** Give entries, bits/bytes/words per entry, indexing overhead, access pattern, external-memory traffic, table construction, and collision handling. A nominal table size may not reflect usable RAM or bandwidth.
5. **Separate phases.** Report preprocessing, per-target online work, amortization population, data collection, solving, ranking, and verification. State whether preprocessing depends on the key, primitive, constants, or parameter set.
6. **Recompute success.** Derive right-key/property survival, wrong-key distribution, false positives, repeated-trial amplification, and confidence intervals. Include weak-key fraction and probability of obtaining required structures.
7. **Audit probabilistic assumptions.** Identify independence, Markov, normal/Poisson/binomial approximations, dominant-trail assumptions, random wrong-key behavior, and solver sampling bias. Test or bound the assumptions where feasible.
8. **Audit parallelism.** Distinguish total work, wall-clock depth, processors/qubits, communication, shared memory, and serial bottlenecks. Do not present perfect parallelism as free.
9. **Compare with generic baselines.** Compare the entire resource vector and success, not just time. State whether the attack is academically non-generic, concretely feasible, or dominated by a generic attack.
10. **Check claim impact.** Identify the exact claim row and scope violated. If the attack uses a stronger model or fewer rounds, state that prominently.
11. **Separate counted from measured cost when code exists.** Report operation counts from the algorithm separately from measured runtime and resource use. Name the implementation, instance, hardware, and measurement method; explain what the measurements do and do not validate about the full attack cost.

## Output contract

Return:

- a line-by-line or stage-by-stage resource ledger;
- counted and measured costs separately when implementation code exists;
- normalized data/time/memory/preprocessing/communication/verification values;
- success and false-positive derivation with assumptions;
- sensitivity analysis for the largest uncertainties;
- comparison with relevant generic frontiers;
- a list of corrected claims, omitted costs, unit mismatches, or infeasible data requirements;
- an audited conclusion with exact scope and confidence.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `HELL80-TMTO`
- `BS00-TMDTO`
- `BR-INTRO`
- `RS04-HASH`
- `GROVER96`
- `GLRS16`
- `SEL08-SUCCESS`
- `BGT11-SUCCESS`

Full records are bundled in `references/REFERENCES.md`.
