---
name: symmetric-cryptanalysis-orchestrator
description: "Coordinates a research-grade symmetric-cryptanalysis evaluation, selects specialist skills, and maintains a shared claim/evidence state. Use when: The task asks for an evaluation of a symmetric primitive, mode, construction, proposal, paper, attack claim, or implementation and requires more than one analytical technique. Use it at the beginning of a project and again whenever the target, model, or evidence changes materially."
metadata:
  version: "0.1"
  display-name: "Symmetric Cryptanalysis Orchestrator"
  tags: "orchestration, symmetric-cryptography, evidence, research"
  requires: "target-artifacts, evaluation-question"
  produces: "evaluation-charter, version-manifest, claim-adversary-matrix, attack-ledger, research-backlog"
---

# Symmetric Cryptanalysis Orchestrator

Use [the environment guide](../investigate/reference/environment.md) to select
available instructions and tools. Native skill invocation, a complete catalog,
independent workers, and persistent files are optional. Read supplied text or
files when no loader exists; identify missing procedures and unchecked scope.


## Use this skill when

The task asks for an evaluation of a symmetric primitive, mode, construction, proposal, paper, attack claim, or implementation and requires more than one analytical technique. Use it at the beginning of a project and again whenever the target, model, or evidence changes materially.

## Required inputs

- The exact question or decision the analysis must support.
- Target specifications, papers, code, test vectors, and known versions.
- Any required attack models, resource limits, exclusions, and reproducibility expectations.

When an input is missing, record it as an explicit uncertainty and proceed with the narrowest defensible interpretation. Do not silently choose a favorable model.

## Mathematical research assignment

For a research proposal or a stated mathematical question, use
[the research workflow](../investigate/reference/mathematical-research-workflow.md).
The full evaluation procedure below applies when that evaluation is requested;
a proposal or lemma does not require completing every assessment artifact.
Use supplied assumptions and prior results at their stated evidence strength.
A catalog link or published ingredient does not itself assign a paper audit;
see [paper use and verification](../investigate/reference/paper-use-and-verification.md).

## Apply research judgment after delegation

Before adopting delegated cryptanalytic work, the main agent applies
[orchestrator review](../investigate/reference/delegated-cryptanalysis-review.md)
to omissions, premature stopping, connections across findings, and overlooked
significance. This applies to all delegated cryptanalysis, not only proof work.
Use an available authorized independent reviewer for correctness checks, or
label a sequential self-check accurately. A favorable review does not establish
that the research went far enough or that important implications were recognized.

## Operating procedure

1. **Create or refresh the evaluation charter.** Record target names, exact artifacts and hashes/commits, parameter sets, claims, exclusions, allowed attacker powers, and the threshold for calling a result reproduced or independently verified.
2. **Freeze the version manifest.** List every specification, paper revision, code repository/commit, compiler/interpreter, solver, and test-vector source. Detect version skew before comparing results.
3. **Invoke `security-model-and-claim-formalizer`.** Require one claim–adversary row for every materially distinct notion or access model.
4. **Invoke `primitive-structure-and-assumption-mapper`.** Build the design graph before selecting attacks. Include state geometry, round functions, nonlinear components, linear layers, constants, key/tweak/nonce injection, initialization/finalization, and security assumptions.
5. **Establish generic baselines.** Use a compatible checked baseline table, or invoke `generic-baseline-calculator` for affected dependencies or an explicitly assigned fresh validation, before accepting “faster than generic,” “practical,” or “break” language.
6. **Audit proofs and bounds when present.** Invoke `security-proof-and-bound-auditor` for theorem-backed claims, reduction-based bounds, or concrete security tables. Keep proof gaps separate from attacks unless a gap is actually exploitable.
7. **Build an attack surface map.** Map each design feature and claim to plausible technique skills. Select techniques by structural prerequisites, not by popularity.
8. **Generate and triage hypotheses.** Invoke `symmetric-attack-hypothesis-generator-and-triage`; require a structural mechanism, prerequisites, expected signal, minimal decisive test, falsifier, and rough resource band for every candidate.
9. **Search and normalize prior work.** Invoke `symmetric-literature-attack-extractor` once per source or coherent source family. Preserve source chronology, corrections, code, and designer responses.
10. **Transfer and extend.** Invoke `symmetric-attack-transfer-and-adaptation` for imported attacks and `distinguisher-to-key-recovery-extension` when a property or distinguisher might become a recovery attack.
11. **Validate and audit.** Invoke `automated-search-model-builder`, `symmetric-reproduction-and-falsification-planner`, and `symmetric-attack-complexity-and-success-auditor` as appropriate. No candidate enters the conclusion ledger without a validation status.
12. **Synthesize at claim level.** Invoke `symmetric-evidence-synthesis-and-research-backlog`. Report exact scope, maturity, confidence, supporting and conflicting evidence, and what would change the conclusion.
13. **Iterate deliberately.** Re-run only the skills affected by a new artifact, corrected model, failed test, or new evidence. Never erase superseded records; mark them superseded and link replacements.

## Technique-selection cues

- Substitution-permutation or Feistel structure: differential, linear, impossible, integral/division, boomerang, algebraic, MITM.
- ARX operations: carry-aware differential, rotational/RX, differential-linear, SAT/SMT/MIQCP.
- Repeated or weakly varying round structure: slide, symmetry, invariant subspace/partition.
- Wide permutations/hash compression: rebound, differential paths, multicollision/herding, MITM preimage.
- Stream ciphers: correlation, algebraic/cube, guess-and-determine, TMDTO, resynchronization.
- Modes/MAC/AEAD: security-game and composition analysis, nonce behavior, forgery bounds, domain separation.
- Quantum claims: Q1/Q2-specific baseline and oracle-cost analysis.

## Output contract

Produce or update:

- an evaluation charter and exact version manifest;
- a claim–adversary matrix;
- a design/assumption graph and attack-surface map;
- generic baseline table;
- normalized attack ledger with status and provenance;
- proof/reproduction/implementation registers as needed;
- a claim-level conclusion table and prioritized research backlog.

The final narrative must be generated from those artifacts, not from memory or an untracked scratchpad.

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
- `LR88`
- `BN00`
- `RS04-HASH`
- `MRH04`

Full records are bundled in `references/REFERENCES.md`.
