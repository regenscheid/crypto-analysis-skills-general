---
name: probabilistic-program-coupling-and-relational-reasoning
description: "Uses couplings, relational invariants, probabilistic program logics, and distributional arguments to prove equivalence or distance bounds between cryptographic computations."
metadata:
  version: "0.1.0"
  display-name: "Probabilistic Program Coupling and Relational Reasoning"
  category: "security-proofs"
  tags: "coupling, relational-reasoning, probability, program-logic"
  requires: "two probabilistic programs or games, candidate relation, distribution assumptions"
  produces: "coupling or relational invariant, equivalence/distance theorem, side-condition proofs, counterexamples to invalid coupling"
  optional: "true"
  namespace: "formal"
---

# Probabilistic Program Coupling and Relational Reasoning

## Purpose

Uses couplings, relational invariants, probabilistic program logics, and distributional arguments to prove equivalence or distance bounds between cryptographic computations.

## Use this skill when

Use this skill when the core difficulty is showing that two probabilistic programs produce equal or close views despite different sampling order, internal state, rejection behavior, or oracle implementation.

## Do not invoke automatically

Do not assert a coupling because marginal distributions “look the same.” A valid coupling must preserve joint dependencies, adversary-visible state, and all conditioned events.

## Optional entry contract

**Inputs**
- two probabilistic programs or games
- candidate relation
- distribution assumptions

**Expected products**
- coupling or relational invariant
- equivalence/distance theorem
- side-condition proofs
- counterexamples to invalid coupling

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Define the two programs, initial-state relation, adversary interface, observations, and target relation over outputs and final memories.
2. Choose a coupling strategy: identity, bijective, maximal, rejection, product, shift, or custom joint distribution. State the construction explicitly.
3. Prove that each marginal of the joint distribution equals the corresponding program distribution and that the desired relation holds with the claimed probability.
4. For looped or stateful programs, define a relational invariant and variant/losslessness argument. Include oracle maps, counters, and adversary state.
5. Handle conditioning and failure events carefully. Check whether a coupling remains valid after rejection sampling, truncation, or adaptive queries.
6. Use EasyCrypt pRHL, SSProve, CryptHOL, or another logic according to available semantics. Keep tool-specific judgments connected to the plain mathematical coupling.
7. Quantify statistical distance or failure probability when exact coupling is impossible, and compose bounds with correct triangle/union arguments.
8. Test candidate couplings on small finite distributions and correlated examples. Search for counterexamples to independence or permutation assumptions.
9. Publish the coupling construction, marginal proofs, invariant, loss terms, and all side conditions as reusable lemmas.

## Output contract

- A precise relational specification and coupling construction.
- Marginal-correctness and relation/invariant proofs.
- Exact equivalence or quantitative distance theorem.
- Boundary cases showing why weaker informal arguments fail.

## Non-negotiable guardrails

- Equal marginals do not imply an arbitrary joint coupling has the required relation.
- Do not assume sampling order is irrelevant when later adaptive code observes state.
- Losslessness and termination are part of probabilistic equivalence.
- Keep computational assumptions separate from information-theoretic coupling steps.

## Related formal skills

- `game-hopping-and-hybrid-proof`
- `lean-probability-combinatorics-and-bounds`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **EASYCRYPT11** — [EasyCrypt: Automated Reasoning for Security Proofs](https://eprint.iacr.org/2011/101) (2011) — Gilles Barthe et al.. `research-paper`.
- **SSPROVE21** — [SSProve: A Foundational Framework for Modular Cryptographic Proofs in Coq](https://eprint.iacr.org/2021/397) (2021) — Philipp G. Haselwarter et al.. `research-paper`.
- **CRYPTHOL** — [CryptHOL](https://isa-afp.org/entries/CryptHOL.html) (2026) — Andreas Lochbihler et al.. `formal-development`.
- **EASYCRYPT-TUTORIALS** — [EasyCrypt tutorials](https://easycrypt.gitlab.io/easycrypt-web/docs/tutorials/) (2026) — EasyCrypt project. `official-manual`.

Bundled source metadata is in `references/REFERENCES.md`.
