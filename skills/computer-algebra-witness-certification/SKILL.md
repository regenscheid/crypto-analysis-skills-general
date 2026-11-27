---
name: computer-algebra-witness-certification
description: "Uses SageMath, Singular, FLINT, NTL, or other computer algebra systems for discovery while converting factors, roots, identities, ideal membership, rank, or solution claims into exact independently checkable evidence."
metadata:
  version: "0.1.0"
  display-name: "Computer Algebra Witness Certification"
  category: "certified-computation"
  tags: "computer-algebra, sage, singular, groebner, exact-witness"
  requires: "algebraic claim or candidate, ring/field/domain definition, CAS computation"
  produces: "exact witness/certificate, independent checker, CAS provenance, formalization option"
  optional: "true"
  namespace: "formal"
---

# Computer Algebra Witness Certification

## Purpose

Uses SageMath, Singular, FLINT, NTL, or other computer algebra systems for discovery while converting factors, roots, identities, ideal membership, rank, or solution claims into exact independently checkable evidence.

## Use this skill when

Use this skill when cryptanalysis produces algebraic objects whose correctness can be verified exactly even if discovery used complex or untrusted CAS algorithms.

## Do not invoke automatically

Do not demand a full proof-assistant reimplementation of every Gröbner or factorization algorithm when a compact exact witness settles the claim. Conversely, do not accept opaque CAS text output for a universal or optimality assertion.

## Optional entry contract

**Inputs**
- algebraic claim or candidate
- ring/field/domain definition
- CAS computation

**Expected products**
- exact witness/certificate
- independent checker
- CAS provenance
- formalization option

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Define the coefficient domain, quotient relations, term order, variable order, embeddings, characteristic, precision, and canonical representations explicitly.
2. Classify the claim: polynomial identity, root/solution, factorization, ideal membership, Gröbner basis, elimination result, rank/kernel, determinant, resultant, interpolation, or count/nonexistence.
3. For positive claims, export compact exact evidence: factors, roots, coefficients expressing ideal membership, matrix transformations, kernel vectors, or explicit substitutions.
4. Check the witness with a small independent exact implementation or a second CAS and, for high-value results, reconstruct the key equality in Lean/Rocq/Isabelle.
5. For Gröbner-basis claims, verify generators reduce to zero, critical pairs or a certified criterion as appropriate, and preserve the exact term order and coefficient field. Distinguish “basis computed” from conclusions derived from it.
6. For factor/primality claims, multiply factors exactly and provide primality certificates or qualified factorization status when needed.
7. For nonexistence/dimension/counting claims, identify a complete certificate or theorem; a CAS failure to solve is not evidence.
8. Pin software, algorithms/options, seeds, memory limits, and input/output serialization. Avoid floating approximations unless rigorously enclosed.
9. Publish source equations, witness, checker, derivation of the cryptanalytic consequence, and remaining trust assumptions.

## Output contract

- Exact serialized algebraic witness and domain definition.
- Independent checker or formal theorem for the decisive relation.
- CAS command/version/provenance record.
- A clear boundary between discovered evidence and universal claims.

## Non-negotiable guardrails

- CAS output is not self-authenticating.
- Term order, field, quotient, and variable conventions can change the result completely.
- Numerical roots do not establish exact solutions without certification.
- Failure, timeout, or degree explosion does not prove nonexistence or hardness.

## Related formal skills

- `lean-finite-algebra-and-number-theory`
- `formal-claim-and-model-authoring`

## Related cryptanalysis skills in this pack (optional)

- `multivariate-public-key-analysis`
- `algebraic-sat-smt-cp-and-cube-analysis`

## Associated primary references

- **SAGEMATH-HOME** — [SageMath](https://www.sagemath.org/) (2026) — SageMath project. `official-project`.
- **SAGEMATH-TUTORIAL** — [SageMath Tutorial](https://doc.sagemath.org/html/en/tutorial/) (2026) — SageMath project. `official-manual`.
- **SINGULAR-HOME** — [Singular](https://www.singular.uni-kl.de/) (2026) — Singular project. `official-project`.
- **FLINT** — [FLINT](https://flintlib.org/) (2026) — FLINT project. `official-project`.
- **NTL-HOME** — [NTL: A Library for doing Number Theory](https://libntl.org/) (2026) — Victor Shoup. `official-project`.

Bundled source metadata is in `references/REFERENCES.md`.
