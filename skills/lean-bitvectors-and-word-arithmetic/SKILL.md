---
name: lean-bitvectors-and-word-arithmetic
description: "Formalizes fixed-width arithmetic, bit operations, carries, rotations, shifts, masks, endianness, and modular machine semantics in Lean, with decision procedures for bounded obligations."
metadata:
  version: "0.1.0"
  display-name: "Lean Bit Vectors and Word Arithmetic"
  category: "lean"
  tags: "lean, bitvector, word-arithmetic, machine-semantics"
  requires: "bit-level algorithm or implementation model, word widths, endianness and overflow rules"
  produces: "bit-vector specification, equivalence lemmas, range and overflow proofs, checked bounded results"
  optional: "true"
  namespace: "formal"
---

# Lean Bit Vectors and Word Arithmetic

## Purpose

Formalizes fixed-width arithmetic, bit operations, carries, rotations, shifts, masks, endianness, and modular machine semantics in Lean, with decision procedures for bounded obligations.

## Use this skill when

Use this skill for symmetric primitives, hashes, ARX designs, encodings, constant-time masks, low-level modular arithmetic, and correspondence between mathematical residues and machine words.

## Do not invoke automatically

Do not replace fixed-width behavior with unbounded integers and postpone overflow indefinitely. That approach commonly proves a mathematically related algorithm rather than the implementation.

## Optional entry contract

**Inputs**
- bit-level algorithm or implementation model
- word widths
- endianness and overflow rules

**Expected products**
- bit-vector specification
- equivalence lemmas
- range and overflow proofs
- checked bounded results

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Fix the exact word widths, signedness, overflow/wrapping semantics, shift behavior, rotation convention, bit numbering, byte order, and conversion rules from the source language or standard.
2. Choose Lean `BitVec` or a project word abstraction with explicit correspondence. Avoid ad hoc lists of Booleans unless bit-level induction is genuinely required.
3. Define serialization and deserialization with lengths and canonicality conditions. Prove round trips in both directions under the correct domains.
4. Separate word-level wrapping identities from integer range lemmas. For algorithms intended to avoid overflow, prove the bounds; for wrapping algorithms, state modular equality directly.
5. Model carries, borrows, high/low multiplication, arithmetic versus logical shifts, and platform intrinsics explicitly. Treat undefined or implementation-defined source behavior as a separate obligation.
6. Use `bv_decide` or other kernel-checked finite procedures for suitably bounded goals, but record proof-term/replay costs and avoid native shortcuts when the trust policy forbids them.
7. For larger bit-vector properties, lower to SAT/SMT with a proved encoding or reconstructable proof and independently validate counterexample assignments against the Lean model.
8. Cross-check known vectors and randomly generated words against an independent implementation, including all-zeros, all-ones, boundary carries, and maximum shift counts.
9. Export abstraction lemmas connecting words to `ZMod`, integers, fields, and array-based code models so higher-level proofs need not unfold bits.

## Output contract

- An exact bit-vector/word specification and source-semantics note.
- Range, wraparound, carry, encoding, and abstraction theorems.
- Bounded decision-procedure or certificate artifacts.
- Independent vector and boundary-case results.

## Non-negotiable guardrails

- Do not assume language shift or overflow semantics; cite and encode them.
- Do not use signed casts where unsigned bit patterns are intended without a proved relation.
- An SMT `unsat` result is not a Lean theorem unless checked or reconstructed.
- Keep endianness and bit numbering visible in theorem names and examples.

## Related formal skills

- `bitvector-equivalence-and-sat-lowering`
- `sat-lrat-certification`

## Related cryptanalysis skills in this pack (optional)

- `algebraic-sat-smt-cp-and-cube-analysis`
- `arx-differential-rotational-rx-analysis`

## Associated primary references

- **LEAN-BVDECIDE** — [Lean tactic reference: bv_decide and decision procedures](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/) (2026) — Lean project. `official-manual`.
- **LEAN-REF** — [Lean Language Reference](https://lean-lang.org/doc/reference/latest/) (2026) — Lean project. `official-manual`.
- **MATHLIB-DOCS** — [Mathlib 4 Documentation](https://leanprover-community.github.io/mathlib4_docs/) (2026) — Lean community. `official-documentation`.
- **LRAT-CATCHER26** — [LRAT-Catcher: Importing SAT Refutations into Lean](https://arxiv.org/abs/2607.00815) (2026) — LRAT-Catcher authors. `research-paper`.
- **CVC5-PROOFS** — [cvc5 Proof Production](https://cvc5.github.io/docs-ci/docs-main/proofs/proofs.html) (2026) — cvc5 project. `official-manual`.
- **CRYPTOL-DOCS** — [Cryptol documentation](https://galoisinc.github.io/cryptol/) (2026) — Galois. `official-manual`.

Bundled source metadata is in `references/REFERENCES.md`.
