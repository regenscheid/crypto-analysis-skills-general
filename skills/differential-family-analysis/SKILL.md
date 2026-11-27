---
name: differential-family-analysis
description: "Find, evaluate, cluster and extend XOR, modular, truncated, higher-order and mixed differential properties of symmetric primitives. Use when differences propagate nonuniformly, diffusion is slow, or a published differential may transfer."
metadata:
  version: "0.1"
  display-name: "Differential Family Analysis"
  tags: "differential, truncated-differential, higher-order, trail-search"
  requires: "design-assumption-graph, claim-model, round-scope"
  produces: "differential-records, trail-clusters, key-recovery-hypotheses, validation-plan"
---

# Differential Family Analysis

## Use this skill when

The target has nonuniform propagation of differences through nonlinear operations, slow diffusion, controllable input structures, useful truncated patterns, or a published differential that may transfer.

## Operating procedure

1. **Choose the difference domain.** Define XOR, modular, additive, truncated/set-valued, mixed, rotational/RX, or higher-order derivatives. Justify why the domain matches the target operations and attacker interface.
2. **Build exact local transitions.** For S-boxes compute the DDT and, where relevant, key/tweak-dependent tables. For modular addition use carry-aware dynamic programming or exact bit-vector constraints. For linear layers prove propagation exactly.
3. **State the stochastic model.** Identify where Markov, independent-round-key, random-key averaging, or independence approximations enter. Do not assume a fixed-key cipher inherits averaged transition probabilities without analysis.
4. **Search trails with exact endpoints and boundaries.** Record fixed/free differences, active components, key-schedule coupling, constants, and excluded cases. Validate every witness directly.
5. **Move from trails to differentials.** Enumerate, sample, or bound clusters of trails sharing endpoints. Account for dependencies and key dependence; do not equate the best trail probability with the differential probability.
6. **Explore truncated and higher-order structure.** Track sets/subspaces of possible differences, impossible transitions, derivative order, and data structures required to realize them. State what information is discarded by truncation.
7. **Test boundary extensions.** Add rounds before/after the core, identify required subkey guesses or filters, and invoke `distinguisher-to-key-recovery-extension` for recovery claims.
8. **Design statistical validation.** Compare observed counts with the correct null distribution across multiple keys, structures, and endpoints. Predefine multiple-testing treatment and confidence intervals.
9. **Audit feasibility.** Enforce unique-data limits, chosen-input requirements, weak-key fractions, memory for counters/tables, and verification cost.
10. **Record negative knowledge.** Save proved impossible endpoints, dominant target-specific blockers, and model relaxations that produced spurious trails.

## Output contract

For each candidate provide:

- exact difference definition and endpoints;
- local transition evidence and complete trail(s);
- trail versus differential/cluster status;
- probability/weight derivation and assumptions;
- key/tweak dependence and round scope;
- data structure and potential extension;
- direct validation and statistical results;
- generic comparison and exact claim impact.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `BS91-DIFF`
- `LMM91-MARKOV`
- `KNU95-TRUNC`
- `MWGP11-MILP`
- `SHW14-AUTO`
- `LM01-ADD`

Full records are bundled in `references/REFERENCES.md`.
