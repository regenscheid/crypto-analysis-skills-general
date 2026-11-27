---
name: proof-artifact-replay-and-publication
description: "Performs clean, isolated replay of proof and certificate artifacts and publishes a claim-scoped bundle containing theorem statements, sources, assumptions, hashes, logs, and non-claims."
metadata:
  version: "0.1.0"
  display-name: "Proof Artifact Replay and Publication"
  category: "control"
  tags: "replay, publication, reproducibility, artifact"
  requires: "completed proof artifacts, toolchain lock, claim manifest"
  produces: "replay result, publication bundle, checksums, human-readable assurance report"
  optional: "true"
  namespace: "formal"
---

# Proof Artifact Replay and Publication

## Purpose

Performs clean, isolated replay of proof and certificate artifacts and publishes a claim-scoped bundle containing theorem statements, sources, assumptions, hashes, logs, and non-claims.

## Use this skill when

Use this skill when a proof, certificate, verified witness, or implementation-refinement result is ready to be treated as evidence outside its development session.

## Do not invoke automatically

Do not publish only a screenshot, prover success message, generated HTML, or final theorem name. The artifact must be replayable from frozen inputs and auditable without trusting the generating agent.

## Optional entry contract

**Inputs**
- completed proof artifacts
- toolchain lock
- claim manifest

**Expected products**
- replay result
- publication bundle
- checksums
- human-readable assurance report

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Create an immutable source snapshot or identify exact repository commits, submodules, package locks, container/Nix derivations, standards revisions, and generated-model inputs.
2. Remove or neutralize the target proof body when evaluating an agent-generated proof, where the backend permits it, so cached objects or imported completed theorems cannot satisfy the task accidentally.
3. Build in an isolated environment with network access disabled after dependency acquisition. Record all commands, environment variables, CPU architecture, solver versions, and resource limits that can affect behavior.
4. Regenerate extracted code models, generated constraints, and certificates from pinned inputs where feasible. Compare hashes with committed artifacts and explain any expected nondeterminism.
5. Run the native kernel/checker, scan for forbidden admissions and unexpected axioms, validate every certificate, and execute independent witness checkers and test vectors.
6. Compare the accepted theorem statement to the claim manifest structurally: quantifiers, domains, preconditions, parameters, error behavior, probability bounds, and exclusions.
7. Package sources, proof scripts, generated evidence, checker logs, dependency/axiom reports, and machine-readable metadata. Include licenses and source links but do not redistribute restricted standards or proprietary code.
8. Write a human assurance statement that separates proved facts, modeled assumptions, toolchain assumptions, empirical cross-checks, and open gaps.
9. Compute hashes and generate a manifest after all files are final. Re-run the pack validator against the publication copy.

## Output contract

- A clean replay log with pass/fail status for each theorem and certificate.
- A proof artifact manifest with toolchain, hashes, sources, trust assumptions, and theorem locators.
- A self-contained or reproducibly fetchable publication bundle.
- A concise assurance and non-claims report suitable for linking from an attack or cryptanalysis record.

## Non-negotiable guardrails

- Cached compiled objects do not count as clean replay unless their provenance is part of the accepted TCB.
- Do not silently update dependencies to make a proof pass.
- Do not publish a stronger prose claim than the replayed theorem statement.
- Failed replay remains part of the evidence chronology; do not overwrite it with a later success.

## Related formal skills

- `evidence-trust-and-tcb-audit`
- `lean-project-reproducibility-and-supply-chain`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **LEAN-FAQ** — [Lean FAQ](https://lean-lang.org/faq/) (2026) — Lean project. `official-documentation`.
- **SHANNON26** — [ShannonProver: Towards Automating Formal Cryptographic Proofs](https://arxiv.org/abs/2607.02847) (2026) — Yiping Ma et al.. `research-paper`.
- **AENEAS-REPO** — [Aeneas repository](https://github.com/AeneasVerif/aeneas) (2026) — Aeneas project. `official-repository`.
- **SYMCRYPT-VERIFIED26** — [Verifying Rust cryptography in SymCrypt: from standards to code](https://www.microsoft.com/en-us/research/blog/verifying-rust-cryptography-in-symcrypt-from-standards-to-code/) (2026) — Microsoft Research. `official-project-report`.
- **LRAT-CATCHER26** — [LRAT-Catcher: Importing SAT Refutations into Lean](https://arxiv.org/abs/2607.00815) (2026) — LRAT-Catcher authors. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
