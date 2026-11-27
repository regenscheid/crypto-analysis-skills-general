---
name: counterexample-guided-formalization
description: "Uses executable models, property testing, small-model search, solvers, and failed proof states to refine false or underspecified conjectures before investing in a full proof."
metadata:
  version: "0.1.0"
  display-name: "Counterexample-Guided Formalization"
  category: "proof-engineering"
  tags: "counterexample, property-testing, small-model, formalization"
  requires: "candidate theorem, executable definitions, bounded domains or generators"
  produces: "counterexamples or confidence tests, revised conjecture, boundary-case suite, formalization decisions"
  optional: "true"
  namespace: "formal"
---

# Counterexample-Guided Formalization

## Purpose

Uses executable models, property testing, small-model search, solvers, and failed proof states to refine false or underspecified conjectures before investing in a full proof.

## Use this skill when

Use this skill for new lemmas, translated paper claims, suspected standards defects, or any theorem whose preconditions and quantifiers have not already been exercised against examples.

## Do not invoke automatically

Do not interpret failure to find a counterexample as proof. Counterexample search validates the formulation and falsifies bad conjectures; only exhaustive certified search or theorem proving establishes universal claims.

## Optional entry contract

**Inputs**
- candidate theorem
- executable definitions
- bounded domains or generators

**Expected products**
- counterexamples or confidence tests
- revised conjecture
- boundary-case suite
- formalization decisions

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Make the definitions executable where possible and construct generators that cover canonical, malformed, weak, extreme, and correlated inputs rather than only uniform happy paths.
2. Test known examples, official vectors, paper witnesses, and deliberately perturbed witnesses. Confirm that the model accepts and rejects the expected cases.
3. Use small exhaustive domains to compare alternative interpretations and check algebraic identities, loop bounds, indexing, encodings, and failure behavior.
4. Apply property-based testing or solver-based model finding to the negation of the candidate theorem. Preserve seeds, shrunk examples, and complete target versions.
5. When the prover stalls, inspect whether the unsolved goal represents a missing lemma or a genuinely false side condition. Attempt concrete instantiations before adding assumptions.
6. Minimize each counterexample while preserving semantics, then map it back to the source algorithm or implementation. Distinguish model-only counterexamples from real cryptanalytic witnesses.
7. Revise the theorem narrowly: correct definitions, add justified preconditions, split cases, or weaken the conclusion only to the strongest statement supported by the source claim.
8. Turn discovered boundary cases into permanent examples or regression theorems. Where finite domains are small, promote the search to a certified exhaustive result.
9. Escalate surprising counterexamples to the relevant cryptanalysis skill; formalization is not the place to decide their security impact in isolation.

## Output contract

- Minimized counterexamples with replay commands and source mapping.
- A revised theorem statement and explanation of every changed assumption.
- A boundary-case and regression suite.
- A clear statement of whether search was heuristic, bounded exhaustive, certified, or merely illustrative.

## Non-negotiable guardrails

- Do not discard counterexamples because they use malformed or weak inputs unless those inputs are provably outside the intended model.
- Do not add nonzero, full-rank, canonical, or independence assumptions solely to make a theorem true.
- Keep random testing results distinct from exhaustive finite checking.
- A counterexample to a formal model is not automatically an attack on the standardized construction; prove the correspondence.

## Related formal skills

- `finite-search-model-and-encoding-validation`
- `specification-validation-and-vacuity-audit`

## Related cryptanalysis skills in this pack (optional)

- `public-key-reproduction-and-falsification-planner`
- `symmetric-reproduction-and-falsification-planner`

## Associated primary references

- **QUICKCHICK** — [QuickChick](https://github.com/QuickChick/QuickChick) (2026) — QuickChick project. `official-repository`.
- **LEAN-BVDECIDE** — [Lean tactic reference: bv_decide and decision procedures](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/) (2026) — Lean project. `official-manual`.
- **SAGEMATH-TUTORIAL** — [SageMath Tutorial](https://doc.sagemath.org/html/en/tutorial/) (2026) — SageMath project. `official-manual`.
- **CVC5-PROOFS** — [cvc5 Proof Production](https://cvc5.github.io/docs-ci/docs-main/proofs/proofs.html) (2026) — cvc5 project. `official-manual`.
- **PANTOGRAPH24** — [Pantograph: A Machine-to-Machine Interaction Interface for Lean 4](https://arxiv.org/abs/2410.16429) (2024) — Leni Aniva et al.. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
