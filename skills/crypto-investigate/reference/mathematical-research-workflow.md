# Mathematical research for cryptographic evaluation

Use this contract for human-directed research about specified constructions,
definitions, assumptions, or parameter choices. The product can be a research
proposal, a mathematical result, or a standards assessment. Identify which was
requested before applying a specialist's full evaluation checklist.

## Match the work to the requested product

| Product | Required progress | Work that is conditional on the assignment |
|---|---|---|
| Research proposal | Precise questions, their significance, known ingredients, open obligations, and a reasoned ordering | Complete proof, reproduction, and full-scheme assessment |
| Mathematical development | Actual definitions, derivations, lemmas, counterexamples, or informative partial results | Complete family coverage or a priced end-to-end result |
| Paper verification | A verdict on a specified source claim supported by an appropriate check | Broad development of new research questions |
| Scheme assessment | Coverage and quantitative conclusions proportionate to the stated assessment scope | Original mathematical results |

A proposal can be complete while its questions remain unresolved. If development
was requested, another proposal is not sufficient completion. A standalone lemma
does not acquire a full-scheme assessment requirement merely because its objects
arise in cryptography. State the limits of the result instead.

## Keep an agenda distinct from active work

There is no universal five-question or two-question limit. Retain the distinct
questions justified by the requested scope, without padding the list. Group
parameter variants and equivalent formulations under their common mathematical
question unless they introduce materially different assumptions or obligations.

When a ranked proposal is requested, explain significance, relationship to known
results, prerequisite uncertainty, likely information gained, and research
horizon separately. Ready-to-calculate is not the same as important. A difficult
question with a meaningful intermediate milestone can deserve attention even
when a nearby routine calculation is easier. Use qualitative reasons; do not
invent probabilities of discovery or priority scores with false precision.

Active work follows the user's selected question and available resources. A
short immediate work list is an allocation choice, not deletion of the broader
agenda. Distinguish analyst effort (reasoning time, model usage, compute, and
review) from the adversary resources modeled in a cryptanalytic cost claim.
Use the host's existing resource controls; do not invent a scheduler or require
a universal percentage split between literature, development, and checking.

## Preserve immature but meaningful mathematics

An observation may motivate a question before there is a conjecture. A conjecture
may require better definitions before there is a useful experiment. A conditional
argument may need a supporting lemma before its consequence can be asserted.
These are legitimate research states, not automatically rejected candidates.

State an unchecked prerequisite explicitly. If useful, develop the implication
conditional on it or identify the mathematical question that would settle it.
A refuted prerequisite defeats the argument that requires it, within that scope.
An unattempted test, unavailable tool, or unknown premise does not do so.

Use a cheap check when it can answer a concrete uncertainty. Do not require every
question to have a quick decisive experiment before mathematical development can
begin. A derivation, a change of representation, or a precise intermediate lemma
may be necessary to make a question testable. Keep final evidence standards tied
to the strength of the conclusion, as in [evidence interpretation](evidence-interpretation.md).

## Continue the reasoning and recognize progress

Use [mathematical development](../../mathematical-research-development/SKILL.md)
to carry a chosen question beyond its outline. A milestone should change what
is understood: derive a relationship, discharge a supporting obligation,
identify an invalid step, or narrow the assumptions under which a claim holds.
Do not switch questions solely because no quick result appeared. Explain a
change of direction in terms of the mathematical obstruction or changed scope.

At a natural boundary, distinguish the current episode's outcome from the overall
question's status. Return the new mathematics, established ingredients reused,
remaining obligations, and the reason the next inference matters. When continuing,
use the formulation and partial argument supplied by the host. Do not restart
the original survey or generate the same proposal without a changed reason.

## Apply research judgment after delegation

When cryptanalytic research is delegated, the main agent must assess omissions,
premature stopping, connections, and overlooked significance. Follow
[orchestrator research judgment](delegated-cryptanalysis-review.md). This covers
all delegated cryptanalysis; proof review is only one supporting component.
A dedicated reviewer's correctness verdict does not establish sufficient depth
or recognition of the findings' implications. Use its checks while supplying
the main agent's own research judgment.

## Keep status dimensions separate

In the ordinary report, distinguish:

- **Work status:** what was attempted, completed, deferred, or blocked.
- **Evidence:** source statement, derivation, exact check, observation, or proof.
- **Review:** unchecked, independently checked, disputed, or refuted at a stated scope.
- **Coverage:** what question, domain, version, and assumptions were examined.
- **Contribution:** reproduction, application, extension, or potentially new result.

Finishing a task does not verify its result. Reviewing a component does not
establish complete scheme coverage. Failing to find a source does not establish
novelty. These are interpretation rules, not a new storage schema or catalog
submission workflow.

This contract limits the research assignment's scope. Detailed costing applies
when making a quantitative cost claim; reproduction applies when assigned or
needed for an empirical conclusion. Consult [paper use and verification](paper-use-and-verification.md)
before turning a cited ingredient into an audit. Existing host context and
permissions remain authoritative.
