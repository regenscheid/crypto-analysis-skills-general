---
name: saw-cryptol-program-refinement
description: "Uses Cryptol specifications and SAW symbolic execution/refinement to verify C/LLVM, Rust/MIR, Java, or other supported implementations against executable bit-level cryptographic models."
metadata:
  version: "0.1.0"
  display-name: "SAW and Cryptol Program Refinement"
  category: "implementation-verification"
  tags: "saw, cryptol, symbolic-execution, llvm, refinement"
  requires: "implementation artifact, Cryptol or SAW specification, memory and calling-convention contract"
  produces: "SAW proof script, refinement result, solver evidence, replay project"
  optional: "true"
  namespace: "formal"
---

# SAW and Cryptol Program Refinement

## Purpose

Uses Cryptol specifications and SAW symbolic execution/refinement to verify C/LLVM, Rust/MIR, Java, or other supported implementations against executable bit-level cryptographic models.

## Use this skill when

Use this skill when the target implementation is already available in a SAW-supported representation and a concise Cryptol or SAW specification can express the relevant functional behavior.

## Do not invoke automatically

Do not rely on SAW alone for claims about unsupported compiler behavior, whole-protocol state, physical leakage, or computational security reductions. Avoid symbolic execution when path explosion or unsupported features make the model unfaithful.

## Optional entry contract

**Inputs**
- implementation artifact
- Cryptol or SAW specification
- memory and calling-convention contract

**Expected products**
- SAW proof script
- refinement result
- solver evidence
- replay project

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Pin SAW, Cryptol, backend solvers, compiler/bitcode producer, target architecture, and source commit. Preserve the exact LLVM/MIR/bytecode artifact proved.
2. Develop the executable Cryptol specification independently and validate it with official vectors and at least one separate implementation.
3. Specify function arguments, memory regions, allocation, aliasing, initialization, alignment, return values, globals, and allowed undefined behavior in the SAW contract.
4. Use symbolic simulation to relate implementation states to the specification. Split large routines at stable internal boundaries and prove reusable lemmas for round functions and arithmetic kernels.
5. Inspect every override, uninterpreted function, external call, and solver assumption. Replace broad overrides with verified or tightly scoped models.
6. For fixed-width arithmetic, confirm endianness, shifts, rotations, overflow, poison/undefined behavior, and compiler intrinsics against the generated artifact.
7. Request and retain solver proof/certificate output when the backend supports it; otherwise record the solver in the TCB and cross-check critical identities independently.
8. Run negative mutations and concrete tests, then replay in isolation from pinned bitcode and proof scripts.
9. Publish the specification, implementation artifact hash, contract, theorem scope, solver trust, and exclusions.

## Output contract

- Cryptol/SAW specification and proof script.
- Exact implementation artifact and memory contract.
- Solver/rewrite/override audit.
- Clean replay logs and claim-scoped assurance report.

## Non-negotiable guardrails

- Do not prove optimized bitcode against a specification generated from the same code without independent semantic review.
- Undefined or poison behavior must not be hidden by a friendly model.
- An override is an assumption unless separately verified.
- Keep the compiler path and artifact hash tied to the result.

## Related formal skills

- `bitvector-equivalence-and-sat-lowering`
- `implementation-refinement-and-equivalence`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **SAW-DOCS** — [Software Analysis Workbench documentation](https://galoisinc.github.io/saw-script/) (2026) — Galois. `official-manual`.
- **SAW-REPO** — [SAWScript repository](https://github.com/GaloisInc/saw-script) (2026) — Galois. `official-repository`.
- **CRYPTOL-DOCS** — [Cryptol documentation](https://galoisinc.github.io/cryptol/) (2026) — Galois. `official-manual`.
- **LAST-MILE20** — [The Last Mile: High-Assurance and High-Speed Cryptographic Implementations](https://arxiv.org/abs/1904.04606) (2020) — José Bacelar Almeida et al.. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
