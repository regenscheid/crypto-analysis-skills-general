# Symmetric encryption and AEAD

> Part of `crypto-analyze-paper`'s security-definitions reference. The framing that
> governs every file here — including the rule that these are **obligations to
> discharge, not prose to cite** — is in [`README.md`](README.md), and the
> shared advantage/query conventions and proof models are in
> [`conventions.md`](conventions.md). Read those first.

## Symmetric encryption and AEAD

**IND-CPA** — as in [`pke-kem.md`](pke-kem.md) but with a symmetric
encryption oracle. Requires randomised
or nonce-based encryption; deterministic ECB-style encryption fails immediately.

**INT-PTXT / INT-CTXT** — integrity of plaintexts / of ciphertexts. INT-CTXT is
the stronger and the one AEAD needs.

Canonical source: **[2000/025](https://eprint.iacr.org/2000/025)** — Bellare,
Namprempre, *Authenticated Encryption: Relations among notions and analysis of
the generic composition*.

```
IND-CPA  ∧  INT-CTXT  ⟹  IND-CCA
INT-CTXT ⟹ INT-PTXT              (strict)
```

**Obligations.**
- [ ] **Nonce-misuse behaviour stated.** Most AEAD security collapses entirely on
      nonce repeat. "Secure" without a nonce-uniqueness assumption is incomplete.
- [ ] Associated data covered by the integrity claim, not just the plaintext
- [ ] Which composition (Encrypt-then-MAC / MAC-then-Encrypt / Encrypt-and-MAC) —
      they are **not** equally secure in general, which is the paper's point
- [ ] Tag length appears in the forgery bound

**Operational break.** Forge a (nonce, AD, ciphertext, tag) that verifies. Then
repeat a nonce and check what leaks — that is where deployed AEAD actually fails.

---
