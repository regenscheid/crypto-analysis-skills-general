# Failure taxonomy for claim verification

> Part of `crypto-verify-claim` (Step 4). Read it when one of these failure
> modes is relevant to the assigned claim.

These historical examples motivate checks when the corresponding failure mode
is relevant. They do not require opening unrelated sources or rerunning unrelated
calculations for every assigned claim.

**1. Uncited recall of reference data.** Parameter tables, published costs, which
scheme a name refers to. *Observed:* a probe's "fresh" parameters were a
published LUOV set, asserted from memory and never checked; the same class of
error recurred a second time on the same file. **Check:** every parameter tuple
and published figure carries `[SOURCE]`.

**2. Over-correction from a partial source.** Treating one document as exhaustive
and overturning a true statement with it. *Observed:* a correct claim that LUOV
round 2 used prime `r` was "corrected" to composite on the strength of a version
of the paper that omits the table showing both — arriving with more confidence
than the original error. **Check:** before overturning a prior claim, establish
that the new source is *complete* for that question. Prefer the archival version
over a conference version; they differ.

**3. Stale derived numbers after an input change.** *Observed:* changing a
parameter set and recomputing some outputs but not others left a key-recovery
figure 10.2 bits wrong, inside a rubric with a ±0.5 tolerance. **Check:** when an
input changes, identify every affected dependency and recompute those conclusions.
Retain checks whose inputs and assumptions did not change; if dependencies are
uncertain, state which additional review is needed to establish their scope.

**4. Unit or model mismatch in a comparison.** *Observed:* "the structure costs
60 bits" subtracted a field-multiplication count over `F_8` from a bit-operation
count over `F_4096`. **Check:** every difference of two costs states the unit and
the cost model of both. A bare exponent is not a result.

**5. A negative concluded from an incomplete look.** *Observed three times in one
session:* "the repo has no attack references" from a sparse checkout that never
pulled `solution/`; "the paper body is unreachable" from one host's `robots.txt`
when another host served it; "the corpus does not cover this" when the full-text
cache held 9 of 924 documents. **Check:** a negative must name what was searched
and how completely. "Not found in X" is a claim about X.

**6. Discarding the diagnostic you already had.** *Observed:* a fetch returned
HTTP 403 and the script kept the status code and threw away the response body.
The body was the Cloudflare interstitial, which would have said the challenge was
never solved. Instead "403" was reported as a bare fact and written up as a
property of the *publisher* — when it was a property of the script's control
flow. Three further "403" rows in the same table inherited the error.

**Check:** when something fails, keep what it said. A status code without its
body, an exception without its message, a non-zero exit without stderr — each is
a diagnosis discarded at the moment it was free. This is worse than failure mode
5: there the evidence was never gathered; here it was in hand and destroyed.

**7. Verification that repeats the asserter's unchecked premise.** A different
reader or citation does not automatically supply independent evidence. **Check:**
identify the error your route could expose. Independently reconstructing an
argument from the same paper or specification is valid checking. Open another
source when it addresses a specific uncertainty; source novelty is not a gate.

**8. Silent aggregate failure.** *Observed twice:* one estimator family raising
discarded eight valid results, and the failure formatted as a tuple rather than
an error. **Check:** any "cheapest of N" states what was skipped. A minimum over
a reduced set is an upper bound on the minimum over the full set, provided the
retained costs are valid and comparable. State omitted cases; invalid estimates
may support no bound at all.
