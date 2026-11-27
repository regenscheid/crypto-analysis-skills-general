---
name: qrom-and-post-quantum-proof-modeling
description: "Models quantum adversary access, quantum random oracles, measurement/reprogramming losses, and post-quantum reductions without silently reusing classical ROM reasoning."
metadata:
  version: "0.1.0"
  display-name: "QROM and Post-Quantum Proof Modeling"
  category: "security-proofs"
  tags: "qrom, post-quantum, quantum-adversary, security-proof"
  requires: "classical or proposed PQ security proof, quantum access model, scheme parameters"
  produces: "QROM model, quantum-proof obligation map, loss analysis, classical-to-quantum gap report"
  optional: "true"
  namespace: "formal"
---

# QROM and Post-Quantum Proof Modeling

## Purpose

Models quantum adversary access, quantum random oracles, measurement/reprogramming losses, and post-quantum reductions without silently reusing classical ROM reasoning.

## Use this skill when

Use this skill when a security claim is intended to hold against quantum adversaries, especially for Fiat–Shamir, hash-and-sign, random-oracle transforms, KEMs, and proofs that observe or program oracle queries.

## Do not invoke automatically

Do not label a classical ROM proof “post-quantum” merely because the underlying hardness assumption is believed quantum resistant. The adversary’s access to the hash/random oracle and the reduction’s rewinding/programming techniques must also survive quantum queries.

## Optional entry contract

**Inputs**
- classical or proposed PQ security proof
- quantum access model
- scheme parameters

**Expected products**
- QROM model
- quantum-proof obligation map
- loss analysis
- classical-to-quantum gap report

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Define whether the adversary is classical, Q1, Q2, or a quantum algorithm with classical interfaces. Specify which oracles can be queried in superposition and how classical outputs/transcripts are measured.
2. Identify every classical proof step using query observation, lazy sampling, adaptive programming, rewinding, forking, copying state, or conditional resampling.
3. Select an appropriate QROM technique—measure-and-reprogram, compressed oracle, one-way-to-hiding, recording, or an available formal framework—and state its exact hypotheses and losses.
4. Model oracle domains and domain separation carefully. Quantum superposition queries make accidental overlap and implementation-level prefixes especially important.
5. Construct the quantum reduction interface and account for query complexity, runtime, success probability, measurement disturbance, guessing factors, and repeated extraction.
6. Check whether the formal tool actually models quantum adversaries or only records a quantum-hard assumption in a classical logic. Treat unsupported quantum steps as external lemmas with explicit trust.
7. Compare classical and quantum theorem statements and bounds. Record which security notions, adversary stages, or parameter claims remain unproved.
8. Use mechanized case studies such as EasyPQC or formally repaired Fiat–Shamir-with-aborts work as patterns, but revalidate scheme-specific assumptions.
9. Publish a QROM-specific non-claims section; avoid implying quantum implementation or quantum-circuit security from a computational reduction.

## Output contract

- An explicit classical/Q1/Q2 oracle and adversary model.
- A map of classical proof steps requiring quantum replacement.
- Quantum reduction lemmas and concrete loss calculation.
- A gap report identifying external or unmechanized quantum arguments.

## Non-negotiable guardrails

- Classical rewinding and oracle programming do not automatically work in the QROM.
- Do not conflate post-quantum assumptions with a post-quantum proof.
- QROM security remains an ideal-model claim and does not prove the concrete hash behaves randomly.
- Record whether quantum lemmas are machine checked or imported mathematical assumptions.

## Related formal skills

- `quantum-algorithm-circuit-and-resource-verification`
- `reduction-tightness-and-concrete-security`

## Related cryptanalysis skills in this pack (optional)

- `security-proof-rom-qrom-and-tightness-auditor`
- `quantum-symmetric-attack-analysis`

## Associated primary references

- **EASYPQC21** — [EasyPQC: Verifying Post-Quantum Cryptography](https://dl.acm.org/doi/10.1145/3460120.3484567) (2021) — EasyPQC authors. `research-paper`.
- **UNRUH17-QROM** — [Post-Quantum Security of Fiat-Shamir](https://eprint.iacr.org/2017/398) (2017) — Dominique Unruh. `research-paper`.
- **DILITHIUM-EC23** — [Fixing and Mechanizing the Security Proof of Fiat-Shamir with Aborts and Dilithium](https://eprint.iacr.org/2023/246) (2023) — Manuel Barbosa et al.. `research-paper`.
- **MLKEM-EC24** — [Formally verifying Kyber Episode V: Machine-checked IND-CCA security and correctness of ML-KEM in EasyCrypt](https://eprint.iacr.org/2024/843) (2024) — José Bacelar Almeida et al.. `research-paper`.
- **SQUIRREL-PQ** — [A Logic and an Interactive Prover for the Computational Post-Quantum Security of Protocols](https://eprint.iacr.org/2022/401) (2022) — Cas Cremers, Alex B. Grilo, Sam Scott, and others. `research-paper`.
- **XMSS-EC23** — [Machine-Checked Security for XMSS as in RFC 8391](https://eprint.iacr.org/2023/408) (2023) — Manuel Barbosa et al.. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
