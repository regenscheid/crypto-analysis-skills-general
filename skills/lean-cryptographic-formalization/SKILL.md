---
name: lean-cryptographic-formalization
description: "Builds maintainable Lean 4 definitions and theorems for cryptographic algorithms, attack witnesses, algebraic structures, encodings, and exact correctness properties."
metadata:
  version: "0.1.0"
  display-name: "Lean Cryptographic Formalization"
  category: "lean"
  tags: "lean, cryptography, formalization, mathlib"
  requires: "formalization charter, source specification, Lean project"
  produces: "Lean definitions, executable specification, theorem interfaces, examples and validation lemmas"
  optional: "true"
  namespace: "formal"
---

# Lean Cryptographic Formalization

## Purpose

Builds maintainable Lean 4 definitions and theorems for cryptographic algorithms, attack witnesses, algebraic structures, encodings, and exact correctness properties.

## Use this skill when

Use this skill when Lean is selected as the general-purpose proof assistant or certificate endpoint for a cryptographic claim. It is suitable for mathematical definitions, finite algorithms, exact witness checkers, implementation specifications, and many correctness or bound lemmas.

## Do not invoke automatically

Do not choose Lean solely because other skills in this pack use it. EasyCrypt, Tamarin, CryptoVerif, Jasmin, Verus, or a certified solver may be a better primary environment for probabilistic reductions, protocols, optimized code, or large finite searches.

## Optional entry contract

**Inputs**
- formalization charter
- source specification
- Lean project

**Expected products**
- Lean definitions
- executable specification
- theorem interfaces
- examples and validation lemmas

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Create a pinned Lean 4 project and import only the required mathlib modules. Establish namespaces that separate normative specifications, implementation models, attack artifacts, and proofs.
2. Translate source types explicitly: fixed-size bytes and words, vectors and matrices, finite fields, quotient polynomial rings, distributions, structured keys, encodings, and failure results. Avoid ambiguous `Nat` stand-ins for machine values.
3. Define pure executable functions for the mathematical algorithm whenever possible. Keep parsing, validation, randomness, and failure behavior visible rather than hidden behind partial functions or defaults.
4. Attach source locators and parameter provenance to definitions in comments or metadata. Give independent names to source-derived and code-derived models.
5. Validate the transcription with official vectors, round trips, algebraic invariants, small exhaustive examples, and comparison to an independent implementation. Record that these are validation evidence, not universal proofs.
6. Choose theorem statements that expose preconditions and results directly. Prefer equality or well-defined refinement relations over vague postconditions that could hold for incorrect implementations.
7. Develop reusable helper libraries for byte order, modular arithmetic, polynomial encodings, finite sums, exact probabilities, and cryptanalytic witness formats rather than re-solving representation issues in every theorem.
8. Use proof automation incrementally and keep the trusted path visible. Inspect generated proof terms or dependency reports for custom tactics and reflection.
9. Package examples, theorem IDs, source crosswalks, and non-claims so other formal skills can consume the development without loading unrelated cryptanalysis context.

## Output contract

- A compiling Lean project with source-derived definitions and examples.
- Public theorem interfaces and helper lemmas organized for reuse.
- A source-to-definition crosswalk and test-vector results.
- An explicit list of remaining semantic and trust assumptions.

## Non-negotiable guardrails

- Do not model cryptographic randomness as an arbitrary fixed value unless the theorem is explicitly deterministic.
- Do not use `Inhabited` defaults to erase parse failures or invalid inputs.
- Do not conflate equality in a quotient/ring with equality of canonical encodings.
- Keep formal definitions independent enough that implementation equivalence is non-circular.

## Related formal skills

- `lean-finite-algebra-and-number-theory`
- `lean-bitvectors-and-word-arithmetic`
- `normative-specification-to-executable-model`

## Related cryptanalysis skills in this pack (optional)

- `scheme-structure-and-assumption-mapper`
- `primitive-structure-and-assumption-mapper`

## Associated primary references

- **LEAN-HOME** — [Lean](https://lean-lang.org/) (2026) — Lean project. `official-project`.
- **LEAN-REF** — [Lean Language Reference](https://lean-lang.org/doc/reference/latest/) (2026) — Lean project. `official-manual`.
- **LEAN-TPIL** — [Theorem Proving in Lean 4](https://leanprover.github.io/theorem_proving_in_lean4/) (2024) — Jeremy Avigad et al.. `official-text`.
- **MATHLIB-REPO** — [Mathlib 4](https://github.com/leanprover-community/mathlib4) (2026) — Lean community. `official-repository`.
- **MATHLIB-DOCS** — [Mathlib 4 Documentation](https://leanprover-community.github.io/mathlib4_docs/) (2026) — Lean community. `official-documentation`.
- **LEAN-FAQ** — [Lean FAQ](https://lean-lang.org/faq/) (2026) — Lean project. `official-documentation`.

Bundled source metadata is in `references/REFERENCES.md`.
