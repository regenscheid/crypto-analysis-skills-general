---
name: hardware-circuit-and-hdl-equivalence-verification
description: "Verifies cryptographic RTL, synthesized netlists, state machines, arithmetic datapaths, and control protocols using equivalence checking, model checking, invariants, and independently checked witnesses where possible."
metadata:
  version: "0.1.0"
  display-name: "Hardware Circuit and HDL Equivalence Verification"
  category: "implementation-verification"
  tags: "hardware, rtl, hdl, yosys, model-checking, equivalence"
  requires: "RTL/netlist artifacts, cycle-accurate specification, clock/reset/interface assumptions"
  produces: "equivalence or safety proof, counterexample trace, synthesis provenance, replay package"
  optional: "true"
  namespace: "formal"
---

# Hardware Circuit and HDL Equivalence Verification

## Purpose

Verifies cryptographic RTL, synthesized netlists, state machines, arithmetic datapaths, and control protocols using equivalence checking, model checking, invariants, and independently checked witnesses where possible.

## Use this skill when

Use this skill when a cryptographic result concerns an FPGA/ASIC implementation, a hardware accelerator, a masked or redundant datapath, or equivalence across RTL and synthesized forms.

## Do not invoke automatically

Do not infer physical side-channel or fault resistance from functional equivalence. Avoid flattening latency, handshakes, reset behavior, or X/unknown semantics into an untimed function when those details are security-relevant.

## Optional entry contract

**Inputs**
- RTL/netlist artifacts
- cycle-accurate specification
- clock/reset/interface assumptions

**Expected products**
- equivalence or safety proof
- counterexample trace
- synthesis provenance
- replay package

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Freeze HDL, generator parameters, synthesis scripts, constraints, tool versions, target technology assumptions, and exact pre/post-synthesis artifacts.
2. Define the reference semantics and temporal contract: clocks, resets, enables, ready/valid handshakes, pipeline latency, stalls, key loading, zeroization, error states, and multi-cycle operation.
3. Normalize endianness, widths, signedness, truncation, memories, ROM initialization, and undefined/X-state behavior before comparing data paths.
4. Use combinational/sequential equivalence for implementation transformations, bounded model checking for shallow bugs, induction/invariants for unbounded safety, and cover properties to detect vacuity/unreachable states.
5. Check generated memories, black boxes, vendor primitives, and clock-domain crossings. Treat unconstrained or abstract modules as explicit assumptions.
6. Validate solver counterexamples in simulation and, for claimed proofs, preserve proof logs/certificates or independent cross-tool checks where supported.
7. Add negative mutations to round constants, state indexing, reset, and handshakes and confirm that properties fail or counterexamples emerge.
8. Keep functional, timing-protocol, leakage, fault, and physical claims separate. Add dedicated models for masking freshness, glitch behavior, or fault detection only when justified.
9. Publish theorem/property files, artifacts, synthesis lineage, assumptions, counterexamples, and replay commands.

## Output contract

- Cycle-accurate specification and formal property set.
- Equivalence/safety/liveness results and minimized counterexamples.
- RTL-to-netlist provenance and black-box assumption register.
- Clean SymbiYosys/Yosys or equivalent replay package.

## Non-negotiable guardrails

- Bounded proof is not unbounded proof unless the bound covers a justified completeness diameter.
- Unreachable antecedents and unconstrained inputs can make properties vacuous.
- Functional equivalence says nothing automatic about glitches, power, EM, or fault injection.
- Keep reset, pipeline, and protocol behavior in scope when they affect cryptographic correctness.

## Related formal skills

- `bitvector-equivalence-and-sat-lowering`
- `constant-time-and-leakage-verification`

## Related cryptanalysis skills in this pack (optional)

- No fixed cross-pack dependency. Invoke from any cryptanalysis skill whose claim matches this capability.

## Associated primary references

- **YOSYS-HOME** — [Yosys Open SYnthesis Suite](https://yosyshq.net/yosys/) (2026) — YosysHQ. `official-project`.
- **SYMBIYOSYS** — [SymbiYosys](https://symbiyosys.readthedocs.io/) (2026) — YosysHQ. `official-manual`.
- **LRAT17** — [Efficient Certified RAT Verification](https://arxiv.org/abs/1612.02353) (2017) — Luís Cruz-Filipe et al.. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
