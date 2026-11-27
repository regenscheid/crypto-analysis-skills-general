---
name: rebound-analysis
description: "Construct inbound-outbound (rebound) attacks on wide permutations and hash-like designs with explicit degrees of freedom, nonlinear matching and outbound probabilities. Use when a dense nonlinear middle can be solved with internal freedom between probabilistic differential parts."
metadata:
  version: "0.1"
  display-name: "Rebound Analysis"
  tags: "rebound, hash-cryptanalysis, permutation, inbound-outbound"
  requires: "design-assumption-graph, differential-candidates, hash-or-permutation-target"
  produces: "rebound-records, degrees-of-freedom-ledger, validation-plan"
---

# Rebound Analysis

## Use this skill when

A wide-trail permutation or compression function has a dense nonlinear middle region that can be solved using internal degrees of freedom, surrounded by probabilistic differential propagation.

## Operating procedure

1. **Define the target property.** Collision, semi-free-start collision, free-start collision, distinguisher, near-collision, preimage component, or permutation property. Keep construction-level and permutation-level claims separate.
2. **Choose inbound and outbound regions.** Identify the nonlinear middle core to solve exactly or with high probability and the outer propagation to pay probabilistically.
3. **Build local differential tables.** For S-box/SuperSbox layers derive compatible input/output differences, values, multiplicities, and key/constant effects.
4. **Maintain a degrees-of-freedom ledger.** Count independent state/message/key variables, constraints imposed at each matching stage, collisions between constraints, and expected number of solutions.
5. **Design the inbound solver.** Specify table lookups, matching order, message modification, neutral bytes/words, linear-system solving, and memory/I/O.
6. **Derive outbound probability.** Include complete differentials/clusters, dependencies, truncation, feedforward, padding, and construction boundary conditions.
7. **Connect to the actual hash construction.** Account for chaining values, message blocks, feedforward, initialization vectors, finalization, and whether the model grants free-start or semi-free-start control.
8. **Optimize without double counting.** Degrees of freedom used inbound cannot also be assumed free for outbound filtering unless proved independent.
9. **Validate each layer.** Test local tables, inbound solution counts, constraint rank, outbound frequencies, and end-to-end successes across seeds/keys/chaining values.
10. **Audit complete work.** Include failed inbound attempts, table construction, memory bandwidth, multiple blocks, message constraints, and verification.

## Output contract

Report:

- exact target property and construction model;
- inbound/outbound round split;
- nonlinear transition tables and matching algorithm;
- constraint/degrees-of-freedom ledger;
- outbound probability and dependencies;
- construction-level boundary handling;
- experiments and raw solution counts;
- full resources, success, and generic comparison.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `MRST09-REBOUND`
- `BS91-DIFF`
- `JOU04-MULTI`
- `KS05-2PRE`

Full records are bundled in `references/REFERENCES.md`.
