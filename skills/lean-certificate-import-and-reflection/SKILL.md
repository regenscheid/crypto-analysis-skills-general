---
name: lean-certificate-import-and-reflection
description: "Imports externally generated SAT, pseudo-Boolean, algebraic, or other certificates into Lean and proves the connection from the encoded problem back to the original cryptographic proposition."
metadata:
  version: "0.1.0"
  display-name: "Lean Certificate Import and Reflection"
  category: "lean"
  tags: "lean, certificate, reflection, solver"
  requires: "original proposition, verified encoding or correspondence plan, external certificate"
  produces: "Lean theorem, certificate checker result, encoding theorem, replayable artifact"
  optional: "true"
  namespace: "formal"
---

# Lean Certificate Import and Reflection

## Purpose

Imports externally generated SAT, pseudo-Boolean, algebraic, or other certificates into Lean and proves the connection from the encoded problem back to the original cryptographic proposition.

## Use this skill when

Use this skill when search is best performed by an external high-performance tool but the final negative, optimality, or exact-computation result should be checked in Lean.

## Do not invoke automatically

Do not import only the solver’s formula and prove that formula unsatisfiable while leaving the cryptographic encoding unverified. The important theorem is about the original problem.

## Optional entry contract

**Inputs**
- original proposition
- verified encoding or correspondence plan
- external certificate

**Expected products**
- Lean theorem
- certificate checker result
- encoding theorem
- replayable artifact

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Define the original-domain object and claim in Lean before generating the solver instance. Give the encoding function a deterministic, versioned representation.
2. Prove soundness: every encoded assignment/witness maps to a valid original object or violation as appropriate. Prove completeness when UNSAT or optimality is used to exclude original objects.
3. Choose a certificate ecosystem with a small checker or proof reconstruction path, such as LRAT/CLRAT for SAT, VeriPB/PBLean for pseudo-Boolean reasoning, or Alethe/SMTCoq for supported SMT fragments.
4. Generate formula maps and objective metadata that preserve variable meaning, symmetry constraints, weights, and parameter values. Hash them together with the certificate.
5. Run the external solver as untrusted search. For SAT results, independently evaluate the model in the Lean specification; for UNSAT/optimality, check the complete certificate.
6. Import or reconstruct the certificate theorem in Lean, then compose it with the encoding theorems to derive the original cryptographic result.
7. Test the encoding on tiny exhaustive instances and deliberately mutated formulas/certificates to confirm the checker rejects missing clauses, wrong weights, and incomplete domains.
8. Monitor certificate size, elaboration memory, and kernel replay time. Use proof compression or hierarchical cube-and-conquer composition only with checked coverage.
9. Publish the original theorem, encoding source, generated instance, map, certificate, checker version, and clean replay log.

## Output contract

- A Lean theorem about the original cryptographic domain.
- Encoding soundness/completeness and objective-correspondence theorems.
- Pinned formula, variable map, certificate, and checker artifacts.
- Scaling and replay metrics.

## Non-negotiable guardrails

- UNSAT proves nothing beyond the exact encoded domain.
- Symmetry breaking and relaxations require preservation proofs.
- Do not trust a certificate parser more than necessary; include it in the TCB report.
- For optimization, certify both the found upper bound/witness and the lower-bound proof.

## Related formal skills

- `sat-lrat-certification`
- `pseudo-boolean-veripb-certification`
- `smt-proof-production-and-reconstruction`

## Related cryptanalysis skills in this pack (optional)

- `automated-algebra-and-search-model-builder`
- `automated-search-model-builder`

## Associated primary references

- **LRAT-CATCHER26** — [LRAT-Catcher: Importing SAT Refutations into Lean](https://arxiv.org/abs/2607.00815) (2026) — LRAT-Catcher authors. `research-paper`.
- **PBLEAN26** — [PBLean: Importing Pseudo-Boolean Proofs into Lean](https://arxiv.org/abs/2602.08692) (2026) — PBLean authors. `research-paper`.
- **LRAT17** — [Efficient Certified RAT Verification](https://arxiv.org/abs/1612.02353) (2017) — Luís Cruz-Filipe et al.. `research-paper`.
- **VERIPB-HOME** — [VeriPB](https://veripb.org/) (2026) — VeriPB project. `official-project`.
- **ALETHE** — [The Alethe Proof Format](https://arxiv.org/abs/2104.00649) (2021) — Hans-Jörg Schurr et al.. `research-paper`.
- **SMTCOQ-REPO** — [SMTCoq repository](https://github.com/smtcoq/smtcoq) (2026) — SMTCoq project. `official-repository`.

Bundled source metadata is in `references/REFERENCES.md`.
