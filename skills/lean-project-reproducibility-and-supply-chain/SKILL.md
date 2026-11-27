---
name: lean-project-reproducibility-and-supply-chain
description: "Pins and audits Lean toolchains, Lake dependencies, generated artifacts, build scripts, native components, and repository provenance for secure clean replay."
metadata:
  version: "0.1.0"
  display-name: "Lean Project Reproducibility and Supply-Chain Control"
  category: "lean"
  tags: "lean, reproducibility, supply-chain, lake, sandbox"
  requires: "Lean project, dependency graph, deployment environment"
  produces: "toolchain lock, dependency and build audit, reproducible environment, security findings"
  optional: "true"
  namespace: "formal"
---

# Lean Project Reproducibility and Supply-Chain Control

## Purpose

Pins and audits Lean toolchains, Lake dependencies, generated artifacts, build scripts, native components, and repository provenance for secure clean replay.

## Use this skill when

Use this skill for any Lean project whose result will be reused, published, run by agents, or built from third-party repositories.

## Do not invoke automatically

Do not assume proof-assistant projects are inert data. Lean/Lake builds and elaboration can execute code, invoke native tools, and load plugins; untrusted projects require the same sandboxing discipline as other code.

## Optional entry contract

**Inputs**
- Lean project
- dependency graph
- deployment environment

**Expected products**
- toolchain lock
- dependency and build audit
- reproducible environment
- security findings

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Pin `lean-toolchain`, Lake manifest, git dependencies and revisions, package sources, submodules, native libraries, and external solvers. Record upstream canonical URLs and local hashes.
2. Inspect build scripts, `lakefile`, macros, elaborators, `run_tac`, custom plugins, FFI, native executables, generated code, and post-build actions before running an untrusted project.
3. Build in a least-privilege container or VM with network and credential isolation. Mount only the required source and output directories and constrain CPU, memory, and process count.
4. Separate dependency acquisition from proof replay. Cache verified source archives or Nix/container derivations and disable network access during final checking.
5. Regenerate derived files from pinned sources and compare hashes. Treat committed generated models or certificates as evidence whose provenance must be checked.
6. Run theorem/axiom scans and distinguish kernel proof checking from native evaluation or external checker invocation. Document every trusted compiled component.
7. Test reproducibility on a second clean environment or architecture when feasible, especially for proofs that depend on native solvers, floating point, or generated code.
8. Produce an SBOM-like inventory for the proof artifact and a vulnerability/update policy. Dependency updates trigger replay and theorem-diff review rather than automatic acceptance.
9. Package an offline replay command and validator that fails on source, toolchain, certificate, or theorem-statement drift.

## Output contract

- A complete Lean/Lake/native dependency lock and source inventory.
- A sandbox and offline replay configuration.
- Build-script, plugin, FFI, and generated-artifact audit findings.
- Cross-environment reproducibility results and update policy.

## Non-negotiable guardrails

- Do not run unreviewed Lean repositories with developer credentials or broad filesystem access.
- Do not substitute a newer dependency when the pinned revision disappears without recording a new proof-artifact version.
- Native decisions and external tools must appear in the trust report.
- Keep source and build-output hashes separate so cached artifacts cannot masquerade as regenerated proof.

## Related formal skills

- `evidence-trust-and-tcb-audit`
- `proof-artifact-replay-and-publication`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **LEAN-FAQ** — [Lean FAQ](https://lean-lang.org/faq/) (2026) — Lean project. `official-documentation`.
- **LEAN-REF** — [Lean Language Reference](https://lean-lang.org/doc/reference/latest/) (2026) — Lean project. `official-manual`.
- **MATHLIB-REPO** — [Mathlib 4](https://github.com/leanprover-community/mathlib4) (2026) — Lean community. `official-repository`.
- **PANTOGRAPH-REPO** — [Pantograph repository](https://github.com/leanprover/Pantograph) (2026) — Pantograph project. `official-repository`.
- **AENEAS-REPO** — [Aeneas repository](https://github.com/AeneasVerif/aeneas) (2026) — Aeneas project. `official-repository`.

Bundled source metadata is in `references/REFERENCES.md`.
