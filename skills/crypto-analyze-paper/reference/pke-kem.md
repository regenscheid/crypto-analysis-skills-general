# Public-key encryption and KEMs

> Part of `crypto-analyze-paper`'s security-definitions reference. The framing that
> governs every file here — including the rule that these are **obligations to
> discharge, not prose to cite** — is in [`README.md`](README.md), and the
> shared advantage/query conventions and proof models are in
> [`conventions.md`](conventions.md). Read those first.

## Public-key encryption and KEMs

### IND-CPA

**Game.** Challenger generates (pk, sk), gives pk. Adversary submits m₀, m₁ with
|m₀| = |m₁|; receives c\* = Enc(pk, m_b) for random b; outputs b'.

**Obligations.**
- [ ] Encryption is randomised, or the scheme cannot achieve this at all
- [ ] |m₀| = |m₁| enforced (length is not hidden)
- [ ] Advantage expressed against a stated hardness assumption
- [ ] Reduction is *tight enough* that the claimed λ survives the loss factor

**Operational break.** At toy parameters, distinguish Enc(m₀) from Enc(m₁) with
advantage bounded away from 0 over N samples. Report the observed advantage and
N; do not report "secure" when the observed advantage is merely small.

### IND-CCA1 (lunchtime) and IND-CCA2 (adaptive)

**Game.** As IND-CPA, plus a decryption oracle. **CCA1**: oracle available only
*before* the challenge. **CCA2**: available after too, on any c ≠ c\*.

**Obligations.**
- [ ] Which of CCA1/CCA2 — they are *not* interchangeable
- [ ] The c ≠ c\* restriction enforced, and **ciphertext equality, not plaintext
      equality** — this is where malleability attacks live
- [ ] Decryption failures handled: what does the oracle return on invalid input,
      and does that leak? (Decryption-failure attacks on lattice KEMs are exactly
      this.)
- [ ] For a KEM built by FO transform: the transform's own preconditions
      (correctness error, γ-spreadness or equivalent) actually checked. Which
      variant of the transform, and from which analysis —
      [2017/604](https://eprint.iacr.org/2017/604) (Hofheinz, Hövelmanns, Kiltz)
      decomposes FO into modules with *different* requirements, so "by FO" is
      not a citation. **Keep the two quantum axes apart:** QROM (classical CCA,
      quantum random oracle) is what NIST claims and is analysed in
      [2017/604](https://eprint.iacr.org/2017/604) itself; IND-qCCA
      (*superposition* decapsulation queries) is a different and stronger notion,
      see [2023/792](https://eprint.iacr.org/2023/792). A classical-**ROM** FO
      result does not carry to the **QROM** for free.
- [ ] Correctness error δ **carried into the bound at the right power and
      multiplied by the query budget**, then compared against the target
      advantage rather than against 0 — roughly q_G·δ classically, ~q_G·√δ in
      the QROM. Note HHK's δ is worst-case over messages while FIPS 203's
      Table 1 figure is an *average*; they are not interchangeable.

**Operational break.** Recover the shared secret or distinguish, using the
decryption oracle. For KEMs specifically, the highest-yield check is
**decryption-failure induction**: craft ciphertexts near the failure boundary and
count failures against the claimed failure probability. ML-KEM's claimed rates
are 2⁻¹³⁸·⁸ / 2⁻¹⁶⁴·⁸ / 2⁻¹⁷⁴·⁸ (FIPS 203, retrievable via `nist-mcp_csrc_fulltext`).

### IND-CCA for KEMs — stated separately, because it is not PKE

**Game.** (pk, sk) ← KeyGen; (c\*, ss₀) ← Encaps(pk); ss₁ ← uniform on the key
space. Adversary gets (pk, ss_b, c\*) and a Decaps oracle that refuses c\*;
outputs b'.

**Two differences from the PKE game that matter.**

- There are **no adversary-chosen messages**, so the |m₀| = |m₁| obligation is
  inapplicable. Importing it produces a nonsense check.
- **Implicit vs explicit rejection.** ML-KEM rejects *implicitly* — a malformed
  ciphertext yields a pseudorandom key derived from the rejection secret z, not
  ⊥. An analysis assuming the oracle returns ⊥ on invalid input is analysing a
  different scheme.

**Obligations.**
- [ ] Rejection behaviour stated, and matched to the scheme's actual construction
- [ ] Key space and the distribution ss₁ is drawn from, both stated
- [ ] Decaps oracle refuses exactly c\*, by ciphertext equality
- [ ] Correctness error handled — see the FO obligations above

### Non-malleability (NM-CPA / NM-CCA1 / NM-CCA2)

**Game** (BDPR Def. 2.2). A₁(pk) outputs a message space M and state s; **M must
be valid** — |x| = |x′| for any x, x′ given non-zero probability by M. Then
x₀, x₁ ← M; y ← Enc(pk, x₁); A₂(M, s, y) outputs a relation R and a ciphertext
vector **y**; x ← Dec(sk, **y**).

`Exp^nm-atk-b` returns 1 iff **y ∉ y** ∧ **⊥ ∉ x** ∧ R(x_b, x), and
`Adv^nm-atk = Pr[Exp^nm-atk-1 = 1] − Pr[Exp^nm-atk-0 = 1]`.

**The advantage is a difference of two probabilities, not "R holds".** Omitting
either side condition makes the notion degenerate — with R = true the adversary
wins outright, so no scheme would ever be non-malleable. BDPR's own rationale:
y ∉ **y** exists "in order to not give the adversary credit for the trivial and
unavoidable action of copying the challenge ciphertext."

**Obligations.**
- [ ] Message space M is **valid** (single length) — the NM analogue of
      |m₀| = |m₁|; without it the notion is unachievable
- [ ] Challenge ciphertext excluded from the vector (y ∉ **y**)
- [ ] Every component decrypts validly (⊥ ∉ x)
- [ ] The break beats the **resampled baseline**, not an absolute threshold
- [ ] If a paper claims "non-malleable", check which attack model. Under **CPA
      and CCA1**, NM-ATK ⟹ IND-ATK but not conversely. Under **CCA2 they are
      equivalent**, so an IND-CCA2 proof does establish non-malleability — state
      the model before calling it a mismatch.

### The PKE implication lattice

Canonical source: **[1998/021](https://eprint.iacr.org/1998/021)** — Bellare,
Desai, Pointcheval, Rogaway, *Relations among Notions of Security for Public-Key
Encryption Schemes*. Consult it for the complete matrix; the load-bearing
relations are:

```
IND-CCA2  ⟺  NM-CCA2          (equivalent)
IND-CCA2  ⟹  IND-CCA1  ⟹  IND-CPA      (each strict)
NM-CPA    ⟹  IND-CPA                   (strict)
IND-CPA   ⇏  NM-CPA                    (separation)
NM-CPA and IND-CCA1 are incomparable
```

**Use.** These are what make notion mismatch *detectable*. A proof establishing
IND-CPA under a claim of IND-CCA2 is not a weaker version of the same result —
it is a different result, and the gap is exactly IND-CPA ⇏ IND-CCA1 ⇏ IND-CCA2.

> **Verify against the source before relying on a relation not listed here.**
> The full lattice includes conditional implications whose side conditions
> matter. This file records the relations, not the proofs.

---
