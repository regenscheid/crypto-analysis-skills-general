---
name: symcrypt-verified-crypto-workflow
description: "Applies the standards-to-executable-Lean-to-Aeneas-Rust methodology demonstrated by Microsoft’s verified SymCrypt work, including property tests, proof agents, and explicit trust reporting."
metadata:
  version: "0.1.0"
  display-name: "SymCrypt Verified-Crypto Workflow"
  category: "implementation-verification"
  tags: "symcrypt, lean, aeneas, rust, verified-crypto"
  requires: "cryptographic standard, Rust implementation, test vectors and proof target"
  produces: "standard-derived Lean spec, Aeneas code model, refinement and panic-freedom proofs, dashboard-style assurance report"
  optional: "true"
  namespace: "formal"
---

# SymCrypt Verified-Crypto Workflow

## Purpose

Applies the standards-to-executable-Lean-to-Aeneas-Rust methodology demonstrated by Microsoft’s verified SymCrypt work, including property tests, proof agents, and explicit trust reporting.

## Use this skill when

Use this skill when designing or reproducing the verified-crypto workflow for SymCrypt code or another Rust cryptographic library with similar standards-to-code requirements.

## Do not invoke automatically

Do not infer that SymCrypt itself is a theorem prover or that all algorithms in the library carry the same verification guarantees. Bind claims to the exact verified branch, function, theorem, and build.

## Optional entry contract

**Inputs**
- cryptographic standard
- Rust implementation
- test vectors and proof target

**Expected products**
- standard-derived Lean spec
- Aeneas code model
- refinement and panic-freedom proofs
- dashboard-style assurance report

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Freeze the standard revision, SymCrypt source branch/commit, Rust wrapper or implementation, Lean/Aeneas toolchain, parameter sets, and official vectors.
2. Independently transcribe the standard into an executable Lean specification and derive high-level mathematical properties. Keep specification authorship separate from code extraction.
3. Run vectors and randomized cross-checks against the standard model before proving code equivalence. Include malformed inputs and error behavior when in scope.
4. Extract the Rust through Charon/Aeneas and review the code-shaped Lean model, panic paths, library models, and intrinsics.
5. Prove a layered chain: generated model to code-shaped auxiliary specification; auxiliary specification to standard-derived specification; parameter and precondition theorems; panic freedom.
6. Use proof agents only through managed sessions with theorem preservation and clean replay. Preserve human review for specification choices and difficult semantic gaps.
7. Generate an assumption dashboard covering Rust compiler/backend, Aeneas/Charon, intrinsic/library models, Lean kernel, native mechanisms, caller preconditions, and excluded leakage properties.
8. Validate mutations or known defects to show the theorem chain is sensitive to incorrect code and incorrect specifications.
9. Publish exact theorem names and non-claims. Functional correctness and panic freedom do not by themselves establish constant-time behavior or end-to-end deployment security.

## Output contract

- A source-derived Lean standard specification and vector suite.
- Pinned Aeneas extraction and layered refinement proof.
- Agent proof traces and clean replay.
- An explicit assumption/non-claims dashboard modeled on the verified SymCrypt project.

## Non-negotiable guardrails

- Do not generalize proof coverage beyond the exact functions and branch checked.
- Keep the Rust compiler and extraction chain in the trust statement.
- Code/spec agreement is not independent evidence if both were generated from one source.
- Constant-time and side-channel properties require separate theorems.

## Related formal skills

- `aeneas-charon-rust-to-lean`
- `lean-agent-integration-pantograph-leandojo`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **SYMCRYPT-REPO** — [Microsoft SymCrypt](https://github.com/microsoft/SymCrypt) (2026) — Microsoft. `official-repository`.
- **SYMCRYPT-VERIFIED26** — [Verifying Rust cryptography in SymCrypt: from standards to code](https://www.microsoft.com/en-us/research/blog/verifying-rust-cryptography-in-symcrypt-from-standards-to-code/) (2026) — Microsoft Research. `official-project-report`.
- **AENEAS-REPO** — [Aeneas repository](https://github.com/AeneasVerif/aeneas) (2026) — Aeneas project. `official-repository`.
- **RUST-LEAN-AI26** — [A Rust-to-Lean Verification Pipeline with AI Provers: An Experience Report](https://arxiv.org/abs/2605.30106) (2026) — Natalia Klaus, Juan Conejero, and Palina Tolmach. `research-paper`.
- **LEAN-FAQ** — [Lean FAQ](https://lean-lang.org/faq/) (2026) — Lean project. `official-documentation`.

Bundled source metadata is in `references/REFERENCES.md`.
