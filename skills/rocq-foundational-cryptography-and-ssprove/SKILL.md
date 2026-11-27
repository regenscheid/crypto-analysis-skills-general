---
name: rocq-foundational-cryptography-and-ssprove
description: "Uses Rocq libraries such as SSProve and the Foundational Cryptography Framework for foundational, modular, machine-checked computational cryptography."
metadata:
  version: "0.1.0"
  display-name: "Rocq Foundational Cryptography, FCF, and SSProve"
  category: "security-proofs"
  tags: "rocq, ssprove, fcf, cryptography"
  requires: "formal games or modular construction, Rocq environment, selected framework"
  produces: "Rocq development, modular security theorem, axiom report, extracted or executable artifacts when applicable"
  optional: "true"
  namespace: "formal"
---

# Rocq Foundational Cryptography, FCF, and SSProve

## Purpose

Uses Rocq libraries such as SSProve and the Foundational Cryptography Framework for foundational, modular, machine-checked computational cryptography.

## Use this skill when

Use this skill when existing Rocq cryptography libraries, state-separating proofs, constructive probability, or foundational proof-term goals make Rocq preferable to EasyCrypt or Lean.

## Do not invoke automatically

Do not combine SSProve and FCF abstractions indiscriminately. Choose a framework based on the desired probability semantics, modularity, existing libraries, and theorem interfaces.

## Optional entry contract

**Inputs**
- formal games or modular construction
- Rocq environment
- selected framework

**Expected products**
- Rocq development
- modular security theorem
- axiom report
- extracted or executable artifacts when applicable

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Pin Rocq, MathComp or other dependencies, SSProve/FCF revisions, and build tooling. Confirm compatibility before importing large developments.
2. Formalize construction packages, adversary interfaces, probabilistic computations, state, and security notions using the chosen framework’s native abstractions.
3. For SSProve, exploit package composition and state-separating laws while proving lower-level relational obligations in the provided logic.
4. For FCF, represent probabilistic computations and computational security definitions explicitly, tracking well-formedness, admissibility, and concrete/asymptotic bounds as supported.
5. Construct modular composition theorems with explicit interfaces and disjointness/state assumptions. Validate them on small encryption, KEM-DEM, PRF, or sigma-protocol examples before specialization.
6. Use Rocq automation, reflection, and external solver reconstruction cautiously; inspect axioms and admitted results throughout the dependency closure.
7. Compare formal definitions to paper games and implementation specifications. Record differences in distributions, failure, oracle state, and adversary resources.
8. Exploit extraction only when the extracted program’s semantics and runtime environment are part of the intended artifact; extraction does not prove compiler or platform behavior automatically.
9. Publish theorem names, dependency/axiom reports, framework-specific assumptions, and clean build instructions.

## Output contract

- A pinned Rocq development using SSProve, FCF, or a justified combination.
- Package/module and game definitions with checked composition theorems.
- A framework semantics and assumption report.
- Clean replay and optional extraction artifacts.

## Non-negotiable guardrails

- Do not treat framework soundness as validation of a handwritten security definition.
- Check all admitted axioms and classical-choice assumptions relevant to probability.
- Do not transfer a theorem between Rocq frameworks without a proved semantic bridge.
- Keep asymptotic and concrete security statements distinct.

## Related formal skills

- `cryptographic-security-game-definition`
- `probabilistic-program-coupling-and-relational-reasoning`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **ROCQ-HOME** — [The Rocq Prover](https://rocq-prover.org/) (2026) — Rocq project. `official-project`.
- **ROCQ-REF** — [Rocq documentation](https://rocq-prover.org/docs) (2026) — Rocq project. `official-manual`.
- **SSPROVE21** — [SSProve: A Foundational Framework for Modular Cryptographic Proofs in Coq](https://eprint.iacr.org/2021/397) (2021) — Philipp G. Haselwarter et al.. `research-paper`.
- **SSPROVE-REPO** — [SSProve repository](https://github.com/SSProve/ssprove) (2026) — SSProve project. `official-repository`.
- **FCF-REPO** — [Foundational Cryptography Framework](https://github.com/adampetcher/fcf) (2026) — Adam Petcher et al.. `official-repository`.
- **QUICKCHICK** — [QuickChick](https://github.com/QuickChick/QuickChick) (2026) — QuickChick project. `official-repository`.

Bundled source metadata is in `references/REFERENCES.md`.
