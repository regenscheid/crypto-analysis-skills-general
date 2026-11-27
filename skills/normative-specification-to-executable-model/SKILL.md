---
name: normative-specification-to-executable-model
description: "Produces an independently derived executable formal model from a standard, submission, RFC, paper algorithm, or other normative source and validates it before implementation comparison."
metadata:
  version: "0.1.0"
  display-name: "Normative Specification to Executable Model"
  category: "implementation-verification"
  tags: "specification, standard, executable-model, validation"
  requires: "normative source, parameter sets, test vectors and errata"
  produces: "executable formal specification, source crosswalk, vector results, ambiguity and errata register"
  optional: "true"
  namespace: "formal"
---

# Normative Specification to Executable Model

## Purpose

Produces an independently derived executable formal model from a standard, submission, RFC, paper algorithm, or other normative source and validates it before implementation comparison.

## Use this skill when

Use this skill when the target is a standardized or published cryptographic algorithm and later work will prove code refinement, derive test oracles, or reason about its exact behavior.

## Do not invoke automatically

Do not derive the “specification” from the implementation being verified. An independently transcribed source model is the main defense against proving that code equals itself.

## Optional entry contract

**Inputs**
- normative source
- parameter sets
- test vectors and errata

**Expected products**
- executable formal specification
- source crosswalk
- vector results
- ambiguity and errata register

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Freeze all normative sources, revisions, errata, parameter tables, referenced primitives, wire-format documents, and official test vectors. Resolve precedence rules among them.
2. Transcribe algorithms into pure, total functions or explicit result types. Preserve loop bounds, indexing, byte order, randomness, rejection, validation, malformed-input behavior, and failure values.
3. Model mathematical domains exactly: machine words, residues, finite fields, polynomial rings, distributions, floating point, or abstract primitives. Record every idealization.
4. Create clause/line-to-definition annotations and a decision log for ambiguous prose, typographical defects, and inferred preconditions.
5. Instantiate every official parameter set and prove/static-check table consistency, lengths, ranges, constants, and algebraic prerequisites.
6. Run official vectors in both directions and create negative vectors for invalid encodings, boundaries, and errors. Compare with at least one independent implementation when available.
7. Prove basic self-consistency properties—round trips, inverse transforms, length preservation, range invariants, or deterministic replay—without assuming the implementation.
8. Separate source-faithful specification from optimized/code-shaped auxiliary specifications. Any later equivalence among them becomes an explicit theorem.
9. Publish unresolved ambiguities and suspected normative defects rather than choosing whichever interpretation matches existing code silently.

## Output contract

- An executable, source-derived formal specification.
- A line/clause-level crosswalk and ambiguity/errata register.
- Official and negative test-vector results.
- Foundational consistency lemmas and parameter proofs.

## Non-negotiable guardrails

- Passing vectors is necessary validation but not proof of full specification fidelity.
- Do not erase errors by returning default values.
- Do not impose implementation limitations as normative preconditions unless the source does so.
- Preserve exact differences among source editions and draft/final standards.

## Related formal skills

- `implementation-refinement-and-equivalence`
- `specification-validation-and-vacuity-audit`

## Related cryptanalysis skills in this pack (optional)

- `scheme-structure-and-assumption-mapper`
- `primitive-structure-and-assumption-mapper`

## Associated primary references

- **SYMCRYPT-VERIFIED26** — [Verifying Rust cryptography in SymCrypt: from standards to code](https://www.microsoft.com/en-us/research/blog/verifying-rust-cryptography-in-symcrypt-from-standards-to-code/) (2026) — Microsoft Research. `official-project-report`.
- **MLKEM-EC24** — [Formally verifying Kyber Episode V: Machine-checked IND-CCA security and correctness of ML-KEM in EasyCrypt](https://eprint.iacr.org/2024/843) (2024) — José Bacelar Almeida et al.. `research-paper`.
- **KYBER-IMPL23** — [Formally verifying Kyber Episode IV: Implementation Correctness](https://eprint.iacr.org/2023/215) (2023) — José Bacelar Almeida et al.. `research-paper`.
- **HBS-CHAIN26** — [Completing the Chain: Verified Implementations of Hash-Based Signatures and Their Security](https://eprint.iacr.org/2026/134) (2026) — Manuel Barbosa et al.. `research-paper`.
- **LEAN-REF** — [Lean Language Reference](https://lean-lang.org/doc/reference/latest/) (2026) — Lean project. `official-manual`.

Bundled source metadata is in `references/REFERENCES.md`.
