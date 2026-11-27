---
name: aeneas-charon-rust-to-lean
description: "Extracts supported Rust through Charon and Aeneas into Lean and proves panic freedom, functional correctness, and refinement against independent cryptographic specifications."
metadata:
  version: "0.1.0"
  display-name: "Aeneas/Charon Rust-to-Lean Verification"
  category: "implementation-verification"
  tags: "aeneas, charon, rust, lean, refinement"
  requires: "Rust crate and source commit, independent Lean specification, supported-subset assessment"
  produces: "LLBC and Lean model, refinement proof, translation assumptions, replayable pipeline"
  optional: "true"
  namespace: "formal"
---

# Aeneas/Charon Rust-to-Lean Verification

## Purpose

Extracts supported Rust through Charon and Aeneas into Lean and proves panic freedom, functional correctness, and refinement against independent cryptographic specifications.

## Use this skill when

Use this skill when production or reference Rust lies within Aeneas’s supported safe sequential subset and the desired final artifact is a Lean theorem about its extracted functional model.

## Do not invoke automatically

Do not choose this path for unsupported unsafe code, concurrency, opaque FFI, or intrinsics whose semantics cannot be modeled responsibly. A different verifier or a smaller verified boundary may be better.

## Optional entry contract

**Inputs**
- Rust crate and source commit
- independent Lean specification
- supported-subset assessment

**Expected products**
- LLBC and Lean model
- refinement proof
- translation assumptions
- replayable pipeline

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Pin Rust, Charon, Aeneas, Lean, mathlib, and all crate dependencies. Record feature flags, target, source commit, and the Aeneas `charon-pin` relationship.
2. Audit the Rust subset: borrowing patterns, loops, generics, mutable references, panics, traits, arrays/slices, unsafe blocks, concurrency, FFI, and intrinsics. Isolate unsupported code behind explicit models or reduce scope.
3. Run Charon with the Aeneas preset and preserve LLBC artifacts and logs. Review extraction warnings and compare the translated control/data flow to the Rust source.
4. Generate Lean code through Aeneas. Keep generated files immutable and place handwritten specifications and proofs separately.
5. Define or import authoritative models for Rust core/library operations and intrinsics. Record each as a translation/TBC assumption unless proved.
6. Prove panic/exception freedom and preconditions, then decompose monadic generated functions into algorithmic phases and connect them to a code-shaped auxiliary specification.
7. Prove the auxiliary specification equal to the independent source-derived specification. Separate integer bounds, modular equalities, encoding correspondence, and mutable-state threading.
8. Regenerate on every source/toolchain change; do not patch generated Lean by hand. Run official vectors through Rust, extracted model, and independent spec.
9. Publish the theorem, source/LLBC/generated hashes, translation assumptions, caller preconditions, and explicit exclusion of constant-time unless separately verified.

## Output contract

- Pinned Rust, Charon, Aeneas, and Lean artifacts.
- Generated LLBC/Lean model plus source comparison notes.
- Panic-freedom and direct refinement theorems.
- Translation/intrinsic/library-model assumptions and clean replay.

## Non-negotiable guardrails

- A Lean proof about the Aeneas model assumes the extraction/modeling chain unless separately verified.
- Do not edit generated code to simplify the proof.
- Do not hide panics in default result values or impossible preconditions.
- Unsafe, FFI, concurrency, and hardware intrinsics require explicit boundaries and semantics.

## Related formal skills

- `hax-multibackend-rust-verification`
- `symcrypt-verified-crypto-workflow`
- `implementation-refinement-and-equivalence`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **AENEAS22** — [Aeneas: Rust Verification by Functional Translation](https://arxiv.org/abs/2206.07185) (2022) — Son Ho et al.. `research-paper`.
- **AENEAS-REPO** — [Aeneas repository](https://github.com/AeneasVerif/aeneas) (2026) — Aeneas project. `official-repository`.
- **CHARON-REPO** — [Charon repository](https://github.com/AeneasVerif/charon) (2026) — Charon project. `official-repository`.
- **SYMCRYPT-VERIFIED26** — [Verifying Rust cryptography in SymCrypt: from standards to code](https://www.microsoft.com/en-us/research/blog/verifying-rust-cryptography-in-symcrypt-from-standards-to-code/) (2026) — Microsoft Research. `official-project-report`.
- **RUST-LEAN-AI26** — [A Rust-to-Lean Verification Pipeline with AI Provers: An Experience Report](https://arxiv.org/abs/2605.30106) (2026) — Natalia Klaus, Juan Conejero, and Palina Tolmach. `research-paper`.
- **LEAN-FAQ** — [Lean FAQ](https://lean-lang.org/faq/) (2026) — Lean project. `official-documentation`.

Bundled source metadata is in `references/REFERENCES.md`.
