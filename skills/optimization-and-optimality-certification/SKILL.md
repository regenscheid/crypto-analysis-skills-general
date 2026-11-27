---
name: optimization-and-optimality-certification
description: "Converts a best-found cryptanalytic object into a defensible optimum or bound by certifying feasibility, objective interpretation, and exclusion of every better solution."
metadata:
  version: "0.1.0"
  display-name: "Optimization and Optimality Certification"
  category: "certified-computation"
  tags: "optimization, optimality, lower-bound, upper-bound, certificate"
  requires: "optimization problem, candidate optimum/witness, exact objective and domain"
  produces: "certified optimum or one-sided bound, witness, exclusion proof, scope statement"
  optional: "true"
  namespace: "formal"
---

# Optimization and Optimality Certification

## Purpose

Converts a best-found cryptanalytic object into a defensible optimum or bound by certifying feasibility, objective interpretation, and exclusion of every better solution.

## Use this skill when

Use this skill when the claim is “best,” “minimum,” “maximum,” “no object below/above B,” or an exact security-margin bound rather than merely a strong candidate found by search.

## Do not invoke automatically

Do not formalize optimality when the practical research question only needs a usable attack witness or a heuristic estimate. Do not certify a surrogate objective unless its relation to the cryptanalytic quantity is established.

## Optional entry contract

**Inputs**
- optimization problem
- candidate optimum/witness
- exact objective and domain

**Expected products**
- certified optimum or one-sided bound
- witness
- exclusion proof
- scope statement

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Define feasible objects and the objective in original cryptographic terms, including exact weights, signs, probabilities, costs, equivalence classes, and boundary conditions.
2. Check the candidate witness independently and compute its exact objective, yielding one side of the bound.
3. Choose a certifiable exclusion route: PB/VeriPB, SAT for every better threshold, branch-and-bound certificate, dynamic-programming proof, dual certificate, or proof-assistant theorem.
4. Prove encoding feasibility and objective correspondence. If optimizing active S-boxes, for example, state whether that is an exact probability bound or only a proxy.
5. Handle rational/logarithmic weights without unsafe floating rounding; use scaled integers or exact rationals and prove rounding direction.
6. Check every certificate and all decomposed subproblems; prove coverage of ranges/partitions and absence of gaps between thresholds.
7. Perform sensitivity analysis for model choices such as key schedule, related-key freedom, truncated states, or symmetry assumptions, and keep each optimum separately scoped.
8. Publish feasible witness, exclusion certificate, exact objective mapping, toolchain, and theorem/bound statement.

## Output contract

- An independently checked feasible object.
- A checked proof excluding all strictly better objects.
- Exact objective/rounding/cost interpretation.
- A parameter- and model-specific optimality statement.

## Non-negotiable guardrails

- Best found is not optimal.
- One-sided solver bounds must be labeled as such.
- Floating objective rounding may reverse a claimed inequality.
- Optimality in a relaxed or restricted model is not optimality for the full cryptographic problem.

## Related formal skills

- `pseudo-boolean-veripb-certification`
- `sat-lrat-certification`

## Related cryptanalysis skills in this pack (optional)

- `generic-baseline-and-security-level-calculator`
- `differential-family-analysis`

## Associated primary references

- **VERIPB-HOME** — [VeriPB](https://veripb.org/) (2026) — VeriPB project. `official-project`.
- **PBLEAN26** — [PBLean: Importing Pseudo-Boolean Proofs into Lean](https://arxiv.org/abs/2602.08692) (2026) — PBLean authors. `research-paper`.
- **LRAT17** — [Efficient Certified RAT Verification](https://arxiv.org/abs/1612.02353) (2017) — Luís Cruz-Filipe et al.. `research-paper`.
- **CVC5-PROOFS** — [cvc5 Proof Production](https://cvc5.github.io/docs-ci/docs-main/proofs/proofs.html) (2026) — cvc5 project. `official-manual`.

Bundled source metadata is in `references/REFERENCES.md`.
