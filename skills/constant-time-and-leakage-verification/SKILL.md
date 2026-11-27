---
name: constant-time-and-leakage-verification
description: "Formalizes and verifies selected noninterference or leakage properties of cryptographic software while keeping source, compiler, machine, microarchitectural, and physical leakage claims distinct."
metadata:
  version: "0.1.0"
  display-name: "Constant-Time and Leakage Verification"
  category: "implementation-verification"
  tags: "constant-time, noninterference, leakage, side-channel, ct-verif"
  requires: "implementation, public/secret partition, leakage model and platform scope"
  produces: "leakage theorem or counterexample, trace model, compiler/platform assumptions, test and replay artifacts"
  optional: "true"
  namespace: "formal"
---

# Constant-Time and Leakage Verification

## Purpose

Formalizes and verifies selected noninterference or leakage properties of cryptographic software while keeping source, compiler, machine, microarchitectural, and physical leakage claims distinct.

## Use this skill when

Use this skill when secret-dependent control flow, memory access, variable-time arithmetic, declassification, or compiler transformation is materially relevant and a precise leakage model can be stated.

## Do not invoke automatically

Do not use “constant-time” as an unqualified synonym for side-channel secure. Ordinary timing tests, source inspection, or a branch-free theorem cannot establish resistance to power, EM, cache effects outside the model, speculative execution, frequency scaling, or faults.

## Optional entry contract

**Inputs**
- implementation
- public/secret partition
- leakage model and platform scope

**Expected products**
- leakage theorem or counterexample
- trace model
- compiler/platform assumptions
- test and replay artifacts

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Freeze source, compiler, flags, target ISA/microarchitecture, libraries, and deployment context. Identify whether the theorem concerns source, IR, assembly, or binary.
2. Classify every input, state component, length, address, error, and output as public, secret, declassified, or outside scope. State whether secret-dependent termination is possible.
3. Define the leakage trace: branches, load/store addresses, instruction count/class, variable-latency operations, exceptions, allocation, cache lines, or a more detailed microarchitectural observation.
4. Choose a method such as self-composition/noninterference, ct-verif-style LLVM analysis, CT-Prover, Jasmin/Vale leakage proofs, relational proof, or binary symbolic execution. Explain model coverage.
5. Prove functional preconditions and memory safety needed for the leakage theorem; undefined behavior can invalidate source-to-machine reasoning.
6. Analyze compilers and optimizations. Either use a preservation theorem, verify the compiled artifact, or list compiler behavior in the TCB and test the exact binary.
7. Exercise declassification explicitly, including tags, rejection outcomes, message lengths, public keys, and protocol-visible timing. Avoid labeling secret-derived public outputs as leaks without the intended policy.
8. Cross-check with dynamic tools and statistical timing tests, but classify those as empirical complements rather than formal proof.
9. Publish the exact leakage relation, artifact level, target platform, counterexamples, residual channels, and non-claims.

## Output contract

- A formal public/secret/declassification policy.
- A checked leakage/noninterference theorem or minimized counterexample.
- Compiler and platform preservation/assumption report.
- Empirical cross-checks and explicit residual-channel inventory.

## Non-negotiable guardrails

- Never claim universal side-channel resistance from a narrow trace model.
- Variable-time instructions, faults, caches, speculation, and OS noise must be included or excluded explicitly.
- Do not hide secret-dependent error paths behind an API abstraction.
- Constant-time claims must follow the final deployed artifact when compiler behavior is relevant.

## Related formal skills

- `jasmin-easycrypt-high-assurance-crypto`
- `fstar-hacl-evercrypt-and-vale`

## Related cryptanalysis skills in this pack (optional)

- `nonce-randomness-and-hidden-number-analysis`
- `mode-mac-and-aead-analysis`

## Associated primary references

- **CT-VERIF16** — [Verifying Constant-Time Implementations](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/almeida) (2016) — José Bacelar Almeida et al.. `research-paper`.
- **CT-PROVER24** — [Towards Efficient Verification of Constant-Time Cryptographic Implementations](https://arxiv.org/abs/2402.13506) (2024) — Lingyun Cai et al.. `research-paper`.
- **JASMIN17** — [Jasmin: High-Assurance and High-Speed Cryptography](https://doi.org/10.1145/3133956.3134078) (2017) — José Bacelar Almeida et al.. `research-paper`.
- **VALE-PAPER** — [Vale: Verifying High-Performance Cryptographic Assembly Code](https://www.microsoft.com/en-us/research/publication/vale-verifying-high-performance-cryptographic-assembly-code/) (2017) — Barry Bond et al.. `research-paper`.
- **HACL-MANUAL** — [HACL* and EverCrypt manual](https://hacl-star.github.io/) (2026) — HACL* project. `official-manual`.
- **LEAN-FAQ** — [Lean FAQ](https://lean-lang.org/faq/) (2026) — Lean project. `official-documentation`.

Bundled source metadata is in `references/REFERENCES.md`.
