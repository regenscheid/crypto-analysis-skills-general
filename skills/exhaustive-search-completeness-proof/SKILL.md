---
name: exhaustive-search-completeness-proof
description: "Establishes that an exhaustive or partitioned computation covers the intended finite domain exactly and that its result aggregation is correct, rather than treating a completed program run as self-certifying."
metadata:
  version: "0.1.0"
  display-name: "Exhaustive Search Completeness Proof"
  category: "certified-computation"
  tags: "exhaustive-search, completeness, partition, enumeration, verification"
  requires: "finite domain definition, search implementation, claim and stopping condition"
  produces: "coverage proof, verified aggregation, run manifest, result theorem or qualified computational claim"
  optional: "true"
  namespace: "formal"
---

# Exhaustive Search Completeness Proof

## Purpose

Establishes that an exhaustive or partitioned computation covers the intended finite domain exactly and that its result aggregation is correct, rather than treating a completed program run as self-certifying.

## Use this skill when

Use this skill when a cryptanalytic conclusion depends on full enumeration—especially nonexistence, exact counts, minimum/maximum values, all counterexamples, or parameter-wide classification.

## Do not invoke automatically

Do not require a formal completeness proof for exploratory sampling or when a found witness alone settles the claim. Use this only when “all,” “none,” “exactly,” or “optimal” depends on coverage.

## Optional entry contract

**Inputs**
- finite domain definition
- search implementation
- claim and stopping condition

**Expected products**
- coverage proof
- verified aggregation
- run manifest
- result theorem or qualified computational claim

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Define the domain mathematically, including ranges, equivalence classes, malformed cases, keys, rounds, boundary values, and whether symmetries are quotiented.
2. Define a canonical enumeration and prove or test bijection/surjection as needed between domain elements and iteration indices, shards, cubes, or recursive branches.
3. Audit loop bounds, integer overflow, work distribution, resume/checkpoint logic, duplicate handling, pruning, and early termination. Treat scheduler success separately from coverage.
4. Prove pruning rules preserve the claimed result and that symmetry representatives cover every equivalence class. Count or otherwise check partitions before running expensive jobs.
5. Use per-shard hashes, immutable parameters, deterministic seeds where relevant, progress records, and a final aggregation function that detects missing, duplicate, or mismatched shards.
6. Validate against direct enumeration on small domains and deliberately remove/duplicate shards to ensure the aggregator fails.
7. For negative or optimality claims, combine coverage with an independently verified predicate/objective and, where possible, a solver certificate or proof-assistant computation.
8. Publish domain theorem/status, shard manifest, code, logs, result hashes, resource limits, and exact conclusion.

## Output contract

- A domain-to-enumeration coverage argument or theorem.
- A complete shard/run/aggregation manifest with integrity checks.
- Validated predicate and objective implementation.
- An exact count/bound/nonexistence result with clearly stated trust level.

## Non-negotiable guardrails

- Completed processes do not imply full domain coverage.
- Pruning and symmetry reduction require preservation proofs.
- Integer overflow and distributed-job loss can silently invalidate counts.
- No result outside the finite stated domain may be inferred.

## Related formal skills

- `finite-search-model-and-encoding-validation`
- `optimization-and-optimality-certification`

## Related cryptanalysis skills in this pack (optional)

- `public-key-reproduction-and-falsification-planner`
- `symmetric-reproduction-and-falsification-planner`

## Associated primary references

- **LEAN-TPIL** — [Theorem Proving in Lean 4](https://leanprover.github.io/theorem_proving_in_lean4/) (2024) — Jeremy Avigad et al.. `official-text`.
- **LRAT17** — [Efficient Certified RAT Verification](https://arxiv.org/abs/1612.02353) (2017) — Luís Cruz-Filipe et al.. `research-paper`.
- **VERIPB-HOME** — [VeriPB](https://veripb.org/) (2026) — VeriPB project. `official-project`.

Bundled source metadata is in `references/REFERENCES.md`.
