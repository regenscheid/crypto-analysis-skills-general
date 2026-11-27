---
name: lean-agent-integration-pantograph-leandojo
description: "Builds controlled LLM or search-agent interfaces to Lean using structured proof states, premise retrieval, reversible actions, and independent evaluation."
metadata:
  version: "0.1.0"
  display-name: "Lean Agent Integration with Pantograph and LeanDojo"
  category: "lean"
  tags: "lean, agent, pantograph, leandojo, llm"
  requires: "Lean repository, agent policy, evaluation goals"
  produces: "agent interface, retrieval index, proof-search traces, isolated evaluation results"
  optional: "true"
  namespace: "formal"
---

# Lean Agent Integration with Pantograph and LeanDojo

## Purpose

Builds controlled LLM or search-agent interfaces to Lean using structured proof states, premise retrieval, reversible actions, and independent evaluation.

## Use this skill when

Use this skill when developing an AI proof worker, theorem-retrieval service, proof repair agent, or benchmark harness for this skill pack.

## Do not invoke automatically

Do not give the model shell-level control over the verifier when a structured proof-session API suffices. Do not evaluate on the same proof bodies, cached artifacts, or near-duplicate theorems used for retrieval/training.

## Optional entry contract

**Inputs**
- Lean repository
- agent policy
- evaluation goals

**Expected products**
- agent interface
- retrieval index
- proof-search traces
- isolated evaluation results

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Pin the Lean repository, toolchain, mathlib revision, Pantograph/LeanDojo version, and build dependencies. Trace the repository only after confirming it is safe to build in the sandbox.
2. Expose structured observations: theorem statement, local context, goals, relevant source snippets, diagnostics, and retrieved premise signatures. Avoid sending hidden completed proof bodies unless the task is explicit repair.
3. Define a constrained action schema for tactic application, term submission, theorem search, file edits, checkpoint/undo, and session termination. The controller, not the LLM, owns process and filesystem state.
4. Build a premise index with dependency-aware data splits and version metadata. Test retrieval precision on crypto concepts, representation conversions, and project-local lemmas.
5. Support both whole-proof proposals and incremental search, but route every proposal through actual elaboration and kernel checking. Capture exact failure states for repair.
6. Prevent contamination: remove target proof bodies, exclude generated object files, detect imported final theorems, and separate training/retrieval repositories from evaluation targets.
7. Add budgets for steps, wall time, tokens, prover processes, and generated file size. Preserve traces and random seeds for comparative evaluation.
8. Evaluate more than success rate: theorem-statement preservation, unexpected axioms, proof minimality, generalization to new premises, repair robustness, and false-claim rejection.
9. Independently replay accepted proofs in a clean environment and publish only the proof artifact—not the model’s narrative claim of success.

## Output contract

- A sandboxed Lean agent API and action/observation schema.
- A versioned retrieval index and contamination policy.
- Complete proof-state traces, budgets, and accepted proof files.
- An evaluation report covering correctness, trust, generalization, and failure modes.

## Non-negotiable guardrails

- The LLM must not be its own verifier or fabricate diagnostics.
- Do not expose secrets, proprietary repositories, or untrusted build scripts outside the approved sandbox.
- Benchmark splits must prevent theorem and premise leakage.
- Any agent-added axiom, `sorry`, unsafe declaration, or theorem weakening is an automatic failure unless the task explicitly studies such behavior.

## Related formal skills

- `interactive-proof-state-operation`
- `formal-methods-campaign-orchestration`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **PANTOGRAPH24** — [Pantograph: A Machine-to-Machine Interaction Interface for Lean 4](https://arxiv.org/abs/2410.16429) (2024) — Leni Aniva et al.. `research-paper`.
- **PANTOGRAPH-REPO** — [Pantograph repository](https://github.com/leanprover/Pantograph) (2026) — Pantograph project. `official-repository`.
- **LEANDOJO23** — [LeanDojo: Theorem Proving with Retrieval-Augmented Language Models](https://arxiv.org/abs/2306.15626) (2023) — Kaiyu Yang et al.. `research-paper`.
- **LEANDOJO-V2** — [LeanDojo-v2](https://leandojo.org/leandojo.html) (2025) — Ryan Hsiang et al.. `official-project`.
- **LEAN-FAQ** — [Lean FAQ](https://lean-lang.org/faq/) (2026) — Lean project. `official-documentation`.
- **RUST-LEAN-AI26** — [A Rust-to-Lean Verification Pipeline with AI Provers: An Experience Report](https://arxiv.org/abs/2605.30106) (2026) — Natalia Klaus, Juan Conejero, and Palina Tolmach. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
