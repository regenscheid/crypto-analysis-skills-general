---
name: shannonprover-agentic-easycrypt
description: "Applies a managed-agent architecture to EasyCrypt proof generation and repair, separating expert security modeling and lemma decomposition from constrained tactic execution and independent replay."
metadata:
  version: "0.1.0"
  display-name: "ShannonProver-Style Agentic EasyCrypt"
  category: "security-proofs"
  tags: "easycrypt, shannonprover, agent, llm"
  requires: "EasyCrypt theorem and proof skeleton, managed session service, agent policy"
  produces: "agent proof traces, checked proof bodies, evaluation results, remaining expert obligations"
  optional: "true"
  namespace: "formal"
---

# ShannonProver-Style Agentic EasyCrypt

## Purpose

Applies a managed-agent architecture to EasyCrypt proof generation and repair, separating expert security modeling and lemma decomposition from constrained tactic execution and independent replay.

## Use this skill when

Use this skill when scaling EasyCrypt tactic proof development with LLM agents after the games, theorem statements, and lemma decomposition have been reviewed by a cryptographer.

## Do not invoke automatically

Do not delegate security definitions, adversary models, or the entire reduction structure to an unconstrained agent and then infer correctness from a passing local proof. The strongest current architecture keeps those high-level choices explicit and reviewable.

## Optional entry contract

**Inputs**
- EasyCrypt theorem and proof skeleton
- managed session service
- agent policy

**Expected products**
- agent proof traces
- checked proof bodies
- evaluation results
- remaining expert obligations

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Freeze the target EasyCrypt source, remove or blank the target proof body for evaluation, and preserve the exact theorem statement and imports.
2. Provide the agent a structured view of the current proof state, relevant definitions, allowed lemmas, and nearby examples. Avoid exposing hidden completed proofs.
3. Require the agent to submit one proof intent or tactic action through a session manager that owns EasyCrypt processes, checkpoints, file writes, timeouts, and undo.
4. Use specialized agents for premise retrieval, local proof generation, repair, and critique, but keep a single source of truth for the prover state.
5. Log every observation, action, diagnostic, external prover invocation, and source edit. Disallow unreviewed axioms, `admit`, theorem-statement changes, and imports of solved targets.
6. Evaluate in isolation with resource budgets and contamination checks. Re-run accepted proofs offline using the pinned EasyCrypt environment.
7. Measure success by checked obligations, theorem preservation, hidden-assumption rate, and robustness to perturbed statements—not persuasive explanations.
8. Escalate failures that indicate missing cryptographic lemmas, false games, or invalid decompositions to human/domain review rather than endless tactic search.
9. Promote successful patterns into small reusable EasyCrypt proof skills or libraries only after adversarial replay on distinct examples.

## Output contract

- Managed proof-session API and constrained action schema.
- Complete auditable agent traces and checked EasyCrypt proof bodies.
- Isolation, contamination, and theorem-preservation evaluation.
- A boundary report identifying what still required cryptographer judgment.

## Non-negotiable guardrails

- The agent cannot approve its own proof.
- Do not reward scripts that close a weakened or imported theorem.
- Keep natural-language proof quality separate from checker acceptance.
- Preserve failed attempts when they reveal specification or decomposition issues.

## Related formal skills

- `formal-methods-campaign-orchestration`
- `interactive-proof-state-operation`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **SHANNON26** — [ShannonProver: Towards Automating Formal Cryptographic Proofs](https://arxiv.org/abs/2607.02847) (2026) — Yiping Ma et al.. `research-paper`.
- **EASYCRYPT-REPO** — [EasyCrypt repository](https://github.com/EasyCrypt/easycrypt) (2026) — EasyCrypt project. `official-repository`.
- **EASYCRYPT-TUTORIALS** — [EasyCrypt tutorials](https://easycrypt.gitlab.io/easycrypt-web/docs/tutorials/) (2026) — EasyCrypt project. `official-manual`.
- **RUST-LEAN-AI26** — [A Rust-to-Lean Verification Pipeline with AI Provers: An Experience Report](https://arxiv.org/abs/2605.30106) (2026) — Natalia Klaus, Juan Conejero, and Palina Tolmach. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
