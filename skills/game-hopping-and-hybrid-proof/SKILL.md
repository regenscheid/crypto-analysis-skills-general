---
name: game-hopping-and-hybrid-proof
description: "Constructs and verifies sequences of exact, computational, and statistical game transformations with explicit bad events, simulators, and accumulated loss."
metadata:
  version: "0.1.0"
  display-name: "Game Hopping and Hybrid Proof"
  category: "security-proofs"
  tags: "game-hopping, hybrid, bad-event, reduction"
  requires: "formal security games, candidate proof outline, assumptions"
  produces: "game sequence, verified hop lemmas, bad-event ledger, final bound"
  optional: "true"
  namespace: "formal"
---

# Game Hopping and Hybrid Proof

## Purpose

Constructs and verifies sequences of exact, computational, and statistical game transformations with explicit bad events, simulators, and accumulated loss.

## Use this skill when

Use this skill for computational security arguments whose proof proceeds by program transformations, oracle replacement, lazy sampling, hybrids, failure conditioning, or reductions to assumptions.

## Do not invoke automatically

Do not reproduce only the paper’s narrative hop names. Each transition must state the changed code, invariant, adversary view, justification, and quantitative effect.

## Optional entry contract

**Inputs**
- formal security games
- candidate proof outline
- assumptions

**Expected products**
- game sequence
- verified hop lemmas
- bad-event ledger
- final bound

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Lay out all games as executable modules/programs and diff adjacent games. Keep unchanged code syntactically aligned when possible so relational proofs focus on the real transformation.
2. Classify each hop as exact equivalence, one-sided implication, statistical distance, computational reduction, conditioning/up-to-bad, or arithmetic bound.
3. For exact hops, prove relational invariants over memories, oracle maps, counters, transcripts, and outputs. Include initialization and all adversary-controlled call paths.
4. For bad-event hops, define the event precisely, prove games agree until bad, and separately bound its probability under the correct game and conditioning.
5. For hybrids, define the indexed family and prove neighboring transitions uniformly. Account for the number of hybrids and whether adversary resources or state change.
6. For oracle replacement/programming, track domains, collisions, query timing, sampled maps, repeated queries, and consistency across modules.
7. For reduction hops, construct the reduction as executable adversarial code, map its runtime and queries, and prove the exact relationship between success probabilities.
8. Accumulate bounds symbolically before concrete instantiation. Check triangle inequalities, union bounds, guessing factors, and sign/direction of every term.
9. Compare the mechanized sequence to the source proof and record repaired, omitted, or newly required steps rather than silently diverging.

## Output contract

- Executable game definitions and adjacency map.
- One checked theorem per hop with classification and assumptions.
- A bad-event and loss ledger.
- A final symbolic and concrete advantage bound.

## Non-negotiable guardrails

- Do not use “identical until bad” without proving the view relation and event location.
- Do not assume independent random-oracle outputs when domains overlap or programming occurs.
- Do not omit the reduction’s own time, queries, aborts, and simulation failures.
- If a source proof step cannot be formalized, preserve it as an open obligation rather than replacing it with an axiom.

## Related formal skills

- `easycrypt-proof-development`
- `probabilistic-program-coupling-and-relational-reasoning`

## Related cryptanalysis skills in this pack (optional)

- `security-proof-rom-qrom-and-tightness-auditor`
- `security-proof-and-bound-auditor`

## Associated primary references

- **EASYCRYPT11** — [EasyCrypt: Automated Reasoning for Security Proofs](https://eprint.iacr.org/2011/101) (2011) — Gilles Barthe et al.. `research-paper`.
- **EASYCRYPT-TUTORIALS** — [EasyCrypt tutorials](https://easycrypt.gitlab.io/easycrypt-web/docs/tutorials/) (2026) — EasyCrypt project. `official-manual`.
- **SSPROVE21** — [SSProve: A Foundational Framework for Modular Cryptographic Proofs in Coq](https://eprint.iacr.org/2021/397) (2021) — Philipp G. Haselwarter et al.. `research-paper`.
- **CRYPTHOL** — [CryptHOL](https://isa-afp.org/entries/CryptHOL.html) (2026) — Andreas Lochbihler et al.. `formal-development`.
- **DILITHIUM-EC23** — [Fixing and Mechanizing the Security Proof of Fiat-Shamir with Aborts and Dilithium](https://eprint.iacr.org/2023/246) (2023) — Manuel Barbosa et al.. `research-paper`.
- **MLKEM-EC24** — [Formally verifying Kyber Episode V: Machine-checked IND-CCA security and correctness of ML-KEM in EasyCrypt](https://eprint.iacr.org/2024/843) (2024) — José Bacelar Almeida et al.. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
