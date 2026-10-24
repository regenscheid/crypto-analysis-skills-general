# Security definitions, as checkable obligations

Ships with `crypto-analyze-paper`, which runs [`mismatches.md`](mismatches.md) as its
checklist. Also consulted by
`crypto-verify-claim` when a claim turns on a notion being met, and by `crypto-analyze-scheme`
for the NIST category ladder.

Split by primitive so an analysis loads what it needs. A KEM review should not
have to read the seven hash notions to find its own obligations.

| file | covers |
|---|---|
| [`conventions.md`](conventions.md) | Advantage conventions, concrete vs asymptotic, query budgets, and the standard/ROM/QROM distinction. **Cross-cutting — read with any of the below.** |
| [`pke-kem.md`](pke-kem.md) | IND-CPA, IND-CCA1/CCA2, KEM IND-CCA (stated separately — it is not PKE), non-malleability, and the PKE implication lattice |
| [`signatures.md`](signatures.md) | EUF-CMA, SUF-CMA, and the state-reuse obligation stateful hash-based schemes carry |
| [`hash.md`](hash.md) | The seven Rogaway–Shrimpton notions and their unconditional and provisional implications |
| [`symmetric-aead.md`](symmetric-aead.md) | IND-CPA, INT-PTXT/INT-CTXT, and generic composition |
| [`nist-categories.md`](nist-categories.md) | Categories I–V, quoted from the CFP, and the four traps in claiming one |
| [`mismatches.md`](mismatches.md) | The checklist `crypto-analyze-paper` runs — twelve recurring findings |


**These are not here to teach a cryptographer what IND-CCA2 means.** They address
a measured failure mode: asserting that a definition is satisfied without
evaluating its obligations. A glossary does not help with that; a list of
obligations that must each be discharged does.

So every notion below is written as:

- **Game** — setup, oracle access, win condition. Enough to be unambiguous.
- **Obligations** — what a proof of this notion *must* discharge. Each is a
  checkbox. A proof that does not address one has a gap, whatever it says.
- **Operational break** — what `crypto-verify-claim` actually runs at toy parameters.

**Three standing rules.**

1. **Name the notion before answering "is it secure".** The question is
   meaningless otherwise, and drift between notions mid-argument is the single
   most common review finding this file exists to catch.
2. **Never report "verified".** Computation falsifies; it does not verify. The
   vocabulary is "no counterexample at n ≤ N", with N stated.
3. **State the model with the notion.** "IND-CCA2" alone is incomplete;
   "IND-CCA2 in the ROM" and "IND-CCA2 in the standard model" are different
   claims with different strengths.

---

## Sources

All confirmed present in the local ePrint corpus, authors verified against it.

| ePrint | Paper |
|---|---|
| [1998/021](https://eprint.iacr.org/1998/021) | Bellare, Desai, Pointcheval, Rogaway — *Relations among Notions of Security for Public-Key Encryption Schemes* |
| [2004/035](https://eprint.iacr.org/2004/035) | Rogaway, Shrimpton — *Cryptographic Hash-Function Basics: Definitions, Implications and Separations* |
| [2000/025](https://eprint.iacr.org/2000/025) | Bellare, Namprempre — *Authenticated Encryption: Relations among notions and analysis of the generic composition* |
| [2010/428](https://eprint.iacr.org/2010/428) | Boneh, Dagdelen, Fischlin, Lehmann, Schaffner, Zhandry — *Random Oracles in a Quantum World* |
| [2007/291](https://eprint.iacr.org/2007/291) | Birkett, Dent — *Relations Among Notions of Plaintext Awareness* |
| [2017/604](https://eprint.iacr.org/2017/604) | Hofheinz, Hövelmanns, Kiltz — *A Modular Analysis of the Fujisaki-Okamoto Transformation* |
| [2023/792](https://eprint.iacr.org/2023/792) | Ge, Shan, Xue — *On the Fujisaki-Okamoto transform: from Classical CCA Security to Quantum CCA Security* |

NIST: FIPS 203/204/205 and IR 8413 via the `nist` connector; the category ladder
from the 2016 PQC Call for Proposals, quoted above.

**Still a gap:** a primary citation for the SUF ⟹ EUF separation in
[`signatures.md`](signatures.md). The
relation is standard and the separation is witnessed by any re-randomisable
scheme, but this file should cite rather than assert, and the corpus search did
not surface a canonical source. Recorded rather than papered over.
