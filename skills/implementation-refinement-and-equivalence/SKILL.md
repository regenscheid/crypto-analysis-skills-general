---
name: implementation-refinement-and-equivalence
description: "Proves that source, intermediate, or low-level implementation behavior refines an independently defined cryptographic specification under explicit preconditions and machine semantics."
metadata:
  version: "0.1.0"
  display-name: "Implementation Refinement and Equivalence"
  category: "implementation-verification"
  tags: "refinement, equivalence, functional-correctness, implementation"
  requires: "independent specification, implementation model, preconditions and semantics"
  produces: "refinement theorem, safety/range obligations, correspondence map, non-claims"
  optional: "true"
  namespace: "formal"
---

# Implementation Refinement and Equivalence

## Purpose

Proves that source, intermediate, or low-level implementation behavior refines an independently defined cryptographic specification under explicit preconditions and machine semantics.

## Use this skill when

Use this skill for code-to-specification correctness, optimized-to-reference equivalence, compiler-stage validation, and proof that an executable implementation inherits a higher-level security theorem.

## Do not invoke automatically

Do not call unit tests, differential testing, or matching sample outputs a refinement proof. Conversely, do not insist on whole-program verification when a narrow function-level theorem is the relevant goal.

## Optional entry contract

**Inputs**
- independent specification
- implementation model
- preconditions and semantics

**Expected products**
- refinement theorem
- safety/range obligations
- correspondence map
- non-claims

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Define the observation relation: return value, output buffers, modified memory, errors, traces, timing/leakage if in scope, and permitted nondeterminism.
2. State preconditions and representation invariants over inputs, memory, alignment, aliasing, canonicality, lengths, keys, and hardware features. Prove they are achievable by callers.
3. Connect implementation types and values to specification types with explicit abstraction/concretization functions. Prove round trips or canonicality where required.
4. Decompose the implementation into algorithmic phases and establish loop invariants, range bounds, memory safety, panic/exception freedom, and arithmetic semantics.
5. Prove each phase refines its corresponding specification fragment, then compose. Avoid one opaque final tactic that obscures which semantic gaps were addressed.
6. For optimized code, use equivalence to a verified reference or code-shaped auxiliary spec, with separate proof from that auxiliary spec to the independent mathematical model.
7. Model intrinsics, SIMD, assembly instructions, library functions, randomness, and I/O from authoritative semantics. Record any axiomatized behavior.
8. Validate the theorem with test vectors and mutation tests: introduce representative code errors and ensure the proof or model comparison fails.
9. Compose with security theorems only after checking that security-game encodings, failure behavior, and side-channel assumptions match the implementation theorem.

## Output contract

- A direct refinement/equivalence theorem and observation relation.
- Precondition, memory, range, and panic/safety proofs.
- Abstraction functions and phase-by-phase correspondence.
- A trust/non-claims report and mutation-test evidence.

## Non-negotiable guardrails

- Do not prove equality to a specification copied from the same implementation unless the independent-specification bridge is also proved.
- Do not omit failure/error behavior from the observation relation.
- Functional correctness does not imply constant-time or compiler correctness.
- Caller preconditions must be visible and checked at integration boundaries.

## Related formal skills

- `normative-specification-to-executable-model`
- `constant-time-and-leakage-verification`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **AENEAS22** — [Aeneas: Rust Verification by Functional Translation](https://arxiv.org/abs/2206.07185) (2022) — Son Ho et al.. `research-paper`.
- **LAST-MILE20** — [The Last Mile: High-Assurance and High-Speed Cryptographic Implementations](https://arxiv.org/abs/1904.04606) (2020) — José Bacelar Almeida et al.. `research-paper`.
- **SAW-DOCS** — [Software Analysis Workbench documentation](https://galoisinc.github.io/saw-script/) (2026) — Galois. `official-manual`.
- **VERUS23** — [Verus: Verifying Rust Programs using Linear Ghost Types](https://arxiv.org/abs/2303.05491) (2023) — Andrea Lattuada et al.. `research-paper`.
- **CREUSOT22** — [Creusot: A Foundry for the Deductive Verification of Rust Programs](https://doi.org/10.1007/978-3-031-17244-1_6) (2022) — Xavier Denis et al.. `research-paper`.
- **SYMCRYPT-VERIFIED26** — [Verifying Rust cryptography in SymCrypt: from standards to code](https://www.microsoft.com/en-us/research/blog/verifying-rust-cryptography-in-symcrypt-from-standards-to-code/) (2026) — Microsoft Research. `official-project-report`.

Bundled source metadata is in `references/REFERENCES.md`.
