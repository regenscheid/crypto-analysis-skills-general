---
name: reduction-tightness-and-concrete-security
description: "Recomputes and mechanizes the complete quantitative loss of a reduction, including query powers, multi-user factors, guessing, statistical terms, correctness, runtime, and success amplification."
metadata:
  version: "0.1.0"
  display-name: "Reduction Tightness and Concrete Security"
  category: "security-proofs"
  tags: "concrete-security, tightness, advantage-bound, resources"
  requires: "verified or proposed reduction, parameter sets, adversary resource model"
  produces: "symbolic bound, concrete instantiations, sensitivity analysis, tightness findings"
  optional: "true"
  namespace: "formal"
---

# Reduction Tightness and Concrete Security

## Purpose

Recomputes and mechanizes the complete quantitative loss of a reduction, including query powers, multi-user factors, guessing, statistical terms, correctness, runtime, and success amplification.

## Use this skill when

Use this skill when a theorem’s practical meaning depends on its exact advantage or resource loss, particularly for PQC parameter claims, ROM/QROM proofs, multi-user settings, and reductions with correctness failures.

## Do not invoke automatically

Do not quote a headline theorem or asymptotic reduction without carrying all constants and resource transformations to the concrete parameters actually claimed.

## Optional entry contract

**Inputs**
- verified or proposed reduction
- parameter sets
- adversary resource model

**Expected products**
- symbolic bound
- concrete instantiations
- sensitivity analysis
- tightness findings

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Extract the exact theorem and define every advantage function, resource tuple, query count, runtime overhead, and assumption instance. Preserve maximum/supremum conventions.
2. Reconstruct the algebraic bound from verified hop lemmas or the source proof, recording each loss term and its provenance.
3. Account for multi-user, multi-target, sessions, signatures/ciphertexts, random-oracle domains, repetitions, forks, rewinding, guessing indices, and abort probability.
4. Include correctness/decryption failure, statistical sampling distance, rejection/termination probability, and implementation-to-specification gaps only where the theorem justifies composition.
5. Map reduction resources to the underlying problem instance: dimensions, modulus, samples, noise distribution, oracle access, success target, and time. Do not compare incomparable cost models.
6. Perform exact rational/integer arithmetic and conservative rounding. Generate parameter tables and sensitivity ranges rather than one favorable exponent.
7. Check the reduction’s success is nontrivial after subtracting losses and that amplification costs do not exceed the stated resources.
8. Compare classical, ROM, QROM, single-user, and multi-user bounds separately. A tight classical proof may have a large quantum reprogramming loss.
9. Publish a machine-readable bound expression that can be re-evaluated when parameters, query limits, or assumption estimates change.

## Output contract

- A symbolic bound with source-linked terms.
- Concrete parameter tables in explicit units and conservative rounding.
- Reduction resource mappings and success conditions.
- Tightness bottlenecks and sensitivity analysis.

## Non-negotiable guardrails

- Do not convert proof advantage directly into “bits of security” without defining the adversary cost and success target.
- Do not omit negative or dominating terms because they make the result vacuous.
- Keep heuristic hardness estimates separate from the proved reduction.
- Use exact arithmetic or rigorously bounded numerics for published exponents.

## Related formal skills

- `lean-probability-combinatorics-and-bounds`
- `qrom-and-post-quantum-proof-modeling`

## Related cryptanalysis skills in this pack (optional)

- `public-key-attack-complexity-and-success-auditor`
- `symmetric-attack-complexity-and-success-auditor`

## Associated primary references

- **EASYCRYPT11** — [EasyCrypt: Automated Reasoning for Security Proofs](https://eprint.iacr.org/2011/101) (2011) — Gilles Barthe et al.. `research-paper`.
- **MLKEM-EC24** — [Formally verifying Kyber Episode V: Machine-checked IND-CCA security and correctness of ML-KEM in EasyCrypt](https://eprint.iacr.org/2024/843) (2024) — José Bacelar Almeida et al.. `research-paper`.
- **SPHINCS-EC24** — [A Tight Security Proof for SPHINCS+, Formally Verified](https://eprint.iacr.org/2024/910) (2024) — Manuel Barbosa et al.. `research-paper`.
- **DILITHIUM-EC23** — [Fixing and Mechanizing the Security Proof of Fiat-Shamir with Aborts and Dilithium](https://eprint.iacr.org/2023/246) (2023) — Manuel Barbosa et al.. `research-paper`.
- **UNRUH17-QROM** — [Post-Quantum Security of Fiat-Shamir](https://eprint.iacr.org/2017/398) (2017) — Dominique Unruh. `research-paper`.
- **ARB** — [Arb: Arbitrary-Precision Ball Arithmetic](https://arblib.org/) (2026) — Arb project. `official-project`.

Bundled source metadata is in `references/REFERENCES.md`.
