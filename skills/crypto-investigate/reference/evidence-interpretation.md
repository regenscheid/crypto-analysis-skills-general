# Interpret evidence at the strength it supports

Use a precise statement and scope before choosing an evidence label.

| Evidence | What it can establish | What remains outside it |
|---|---|---|
| Source inspected at an exact locator | What that revision states under its assumptions | Independent correctness of the source |
| Mathematical derivation | Its conclusion if the argument and premises hold | Unchecked premises or missing inferences |
| Independently checked exact witness | The stated instance satisfies the checked predicate | A universal statement or asymptotic behavior |
| Exhaustive finite computation | The stated property on the entire enumerated domain, if enumeration and checking are sound | A larger domain or general theorem |
| Randomized experiment | Observations under a stated sampling process, with uncertainty | Exhaustiveness, proof, or untested distributions |
| Solver result | What the encoded model and checked evidence support | Faithfulness of the encoding by itself |
| Replayed formal proof | The theorem in the formal system, with its assumptions and trusted components | Unproved correspondence to an external specification |
| Timeout, failed search, or unavailable source | A limit of this attempt | Refutation, security, impossibility, or novelty |

Computation can verify a scoped finite fact. Say what was checked, how completely,
and which implementation or certificate was trusted. Use “no counterexample found”
for an unsuccessful non-exhaustive search, not as the universal label for computation.

A missing precondition is **unchecked**, not false. A demonstrated contradiction
may refute the exact claim; a failed implementation may instead reveal an encoding,
input, arithmetic, or software error. Diagnose the discrepancy before assigning it
to the mathematics.

Controls need justified predictions. Removing a sufficient condition need not
make a conclusion false. Choose a known-answer case, an independent implementation,
or another control whose expected behavior follows from the claim. Report the
control's scope; no single kind of control is mandatory for every evidence route.

Independent checking addresses different failure modes. A checker can use the
same normative source while independently reconstructing an argument. An unread
second paper is not a prerequisite, and a second agent repeating the author is
not independent evidence. Keep development and checking distinguishable.

For valid costs in a common model, the minimum over a subset is an **upper bound**
on the minimum over the full set. If retained estimates are not valid comparable
costs, even that interpretation is unavailable. State omitted cases explicitly.

Literature absence supports a bounded search statement with channels, queries,
date, and gaps. It does not establish novelty. A catalog match is a reference lead;
it does not establish applicability or truth.

For a potentially consequential result intended for external release, preserve
the versioned argument, implementation, experiments, and cost assumptions for
domain-expert review. Record which parts received independent human review and
which remain pending; internal agent agreement is not external validation.
Follow the project's disclosure process before making a public claim.
