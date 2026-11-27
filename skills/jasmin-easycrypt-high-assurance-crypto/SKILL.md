---
name: jasmin-easycrypt-high-assurance-crypto
description: "Verifies high-performance cryptographic routines written in Jasmin by connecting assembly-like source, compiler guarantees, leakage models, and EasyCrypt functional or security proofs."
metadata:
  version: "0.1.0"
  display-name: "Jasmin and EasyCrypt High-Assurance Crypto"
  category: "implementation-verification"
  tags: "jasmin, easycrypt, assembly, compiler, constant-time"
  requires: "Jasmin program, mathematical specification, target architecture and leakage model"
  produces: "Jasmin verification project, EasyCrypt proof, compiled implementation, compiler and leakage audit"
  optional: "true"
  namespace: "formal"
---

# Jasmin and EasyCrypt High-Assurance Crypto

## Purpose

Verifies high-performance cryptographic routines written in Jasmin by connecting assembly-like source, compiler guarantees, leakage models, and EasyCrypt functional or security proofs.

## Use this skill when

Use this skill for performance-critical cryptographic routines where Jasmin’s controlled low-level language and verified compilation/proof ecosystem are a better fit than verifying arbitrary handwritten assembly.

## Do not invoke automatically

Do not use it to verify a binary that cannot be represented faithfully in Jasmin, or to claim protocol/construction security when only a primitive implementation has been proved correct.

## Optional entry contract

**Inputs**
- Jasmin program
- mathematical specification
- target architecture and leakage model

**Expected products**
- Jasmin verification project
- EasyCrypt proof
- compiled implementation
- compiler and leakage audit

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Pin Jasmin, EasyCrypt, architecture, compiler revision, assembler/linker, and all generated files. Record whether the compiler theorem covers the selected backend and optimizations.
2. Write or review a pure specification of the primitive and a Jasmin-level functional contract. State memory layout, aliasing, alignment, input ranges, output encoding, and failure behavior.
3. Prove local arithmetic and bit-level lemmas, then prove functional equivalence between the Jasmin routine and the specification for all permitted inputs.
4. Model leakage explicitly: branches, memory addresses, instruction classes, variable latency, or the leakage trace supported by the tool. Prove the property actually represented by that model.
5. For probabilistic or security properties, extract or connect the relevant Jasmin semantics to EasyCrypt and keep implementation correctness separate from the game-based theorem.
6. Inspect generated assembly and validate calling conventions, stack use, register preservation, and target-feature assumptions. Test on the exact supported architecture.
7. Use official vectors plus randomized differential testing against an independent model. Mutate code paths to ensure the proof or tests fail when expected.
8. Replay the compiler and proofs from clean sources and publish source, theorem, architecture, compiler, and leakage scope together.

## Output contract

- Jasmin source, specifications, and proof scripts.
- Functional-equivalence and selected leakage theorems.
- Compiled assembly with compiler/architecture provenance.
- Independent test vectors and clean replay report.

## Non-negotiable guardrails

- Constant-time in a source-level leakage model is not a claim about power, EM, speculative execution, or every microarchitecture.
- Do not omit aliasing, alignment, or CPU-feature preconditions.
- Do not conflate compiler correctness with correctness of assembler, linker, loader, or hardware.
- EasyCrypt proof obligations must use the same semantics and encodings as the implementation theorem.

## Related formal skills

- `constant-time-and-leakage-verification`
- `easycrypt-proof-development`

## Related cryptanalysis skills in this pack (optional)

- `primitive-structure-and-assumption-mapper`

## Associated primary references

- **JASMIN-HOME** — [Jasmin](https://formosa-crypto.org/tools/jasmin) (2026) — Formosa Crypto. `official-project`.
- **JASMIN-DOCS** — [Jasmin documentation](https://jasmin-lang.readthedocs.io/) (2026) — Jasmin project. `official-manual`.
- **JASMIN-REPO** — [Jasmin repository](https://github.com/jasmin-lang/jasmin) (2026) — Jasmin project. `official-repository`.
- **JASMIN17** — [Jasmin: High-Assurance and High-Speed Cryptography](https://doi.org/10.1145/3133956.3134078) (2017) — José Bacelar Almeida et al.. `research-paper`.
- **LAST-MILE20** — [The Last Mile: High-Assurance and High-Speed Cryptographic Implementations](https://arxiv.org/abs/1904.04606) (2020) — José Bacelar Almeida et al.. `research-paper`.
- **EASYCRYPT-HOME** — [EasyCrypt](https://www.easycrypt.info/) (2026) — EasyCrypt project. `official-project`.

Bundled source metadata is in `references/REFERENCES.md`.
