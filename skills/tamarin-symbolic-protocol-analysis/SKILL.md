---
name: tamarin-symbolic-protocol-analysis
description: "Models stateful cryptographic protocols with multiset rewriting, equational theories, trace properties, observational equivalence, and symbolic adversaries, producing proof scripts or attack traces."
metadata:
  version: "0.1.0"
  display-name: "Tamarin Symbolic Protocol Analysis"
  category: "protocol-verification"
  tags: "tamarin, protocol, symbolic, multiset-rewriting"
  requires: "protocol specification, roles and state, security properties and equational theory"
  produces: "Tamarin theory, proof or attack trace, model assumptions, replay bundle"
  optional: "true"
  namespace: "formal"
---

# Tamarin Symbolic Protocol Analysis

## Purpose

Models stateful cryptographic protocols with multiset rewriting, equational theories, trace properties, observational equivalence, and symbolic adversaries, producing proof scripts or attack traces.

## Use this skill when

Use this skill when unbounded sessions, mutable state, compromise/reveal events, complex equational theories, or trace-based authentication/secrecy properties make Tamarin a strong fit.

## Do not invoke automatically

Do not present a symbolic proof as a concrete computational bound or an implementation proof. Do not force probabilistic leakage, finite-precision behavior, or algorithmic cryptanalysis into a Dolev–Yao model that abstracts away the decisive structure.

## Optional entry contract

**Inputs**
- protocol specification
- roles and state
- security properties and equational theory

**Expected products**
- Tamarin theory
- proof or attack trace
- model assumptions
- replay bundle

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Freeze the protocol version, message formats, cryptographic constructors, state, roles, channels, compromise model, and intended deployment assumptions.
2. Define multiset-rewriting rules for every transition, including generation, storage, retries, errors, corruption, reveal, revocation, and concurrency. Keep persistent and linear facts distinct.
3. Specify equations only for algebraic identities intentionally available to the adversary. Check convergence/variant assumptions and avoid equations that over- or under-approximate the primitive accidentally.
4. Write executability and sanity lemmas before security lemmas. Use `exists-trace`/cover-style checks to ensure honest runs and critical branches are reachable.
5. Formalize secrecy, authentication, agreement, freshness, forward secrecy, post-compromise properties, accountability, or equivalence with exact quantification and temporal ordering.
6. Run automated proof search, inspect generated cases, and guide difficult proofs with source lemmas/restrictions while preserving their soundness conditions.
7. For counterexamples, minimize and narrate the attack trace and map every symbolic action to a concrete protocol/API capability.
8. For proofs, audit restrictions, case splits, oracles, lemmas, and unfinished branches. Replay from a pinned Tamarin/Maude environment.
9. Publish the symbolic model, property, result, equational theory, compromise scope, and computational/implementation non-claims.

## Output contract

- A complete Tamarin theory and pinned replay environment.
- Checked trace/equivalence proof or minimized attack trace.
- Executability/vacuity tests and assumption report.
- A mapping between symbolic events and the target protocol artifacts.

## Non-negotiable guardrails

- Unbounded symbolic sessions do not imply computational soundness for arbitrary primitives.
- An omitted state transition or parser rule can invalidate the model while all lemmas remain proved.
- Restrictions and helper lemmas must not encode the desired security conclusion.
- Attack traces must be checked for realizability in the actual interface.

## Related formal skills

- `proverif-symbolic-protocol-analysis`
- `cryptoverif-computational-protocol-analysis`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **TAMARIN-HOME** — [Tamarin Prover](https://tamarin-prover.com/) (2026) — Tamarin project. `official-project`.
- **TAMARIN-MANUAL** — [Tamarin Prover Manual](https://tamarin-prover.com/manual/master/book/001_introduction.html) (2026) — Tamarin project. `official-manual`.
- **TAMARIN-REPO** — [Tamarin repository](https://github.com/tamarin-prover/tamarin-prover) (2026) — Tamarin project. `official-repository`.

Bundled source metadata is in `references/REFERENCES.md`.
