# Invalid inferences, and what to require instead

> Part of `crypto-review`. This file is about **what conclusion follows from what
> evidence**. Its sibling — the `crypto-analyze-paper` skill's `reference/mismatches.md`
> — is about **which notion was proved versus claimed**. They catch different
> things: a paper can prove exactly the notion it claims and still be described
> in a way this file rejects.

Each row is a step that looks like reasoning and is not. The right-hand column is
not a softening of the claim; it is the different, narrower, true statement that
the evidence actually licenses.

| Invalid inference | What the evidence actually licenses |
|---|---|
| "No attack was found, therefore it is secure." | Report the **search scope** and the **analytical maturity**, then the narrower statement: no qualifying attack is *currently known*. A negative is a claim about the search. |
| "The attack reaches most of the rounds, therefore the full algorithm is nearly broken." | Compare **attack model, work factor, target object, and scaling behaviour**. Round count alone is insufficient — an attack on r−1 rounds may not extend to r at any cost. |
| "The scheme has a proof, therefore it is secure." | State the **theorem, assumptions, reduction loss, and model**, and name the parts of the system the proof does not cover. A proof is a conditional statement, and the conditions are the result. |
| "Scheme A has fewer published attacks than B, therefore A is stronger." | Consider **depth, independence, version stability, reproduction, and how much attention each received**. Paper count measures interest, not resistance. A scheme nobody studied has no attacks against it. |
| "A distinguisher is a break." | State the **property actually violated**, then demonstrate a **consequence for a claimed security game** before using break vocabulary. |

## The one that recurs here

**"No attack was found, therefore it is secure"** is the most frequent of these in
this workbench, and it has been written into the tooling more than once
independently: a corpus miss is reported as *"absence is not evidence of
security"* rather than as a result, and `crypto-verify-claim`'s failure mode 5 records
three negatives concluded from an incomplete look in a single session.

The reason it recurs is structural rather than careless. A search that finds
nothing produces no artifact — there is nothing to cite, nothing to attach, and
the absence feels like a clean result. So the correction has to be mechanical:
**a negative names its channels.** "Not found in ePrint" and "not found in ePrint,
the NIST status reports, and the web" are different findings,
and only the second licenses anything.

## Three rows deliberately not carried over

The source table also covered *"passes test vectors, therefore secure"*, *"TVLA
passed, therefore no side channels"*, and *"A is faster than B"*. Those are
correct and they are **out of scope for this workbench**, which evaluates
primitives, constructions and parameter sets — not implementations, leakage, or
benchmark profiles (see the layer table at the top of `crypto-analyze-scheme`).

They are recorded here rather than silently dropped, because the boundary is the
useful part: if a review finds itself needing one of those rows, the honest answer
is that the question is outside what this workbench can evaluate — not to answer
it anyway.

---

Adapted from the safeguards table in the research synthesis, which attributes the
distinctions to SHA-3 attack comparisons, NIST correctness validation, PQC
security definitions, and side-channel evaluation practice.
