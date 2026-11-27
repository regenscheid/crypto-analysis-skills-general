---
name: cryptoverif-computational-protocol-analysis
description: "Constructs and checks computational protocol-security proofs through automatically or interactively generated game transformations and explicit probability bounds."
metadata:
  version: "0.1.0"
  display-name: "CryptoVerif Computational Protocol Analysis"
  category: "protocol-verification"
  tags: "cryptoverif, protocol, computational, game-hopping"
  requires: "protocol model, cryptographic assumptions, security query and parameter bounds"
  produces: "CryptoVerif proof, game sequence, concrete probability bound, replay package"
  optional: "true"
  namespace: "formal"
---

# CryptoVerif Computational Protocol Analysis

## Purpose

Constructs and checks computational protocol-security proofs through automatically or interactively generated game transformations and explicit probability bounds.

## Use this skill when

Use this skill when a protocol property needs a computational rather than purely symbolic guarantee and CryptoVerif can model the primitives, replication, oracles, and events involved.

## Do not invoke automatically

Do not use CryptoVerif as a black-box source of a theorem without inspecting the generated games, assumptions, transformations, and bound. It does not replace implementation-refinement or leakage analysis.

## Optional entry contract

**Inputs**
- protocol model
- cryptographic assumptions
- security query and parameter bounds

**Expected products**
- CryptoVerif proof
- game sequence
- concrete probability bound
- replay package

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Pin CryptoVerif and freeze the protocol/version, message encodings, roles, replications, keys, channels, corruption model, and target query.
2. Encode cryptographic primitives with the exact assumptions supported by the intended algorithms, including key generation, randomness, collision conditions, and domains.
3. Validate the initial process against honest executions and implementation/specification behavior, particularly parsing, canonical encodings, failure/rejection, and state updates.
4. Run proof search or guide transformations. Preserve the complete sequence of games and classify each hop as syntactic, probabilistic, assumption-based, or conditioned on a bad event.
5. Recompute concrete loss terms, query counts, replication/multi-user factors, collision probabilities, failure events, and runtime of reductions.
6. Inspect generated freshness/independence facts and oracle transformations for hidden assumptions. Check whether implementation domain separation and key reuse match the model.
7. If CryptoVerif cannot prove the query, analyze whether the cause is tool incompleteness, a missing assumption, model error, or a real attack; validate any attack externally.
8. Replay from pinned sources and publish games, assumptions, bounds, result scope, and non-claims.

## Output contract

- A CryptoVerif model and exact computational query.
- Complete game/transformation sequence and assumption map.
- Recomputed concrete bound and resource accounting.
- Pinned proof replay and implementation-model crosswalk.

## Non-negotiable guardrails

- Automatic transformations remain subject to the correctness of the initial model and declared assumptions.
- Do not suppress failure or parsing behavior that could invalidate a hop.
- Asymptotic security does not imply an adequate concrete bound.
- A computational protocol proof is not automatically QROM/PQ sound or an implementation theorem.

## Related formal skills

- `game-hopping-and-hybrid-proof`
- `squirrel-computational-and-pq-protocol-proof`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **CRYPTOVERIF-HOME** — [CryptoVerif](https://bblanche.gitlabpages.inria.fr/cryptoverif/) (2026) — Bruno Blanchet. `official-project`.
- **CRYPTOVERIF-MANUAL** — [CryptoVerif Manual](https://bblanche.gitlabpages.inria.fr/cryptoverif/manual.pdf) (2025) — Bruno Blanchet. `official-manual`.
- **EASYCRYPT11** — [EasyCrypt: Automated Reasoning for Security Proofs](https://eprint.iacr.org/2011/101) (2011) — Gilles Barthe et al.. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
