---
name: sat-lrat-certification
description: "Certifies Boolean satisfiability witnesses or unsatisfiability results using independent evaluation and LRAT/FRAT-derived proof checking, optionally importing the result into Lean."
metadata:
  version: "0.1.0"
  display-name: "SAT and LRAT Certification"
  category: "certified-computation"
  tags: "sat, lrat, frat, unsat, certificate"
  requires: "CNF formula and provenance, claim/encoding crosswalk, SAT solver and checker"
  produces: "checked model or UNSAT certificate, checker log, original-domain result when correspondence is proved"
  optional: "true"
  namespace: "formal"
---

# SAT and LRAT Certification

## Purpose

Certifies Boolean satisfiability witnesses or unsatisfiability results using independent evaluation and LRAT/FRAT-derived proof checking, optionally importing the result into Lean.

## Use this skill when

Use this skill when a finite cryptographic question has an exact CNF encoding and a machine-checkable SAT/UNSAT result would materially strengthen an existence, impossibility, or lower-bound claim.

## Do not invoke automatically

Do not require LRAT for an ordinary candidate witness that can be checked much more simply in the original cryptographic domain. Do not claim original-domain impossibility from CNF UNSAT without the encoding correspondence.

## Optional entry contract

**Inputs**
- CNF formula and provenance
- claim/encoding crosswalk
- SAT solver and checker

**Expected products**
- checked model or UNSAT certificate
- checker log
- original-domain result when correspondence is proved

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Freeze the original problem, encoding generator, CNF bytes/hash, variable map, solver, proof logger, elaborator, and checker versions.
2. For SAT, retain the full model and independently evaluate every clause, then decode it and verify the cryptographic witness in a separate implementation.
3. For UNSAT, configure the solver to emit FRAT/LRAT or another accepted proof log; if using FRAT, elaborate to a checker-oriented format and preserve both artifacts.
4. Run an independent LRAT checker with resource limits and verify the exact CNF hash. Reject truncated, mismatched, or unchecked proof logs.
5. Where Lean integration is desired, use LRAT-Catcher or a verified importer and prove the formula/encoding connection to the original theorem.
6. For cube-and-conquer or partitioned search, prove that cubes cover the domain and check every subproof plus the top-level coverage proof.
7. Cross-check small instances and, for large claims, test intentional CNF mutations or clause deletions to ensure the pipeline notices changes.
8. Record certificate size, checking time/memory, solver/checker exit status, and any trusted parser or native component.
9. Publish the CNF, mapping, certificate/model, checker logs, theorem scope, and TCB.

## Output contract

- A satisfiable assignment plus original-domain verified witness, or an independently checked UNSAT certificate.
- Exact CNF/variable-map/generator provenance.
- Checker and optional Lean-import logs.
- A claim statement limited to the proved encoding domain.

## Non-negotiable guardrails

- `UNSAT` printed by a solver is not a certificate.
- A checked LRAT proof establishes only unsatisfiability of the exact CNF.
- Partition coverage and encoding correctness are separate proof obligations.
- Keep solver heuristics untrusted and checker/parser assumptions explicit.

## Related formal skills

- `finite-search-model-and-encoding-validation`
- `lean-certificate-import-and-reflection`

## Related cryptanalysis skills in this pack (optional)

- `automated-search-model-builder`

## Associated primary references

- **LRAT17** — [Efficient Certified RAT Verification](https://arxiv.org/abs/1612.02353) (2017) — Luís Cruz-Filipe et al.. `research-paper`.
- **FRAT22** — [FRAT: A Flexible Proof Format for SAT Solver Elaboration](https://arxiv.org/abs/2109.09665) (2022) — Marijn Heule et al.. `research-paper`.
- **LRAT-CATCHER26** — [LRAT-Catcher: Importing SAT Refutations into Lean](https://arxiv.org/abs/2607.00815) (2026) — LRAT-Catcher authors. `research-paper`.
- **CADICAL-REPO** — [CaDiCaL SAT solver](https://github.com/arminbiere/cadical) (2026) — Armin Biere et al.. `official-repository`.
- **LEAN-BVDECIDE** — [Lean tactic reference: bv_decide and decision procedures](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/) (2026) — Lean project. `official-manual`.

Bundled source metadata is in `references/REFERENCES.md`.
