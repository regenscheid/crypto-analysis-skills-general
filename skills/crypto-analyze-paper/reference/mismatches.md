# Mismatches to detect

> Part of `crypto-analyze-paper`'s security-definitions reference. The framing that
> governs every file here — including the rule that these are **obligations to
> discharge, not prose to cite** — is in [`README.md`](README.md), and the
> shared advantage/query conventions and proof models are in
> [`conventions.md`](conventions.md). Read those first.

## Mismatches to detect

The checklist `crypto-analyze-paper` should run. Each is a real, recurring finding.

- [ ] **Proof gives IND-CPA, claim says IND-CCA2** — the commonest of all
- [ ] **EUF-CMA proved, SUF-CMA claimed** (or the scheme is re-randomisable and
      the distinction is never raised)
- [ ] **ROM proof presented as standard-model**
- [ ] **PQC scheme with ROM-only proof and no QROM discussion**
- [ ] **Collision resistance assumed where the reduction only needs second
      preimage** — or, worse, the reverse
- [ ] **Birthday bound applied to a preimage claim** (2^(n/2) where 2^n is right)
- [ ] **Advantage convention switched** between a cited bound and the paper's own
- [ ] **q_H / q_S / q_D missing** from a concrete bound
- [ ] **Asymptotic proof supporting a concrete parameter claim**
- [ ] **Reduction loss not carried into the claimed security level**
- [ ] **AEAD claim with no nonce-misuse statement**
- [ ] **Category claim under a single metric**

---
