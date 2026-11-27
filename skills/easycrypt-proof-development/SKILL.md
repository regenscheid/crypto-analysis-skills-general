---
name: easycrypt-proof-development
description: "Develops and checks computational cryptographic proofs in EasyCrypt using modules, probabilistic programs, relational judgments, equivalence reasoning, and concrete bounds."
metadata:
  version: "0.1.0"
  display-name: "EasyCrypt Proof Development"
  category: "security-proofs"
  tags: "easycrypt, pRHL, security-proof, game-hopping"
  requires: "formal games, EasyCrypt environment, proof obligation plan"
  produces: "EasyCrypt development, checked lemmas, game and bound report, replay package"
  optional: "true"
  namespace: "formal"
---

# EasyCrypt Proof Development

## Purpose

Develops and checks computational cryptographic proofs in EasyCrypt using modules, probabilistic programs, relational judgments, equivalence reasoning, and concrete bounds.

## Use this skill when

Use this skill for game-based computational security arguments, especially when adversarial modules, probabilistic program equivalence, oracle simulation, and concrete advantage bounds dominate the work.

## Do not invoke automatically

Do not use EasyCrypt for a purely finite bit-vector search, ordinary functional equality, or symbolic protocol reachability when Lean, SAT certification, SAW, or a protocol prover is a better semantic match.

## Optional entry contract

**Inputs**
- formal games
- EasyCrypt environment
- proof obligation plan

**Expected products**
- EasyCrypt development
- checked lemmas
- game and bound report
- replay package

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Pin the EasyCrypt version, prover backends, libraries, and project sources. Reproduce official examples before beginning a large development.
2. Encode types, operators, distributions, construction modules, adversary interfaces, and games independently of the desired proof script. Keep source and implementation variants distinct.
3. Use relational judgments to align memories, modules, random samplings, and oracle state. State invariants before attempting automation.
4. Decompose proofs into local procedure equivalences, module-level equivalences, lossless/termination obligations, probability bounds, and final advantage theorems.
5. Apply eager/lazy sampling, swapping, inlining, code motion, oracle replacement, and up-to-bad reasoning only with the side conditions required by the logic.
6. Manage external SMT/prover calls deterministically and inspect unresolved goals. Record which obligations are reconstructed or trusted by the EasyCrypt environment.
7. Validate games and theorem statements with toy constructions and sanity adversaries. Compare to source pseudocode and exact implementation encodings.
8. Recompute concrete bounds and ensure resource variables are not accidentally abstracted away by module types or adversary assumptions.
9. Replay the entire development in isolation, forbid `admit`, and publish the exact theorem names, assumptions, and source versions.

## Output contract

- A clean EasyCrypt project with modular game definitions and proofs.
- A theorem-by-theorem game-hop and assumption map.
- Concrete bound expressions and parameter instantiations.
- A pinned replay environment and audit report.

## Non-negotiable guardrails

- Do not hide difficult cryptographic facts as uninterpreted axioms without explicit trust classification.
- Losslessness and termination assumptions can be security-critical; do not discharge them casually.
- Do not equate code-level functional correctness with the security proof unless a correspondence theorem connects them.
- Classical EasyCrypt developments do not automatically establish QROM security.

## Related formal skills

- `game-hopping-and-hybrid-proof`
- `shannonprover-agentic-easycrypt`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **EASYCRYPT-HOME** — [EasyCrypt](https://www.easycrypt.info/) (2026) — EasyCrypt project. `official-project`.
- **EASYCRYPT-REPO** — [EasyCrypt repository](https://github.com/EasyCrypt/easycrypt) (2026) — EasyCrypt project. `official-repository`.
- **EASYCRYPT-TUTORIALS** — [EasyCrypt tutorials](https://easycrypt.gitlab.io/easycrypt-web/docs/tutorials/) (2026) — EasyCrypt project. `official-manual`.
- **EASYCRYPT11** — [EasyCrypt: Automated Reasoning for Security Proofs](https://eprint.iacr.org/2011/101) (2011) — Gilles Barthe et al.. `research-paper`.
- **MLKEM-EC24** — [Formally verifying Kyber Episode V: Machine-checked IND-CCA security and correctness of ML-KEM in EasyCrypt](https://eprint.iacr.org/2024/843) (2024) — José Bacelar Almeida et al.. `research-paper`.
- **DILITHIUM-EC23** — [Fixing and Mechanizing the Security Proof of Fiat-Shamir with Aborts and Dilithium](https://eprint.iacr.org/2023/246) (2023) — Manuel Barbosa et al.. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
