---
name: formal-claim-and-model-authoring
description: "Turns an informal cryptographic or cryptanalytic statement into a typed, version-bound formal target with explicit domains, quantifiers, adversary powers, assumptions, and non-claims."
metadata:
  version: "0.1.0"
  display-name: "Formal Claim and Model Authoring"
  category: "control"
  tags: "claim-modeling, specification, quantifiers, assumptions"
  requires: "informal claim, exact target artifacts, security or attack context"
  produces: "formalization charter, candidate theorem or game, model dictionary, assumption and non-claim lists"
  optional: "true"
  namespace: "formal"
---

# Formal Claim and Model Authoring

## Purpose

Turns an informal cryptographic or cryptanalytic statement into a typed, version-bound formal target with explicit domains, quantifiers, adversary powers, assumptions, and non-claims.

## Use this skill when

Use this skill before proving any nontrivial claim. It is the bridge from a paper, standard, implementation finding, or agent hypothesis to a theorem statement, game, transition system, or finite constraint problem.

## Do not invoke automatically

Do not start by transcribing the desired conclusion into prover syntax. First determine whether the claim concerns the published algorithm, an implementation, a mathematical abstraction, an encoded search domain, or a probabilistic/heuristic model.

## Optional entry contract

**Inputs**
- informal claim
- exact target artifacts
- security or attack context

**Expected products**
- formalization charter
- candidate theorem or game
- model dictionary
- assumption and non-claim lists

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Freeze the target artifacts: specification revision, source commit, parameter set, build configuration, test-vector version, proof source, and any errata. Assign stable identifiers and hashes where possible.
2. Normalize the result type. Separate “there exists a trail,” “this witness is valid,” “all executions satisfy an invariant,” “no object in domain D has cost below B,” “construction C reduces to assumption A,” and “implementation I refines specification S.”
3. Write every domain and quantifier explicitly. Include input lengths, canonical encodings, key distributions, randomness, oracle/session limits, round counts, malformed inputs, failure events, and resource bounds.
4. Define equality and arithmetic semantics. State whether values are integers, residues, bit vectors, field elements, polynomials, distributions, floating-point values, observationally equivalent programs, or protocol traces.
5. Separate definitions derived independently from normative sources from models extracted from code. If both are needed, give them different names and plan a correspondence theorem.
6. Type assumptions by category: mathematical axioms, cryptographic hardness, idealized models, statistical approximations, numerical conditions, extraction/compiler assumptions, environment behavior, and caller preconditions.
7. Write non-claims with the same care as claims. Examples include constant time, compiler correctness, physical leakage, quantum security, average-case prevalence, or full-round applicability.
8. Construct tiny examples and boundary cases that distinguish plausible alternative interpretations. Use them to validate the model before proof work.
9. Produce a human-readable statement and a machine-oriented manifest. Ensure they are linked so changes to the prose claim invalidate the formal target rather than drifting silently.

## Output contract

- A formalization charter using the shared template.
- A precise theorem/game/constraint target with named definitions and source locators.
- A model dictionary for every type, operation, distribution, oracle, and failure value.
- Explicit assumptions, preconditions, non-claims, examples, and ambiguity decisions.

## Non-negotiable guardrails

- A theorem can be perfectly checked and still formalize the wrong claim; specification adequacy remains a review obligation.
- Never hide a domain restriction inside helper definitions or notation.
- Do not model floating-point or machine arithmetic as real or unbounded integer arithmetic without a proved abstraction.
- Do not infer protocol or computational security from a purely functional-correctness model.

## Related formal skills

- `specification-validation-and-vacuity-audit`
- `normative-specification-to-executable-model`

## Related cryptanalysis skills in this pack (optional)

- `public-key-security-model-and-claim-formalizer`
- `security-model-and-claim-formalizer`

## Associated primary references

- **LEAN-REF** — [Lean Language Reference](https://lean-lang.org/doc/reference/latest/) (2026) — Lean project. `official-manual`.
- **EASYCRYPT-TUTORIALS** — [EasyCrypt tutorials](https://easycrypt.gitlab.io/easycrypt-web/docs/tutorials/) (2026) — EasyCrypt project. `official-manual`.
- **CRYPTHOL-GAMES** — [Game-Based Cryptography in HOL](https://isa-afp.org/entries/Game_Based_Crypto.html) (2026) — CryptHOL contributors. `formal-development`.
- **TAMARIN-MANUAL** — [Tamarin Prover Manual](https://tamarin-prover.com/manual/master/book/001_introduction.html) (2026) — Tamarin project. `official-manual`.
- **IEEE754** — [IEEE Standard for Floating-Point Arithmetic](https://standards.ieee.org/ieee/754/6210/) (2019) — IEEE. `standard`.

Bundled source metadata is in `references/REFERENCES.md`.
