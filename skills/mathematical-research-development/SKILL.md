---
name: mathematical-research-development
description: Develop an explicitly stated mathematical question into definitions, lemmas, derivations, counterexamples, or scoped partial results. Use for a stated mathematical problem, proof exploration, an incomplete argument, or extended derivation work. Formal proof assistants are optional.
---

# Develop a mathematical argument

Use [the environment guide](../crypto-investigate/reference/environment.md) to read
related instructions through a native loader, files, or supplied text. Tool names
and Python record-keeping examples below apply only when those capabilities are
available. Without them, analyze the inspected evidence and keep a text record;
label missing source retrieval, computation, or independent checks explicitly.


Take one stated mathematical question. Work on its unresolved reasoning and
return the mathematics produced, including useful partial results. For open-ended
or extended derivation work, read [development guidance](references/development.md)
for alternative representations, sustained reasoning, and proportionate checking.

For proposals, longer research horizons, and continuation milestones, read
[the research workflow](../crypto-investigate/reference/mathematical-research-workflow.md).
For literature ingredients, use [paper use and verification](../crypto-investigate/reference/paper-use-and-verification.md).
For empirical evidence, the statistical skill is directly available without
formalization. Consult [catalog reading](../crypto-investigate/reference/catalog-reading.md)
when historical examples would clarify a mathematical concept or scope distinction.

## Make the question precise

State the objects, domains, quantifiers, assumptions, desired conclusion, and
what would constitute a counterexample. Distinguish a theorem sought from a
numerical observation or an interpretation of an existing source.

Use supplied context and cite known ingredients. Recheck an established fact
when its statement, assumptions, version, or reliability matters to the current
inference. Do not restart a broad literature survey merely because work resumes.
Read a load-bearing source before treating its exact statement as established.
Separate using an established theorem, checking its hypotheses here, and
re-proving it. The current inference usually needs the first two. Repeat a check
only for a concrete uncertainty or an explicit validation objective.

## Develop the unresolved part

Separate a difficult assertion into explicit mathematical obligations. For each
step, write the inference and the assumptions it consumes. A conditional lemma
can be useful while one premise remains open; carry that premise into every
dependent conclusion.

Choose a representation that makes the argument inspectable: definitions and
equations, a dependency diagram, a finite example, or a proof with named lemmas.
If a calculation is needed, state which mathematical uncertainty it addresses.
Do not treat more citations, a longer plan, or repeated arithmetic as a substitute
for the missing inference.

Distinguish these outcomes:

- **Established step:** the stated argument or exact check supports its scope.
- **Conditional step:** the implication is justified, but a premise remains open.
- **Conjecture:** a proposed statement whose proof is incomplete.
- **Refuted statement:** a valid counterexample or contradiction defeats it.
- **Unresolved question:** available work has not decided it.

Failure to prove a statement does not refute it. Failure of one proof strategy
does not refute the statement either. Explain what each failed argument actually
rules out.

## Check the claim at the right strength

Read [evidence interpretation](../crypto-investigate/reference/evidence-interpretation.md)
when deciding what a derivation or computation establishes. Review quantifiers,
boundary cases, hidden assumptions, and dependence between lemmas. Separate
development from independent checking when the conclusion warrants it. A formal
proof assistant is one assurance option, not a requirement for doing mathematics.

If work was delegated, the main agent applies
[orchestrator review](../crypto-investigate/reference/delegated-cryptanalysis-review.md)
to its depth, omissions, connections, and significance before synthesis. Use
an available authorized reviewer for correctness, or label a sequential self-check
accurately; a checked argument can still leave
important parts of the requested mathematical development undone.

## Assess what was contributed

Read [contribution assessment](../crypto-investigate/reference/contribution-assessment.md)
before claiming originality. Separate a known theorem's instantiation, a new
evaluation, a substantive extension, and a potentially new result. Identify the
additional mathematical step; new notation or a different parameter value does
not by itself supply one. Useful progress need not be scientifically novel.
Check whether the result is an elementary corollary, equivalent reformulation,
or direct chain of standard facts. Show that chain and label it a routine
derivation when no substantive additional step is identified. An unfamiliar
statement or independently written proof is not automatically potentially new.

## Return useful partial work

Give the current statement, derivation or counterexample, scope, remaining
obligation, and why that obligation matters. If time ends, return the mathematical
progress already made; do not relabel an unfinished proof as a failed conjecture.

The host supplies investigation context and project knowledge. This skill does
not define storage, checkpoints, background execution, or a new persistence
format. It does not select targets or execute exploitation workflows. Physical
security is outside this skill's scope.
