---
name: isabelle-crypthol-proof-development
description: "Develops cryptographic definitions and game-based proofs in Isabelle/HOL using CryptHOL, probabilistic programs, oracle constructions, and Sledgehammer-assisted reasoning."
metadata:
  version: "0.1.0"
  display-name: "Isabelle/CryptHOL Proof Development"
  category: "security-proofs"
  tags: "isabelle, crypthol, hol, security-proof"
  requires: "cryptographic construction and claim, Isabelle session, CryptHOL libraries"
  produces: "Isabelle theories, checked CryptHOL proof, dependency report, replay session"
  optional: "true"
  namespace: "formal"
---

# Isabelle/CryptHOL Proof Development

## Purpose

Develops cryptographic definitions and game-based proofs in Isabelle/HOL using CryptHOL, probabilistic programs, oracle constructions, and Sledgehammer-assisted reasoning.

## Use this skill when

Use this skill when an existing CryptHOL development, Isabelle library, or higher-order logic formulation materially reduces the work, or when Sledgehammer-assisted proof reconstruction is valuable.

## Do not invoke automatically

Do not invoke Isabelle only as a second prover for prestige. Cross-prover replication is useful when it independently challenges definitions or trust assumptions, not when it mechanically restates an accepted theorem.

## Optional entry contract

**Inputs**
- cryptographic construction and claim
- Isabelle session
- CryptHOL libraries

**Expected products**
- Isabelle theories
- checked CryptHOL proof
- dependency report
- replay session

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Pin Isabelle and the Archive of Formal Proofs session versions. Build the relevant CryptHOL examples before extending them.
2. Define probabilistic programs, distributions, oracles, adversaries, and security games using CryptHOL conventions, including failure and state.
3. Structure the proof as explicit program transformations, relational arguments, probability bounds, and cryptographic assumptions. Preserve executable game intuition.
4. Use Isabelle locales/type classes to abstract reusable constructions without hiding assumptions. Instantiate parameters and finiteness conditions explicitly.
5. Use Sledgehammer and automated provers for premise discovery, then require reconstruction into Isabelle-checked proof steps under the accepted oracle settings.
6. Inspect all axioms, `sorry` placeholders, oracle invocations, and imported AFP assumptions. Distinguish reconstructed proofs from external prover trust.
7. Validate security definitions against literature games and compare any corresponding EasyCrypt/SSProve formalizations at the semantic level.
8. Use code generation only for validated executable components; preserve the difference between executable tests and HOL theorems.
9. Publish the complete Isabelle session, theory dependencies, AFP versions, build command, and assumption report.

## Output contract

- A compiling Isabelle session with CryptHOL definitions and theorems.
- Game/program transformation and probability-bound documentation.
- Sledgehammer reconstruction and assumption report.
- A clean replay package tied to exact Isabelle/AFP versions.

## Non-negotiable guardrails

- External automated-prover success must be reconstructed or explicitly trusted.
- Do not erase finiteness or losslessness conditions through locale assumptions without reporting them.
- Keep HOL equality, probabilistic equivalence, and computational indistinguishability distinct.
- Cross-system comparisons require definition correspondence, not theorem-name similarity.

## Related formal skills

- `cross-prover-evidence-packaging`
- `cryptographic-security-game-definition`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **ISABELLE-DOCS** — [Isabelle Documentation](https://isabelle.in.tum.de/documentation.html) (2026) — Isabelle project. `official-manual`.
- **CRYPTHOL** — [CryptHOL](https://isa-afp.org/entries/CryptHOL.html) (2026) — Andreas Lochbihler et al.. `formal-development`.
- **CRYPTHOL-GAMES** — [Game-Based Cryptography in HOL](https://isa-afp.org/entries/Game_Based_Crypto.html) (2026) — CryptHOL contributors. `formal-development`.
- **SSPROVE21** — [SSProve: A Foundational Framework for Modular Cryptographic Proofs in Coq](https://eprint.iacr.org/2021/397) (2021) — Philipp G. Haselwarter et al.. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
