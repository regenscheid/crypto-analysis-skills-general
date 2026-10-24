---
name: public-key-evidence-synthesis-and-research-backlog
description: "Synthesizes proofs, attacks, estimates, experiments, failed transfers, and implementation findings into calibrated claim-level conclusions and a prioritized public-key cryptanalysis backlog."
metadata:
  version: "0.1"
  display-name: "Evidence Synthesis and Research Backlog"
  tags: "synthesis, confidence, evidence, research-backlog"
  requires: "claim-matrix, attack-ledger, proof-audit, reproduction-results"
  produces: "claim-level-findings, confidence-assessment, prioritized-backlog"
---

# Evidence Synthesis and Research Backlog

## Use this skill when

The project has accumulated heterogeneous evidence and needs a defensible conclusion without collapsing scope or uncertainty.

## Research maturity

Use [the mathematical research workflow](../crypto-investigate/reference/mathematical-research-workflow.md)
for proposals and incomplete arguments. Requirements for a ready experiment or
an established result do not determine which open mathematical questions may be
included in a proposal. Preserve unchecked premises, conditional implications,
and supporting lemmas without calling them validated results. Keep work status,
evidence maturity, review outcome, coverage, and contribution distinct.

## Operating procedure

1. Group evidence by claim ID, exact target version, parameter set, adversary model, and result type. Do not synthesize across incompatible rows.
2. Build an evidence table separating theorem, derivation, estimator output, implementation measurement, exhaustive experiment, statistical estimate, solver result, and expert inference.
3. Assess independence: identify shared code, transcriptions, estimator assumptions, datasets, proofs, and authorship that prevent evidence from counting as independent confirmation.
4. Resolve chronology. Prefer corrected specifications and later validated results while preserving earlier claims, rebuttals, withdrawals, and reasons for changes.
5. Classify each conclusion as established break, validated attack below target, security-margin result, proof/definition issue, implementation defect, unsupported claim, inconclusive, or no attack found within a stated search scope.
6. Assign confidence based on evidence quality, reproduction, model fidelity, sensitivity, and unresolved assumptions—not on rhetorical consensus.
7. State exact consequences: affected keys/messages/sessions, parameter sets, security games, success probability, resources, mitigations, and whether standards-level claims remain intact.
8. Convert uncertainties into falsifiable backlog items with the smallest decisive test, expected information gain, dependencies, cost, and stopping rule.
9. Preserve negative knowledge: failed attack transfers, corrected models, false leads, and regions already exhaustively searched.
10. Produce a concise executive finding and a technical annex that exposes the complete reasoning chain through artifacts and source locators.

## Contribution and originality

Before claiming a new result, use
[contribution assessment](../crypto-investigate/reference/contribution-assessment.md).
State the closest known result, the changed scope, and the additional reasoning
actually supplied. Distinguish routine applications and new evaluations from
substantive extensions or potentially new methods. Keep correctness, originality,
and significance separate; a useful parameter-specific finding need not be novel.

For sampling, selected observations, or inconclusive experiments, read
[research stages](../empirical-statistical-and-heuristic-claim-separation/references/research-stages.md).
Exploratory observations can motivate questions; confirmation requires an
appropriate sampling and uncertainty analysis. Formalization is optional.

## Output contract

- Claim-level findings with scope, confidence, evidence, and consequence.
- An evidence-dependence and disagreement map.
- A prioritized falsifiable research backlog.
- A durable negative-knowledge record and technical annex.

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

- `NIST-IR8545`
- `NIST-IR8610`
- `HHK17-FO`
- `HULSING22-TIGHT`
- `BEULLENS22-RAINBOW`
- `CD22-SIDH`

Full records are bundled in `references/REFERENCES.md`.
