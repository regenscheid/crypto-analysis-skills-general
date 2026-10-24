---
name: public-key-attack-complexity-and-success-auditor
description: "Recomputes end-to-end resources and success probability for public-key attacks, exposing omitted preprocessing, oracle acquisition, filtering, false positives, verification, estimator assumptions, and model mismatches."
metadata:
  version: "0.1"
  display-name: "Attack Complexity and Success Auditor"
  tags: "complexity, success-probability, cost-model, audit"
  requires: "attack-record, claim-row, generic-baseline"
  produces: "audited-cost-record, success-derivation, sensitivity-analysis"
---

# Attack Complexity and Success Auditor

## Use this skill when

An attack or security estimate is being compared with an advertised security level or generic baseline.

## Assigned scope

Apply this procedure to the assigned quantitative or empirical claim. Being
listed as a related skill or citing a published result does not assign a fresh
cost audit or reproduction. Retain rigorous checks when that is the task. Reuse
compatible evidence and identify the changed dependency behind a repeated check;
see [paper use and verification](../crypto-investigate/reference/paper-use-and-verification.md).
A mathematical proposal may state unresolved cost or empirical obligations
without completing this workflow.

## Operating procedure

1. Reconstruct the complete algorithm from input acquisition through candidate generation, filtering, recovery/forgery, and final verification.
2. Inventory data and oracle costs: public keys, ciphertexts, decapsulation attempts, signatures, chosen messages, protocol sessions, malformed inputs, and adaptive rounds. Distinguish available data from generated offline samples.
3. Count arithmetic operations in native units and derive bit complexity with operand sizes and algorithms. Record memory, bandwidth, storage, communication, and parallel depth.
4. Separate one-time preprocessing, per-target work, per-key work, online latency, and amortized cost. Verify whether precomputation actually transfers across users or standardized parameters.
5. Recompute success probability from all events: weak keys, favorable instances, decoding or decryption failures, collision probability, lattice/solver success, sampling/rejection, oracle noise, false positives, and verification.
6. Account for repetitions, parameter tuning, failed branches, candidate lists, post-processing, and the cost of recognizing success.
7. Audit estimator and solver evidence: version, commit, flags, cost model, pruning/sieving assumptions, memory convention, parallelism, and interpolation/extrapolation.
8. For quantum attacks, report query complexity, logical gates, depth, logical qubits, qRAM or coherent-memory assumptions, state preparation, error correction, and physical estimates separately.
9. Compare against the exact claim and baseline at equal success probability and in compatible units. Produce sensitivity ranges when conventions are disputed.
10. Label results as asymptotic, estimated, implemented, or experimentally demonstrated and state the largest validated instance.
11. When code exists, separate counted algorithmic operations from measured runtime and resource use. Name the implementation, instance, hardware, and measurement method; state which portions of the end-to-end attack the measurements cover.

## Output contract

- An end-to-end cost breakdown with native units and normalized comparisons.
- Counted and measured costs reported separately when implementation code exists.
- A success-probability derivation and false-positive/verification analysis.
- A preprocessing/amortization and parallelism audit.
- Sensitivity ranges and a list of unsupported cost assumptions.

## Non-negotiable guardrails

- Bind every conclusion to the exact artifact, version, parameter set, key format, and security game.
- Distinguish a faster algorithm for an underlying mathematical problem from a complete attack on the cryptosystem, and distinguish a proof gap from an exploit.
- Never present a weak-key, malformed-input, related-key, multi-target, decryption-oracle, leakage, fault, or quantum result as a standard-model full-scheme break without that qualification.
- For a new or independently verified quantitative conclusion, account for the relevant data, oracle queries, arithmetic/bit operations, memory, preprocessing, communication, verification, parallel depth, and success probability in explicit units. Preserve attributed published quantities as source claims; reuse unchanged checked inputs and recompute affected dependencies.
- State the cost model, implementation assumptions, and estimator version; a single headline exponent is not a reproducible security estimate.
- Preserve failed attacks, rebuttals, corrections, withdrawn claims, and source-version chronology in the evidence ledger.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not established by a proof, derivation, experiment, validated implementation, or cited source.

## Associated references

- `LL93-NFS`
- `VOW99-PARALLEL`
- `GE21-RSA`
- `LATTICE-ESTIMATOR`
- `ESSER22-ISD`
- `F4-99`
- `DELFS16-ISO`

Full records are bundled in `references/REFERENCES.md`.
