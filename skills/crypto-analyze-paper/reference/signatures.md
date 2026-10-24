# Signatures

> Part of `crypto-analyze-paper`'s security-definitions reference. The framing that
> governs every file here — including the rule that these are **obligations to
> discharge, not prose to cite** — is in [`README.md`](README.md), and the
> shared advantage/query conventions and proof models are in
> [`conventions.md`](conventions.md). Read those first.

## Signatures

### EUF-CMA and SUF-CMA

**Game.** Adversary gets pk and a signing oracle; outputs (m\*, σ\*).
**EUF-CMA** (existential unforgeability): wins if σ\* verifies and **m\*** was
never queried. **SUF-CMA** (strong): wins if σ\* verifies and **(m\*, σ\*)** was
never returned — so producing a *different valid signature on an already-signed
message* is a break.

**Obligations.**
- [ ] EUF or SUF stated — the difference is precisely whether signature
      re-randomisation counts as a break
- [ ] Signing-query budget q_S appears in the bound
- [ ] For Fiat–Shamir constructions: which forking/rewinding argument, and its
      loss factor. In the **QROM** the classical forking lemma does not apply.
- [ ] For hash-and-sign: which hash notion the reduction needs
      ([`hash.md`](hash.md)) — usually
      collision resistance, sometimes only second-preimage

```
SUF-CMA  ⟹  EUF-CMA      (strict — the converse fails for any
                           scheme with re-randomisable signatures)
```

**Operational break.** Produce a verifying (m\*, σ\*) outside the query set at
toy parameters. For SUF specifically, take a signed (m, σ) and attempt to derive
σ′ ≠ σ that also verifies — cheap, and it catches re-randomisability immediately.

### Stateful hash-based signatures

LMS and XMSS (SP 800-208) carry an obligation no other signature scheme does:

- [ ] **State is never reused.** One-time-key reuse is catastrophic and total,
      not gradual. Any argument about these schemes that does not address state
      management is incomplete regardless of its cryptographic content.

---
