---
name: public-key-reproduction-and-falsification-planner
description: "Turns public-key cryptanalytic claims into controlled, reproducible proofs, implementations, solver experiments, simulations, and independent checks with explicit falsification conditions."
metadata:
  version: "0.1"
  display-name: "Reproduction and Falsification Planner"
  tags: "reproduction, falsification, experiments, controls"
  requires: "claim-or-attack-record, source-artifacts"
  produces: "reproduction-manifest, controls, evidence-package, validation-status"
---

# Reproduction and Falsification Planner

## Use this skill when

A claim, attack, failure probability, proof discrepancy, or estimator result needs decisive validation rather than narrative plausibility.

## Assigned scope

Apply this procedure to the assigned quantitative or empirical claim. Being
listed as a related skill or citing a published result does not assign a fresh
cost audit or reproduction. Retain rigorous checks when that is the task. Reuse
compatible evidence and identify the changed dependency behind a repeated check;
see [paper use and verification](../crypto-investigate/reference/paper-use-and-verification.md).
A mathematical proposal may state unresolved cost or empirical obligations
without completing this workflow.

## Operating procedure

1. State the exact proposition to test, target artifact/version, model, parameter range, and what observation would confirm, weaken, or falsify it.
2. Choose the smallest decisive method: algebraic proof, exhaustive toy instance, known-answer test, differential comparison, solver certificate, Monte Carlo estimate, rare-event method, or full implementation reproduction.
3. Build positive and negative controls, including a corrected/reference mode, deliberately vulnerable instance, independent implementation, and randomized instances where appropriate.
4. Pin source commits, compiler/interpreter, dependencies, estimator/solver versions, hardware, environment variables, and all command lines.
5. Record seeds, generated instances, test vectors, input hashes, output hashes, logs, and intermediate invariants sufficient to locate divergence.
6. For probabilistic claims, predefine sample size, stopping rule, confidence interval, multiple-testing treatment, and rare-event methodology. Do not infer tiny failure probabilities from zero observations.
7. For solver claims, request witnesses or independently checkable certificates; distinguish UNSAT/proven bounds from timeout or search exhaustion.
8. For attacks, include the full verification stage and compare observed success, false positives, and resources with the source derivation.
9. Arrange an independent check that does not reuse the same transcription, code path, random generator, or estimator assumptions when practical.
10. Package results in the reproduction manifest and update the ledger with both successful and failed reproductions.

For sampling, selected observations, or inconclusive experiments, read
[research stages](../empirical-statistical-and-heuristic-claim-separation/references/research-stages.md).
Exploratory observations can motivate questions; confirmation requires an
appropriate sampling and uncertainty analysis. Formalization is optional.

## Output contract

- A completed reproduction manifest.
- Executable commands, pinned environment, inputs, seeds, hashes, and expected outputs.
- Controls, statistical plan, and explicit falsification criteria.
- A reproduction report and ledger update.

## Non-negotiable guardrails

- Bind every conclusion to the exact artifact, version, parameter set, key format, and security game.
- Distinguish a faster algorithm for an underlying mathematical problem from a complete attack on the cryptosystem, and distinguish a proof gap from an exploit.
- Never present a weak-key, malformed-input, related-key, multi-target, decryption-oracle, leakage, fault, or quantum result as a standard-model full-scheme break without that qualification.
- For a new or independently verified quantitative conclusion, account for the relevant data, oracle queries, arithmetic/bit operations, memory, preprocessing, communication, verification, parallel depth, and success probability in explicit units. Preserve attributed published quantities as source claims; reuse unchanged checked inputs and recompute affected dependencies.
- State the cost model, implementation assumptions, and estimator version; a single headline exponent is not a reproducible security estimate.
- Preserve failed attacks, rebuttals, corrections, withdrawn claims, and source-version chronology in the evidence ledger.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not established by a proof, derivation, experiment, validated implementation, or cited source.

## Associated references

- `BLE98`
- `DANVERS19-BOOTFAIL`
- `NR06-HPP`
- `BEULLENS22-RAINBOW`
- `CD22-SIDH`
- `PERLNER22-SPHINCS`

Full records are bundled in `references/REFERENCES.md`.
