---
name: interactive-proof-state-operation
description: "Operates an interactive prover through small, state-aware actions, using actual goals and diagnostics rather than hallucinated proof progress."
metadata:
  version: "0.1.0"
  display-name: "Interactive Proof-State Operation"
  category: "proof-engineering"
  tags: "interactive-theorem-proving, tactics, proof-state, agent"
  requires: "theorem goal, live prover session, allowed tactics and imports"
  produces: "checked proof steps, state trace, diagnostics, completed or minimized blocker"
  optional: "true"
  namespace: "formal"
---

# Interactive Proof-State Operation

## Purpose

Operates an interactive prover through small, state-aware actions, using actual goals and diagnostics rather than hallucinated proof progress.

## Use this skill when

Use this skill whenever an LLM or automated controller is constructing a proof incrementally in Lean, Rocq, Isabelle, EasyCrypt, or another interactive environment.

## Do not invoke automatically

Do not generate long proof scripts from memory without testing intermediate states when an interactive interface is available. Whole-proof generation can be attempted as a proposal, but acceptance requires live elaboration and checking.

## Optional entry contract

**Inputs**
- theorem goal
- live prover session
- allowed tactics and imports

**Expected products**
- checked proof steps
- state trace
- diagnostics
- completed or minimized blocker

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Read the complete current state: local context, target, metavariables, side conditions, namespace, imports, universe/implicit arguments, and source location.
2. Normalize the goal semantically before selecting a tactic. Identify whether it is definitional equality, rewriting, induction, algebra, finite computation, relational program reasoning, probability, or an API mismatch.
3. Search existing declarations and inspect exact types before inventing a lemma name. Prefer library lemmas and small adapters over re-proving broad facts.
4. Submit one coherent proof action or a short reversible block. Capture the resulting goals and diagnostics exactly; never infer success from absence of visible output.
5. When a tactic creates unexpected obligations, explain their origin and choose whether to solve, refactor, or undo. Do not bury them under broad automation that changes the proof shape unpredictably.
6. Use local examples or `have` statements to test typeclass inference, coercions, simplification, and rewriting direction before modifying the main proof.
7. Checkpoint frequently. Keep a minimal known-good proof prefix and record the environment so agent retries do not accumulate accidental state.
8. If the goal appears false or underspecified, switch to counterexample and specification audit rather than forcing completion through stronger assumptions.
9. Finish by recompiling the file or theory outside the interactive session and checking that no hidden goals, admissions, or temporary declarations remain.

## Output contract

- A prover-checked sequence of actions or complete proof.
- Exact proof-state and diagnostic trace sufficient for repair or audit.
- A list of premises used and any new helper lemmas introduced.
- A minimized blocker when completion is not justified.

## Non-negotiable guardrails

- Never fabricate prover output, theorem names, goal states, or successful checks.
- Do not add axioms or widen imports merely to satisfy automation without review.
- Preserve the original theorem statement and formalization scope.
- Use actual kernel/checker acceptance as the completion signal.

## Related formal skills

- `premise-retrieval-and-lemma-search`
- `proof-repair-and-maintenance`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **LEAN-TPIL** — [Theorem Proving in Lean 4](https://leanprover.github.io/theorem_proving_in_lean4/) (2024) — Jeremy Avigad et al.. `official-text`.
- **PANTOGRAPH-REPO** — [Pantograph repository](https://github.com/leanprover/Pantograph) (2026) — Pantograph project. `official-repository`.
- **LEANDOJO-V2** — [LeanDojo-v2](https://leandojo.org/leandojo.html) (2025) — Ryan Hsiang et al.. `official-project`.
- **EASYCRYPT-TUTORIALS** — [EasyCrypt tutorials](https://easycrypt.gitlab.io/easycrypt-web/docs/tutorials/) (2026) — EasyCrypt project. `official-manual`.
- **ROCQ-REF** — [Rocq documentation](https://rocq-prover.org/docs) (2026) — Rocq project. `official-manual`.

Bundled source metadata is in `references/REFERENCES.md`.
