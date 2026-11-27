---
name: formalization-value-and-scope-triage
description: "Assesses whether a proposed formal effort is likely to reduce the important uncertainty, and selects a defensible scope that can be completed and reused."
metadata:
  version: "0.1.0"
  display-name: "Formalization Value and Scope Triage"
  category: "control"
  tags: "scope, triage, research-planning, assurance"
  requires: "candidate claim, target artifacts, existing evidence"
  produces: "value assessment, scope options, risk register, stop conditions"
  optional: "true"
  namespace: "formal"
---

# Formalization Value and Scope Triage

## Purpose

Assesses whether a proposed formal effort is likely to reduce the important uncertainty, and selects a defensible scope that can be completed and reused.

## Use this skill when

Use this skill after a potentially formalizable claim has been identified but before committing to a toolchain or translating a large specification. It is especially useful for new cryptanalytic claims, standards defects, difficult probability arguments, and code-verification projects.

## Do not invoke automatically

Do not use formalization as a substitute for first understanding the target. If the algorithm, alleged attack, or security theorem cannot yet be stated precisely in ordinary mathematics or executable pseudocode, return to domain analysis first.

## Optional entry contract

**Inputs**
- candidate claim
- target artifacts
- existing evidence

**Expected products**
- value assessment
- scope options
- risk register
- stop conditions

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. List the decision the formal artifact is intended to support: validate a suspected attack, eliminate a class of mistakes, certify a finite search, establish a reusable lemma, audit a proof, or connect code to a standard.
2. Create three scope candidates: minimum decisive obligation, useful intermediate development, and ambitious end-to-end result. State exactly what each would and would not establish.
3. Assess semantic availability: mathematical structures, probability model, machine-word semantics, floating-point model, protocol adversary, source-language subset, hardware intrinsics, and external primitives.
4. Assess evidence leverage. Prefer obligations whose proof would invalidate many dependent claims, resolve a disputed assumption, certify a high-value negative result, or become shared infrastructure for several skill families in this pack.
5. Assess specification risk separately from proof difficulty. A hard proof of a trustworthy specification may be worthwhile; an easy proof of a code-derived or underspecified model may be nearly valueless.
6. Identify expected counterexamples and boundary cases before proving. A formalization that cannot express malformed inputs, failure behavior, weak keys, or correlated randomness may answer the wrong question.
7. Choose milestones that produce useful artifacts even if the full proof fails: executable specification plus vectors, isolated lemma library, verified witness checker, encoding correspondence theorem, or replayable proof skeleton.
8. Define abandonment and escalation criteria. Examples include unsupported unsafe Rust, intractable measure theory, certificate sizes beyond the checker, or a discovered model/specification mismatch that requires domain review.

## Output contract

- A scope comparison with minimum, intermediate, and end-to-end options.
- A value/risk matrix covering assurance gain, reuse, semantics, proof burden, and specification risk.
- Milestones, stop conditions, and fallback evidence routes.
- A recommendation that can explicitly be “do not formalize at this stage.”

## Non-negotiable guardrails

- Do not estimate value solely from theorem prestige or line count.
- Do not choose a backend before identifying the claim shape and required semantics.
- Include model-maintenance cost when the target implementation or standard is still changing.
- Preserve an explicit list of phenomena excluded by the proposed formal scope.

## Related formal skills

- `formal-methods-router`
- `formal-claim-and-model-authoring`
- `proof-obligation-and-lemma-planning`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **LEAN-TPIL** — [Theorem Proving in Lean 4](https://leanprover.github.io/theorem_proving_in_lean4/) (2024) — Jeremy Avigad et al.. `official-text`.
- **EASYCRYPT11** — [EasyCrypt: Automated Reasoning for Security Proofs](https://eprint.iacr.org/2011/101) (2011) — Gilles Barthe et al.. `research-paper`.
- **AENEAS22** — [Aeneas: Rust Verification by Functional Translation](https://arxiv.org/abs/2206.07185) (2022) — Son Ho et al.. `research-paper`.
- **RUST-LEAN-AI26** — [A Rust-to-Lean Verification Pipeline with AI Provers: An Experience Report](https://arxiv.org/abs/2605.30106) (2026) — Natalia Klaus, Juan Conejero, and Palina Tolmach. `research-paper`.
- **SHANNON26** — [ShannonProver: Towards Automating Formal Cryptographic Proofs](https://arxiv.org/abs/2607.02847) (2026) — Yiping Ma et al.. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
