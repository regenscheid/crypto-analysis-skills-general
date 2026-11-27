---
name: public-key-security-model-and-claim-formalizer
description: "Turn informal public-key security statements into explicit PKE, KEM, signature, key-agreement, correctness, multi-user, ROM and quantum games. Use when a document says CCA secure, unforgeable, 128-bit or post-quantum secure without a full experiment; symmetric: security-model-and-claim-formalizer."
metadata:
  version: "0.1"
  display-name: "Public-Key Security Model and Claim Formalizer"
  tags: "security-model, definitions, games, pke, kem, signatures, ake"
  requires: "target-artifact, security-claims"
  produces: "claim-adversary-matrix, game-sketches, oracle-session-model, ambiguity-log"
---

# Public-Key Security Model and Claim Formalizer

## Use this skill when

A specification, paper, review, or implementation makes a security claim that must be tied to an exact game, oracle interface, success event, and resource budget.

## Operating procedure

1. Identify the exact object: deterministic or randomized PKE, KEM, DEM composition, signature, identification scheme, unauthenticated or authenticated key exchange, group signature, aggregate signature, or a lower-level hard problem.
2. Extract every claim verbatim and assign a stable claim ID with a source locator, version, parameter set, and any qualifiers.
3. For PKE, separate one-wayness, semantic security, IND-CPA, IND-CCA1, IND-CCA2, non-malleability, plaintext awareness, robustness, and key privacy. Specify message distributions and challenge restrictions.
4. For KEMs, define key indistinguishability, decapsulation-oracle exclusions, validity and rejection behavior, correctness/failure probability, contributory behavior, and whether the claim covers malicious public keys or ciphertexts.
5. For signatures, distinguish existential from strong unforgeability, chosen-message access, key substitution, multi-signatures/aggregation, stateful signing, deterministic versus randomized signing, and quantum signing/hash queries.
6. For key agreement, define sessions, matching conversations, peer identities, freshness, reveal and corruption queries, known-key security, forward secrecy, KCI, unknown-key share, reflection, key confirmation, and channel binding.
7. Write the adversary interface precisely: key-generation control, public-key registration, chosen messages/ciphertexts, decapsulation or validation results, corruptions, state reveals, resets, concurrency, and classical/Q1/Q2 oracle access.
8. Define the success event and advantage, including correctness failures, aborts, invalid encodings, false accepts, and whether a multi-user or multi-target union is included.
9. State resources in explicit units and list assumptions/non-goals. If two plausible interpretations exist, create two rows rather than silently choosing one.
10. Map every attack or proof statement to the exact claim row it affects; a hard-problem speedup may only change a baseline and not violate a construction game.

## Output contract

- A completed claim-adversary matrix.
- A game sketch or pseudocode experiment for each material claim.
- An oracle/session model and ambiguity log.
- A mapping from existing attack records and proofs to claim IDs.

## Non-negotiable guardrails

- Bind every conclusion to the exact artifact, version, parameter set, key format, and security game.
- Distinguish a faster algorithm for an underlying mathematical problem from a complete attack on the cryptosystem, and distinguish a proof gap from an exploit.
- Never present a weak-key, malformed-input, related-key, multi-target, decryption-oracle, leakage, fault, or quantum result as a standard-model full-scheme break without that qualification.
- For a new or independently verified quantitative conclusion, account for the relevant data, oracle queries, arithmetic/bit operations, memory, preprocessing, communication, verification, parallel depth, and success probability in explicit units. Preserve attributed published quantities as source claims; reuse unchanged checked inputs and recompute affected dependencies.
- State the cost model, implementation assumptions, and estimator version; a single headline exponent is not a reproducible security estimate.
- Preserve failed attacks, rebuttals, corrections, withdrawn claims, and source-version chronology in the evidence ledger.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not established by a proof, derivation, experiment, validated implementation, or cited source.
- Do not use “CCA secure” without identifying the exact decryption/decapsulation exclusion and treatment of invalid ciphertexts.
- Do not equate EUF-CMA, SUF-CMA, key-substitution resistance, and non-repudiation.
- Separate Q1 from Q2 and state whether signing, hash, group-operation, or public-key oracles are available in superposition.

## Associated references

- `GM84-PKE`
- `GMR88-SIG`
- `BDPR98-PKE`
- `CS98-CCA`
- `BR93-ROM`
- `BBM00-MULTIUSER`
- `BR93-AKE`
- `CK01-AKE`
- `ECK07`
- `NIST-SP800-227`

Full records are bundled in `references/REFERENCES.md`.
