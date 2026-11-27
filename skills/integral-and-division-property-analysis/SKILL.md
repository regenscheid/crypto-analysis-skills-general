---
name: integral-and-division-property-analysis
description: "Find and verify integral properties of symmetric primitives with structured sets, algebraic degree and division properties, and extend them to key recovery. Use when controllable input sets or bounded degree growth may give balanced or predictable sums."
metadata:
  version: "0.1"
  display-name: "Integral and Division-Property Analysis"
  tags: "integral, division-property, higher-order, algebraic-degree"
  requires: "design-assumption-graph, claim-model, round-scope"
  produces: "integral-records, division-model, data-structures, extension-plan"
---

# Integral and Division-Property Analysis

## Use this skill when

The primitive has byte/word/bit structure, controllable input sets, bounded algebraic-degree growth, or diffusion patterns that may produce balanced, constant, or otherwise predictable aggregates.

## Operating procedure

1. **Define the input multiset.** Specify active, constant, balanced, all, unknown, repeated, or affine-subspace coordinates and multiplicities. State whether data are chosen plaintexts, nonces, tweaks, states, or messages.
2. **Define the observed aggregate.** XOR sum, modular sum, parity, monomial sum, multiset equality, or another exact statistic. Avoid using “balanced” without naming the algebra and coordinate.
3. **Analyze direct integrals.** Propagate structured sets through rounds, track cancellations and bijective mappings, and verify with exhaustive reduced examples.
4. **Analyze algebraic degree.** Bound or compute degree growth, including key/constant variables and initialization/finalization. Translate higher-order derivatives into exact data and output predictions.
5. **Build a division-property model.** Choose word-based, bit-based, or generalized division property. Encode S-box/Boolean/linear/addition transitions with justified soundness. State whether the model is exact or over-approximating.
6. **Validate the model.** Exhaustively compare possible monomials/properties for small components and rounds. Directly test solver witnesses and known distinguishers.
7. **Optimize data complexity.** Count the full structured set, repeated structures, partial sums, and feasibility under the target interface/codebook.
8. **Extend to key recovery.** Add rounds, identify partial decryptions and guessed subkeys, derive zero/nonzero tests, false positives, candidate counts, and verification.
9. **Account for key dependence and cancellations.** Determine whether the property holds for all keys, most keys, or only in expectation. Test multiple keys and avoid assuming independent output coordinates.
10. **Compare with alternative explanations.** Check whether a found property is simply a lower-order differential, invariant subspace, or generic full-codebook effect.

## Output contract

Provide:

- exact input multiset and output aggregate;
- direct, degree-based, or division-property derivation;
- model soundness/completeness evidence;
- round and key-schedule scope;
- exact data structures and codebook feasibility;
- recovery extension and filtering statistics;
- exhaustive/statistical validation;
- complete resources and claim impact.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `DKR97-SQUARE`
- `KW02-INTEGRAL`
- `TODO15-DIVPROP`
- `XZR16-BITDIV`
- `GD21-BITDIV`
- `KNU95-TRUNC`

Full records are bundled in `references/REFERENCES.md`.
