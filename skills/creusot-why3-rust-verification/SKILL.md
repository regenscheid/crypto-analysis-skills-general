---
name: creusot-why3-rust-verification
description: "Verifies Rust through Creusot and Why3 using source annotations, verification conditions, multiple automated provers, and interactive proof when needed."
metadata:
  version: "0.1.0"
  display-name: "Creusot/Why3 Rust Verification"
  category: "implementation-verification"
  tags: "creusot, why3, rust, deductive-verification"
  requires: "annotated Rust target, Creusot/Why3 toolchain, formal contract"
  produces: "verification conditions, checked contracts, prover configuration, replay package"
  optional: "true"
  namespace: "formal"
---

# Creusot/Why3 Rust Verification

## Purpose

Verifies Rust through Creusot and Why3 using source annotations, verification conditions, multiple automated provers, and interactive proof when needed.

## Use this skill when

Use this skill when deductive verification through Why3’s multi-prover ecosystem and Creusot’s Rust contracts fits the implementation and team better than Aeneas or Verus.

## Do not invoke automatically

Do not treat a green external prover result as self-explanatory. Record which prover discharged each verification condition, whether proof certificates are available, and what Creusot translation semantics are trusted.

## Optional entry contract

**Inputs**
- annotated Rust target
- Creusot/Why3 toolchain
- formal contract

**Expected products**
- verification conditions
- checked contracts
- prover configuration
- replay package

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Pin Creusot, Rust, Why3, every automated prover, and source dependencies. Register exact prover versions/configurations in Why3.
2. Specify preconditions, postconditions, variants, loop invariants, purity, framing, ownership, arithmetic semantics, and panic/overflow expectations in Creusot annotations.
3. Inspect generated WhyML/verification conditions for representative functions and confirm the translation captures Rust control flow, borrowing, and library operations.
4. Solve simple VCs with automation and isolate hard algebraic or quantified obligations into named lemmas. Use interactive provers only with reproducible proof artifacts.
5. Cross-check machine arithmetic and array bounds carefully; Why3 integer reasoning can diverge from Rust wrapping behavior unless encoded explicitly.
6. Audit trusted externals, opaque functions, axioms, and unsupported Rust features. Build verified wrappers or narrow the theorem rather than assuming behavior silently.
7. Validate against tests, vectors, and code mutations and ensure changed source regenerates the VCs.
8. Replay all VCs in an isolated environment and capture per-prover results, timeouts, and nondeterminism.
9. Publish the Creusot contracts, translated obligations, solver trust model, and limitations regarding compiler, leakage, and unverified libraries.

## Output contract

- Annotated Rust and generated Why3 obligations.
- Per-VC prover/check status and interactive proof artifacts.
- Translation, arithmetic, and external-function audit.
- Pinned clean replay configuration.

## Non-negotiable guardrails

- Do not let different provers discharge subtly different encodings without preserving the exact VC.
- Do not model wrapping arithmetic as mathematical integer arithmetic accidentally.
- External solver status is part of the trust story unless reconstructed.
- Unsupported library behavior must be isolated and specified.

## Related formal skills

- `verus-rust-verification`
- `smt-proof-production-and-reconstruction`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **CREUSOT-HOME** — [Creusot](https://creusot.rs/) (2026) — Creusot project. `official-project`.
- **CREUSOT-REPO** — [Creusot repository](https://github.com/creusot-rs/creusot) (2026) — Creusot project. `official-repository`.
- **CREUSOT22** — [Creusot: A Foundry for the Deductive Verification of Rust Programs](https://doi.org/10.1007/978-3-031-17244-1_6) (2022) — Xavier Denis et al.. `research-paper`.
- **WHY3-HOME** — [Why3](https://why3.org/) (2026) — Why3 project. `official-project`.

Bundled source metadata is in `references/REFERENCES.md`.
