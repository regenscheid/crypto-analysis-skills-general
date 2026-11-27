---
name: automated-search-model-builder
description: "Build, validate and audit exact or relaxed solver models for symmetric-cryptanalysis searches (trails, division properties, impossible transitions, MITM cuts). Use before trusting a solver's search result; public-key models are automated-algebra-and-search-model-builder."
metadata:
  version: "0.1"
  display-name: "Automated Search Model Builder"
  tags: "MILP, SAT, SMT, CP-SAT, MIQCP, solver"
  requires: "design-assumption-graph, search-objective, target-scope"
  produces: "solver-model, validation-suite, witnesses, search-limitations"
---

# Automated Search Model Builder

## Use this skill when

Searching differential/linear trails, integral/division properties, impossible transitions, ARX characteristics, boomerang components, algebraic solutions, meet-in-the-middle cuts, or other combinatorial structures with a solver or custom search.

## Operating procedure

1. **Define the searched object.** Distinguish exact trail, truncated pattern, differential/hull, division-property transition, impossible property, algebraic solution, cut/matching schedule, or lower bound. Do not let the solver objective redefine the cryptanalytic claim.
2. **Choose a modeling family.** Use MILP/CP-SAT for activity patterns and many discrete optimizations; SAT/SMT for exact bit-vector logic; MIQCP or specialized models for nonlinear probability/correlation relations; dynamic programming/branch-and-bound for transition enumeration; ANF/Gröbner methods for polynomial systems. Justify the choice.
3. **Encode exact semantics first.** Specify bit/word ordering, boundaries, constants, key schedule, modular carries, S-box transition tables, linear layers, and domain restrictions. Mark every relaxation and the direction of its error.
4. **Separate feasibility and weight.** First verify that witnesses correspond to valid primitive executions; then optimize probability, correlation, active components, degrees of freedom, or cost.
5. **Test soundness and completeness.** Exhaustively enumerate small components/rounds and compare solver-accepted and actual transitions. Include deliberately invalid witnesses and boundary cases.
6. **Validate witnesses directly.** Re-run every reported trail/solution in an independent primitive model and recompute its exact weight or property. Solver objective values are not cryptanalytic evidence by themselves.
7. **Treat aggregation separately.** A best trail does not establish the probability of a differential or correlation of a hull. Search or bound clusters, signs, key dependence, and dependencies as required.
8. **Handle infeasibility cautiously.** Prefer certificates, dual bounds, independently implemented models, and exhaustive reduced checks. Distinguish proved infeasible, infeasible under a relaxation/constraint set, timed out, and not searched.
9. **Make search limits explicit.** Record bounds, symmetry breaking, fixed endpoints, key assumptions, excluded patterns, solver gaps, time/memory limits, randomness, and number of models tried.
10. **Export reproducible artifacts.** Save source model, generated instance, solver command/options/version, logs, witnesses/certificates, direct-validation output, and an interpretation script.

## Output contract

Produce:

- modeling rationale and exact semantics;
- variables, constraints, objective, and relaxations;
- small-case soundness/completeness tests;
- solver artifacts and independent witness checks;
- aggregation plan beyond the best trail;
- precise meaning of optimality/infeasibility/timeout;
- limitations that prevent extrapolation to unsearched rounds or models.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `MWGP11-MILP`
- `SHW14-AUTO`
- `TODO15-DIVPROP`
- `XZR16-BITDIV`
- `GD21-BITDIV`
- `MM00-SAT`
- `CP02-ALG`

Full records are bundled in `references/REFERENCES.md`.
