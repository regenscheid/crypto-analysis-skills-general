---
name: public-key-literature-attack-extractor
description: "Converts papers, reports, code, specifications, issue discussions, or prior-agent findings into normalized public-key attack records with exact provenance, models, requirements, costs, and validation status."
metadata:
  version: "0.1"
  display-name: "Literature Attack Extractor"
  tags: "literature, extraction, provenance, attack-record"
  requires: "source-artifact, target-context"
  produces: "normalized-attack-record, source-chronology, prerequisite-list"
---

# Literature Attack Extractor

## Use this skill when

A source contains a claimed attack, estimator result, proof criticism, parameter analysis, or implementation finding that may be relevant to the target.

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

1. Identify the exact source version, publication date, authors, artifact URL or hash, errata, follow-up papers, code commit, and any later retraction or rebuttal.
2. Extract the target object and result type exactly: mathematical algorithm, distinguisher, key recovery, message recovery, forgery, decoding, decryption failure, reaction attack, proof gap, or implementation defect.
3. Reconstruct the adversary model, oracle access, data source, preprocessing, malformed-input powers, quantum model, and weak-key or parameter restrictions.
4. Write the attack skeleton as a sequence of operations and identify every indispensable requirement rather than copying only the abstract or headline exponent.
5. Extract complete complexity: arithmetic and bit operations, memory, data/oracle queries, preprocessing, communication, parallelism, success probability, false positives, verification, and amortization.
6. Separate asymptotic claims, concrete estimates, implementation measurements, and extrapolations. Record the hardware, software, solver, estimator, and cost model for empirical numbers.
7. Capture proof or experimental evidence, parameter files, seeds, tables, and source locators. Mark results that were not independently reproduced.
8. Compare the source claim with generic baselines and with the source scheme’s advertised claim; preserve the authors’ scope language.
9. Create a normalized attack record and link prerequisites to the target’s structure map for later transfer analysis.
10. Record unresolved ambiguities and contradictions rather than silently resolving them.

## Output contract

- A schema-valid normalized attack record.
- A source chronology including corrections, rebuttals, and code versions.
- A prerequisite list suitable for a transfer matrix.
- A reproduction-assets inventory and ambiguity log.

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
- `MANGER01`
- `NR06-HPP`
- `DANVERS19-FAIL`
- `GJS16-REACTION`
- `BEULLENS22-RAINBOW`
- `CD22-SIDH`

Full records are bundled in `references/REFERENCES.md`.
