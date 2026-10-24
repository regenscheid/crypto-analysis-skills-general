---
name: symmetric-evidence-synthesis-and-research-backlog
description: "Converts attack records, proofs, reproductions, failures, and disagreements into claim-level judgments and a prioritized falsifiable research agenda. Use when: Enough evidence exists to update a review, recommendation, standards comment, research plan, or team knowledge base. It should be the only skill that writes final claim-level conclusions."
metadata:
  version: "0.1"
  display-name: "Evidence Synthesis and Research Backlog"
  tags: "synthesis, confidence, evidence, research-backlog"
  requires: "claim-adversary-matrix, attack-ledger, reproduction-results, proof-audit"
  produces: "claim-status-table, technical-synthesis, research-backlog"
---

# Evidence Synthesis and Research Backlog

## Use this skill when

Enough evidence exists to update a review, recommendation, standards comment, research plan, or team knowledge base. It should be the only skill that writes final claim-level conclusions.

## Research maturity

Use [the mathematical research workflow](../crypto-investigate/reference/mathematical-research-workflow.md)
for proposals and incomplete arguments. Requirements for a ready experiment or
an established result do not determine which open mathematical questions may be
included in a proposal. Preserve unchecked premises, conditional implications,
and supporting lemmas without calling them validated results. Keep work status,
evidence maturity, review outcome, coverage, and contribution distinct.

## Operating procedure

1. **Synthesize by claim row.** Group evidence by exact target/version/model/property rather than by attack name or source prestige.
2. **Preserve result granularity.** Separate full-round from reduced-round, primitive from construction, random-key from weak/related-key, classical from Q1/Q2, mathematical from implementation, and proved from experimental.
3. **Assess evidence maturity.** For each item record source quality, derivation completeness, artifact availability, reproduction, independent verification, sensitivity to assumptions, and unresolved contradictions.
4. **Resolve chronology.** Show original claim, revisions, errata, designer response, follow-up work, and which evidence supersedes what. Never silently replace history.
5. **Calibrate confidence.** Use explicit labels such as high/moderate/low or a stated rubric. Confidence applies to a narrowly worded conclusion, not to the primitive in general.
6. **State exact impact.** Explain which claim is violated, weakened, unaffected, or not evaluable. Quantify resource/security margin only when baseline and audit support it.
7. **Report negative results correctly.** Say “no attack found in model/search space/budget X” and list coverage. Do not convert it to “secure.”
8. **Expose disagreements.** Present strongest evidence for each serious interpretation and identify the experiment, proof, or artifact that would discriminate between them.
9. **Build the backlog.** Convert uncertainties into falsifiable tasks. Rank by expected effect on conclusions, feasibility, cost, prerequisite dependencies, and information gain.
10. **Keep machine-readable links.** Every conclusion and backlog item must link to claim IDs, attack records, evidence locators, and reproduction artifacts.

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

Produce a claim-status table with:

- exact claim/model/scope;
- current status and narrowly worded conclusion;
- confidence and maturity;
- supporting and conflicting evidence;
- assumptions and untested regions;
- known attacks and generic comparison;
- evidence that would change the conclusion.

Produce a research backlog with:

- falsifiable question;
- rationale and expected information gain;
- minimal test/proof;
- required artifacts/tools;
- dependencies;
- estimated computational scale in qualitative bands;
- stop/falsification conditions;
- owner/status links where the environment supports them.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `BN00`
- `RS04-HASH`
- `MRH04`
- `SHW14-AUTO`
- `KLLN16`

Full records are bundled in `references/REFERENCES.md`.
