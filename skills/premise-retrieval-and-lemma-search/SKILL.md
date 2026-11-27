---
name: premise-retrieval-and-lemma-search
description: "Finds relevant existing definitions and theorems, validates their exact types and assumptions, and constructs small bridging lemmas when library interfaces do not align."
metadata:
  version: "0.1.0"
  display-name: "Premise Retrieval and Lemma Search"
  category: "proof-engineering"
  tags: "premise-selection, retrieval, library-search, proof-engineering"
  requires: "current proof state, available libraries, target semantics"
  produces: "ranked premises, validated theorem signatures, bridge-lemma plan, retrieval trace"
  optional: "true"
  namespace: "formal"
---

# Premise Retrieval and Lemma Search

## Purpose

Finds relevant existing definitions and theorems, validates their exact types and assumptions, and constructs small bridging lemmas when library interfaces do not align.

## Use this skill when

Use this skill when proof progress depends on discovering existing algebra, probability, bit-vector, program-logic, or cryptographic lemmas rather than inventing tactics blindly.

## Do not invoke automatically

Do not select premises by lexical similarity alone. A theorem using a different equality, field, distribution model, side condition, or indexing convention can be actively misleading.

## Optional entry contract

**Inputs**
- current proof state
- available libraries
- target semantics

**Expected products**
- ranked premises
- validated theorem signatures
- bridge-lemma plan
- retrieval trace

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Extract semantic search terms from the goal: mathematical object, operation, relation, direction, side conditions, and likely namespace. Include alternate vocabulary used by the prover community.
2. Use prover-native search, documentation, repository search, retrieval models, and cited formal developments. Search definitions as well as theorem names because unfolding boundaries often explain failed rewrites.
3. Inspect complete signatures, implicit arguments, typeclasses, universes, attributes, and required imports. Instantiate a tiny local example before relying on a candidate.
4. Rank premises by semantic fit and proof robustness, not only by ability to close the current goal. Prefer stable public lemmas over internal implementation details.
5. Identify representation mismatches: lists versus vectors, naturals versus integers, modular equivalence versus equality, bit vectors versus words, distributions versus functions, and code models versus mathematical specs.
6. Create narrowly scoped bridge lemmas when necessary. State their source and target representations and prove them independently before using them repeatedly.
7. For agent retrieval, prevent leakage from the target proof and evaluate generalization across repository versions. Record whether a suggestion came from retrieval, generation, or prior local knowledge.
8. Update a project-specific lemma index with cryptographic concepts, source locations, and examples, but do not duplicate entire upstream manuals in skill context.
9. After proof completion, prune unused imports and premises and preserve only the minimal stable dependency set.

## Output contract

- A ranked, type-checked premise list.
- Exact import and namespace requirements.
- Bridge lemmas and representation-conversion notes.
- A project lemma index entry suitable for future tasks with these skills.

## Non-negotiable guardrails

- Do not cite a theorem without checking that it applies to the exact instantiated types.
- Do not use a theorem whose hidden assumptions are stronger than the target claim.
- Keep retrieved proof bodies out of evaluation contexts intended to measure novel proof generation.
- Prefer explicit conversions over coercion-heavy proofs whose semantics are hard to audit.

## Related formal skills

- `interactive-proof-state-operation`
- `lean-cryptographic-formalization`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **MATHLIB-DOCS** — [Mathlib 4 Documentation](https://leanprover-community.github.io/mathlib4_docs/) (2026) — Lean community. `official-documentation`.
- **LEANDOJO23** — [LeanDojo: Theorem Proving with Retrieval-Augmented Language Models](https://arxiv.org/abs/2306.15626) (2023) — Kaiyu Yang et al.. `research-paper`.
- **LEANDOJO-V2** — [LeanDojo-v2](https://leandojo.org/leandojo.html) (2025) — Ryan Hsiang et al.. `official-project`.
- **PANTOGRAPH24** — [Pantograph: A Machine-to-Machine Interaction Interface for Lean 4](https://arxiv.org/abs/2410.16429) (2024) — Leni Aniva et al.. `research-paper`.
- **ROCQ-REF** — [Rocq documentation](https://rocq-prover.org/docs) (2026) — Rocq project. `official-manual`.
- **ISABELLE-DOCS** — [Isabelle Documentation](https://isabelle.in.tum.de/documentation.html) (2026) — Isabelle project. `official-manual`.

Bundled source metadata is in `references/REFERENCES.md`.
