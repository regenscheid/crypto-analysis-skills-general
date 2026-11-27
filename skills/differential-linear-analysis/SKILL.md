---
name: differential-linear-analysis
description: "Construct and validate differential-linear distinguishers and key recovery on symmetric primitives without assuming unjustified independence at the middle connection. Use when an early differential and a later linear approximation may be joined."
metadata:
  version: "0.1"
  display-name: "Differential-Linear Analysis"
  tags: "differential-linear, DLCT, hybrid-attack, dependency"
  requires: "design-assumption-graph, differential-candidates, linear-candidates"
  produces: "differential-linear-records, middle-model, extension-plan"
---

# Differential-Linear Analysis

## Use this skill when

A target admits a relatively likely differential over an early region and a useful linear approximation over a later region, or when the middle connection has exploitable nonlinear dependence.

## Operating procedure

1. **Choose a split.** Write the target as an upper part, middle connection, and lower part. Define exact differential endpoints and linear masks at each boundary.
2. **Establish upper behavior.** Determine whether the upper result is one trail, a clustered differential, a truncated distribution, or a conditional distribution. Preserve its full relevant output distribution where possible.
3. **Establish lower behavior.** Determine trail/hull correlations, signs, key dependence, and the input distribution assumed by the lower approximation.
4. **Model the middle exactly.** Do not multiply an upper probability and squared lower correlation by default. Use exact enumeration, conditional correlations, DLCT-style tables, transition matrices, or a justified independence theorem/approximation.
5. **Aggregate alternatives.** Search multiple splits, endpoints, and masks. Account for clusters and dependencies rather than selecting only the strongest component pair.
6. **Derive the distinguisher statistic.** Define paired samples, parity relation, expected bias under right and random cases, variance, data requirement, and effect of repeated/plaintext structures.
7. **Extend to recovery.** Identify boundary subkey guesses, partial encryption/decryption, filters, sign handling, ranking, false positives, and verification.
8. **Test key dependence.** Evaluate across keys and, where applicable, related tweaks/nonces. Report mean, variance, tails, and weak-key subsets rather than only an average.
9. **Validate the decomposition.** Compare predicted and measured bias for upper only, lower only, middle conditional behavior, and the full distinguisher. Include null endpoint/mask controls.
10. **Audit the complete attack.** Recompute data, time, memory, success, and generic comparison under the exact oracle model.

## Output contract

Provide:

- split and exact boundary variables;
- upper differential distribution and lower linear hull data;
- middle-dependence calculation and assumptions;
- predicted full bias/correlation and statistical test;
- key dependence and cluster aggregation;
- recovery extension if any;
- component-level and end-to-end validation;
- exact scope and claim impact.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `LH94-DL`
- `BDKW19-DLCT`
- `BS91-DIFF`
- `MAT93-LIN`

Full records are bundled in `references/REFERENCES.md`.
