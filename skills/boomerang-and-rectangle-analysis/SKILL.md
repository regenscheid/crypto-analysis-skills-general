---
name: boomerang-and-rectangle-analysis
description: "Build boomerang, amplified-boomerang and rectangle attacks on symmetric primitives with dependence-aware middle transitions and quartet-level data accounting. Use when no single long differential suffices but upper and lower differentials may combine."
metadata:
  version: "0.1"
  display-name: "Boomerang and Rectangle Analysis"
  tags: "boomerang, rectangle, BCT, quartets"
  requires: "design-assumption-graph, upper-and-lower-differentials, claim-model"
  produces: "boomerang-records, quartet-model, key-recovery-plan"
---

# Boomerang and Rectangle Analysis

## Use this skill when

No single long differential is strong enough, but the cipher can be split into upper and lower regions with useful differentials whose middle interaction may form quartets.

## Operating procedure

1. **Select the split and oracle model.** State whether the construction requires adaptive chosen plaintext/ciphertext, decryption, chosen tweaks, related keys, or can be converted to a rectangle attack using plaintext structures.
2. **Characterize the upper differential.** Give endpoint distribution, clusters, key dependence, and exact probability—not only a dominant trail.
3. **Characterize the lower differential.** Do the same in the reverse or forward direction required by the quartet construction.
4. **Model the middle dependency.** Use BCT, generalized/double BCT, exact enumeration, or target-specific conditional transitions. Do not assume upper and lower events are independent around shared S-boxes or nonlinear layers.
5. **Construct quartets.** Specify data structures, pairing, switching, filtering, expected right quartets, random quartets, collisions/duplicates, and memory/indexing.
6. **Choose boomerang versus rectangle variants.** Explain how the oracle model and data generation change probabilities and complexity. State any amplified or sandwich behavior explicitly.
7. **Extend boundary rounds.** Derive subkey guesses, partial encryption/decryption, quartet filters, false positives, candidate ranking, and final verification.
8. **Aggregate clusters carefully.** Include compatible upper/lower differential families and signs/dependencies. Avoid multiplying summed probabilities when compatibility is untested.
9. **Validate in layers.** Test local BCT/DBCT entries, core quartet probability, full data structure, wrong-key behavior, and key recovery over multiple keys.
10. **Audit full resources.** Count unique plaintexts/ciphertexts, queries, quartet generation, table memory, filtering, verification, and success.

## Output contract

Report:

- split, endpoints, and oracle requirements;
- upper/lower differential clusters;
- middle connectivity/dependence calculation;
- quartet construction and expected signal/noise;
- boundary key-recovery extension;
- direct experiments across keys;
- complete resource/success comparison;
- exact model, rounds, and claim impact.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `WAG99-BOOM`
- `CID18-BCT`
- `BS91-DIFF`

Full records are bundled in `references/REFERENCES.md`.
