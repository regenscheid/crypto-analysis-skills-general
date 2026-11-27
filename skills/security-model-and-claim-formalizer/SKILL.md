---
name: security-model-and-claim-formalizer
description: "Turn informal symmetric-cryptography security statements into explicit games, adversary powers, success events, resources and non-goals. Use before evaluating attacks when a symmetric primitive is called secure or 128-bit without a game; public-key: public-key-security-model-and-claim-formalizer."
metadata:
  version: "0.1"
  display-name: "Security Model and Claim Formalizer"
  tags: "security-model, definitions, games, claims"
  requires: "target-artifact, security-claims"
  produces: "claim-adversary-matrix, formal-game-sketch, ambiguity-log"
---

# Security Model and Claim Formalizer

## Use this skill when

A specification, paper, review, or discussion says a primitive or construction is “secure,” “128-bit secure,” “indistinguishable,” “authenticated,” “misuse-resistant,” or “resistant to attack” without an exact game and resource statement. Run it before evaluating attacks or comparing complexities.

## Operating procedure

1. **Identify the object being modeled.** Choose the exact abstraction:
   - block cipher as a keyed permutation or strong pseudorandom permutation;
   - tweakable block cipher;
   - stream cipher/stateful generator;
   - PRF, MAC, or variable-input-length PRF;
   - compression function, hash, XOF, or public permutation;
   - encryption, authenticated encryption, deterministic AE, or key wrap;
   - composed protocol interface rather than the primitive alone.
2. **Extract each claim verbatim and assign a claim ID.** Preserve qualifiers such as “up to,” “assuming unique nonces,” “single user,” “classical,” or “excluding related keys.”
3. **Choose the exact security property/game.** Examples include PRF, PRP, SPRP, tweakable PRP, IND-CPA, IND-CCA, ciphertext integrity, authenticated encryption, nonce-respecting AEAD, nonce-misuse resistance, deterministic AE, EUF-CMA/SUF-CMA, collision resistance, preimage resistance, second-preimage resistance, indifferentiability, key recovery, state recovery, forgery, or distinguishing advantage.
4. **Enumerate adversary interfaces.** Record encryption/decryption, chosen plaintext/ciphertext, known plaintext, chosen IV/nonce/tweak, nonce reuse, state reset, related-key functions, multi-user access, adaptivity, online/offline phases, and access to internal permutations or components.
5. **Separate quantum models.** Distinguish classical, Q1 (classical online queries with quantum offline computation), and Q2 (superposition oracle queries). State how the oracle is implemented and costed.
6. **Define the success event and advantage.** Write the experiment or an unambiguous pseudocode sketch. Specify whether success means distinguishing, recovering all/part of a key or state, producing a fresh valid forgery, finding any collision, or violating a reduction bound.
7. **State resources and units.** Include query count, unique data, chosen structures, primitive-equivalent time, memory bits/bytes/words, preprocessing, communication, parallel depth, and success probability/advantage.
8. **Record assumptions and non-goals.** Separate ideal-primitive, random-key, nonce uniqueness, independent keys, weak-key exclusions, leakage-free implementation, and computational assumptions. Record attack classes the claim does not cover.
9. **Resolve or expose ambiguity.** If prose admits two plausible games, create two matrix rows. Do not collapse them into one conclusion.
10. **Connect attacks to claims.** For every attack record, identify the exact row it violates or merely informs. A structural property may be interesting without violating any advertised game.

## Output contract

For each claim produce:

- claim ID and verbatim source locator;
- exact target/version/parameters;
- game/property and pseudocode sketch;
- adversary interfaces and restrictions;
- classical/Q1/Q2 classification;
- resource budget and success measure;
- assumptions and non-goals;
- ambiguities and alternate interpretations;
- attacks/evidence currently mapped to the row.

Use `assets/CLAIM_ADVERSARY_MATRIX.md`.

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
- `RS04-HASH`
- `RS06-SIV`
- `MRH04`
- `ML15-MULTIKEY`
- `NIST-38D`
- `ROG02-AEAD`

Full records are bundled in `references/REFERENCES.md`.
