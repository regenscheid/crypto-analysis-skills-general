---
name: public-key-cryptanalysis-orchestrator
description: "Routes a public-key cryptanalysis project through security-model, construction-level, hard-problem, implementation-interface, proof, cost, transfer, and reproduction skills while maintaining one shared evidence state. Use when starting or resuming an evaluation of a signature, KEM, public-key encryption scheme, key-agreement mechanism, or hybrid construction."
metadata:
  version: "0.1"
  display-name: "Public-Key Cryptanalysis Orchestrator"
  tags: "orchestration, public-key, cryptanalysis, evidence"
  requires: "target-artifacts, claimed-security-properties"
  produces: "evaluation-charter, routing-plan, shared-evidence-state, claim-level-findings"
---

# Public-Key Cryptanalysis Orchestrator

Use [the environment guide](../investigate/reference/environment.md) to select
available instructions and tools. Native skill invocation, a complete catalog,
independent workers, and persistent files are optional. Read supplied text or
files when no loader exists; identify missing procedures and unchecked scope.


## Use this skill when

Start or resume a cryptanalysis project involving a public-key primitive or protocol. Run this before family-specific analysis so the claim, artifact, interfaces, and evidence standards are fixed.

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

1. Freeze the target: collect the exact specification, revision, parameter sets, reference and optimized implementations, test vectors, errata, proof version, and wire-format documents. Hash or otherwise identify every artifact.
2. Create the evaluation charter. List every advertised confidentiality, authenticity, correctness, robustness, and security-level claim; record explicit exclusions such as side channels or malicious implementations.
3. Invoke the security-model skill to create one claim-adversary row per materially different PKE, KEM, signature, AKE, multi-user, quantum, or malformed-input model.
4. Invoke the structure mapper and reduction auditor. Record key generation, algebraic objects, distributions, transforms, encodings, validation rules, and the complete chain from scheme security to mathematical assumptions. Enumerate the automorphisms of each relevant public structure, including all applicable Galois involutions rather than only conjugation, and state any limit on the enumeration.
5. Route along two axes. Select at least one construction skill (PKE, KEM, signature, key agreement, Fiat–Shamir, decryption failure, or hybrid composition) and every applicable mathematical-family skill.
6. Establish generic and family-specific baselines before judging specialized attacks. Reuse compatible checked baselines; recompute affected dependencies or perform an explicitly assigned fresh validation. Pin all estimator versions and cost models.
7. Normalize literature and prior-agent findings into attack records; use transfer analysis rather than analogy to map them to the exact target.
8. For each promising hypothesis, run complexity auditing and design the smallest decisive proof, exhaustive experiment, solver model, or reproduction package.
9. Keep contradictory results, failed branches, proof gaps, implementation defects, and cryptanalytic attacks separate in the ledger. Do not let a summary erase scope qualifiers.
10. Synthesize only at the claim-row level. Report what is established, what is merely plausible, and what evidence would change the conclusion.

## Output contract

- A completed evaluation charter and version manifest.
- A claim-adversary matrix, structure/assumption map, generic baselines, attack ledger, proof audit, parameter-estimate ledger, and research backlog.
- A routing record naming every invoked skill and why it applies.
- Claim-level conclusions with confidence, evidence, scope, and unresolved falsification tasks.

## Non-negotiable guardrails

- Bind every conclusion to the exact artifact, version, parameter set, key format, and security game.
- Distinguish a faster algorithm for an underlying mathematical problem from a complete attack on the cryptosystem, and distinguish a proof gap from an exploit.
- Never present a weak-key, malformed-input, related-key, multi-target, decryption-oracle, leakage, fault, or quantum result as a standard-model full-scheme break without that qualification.
- For a new or independently verified quantitative conclusion, account for the relevant data, oracle queries, arithmetic/bit operations, memory, preprocessing, communication, verification, parallel depth, and success probability in explicit units. Preserve attributed published quantities as source claims; reuse unchanged checked inputs and recompute affected dependencies.
- State the cost model, implementation assumptions, and estimator version; a single headline exponent is not a reproducible security estimate.
- Preserve failed attacks, rebuttals, corrections, withdrawn claims, and source-version chronology in the evidence ledger.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not established by a proof, derivation, experiment, validated implementation, or cited source.
- Do not allow a family label such as “lattice-based” or “code-based” to substitute for a concrete parameterized assumption and attack surface.

## Associated references

- `GM84-PKE`
- `GMR88-SIG`
- `BDPR98-PKE`
- `FO99`
- `BR93-AKE`
- `NIST-SP800-227`
- `NIST-FIPS186-5`

Full records are bundled in `references/REFERENCES.md`.
