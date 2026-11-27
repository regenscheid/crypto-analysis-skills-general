---
name: squirrel-computational-and-pq-protocol-proof
description: "Uses Squirrel’s interactive higher-order logic for trace and equivalence properties of stateful protocols, with explicit computational assumptions and post-quantum soundness where supported."
metadata:
  version: "0.1.0"
  display-name: "Squirrel Computational and Post-Quantum Protocol Proof"
  category: "protocol-verification"
  tags: "squirrel, protocol, computational, post-quantum, equivalence"
  requires: "Squirrel protocol model, security statement, primitive assumptions and PQ model"
  produces: "Squirrel proof, assumption/soundness report, trace or equivalence theorem, replay package"
  optional: "true"
  namespace: "formal"
---

# Squirrel Computational and Post-Quantum Protocol Proof

## Purpose

Uses Squirrel’s interactive higher-order logic for trace and equivalence properties of stateful protocols, with explicit computational assumptions and post-quantum soundness where supported.

## Use this skill when

Use this skill when an interactive computational protocol proof, trace logic, equivalence reasoning, or a supported post-quantum protocol model is more suitable than fully automatic symbolic analysis.

## Do not invoke automatically

Do not label a proof post-quantum merely because the primitives are PQC. Confirm that the logic, adversary, oracle access, assumptions, and proof rules used by the development have the required post-quantum soundness.

## Optional entry contract

**Inputs**
- Squirrel protocol model
- security statement
- primitive assumptions and PQ model

**Expected products**
- Squirrel proof
- assumption/soundness report
- trace or equivalence theorem
- replay package

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Pin Squirrel and freeze the protocol, state, message algebra, oracle interfaces, corruption/reveal events, and exact trace or equivalence property.
2. Encode names, actions, macros, state updates, conditionals, and adversarial observations. Validate honest traces and ensure encodings/errors relevant to the property are represented.
3. Declare cryptographic assumptions at the right interface and security notion. Distinguish classical, post-quantum classical-query, and superposition-query assumptions.
4. Decompose the proof into trace, freshness, dependency, indistinguishability, and cryptographic steps. Use automation only after the goal’s semantic form is understood.
5. For equivalence proofs, track frames, conditionals, state, and side conditions carefully and ensure the compared systems differ only where intended.
6. For PQ claims, identify the soundness theorem and restrictions that justify each rule; do not import classical rewinding or oracle programming silently.
7. Inspect all admitted lemmas and assumptions, then replay the proof in a clean environment.
8. Publish the theorem, model, computational assumptions, soundness scope, replay files, and implementation/bit-level non-claims.

## Output contract

- A checked Squirrel model and trace/equivalence proof.
- Classical/PQ assumption and soundness map.
- Executability/vacuity and model-fidelity tests.
- Pinned replay and human-readable theorem report.

## Non-negotiable guardrails

- Post-quantum soundness is rule- and model-specific.
- Do not abstract away encodings, validation, or state that are central to the attack surface.
- Interactive lemmas must not assume the desired equivalence in disguised form.
- Keep computational proof separate from code and side-channel correctness.

## Related formal skills

- `cryptoverif-computational-protocol-analysis`
- `qrom-and-post-quantum-proof-modeling`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **SQUIRREL-HOME** — [Squirrel Prover](https://squirrel-prover.github.io/) (2026) — Squirrel project. `official-project`.
- **SQUIRREL-REPO** — [Squirrel repository](https://github.com/squirrel-prover/squirrel-prover) (2026) — Squirrel project. `official-repository`.
- **SQUIRREL-PQ** — [A Logic and an Interactive Prover for the Computational Post-Quantum Security of Protocols](https://eprint.iacr.org/2022/401) (2022) — Cas Cremers, Alex B. Grilo, Sam Scott, and others. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
