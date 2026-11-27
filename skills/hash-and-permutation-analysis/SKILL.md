---
name: hash-and-permutation-analysis
description: "Evaluate hash functions, XOFs, compression functions, sponges and public permutations for collision, preimage, distinguishing, multicollision, herding and sponge-specific attacks. Use when the target is a hash or permutation; keeps primitive and full-construction properties apart."
metadata:
  version: "0.1"
  display-name: "Hash and Permutation Analysis"
  tags: "hash, permutation, collision, preimage, sponge"
  requires: "hash-or-permutation-spec, claim-model, construction-map"
  produces: "hash-attack-records, construction-analysis, generic-comparison, validation-plan"
---

# Hash and Permutation Analysis

## Use this skill when

The target is a hash function, XOF, compression function, sponge/duplex construction, public permutation, or hash-based composition. Always distinguish the primitive/permutation property from the full construction property.

## Operating procedure

1. **Formalize the target notion.** Collision, chosen-prefix collision, near collision, preimage, second preimage, multicollision, herding/commitment, indifferentiability, state recovery, or permutation distinguisher. State fixed- versus variable-length and target-message conditions.
2. **Map the construction.** Compression mode, chaining value, message schedule, feedforward, padding, counters, domain separation, rate/capacity, absorb/squeeze, finalization, and output truncation.
3. **Establish generic baselines.** Include collision, preimage, second-preimage, multicollision, long-message, many-target, capacity, and quantum baselines under the exact domain/output lengths.
4. **Search differential/local-collision paths.** Build operation-level conditions, message modification, neutral bits/words, disturbance correction, clusters, and path probabilities. Account for feedforward and valid padding/message constraints.
5. **Evaluate rebound and MITM.** Identify inbound degrees of freedom, outbound probabilities, preimage cuts, partial matching, table memory, and construction-level boundary control.
6. **Evaluate generic construction attacks.** Check Joux multicollisions, expandable messages, second-preimage shortcuts for long messages, herding, length extension, and multicall/domain-separation interactions only where construction prerequisites hold.
7. **For sponge/duplex designs, model rate and capacity.** Track what is public/hidden, permutation calls, state collisions, absorption/squeezing, domain separators, keyed modes, and whether an attack is generic in capacity or exploits the permutation.
8. **Separate free-start/semi-free-start.** State whether chaining value, state, message, key, or IV is controlled. Do not translate a free-start collision into a standard collision without a construction bridge.
9. **Validate artifacts.** Recompute paths, verify message pairs/preimages, instrument intermediate states, check padding/encoding, and independently hash outputs. Preserve actual examples and scripts.
10. **State security impact precisely.** A permutation distinguisher or reduced-round collision may be valuable without violating full hash security; explain its relation to margins and proofs.

## Output contract

Provide:

- exact notion, construction, and controlled variables;
- generic baseline table;
- attack path/skeleton and construction bridge;
- free-start/standard and reduced/full distinctions;
- message/state constraints and examples;
- complete resources, success, and quantum/classical model;
- independent validation;
- exact claim impact and remaining margin.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `RS04-HASH`
- `MRH04`
- `JOU04-MULTI`
- `KS05-2PRE`
- `KK06-HERD`
- `MRST09-REBOUND`
- `BDPV08-SPONGE`
- `KECCAK-SPEC`

Full records are bundled in `references/REFERENCES.md`.
