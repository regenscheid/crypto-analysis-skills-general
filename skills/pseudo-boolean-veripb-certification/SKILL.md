---
name: pseudo-boolean-veripb-certification
description: "Certifies pseudo-Boolean feasibility, optimization, counting-related transformations, and lower/upper bounds using VeriPB proof logs and optional PBLean reconstruction."
metadata:
  version: "0.1.0"
  display-name: "Pseudo-Boolean and VeriPB Certification"
  category: "certified-computation"
  tags: "pseudo-boolean, veripb, pblean, optimization, certificate"
  requires: "PB instance and objective, encoding map, solver/proof log"
  produces: "checked PB proof, certified bound or optimum, optional Lean theorem, replay artifacts"
  optional: "true"
  namespace: "formal"
---

# Pseudo-Boolean and VeriPB Certification

## Purpose

Certifies pseudo-Boolean feasibility, optimization, counting-related transformations, and lower/upper bounds using VeriPB proof logs and optional PBLean reconstruction.

## Use this skill when

Use this skill for cryptanalytic searches naturally expressed with weighted Boolean constraints or optimization, such as minimum trail weight, active-component bounds, combinatorial designs, codeword constraints, or cardinality-heavy models.

## Do not invoke automatically

Do not use pseudo-Boolean optimization merely because a MILP model already exists; first determine whether the exact objective and solver techniques can be logged in a supported, independently checkable proof format.

## Optional entry contract

**Inputs**
- PB instance and objective
- encoding map
- solver/proof log

**Expected products**
- checked PB proof
- certified bound or optimum
- optional Lean theorem
- replay artifacts

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Freeze the original problem, OPB/PB instance, objective sense, variable map, generator, solver, VeriPB proof format/checker, and optional PBLean version.
2. Validate the encoding and objective on tiny direct-enumeration instances. Confirm signs, offsets, inequalities, weights, objective scaling, and treatment of infeasible assignments.
3. Generate a proof log covering preprocessing, learned constraints, cutting planes, symmetry handling, objective bounds, and final conclusion. Ensure every solver feature used is supported by the checker.
4. Run VeriPB independently against the exact instance and proof hash. Capture checker resources and any warnings about unsupported steps.
5. For optimum claims, ensure both a feasible witness at the claimed value and a checked proof excluding every better value, or an equivalent certified optimization derivation.
6. When importing through PBLean, connect the PB variables and objective to original-domain definitions and record any native/reflective TCB components.
7. For decomposed instances, prove coverage and aggregate subproofs without gaps or duplicated assumptions.
8. Publish the PB instance, model/witness, proof log, checker output, objective interpretation, and exact cryptanalytic scope.

## Output contract

- A VeriPB-checked feasibility/bound/optimality artifact.
- A decoded and independently checked witness when feasible.
- Encoding/objective correspondence evidence and optional PBLean theorem.
- Replay manifest with solver/checker versions and resources.

## Non-negotiable guardrails

- A lower bound requires proof that no better feasible original-domain object was omitted by the encoding.
- Optimization preprocessing must be represented in the proof log or trusted explicitly.
- Do not confuse an activity-count surrogate with exact probability/correlation unless their relation is proved.
- PBLean imports the certified instance result; original-domain semantics remain a separate obligation.

## Related formal skills

- `optimization-and-optimality-certification`
- `lean-certificate-import-and-reflection`

## Related cryptanalysis skills in this pack (optional)

- `differential-family-analysis`
- `integral-and-division-property-analysis`

## Associated primary references

- **VERIPB-HOME** — [VeriPB](https://veripb.org/) (2026) — VeriPB project. `official-project`.
- **VERIPB-REPO** — [VeriPB repository](https://github.com/VeriPB/VeriPB) (2026) — VeriPB project. `official-repository`.
- **PBLEAN26** — [PBLean: Importing Pseudo-Boolean Proofs into Lean](https://arxiv.org/abs/2602.08692) (2026) — PBLean authors. `research-paper`.
- **PBLEAN-REPO** — [PBLean repository](https://github.com/leansolving/pblean) (2026) — PBLean project. `official-repository`.

Bundled source metadata is in `references/REFERENCES.md`.
