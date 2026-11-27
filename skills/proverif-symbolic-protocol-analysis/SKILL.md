---
name: proverif-symbolic-protocol-analysis
description: "Uses ProVerif’s Horn-clause abstraction and applied pi calculus to analyze secrecy, correspondence/authentication, reachability, and equivalence properties with high automation."
metadata:
  version: "0.1.0"
  display-name: "ProVerif Symbolic Protocol Analysis"
  category: "protocol-verification"
  tags: "proverif, protocol, symbolic, applied-pi"
  requires: "protocol process, cryptographic equations/reductions, security queries"
  produces: "ProVerif model, proof result or reconstructed trace, abstraction audit, replay package"
  optional: "true"
  namespace: "formal"
---

# ProVerif Symbolic Protocol Analysis

## Purpose

Uses ProVerif’s Horn-clause abstraction and applied pi calculus to analyze secrecy, correspondence/authentication, reachability, and equivalence properties with high automation.

## Use this skill when

Use this skill when rapid, highly automated symbolic analysis is valuable and the protocol maps naturally to ProVerif processes, channels, tables, events, and supported equations.

## Do not invoke automatically

Do not treat “cannot prove” as an attack or every abstract attack as executable. Avoid using ProVerif for properties whose state, algebra, probability, or temporal structure is distorted by the abstraction without additional validation.

## Optional entry contract

**Inputs**
- protocol process
- cryptographic equations/reductions
- security queries

**Expected products**
- ProVerif model
- proof result or reconstructed trace
- abstraction audit
- replay package

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Pin ProVerif and freeze the protocol, parser/encoding assumptions, state, roles, compromise powers, channels, and cryptographic constructors.
2. Encode honest processes, replication/session structure, names, tables, events, phases, and destructors. Preserve error and validation branches that affect adversarial behavior.
3. Define secrecy, correspondence, injective agreement, strong secrecy, or equivalence queries with explicit scope and event ordering.
4. Check basic reachability and honest execution before interpreting proofs. Add events and queries that expose dead code or impossible antecedents.
5. Run ProVerif and inspect proof explanations, generated traces, and abstraction warnings. Determine whether a reported attack is real, spurious, or requires a model change.
6. Reconstruct candidate attacks concretely against the protocol specification or implementation. For proofs, inspect equations, private functions, tables, and barriers that may hide behavior.
7. Compare with Tamarin or a bounded executable model for high-value stateful/temporal claims when the abstraction is difficult to audit.
8. Replay in a pinned environment and publish the process model, queries, result class, abstraction limitations, and symbolic scope.

## Output contract

- A ProVerif process/model and exact query set.
- Proof reports or concretely validated attack traces.
- Abstraction, reachability, and vacuity audit.
- Reproducible tool/version manifest.

## Non-negotiable guardrails

- ProVerif over-approximation can produce false attacks and nontermination; classify results correctly.
- Symbolic primitives hide bit-level and probabilistic weaknesses by design.
- Parser, length, canonicality, and implementation behavior must be modeled if relevant.
- Do not strengthen the model by declaring adversary-visible operations private.

## Related formal skills

- `tamarin-symbolic-protocol-analysis`
- `squirrel-computational-and-pq-protocol-proof`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **PROVERIF-HOME** — [ProVerif](https://bblanche.gitlabpages.inria.fr/proverif/) (2026) — Bruno Blanchet and contributors. `official-project`.
- **PROVERIF22** — [Automatic Verification of Security Protocols in the Symbolic Model: the Verifier ProVerif](https://doi.org/10.1561/3300000004) (2022) — Bruno Blanchet. `research-monograph`.

Bundled source metadata is in `references/REFERENCES.md`.
