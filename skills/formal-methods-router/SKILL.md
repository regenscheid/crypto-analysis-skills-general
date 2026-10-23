---
name: formal-methods-router
description: "Chooses whether formalization is worthwhile and, when it is, routes the task to an appropriate proof, certificate, implementation, protocol, or witness workflow without imposing formal methods on ordinary cryptanalysis."
metadata:
  version: "0.1.0"
  display-name: "Formal Methods Router"
  category: "control"
  tags: "routing, formalization, cryptanalysis, optional"
  requires: "target claim or research question, available artifacts and time budget"
  produces: "route decision, candidate backends, formalization boundary, decline rationale when ordinary analysis is preferable"
  optional: "true"
  namespace: "formal"
---

# Formal Methods Router

Use [the environment guide](../investigate/reference/environment.md) for the
current session's instruction access, tools, and storage. Select only available
backends; when a checker cannot run, return a plan or unreplayed source with the
proof obligation still open. Native skill routing is optional: read available
files or supplied text and identify missing specialist procedures.


## Purpose

Chooses whether formalization is worthwhile and, when it is, routes the task to an appropriate proof, certificate, implementation, protocol, or witness workflow without imposing formal methods on ordinary cryptanalysis.

## Use this skill when

Use this skill when a cryptanalysis agent encounters a claim that might benefit from machine-checked proof, certified computation, implementation refinement, or protocol verification, or when the user explicitly asks for those methods. It is the normal entry point into this pack, but it is not a prerequisite for ordinary experiments, literature review, exploratory algebra, heuristic search, or attack implementation.

## Do not invoke automatically

Do not invoke a prover merely to make a result appear stronger. Prefer ordinary derivation, reproducible code, or empirical work when the main uncertainty is exploratory, the formal model would omit the decisive phenomenon, or the expected assurance gain is smaller than the modeling cost.

## Optional entry contract

**Inputs**
- target claim or research question
- available artifacts and time budget

**Expected products**
- route decision
- candidate backends
- formalization boundary
- decline rationale when ordinary analysis is preferable

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Write the exact candidate claim in one sentence and classify it as existence, counterexample, equivalence, correctness, lower bound, optimality, security reduction, protocol property, leakage property, or probabilistic bound. Preserve the target version, parameters, adversary powers, and non-goals.
2. Identify the current evidence and the actual source of uncertainty. Distinguish uncertainty about mathematics, implementation behavior, a finite search, a protocol model, numerical error, empirical frequency, or a heuristic cost estimate.
3. Estimate formalization value. Favor formal methods for delicate invariants, universal or negative claims, security reductions, standards-to-code correspondence, machine arithmetic, exact finite bounds, and claims likely to be reused or challenged.
4. Estimate modeling risk and cost. Record missing semantics, unsupported language features, idealizations, probabilistic or quantum features, external libraries, and whether a formal model could accidentally remove the suspected attack surface.
5. Choose the lightest adequate evidence route: direct witness checker; exact executable specification; SAT/PB/SMT certificate; Lean/Rocq/Isabelle theorem; EasyCrypt/SSProve/CryptHOL security proof; Aeneas/hax/Verus/Creusot refinement; protocol prover; or rigorous numerical proof.
6. Define a stopping point before work begins. Examples include a checked attack witness, a theorem for one algebraic lemma, a certified lower bound for a bounded model, or a full implementation-refinement theorem. Do not silently expand to “verify the whole scheme.”
7. Name the trusted computing base and independent replay requirement appropriate to the route. For search tools, require a witness or certificate when possible; for proof assistants, require clean kernel checking and an assumption report.
8. Return either a narrow formalization charter and selected skills, or a documented decision to continue with non-formal cryptanalysis. The latter is a successful routing outcome, not a failure.

## Output contract

- A claim classification and explicit formalization boundary.
- A ranked route table with expected assurance, modeling risk, prerequisites, and estimated proof-engineering burden.
- The selected skill slugs and backend candidates, with alternatives if the preferred tool lacks required semantics.
- A recorded decision not to formalize when ordinary cryptanalytic work is more informative.

## Non-negotiable guardrails

- Formal methods are opt-in. Never make completion of this router a condition for running unrelated cryptanalysis skills.
- Do not convert “important claim” into “formalize everything”; select the smallest high-value obligation.
- Do not call a bounded or idealized theorem a statement about the full construction without a proved correspondence.
- Keep empirical, heuristic, certified, and kernel-checked evidence labels distinct.

## Related formal skills

- `formalization-value-and-scope-triage`
- `formal-claim-and-model-authoring`
- `evidence-trust-and-tcb-audit`

## Optional CryptoSkills cross-references

- `automated-algebra-and-search-model-builder`
- `security-proof-rom-qrom-and-tightness-auditor`
- `symmetric-reproduction-and-falsification-planner`
- `security-proof-and-bound-auditor`

## Associated primary references

- **LEAN-FAQ** — [Lean FAQ](https://lean-lang.org/faq/) (2026) — Lean project. `official-documentation`.
- **EASYCRYPT-HOME** — [EasyCrypt](https://www.easycrypt.info/) (2026) — EasyCrypt project. `official-project`.
- **AENEAS-REPO** — [Aeneas repository](https://github.com/AeneasVerif/aeneas) (2026) — Aeneas project. `official-repository`.
- **TAMARIN-HOME** — [Tamarin Prover](https://tamarin-prover.com/) (2026) — Tamarin project. `official-project`.
- **LRAT17** — [Efficient Certified RAT Verification](https://arxiv.org/abs/1612.02353) (2017) — Luís Cruz-Filipe et al.. `research-paper`.
- **VERIPB-HOME** — [VeriPB](https://veripb.org/) (2026) — VeriPB project. `official-project`.

Bundled source metadata is in `references/REFERENCES.md`.
