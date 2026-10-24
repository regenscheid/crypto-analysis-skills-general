# Hash functions

> Part of `crypto-analyze-paper`'s security-definitions reference. The framing that
> governs every file here — including the rule that these are **obligations to
> discharge, not prose to cite** — is in [`README.md`](README.md), and the
> shared advantage/query conventions and proof models are in
> [`conventions.md`](conventions.md). Read those first.

## Hash functions

Canonical source: **[2004/035](https://eprint.iacr.org/2004/035)** — Rogaway,
Shrimpton, *Cryptographic Hash-Function Basics: Definitions, Implications and
Separations*. Seven notions, not three:

| Notion | Adversary must find | Key/salt |
|---|---|---|
| **Coll** | x ≠ x′ with H(x) = H(x′) | — |
| **Pre** | preimage of H(x) for random x | — |
| **ePre** | preimage, target chosen by adversary *first* | everywhere |
| **aPre** | preimage, worst case over keys | always |
| **Sec** | second preimage of random x | — |
| **eSec** | second preimage, x chosen by adversary first | everywhere |
| **aSec** | second preimage, worst case over keys | always |

**Obligations.**
- [ ] Which of the seven — "collision resistant" is often asserted where only
      second-preimage resistance is needed *or* proved
- [ ] For keyed/salted constructions: which of the a-/e- variants
- [ ] Birthday bound applied to the right notion — Coll ~2^(n/2); Pre ~2^n for a
      single target. **Sec is ~2^n only for short messages, or for wide-pipe and
      truncated constructions.** Under Merkle–Damgård with an n-bit chaining
      value and a 2^M-block target, second-preimage strength falls to ≈ (n − M):
      SP 800-107r1 App. A gives SHA-256 on a gigabyte message as **232 bits, not
      256**. SHA-384, SHA-512/224 and SHA-512/256 are exempt. Quoting 2^(n/2)
      for a preimage claim is a separate and also frequent error.

**Unconditional** — RS04 Prop. 6, "conventional implications", verified verbatim:

```
Coll ⟹ Sec     Coll ⟹ eSec     aSec ⟹ Sec
eSec ⟹ Sec     aPre ⟹ Pre      ePre ⟹ Pre
```

**Provisional** — RS04 Thm. 7. Meaningful only when H compresses substantially;
each carries additive loss 2^(n−m) for domain {0,1}^m, range {0,1}^n:

```
Sec ⟹ Pre     aSec ⟹ Pre     eSec ⟹ Pre     Coll ⟹ Pre     aSec ⟹ aPre
```

> Every other pair among the seven is **separated**. Note especially that
> **Coll ⇏ Pre unconditionally** — RS04 Prop. 9's identity-function
> counterexample — which is the confusion 2004/035 exists to settle.

**Operational break.** Collision search at reduced rounds or truncated output;
report the work done and the birthday expectation for that output size, so an
"attack" that merely matches the generic bound is visible as such.

---
