---
name: slide-invariant-subspace-and-symmetry-analysis
description: "Find exploitable self-similarity in symmetric primitives: slid pairs, invariant subspaces and partitions, fixed structures and weak-key symmetries, checking constants and schedules. Use when rounds repeat, constants are weak or periodic, or the design has automorphisms."
metadata:
  version: "0.1"
  display-name: "Slide, Invariant-Subspace, and Symmetry Analysis"
  tags: "slide, invariant-subspace, partitioning, symmetry"
  requires: "design-assumption-graph, claim-model, round-structure"
  produces: "structural-attack-records, invariant-proof, weak-key-analysis"
---

# Slide, Invariant-Subspace, and Symmetry Analysis

## Use this skill when

Rounds repeat or nearly repeat, constants are weak or periodic, key schedules preserve relations, affine/nonlinear subspaces may map to themselves, or the primitive has complementations, rotations, branch permutations, or other automorphisms.

## Operating procedure

1. **Enumerate candidate symmetries.** Consider round shifts, state rotations/reflections, branch/lane permutations, affine translations, complementations, key transformations, fixed points, and invariant partitions.
2. **Test operation commutation.** For each transformation prove or refute how it interacts with every S-box, linear layer, addition, rotation, constant, key/tweak injection, initialization, and finalization.
3. **Analyze round self-similarity.** Determine whether consecutive rounds are identical, conjugate, periodic, or made equivalent under a key/state transformation. Quantify how constants or schedule evolution break the relation.
4. **Search slid pairs.** Define exact pair relation, expected density, data generation, matching/filtering, false pairs, and how a slid pair exposes key/state information.
5. **Search invariant subspaces/partitions.** Solve for affine or nonlinear sets preserved by the round/keyed transformation. Prove closure and state the key class, constants, and round range.
6. **Quantify weak structure.** Calculate weak-key fraction, invariant-set size, probability of entering/staying in it, and whether the attacker can select or recognize relevant inputs/outputs.
7. **Connect to a security result.** Build a distinguisher, key recovery, partitioning attack, equivalent-key attack, or proof of reduced effective domain. Do not stop at a visually symmetric state.
8. **Use exact and computational checks.** SAT/SMT, algebraic solving, group-action reasoning, and exhaustive small instances can discover candidates; independently verify closure and attack behavior.
9. **Test symmetry breakers.** Vary constants, round numbers, key schedule, domain separators, and finalization to identify exactly which component blocks transfer to the full construction.
10. **Avoid average-case overclaiming.** A severe weak-key attack may be irrelevant to random keys unless its density and detectability are quantified; conversely, a tiny invariant set may still violate a universal claim.

## Output contract

Provide:

- candidate transformation/subspace/partition;
- operation-by-operation commutation or closure proof;
- round/key/constant scope;
- weak-key/state density and attainability;
- slid-pair or invariant-based attack algorithm;
- false-positive and verification analysis;
- exact computational/proof validation;
- claim impact with average- versus worst-case distinction.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `BW99-SLIDE`
- `BW00-SLIDE`
- `LAAZ11-INV`
- `TLS19-NLINV`
- `HM97-PARTITION`

Full records are bundled in `references/REFERENCES.md`.
