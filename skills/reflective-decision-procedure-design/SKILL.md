---
name: reflective-decision-procedure-design
description: "Builds small verified or proof-producing decision procedures for recurring cryptographic algebra, finite computation, normalization, and witness-checking obligations."
metadata:
  version: "0.1.0"
  display-name: "Reflective Decision-Procedure Design"
  category: "proof-engineering"
  tags: "reflection, decision-procedure, automation, kernel-checking"
  requires: "recurring decidable goal family, formal semantics, performance requirements"
  produces: "procedure specification, soundness/completeness theorem, implementation, benchmarks and trust report"
  optional: "true"
  namespace: "formal"
---

# Reflective Decision-Procedure Design

## Purpose

Builds small verified or proof-producing decision procedures for recurring cryptographic algebra, finite computation, normalization, and witness-checking obligations.

## Use this skill when

Use this skill when many similar obligations overwhelm general tactics but have a clear executable decision method, such as bit-vector equality, finite-field normalization, polynomial identities, transition-table membership, or attack-witness validation.

## Do not invoke automatically

Do not create custom automation when a maintained library procedure already provides the required theorem and trust profile. Novel tactics add code, maintenance, and soundness risk.

## Optional entry contract

**Inputs**
- recurring decidable goal family
- formal semantics
- performance requirements

**Expected products**
- procedure specification
- soundness/completeness theorem
- implementation
- benchmarks and trust report

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Define the logical proposition and the executable representation independently. State soundness, and completeness if the procedure is used to prove negative results.
2. Choose proof by reflection, verified computation, certificate checking, or theorem generation. Minimize the amount of opaque native code in the trusted path.
3. Canonicalize representations explicitly: coefficient ranges, monomial ordering, bit order, modular residues, vector lengths, permutations, and serialization.
4. Prove correspondence between the decision procedure’s Boolean/result type and the original proposition. Include failure and malformed-input behavior.
5. Use small exhaustive tests and known cryptographic examples to validate both directions before optimizing.
6. Benchmark kernel reduction, generated proof-term size, native execution, and replay time. Split computation from checking if direct reduction produces impractical terms.
7. Expose a narrow user-facing tactic or checker with deterministic diagnostics and stable output artifacts. Do not let it silently change the theorem statement or add assumptions.
8. Audit all foreign functions, compiled code, solver calls, and generated certificates. Record whether the final theorem is kernel-reduced, reconstructed, or relies on an extension.
9. Package the soundness theorem, implementation, examples, and versioning policy as reusable infrastructure for these skills.

## Output contract

- A formal proposition and executable checker specification.
- Soundness and, when needed, completeness theorems.
- A deterministic tactic/checker interface with examples.
- Performance and TCB report.

## Non-negotiable guardrails

- Never use an unproved Boolean checker to discharge a theorem merely because it passes tests.
- Completeness is mandatory when “false” or search exhaustion is used as a universal negative result.
- Beware of proof-term blowup and native-evaluation trust changes.
- Keep the checker independent of the search program whenever practical.

## Related formal skills

- `lean-metaprogramming-and-custom-tactics`
- `lean-certificate-import-and-reflection`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **LEAN-BVDECIDE** — [Lean tactic reference: bv_decide and decision procedures](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/) (2026) — Lean project. `official-manual`.
- **LRAT-CATCHER26** — [LRAT-Catcher: Importing SAT Refutations into Lean](https://arxiv.org/abs/2607.00815) (2026) — LRAT-Catcher authors. `research-paper`.
- **PBLEAN26** — [PBLean: Importing Pseudo-Boolean Proofs into Lean](https://arxiv.org/abs/2602.08692) (2026) — PBLean authors. `research-paper`.
- **SMTCOQ-REPO** — [SMTCoq repository](https://github.com/smtcoq/smtcoq) (2026) — SMTCoq project. `official-repository`.
- **FIAT-CRYPTO19** — [Simple High-Level Code for Cryptographic Arithmetic—with Proofs, Without Compromises](https://adam.chlipala.net/papers/FiatCryptoSP19/) (2019) — Andres Erbsen et al.. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
