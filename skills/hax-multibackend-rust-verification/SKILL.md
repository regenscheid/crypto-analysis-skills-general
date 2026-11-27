---
name: hax-multibackend-rust-verification
description: "Uses hax to translate high-assurance Rust into Lean via Aeneas, F*, Rocq, or experimental cryptographic/protocol backends, selecting the backend according to the property."
metadata:
  version: "0.1.0"
  display-name: "hax Multibackend Rust Verification"
  category: "implementation-verification"
  tags: "hax, rust, lean, fstar, rocq"
  requires: "Rust crate, property and target backend, hax-supported subset"
  produces: "translated artifacts, backend proof obligations, feature/translation report, replay package"
  optional: "true"
  namespace: "formal"
---

# hax Multibackend Rust Verification

## Purpose

Uses hax to translate high-assurance Rust into Lean via Aeneas, F*, Rocq, or experimental cryptographic/protocol backends, selecting the backend according to the property.

## Use this skill when

Use this skill when one Rust codebase may benefit from several formal backends, when hax annotations/specifications are already present, or when F* is preferable while retaining a path to Lean or protocol tools.

## Do not invoke automatically

Do not assume all hax backends have equal maturity. The current recommended Lean path uses Charon+Aeneas; other cryptography/protocol backends may be experimental and require stricter validation.

## Optional entry contract

**Inputs**
- Rust crate
- property and target backend
- hax-supported subset

**Expected products**
- translated artifacts
- backend proof obligations
- feature/translation report
- replay package

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Pin hax, Rust, Charon/Aeneas where applicable, backend prover, proof libraries, and crate dependencies. Record the backend maturity documented for that revision.
2. Audit the supported Rust subset and hax-specific annotations, erasures, replacements, trait handling, and library models. Minimize backend-specific source divergence.
3. Choose the backend by claim: Lean for general functional proof, F* for refinement/effects and extraction, Rocq for existing libraries, or experimental EasyCrypt/ProVerif/SSProve only for scoped research prototypes.
4. Run `cargo hax` extraction and preserve typed AST/translation artifacts. Review warnings, dropped constructs, and generated assumptions.
5. Define the independent specification in the backend rather than deriving it entirely from translated Rust. Use hax library models with explicit provenance.
6. Prove safety/refinement at the chosen level and validate with vectors and cross-backend examples. If two backends are used, establish semantic correspondence rather than comparing output text.
7. For experimental backends, construct small hand-audited examples and treat the translator as a larger TCB until soundness and coverage are better established.
8. Re-run translation and proofs after source or hax updates; preserve old artifacts for comparison.
9. Publish backend-specific theorem statements, translation assumptions, unsupported constructs, and which backends were merely generated versus fully checked.

## Output contract

- A backend-selection rationale and maturity record.
- Pinned hax translation artifacts and warnings.
- Checked backend proofs or clearly labeled experimental outputs.
- A source/translation/library-model trust report.

## Non-negotiable guardrails

- Do not claim verification because hax successfully generated code for a backend.
- Experimental translation paths require independent semantic checks.
- Keep generated formal code separate from the independent specification.
- Do not silently switch backends when proof obligations become difficult; record the changed semantics and trust model.

## Related formal skills

- `aeneas-charon-rust-to-lean`
- `fstar-hacl-evercrypt-and-vale`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **HAX-REPO** — [hax repository](https://github.com/cryspen/hax) (2026) — Cryspen. `official-repository`.
- **HAX-MANUAL** — [hax manual](https://hax.cryspen.com/) (2026) — Cryspen. `official-manual`.
- **AENEAS-REPO** — [Aeneas repository](https://github.com/AeneasVerif/aeneas) (2026) — Aeneas project. `official-repository`.
- **CHARON-REPO** — [Charon repository](https://github.com/AeneasVerif/charon) (2026) — Charon project. `official-repository`.
- **FSTAR-HOME** — [F*](https://fstar-lang.org/) (2026) — F* project. `official-project`.
- **ROCQ-HOME** — [The Rocq Prover](https://rocq-prover.org/) (2026) — Rocq project. `official-project`.

Bundled source metadata is in `references/REFERENCES.md`.
