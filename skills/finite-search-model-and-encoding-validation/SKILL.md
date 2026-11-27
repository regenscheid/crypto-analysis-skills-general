---
name: finite-search-model-and-encoding-validation
description: "Builds a semantics-first finite cryptanalytic search model and proves or tests the correspondence between target objects and SAT, SMT, PB, MILP, CP, or custom-search encodings before interpreting results."
metadata:
  version: "0.1.0"
  display-name: "Finite Search Model and Encoding Validation"
  category: "certified-computation"
  tags: "encoding, finite-search, soundness, completeness, cryptanalysis"
  requires: "cryptanalytic search question, exact target semantics, candidate backend"
  produces: "validated encoding, soundness/completeness obligations, small-instance tests, witness checker"
  optional: "true"
  namespace: "formal"
---

# Finite Search Model and Encoding Validation

## Purpose

Builds a semantics-first finite cryptanalytic search model and proves or tests the correspondence between target objects and SAT, SMT, PB, MILP, CP, or custom-search encodings before interpreting results.

## Use this skill when

Use this skill before relying on an automated finite search for trails, impossible transitions, integral properties, bounds, codewords, algebraic solutions, reduced-round collisions, or other bounded cryptanalytic objects.

## Do not invoke automatically

Do not invoke it for exploratory heuristic search whose results will be validated only as individual witnesses and where no negative or optimality claim will be made. In that case, a smaller witness checker may suffice.

## Optional entry contract

**Inputs**
- cryptanalytic search question
- exact target semantics
- candidate backend

**Expected products**
- validated encoding
- soundness/completeness obligations
- small-instance tests
- witness checker

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Define the searched object independently of solver syntax: variables, domains, rounds/parameters, constants, key treatment, boundary conditions, equivalence classes, weight/objective, and success witness.
2. State separately the positive and negative claims the encoding might support: existence, enumeration, counting, lower bound, impossibility, or optimality.
3. Construct forward and reverse interpretation functions between cryptographic objects and assignments/solutions. Identify where only one direction is needed and where both are required.
4. Prove or exhaustively test local component encodings: S-box transitions, modular additions/carries, linear layers, field equations, rank/weight constraints, decoding relations, and canonicality.
5. Compare the full encoding with direct enumeration on reduced parameters/rounds. Measure both false positives and false negatives, not merely objective agreement.
6. Validate accepted assignments through an independent executable model. Generate real objects and ensure the encoding accepts them; mutate them and ensure invalid cases are rejected.
7. Audit symmetry breaking, relaxations, genericity assumptions, truncated models, fixed keys, and omitted states. Prove that each preserves the claimed domain or narrow the theorem.
8. For negative/optimal results, create explicit obligations for search-space completeness, objective correspondence, and certificate checking.
9. Publish encoding generator, checker, tiny instances, tests, mapping theorem/status, and exact scope.

## Output contract

- A mathematical encoding specification and machine generator.
- Soundness/completeness correspondence proof or bounded validation record.
- Independent witness checker and small-instance exhaustive comparison.
- An obligation list for the selected certificate backend.

## Non-negotiable guardrails

- Solver correctness cannot repair a wrong or incomplete encoding.
- Symmetry breaking and relaxations must have a stated preservation direction.
- A found assignment establishes only the decoded witness, not prevalence or optimality.
- A timeout or empty heuristic search is not evidence of nonexistence.

## Related formal skills

- `sat-lrat-certification`
- `pseudo-boolean-veripb-certification`
- `exhaustive-search-completeness-proof`

## Related cryptanalysis skills in this pack (optional)

- `automated-algebra-and-search-model-builder`
- `automated-search-model-builder`

## Associated primary references

- **LRAT17** — [Efficient Certified RAT Verification](https://arxiv.org/abs/1612.02353) (2017) — Luís Cruz-Filipe et al.. `research-paper`.
- **PBLEAN26** — [PBLean: Importing Pseudo-Boolean Proofs into Lean](https://arxiv.org/abs/2602.08692) (2026) — PBLean authors. `research-paper`.
- **CVC5-PROOFS** — [cvc5 Proof Production](https://cvc5.github.io/docs-ci/docs-main/proofs/proofs.html) (2026) — cvc5 project. `official-manual`.
- **LEAN-BVDECIDE** — [Lean tactic reference: bv_decide and decision procedures](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/) (2026) — Lean project. `official-manual`.

Bundled source metadata is in `references/REFERENCES.md`.
