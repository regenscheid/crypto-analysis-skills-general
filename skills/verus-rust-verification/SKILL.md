---
name: verus-rust-verification
description: "Verifies annotated Rust using Verus specifications, ghost state, linear ghost types, SMT-backed proof, and explicit separation between mathematical integers and machine values."
metadata:
  version: "0.1.0"
  display-name: "Verus Rust Verification"
  category: "implementation-verification"
  tags: "verus, rust, smt, functional-correctness"
  requires: "Rust crate or module, Verus environment, functional and safety specification"
  produces: "Verus-checked implementation, contracts and invariants, SMT/resource report, replay project"
  optional: "true"
  namespace: "formal"
---

# Verus Rust Verification

## Purpose

Verifies annotated Rust using Verus specifications, ghost state, linear ghost types, SMT-backed proof, and explicit separation between mathematical integers and machine values.

## Use this skill when

Use this skill when source-local Rust contracts, modular verification, ghost state, and SMT automation are preferable to translation into a separate proof assistant.

## Do not invoke automatically

Do not choose Verus if the code relies heavily on unsupported unsafe/FFI/concurrency patterns or if the main goal is a theorem in Lean against an independently developed library. Compare the workflows first.

## Optional entry contract

**Inputs**
- Rust crate or module
- Verus environment
- functional and safety specification

**Expected products**
- Verus-checked implementation
- contracts and invariants
- SMT/resource report
- replay project

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Pin Verus, Rust toolchain, solver, dependencies, target features, and source commit. Build official examples before adapting crypto code.
2. Write executable Rust separately from `spec`, `proof`, and ghost constructs. Define abstraction functions from byte/word representations to mathematical values.
3. Specify preconditions, postconditions, recommends clauses, invariants, framing, overflow behavior, panics, and memory ownership. Keep all caller obligations visible.
4. Decompose loops and stateful algorithms with inductive invariants. Separate machine-word wraparound from mathematical integer reasoning and prove range connections.
5. Use trigger/quantifier guidance and SMT lemmas deliberately. Avoid brittle proofs that pass only under enormous resource limits or incidental solver behavior.
6. For cryptographic arithmetic, prove modular identities and bounds independently; for arrays/encodings, prove length, indexing, and canonicality properties.
7. Validate with executable tests and mutations, then run Verus in a clean environment and capture solver versions, seeds/options, timeouts, and resource limits.
8. Audit trusted and external functions, assumes, opaque specs, and verifier escape hatches. Treat them as TCB entries.
9. Publish exact contracts and non-claims; Verus verification does not automatically establish constant-time, compiler correctness, or a computational security reduction.

## Output contract

- A compiling Verus project with explicit contracts and invariants.
- Checked functional/safety theorems and abstraction lemmas.
- SMT configuration, performance, and trusted-function audit.
- Clean replay and source-version manifest.

## Non-negotiable guardrails

- Do not use `assume` to encode the desired result or hide unsupported functions.
- Do not confuse `int` specifications with machine integer behavior.
- Large solver limits and fragile triggers are maintenance risks that must be reported.
- Source annotations should not alter runtime semantics unexpectedly.

## Related formal skills

- `creusot-why3-rust-verification`
- `implementation-refinement-and-equivalence`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **VERUS-GUIDE** — [Verus Tutorial and Reference](https://verus-lang.github.io/verus/guide/) (2026) — Verus project. `official-manual`.
- **VERUS-REPO** — [Verus repository](https://github.com/verus-lang/verus) (2026) — Verus project. `official-repository`.
- **VERUS23** — [Verus: Verifying Rust Programs using Linear Ghost Types](https://arxiv.org/abs/2303.05491) (2023) — Andrea Lattuada et al.. `research-paper`.
- **VERUSAGE25** — [VeruSAGE: A Study of Agent-Based Verification for Rust Systems](https://arxiv.org/abs/2512.18436) (2025) — Chenyuan Yang, Natalie Neamtu, Chris Hawblitzel, Jacob R. Lorch, and Shan Lu. `research-paper`. Additional primary links: [1](https://github.com/microsoft/verus-proof-synthesis).

Bundled source metadata is in `references/REFERENCES.md`.
