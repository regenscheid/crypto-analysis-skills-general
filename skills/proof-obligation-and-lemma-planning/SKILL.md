---
name: proof-obligation-and-lemma-planning
description: "Decomposes a formal target into a dependency DAG of definitions, correspondence lemmas, invariants, game hops, arithmetic bounds, certificates, and final theorems."
metadata:
  version: "0.1.0"
  display-name: "Proof Obligation and Lemma Planning"
  category: "control"
  tags: "proof-planning, lemma-dag, decomposition, dependencies"
  requires: "formalization charter, candidate backend, existing libraries"
  produces: "proof-obligation DAG, lemma statements, dependency and risk annotations, work packages"
  optional: "true"
  namespace: "formal"
---

# Proof Obligation and Lemma Planning

## Purpose

Decomposes a formal target into a dependency DAG of definitions, correspondence lemmas, invariants, game hops, arithmetic bounds, certificates, and final theorems.

## Use this skill when

Use this skill once the formal claim is stable enough to plan. It supports both human and LLM proof development and is particularly valuable for cryptographic proofs whose apparent single theorem hides several semantic layers.

## Do not invoke automatically

Do not decompose solely according to source-code function boundaries or paper section headings. Decompose around semantic gaps that require distinct evidence.

## Optional entry contract

**Inputs**
- formalization charter
- candidate backend
- existing libraries

**Expected products**
- proof-obligation DAG
- lemma statements
- dependency and risk annotations
- work packages

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Draw the semantic chain from source artifact to conclusion. Typical layers are normative algorithm, executable mathematical specification, code-shaped specification, extracted implementation model, machine semantics, and security theorem.
2. Create one proof obligation for every nontrivial arrow in that chain. Never let a final `simp`-style theorem conceal an unproved extraction, encoding, or model correspondence.
3. Separate definition-validation obligations from mathematical proof obligations. Test vectors, round trips, and examples validate transcription; they do not replace universal theorems.
4. For security proofs, represent each game transition, simulator, bad event, distributional equality, statistical-distance bound, and reduction loss as a node. Record which nodes require adversary-independent lemmas.
5. For solver-backed work, include encoding soundness, encoding completeness, objective correspondence, certificate checking, and original-domain theorem lifting as separate nodes.
6. For implementation work, include safety/panic freedom, preconditions, memory layout, arithmetic semantics, intrinsics, serialization, loops, and compiler/extraction assumptions.
7. Annotate each node with backend, expected automation, likely library premises, counterexample strategy, trusted components, reuse potential, and failure impact.
8. Order work to fail early on semantic mistakes: prove small correspondence and boundary lemmas before launching long automation or agent campaigns.
9. Assign stable theorem IDs and keep the DAG synchronized with actual files. A renamed or weakened theorem must update dependent claims and the proof manifest.

## Output contract

- A machine-readable and human-readable proof-obligation DAG.
- Candidate statements for helper lemmas and final theorems.
- Backend and artifact type for each node.
- Critical-path, reuse, and high-risk annotations suitable for parallel proof campaigns.

## Non-negotiable guardrails

- Prevent circular dependencies and “proof by imported final theorem.”
- Do not mark an obligation complete because a stronger-looking but differently scoped theorem exists.
- Keep arithmetic range proofs separate from modular identity proofs when the implementation needs both.
- Every external solver result must have a node for checking and a node for encoding correspondence.

## Related formal skills

- `formal-methods-campaign-orchestration`
- `proof-repair-and-maintenance`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **LEAN-TPIL** — [Theorem Proving in Lean 4](https://leanprover.github.io/theorem_proving_in_lean4/) (2024) — Jeremy Avigad et al.. `official-text`.
- **SHANNON26** — [ShannonProver: Towards Automating Formal Cryptographic Proofs](https://arxiv.org/abs/2607.02847) (2026) — Yiping Ma et al.. `research-paper`.
- **SSPROVE21** — [SSProve: A Foundational Framework for Modular Cryptographic Proofs in Coq](https://eprint.iacr.org/2021/397) (2021) — Philipp G. Haselwarter et al.. `research-paper`.
- **LAST-MILE20** — [The Last Mile: High-Assurance and High-Speed Cryptographic Implementations](https://arxiv.org/abs/1904.04606) (2020) — José Bacelar Almeida et al.. `research-paper`.
- **AENEAS22** — [Aeneas: Rust Verification by Functional Translation](https://arxiv.org/abs/2206.07185) (2022) — Son Ho et al.. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
