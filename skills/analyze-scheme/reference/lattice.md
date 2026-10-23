# Attack families: lattice (LWE, NTRU, SIS)

Historical environment observations and timings below describe earlier runs.
They do not establish software availability, current versions, or measured
behavior in this session. Confirm the actual runtime before using its outputs.


Load this checklist for the lattice-family coverage phase of `analyze-scheme`.

## The rule this file exists to enforce

> **Walk every family. Check each family's preconditions *before* running it.
> Report the cheapest, not the familiar one.**

Both halves are load-bearing, and each targets a measured failure.

**Walking every family** prevents pattern matching from replacing analysis.
Measured on ML-KEM-512 with `RC.MATZOV`:

| Family | cost | |
|---|---|---|
| `dual_hybrid` | **2^139.7** | cheapest |
| `primal_bdd` | 2^140.2 | |
| `primal_usvp` | 2^143.8 | **the one usually quoted** |
| `dual` | 2^149.9 | |
| `coded_bkw` | 2^178.8 | |
| `primal_hybrid` | 2^262.1 | |

Quoting `primal_usvp` alone overstates security by **4 bits**. That is small
here and is not always small — the same check on UOV moved ov-Is and ov-V by
17–20 bits (`multivariate.md`, when written).

**Checking preconditions first** targets class 3's other half: firing an attack
without verifying its hypotheses hold. In this domain the estimator will often
tell you — but only if you read the exception instead of catching it.

---

## How to read an entry

- **Applies when** — the precondition. Check before running, not after.
- **Fails how** — what you see when it does not apply. Several of these surface
  as exceptions, and an exception is a *result*, not an error to be swallowed.
- **Call** — the `lattice-estimator` invocation.
- **Bites when** — the structural deviation that makes this family the winner.
  This is the `analyze-scheme` step-6 hook.

Every cost below is `RC.MATZOV` unless stated. **Never report a bare λ** — see
"Cost models" at the end.

---

## Primal attacks

### `primal_usvp` — unique-SVP embedding

- **Applies when** always, for LWE with a unique/bounded solution. The default
  baseline.
- **Fails how** n/a.
- **Call** `LWE.primal_usvp(params, red_cost_model=RC.MATZOV)`
- **Bites when** nothing special — it is the floor everyone quotes, which is
  exactly why it must not be the only one run.

Returns β (BKZ blocksize) and d (lattice dimension) alongside the cost. β is the
number to sanity-check against published figures: ML-KEM-512/768/1024 give
**β = 406 / 624 / 874**.

### `primal_bdd` — bounded-distance decoding

- **Applies when** always. Uses a Babai/Nearest-Plane step after reduction, so it
  can beat uSVP when the embedding wastes the error's structure.
- **Fails how** n/a.
- **Call** `LWE.primal_bdd(params, red_cost_model=RC.MATZOV)`
- **Bites when** the secret and error distributions differ, or the error is small
  relative to q. On ML-KEM-512 it beats `primal_usvp` (2^140.2 vs 2^143.8) —
  **so the "standard" primal number is already not the cheapest primal attack.**

### `primal_hybrid` — meet-in-the-middle guessing plus reduction

- **Applies when** the secret is **sparse or small-support**. Guessing part of
  the secret only pays if guessing is cheap.
- **Fails how** it does not throw — it silently returns a much *worse* number.
  On ML-KEM-512 (centred binomial, dense secret) it gives **2^262.1**, ~120 bits
  worse than uSVP. A large `primal_hybrid` result is evidence the precondition is
  absent, not evidence of security.
- **Call** `LWE.primal_hybrid(params, red_cost_model=RC.MATZOV)`
- **Bites when** the scheme uses **sparse ternary secrets**, fixed Hamming
  weight, or small-support distributions — common in FHE parameter sets and in
  some NTRU variants. If a design chose a sparse secret for performance, this is
  the family that punishes it.

### `primal_dsd` — dense sublattice discovery *(NTRU only)*

- **Applies when** NTRU with a **large modulus relative to n** — the
  "overstretched" regime.
- **Fails how** absent from `LWE`; only exposed on `NTRU`.
- **Call** `NTRU.primal_dsd(params, red_cost_model=RC.MATZOV)`
- **Bites when** q is pushed up to reduce decryption failures or to support
  homomorphic depth. This is the attack that killed overstretched-NTRU
  constructions, and **the deviation that triggers it is a parameter choice made
  for performance, not for security** — precisely the step-6 pattern.

Sources: [2018/630](https://eprint.iacr.org/2018/630) De Micheli, Heninger,
Shani, *Characterizing overstretched NTRU attacks*; and for the current limits of
the technique, [2025/1694](https://eprint.iacr.org/2025/1694) Ducas, Loyer,
*Lattice Reduction via Dense Sublattices: A Cryptanalytic No-Go*.

---

## Dual attacks

### `dual` and `dual_hybrid`

- **Applies when** always for `dual`; `dual_hybrid` additionally guesses secret
  coordinates and so benefits from small/sparse secrets — but note it still won
  on ML-KEM-512's dense secret.
- **Fails how** n/a.
- **Call** `LWE.dual(p, red_cost_model=RC.MATZOV)` /
  `LWE.dual_hybrid(p, red_cost_model=RC.MATZOV)`
- **Bites when** the sample count m is generous, or the secret is small. On
  ML-KEM-512 `dual_hybrid` is **the cheapest family of all nine at 2^139.7**.

### ⚠ The dual-attack caveat — do not report a dual number bare

The cost model for dual-sieve attacks is **actively disputed**, and this is the
single most important caveat in this file.

[2023/302](https://eprint.iacr.org/2023/302) — Ducas, Pulles, *Does the
Dual-Sieve Attack on Learning with Errors even Work?* — argues that the standard
heuristic analysis of dual-sieve attacks is contradicted by experiment, so
published dual costs may not reflect attainable attacks.
[2023/1508](https://eprint.iacr.org/2023/1508) — Pouly, Shen, *Provable Dual
Attacks on Learning with Errors* — responds with provable variants. The
literature has continued to move.

**Obligations when a dual attack is the cheapest family:**
- [ ] Say so, and say that the dual cost model is disputed — cite 2023/302
- [ ] Report the cheapest **primal** cost alongside it, as the defensible number
- [ ] Do not let a dual number alone drive a "broken" claim without a
      corroborating primal result or an implementation

This matters directly for the table above: `dual_hybrid` beats `primal_usvp` by
4 bits on ML-KEM-512, and that 4 bits sits inside the disputed region.

---

## Algebraic and combinatorial families

### `arora_gb` — Arora–Ge

- **Applies when** the noise is **very small and bounded** — essentially, when
  the error takes few values.
- **Fails how** on ML-KEM-512 it raises `int too large to convert to float` —
  the cost overflows a double. **That exception is the answer**: the family is
  astronomically inapplicable at binomial noise. Catch it, report "inapplicable
  (cost overflow)", and do not let it abort the sweep.
- **Call** `LWE.arora_gb(params)`
- **Bites when** a design uses a **bounded, low-entropy error** — binary or
  ternary error, or an error distribution truncated for implementation
  convenience. That is a classic performance-motivated deviation.

### `coded_bkw`

- **Applies when** **many samples** are available — BKW-family attacks are
  sample-hungry.
- **Fails how** returns a large number rather than throwing when m is tight.
  2^178.8 on ML-KEM-512.
- **Call** `LWE.coded_bkw(params)`
- **Bites when** the scheme exposes unlimited samples — a key-reuse or
  many-ciphertext setting rather than the m = n of a KEM.

### `mitm` and `exhaustive_search`

- **Applies when** enough samples exist. Both state their requirement precisely.
- **Fails how** explicit, useful exceptions:
  - `mitm` → `MITM: Need 728 samples but only 512 available.`
  - `exhaustive_search` → `Need 8012.8 samples`
  **Record the requirement and the shortfall** — "needs 728, has 512" is a more
  informative line in a report than "not applicable".
- **Bites when** m is unbounded, or n is small enough that brute force is real
  (toy parameters, and the reduced-parameter ladders used by `validate-attack`).

---

## SIS

`SIS.Parameters(n, q, length_bound, m=None, norm=2, tag=None)`. Distinct from
LWE: the governing quantity is the norm bound β relative to q and the dimensions.

Two families:

### `SIS.lattice`
- **Applies when** always. The standard lattice-reduction attack.
- **Call** `SIS.lattice(params)`

### `SIS.large_norm`
- **Applies when** the norm bound is **large relative to q** — there is a regime
  where the bound is loose enough that a different approach wins.
- **Fails how** returns **`2^inf`** rather than throwing. Measured on an ML-DSA-44
  shaped instance (n=1024, q=8380417, β=350209, m=2048): `lattice` gives
  **2^263.9** while `large_norm` gives **2^inf** — inapplicable at that bound.
  An `inf` here is a precondition failure, not a security result, and must not be
  reported as "no attack found".

**Obligation: check which norm the claim is in.** `norm` defaults to **2**; ℓ∞
bounds are extremely common in signature schemes (ML-DSA states its bounds in
ℓ∞). Estimating an ℓ∞ bound under the ℓ₂ default silently answers a different
question, and nothing in the output flags it.
- [ ] `norm` set to match the specification's bound
- [ ] β taken from the spec, not inferred from a related parameter

---

## Running the whole sweep

`LWE.estimate(params)` runs everything, but three families throw rather than
return on typical KEM parameters, so a naive loop aborts partway. Catch per
family and record the exception text as the applicability finding:

```python
from estimator import *
import math
p = LWE.Parameters(n=512, q=3329, Xs=ND.CenteredBinomial(3),
                   Xe=ND.CenteredBinomial(3), m=512)
FAMILIES = ["primal_usvp", "primal_bdd", "primal_hybrid",
            "dual", "dual_hybrid", "arora_gb", "coded_bkw",
            "mitm", "exhaustive_search"]
for name in FAMILIES:
    fn = getattr(LWE, name)
    try:
        r = fn(p, red_cost_model=RC.MATZOV) if name.startswith(("primal", "dual")) else fn(p)
        print(name, "2^%.1f" % math.log2(float(r["rop"])))
    except Exception as exc:                 # the exception IS the precondition
        print(name, "inapplicable:", exc)
```

**It is slow.** The UOV sweep took 4m06s for four parameter sets; budget
accordingly and do not run every family on every parameter set by reflex.

---

## Cost models — never report a bare λ

`RC` exposes: `ADPS16`, `BDGL16`, `MATZOV`, `CheNgu12`, `ABLR21`, `ABFKSW20`,
`ChaLoy21`, `GJ21`, `Kyber`, `LaaMosPol14`, `LLL`.

Same instance, same β, different model:

| Model | ML-KEM-512 | 768 | 1024 |
|---|---|---|---|
| `ADPS16` — core-SVP, classical | 2^118.6 | 2^182.2 | 2^255.2 |
| `MATZOV` — 2022 gate-count refinement | 2^143.8 | 2^204.9 | 2^275.1 |
| `BDGL16` — sieve, gate count | 2^147.9 | 2^212.1 | 2^285.5 |
| `CheNgu12` — enumeration | 2^280.8 | 2^485.4 | 2^745.3 |

**25 bits** between two defensible sieving models; 160+ across the table.
`CheNgu12` prices a different algorithm family (enumeration, not sieving) and is
not apples-to-apples with the rest.

**Obligations for any reported cost:**
- [ ] Model named
- [ ] Spread reported where models disagree materially
- [ ] `ADPS16` given when comparing against a NIST submission's own claim, since
      core-SVP is the convention those are stated in
- [ ] Estimator commit recorded — these measurements used
      `lattice-estimator` at `3e48ef42`
- [ ] Sage and Python versions printed with the result

---

## Verification status

Every number in this file was produced on this machine with
`lattice-estimator` @ `3e48ef42` in the original recorded SageMath environment
(SageMath 10.7), not recalled. The β values 406/624/874 and the ADPS16 row
reproduce the ML-KEM submission's published core-SVP figures.

SIS was exercised too: an ML-DSA-44-shaped instance gives `lattice` 2^263.9 and
`large_norm` 2^inf, which is where the `large_norm` precondition above comes from.

**Not verified here:** `primal_dsd` has not been run against a real overstretched
NTRU parameter set — the family and its trigger are documented from the cited
sources, not from a measurement on this machine. Marked rather than implied.
