# NIST security categories

> Part of `crypto-analyze-paper`'s security-definitions reference. The framing that
> governs every file here — including the rule that these are **obligations to
> discharge, not prose to cite** — is in [`README.md`](README.md), and the
> shared advantage/query conventions and proof models are in
> [`conventions.md`](conventions.md). Read those first.

## NIST security categories

**Where the definition lives, and why that matters.** FIPS 203's glossary defines
*security category* only as "a number associated with the security strength of a
post-quantum cryptographic algorithm, as specified by NIST (see [7])" — it
defers. The ladder itself is in the **PQC Call for Proposals** (Dec 2016), which
is a project document rather than a numbered publication, so a search tool over
NIST's numbered publications may not hold it. It is fetchable directly:
`csrc.nist.gov/CSRC/media/Projects/Post-Quantum-Cryptography/documents/call-for-proposals-final-dec-2016.pdf`

The round status reports (for example IR 8413) restate the categories, and the
initial public draft of SP 800-57 Part 1 Rev. 6 carried the category
descriptions and MAXDEPTH. Whether a NIST tool holds a given edition is a
question for the tool: resolve it by designation (for example
`nist_get_publication(query="IR 8413")`), and ask its corpus status for coverage,
rather than assuming. Go to the CFP itself for the "all metrics" requirement and
the ordering footnote.

Verbatim from that document — each category is "any attack that breaks the
relevant security definition must require computational resources comparable to
or greater than those required for":

| Cat | Requirement |
|---|---|
| **1** | key search on a block cipher with a 128-bit key (e.g. AES128) |
| **2** | collision search on a 256-bit hash function (e.g. SHA256/SHA3-256) |
| **3** | key search on a block cipher with a 192-bit key (e.g. AES192) |
| **4** | collision search on a 384-bit hash function (e.g. SHA384/SHA3-384) |
| **5** | key search on a block cipher with a 256-bit key (e.g. AES 256) |

**Four things that make category claims treacherous.**

1. **The pegs are computational-resource comparisons, not bit counts.** The CFP
   says resources "may be measured using a variety of different metrics (e.g.,
   number of classical elementary operations, quantum circuit size, etc.)" and
   requires the threshold be met "with respect to **all** metrics that NIST deems
   to be potentially relevant". A single-metric argument does not establish a
   category.
2. **The pegs are themselves estimates that have moved.** Quantum gate counts for
   AES have been revised (e.g. [2019/854](https://eprint.iacr.org/2019/854)). A
   category is a moving target, not a constant.
3. **Category claims have been withdrawn in practice.** IR 8413 records that
   during round 3 "two attacks were discovered which called into question the
   claimed category 5 security of parameter sets using SHA-256." Treat a category
   claim as a claim, not a fact.
4. **"Security category" is overloaded inside NIST.** FIPS 199 uses it for
   *information-system impact levels* (low/moderate/high), unrelated to PQC
   strength, and a search for `"security category"` can surface that sense
   (SP 800-60, FIPS 199, ITL Bulletins) before the PQC ladder. Name the PQC
   context in the query, or go to the documents above directly.

**Obligations for any category claim.**
- [ ] Category number stated, and which parameter set it applies to
- [ ] The metric(s) under which the threshold is claimed
- [ ] Whether the claim is against classical or quantum resources, or both
- [ ] **MAXDEPTH accounted for.** The CFP's quantum thresholds are all
      depth-divided — 2^170/MAXDEPTH for AES-128, 2^233/MAXDEPTH for AES-192,
      2^298/MAXDEPTH for AES-256 — because a quantum attack's usable parallelism
      is bounded by how long a coherent computation can run. A quantum cost
      quoted without a MAXDEPTH assumption is not comparable to the threshold.
- [ ] Cross-checked against an estimator (`lattice-estimator`,
      `cryptographic_estimators`) with a **named cost model** — never a bare λ

---
