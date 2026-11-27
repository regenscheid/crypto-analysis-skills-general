---
name: quantum-algorithm-circuit-and-resource-verification
description: "Formalizes quantum cryptanalytic algorithms, reversible oracles, circuit transformations, correctness probabilities, and resource counts using SQIR/VOQC, QWIRE, Qbricks, or related proof frameworks."
metadata:
  version: "0.1.0"
  display-name: "Quantum Algorithm, Circuit, and Resource Verification"
  category: "quantum-verification"
  tags: "quantum, sqir, voqc, qbricks, oracle, resource-estimation"
  requires: "quantum algorithm or attack, oracle specification, resource and access model"
  produces: "verified circuit/algorithm theorem, oracle correctness proof, resource bounds, assumption report"
  optional: "true"
  namespace: "formal"
---

# Quantum Algorithm, Circuit, and Resource Verification

## Purpose

Formalizes quantum cryptanalytic algorithms, reversible oracles, circuit transformations, correctness probabilities, and resource counts using SQIR/VOQC, QWIRE, Qbricks, or related proof frameworks.

## Use this skill when

Use this skill when a cryptanalytic claim depends on correctness of a nontrivial quantum circuit, reversible implementation of a classical predicate, amplitude-amplification conditions, phase/order finding, or rigorous gate/qubit/depth bounds.

## Do not invoke automatically

Do not formalize a generic statement such as “Grover gives a square-root speedup” unless the decisive issue is the concrete oracle, marked-state count, verification cost, data access, parallelism, or resource estimate.

## Optional entry contract

**Inputs**
- quantum algorithm or attack
- oracle specification
- resource and access model

**Expected products**
- verified circuit/algorithm theorem
- oracle correctness proof
- resource bounds
- assumption report

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Define the quantum access model first: Q1/Q2, coherent access to which primitive or data, qRAM assumptions, state preparation, measurement schedule, noise/error correction scope, and classical preprocessing.
2. Write the mathematical algorithm and success theorem, including initial state, unitary/oracle action, number of marked items, phase conventions, repetitions, amplification, and output verification.
3. Define the classical cryptographic predicate exactly and build a reversible oracle with ancilla initialization, garbage management, uncomputation, and failure behavior.
4. Use SQIR/QWIRE for denotational circuit reasoning and VOQC for verified optimization, or Qbricks for parametric circuit-building programs and resource specifications. Pin the semantics and versions.
5. Prove oracle functional correctness and well-formedness before composing the quantum algorithm. Connect bit widths, modular arithmetic, key schedule, memory access, and comparison circuits to the target.
6. Derive gate counts by type, depth, qubits/ancillas, T-count/T-depth where relevant, calls to expensive subroutines, state-preparation cost, and classical verification/output cost.
7. Audit optimized circuits through a verified optimizer or equivalence proof. Preserve architecture/error-correction assumptions separately from logical-circuit correctness.
8. Cross-check small instances by simulation and classical enumeration and test deliberate oracle/circuit mutations.
9. Publish circuit source, theorem, resource formulas, model assumptions, and the exact relationship to the cryptanalytic security estimate.

## Output contract

- A checked quantum algorithm/circuit correctness theorem.
- A verified reversible-oracle implementation or explicit oracle assumption.
- Symbolic and instantiated resource bounds.
- A Q1/Q2, qRAM, error-correction, and implementation assumption report.

## Non-negotiable guardrails

- Query complexity is not total gate, depth, qubit, or wall-clock cost.
- A coherent oracle may be far more expensive than one classical primitive evaluation.
- Classical data does not become coherently queryable without an explicit model and cost.
- Logical circuit proofs do not establish fault-tolerant hardware feasibility.

## Related formal skills

- `bitvector-equivalence-and-sat-lowering`
- `formal-claim-and-model-authoring`

## Related cryptanalysis skills in this pack (optional)

- `quantum-public-key-attack-analysis`
- `quantum-symmetric-attack-analysis`

## Associated primary references

- **SQIR-REPO** — [SQIR and VOQC repository](https://github.com/inQWIRE/SQIR) (2026) — inQWIRE project. `official-repository`.
- **VOQC20** — [A Verified Optimizer for Quantum Circuits](https://arxiv.org/abs/1912.02250) (2020) — Kesha Hietala et al.. `research-paper`.
- **QWIRE18** — [QWIRE Practice: Formal Verification of Quantum Circuits in Coq](https://arxiv.org/abs/1803.00699) (2018) — Robert Rand et al.. `research-paper`.
- **QBRICKS** — [Qbricks](https://qbricks.github.io/) (2026) — Qbricks project. `official-project`.
- **QBRICKS21** — [A Deductive Verification Framework for Circuit-building Quantum Programs](https://arxiv.org/abs/2003.05841) (2021) — Christophe Chareton et al.. `research-paper`.
- **VQO21** — [Verified Compilation of Quantum Oracles](https://arxiv.org/abs/2112.06700) (2021) — Liyi Li et al.. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
