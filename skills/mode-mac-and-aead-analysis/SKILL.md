---
name: mode-mac-and-aead-analysis
description: "Analyze symmetric modes, MACs, key wrap and AEAD for privacy, authenticity, nonce behavior, tag bounds, domain separation, multi-user effects and misuse. Use when a block cipher, hash or permutation is composed into an encryption or authentication construction."
metadata:
  version: "0.1"
  display-name: "Mode, MAC, and AEAD Analysis"
  tags: "AEAD, MAC, mode-of-operation, nonce-misuse"
  requires: "construction-spec, primitive-assumptions, claim-model"
  produces: "composition-attack-records, bound-audit, misuse-matrix, test-plan"
---

# Mode, MAC, and AEAD Analysis

## Use this skill when

The target composes a block cipher, tweakable cipher, stream cipher, hash, or permutation into encryption, authentication, key wrap, storage, record protection, or AEAD. This skill emphasizes game/interface analysis and generic/algebraic attacks rather than only reduced-round primitive attacks.

## Operating procedure

1. **Specify the complete interface.** Key, nonce/IV, associated data, plaintext, ciphertext, tag, lengths, formatting, errors, state, rekeying, and decryption-before-verification behavior.
2. **Separate security goals.** Formalize confidentiality and authenticity independently and jointly. State nonce-respecting, nonce-misuse, deterministic, online, robust/committing, single/multi-user, and chosen-ciphertext properties actually claimed.
3. **Map primitive assumptions and reductions.** Identify PRP/PRF/tweakable-PRP/hash/permutation assumptions, reduction terms, query/length limits, birthday terms, tag terms, and proof gaps caused by real encodings or variable lengths.
4. **Build a misuse matrix.** Analyze nonce collision, accidental reuse, adversarial reuse, predictable IV, counter reset, truncation, rollback/replay, key/nonce domain collision, state loss, reordering, and cross-protocol/key reuse. State expected confidentiality and integrity degradation for each.
5. **Audit authentication algebra.** For polynomial/universal hashing, counters, or linear tags, derive collision/forgery equations, nonce-reuse effects, tag truncation, verification attempts, and multi-user aggregation.
6. **Audit formatting/domain separation.** Check injectivity, length encoding, padding, component tags, associated-data/message boundaries, key roles, empty inputs, streaming chunks, and finalization. Search for ambiguous transcripts and cross-domain collisions.
7. **Audit decryption behavior.** Verify that unauthenticated plaintext is not released or acted on, errors do not create useful oracles, partial records are handled consistently, and state updates occur only after successful verification.
8. **Connect primitive attacks carefully.** Use `symmetric-attack-transfer-and-adaptation` to determine whether a primitive distinguisher/recovery attack changes the construction claim or only the proof assumption.
9. **Test boundaries and misuse.** Generate differential/mutation tests for encodings, nonce sequences, lengths, tag failures, replays, truncation, empty fields, maximum inputs, and cross-implementation behavior.
10. **Audit concrete bounds.** Substitute actual message counts, lengths, users, tag size, nonce distribution, rekey cadence, and primitive security into the bound; compare with operational limits.

## Output contract

Provide:

- complete interface and security-game rows;
- primitive/reduction assumption map;
- nonce/misuse behavior matrix;
- authentication/tag/encoding analysis;
- multi-user and concrete bound calculations;
- decryption/error/state-machine findings;
- test vectors and negative/misuse tests;
- exact claim violations, proof limitations, and operational mitigations.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `BN00`
- `RS06-SIV`
- `NIST-38D`
- `NIST-MODES`
- `ROG02-AEAD`
- `RFC8452`
- `LR88`
- `LRW02-TBC`

Full records are bundled in `references/REFERENCES.md`.
