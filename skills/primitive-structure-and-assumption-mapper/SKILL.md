---
name: primitive-structure-and-assumption-mapper
description: "Map the exact structure and assumptions of a symmetric primitive or construction to expose attack-relevant dependencies before choosing techniques or encoding a search. Use first on a symmetric target; for public-key schemes use scheme-structure-and-assumption-mapper."
metadata:
  version: "0.1"
  display-name: "Primitive Structure and Assumption Mapper"
  tags: "structure, specification, assumptions, attack-surface"
  requires: "specification, reference-code, security-claims"
  produces: "design-assumption-graph, round-map, dependency-table, attack-surface-map"
---

# Primitive Structure and Assumption Mapper

## Use this skill when

Before selecting attack techniques, transferring a published attack, or encoding a search model. It prevents analysis of an idealized cipher that differs from the specified or implemented object.

## Operating procedure

1. **Freeze the target.** Record specification version/date, parameter set, code commit, endianness, indexing, padding/encoding, and any implementation-defined behavior.
2. **Describe interfaces and domains.** List key, plaintext/message, nonce/IV, tweak, associated data, tag, output lengths, state widths, and legal/illegal input relationships.
3. **Draw the computation graph.** Represent initialization, key schedule, per-round state update, feedforward, finalization, extraction, and verification as directed operations with exact bit ranges.
4. **Annotate operations.** For each operation record algebraic domain and properties relevant to attack transfer: XOR, modular addition/subtraction, rotation, S-box, finite-field multiplication, permutation, linear diffusion, truncation, table lookup, conditional, constant addition, and key/tweak injection.
5. **Map state geometry.** Give word/bit ordering, lanes/branches, branch number or diffusion metrics if established, active-component propagation, and round boundaries used in the literature.
6. **Map key/tweak schedules.** Record master-key mapping, round-key dependencies, linear/nonlinear recurrences, equivalent keys, repeated subkeys, related-tweak behavior, and where independent-round-key assumptions would be false.
7. **Map constants and symmetry breakers.** Identify round constants, domain separators, frame bits, position encodings, counters, and asymmetric operations. Note which potential slides, rotations, invariants, or related-key relations they prevent—and which they do not.
8. **State assumptions as graph nodes.** Examples: ideal block cipher, random permutation, Markov/independence approximation, independent round keys, uniformly random differences, absence of weak keys, nonce uniqueness, capacity secrecy, or random-oracle modeling.
9. **Cross-check specification and code.** Compare formulas, loop bounds, indexing, encodings, test vectors, and intermediate values. Record discrepancies separately from cryptanalytic properties.
10. **Generate an attack-surface map.** For each structural feature list plausible technique families, required conditions, and likely blockers. Rank by structural fit rather than novelty.

## Output contract

Produce a design/assumption graph containing:

- exact operations and state slices;
- round/phase boundaries;
- key/tweak/nonce dependencies;
- constants and domain separation;
- claimed diffusion/nonlinearity metrics and their evidence;
- assumptions, where each is used, and whether it is proved, measured, or heuristic;
- specification/code discrepancies;
- technique-to-feature attack-surface table.

All later solver models and transfer matrices must reference graph node IDs so a changed interpretation can invalidate dependent results automatically.

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
- `LMM91-MARKOV`
- `DR02-RIJNDAEL`
- `LR88`
- `NIST-MODES`
- `BDPV08-SPONGE`

Full records are bundled in `references/REFERENCES.md`.
