---
name: symmetric-attack-transfer-and-adaptation
description: "Decomposes an attack from literature or prior agent work, maps each indispensable requirement to a new target, and develops minimally modified falsifiable adaptations. Use when: A known attack on one primitive, version, parameter set, round count, component, or adversary model might apply to another. Also use it to transfer an agent-discovered reduced or toy attack toward the real target."
metadata:
  version: "0.1"
  display-name: "Attack Transfer and Adaptation"
  tags: "attack-transfer, adaptation, hypothesis, requirements"
  requires: "normalized-attack-record, design-assumption-graph, target-model"
  produces: "transfer-matrix, adapted-attack-records, decisive-tests"
---

# Attack Transfer and Adaptation

## Use this skill when

A known attack on one primitive, version, parameter set, round count, component, or adversary model might apply to another. Also use it to transfer an agent-discovered reduced or toy attack toward the real target.

## Research maturity

Use [the mathematical research workflow](../crypto-investigate/reference/mathematical-research-workflow.md)
for proposals and incomplete arguments. Requirements for a ready experiment or
an established result do not determine which open mathematical questions may be
included in a proposal. Preserve unchecked premises, conditional implications,
and supporting lemmas without calling them validated results. Keep work status,
evidence maturity, review outcome, coverage, and contribution distinct.

## Operating procedure

1. **Start from a normalized source attack.** Refuse to transfer from a headline or analogy. Require the source attack skeleton, requirements, model, complexity, and validation status.
2. **Identify invariants of the attack.** Separate indispensable mathematical structure from source-specific notation and optimizations. Examples: a low-weight transition, a deterministic zero set, a key-schedule relation, repeated round function, matching degrees of freedom, a low-degree superpoly, or a period accessible in Q2.
3. **Map state and operations.** Align source and target states, round boundaries, nonlinear layers, linear diffusion, constants, key/tweak injection, initialization/finalization, and output filtering. State where the mapping is exact, many-to-one, approximate, or impossible.
4. **Build the transfer matrix.** For every indispensable requirement record source evidence, target analogue, status (`preserved`, `modified`, `absent`, or `unknown`), consequence, and smallest decisive test or proof obligation.
5. **Check model feasibility.** Verify that source plaintext/ciphertext/nonce/tweak/key relations and online/offline access are available in the target claim. Do not treat a stronger oracle as a harmless implementation detail.
6. **Re-derive probabilities and correlations.** Do not carry over source exponents. Recompute transition weights, clusters/hulls, dependencies, available degrees of freedom, filtering, and boundary effects under the target’s actual schedule and constants.
7. **Generate minimal adaptations.** Change one failed requirement at a time: move the cut, shorten/extend rounds, change difference domain, replace exact matching with probabilistic filtering, alter data structures, guess extra subkey bits, or exploit a target-specific symmetry.
8. **Classify transfer confidence.** `Exact` means all indispensable requirements are preserved and the attack is fully recomputed. `Conservative` means target changes can only weaken the claim and the bound reflects them. `Speculative` means a requirement or heuristic remains unvalidated.
9. **Design the smallest decisive test.** Prefer exhaustive toy instances, reduced rounds, direct transition enumeration, intermediate-state instrumentation, or a proof of impossibility before a large experiment.
10. **Update—not overwrite—the ledger.** Link adapted records to the source record, record failed branches, and retain target-specific blockers as reusable negative knowledge.

## Output contract

Produce:

- a completed transfer matrix using `assets/TRANSFER_MATRIX.md`;
- one adapted attack record per materially different hypothesis;
- target-specific derivations rather than copied source estimates;
- a ranked list of decisive tests with expected outcomes and falsification conditions;
- a conclusion of exact, conservative, speculative, failed, or not applicable.

A persuasive analogy is not evidence. The central deliverable is the requirement-by-requirement mapping.

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
- `LH94-DL`
- `WAG99-BOOM`
- `BW99-SLIDE`
- `MRST09-REBOUND`
- `BK03-RKA`
- `KLLN16`

Full records are bundled in `references/REFERENCES.md`.
