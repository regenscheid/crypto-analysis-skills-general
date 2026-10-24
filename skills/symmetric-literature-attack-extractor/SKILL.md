---
name: symmetric-literature-attack-extractor
description: "Extracts a published or discovered symmetric-cryptanalysis result into a normalized, source-grounded attack record suitable for reproduction and transfer. Use when: Reading a paper, preprint, thesis, standards comment, issue, code artifact, talk, or internal agent report that claims a cryptanalytic property or attack. Run it before attempting to adapt the result."
metadata:
  version: "0.1"
  display-name: "Literature Attack Extractor"
  tags: "literature, provenance, attack-record, evidence"
  requires: "source-paper-or-report, target-version"
  produces: "attack-record, source-chronology, open-questions"
---

# Literature Attack Extractor

## Use this skill when

Reading a paper, preprint, thesis, standards comment, issue, code artifact, talk, or internal agent report that claims a cryptanalytic property or attack. Run it before attempting to adapt the result.

## Catalog references

Read [catalog use](../crypto-investigate/reference/catalog-use.md) when consulting the
configured catalog MCP server. It supplies changing examples and citations;
linked skills are relevant reading, not mandatory invocations.

## Extract, use, or verify

Read [paper use and verification](../crypto-investigate/reference/paper-use-and-verification.md).
Extraction records the exact published claim, its assumptions, evidence, and
unresolved details. It does not automatically reproduce the paper. Preserve
published quantities as attributed source claims; independently recompute when
verification is assigned, a discrepancy matters, or a changed input requires it.
Reuse previously inspected compatible source material. A missing code artifact
or missing locator remains explicit; it is not a reason to invent evidence.

## Operating procedure

1. **Collect the source family.** Obtain the earliest public version, latest ePrint/final version, errata, supplementary material, code, test vectors, slides only when they add information, designer responses, and independent follow-up work.
2. **Freeze provenance.** Record title, authors, date, version/hash, exact page/section/theorem/table/algorithm, and artifact commit. Preserve what changed between revisions.
3. **Identify the exact target.** Record primitive/spec version, parameters, round count, phases, key schedule assumptions, and whether the paper studies a component, idealized variant, reduced-round construction, or full scheme.
4. **Classify the result.** Use one or more of: structural observation, trail, differential/hull, distinguisher, key/state recovery, forgery, collision/preimage/second-preimage, proof gap, implementation discrepancy, or security reduction.
5. **Extract the adversary model.** Record all oracle access, data control, adaptivity, key/tweak/nonce relations, single/multi-user setting, preprocessing, weak-key conditions, and classical/Q1/Q2 access.
6. **Write the attack skeleton.** Express the attack as a sequence of indispensable transformations independent of the source’s notation: data structure, propagated property, middle condition, guessed material, filtering statistic, ranking, verification.
7. **Extract every requirement.** Include exact state alignment, operation identities, independence/Markov assumptions, key-schedule relations, available degrees of freedom, data structures, memory access, and implementation capabilities.
8. **Extract quantitative claims and their basis.** Preserve the source model, units, assumptions, and omitted terms. Recompute the relevant quantities when verification is assigned or a specific discrepancy requires it; label quantities that remain attributed and unreproduced.
9. **Separate evidence types.** Label theorem, derivation, heuristic, simulation, concrete experiment, solver output, code, or assertion. A plot without raw data and a theorem with unchecked premises have different status.
10. **Record limitations and unresolved questions.** Include model mismatch, parameter restrictions, non-reproduced claims, unavailable code, fragile heuristics, and later corrections or rebuttals.

## Output contract

Create one record conforming to `assets/attack-record.schema.json`, plus:

- a source chronology;
- exact quotation locators without excessive quotation;
- an attack skeleton;
- a requirement list ready for the transfer matrix;
- attributed complexity/success notes, with any independent checks distinguished;
- reproduction status and missing artifacts;
- open questions ranked by their effect on the conclusion.

Do not summarize a source as “breaks X.” State exactly what result it establishes, under which model, and at what scope.

## Non-negotiable guardrails

- Bind every statement to the exact target artifact, version, parameters, round/phase scope, and adversary model.
- Label a result accurately as a property, trail, differential/linear hull, distinguisher, recovery attack, forgery, collision, proof gap, or implementation failure.
- Never describe a reduced-round, weak-key, related-key, nonce-misuse, chosen-ciphertext, Q2, or component-only result as a full-scheme break without the corresponding full-scheme model.
- For a new or independently verified quantitative conclusion, account for relevant data, time, memory, preprocessing, communication, verification, and success probability. Preserve source units and assumptions; distinguish attributed quantities from independent checks and reuse compatible checked inputs.
- Preserve contradictory evidence, failed reproductions, corrections, and source-version chronology.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not directly established by a proof, derivation, experiment, or cited source.

## Associated references

- `BS91-DIFF`
- `MAT93-LIN`
- `WAG99-BOOM`
- `BKR11-BICLIQUE`
- `MRST09-REBOUND`
- `CP02-ALG`
- `KLLN16`

Full records are bundled in `references/REFERENCES.md`.
