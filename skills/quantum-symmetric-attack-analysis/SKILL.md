---
name: quantum-symmetric-attack-analysis
description: "Formalize Q1/Q2 quantum access and evaluate Grover, collision, period-finding and hybrid quantum attacks on symmetric constructions with concrete oracle, depth, qubit and verification costs. Use when a claim invokes quantum security or structure may be exposed to quantum queries."
metadata:
  version: "0.1"
  display-name: "Quantum Symmetric Attack Analysis"
  tags: "quantum-cryptanalysis, Q1, Q2, Grover, Simon"
  requires: "claim-adversary-matrix, classical-attack-record, quantum-resource-model"
  produces: "quantum-attack-records, resource-estimate, model-comparison"
---

# Quantum Symmetric Attack Analysis

## Use this skill when

A security claim invokes “quantum security,” a classical attack may be accelerated quantumly, or a construction exposes algebraic/periodic structure to quantum queries.

## Operating procedure

1. **Choose the access model first.** Q1 permits classical online oracle queries with quantum offline computation; Q2 permits superposition queries to a coherent oracle. Treat offline-Simon-style precomputed quantum states, qRAM, and coherent access to public primitives as separate capabilities. Define which interfaces—encryption, decryption, related key, tweak, nonce, permutation—are classical or coherent.
2. **Specify the oracle circuit.** Include key schedule, rounds, memory lookups, inverse operations, comparisons, uncomputation, data loading, and whether external classical data can be queried coherently.
3. **Apply amplitude amplification carefully.** Identify the searched domain, number of marked items, predicate cost, success amplification, verification, and parallel strategy. A classical attack does not automatically receive a square-root speedup in every phase.
4. **Analyze collisions/preimages under the right model.** Distinguish query complexity from total gates, memory, depth, and classical output/storage. Account for multiple targets and construction constraints.
5. **Search for quantum period structure.** For Simon/period-finding-style attacks, distinguish direct Q2 access, Q1/offline-Simon constructions, and hybrids. Define the function, period/collision promise, noise or deviation from the promise, key/nonce/tweak relations, state-preparation cost, reusable quantum data, and postprocessing that recovers useful secret information.
6. **Quantize hybrid attacks explicitly.** For differential, linear, MITM, TMTO, or key recovery, identify which loops/searches are accelerated, data remains classical or quantum, memory model, and bottlenecks that are not accelerated.
7. **Estimate resources concretely.** Report oracle calls, logical gates, T/Toffoli count if available, logical depth, qubits, measurements, repetitions, classical memory/time, and error-correction assumptions separately.
8. **Audit parallelism and tradeoffs.** Distinguish total work from depth and processors. State limits of parallel Grover search and the effect of multiple users/targets.
9. **Compare with classical and generic quantum baselines.** Show whether structure improves over generic quantum search/collision algorithms and whether the result violates the advertised Q1 or Q2 claim.
10. **Avoid security-bit slogans.** Report a resource vector and model. Explain uncertainty from reversible implementation, data access, and fault-tolerant cost.

## Output contract

Provide:

- explicit Q1/Q2 game and coherent interfaces;
- oracle/predicate circuit description;
- algorithm and success derivation;
- logical queries/gates/depth/qubits plus classical resources;
- data-loading, memory, verification, and parallel assumptions;
- comparison with classical and generic quantum attacks;
- exact target/model/claim impact and implementation uncertainties.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `GROVER96`
- `BHT97`
- `KLLN16`
- `BHNS19-OFFSIMON`
- `GLRS16`

Full records are bundled in `references/REFERENCES.md`.
