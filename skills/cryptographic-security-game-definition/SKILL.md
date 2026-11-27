---
name: cryptographic-security-game-definition
description: "Defines adversarial experiments, oracles, resources, success events, advantages, correctness events, and multi-user or quantum variants precisely enough for mechanized security proofs."
metadata:
  version: "0.1.0"
  display-name: "Cryptographic Security Game Definition"
  category: "security-proofs"
  tags: "security-game, adversary, advantage, cryptography"
  requires: "construction specification, claimed security property, adversary model"
  produces: "formal games, oracle interfaces, advantage definitions, model comparison"
  optional: "true"
  namespace: "formal"
---

# Cryptographic Security Game Definition

## Purpose

Defines adversarial experiments, oracles, resources, success events, advantages, correctness events, and multi-user or quantum variants precisely enough for mechanized security proofs.

## Use this skill when

Use this skill when a formal proof concerns IND, OW, PRF/PRP, EUF/SUF, robustness/binding, key agreement, correctness, anonymity, simulation, or another computational security notion.

## Do not invoke automatically

Do not begin game hopping from an informal “standard definition.” Small differences in challenge timing, oracle exclusions, failure behavior, random-oracle access, multi-user structure, or quantum access can change the theorem.

## Optional entry contract

**Inputs**
- construction specification
- claimed security property
- adversary model

**Expected products**
- formal games
- oracle interfaces
- advantage definitions
- model comparison

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Identify the construction algorithms, state, randomness, failure symbols, encodings, and all public or secret parameters. Bind them to exact versions and parameter sets.
2. Define the adversary interface: setup values, phases, state passing, adaptive queries, challenge selection, corruptions/reveals, malformed inputs, decryption/signing restrictions, and termination/resource limits.
3. Define the success event as an executable predicate over the complete transcript and outputs. Avoid relying on prose such as “wins in the usual way.”
4. Define probability and advantage conventions, including factors of two, absolute differences, conditional events, correctness subtraction, statistical distance, and maximum over adversaries.
5. Separate single-user, multi-user, multi-target, multi-instance, chosen-key, weak-key, and related-key games. Provide explicit embeddings or reductions before transferring results among them.
6. For random-oracle models, define domains, prefixes, output lengths, lazy sampling, programming powers, classical or quantum query access, and cross-protocol sharing.
7. For imperfectly correct constructions, define decryption/verification failure, validity, fallback behavior, and how correctness events enter the security theorem.
8. Construct sanity adversaries and toy schemes that should win or lose. Use them to catch reversed bits, impossible games, excluded challenge queries, and vacuous advantages.
9. Export the games as stable interfaces before proof work and record all alternative definitions from the literature that are not equivalent without additional assumptions.

## Output contract

- Machine-readable and prover-level game definitions.
- Oracle/session interface and resource model.
- Advantage and success-event definitions with conventions.
- A comparison table for literature, standard, and implementation-relevant variants.

## Non-negotiable guardrails

- Do not call a proof meaningful if the adversary class is empty or the success event unreachable.
- Do not silently replace computational indistinguishability with equality of distributions.
- Classical ROM and QROM games are distinct.
- Correctness and parsing behavior must match the concrete specification used by the implementation proof.

## Related formal skills

- `game-hopping-and-hybrid-proof`
- `reduction-tightness-and-concrete-security`

## Related cryptanalysis skills in this pack (optional)

- `public-key-security-model-and-claim-formalizer`
- `security-model-and-claim-formalizer`

## Associated primary references

- **EASYCRYPT11** — [EasyCrypt: Automated Reasoning for Security Proofs](https://eprint.iacr.org/2011/101) (2011) — Gilles Barthe et al.. `research-paper`.
- **EASYCRYPT-TUTORIALS** — [EasyCrypt tutorials](https://easycrypt.gitlab.io/easycrypt-web/docs/tutorials/) (2026) — EasyCrypt project. `official-manual`.
- **SSPROVE21** — [SSProve: A Foundational Framework for Modular Cryptographic Proofs in Coq](https://eprint.iacr.org/2021/397) (2021) — Philipp G. Haselwarter et al.. `research-paper`.
- **CRYPTHOL-GAMES** — [Game-Based Cryptography in HOL](https://isa-afp.org/entries/Game_Based_Crypto.html) (2026) — CryptHOL contributors. `formal-development`.
- **MLKEM-EC24** — [Formally verifying Kyber Episode V: Machine-checked IND-CCA security and correctness of ML-KEM in EasyCrypt](https://eprint.iacr.org/2024/843) (2024) — José Bacelar Almeida et al.. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
