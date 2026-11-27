---
name: fstar-hacl-evercrypt-and-vale
description: "Uses the Project Everest stack to specify and verify cryptographic software from Low* and HACL* through agile EverCrypt composition and Vale assembly, with explicit extraction, memory-safety, functional-correctness, and leakage assumptions."
metadata:
  version: "0.1.0"
  display-name: "F*, HACL*, EverCrypt, and Vale Verification"
  category: "implementation-verification"
  tags: "fstar, hacl, evercrypt, vale, lowstar"
  requires: "cryptographic implementation or design, F* specification boundary, target C or assembly requirements"
  produces: "verified F*/Low* development, extracted implementation, assumption and extraction audit, replay package"
  optional: "true"
  namespace: "formal"
---

# F*, HACL*, EverCrypt, and Vale Verification

## Purpose

Uses the Project Everest stack to specify and verify cryptographic software from Low* and HACL* through agile EverCrypt composition and Vale assembly, with explicit extraction, memory-safety, functional-correctness, and leakage assumptions.

## Use this skill when

Use this skill when the target is new or existing C/assembly-oriented cryptographic code and the Project Everest ecosystem provides an appropriate verified implementation path, reusable primitive, or proof pattern.

## Do not invoke automatically

Do not choose this stack merely because the implementation is cryptographic. Ordinary Rust, arbitrary legacy C, highly dynamic code, or a claim about computational security may fit Aeneas, SAW, EasyCrypt, or another route better.

## Optional entry contract

**Inputs**
- cryptographic implementation or design
- F* specification boundary
- target C or assembly requirements

**Expected products**
- verified F*/Low* development
- extracted implementation
- assumption and extraction audit
- replay package

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Pin F*, Z3/SMT dependencies, KaRaMeL or extraction tools, HACL*/EverCrypt/Vale revisions, C compiler, target architecture, and build flags.
2. Define the functional specification independently of optimized code. State byte order, modular arithmetic, lengths, aliasing, error behavior, and accepted input domain.
3. Choose the implementation level: pure F* for specifications and lemmas, Low* for memory-aware code extracted to C, HACL* for reusable verified primitives, EverCrypt for agile dispatch/composition, and Vale for hand-tuned assembly.
4. Prove functional correctness, memory safety, termination, and range/overflow obligations at the appropriate layer. Keep refinement steps and abstraction functions named and reviewable.
5. For EverCrypt-style dispatch, prove that feature detection and implementation selection preserve the common specification and do not bypass preconditions.
6. For Vale, connect assembly instruction semantics, calling convention, register/stack discipline, and machine state to the higher-level theorem. Record target-specific assumptions.
7. Analyze secret independence and leakage using the guarantees actually supplied by the selected libraries and extraction path; do not infer physical side-channel resistance from source-level control flow alone.
8. Run known-answer tests and differential tests against an independent implementation, then replay all proofs and extraction in a clean environment.
9. Publish the exact theorem chain, extracted-code hashes, compiler assumptions, external library boundaries, and non-claims.

## Output contract

- A pinned F*/Low*/Vale project and independent executable specification.
- Functional-correctness, memory-safety, and relevant leakage theorems.
- Extraction/compiler/assembly trust report and clean replay logs.
- Generated C or assembly artifacts with source-to-binary provenance.

## Non-negotiable guardrails

- Do not treat SMT success as a substitute for reviewing the specification and admitted assumptions.
- Do not claim that extracted C inherits properties not stated by the extraction theorem or build assumptions.
- Architecture-specific assembly proofs must remain tied to the exact instruction semantics and ABI.
- Agility and dispatch add proof obligations; they are not transparent implementation details.

## Related formal skills

- `constant-time-and-leakage-verification`
- `jasmin-easycrypt-high-assurance-crypto`

## Related cryptanalysis skills in this pack (optional)

- `lattice-kem-and-pke-analysis`
- `mode-mac-and-aead-analysis`

## Associated primary references

- **FSTAR-HOME** — [F*](https://fstar-lang.org/) (2026) — F* project. `official-project`.
- **PROJECT-EVEREST** — [Project Everest](https://project-everest.github.io/) (2026) — Project Everest. `official-project`.
- **HACL-REPO** — [HACL* repository](https://github.com/hacl-star/hacl-star) (2026) — HACL* project. `official-repository`.
- **HACL-MANUAL** — [HACL* and EverCrypt manual](https://hacl-star.github.io/) (2026) — HACL* project. `official-manual`.
- **EVERCRYPT19** — [EverCrypt: A Fast, Verified, Cross-Platform Cryptographic Provider](https://eprint.iacr.org/2019/757) (2019) — Jonathan Protzenko et al.. `research-paper`.
- **VALE-PAPER** — [Vale: Verifying High-Performance Cryptographic Assembly Code](https://www.microsoft.com/en-us/research/publication/vale-verifying-high-performance-cryptographic-assembly-code/) (2017) — Barry Bond et al.. `research-paper`.
- **VALE-REPO** — [Vale repository](https://github.com/project-everest/vale) (2026) — Project Everest. `official-repository`.

Bundled source metadata is in `references/REFERENCES.md`.
