---
name: proof-repair-and-maintenance
description: "Repairs proofs after specification, implementation, extraction, dependency, or prover changes while detecting theorem weakening and preserving the intended semantic contract."
metadata:
  version: "0.1.0"
  display-name: "Proof Repair and Maintenance"
  category: "proof-engineering"
  tags: "proof-repair, maintenance, regression, migration"
  requires: "failing proof, previous passing artifact, change set and diagnostics"
  produces: "minimal repair, semantic impact assessment, regression tests, updated proof manifest"
  optional: "true"
  namespace: "formal"
---

# Proof Repair and Maintenance

## Purpose

Repairs proofs after specification, implementation, extraction, dependency, or prover changes while detecting theorem weakening and preserving the intended semantic contract.

## Use this skill when

Use this skill when a previously checked proof fails, generated models change, a library updates, or the implementation/specification evolves.

## Do not invoke automatically

Do not treat every failure as syntax drift. A broken proof may correctly reveal changed behavior, a new precondition, a strengthened theorem, or an invalidated model assumption.

## Optional entry contract

**Inputs**
- failing proof
- previous passing artifact
- change set and diagnostics

**Expected products**
- minimal repair
- semantic impact assessment
- regression tests
- updated proof manifest

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Reproduce the failure in the pinned old and new environments. Separate environmental, parser/elaborator, API, automation, definition, and semantic failures.
2. Diff theorem statements, definitions, generated models, imports, compiler/extractor versions, and axiom dependencies before editing the proof script.
3. Find the earliest failing obligation and inspect the changed proof state. Avoid broad global rewrites until the semantic cause is understood.
4. Classify the change as proof-only, representation-only, specification change, implementation behavior change, or trust-boundary change. Escalate the latter three for domain review.
5. Attempt the smallest local repair using stable library interfaces. Add a bridge lemma when an upstream representation changed rather than scattering casts or rewrites throughout the development.
6. Run vacuity and counterexample checks if a new precondition or changed definition makes the theorem easier. Compare quantified domains and executable examples before accepting the repair.
7. Replay all dependent proofs and certificates. Regenerate extracted models or constraints from source rather than patching generated files manually.
8. Update the proof manifest with changed dependencies, assumptions, runtime, and source hashes. Preserve the prior artifact and failure chronology.
9. Add a regression theorem or example that would fail if the semantic issue recurs.

## Output contract

- A minimal checked repair or a justified semantic-change finding.
- A before/after theorem and trust-boundary comparison.
- Regression tests and affected-dependency list.
- Updated replay manifest and chronology.

## Non-negotiable guardrails

- Never repair by replacing a theorem with a weaker relation or impossible precondition without explicit approval.
- Do not edit extracted/generated models unless the generation process itself is the subject of the fix.
- Preserve reproducibility of the last known-good environment.
- If the implementation changed, revalidate standard vectors and independent specifications before proving equivalence again.

## Related formal skills

- `specification-validation-and-vacuity-audit`
- `formal-methods-campaign-orchestration`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **LEAN-REF** — [Lean Language Reference](https://lean-lang.org/doc/reference/latest/) (2026) — Lean project. `official-manual`.
- **AENEAS-REPO** — [Aeneas repository](https://github.com/AeneasVerif/aeneas) (2026) — Aeneas project. `official-repository`.
- **HAX-MANUAL** — [hax manual](https://hax.cryspen.com/) (2026) — Cryspen. `official-manual`.
- **RUST-LEAN-AI26** — [A Rust-to-Lean Verification Pipeline with AI Provers: An Experience Report](https://arxiv.org/abs/2605.30106) (2026) — Natalia Klaus, Juan Conejero, and Palina Tolmach. `research-paper`.
- **VERUS-GUIDE** — [Verus Tutorial and Reference](https://verus-lang.github.io/verus/guide/) (2026) — Verus project. `official-manual`.

Bundled source metadata is in `references/REFERENCES.md`.
