# Investigation completion contract

Use this contract to prevent premature or invisible completion.

## Skill trace

Record only instructions whose bodies were actually inspected and whose
procedures materially affected the work. Distinguish native loading, file reads,
and supplied text. Record missing specialist material separately; a name mention
is not an instruction read.

| Order | Skill/method | Access route | Why selected | Product or decision |
|---:|---|---|---|---|
| 1 | `crypto-investigate` | native, file, or supplied text | Cryptographic investigation | Mode and method selection |

Do not list a skill merely because it was installed or mentioned by another
skill. If the runtime exposes skill-call identifiers or transcripts, retain them
with the research artifact.

## Source-grounding record

Record enough detail to distinguish a grounded investigation from an unsupported
claim of having searched.

| Channel or capability | Query, identifier, or artifact | Exact source opened | Version, date, or locator | Outcome | Status |
|---|---|---|---|---|---|

Use `DISCOVERED` for metadata, snippets, or abstracts; `READ` only after opening
the body or exact artifact; `PROVIDED` for a user-supplied artifact actually
inspected; and `BLOCKED` for an unavailable source or capability with the failed
routes recorded. A load-bearing claim cannot rely only on `DISCOVERED` evidence.

For a scheme assessment, cover the source classes material to its scope: normative specifications and
design documents; primary papers; follow-ups, errata, rebuttals, and failed
approaches; implementations and issue discussions; and non-paper competition or
community records. Mark a class `NOT_APPLICABLE` with a reason rather than
silently omitting it.

For a standalone mathematical question, record only the sources and supplied
premises material to that question. The assessment's source-class inventory is
not a prerequisite to developing a lemma or recognizing a routine deduction.

Source inspection and paper correctness are different judgments. Previously
inspected, unchanged source statements supplied in host context can be reused;
identify that provenance without claiming a fresh read. Paper verification is a
separate assigned task: see [paper use](paper-use-and-verification.md).

## Coverage ledger

For an assigned scheme assessment, create one row for each family in its
coverage scope. A proposal or standalone lemma need not complete this assessment
ledger. State what was unexamined without calling it inapplicable.

| Family or surface | Skill | Applicability reason | Status | Evidence | Next decisive action |
|---|---|---|---|---|---|

Use only these statuses:

- `EXAMINED` — the stated evidence supports the scoped result;
- `CANDIDATE` — a falsifiable attack hypothesis survives initial triage;
- `FALSIFIED` — a named proof, counterexample, or controlled experiment defeats
  this exact candidate;
- `NOT_APPLICABLE` — a concrete structural or model precondition fails;
- `BLOCKED` — missing artifact, capability, access, or prerequisite;
- `DEFERRED` — worthwhile but outside the declared budget, with a proposed test;
- `INCONCLUSIVE` — attempted evidence does not decide the question.

Never use `NO_ATTACK` or `SECURE` as a status.

## Candidate record

When reporting a developed cryptanalytic candidate, record:

1. exact target and mechanism;
2. structural reason it might work;
3. required attacker model and preconditions;
4. expected impact if true;
5. cheapest decisive falsifier;
6. test result or unresolved obligation;
7. preliminary time, data, memory, and success accounting;
8. evidence provenance and confidence.

An analogy, related paper, or unexplained statistical anomaly can motivate a
research question; it is not an established candidate result. Do not force an
open mathematical question into a completed attack-record schema. Use the
ordinary proposal or mathematical explanation supplied through the host.

## Completion gates

### All modes

- Complete a source-grounding record proportionate to the claim.
- Inspect each load-bearing source at its exact statement or artifact level,
  or reuse compatible prior inspection with identifiable provenance.
- Expose blocked retrieval and unsearched source classes; do not substitute
  model recall for missing evidence.

### ASSESS

- Freeze target, claims, and models.
- Cover every applicable known family from the selected orchestrator.
- Compare costs to named generic and claimed baselines.
- State search channels and exclusions behind every negative result.

### DISCOVER

- Identify whether the requested product is a proposal or mathematical development.
- Establish the definitions and known ingredients needed for that question; cite
  limits of prior-art coverage before making originality claims.
- For proposals, return reasoned questions, dependencies, horizons, and meaningful
  milestones. The agenda need not fit a fixed number of entries.
- For development, return substantive mathematics and its unresolved obligations.
- Use an informative check when available; lack of a quick falsifier does not
  disqualify an unresolved mathematical question.
- Preserve conditional and negative results at the scope their evidence supports.
- Apply [the research workflow](mathematical-research-workflow.md); full ASSESS
  coverage is required only when a full assessment is part of the assignment.

### VALIDATE

- State the claim so one result can decide it.
- Check preconditions before implementation.
- Read the exact source claim and material corrections or errata.
- Check load-bearing numbers by the appropriate exact calculation, derivation,
  or reproducible computation; state the route and its scope.
- Seek an independent source, derivation, implementation, or checker.

### FORMALIZE

- State the exact theorem and correspondence boundary.
- Pin the normative source and the imported theorem or implementation revision.
- Pin the toolchain and declare axioms or assumptions.
- Replay from a clean state.
- Report the trusted computing base and unformalized gaps.

If a gate cannot be satisfied, return a scoped partial result with the blocking
condition. Do not silently lower the gate.

## Partial mathematical results

An unchecked premise is not a refutation. Report a conditional lemma, incomplete
derivation, or scoped observation with its remaining obligation. Completion of
the overall question and usefulness of the current result are separate judgments.
Use the host-provided context; this contract does not define a project store or
checkpoint format. Evidence labels follow [evidence interpretation](evidence-interpretation.md).

## Contribution language

For a result described as new, state its relationship to the closest known result
and identify the additional reasoning. An unchanged method at a new parameter
set is an application or evaluation, not automatically a novel attack. Use
[contribution assessment](contribution-assessment.md); apply its qualification
in the summary as well as in the detailed finding.
