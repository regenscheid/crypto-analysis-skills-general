---
name: symmetric-attack-hypothesis-generator-and-triage
description: "Generates structurally justified, falsifiable attack hypotheses from claims, design features, literature skeletons, and reduced or toy findings, then prioritizes them by likely claim impact and information gain. Use when: A design map and claim model exist, but the project needs novel attack directions or a disciplined choice among many plausible techniques. Use it before expensive solver searches or large experiments, and again when a failed test changes the design understanding."
metadata:
  version: "0.1"
  display-name: "Attack Hypothesis Generator and Triage"
  tags: "hypothesis-generation, attack-planning, triage, falsification"
  requires: "claim-adversary-matrix, design-assumption-graph, generic-baselines, attack-ledger"
  produces: "hypothesis-cards, ranked-experiment-queue, negative-knowledge-plan"
---

# Attack Hypothesis Generator and Triage

## Use this skill when

A design map and claim model exist, but the project needs novel attack directions or a disciplined choice among many plausible techniques. Use it before expensive solver searches or large experiments, and again when a failed test changes the design understanding.

## Research maturity

Use [the mathematical research workflow](../crypto-investigate/reference/mathematical-research-workflow.md)
for proposals and incomplete arguments. Requirements for a ready experiment or
an established result do not determine which open mathematical questions may be
included in a proposal. Preserve unchecked premises, conditional implications,
and supporting lemmas without calling them validated results. Keep work status,
evidence maturity, review outcome, coverage, and contribution distinct.

## Operating procedure

1. **Select one exact claim row.** Bind the exercise to a target/version/parameter set and adversary game. Generate hypotheses against a stated success event, not against the word “security.”
2. **Invert the claim.** Enumerate the direct success event and useful intermediate results: a nonrandom property, distinguisher, subkey filter, state constraint, forgery condition, collision structure, proof-counterexample, or complexity improvement.
3. **Expand the attack surface without conflating models.** Consider chosen/known data, adaptive access, decryption access, related keys or tweaks, nonce repetition or misuse, multi-user amplification, weak-key subsets, reduced rounds, and Q1/Q2 access. Put every materially different model in a separate hypothesis card.
4. **Cut the construction into analyzable regions.** Identify candidate middle states and boundaries around nonlinear layers, diffusion steps, key/tweak injection, initialization/finalization, feed-forward, domain separators, tag checks, and verification points.
5. **Inventory exploitable structure.** Look for low entropy or few degrees of freedom, slow diffusion, sparse dependencies, biased local transitions, low algebraic degree, repeated round functions, weak constants, key-schedule relations, symmetries, invariant sets, separable computations, controllable carries, and unusually cheap filters.
6. **Generate hypotheses by explicit transformations.** Use: local-to-global extension; middle-out matching; boundary extension; differential/linear/integral dualities; hybridization of two partial attacks; time–memory–data exchange; relaxation then recovery of a model restriction; weak-key-to-random-key averaging analysis; reduced-round ladders; toy-instance self-transfer; symmetry or automorphism search; and proof-bound stress cases.
7. **State prerequisites and mechanism.** For every candidate list the indispensable structural and access requirements, why the target may satisfy them, what statistic or witness should appear, and which observation would refute the mechanism.
8. **Design the minimum decisive test.** Prefer the smallest round count, state width, sample size, or solver instance that distinguishes a valid mechanism from an encoding bug or random fluctuation. Include positive, negative, and null-model controls.
9. **Estimate a resource band and baseline.** Give rough data/time/memory/preprocessing/success bounds sufficient to reject candidates that cannot plausibly beat the applicable generic attack even under optimistic assumptions.
10. **Check novelty and lineage.** Link each candidate to source attacks, previous internal hypotheses, and failed attempts. Mark exact reuse, adaptation, hybridization, or genuinely new mechanism; do not claim novelty from unfamiliar terminology.
11. **Prioritize deliberately.** Rank by potential impact on the claim, probability the prerequisites hold, experiment/proof cost, decisiveness, expected information gain, and how much reusable negative knowledge a failure would produce.
12. **Separate questions from experiment-ready candidates.** Keep mathematically meaningful questions and unresolved prerequisites in the research proposal. A candidate enters an experiment queue only when its claim, observable, method, and stopping rule are sufficiently specified. An unready experiment is not a refuted mathematical question.

## Output contract

Create one hypothesis card per candidate containing:

- hypothesis ID and lineage;
- exact target, claim row, model, and scope;
- proposed result type and claim impact;
- attack mechanism and construction cut;
- indispensable prerequisites with evidence/unknowns;
- expected observable, minimal decisive test, controls, and falsifier;
- optimistic and conservative resource bands plus generic baseline;
- transfer or hybridization path;
- priority score with rationale;
- status: proposed, queued, testing, supported, refuted, dormant, or superseded.

Also produce a ranked experiment queue and a negative-knowledge plan describing what each failed test would rule out.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `BR-INTRO`
- `DR02-RIJNDAEL`
- `BS91-DIFF`
- `MAT93-LIN`
- `KW02-INTEGRAL`
- `WAG99-BOOM`
- `DDKS12-DISSECTION`
- `SHW14-AUTO`

Full records are bundled in `references/REFERENCES.md`.
