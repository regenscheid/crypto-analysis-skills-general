---
name: security-proof-and-bound-auditor
description: "Audit symmetric constructions' security games, reductions, bad-event bounds, concrete constants, idealized models and instantiation. Use when a symmetric claim rests on a theorem or advantage table; public-key ROM/QROM proofs use security-proof-rom-qrom-and-tightness-auditor."
metadata:
  version: "0.1"
  display-name: "Security Proof and Bound Auditor"
  tags: "proof-audit, concrete-security, reductions, bounds"
  requires: "claim-adversary-matrix, target-proof, parameter-set, usage-profile"
  produces: "proof-audit, bound-recalculation, assumption-gap-log, counterexample-tests"
---

# Security Proof and Bound Auditor

## Use this skill when

A security claim is justified by a theorem, game-hopping proof, reduction, idealized primitive model, or concrete advantage table. This skill checks what the result actually establishes and whether the bound survives concrete instantiation and operational use.

## Operating procedure

1. **Freeze the proof artifact.** Record paper/specification version, theorem and lemma numbers, corrections, proof appendix, and the construction version to which the proof applies.
2. **Map theorem to claim.** Rewrite the theorem as a claim–adversary row: object, game, oracles, adaptivity, nonce/tweak/key rules, number of users, query and length limits, success metric, and assumptions. Identify any advertised prose claim broader than the theorem.
3. **Reconstruct syntax and domains.** Check input/output spaces, parsing, injective encodings, length limits, statefulness, error behavior, decryption/verification semantics, and domain separation. Prove or test correctness conditions separately from security.
4. **List ideal objects and assumptions.** Identify random functions/permutations, ideal ciphers, tweakable permutations, independent keys, uniform nonces, secret/public randomness, computational assumptions, and independence assumptions. State which are modeled and which are merely asserted.
5. **Rebuild the game hops or reduction.** For each transition record the changed experiment, simulator interface, adversary view, claimed indistinguishability step, and exact loss. Check that the simulator can answer adaptive and inverse queries consistently and within its resource budget.
6. **Audit bad events and probability accounting.** Recompute collision, repetition, forgery, truncation, and conditioning probabilities. Check union bounds, dependence, adaptivity, hidden conditioning, omitted event intersections, and whether a birthday approximation is used outside its range.
7. **Audit restrictions.** Track per-user and total queries, total processed blocks, message-length distributions, nonce uniqueness/misuse, decryption failures, tag length, state resets, key commitment, related keys/tweaks, chosen-ciphertext access, and Q1/Q2 limitations. Do not average away an operationally relevant worst case without justification.
8. **Recompute concrete loss.** Substitute actual parameters and usage limits with exact constants where available. Separate primitive advantage, construction loss, multi-user factors, verification terms, and implementation failure probabilities.
9. **Bridge ideal to real.** State what PRP/PRF/TBC or permutation security is required of the instantiated primitive and add the best applicable cryptanalytic bound. Do not treat an ideal-cipher or random-permutation theorem as an unconditional construction guarantee.
10. **Probe edge cases.** Test zero/maximum lengths, repeated or malformed domains, nonce collisions, related inputs, decryption-error behavior, empty associated data, tag truncation, state reinitialization, and parameter limits. Use small exhaustive models when they can falsify a proof step.
11. **Separate proof defects from attacks.** Classify findings as ambiguity, missing case, invalid step, loose bound, model mismatch, concrete-parameter problem, or exploitable counterexample. A gap alone is not an attack; an attack requires an adversary and measured or proved advantage.
12. **Record uncertainty and corrections.** Preserve author/designer responses, errata, revised bounds, and which conclusions they supersede.

## Output contract

Produce a proof audit containing:

- exact theorem-to-claim mapping;
- construction syntax and correctness checks;
- assumptions and ideal objects;
- game-hop/reduction table with per-hop losses;
- bad-event and probability recalculation;
- model and usage restrictions;
- concrete instantiated bound and generic/cryptanalytic comparison;
- ideal-to-real gap;
- edge-case tests or counterexamples;
- findings classified by severity and exploitability;
- conclusion limited to the theorem's exact scope, plus evidence needed to resolve open issues.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `BR-INTRO`
- `LR88`
- `LRW02-TBC`
- `BN00`
- `RS06-SIV`
- `MRH04`
- `ML15-MULTIKEY`
- `NIST-38D`

Full records are bundled in `references/REFERENCES.md`.
