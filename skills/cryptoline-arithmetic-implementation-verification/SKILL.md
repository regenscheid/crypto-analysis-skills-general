---
name: cryptoline-arithmetic-implementation-verification
description: "Verifies low-level cryptographic arithmetic through algebraic and range specifications, especially multi-precision, finite-field, vectorized, and assembly-level kernels."
metadata:
  version: "0.1.0"
  display-name: "CryptoLine Arithmetic Implementation Verification"
  category: "implementation-verification"
  tags: "cryptoline, arithmetic, assembly, range-proof, algebraic-proof"
  requires: "low-level arithmetic routine, input/output representation, modular or algebraic specification"
  produces: "CryptoLine specification, algebraic/range proof result, assumption report, replay bundle"
  optional: "true"
  namespace: "formal"
---

# CryptoLine Arithmetic Implementation Verification

## Purpose

Verifies low-level cryptographic arithmetic through algebraic and range specifications, especially multi-precision, finite-field, vectorized, and assembly-level kernels.

## Use this skill when

Use this skill for arithmetic kernels whose correctness naturally separates into polynomial/algebraic identities and machine-integer range or safety conditions, including ECC, lattice, and finite-field implementations.

## Do not invoke automatically

Do not treat CryptoLine as a whole-program verifier or use it without specifying memory/calling behavior that lies outside the arithmetic model. Use another workflow for parsing, allocation, protocol state, or security reductions.

## Optional entry contract

**Inputs**
- low-level arithmetic routine
- input/output representation
- modular or algebraic specification

**Expected products**
- CryptoLine specification
- algebraic/range proof result
- assumption report
- replay bundle

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Pin CryptoLine, SMT/CAS backends, source or assembly artifact, target ISA, and compilation route. Record the precise instruction semantics being modeled.
2. Transcribe inputs, limb order, radix, signedness, modulus, preconditions, outputs, and allowed representations into a CryptoLine procedure.
3. Separate the algebraic postcondition from range, carry, overflow, memory-safety, and instruction-safety obligations. Avoid proving only congruence when canonical output is required.
4. Model SIMD lanes, shuffles, multiply-high operations, condition flags, and special instructions exactly; validate selected instructions against architecture documentation and concrete tests.
5. Prove intermediate bounds sufficient for every carry and reduction step. Check that assumptions compose across called routines and loops/unrolled blocks.
6. Use independent exact arithmetic to validate random and boundary cases, including maximum limbs, zero, modulus boundaries, and aliasing patterns.
7. Review solver output, timeouts, cut lemmas, and any admitted facts. Where practical, export or reconstruct critical certificates.
8. Publish the routine, theorem, representation, preconditions, proof logs, and non-arithmetic assumptions.

## Output contract

- A complete CryptoLine procedure and specification.
- Algebraic and range verification reports.
- Instruction/model and external-call assumption inventory.
- Independent boundary tests and clean replay configuration.

## Non-negotiable guardrails

- Congruence modulo p is not canonical reduction or equality over integers.
- Range assumptions must be proved at call boundaries, not copied forward optimistically.
- Architecture-specific instructions and undefined behavior belong in the TCB statement.
- Do not infer constant-time beyond the leakage properties actually checked.

## Related formal skills

- `fiat-crypto-and-verified-arithmetic-synthesis`
- `constant-time-and-leakage-verification`

## Related cryptanalysis skills in this pack (optional)

- `elliptic-curve-discrete-log-and-ecc-analysis`
- `lattice-hard-problem-and-estimator-analysis`

## Associated primary references

- **CRYPTOLINE-REPO** — [CryptoLine repository](https://github.com/fmlab-iis/cryptoline) (2026) — Formosa Crypto Lab. `official-repository`.
- **SAW-REPO** — [SAWScript repository](https://github.com/GaloisInc/saw-script) (2026) — Galois. `official-repository`.
- **FIAT-CRYPTO19** — [Simple High-Level Code for Cryptographic Arithmetic—with Proofs, Without Compromises](https://adam.chlipala.net/papers/FiatCryptoSP19/) (2019) — Andres Erbsen et al.. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
