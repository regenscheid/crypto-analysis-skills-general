---
name: related-key-and-tweakey-analysis
description: "Formalize realistic key and tweak relations, propagate them through schedules, and evaluate related-key and tweakey differentials, symmetries and key recovery. Use when the schedule diffuses weakly or an attack assumes related keys; also judges whether that model fits the interface."
metadata:
  version: "0.1"
  display-name: "Related-Key and Tweakey Analysis"
  tags: "related-key, tweakey, key-schedule, RKA"
  requires: "design-assumption-graph, claim-model, relation-class"
  produces: "relation-model, related-key-attack-records, feasibility-assessment"
---

# Related-Key and Tweakey Analysis

## Use this skill when

The key/tweak schedule has low diffusion, linear recurrences, repeated subkeys, symmetries, or a literature attack assumes chosen related keys or tweaks. Also use it to determine whether such a model is meaningful for the intended interface.

## Operating procedure

1. **Define the relation class.** Give explicit functions mapping a base key/tweak to related values. State whether relations are chosen by the adversary, fixed by a protocol, induced by derivation, accidental, or only analytical.
2. **Formalize the RKA game.** Specify oracle access, restrictions preventing trivial key collisions, adaptivity, number of base keys/users, and whether encryption/decryption or Q2 access is allowed.
3. **Propagate relations through the schedule.** Derive exact round-key/tweak differences or algebraic relations, including constants, nonlinear schedule components, rotations, word permutations, and equivalent-key behavior.
4. **Find compatible state relations.** Search related-key differentials, boomerangs, slides, rotational/RX relations, invariant subspaces, or cancellation patterns jointly across data and key schedules.
5. **Classify key scope.** Determine whether the result holds for all keys, a weak-key class, related pairs of a given density, or only an idealized independent-round-key model. Quantify the fraction.
6. **Check real-world attainability.** Identify whether the construction/API/protocol actually lets an adversary instantiate the relation or observe multiple derived keys. Keep theoretical schedule weaknesses distinct from advertised-model violations.
7. **Extend and recover.** Derive required related-key queries, partial subkey guesses, filters, candidate reconstruction, and verification under the relation constraints.
8. **Test schedule and state jointly.** Use multiple base keys and related families; instrument round keys and state differences; include random unrelated-key controls.
9. **Audit generic comparisons.** Compare against generic RKA baselines for the defined relation class, not only single-key exhaustive search.
10. **Report defensive relevance.** Explain whether domain-separated KDFs, independent keys, constants, or interface restrictions eliminate the model—and whether those are normative requirements.

## Output contract

Provide:

- exact relation class and security game;
- schedule propagation derivation;
- compatible state property/attack;
- all-key versus weak-key scope and density;
- interface/protocol attainability;
- data/time/memory/success and verification;
- experiments across related and random controls;
- exact relation to advertised claims.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `BIH94-RK`
- `BK03-RKA`
- `SHW14-AUTO`
- `KN10-ROT`
- `BW99-SLIDE`

Full records are bundled in `references/REFERENCES.md`.
