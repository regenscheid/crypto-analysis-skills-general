---
name: symmetric-reproduction-and-falsification-planner
description: "Designs decisive, controlled, reproducible tests of symmetric-cryptanalysis claims, from exhaustive toy checks through full experiments and solver certificates. Use when: A claim depends on computation, simulation, solver output, undocumented code, probabilistic evidence, or an attack transfer. Use it to turn “try this” into a smallest decisive and independently repeatable test."
metadata:
  version: "0.1"
  display-name: "Reproduction and Falsification Planner"
  tags: "reproduction, falsification, experiments, statistics"
  requires: "claim-or-attack-record, target-code, evidence-requirements"
  produces: "reproduction-manifest, test-plan, artifacts, validation-status"
---

# Reproduction and Falsification Planner

## Use this skill when

A claim depends on computation, simulation, solver output, undocumented code, probabilistic evidence, or an attack transfer. Use it to turn “try this” into a smallest decisive and independently repeatable test.

## Assigned scope

Apply this procedure to the assigned quantitative or empirical claim. Being
listed as a related skill or citing a published result does not assign a fresh
cost audit or reproduction. Retain rigorous checks when that is the task. Reuse
compatible evidence and identify the changed dependency behind a repeated check;
see [paper use and verification](../crypto-investigate/reference/paper-use-and-verification.md).
A mathematical proposal may state unresolved cost or empirical obligations
without completing this workflow.

## Operating procedure

1. **State the claim and falsifier.** Write one sentence for the claimed effect and one observable outcome that would falsify or materially weaken it.
2. **Freeze artifacts.** Record spec version, code commit, patches, compiler/interpreter, dependencies, solver/version/options, hardware-relevant settings, and input-generation rules.
3. **Create an independent reference path.** Prefer a second implementation, high-precision computation, exhaustive small instance, symbolic check, or direct simulation that does not share the same likely bug.
4. **Stage the experiment.** Start with hand-checkable vectors and toy/reduced instances; then exhaustive reduced searches; then statistically powered full experiments. Stop when a cheaper stage decisively refutes the claim.
5. **Instrument intermediate values.** Record round states, differences/masks, carries, key-schedule values, constraints, solver witnesses, counters, and filtering stages so failures can be localized.
6. **Use controls.** Include known-positive examples, known-negative examples, randomized/null instances, wrong-key samples, deliberately broken encodings, and boundary cases.
7. **Plan statistics before sampling.** Define test statistic, null/alternative, sample size or sequential stopping rule, confidence interval, multiple-testing correction, and treatment of zero events. Preserve raw counts and seeds.
8. **Validate solver claims.** Check witnesses directly in the primitive. For infeasibility, require a proof/certificate where available or independent encodings and exhaustive small-case comparison. A timeout proves nothing.
9. **Package reproducibly.** Include commands, locked dependencies, deterministic seeds, generated-data manifest, expected outputs, logs, checksums, plots from raw data, and machine-readable results.
10. **Assign status.** Use hypothesis, partially supported, reproduced, independently verified, refuted, superseded, or inconclusive. Explain exactly what remains untested.

For sampling, selected observations, or inconclusive experiments, read
[research stages](../empirical-statistical-and-heuristic-claim-separation/references/research-stages.md).
Exploratory observations can motivate questions; confirmation requires an
appropriate sampling and uncertainty analysis. Formalization is optional.

## Output contract

Fill `assets/REPRODUCTION_MANIFEST.yaml` and produce:

- prioritized tests from cheapest/most decisive to most expensive;
- explicit positive, negative, and null controls;
- sample-size and statistical analysis plan;
- independent validation route;
- commands and expected outputs;
- raw-data and artifact layout;
- falsification conditions and stop rules;
- final validation status with limitations.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `MWGP11-MILP`
- `SHW14-AUTO`
- `TODO15-DIVPROP`
- `GLRS16`

Full records are bundled in `references/REFERENCES.md`.
