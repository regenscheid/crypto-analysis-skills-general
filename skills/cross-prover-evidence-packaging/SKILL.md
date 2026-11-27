---
name: cross-prover-evidence-packaging
description: "Combines results from multiple proof assistants, protocol tools, solvers, and computational checkers without falsely claiming that one system has checked another system’s theorem."
metadata:
  version: "0.1.0"
  display-name: "Cross-Prover Evidence Packaging"
  category: "proof-engineering"
  tags: "cross-prover, evidence, interoperability, trust"
  requires: "heterogeneous proof results, shared claim manifest, tool-specific replay artifacts"
  produces: "typed evidence bundle, claim-to-artifact mapping, combined trust statement, gaps and non-translations"
  optional: "true"
  namespace: "formal"
---

# Cross-Prover Evidence Packaging

## Purpose

Combines results from multiple proof assistants, protocol tools, solvers, and computational checkers without falsely claiming that one system has checked another system’s theorem.

## Use this skill when

Use this skill when one cryptanalysis result depends on, for example, an EasyCrypt reduction, a Lean arithmetic lemma, an LRAT lower bound, and an Aeneas refinement theorem.

## Do not invoke automatically

Do not flatten heterogeneous results into a single “formally verified” badge. Each system has its own logic, model, assumptions, and trust boundary unless an explicit proof translation or certificate import exists.

## Optional entry contract

**Inputs**
- heterogeneous proof results
- shared claim manifest
- tool-specific replay artifacts

**Expected products**
- typed evidence bundle
- claim-to-artifact mapping
- combined trust statement
- gaps and non-translations

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Assign one stable claim ID and decompose it into subclaims accepted by different systems. Record exact implication edges between them.
2. For each artifact, store backend, theorem or property name, source files, toolchain, replay command, model class, assumptions, evidence kind, checker result, and hash.
3. Distinguish imported/reconstructed theorems from externally checked evidence. A PDF, log, or foreign proof file referenced by Lean is not thereby a Lean theorem.
4. Express correspondence obligations explicitly: shared encodings, parameter maps, mathematical definitions, probability conventions, and implementation identifiers.
5. When a common neutral representation exists, validate it independently. Examples include JSON attack witnesses, SMT-LIB formulas, CNF plus maps, executable test vectors, and formal claim manifests.
6. Compute the combined trust statement as the union of residual assumptions plus the correctness of cross-system correspondence. Do not keep only the smallest kernel in the summary.
7. Package replay environments separately if toolchains conflict, then provide a top-level orchestrator that verifies hashes and expected results.
8. Generate a human-readable claim graph showing which subclaims are proved, certified, checked witnesses, empirical, or heuristic.
9. Leave gaps explicit. A partially formal chain can still be valuable, but no unstated implication may bridge the missing link.

## Output contract

- A typed evidence record for each backend artifact.
- A claim/subclaim implication graph and correspondence obligations.
- Replay commands and hashes for every environment.
- A combined assurance statement with unresolved links.

## Non-negotiable guardrails

- Do not say “imported into Lean” unless Lean checks a proof/certificate establishing the stated proposition.
- Do not treat identical prose names as identical formal definitions.
- Preserve each tool’s symbolic, computational, bounded, or implementation semantics.
- Use machine-readable status values rather than prose-only confidence labels.

## Related formal skills

- `evidence-trust-and-tcb-audit`
- `proof-artifact-replay-and-publication`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **LEAN-FAQ** — [Lean FAQ](https://lean-lang.org/faq/) (2026) — Lean project. `official-documentation`.
- **EASYCRYPT-HOME** — [EasyCrypt](https://www.easycrypt.info/) (2026) — EasyCrypt project. `official-project`.
- **TAMARIN-MANUAL** — [Tamarin Prover Manual](https://tamarin-prover.com/manual/master/book/001_introduction.html) (2026) — Tamarin project. `official-manual`.
- **LRAT-CATCHER26** — [LRAT-Catcher: Importing SAT Refutations into Lean](https://arxiv.org/abs/2607.00815) (2026) — LRAT-Catcher authors. `research-paper`.
- **PBLEAN26** — [PBLean: Importing Pseudo-Boolean Proofs into Lean](https://arxiv.org/abs/2602.08692) (2026) — PBLean authors. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
