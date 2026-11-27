---
name: cryptopt-verified-arithmetic-optimization
description: "Synthesizes or optimizes low-level arithmetic while preserving a formal specification, then validates the generated implementation and compiler/assembly proof chain."
metadata:
  version: "0.1.0"
  display-name: "CryptOpt Verified Arithmetic Optimization"
  category: "implementation-verification"
  tags: "cryptopt, synthesis, optimization, arithmetic, fiat-crypto"
  requires: "field-arithmetic specification, target architecture, performance constraints"
  produces: "optimized routine, equivalence proof, benchmark record, toolchain and trust report"
  optional: "true"
  namespace: "formal"
---

# CryptOpt Verified Arithmetic Optimization

## Purpose

Synthesizes or optimizes low-level arithmetic while preserving a formal specification, then validates the generated implementation and compiler/assembly proof chain.

## Use this skill when

Use this skill when a verified high-level arithmetic routine exists but hand optimization is costly, and CryptOpt-style search can explore instruction schedules while preserving proven semantics.

## Do not invoke automatically

Do not use performance search as cryptanalysis evidence, or accept an optimized routine solely because randomized tests pass. Avoid unsupported architectures or semantics unless the model is extended and audited.

## Optional entry contract

**Inputs**
- field-arithmetic specification
- target architecture
- performance constraints

**Expected products**
- optimized routine
- equivalence proof
- benchmark record
- toolchain and trust report

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Pin CryptOpt, Fiat-Crypto/Rocq dependencies, architecture model, compiler/assembler, benchmark harness, and source specifications.
2. Confirm the input specification and representation theorem before optimization. Record modulus, radix, bounds, carry discipline, aliasing, and canonicality requirements.
3. Run optimization/search with deterministic seeds or a preserved search log where possible. Distinguish heuristic performance search from formal equivalence checking.
4. Check every generated candidate through the formal validation path, not merely the fastest candidate or a post-hoc test suite.
5. Inspect architecture models, instruction costs, and any undefined or variable-latency behavior. Benchmark on representative hardware without treating timings as a proof property.
6. Validate generated code against official vectors and an independent exact model, including boundary inputs and aliasing conditions.
7. Replay synthesis and/or at minimum replay proof checking from pinned artifacts. Preserve the exact selected candidate and its provenance.
8. Publish correctness theorem, performance methodology, architecture/compiler assumptions, and any leakage non-claims.

## Output contract

- Optimized arithmetic implementation and exact source specification.
- Machine-checked equivalence/correctness artifact.
- Reproducible or preserved optimization provenance.
- Benchmark and trust-boundary report.

## Non-negotiable guardrails

- Optimization heuristics need not be trusted for correctness if every result is checked, but the checker path must be explicit.
- Do not compare performance across incompatible compiler flags or CPUs.
- Instruction-cost models are empirical/modeling inputs, not theorems about all hardware.
- Preserve bounds and representation preconditions through generated interfaces.

## Related formal skills

- `fiat-crypto-and-verified-arithmetic-synthesis`
- `cryptoline-arithmetic-implementation-verification`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **CRYPTOPT23** — [CryptOpt: Verified Compilation with Randomized Program Search for Cryptographic Primitives](https://arxiv.org/abs/2211.10665) (2023) — Joel Kuepper et al.. `research-paper`.
- **CRYPTOPT-REPO** — [CryptOpt repository](https://github.com/0xADE1A1DE/CryptOpt) (2026) — CryptOpt project. `official-repository`.
- **FIAT-CRYPTO-REPO** — [Fiat Cryptography](https://github.com/mit-plv/fiat-crypto) (2026) — MIT PLV. `official-repository`.
- **FIAT-CRYPTO19** — [Simple High-Level Code for Cryptographic Arithmetic—with Proofs, Without Compromises](https://adam.chlipala.net/papers/FiatCryptoSP19/) (2019) — Andres Erbsen et al.. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
