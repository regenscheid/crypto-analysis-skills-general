---
name: lean-finite-algebra-and-number-theory
description: "Uses mathlib to formalize finite fields, modular rings, polynomials, quotient rings, matrices, groups, number theory, and exact algebraic identities arising in classical and post-quantum cryptography."
metadata:
  version: "0.1.0"
  display-name: "Lean Finite Algebra and Number Theory"
  category: "lean"
  tags: "lean, finite-fields, polynomials, number-theory, algebra"
  requires: "algebraic claim, chosen representations, mathlib environment"
  produces: "formal algebraic model, proved identities, representation lemmas, computable examples"
  optional: "true"
  namespace: "formal"
---

# Lean Finite Algebra and Number Theory

## Purpose

Uses mathlib to formalize finite fields, modular rings, polynomials, quotient rings, matrices, groups, number theory, and exact algebraic identities arising in classical and post-quantum cryptography.

## Use this skill when

Use this skill for S-box fields, NTTs, polynomial rings, elliptic-curve or group identities, coding-theory algebra, lattice basis relations, finite-field matrix arguments, and exact number-theoretic sublemmas.

## Do not invoke automatically

Do not invoke heavy abstract algebra before deciding whether the claim is about abstract elements, canonical representatives, executable arrays, or machine arithmetic. Proofs often fail because those levels are mixed.

## Optional entry contract

**Inputs**
- algebraic claim
- chosen representations
- mathlib environment

**Expected products**
- formal algebraic model
- proved identities
- representation lemmas
- computable examples

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Choose the weakest structure that captures the theorem: semiring, ring, field, finite field, Euclidean domain, module, algebra, group, or quotient. This improves reuse and reduces typeclass friction.
2. Define parameter conditions explicitly, including primality, irreducibility, roots of unity, dimensions, coprimality, subgroup order, and canonical reduction ranges.
3. Use existing mathlib constructions for `ZMod`, finite fields, polynomials, matrices, ideals, quotients, modules, and group actions. Inspect APIs and coercions before creating parallel structures.
4. Separate abstract identities from representation theorems. First prove the algebraic statement; then prove that arrays, coefficient vectors, Montgomery forms, or serialized elements implement it.
5. For NTT and convolution, state index domains, primitive-root assumptions, normalization convention, forward/inverse factors, cyclic versus negacyclic ring, and coefficient reduction.
6. For elliptic curves or groups, make exceptional cases, subgroup membership, identity points, coordinate charts, and denominator conditions explicit. Avoid informal cancellation over zero.
7. For coding and lattice claims, distinguish vector-space/module statements, integer lattices, quotient modules, norms, and chosen bases. Prove membership and transformation identities exactly.
8. Use normalization tactics only after the intended ring and coercions are established. Verify that automation is proving the desired equality rather than a coerced or weakened form.
9. Create small computed examples and source-linked lemmas for constants and parameter sets, then export stable abstractions for higher-level crypto skills.

## Output contract

- Lean definitions for the exact algebraic structures and parameter predicates.
- Abstract identities and separate representation/canonicalization theorems.
- Executable examples and parameter-instantiation proofs.
- A list of any unformalized external algebra facts or primality/irreducibility certificates.

## Non-negotiable guardrails

- Do not cancel, divide, or invert without proving nonzero conditions.
- Do not treat polynomial equality modulo an ideal as literal coefficient equality.
- Do not hide a failed parameter condition in an axiom for a standardized instance; certify it.
- When automation relies on normalization, preserve a human-readable statement of the algebraic transformation.

## Related formal skills

- `computer-algebra-witness-certification`
- `lean-metaprogramming-and-custom-tactics`

## Related cryptanalysis skills in this pack (optional)

- `elliptic-curve-discrete-log-and-ecc-analysis`
- `lattice-hard-problem-and-estimator-analysis`
- `algebraic-sat-smt-cp-and-cube-analysis`

## Associated primary references

- **MATHLIB-DOCS** — [Mathlib 4 Documentation](https://leanprover-community.github.io/mathlib4_docs/) (2026) — Lean community. `official-documentation`.
- **LEAN-TPIL** — [Theorem Proving in Lean 4](https://leanprover.github.io/theorem_proving_in_lean4/) (2024) — Jeremy Avigad et al.. `official-text`.
- **FIAT-CRYPTO19** — [Simple High-Level Code for Cryptographic Arithmetic—with Proofs, Without Compromises](https://adam.chlipala.net/papers/FiatCryptoSP19/) (2019) — Andres Erbsen et al.. `research-paper`.
- **SAGEMATH-HOME** — [SageMath](https://www.sagemath.org/) (2026) — SageMath project. `official-project`.
- **FLINT** — [FLINT](https://flintlib.org/) (2026) — FLINT project. `official-project`.
- **NTL-HOME** — [NTL: A Library for doing Number Theory](https://libntl.org/) (2026) — Victor Shoup. `official-project`.

Bundled source metadata is in `references/REFERENCES.md`.
