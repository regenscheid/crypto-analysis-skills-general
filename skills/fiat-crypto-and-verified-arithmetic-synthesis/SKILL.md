---
name: fiat-crypto-and-verified-arithmetic-synthesis
description: "Generates and verifies high-performance modular arithmetic from mathematical specifications using Fiat-Crypto and related verified synthesis pipelines."
metadata:
  version: "0.1.0"
  display-name: "Fiat-Crypto and Verified Arithmetic Synthesis"
  category: "security-proofs"
  tags: "fiat-crypto, rocq, arithmetic, code-generation"
  requires: "field/modulus specification, operation set, target word sizes and platforms"
  produces: "generated implementation, functional-correctness theorem, bounds and representation proof, benchmarks"
  optional: "true"
  namespace: "formal"
---

# Fiat-Crypto and Verified Arithmetic Synthesis

## Purpose

Generates and verifies high-performance modular arithmetic from mathematical specifications using Fiat-Crypto and related verified synthesis pipelines.

## Use this skill when

Use this skill for prime-field arithmetic, Montgomery/Barrett-style representations, inversion templates, and other straight-line cryptographic arithmetic where verified synthesis can replace hand proof of every implementation.

## Do not invoke automatically

Do not use generated field routines as proof of the surrounding elliptic-curve, lattice, signature, serialization, or protocol code. The theorem scope is the generated arithmetic contract.

## Optional entry contract

**Inputs**
- field/modulus specification
- operation set
- target word sizes and platforms

**Expected products**
- generated implementation
- functional-correctness theorem
- bounds and representation proof
- benchmarks

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Define the modulus, limb width/count, representation, input bounds, canonicality, and required operations independently of target code.
2. Prove or certify modulus properties and any preconditions required by the generator, including positivity, oddness, size, and reduction bounds.
3. Run Fiat-Crypto from pinned sources and record command-line/configuration choices, generated intermediate language, target language, and compiler assumptions.
4. Inspect the resulting theorem statement: mathematical operation, input/output representation, range guarantees, aliasing/memory model, and word semantics.
5. Validate generated code against independent big-integer/reference computations and official vectors, including boundary values and noncanonical inputs permitted by the contract.
6. Integrate into higher-level code only through explicit refinement lemmas or verified wrappers. Preserve calling conventions and bounds across each operation.
7. For CryptOpt-style optimization, treat randomized search and benchmarking as untrusted optimization; rely on the verified equivalence checker to connect optimized assembly to the source program.
8. Measure performance on pinned hardware separately from correctness. Re-run verification when code generation, target architecture, or compiler changes.
9. Publish source specification, generator version, proofs, generated code, benchmark methodology, and residual compiler/platform trust.

## Output contract

- A mathematical arithmetic specification and parameter proofs.
- Generated source/assembly with machine-checked functional correctness.
- Representation, range, and integration contracts.
- Independent tests, performance measurements, and trust report.

## Non-negotiable guardrails

- Do not widen input ranges beyond the proved contract.
- Do not assume constant-time behavior unless separately established and preserved by compilation.
- Do not hand-edit generated code without re-establishing equivalence.
- Randomized optimizer success is irrelevant to correctness without the verified checker.

## Related formal skills

- `cryptopt-verified-arithmetic-optimization`
- `cryptoline-arithmetic-implementation-verification`

## Related cryptanalysis skills in this pack (optional)

- `elliptic-curve-discrete-log-and-ecc-analysis`
- `lattice-hard-problem-and-estimator-analysis`

## Associated primary references

- **FIAT-CRYPTO-REPO** — [Fiat Cryptography](https://github.com/mit-plv/fiat-crypto) (2026) — MIT PLV. `official-repository`.
- **FIAT-CRYPTO19** — [Simple High-Level Code for Cryptographic Arithmetic—with Proofs, Without Compromises](https://adam.chlipala.net/papers/FiatCryptoSP19/) (2019) — Andres Erbsen et al.. `research-paper`.
- **CRYPTOPT23** — [CryptOpt: Verified Compilation with Randomized Program Search for Cryptographic Primitives](https://arxiv.org/abs/2211.10665) (2023) — Joel Kuepper et al.. `research-paper`.
- **CRYPTOPT-REPO** — [CryptOpt repository](https://github.com/0xADE1A1DE/CryptOpt) (2026) — CryptOpt project. `official-repository`.
- **ROCQ-HOME** — [The Rocq Prover](https://rocq-prover.org/) (2026) — Rocq project. `official-project`.

Bundled source metadata is in `references/REFERENCES.md`.
