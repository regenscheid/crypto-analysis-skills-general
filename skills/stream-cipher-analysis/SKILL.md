---
name: stream-cipher-analysis
description: "Analyze stream-cipher initialization and keystream generation with correlation, algebraic and cube, guess-and-determine, state-recovery, resynchronization and time-memory-data attacks. Use when the target produces keystream from a key and IV, including LFSR/NLFSR and ARX state machines."
metadata:
  version: "0.1"
  display-name: "Stream Cipher Analysis"
  tags: "stream-cipher, correlation, state-recovery, TMDTO"
  requires: "stream-cipher-spec, claim-model, keystream-access"
  produces: "stream-attack-records, state-model, tradeoff-analysis, validation-plan"
---

# Stream Cipher Analysis

## Use this skill when

The target generates keystream or a stateful output from a key and IV/nonce, including synchronous stream ciphers, LFSR/NLFSR constructions, filter/combiner generators, ARX state machines, or stream-like modes.

## Operating procedure

1. **Model phases separately.** Describe key loading, IV setup, warm-up, state update, output, rekey/resynchronization, and any state reset or packet boundary. Many attacks target initialization rather than steady-state generation.
2. **Define attacker observations and control.** Known/chosen plaintext, raw keystream, chosen/reused IVs, multiple IVs per key, state resets, output length, packet loss, related keys, and online/adaptive access.
3. **Map state and dependencies.** Identify linear recurrences, nonlinear filters/combiners, carries, memory cells, irregular clocks, algebraic degree, correlation immunity, and diffusion from key/IV to output.
4. **Evaluate correlation attacks.** Derive correlations to internal sequences, parity checks, fast-correlation decoding model, data, noise assumptions, code parameters, and key/state reconstruction.
5. **Evaluate algebraic/cube attacks.** Build equations across time/IVs, degree/sparsity analysis, annihilators, cube superpolys, rank, and solver behavior.
6. **Evaluate guess-and-determine/state recovery.** Choose guessed state variables, deterministic propagation, contradictions, branching, early abort, multiple traces, and verification. Count average branching and weak states.
7. **Evaluate TMTO/TMDTO.** Specify state/key domain, preprocessing, distinguished points/chains, coverage, merges, false alarms, data per key, online lookup, and amortization. Check whether initialization or multiple IVs changes the domain.
8. **Check resynchronization and IV structure.** Look for collisions, equivalent IVs, related states, short cycles, slide/rotation relations, and multi-session aggregation.
9. **Validate end to end.** Recover states/keys on reduced and full targets where feasible; test wrong-key/state controls, multiple IVs/keys, and predicted success distributions.
10. **Compare to exact claims.** Distinguish keystream distinguishing, internal-state recovery, future-output prediction, past-output recovery, and key recovery.

## Output contract

Provide:

- phase-accurate state/interface model;
- selected attack family and structural rationale;
- complete data/time/memory/preprocessing/success derivation;
- multi-IV/key and reset assumptions;
- state/key reconstruction and verification;
- experimental distributions and weak-state classes;
- generic TMDTO/exhaustive comparison;
- exact claim impact.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `SIE84-CORR`
- `MS89-FASTCORR`
- `CM03-ALGSTREAM`
- `DS09-CUBE`
- `HELL80-TMTO`
- `BS00-TMDTO`

Full records are bundled in `references/REFERENCES.md`.
