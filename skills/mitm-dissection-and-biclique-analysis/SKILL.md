---
name: mitm-dissection-and-biclique-analysis
description: "Design and audit meet-in-the-middle attacks on symmetric primitives: cuts, partial matching, splice-and-cut, initial structures, dissection and bicliques. Use when the computation splits into forward and backward parts with partly independent key or state bits."
metadata:
  version: "0.1"
  display-name: "Meet-in-the-Middle, Dissection, and Biclique Analysis"
  tags: "meet-in-the-middle, dissection, biclique, time-memory"
  requires: "design-assumption-graph, claim-model, target-scope"
  produces: "mitm-records, cut-analysis, time-memory-frontier, validation-plan"
---

# Meet-in-the-Middle, Dissection, and Biclique Analysis

## Use this skill when

The target can be decomposed into forward and backward computations with partially independent key/state variables, has a narrow internal cut, repeated/expandable subcomputations, or enough degrees of freedom for biclique/initial-structure methods.

## Operating procedure

1. **Choose candidate cuts.** For each cut list the exact internal bits/words compared, forward-dependent variables, backward-dependent variables, shared variables, and computations that cross the cut.
2. **Map key-schedule dependencies.** Express round keys as functions of master-key variables. Reject fictitious independence introduced by treating round keys as free.
3. **Minimize matching information.** Explore partial matching, indirect partial matching, guessed intermediate bits, differential matching, and multi-stage filters. Derive random-collision and false-match rates.
4. **Use structural enhancements deliberately.** Consider splice-and-cut, initial structures, neutral words, bicliques, precomputed chunks, and multiple subsets only when their degrees of freedom and compatibility are proved.
5. **Construct the table/recursion.** Specify stored values, entry size, sort/hash/index method, collision handling, recomputation, and external-memory/I/O costs.
6. **Evaluate dissection.** For memory-limited settings derive recursive or staged time-memory tradeoffs and communication. Compare total work and wall-clock assumptions.
7. **Count data and verification.** State plaintext/ciphertext pairs, chosen conditions, number of surviving key/state candidates, equivalent keys, and final checks.
8. **Avoid misleading full-round claims.** Biclique-style attacks may produce a small asymptotic improvement with enormous constants or data restrictions. Compare concrete and generic costs honestly.
9. **Validate on reduced instances.** Verify dependency sets, matching values, candidate counts, and recovery end to end. Use randomized cut values to test false-match formulas.
10. **Map the Pareto frontier.** Report alternative cuts across time, memory, data, preprocessing, I/O, and parallelism rather than one optimized exponent.

## Output contract

Provide:

- exact cut/state/key dependency diagrams;
- forward/backward pseudocode and matching predicates;
- enhancements and their degrees of freedom;
- table/recursion/I/O design;
- false matches, survivors, and verification;
- complete time-memory-data-preprocessing frontier;
- experiments validating candidate counts;
- exact target/model/round impact.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `BKR11-BICLIQUE`
- `DDKS12-DISSECTION`
- `HELL80-TMTO`

Full records are bundled in `references/REFERENCES.md`.
