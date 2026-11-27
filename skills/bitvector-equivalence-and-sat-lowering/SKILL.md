---
name: bitvector-equivalence-and-sat-lowering
description: "Proves equivalence of fixed-width cryptographic functions or lowers precise bit-vector semantics to SAT while preserving word operations, undefined behavior, and the connection to original algorithms."
metadata:
  version: "0.1.0"
  display-name: "Bit-Vector Equivalence and SAT Lowering"
  category: "certified-computation"
  tags: "bitvector, word-arithmetic, equivalence, sat-lowering, cryptographic-code"
  requires: "two functions or function/spec pair, word semantics, bounded input contract"
  produces: "equivalence theorem or counterexample, lowering correspondence, SAT/SMT artifacts"
  optional: "true"
  namespace: "formal"
---

# Bit-Vector Equivalence and SAT Lowering

## Purpose

Proves equivalence of fixed-width cryptographic functions or lowers precise bit-vector semantics to SAT while preserving word operations, undefined behavior, and the connection to original algorithms.

## Use this skill when

Use this skill for S-boxes, ARX layers, permutations, key schedules, encodings, arithmetic kernels, compiler rewrites, or reduced bounded implementations where all relevant state is finite and fixed-width.

## Do not invoke automatically

Do not use bit-vector equivalence to claim mathematical integer correctness outside the represented width or to ignore panics, poison, aliasing, memory, or protocol state not captured by the functions.

## Optional entry contract

**Inputs**
- two functions or function/spec pair
- word semantics
- bounded input contract

**Expected products**
- equivalence theorem or counterexample
- lowering correspondence
- SAT/SMT artifacts

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Freeze both definitions and normalize parameter widths, byte/bit order, shifts, rotations, signedness, overflow, division/modulo, comparisons, and exceptional behavior.
2. Define the equivalence relation: exact output equality, relation under representation conversion, refinement under preconditions, or observational equivalence including failure behavior.
3. Construct a shared executable test harness and compare boundary/random cases before formal solving. Preserve any counterexample inputs and intermediate states.
4. Use Lean `bv_decide`, SMT bit-vectors, SAW/Cryptol, or a bit-blasted SAT model according to scale and desired TCB. Record lowering and preprocessing steps.
5. If lowering to CNF, prove or validate the Tseitin/circuit mapping and retain variable maps sufficient to decode models and connect UNSAT to the equivalence theorem.
6. For implementation artifacts, include memory reads/writes and compiler semantics or constrain the theorem to pure extracted functions.
7. Partition huge domains only with a proved cover. Check every partition certificate and combine results mechanically.
8. Publish theorem, preconditions, counterexamples or certificates, lowering trust, and exact bounded scope.

## Output contract

- A word-level equivalence/refinement statement.
- A checked theorem, decoded counterexample, or certified partitioned search.
- Bit/byte/order and operation-semantics crosswalk.
- Lowering/encoding and TCB report.

## Non-negotiable guardrails

- Fixed-width equivalence is width- and precondition-specific.
- Undefined behavior or unmodeled memory can make a pure bit-vector theorem irrelevant to deployed code.
- Do not hide representation conversion or failure behavior outside the equivalence relation.
- Partition coverage must be proved.

## Related formal skills

- `lean-bitvectors-and-word-arithmetic`
- `sat-lrat-certification`

## Related cryptanalysis skills in this pack (optional)

- `arx-differential-rotational-rx-analysis`

## Associated primary references

- **LEAN-BVDECIDE** — [Lean tactic reference: bv_decide and decision procedures](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/) (2026) — Lean project. `official-manual`.
- **LRAT17** — [Efficient Certified RAT Verification](https://arxiv.org/abs/1612.02353) (2017) — Luís Cruz-Filipe et al.. `research-paper`.
- **SAW-DOCS** — [Software Analysis Workbench documentation](https://galoisinc.github.io/saw-script/) (2026) — Galois. `official-manual`.
- **CRYPTOL-DOCS** — [Cryptol documentation](https://galoisinc.github.io/cryptol/) (2026) — Galois. `official-manual`.

Bundled source metadata is in `references/REFERENCES.md`.
