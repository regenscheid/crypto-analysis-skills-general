---
name: evidence-trust-and-tcb-audit
description: "Identifies exactly what must be trusted for a formal or certified result and prevents untrusted search, extraction, native evaluation, opaque models, or hidden axioms from being presented as kernel-checked proof."
metadata:
  version: "0.1.0"
  display-name: "Evidence, Trust, and TCB Audit"
  category: "control"
  tags: "trust, tcb, assumptions, audit"
  requires: "proof or certificate artifact, toolchain manifest, formal claim"
  produces: "TCB inventory, axiom and assumption report, trust classification, remediation tasks"
  optional: "true"
  namespace: "formal"
---

# Evidence, Trust, and TCB Audit

## Purpose

Identifies exactly what must be trusted for a formal or certified result and prevents untrusted search, extraction, native evaluation, opaque models, or hidden axioms from being presented as kernel-checked proof.

## Use this skill when

Use this skill before accepting or publishing any generated proof, solver certificate, extracted-code theorem, protocol result, or rigorous numerical claim.

## Do not invoke automatically

Do not equate “the tool exited successfully” with a small trusted computing base. Some workflows trust compilers, extractors, native code, SMT solvers, handwritten models, or external theorem declarations unless the artifact is independently reconstructed.

## Optional entry contract

**Inputs**
- proof or certificate artifact
- toolchain manifest
- formal claim

**Expected products**
- TCB inventory
- axiom and assumption report
- trust classification
- remediation tasks

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Inventory every executable and semantic component from source artifact to accepted theorem: parsers, translators, compilers, libraries, kernels, tactics, solvers, certificate checkers, native evaluators, code generators, hardware models, and scripts.
2. Classify each component as kernel/checker trusted, specification trusted, certificate-producing but untrusted, proof-generating with reconstruction, assumed-correct translation, empirical oracle, or environment dependency.
3. Inspect the theorem dependency closure for axioms, admitted results, `sorry`/`admit`, unsafe declarations, opaque native computations, unverified reflection, foreign-function calls, and imported precompiled artifacts.
4. For Lean, distinguish kernel reduction and proof terms from `native_decide`, custom kernels, compiled plugins, and project build steps. Use the official trust guidance and record exceptions.
5. For extraction workflows, list the Rust/LLVM/assembly semantics and all library or intrinsic models. A theorem about an extracted model inherits assumptions about translation and model fidelity.
6. For solver workflows, determine whether SAT/SMT/PB output is merely status, a checkable certificate, or a proof reconstructed in the central prover. Include the encoding generator and correspondence theorem.
7. For probabilistic and protocol tools, record the mathematical soundness result of the logic, admitted axioms, symbolic-versus-computational model, boundedness, equational theory, and termination limitations.
8. For numerical results, distinguish exact arithmetic, directed rounding/ball arithmetic, high-precision reference computation, and ordinary floating-point experiments.
9. Produce a concise claim-level trust statement: “The result is valid if A, B, and C hold; X and Y were independently checked; Z remains outside the theorem.”

## Output contract

- A layered TCB inventory and data-flow diagram.
- An assumption/axiom report tied to theorem IDs.
- A classification of each external result as checked, reconstructed, or trusted.
- Remediation options that reduce the TCB or make residual assumptions explicit.

## Non-negotiable guardrails

- Do not claim that a small proof-assistant kernel validates the handwritten formal specification.
- Do not omit the build system or package sources from the execution trust boundary.
- Do not treat a solver as untrusted if the checker still trusts an unverified parser or translation without recording that fact.
- Publish non-claims and residual assumptions beside the main theorem, not in a hidden appendix.

## Related formal skills

- `proof-artifact-replay-and-publication`
- `lean-project-reproducibility-and-supply-chain`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **LEAN-FAQ** — [Lean FAQ](https://lean-lang.org/faq/) (2026) — Lean project. `official-documentation`.
- **AENEAS-REPO** — [Aeneas repository](https://github.com/AeneasVerif/aeneas) (2026) — Aeneas project. `official-repository`.
- **SYMCRYPT-VERIFIED26** — [Verifying Rust cryptography in SymCrypt: from standards to code](https://www.microsoft.com/en-us/research/blog/verifying-rust-cryptography-in-symcrypt-from-standards-to-code/) (2026) — Microsoft Research. `official-project-report`.
- **LRAT17** — [Efficient Certified RAT Verification](https://arxiv.org/abs/1612.02353) (2017) — Luís Cruz-Filipe et al.. `research-paper`.
- **PBLEAN26** — [PBLean: Importing Pseudo-Boolean Proofs into Lean](https://arxiv.org/abs/2602.08692) (2026) — PBLean authors. `research-paper`.
- **CVC5-PROOFS** — [cvc5 Proof Production](https://cvc5.github.io/docs-ci/docs-main/proofs/proofs.html) (2026) — cvc5 project. `official-manual`.

Bundled source metadata is in `references/REFERENCES.md`.
