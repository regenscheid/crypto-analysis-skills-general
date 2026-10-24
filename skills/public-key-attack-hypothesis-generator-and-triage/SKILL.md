---
name: public-key-attack-hypothesis-generator-and-triage
description: "Generates falsifiable attack hypotheses from a public-key scheme’s structure, proof seams, distributions, interfaces, and literature, then ranks them by potential impact and information gain."
metadata:
  version: "0.1"
  display-name: "Attack Hypothesis Generator and Triage"
  tags: "hypothesis, triage, research-agenda, falsification"
  requires: "claim-matrix, structure-map, baselines, attack-ledger"
  produces: "ranked-hypotheses, decisive-tests, research-backlog"
---

# Attack Hypothesis Generator and Triage

## Use this skill when

The target has been modeled and the project needs a disciplined research agenda rather than a generic list of attack names.

## Research maturity

Use [the mathematical research workflow](../crypto-investigate/reference/mathematical-research-workflow.md)
for proposals and incomplete arguments. Requirements for a ready experiment or
an established result do not determine which open mathematical questions may be
included in a proposal. Preserve unchecked premises, conditional implications,
and supporting lemmas without calling them validated results. Keep work status,
evidence maturity, review outcome, coverage, and contribution distinct.

## Operating procedure

1. Read the claim matrix, structure map, reduction audit, baselines, and existing ledger. Do not generate hypotheses from the family label alone.
2. Enumerate leverage points: algebraic structure, low entropy, biased or correlated randomness, hidden subspaces, decoding or decryption failures, malformed inputs, validation gaps, transform seams, proof tightness, transcript collisions, and reusable preprocessing.
3. Generate hypotheses at multiple scopes: underlying problem, key generation, core primitive, transform, full construction, multi-user setting, and protocol integration.
4. For each hypothesis write an attack skeleton with required access, indispensable structural conditions, expected signal, target secret/relation, and the exact claim row that would be affected.
5. Estimate optimistic and conservative resources against the generic baseline, explicitly marking unknown exponents and heuristic assumptions.
6. Define a smallest decisive test: proof obligation, toy-instance exhaustive check, reduced-parameter solver experiment, distribution test, estimator sensitivity run, or source-code instrumentation.
7. Create negative controls and failure criteria. State which observation would falsify the idea rather than merely fail to confirm it.
8. Rank by expected impact, plausibility, novelty, feasibility, cost, decisiveness, and information gain. Avoid over-prioritizing attacks merely because tooling already exists.
9. Deduplicate hypotheses that share the same mathematical core and record dependency relationships among branches.
10. Distinguish research questions from experiment-ready hypotheses. A proposal may identify a missing formulation or supporting lemma as its next mathematical obligation. Reserve experimental admission requirements for the experiment queue; scope rejected arguments to what their evidence actually rules out.

## Output contract

- A ranked hypothesis portfolio with attack skeletons and claim mappings.
- A smallest-decisive-test plan and falsification condition for each retained hypothesis.
- Optimistic/conservative resource envelopes and baseline comparisons.
- A deduplicated research backlog with dependencies and stopping criteria.

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

- `COP96-SMALLROOTS`
- `BMM00-INVALIDCURVE`
- `DANVERS19-FAIL`
- `ABD16-SUBFIELD`
- `GJS16-REACTION`
- `BEULLENS20-UOV`
- `CD22-SIDH`
- `KALES20-PICNIC`

Full records are bundled in `references/REFERENCES.md`.
