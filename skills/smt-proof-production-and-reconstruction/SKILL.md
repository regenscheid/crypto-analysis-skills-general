---
name: smt-proof-production-and-reconstruction
description: "Uses SMT solvers for bit-vectors, arrays, arithmetic, datatypes, or combinations of theories while preserving proof output, independent checking, reconstruction limits, and exact theory semantics."
metadata:
  version: "0.1.0"
  display-name: "SMT Proof Production and Reconstruction"
  category: "certified-computation"
  tags: "smt, cvc5, alethe, proof-reconstruction, theories"
  requires: "SMT-LIB problem, theory/logic selection, claim and encoding map"
  produces: "checked or reconstructed SMT proof, model/counterexample, theory coverage report, replay bundle"
  optional: "true"
  namespace: "formal"
---

# SMT Proof Production and Reconstruction

## Purpose

Uses SMT solvers for bit-vectors, arrays, arithmetic, datatypes, or combinations of theories while preserving proof output, independent checking, reconstruction limits, and exact theory semantics.

## Use this skill when

Use this skill when first-order theory reasoning substantially simplifies the formal obligation and the chosen solver can emit a proof or model that can be checked or reconstructed with acceptable trust.

## Do not invoke automatically

Do not choose SMT solely for convenience when the result is a high-value universal claim but the selected theory combination has no usable proof export/checker. A SAT lowering or in-prover proof may provide stronger evidence.

## Optional entry contract

**Inputs**
- SMT-LIB problem
- theory/logic selection
- claim and encoding map

**Expected products**
- checked or reconstructed SMT proof
- model/counterexample
- theory coverage report
- replay bundle

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Freeze SMT-LIB input, solver, options, random seeds, proof format, checker/reconstructor, and theory versions. Avoid implicit solver defaults.
2. Specify exact semantics for bit-vectors, integers, reals, arrays, floating point, datatypes, quantifiers, and uninterpreted functions. Confirm that coercions match the cryptographic model.
3. For SAT results, retain the model, evaluate every assertion, decode original variables, and verify the counterexample/witness independently.
4. For UNSAT, request cvc5 internal/CPC, Alethe, LFSC, or another supported proof. Determine whether an independent checker or proof-assistant reconstruction covers every rule/theory used.
5. Use Carcara, SMTCoq, Isabelle reconstruction, or another checker only within documented coverage; classify unsupported steps, trusted theory lemmas, and solver-specific extensions.
6. For quantified problems, inspect instantiations and triggers; avoid interpreting timeout or `unknown` as evidence. For nonlinear arithmetic, verify exactness and proof support.
7. Cross-check critical obligations with an alternate solver or bit-blasted SAT route and test reduced instances exhaustively.
8. Publish input, model/proof, checker output, theory coverage, original-domain correspondence, and remaining TCB.

## Output contract

- A model plus independently checked original-domain witness, or a proof artifact with documented checking/reconstruction coverage.
- Exact SMT-LIB and solver configuration.
- Theory/rule support and trust report.
- Clean replay and alternate-check results where practical.

## Non-negotiable guardrails

- `unknown`, timeout, or resource exhaustion proves nothing.
- An Alethe proof is useful only if the checker supports the emitted theory rules.
- Bit-vector, integer, and real arithmetic are not interchangeable.
- Quantifier instantiation and opaque theory lemmas belong in the audit.

## Related formal skills

- `bitvector-equivalence-and-sat-lowering`
- `sat-lrat-certification`

## Related cryptanalysis skills in this pack (optional)

- `algebraic-sat-smt-cp-and-cube-analysis`

## Associated primary references

- **CVC5-PROOFS** — [cvc5 Proof Production](https://cvc5.github.io/docs-ci/docs-main/proofs/proofs.html) (2026) — cvc5 project. `official-manual`.
- **ALETHE** — [The Alethe Proof Format](https://arxiv.org/abs/2104.00649) (2021) — Hans-Jörg Schurr et al.. `research-paper`.
- **CVC5-ALETHE** — [cvc5 Alethe proof output](https://cvc5.github.io/docs/cvc5-1.0.0/proofs/output_alethe.html) (2026) — cvc5 project. `official-manual`.
- **SMTCOQ-REPO** — [SMTCoq repository](https://github.com/smtcoq/smtcoq) (2026) — SMTCoq project. `official-repository`.
- **CARCARA-REPO** — [Carcara Alethe proof checker](https://github.com/ufmg-smite/carcara) (2026) — SMITE. `official-repository`.

Bundled source metadata is in `references/REFERENCES.md`.
