---
name: arx-differential-rotational-rx-analysis
description: "Analyze addition-rotation-XOR (ARX) designs with carry-aware differential models, rotational and RX properties, constants and key schedules. Use when modular addition, rotation and XOR dominate, or when XOR-only trail models miss carries."
metadata:
  version: "0.1"
  display-name: "ARX Differential, Rotational, and RX Analysis"
  tags: "ARX, rotational, RX, modular-addition"
  requires: "design-assumption-graph, claim-model, round-scope"
  produces: "arx-attack-records, carry-model, solver-artifacts, validation-plan"
---

# ARX Differential, Rotational, and RX Analysis

## Use this skill when

The target is dominated by modular addition/subtraction, rotation, and XOR, or when XOR-only trail models fail to capture carries and rotational structure.

## Operating procedure

1. **Define exact word semantics.** Record word size, modular arithmetic, rotation constants/directions, endian/bit numbering, constants, key additions, and whether operations mix word sizes.
2. **Choose relation domains.** Analyze XOR differences, modular differences, signed differences, rotational pairs, RX differences, or mixed relations. State what each relation preserves through XOR, rotation, and addition.
3. **Model addition exactly.** Use carry-state dynamic programming, exact bit-vector SAT/SMT, or validated transition formulas. Include simultaneous/additive correlations when combining differential and linear methods.
4. **Account for constants.** Round constants, counters, and asymmetric rotations can destroy rotational symmetry. Model their exact effect rather than treating them as random penalties.
5. **Account for key schedules.** Analyze related rotations/differences through the schedule and whether random-key averaging masks strong or weak key classes.
6. **Search trails and clusters.** Use SAT/SMT/MIQCP, dynamic programming, branch-and-bound, or specialized ARX search. Validate every witness and aggregate compatible trails when making differential claims.
7. **Explore neutral bits and local collisions.** Prove which message/key/state modifications preserve earlier conditions and calculate downstream impact and success.
8. **Consider hybrids.** Differential-linear, boomerang, meet-in-the-middle, rotational rebound, and algebraic constraints may exploit ARX structure better than a pure trail.
9. **Validate carries explicitly.** Instrument per-bit carries and test predicted probabilities over many random values and keys. Include null difference/rotation controls and boundary word cases.
10. **Audit the model.** Check independence across additions, reuse of state words, key dependence, data feasibility, solver relaxations, and exact claim scope.

## Output contract

Provide:

- relation domain and exact operation semantics;
- carry/rotation transition model with validation;
- trails, clusters, constants, and key-schedule effects;
- weak-key or related-key conditions if any;
- hybrid/extension plan;
- direct carry-level experiments;
- complete resources/success and generic comparison;
- exact rounds/model/claim impact.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `KN10-ROT`
- `LM01-ADD`
- `MWGP11-MILP`
- `LH94-DL`
- `CID18-BCT`

Full records are bundled in `references/REFERENCES.md`.
