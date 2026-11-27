---
name: lean-metaprogramming-and-custom-tactics
description: "Implements auditable Lean macros, elaborators, tactics, theorem generators, and domain-specific automation for recurring cryptographic proof patterns."
metadata:
  version: "0.1.0"
  display-name: "Lean Metaprogramming and Custom Tactics"
  category: "lean"
  tags: "lean, metaprogramming, tactics, automation"
  requires: "repeated proof pattern, formal soundness plan, performance target"
  produces: "Lean tactic or generator, tests, trust assessment, documentation"
  optional: "true"
  namespace: "formal"
---

# Lean Metaprogramming and Custom Tactics

## Purpose

Implements auditable Lean macros, elaborators, tactics, theorem generators, and domain-specific automation for recurring cryptographic proof patterns.

## Use this skill when

Use this skill when ordinary tactics and library lemmas leave a repetitive, structured burden—such as normalizing crypto expressions, generating round equations, checking witness formats, or constructing proof terms from certificates.

## Do not invoke automatically

Do not introduce custom metaprogramming to avoid understanding a one-off theorem. Custom tactics are software components with maintenance and trust consequences.

## Optional entry contract

**Inputs**
- repeated proof pattern
- formal soundness plan
- performance target

**Expected products**
- Lean tactic or generator
- tests
- trust assessment
- documentation

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Specify the tactic’s accepted goal shape, generated terms, failure behavior, and soundness story before coding. Decide whether it merely assembles existing lemmas or performs reflection/certificate checking.
2. Use Lean’s syntax, elaborator, expression, metavariable, and environment APIs through documented interfaces. Avoid depending on unstable internals when a public API exists.
3. Keep the tactic deterministic and diagnostic. It should explain unsupported forms and never silently close a different or weakened goal.
4. For theorem generation, separate untrusted computation from proof construction. Generate explicit proof terms, equality chains, or certificates that the kernel checks.
5. For reflective tactics, prove the correspondence between encoded syntax/evaluation and the proposition being decided. Include malformed encodings and partial operations.
6. Test on positive, negative, boundary, and adversarial examples, including goals that differ subtly in type, modulus, endianness, or assumptions.
7. Benchmark elaboration, kernel checking, memory, and proof-term size on realistic crypto obligations. Provide fallback paths when automation becomes too expensive.
8. Inspect dependencies for unsafe/native components and document whether compiled code participates in the trusted path.
9. Version the tactic with the formal library, publish minimal examples, and add regression tests for every prior unsound-looking or misdiagnosed case.

## Output contract

- A documented Lean tactic/macro/generator with a narrow contract.
- Proof of soundness or explanation of kernel-checked term construction.
- Adversarial tests and performance benchmarks.
- A TCB and compatibility report.

## Non-negotiable guardrails

- Never use `unsafe` proof construction to bypass kernel validation.
- Do not parse pretty-printed goals when structured expressions are available.
- Do not make tactic success depend on network services or mutable external state.
- Generated code and certificates must be reproducible from pinned inputs.

## Related formal skills

- `reflective-decision-procedure-design`
- `lean-agent-integration-pantograph-leandojo`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **LEAN-REF** — [Lean Language Reference](https://lean-lang.org/doc/reference/latest/) (2026) — Lean project. `official-manual`.
- **LEAN-TPIL** — [Theorem Proving in Lean 4](https://leanprover.github.io/theorem_proving_in_lean4/) (2024) — Jeremy Avigad et al.. `official-text`.
- **PANTOGRAPH-REPO** — [Pantograph repository](https://github.com/leanprover/Pantograph) (2026) — Pantograph project. `official-repository`.
- **LEAN-BVDECIDE** — [Lean tactic reference: bv_decide and decision procedures](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/) (2026) — Lean project. `official-manual`.
- **LRAT-CATCHER26** — [LRAT-Catcher: Importing SAT Refutations into Lean](https://arxiv.org/abs/2607.00815) (2026) — LRAT-Catcher authors. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
