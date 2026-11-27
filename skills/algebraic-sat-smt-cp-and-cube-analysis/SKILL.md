---
name: algebraic-sat-smt-cp-and-cube-analysis
description: "Model a symmetric primitive as equations or exact constraints and evaluate SAT/SMT/CP, algebraic and cube attacks. Use when it has low-degree or sparse structure or controllable public variables; separates concrete solver success from scalable attack claims."
metadata:
  version: "0.1"
  display-name: "Algebraic, SAT/SMT/CP, and Cube Analysis"
  tags: "algebraic-cryptanalysis, SAT, SMT, CP, cube-attack"
  requires: "design-assumption-graph, claim-model, known-or-chosen-data"
  produces: "equation-system, solver-records, cube-records, scaling-analysis"
---

# Algebraic, SAT/SMT/CP, and Cube Analysis

## Use this skill when

The target has low-degree Boolean structure, sparse equations, exploitable initialization, controllable public variables, or a solver may recover key/state or certify structural properties.

## Operating procedure

1. **Choose variables and observations.** Specify secret key/state variables, public plaintext/message/nonce/tweak variables, intermediate variables, output constraints, and number/type of transcripts.
2. **Derive exact equations.** Produce ANF/MQ, finite-field equations, bit-vector formulas, CNF, SMT, or CP constraints with exact constants, schedule, initialization, and finalization. Record auxiliary-variable definitions.
3. **Measure structure.** Track degree growth, monomial count, sparsity, equation/unknown ratio, rank, repeated subexpressions, symmetries, and transcript coupling. Do not infer hardness solely from equation count.
4. **Select the solving strategy.** Consider Gröbner bases, XL/XSL-style linearization, SAT/CDCL, SMT bit-vectors, CP-SAT, Gaussian elimination, meet-in-the-middle, guess-and-determine, or hybrids. Justify expected leverage.
5. **Use preprocessing honestly.** Record key-independent simplification, learned clauses, monomial bases, Gröbner precomputation, cube selection, and amortization.
6. **For cube/interpolation attacks, define cubes exactly.** Identify public cube variables, fixed variables, superpoly, degree assumptions, offline extraction, online equations, independence/rank, and noise/error handling.
7. **Validate encodings.** Compare with reference vectors, random intermediate states, exhaustive tiny instances, and deliberately incorrect assignments. Verify every recovered key/state in the real primitive.
8. **Study scaling.** Run controlled parameter/round sweeps, report distributions over instances, conflicts/nodes/memory, timeout/censoring, and model changes. Avoid extrapolating from one easy instance.
9. **Distinguish uses of solvers.** A solver that finds a trail, proves a property, recovers a toy key, or recovers a full key under many chosen transcripts establishes different results.
10. **Audit against generic recovery.** Include transcript generation, equation construction, memory, solver restarts/parallelism, verification, success rate, and instance selection bias.

## Output contract

Provide:

- exact variable/equation/constraint specification;
- encoding validation tests;
- solver/cube algorithm and preprocessing;
- instance distributions and scaling evidence;
- recovered witness verification;
- full data/time/memory/success accounting;
- limitations of asymptotic or heuristic claims;
- exact target/model/round impact.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `CP02-ALG`
- `MM00-SAT`
- `DS09-CUBE`
- `CM03-ALGSTREAM`
- `SHW14-AUTO`

Full records are bundled in `references/REFERENCES.md`.
