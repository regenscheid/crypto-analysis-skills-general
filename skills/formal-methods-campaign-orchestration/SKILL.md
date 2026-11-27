---
name: formal-methods-campaign-orchestration
description: "Coordinates multiple human or LLM proof workers across an explicit obligation DAG while preserving isolated workspaces, theorem ownership, reproducibility, and independent verification."
metadata:
  version: "0.1.0"
  display-name: "Formal Methods Campaign Orchestration"
  category: "control"
  tags: "orchestration, multi-agent, proof-campaign, coordination"
  requires: "proof-obligation DAG, toolchain environment, worker capabilities"
  produces: "campaign plan, work assignments, merge and replay log, unresolved obligation register"
  optional: "true"
  namespace: "formal"
---

# Formal Methods Campaign Orchestration

## Purpose

Coordinates multiple human or LLM proof workers across an explicit obligation DAG while preserving isolated workspaces, theorem ownership, reproducibility, and independent verification.

## Use this skill when

Use this skill for developments large enough to benefit from parallel lemma proof, independent encodings, proof repair, or separate specification and audit roles.

## Do not invoke automatically

Do not parallelize before definitions and theorem interfaces are stable. Multiple agents editing shared foundational files without ownership boundaries usually create churn rather than proof progress.

## Optional entry contract

**Inputs**
- proof-obligation DAG
- toolchain environment
- worker capabilities

**Expected products**
- campaign plan
- work assignments
- merge and replay log
- unresolved obligation register

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Freeze the root definitions, namespace plan, toolchain, style rules, forbidden shortcuts, and completion criteria before distributing obligations.
2. Partition the proof DAG into work packages with one owner per theorem or file. Prefer packages whose interfaces are narrow and independently replayable.
3. Give each worker only the required context: theorem statement, imports, relevant definitions, nearby lemmas, references, and allowed tools. Avoid loading the entire skill catalog into each proof session.
4. Use isolated branches, worktrees, or containers. Require workers to report actual prover diagnostics, modified files, new assumptions, and commands rather than prose-only claims of completion.
5. Create specialized roles when useful: specification author, lemma prover, search/certificate worker, proof repairer, adversarial reviewer, and replay verifier. The generator must not approve its own result without an independent check.
6. Merge foundational lemmas before dependent proofs and rerun all affected nodes. Reject changes that weaken theorem statements, introduce unexplained axioms, or alter definitions to make goals trivial.
7. Track failed branches and useful counterexamples. A failed formal approach can expose an incorrect conjecture, missing precondition, or better decomposition and should update the campaign state.
8. Periodically regenerate the dependency graph, axiom report, and open-obligation list. Prevent stale workers from proving against superseded definitions.
9. Close the campaign only after clean replay from the merged state and claim-level audit; local green checks are insufficient.

## Output contract

- A worker/obligation assignment table and dependency-aware schedule.
- Isolated workspace and merge policy.
- Progress records containing prover-verified partial results and exact blockers.
- A final merged replay and unresolved-obligation report.

## Non-negotiable guardrails

- No worker may replace a target theorem with a weaker theorem without explicit review.
- Do not permit hidden local axioms, generated binary artifacts, or network-fetched proofs in worker results.
- Use independent agents or implementations for high-impact encoding and specification checks.
- Preserve exact provenance when a proof is synthesized from fragments produced by several workers.

## Related formal skills

- `proof-obligation-and-lemma-planning`
- `proof-artifact-replay-and-publication`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **PANTOGRAPH24** — [Pantograph: A Machine-to-Machine Interaction Interface for Lean 4](https://arxiv.org/abs/2410.16429) (2024) — Leni Aniva et al.. `research-paper`.
- **LEANDOJO-V2** — [LeanDojo-v2](https://leandojo.org/leandojo.html) (2025) — Ryan Hsiang et al.. `official-project`.
- **SHANNON26** — [ShannonProver: Towards Automating Formal Cryptographic Proofs](https://arxiv.org/abs/2607.02847) (2026) — Yiping Ma et al.. `research-paper`.
- **RUST-LEAN-AI26** — [A Rust-to-Lean Verification Pipeline with AI Provers: An Experience Report](https://arxiv.org/abs/2605.30106) (2026) — Natalia Klaus, Juan Conejero, and Palina Tolmach. `research-paper`.
- **AENEAS-REPO** — [Aeneas repository](https://github.com/AeneasVerif/aeneas) (2026) — Aeneas project. `official-repository`.

Bundled source metadata is in `references/REFERENCES.md`.
