---
name: lattice-witness-and-bound-certification
description: "Validates lattice bases, transformations, short/close vectors, decoded secrets, embeddings, norms, and claimed bounds while separating heuristic reduction performance from exact mathematical evidence."
metadata:
  version: "0.1.0"
  display-name: "Lattice Witness and Bound Certification"
  category: "certified-computation"
  tags: "lattice, lll, bkz, svp, cvp, witness"
  requires: "lattice instance and representation, candidate vector/secret, claimed norm or recovery result"
  produces: "exact membership/recovery proof, norm and transformation checks, heuristic/bound classification, replay artifacts"
  optional: "true"
  namespace: "formal"
---

# Lattice Witness and Bound Certification

## Purpose

Validates lattice bases, transformations, short/close vectors, decoded secrets, embeddings, norms, and claimed bounds while separating heuristic reduction performance from exact mathematical evidence.

## Use this skill when

Use this skill when a lattice attack, hidden-number attack, NTRU/Falcon analysis, decoding embedding, or parameter experiment produces a candidate vector or secret whose validity can be checked exactly, or when a rigorous bound is claimed.

## Do not invoke automatically

Do not confuse successful BKZ output with proof of shortestness, failure with hardness, or an estimator with a theorem. Formal optimality is usually much harder than validating a recovered key.

## Optional entry contract

**Inputs**
- lattice instance and representation
- candidate vector/secret
- claimed norm or recovery result

**Expected products**
- exact membership/recovery proof
- norm and transformation checks
- heuristic/bound classification
- replay artifacts

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Freeze the integer/rational lattice basis, row/column convention, scaling, embedding, modulus, target vector, norm, and exact relation to the cryptographic instance.
2. Validate dimensions, determinants/indexes where relevant, and the basis-generation code against small hand-checkable instances.
3. For a candidate vector, prove lattice membership using an exact coefficient vector or unimodular transformation and compute its norm exactly or with rigorous bounds.
4. For key/secret recovery, verify the public relation independently and check all scheme-specific distribution/range/canonicality conditions. A vector that is short but not the real secret is not recovery.
5. For CVP/BDD or embedding attacks, check the decoded difference, target relation, embedding parameter, and uniqueness/decoding-radius assumptions.
6. Record fplll/fpylll version, floating precision, BKZ block sizes, pruning, seeds, tours, threads, and stopping criteria. Classify these as search methodology, not proof.
7. If shortestness, uniqueness, or a lower bound is claimed, require enumeration certificates, exact branch-and-bound evidence, a theorem, or another independently checkable exclusion proof.
8. Cross-check the witness with exact arithmetic and an independent implementation; preserve failed runs and selection bias when estimating success.
9. Publish instance, basis, transformation coefficients, vector/secret, exact checks, search parameters, and the precise proved versus heuristic claims.

## Output contract

- Exact lattice-membership and norm evidence.
- Independent cryptographic secret/witness verification.
- Reproducible reduction/search configuration and run logs.
- A separate statement for found-vector validity, success estimates, and any optimality bound.

## Non-negotiable guardrails

- A short vector is not necessarily the shortest or secret vector.
- Floating-point Gram–Schmidt and pruning affect search reliability and must be recorded.
- Estimator output and Gaussian-heuristic reasoning remain heuristic unless separately proved.
- Do not infer security from unsuccessful reduction runs.

## Related formal skills

- `computer-algebra-witness-certification`
- `optimization-and-optimality-certification`

## Related cryptanalysis skills in this pack (optional)

- `lattice-hard-problem-and-estimator-analysis`
- `nonce-randomness-and-hidden-number-analysis`

## Associated primary references

- **FPLLL-REPO** — [fplll](https://github.com/fplll/fplll) (2026) — fplll project. `official-repository`.
- **FPYLLL-REPO** — [fpylll](https://github.com/fplll/fpylll) (2026) — fplll project. `official-repository`.
- **SAGEMATH-HOME** — [SageMath](https://www.sagemath.org/) (2026) — SageMath project. `official-project`.
- **NTL-HOME** — [NTL: A Library for doing Number Theory](https://libntl.org/) (2026) — Victor Shoup. `official-project`.

Bundled source metadata is in `references/REFERENCES.md`.
