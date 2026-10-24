---
name: public-key-attack-transfer-and-adaptation
description: "Decomposes an attack from literature or prior agent work, maps every indispensable requirement to a new public-key target, and develops minimally modified falsifiable adaptations. Use for cross-version, cross-parameter, cross-family, reduced-to-full, component-to-construction, and toy-to-real transfer."
metadata:
  version: "0.1"
  display-name: "Attack Transfer and Adaptation"
  tags: "attack-transfer, adaptation, requirements, cross-scheme"
  requires: "normalized-attack-record, target-structure-map, target-model"
  produces: "transfer-matrix, adapted-attack-records, decisive-tests"
---

# Attack Transfer and Adaptation

## Use this skill when

A known or agent-discovered attack may apply to another scheme, version, parameter set, component, or adversary model.

## Research maturity

Use [the mathematical research workflow](../crypto-investigate/reference/mathematical-research-workflow.md)
for proposals and incomplete arguments. Requirements for a ready experiment or
an established result do not determine which open mathematical questions may be
included in a proposal. Preserve unchecked premises, conditional implications,
and supporting lemmas without calling them validated results. Keep work status,
evidence maturity, review outcome, coverage, and contribution distinct.

## Operating procedure

1. Require a normalized source attack. Refuse to transfer from a headline, family resemblance, or complexity exponent without the attack skeleton and prerequisites.
2. Identify the source attack invariants: algebraic relation, secret distribution, oracle response, failure event, validation omission, subspace, code structure, lattice embedding, transcript property, or graph/path information that actually creates leverage.
3. Map source and target algorithms, algebraic domains, key/ciphertext/signature formats, distributions, transformations, and protocol boundaries. Mark mappings as exact, approximate, many-to-one, or absent.
4. Build the transfer matrix. For every indispensable requirement record source evidence, target analogue, status (preserved, modified, absent, unknown), consequence, and smallest decisive test.
5. Check model feasibility independently from mathematics. Verify that required chosen inputs, malformed keys, decapsulation outcomes, signature queries, related keys, quantum oracles, or session reveals exist in the target claim.
6. Re-derive probabilities, dimensions, ranks, noise/failure distributions, subgroup orders, transcript counts, and complexity. Never carry over source exponents or estimator outputs unchanged.
7. Modify one failed condition at a time: alter the embedding, decoding target, lattice attack, cut, guessed coordinates, oracle statistic, transcript relation, or protocol placement. Create a separate attack record for materially different adaptations.
8. Check boundary elevation: underlying-problem to scheme, component to transform, distinguisher to recovery, reduced parameter to standardized parameter, or active oracle to passive model. Account for every added step and verification cost.
9. Classify transfer as exact, conservative, speculative, failed, or not applicable. Preserve failed transfer branches as reusable negative evidence.
10. Design the smallest decisive target-specific experiment or proof before undertaking a large computation.

## Output contract

- A completed transfer matrix.
- One adapted attack record per materially different hypothesis.
- Target-specific derivations and recomputed resource estimates.
- Ranked decisive tests and a transfer classification.

## Non-negotiable guardrails

- Bind every conclusion to the exact artifact, version, parameter set, key format, and security game.
- Distinguish a faster algorithm for an underlying mathematical problem from a complete attack on the cryptosystem, and distinguish a proof gap from an exploit.
- Never present a weak-key, malformed-input, related-key, multi-target, decryption-oracle, leakage, fault, or quantum result as a standard-model full-scheme break without that qualification.
- For a new or independently verified quantitative conclusion, account for the relevant data, oracle queries, arithmetic/bit operations, memory, preprocessing, communication, verification, parallel depth, and success probability in explicit units. Preserve attributed published quantities as source claims; reuse unchanged checked inputs and recompute affected dependencies.
- State the cost model, implementation assumptions, and estimator version; a single headline exponent is not a reproducible security estimate.
- Preserve failed attacks, rebuttals, corrections, withdrawn claims, and source-version chronology in the evidence ledger.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not established by a proof, derivation, experiment, validated implementation, or cited source.
- A break of SIDH, Rainbow, a weak NTRU parameter set, or a reduced-round proof system does not transfer to an adjacent family merely because some algebraic vocabulary is shared.

## Associated references

- `COP96-SMALLROOTS`
- `LIMLEE97-SUBGROUP`
- `ABD16-SUBFIELD`
- `DANVERS21-MTFAIL`
- `BEULLENS20-UOV`
- `CD22-SIDH`
- `KLS18-FSQROM`

Full records are bundled in `references/REFERENCES.md`.
