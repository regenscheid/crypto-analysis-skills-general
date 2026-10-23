# Attack families: multivariate and code-based

Historical environment observations and timings below describe earlier runs.
They do not establish software availability, current versions, or measured
behavior in this session. Confirm the actual runtime before using its outputs.


UOV, MQ, MinRank, Permuted Kernel, and Linear Equivalence. Load this checklist
for the multivariate/code-family coverage phase of `analyze-scheme`. It is a
companion to `lattice.md`; the same rule applies:

> **Walk every family. Check each family's preconditions *before* running it.
> Report the cheapest, not the familiar one.**

## Why this domain punishes the familiar answer hardest

The obvious algebraic attack on an MQ system is a Gröbner basis — **F5**. On an
ov-Ip-shaped system (n=112, m=44, q=256), measured on this machine:

| Family | cost | |
|---|---|---|
| **PXL** | **2^134.5** | cheapest |
| BooleanSolveFXL | 2^144.5 | |
| Crossbred | 2^153.2 | |
| HybridF5 | 2^167.8 | |
| Hashimoto | 2^177.2 | *underdetermined systems only* |
| **F5** | **2^243.0** | **the obvious one** |

**F5 is 108 bits worse than the cheapest family.** Running the obvious algebraic
attack and reporting its cost would overstate security by more than a hundred
bits — the largest gap between the familiar answer and the right one anywhere in
these checklists. For comparison, the same failure costs 4 bits on ML-KEM-512 and
17–20 bits on UOV at the scheme level.

Consistency check worth knowing: `UOVEstimator`'s `DirectAttack` on ov-Ip returns
**2^134.5**, exactly matching `MQEstimator`'s PXL. The scheme-level estimator is
driving the problem-level one and already picks the best family — so *use the
scheme estimator where one exists*, and drop to `MQEstimator` only when analysing
a raw system or a scheme with no dedicated estimator.

---

## Scheme level: `UOVEstimator`

Five families. Measured on the NIST UOV submission parameter sets:

| | ov-Is (q=16) | ov-Ip (q=256) | ov-III | ov-V |
|---|---|---|---|---|
| DirectAttack | 2^158.5 | **2^134.5** | 2^214.1 | 2^276.8 |
| KipnisShamir | 2^152.5 | 2^217.1 | 2^347.1 | 2^444.2 |
| CollisionAttack | **2^141.0** | 2^189.3 | 2^301.6 | 2^397.8 |
| IntersectionAttack | 2^175.0 | 2^164.6 | 2^248.9 | 2^310.5 |
| WedgeAttack | 2^174.8 | 2^139.6 | **2^205.9** | **2^256.7** |

**The cheapest family changes with the parameter set** — Collision at q=16,
Direct at ov-Ip, Wedge at both high levels. Running only DirectAttack overstates
ov-Is by 17.5 bits and ov-V by 20.1 bits.

- **`DirectAttack`** — solve the public system directly. Delegates to the MQ
  families below. *Bites when* m is small relative to n.
- **`KipnisShamir`** — exploits the oil-subspace structure. *Bites when* the
  oil/vinegar split is unbalanced; note it is worst at large q here.
- **`CollisionAttack`** — birthday-style. *Bites when* **q is small** — it wins
  at q=16 and loses badly at q=256. Memory-hungry: 2^131.7 memory at ov-Is.
      **Check the memory column before calling it the cheapest attack.**
- **`IntersectionAttack`** — Beullens. *Bites when* n/m is close to 2.
- **`WedgeAttack`** — recent; wins at the high security levels. Its presence is
  why this list must be regenerated when the library updates: a new family can
  silently become the cheapest.

**Cost:** `UOVEstimator.estimate()` over those four sets took **4m06s**. Do not
run it on every parameter set by reflex.

---

## Problem level: `MQEstimator`

14 families, and **most are field- or shape-restricted**. Preconditions below
were established by running each in isolation, not recalled.

### Field restrictions — established empirically

| Family | q=2 | q=256 |
|---|---|---|
| `Bjorklund` | 2^62.7 | **not offered** |
| `DinurFirst` | 2^54.8 | **not offered** |
| `DinurSecond` | **2^45.4** (cheapest at q=2) | **not offered** |
| `Lokshtanov` | 2^88.8 | **crashes** — `ValueError: math domain error` |
| `PXL`, `BooleanSolveFXL`, `Crossbred`, `HybridF5`, `F5`, `ExhaustiveSearch` | ✓ | ✓ |

- **`Bjorklund`, `DinurFirst`, `DinurSecond` are Boolean-only.** They are the
  right families for a q=2 system and simply absent otherwise.
- **`Lokshtanov` raises rather than returning inf at large q.** Catch it; the
  exception is the precondition. Do not let it abort a sweep.
- **The ranking inverts with q.** At q=2 the order is DinurSecond <
  ExhaustiveSearch < HybridF5 < Crossbred < BooleanSolveFXL < PXL. At q=256 it
  is PXL < BooleanSolveFXL < Crossbred < HybridF5 < F5 < ExhaustiveSearch.
  **A family ranking carried over from a Boolean instance is wrong at q=256.**

### Shape restrictions

`CGMTA`, `KPG`, `MHT`, `Hashimoto` are offered only for particular m-to-n
relationships.

- **`Hashimoto` appears only when the system is underdetermined.** Present at
  n=112, m=44 (2^177.2); **not offered** at n=m=44. Since a UOV public map *is*
  underdetermined, this family is live for UOV-like schemes and dead for square
  systems.
- `CGMTA`, `KPG`, `MHT` were not offered at either shape tested. Their conditions
  are narrower still — do not assume absence means inapplicability in general,
  only that it was inapplicable here.

### Running it

```python
from cryptographic_estimators.MQEstimator import MQEstimator
from cryptographic_estimators.MQEstimator.mq_algorithm import MQAlgorithm
ALL = {c.__name__: c for c in MQAlgorithm.__subclasses__()}

# excluded_algorithms takes CLASSES, not names -- passing strings raises
# "TypeError: issubclass() arg 1 must be a class"
E = MQEstimator(n=112, m=44, q=256)
for name, d in sorted(E.estimate().items(), key=lambda kv: kv[1]["estimate"]["time"]):
    print(name, "2^%.1f" % d["estimate"]["time"])
```

### ⚠ Report the memory-access spread — the multivariate analogue of the cost model

`lattice.md` mandates a cost-model spread and this file had no equivalent, which
was a real gap. `cryptographic_estimators` takes a `memory_access` parameter, and
on **ov-Ip** the cheapest cost moves:

| `memory_access` | cheapest |
|---|---|
| 0 — constant | 2^134.5 |
| 1 — logarithmic | 2^138.3 |
| 3 — cube-root | 2^166.8 |
| 2 — square-root | **2^184.4** |

**A 50-bit spread, and it flips the category-1 verdict.** Reporting 2^134.5 alone
is the multivariate equivalent of reporting a bare λ. `sweep.py` now prints all
four rows.

**Report memory as well as time.** Several of these are memory-bound;
`CollisionAttack` at ov-Is needs 2^131.7. A time-cheapest attack that needs more
memory than atoms in the observable universe is not the cheapest attack.

---

## MinRank — `MREstimator`

`SupportMinors`, `KernelSearch`, `BigK`, `Minors`, `BruteForce`.

Load-bearing for the Rainbow break ([2022/214](https://eprint.iacr.org/2022/214),
Beullens, *Breaking Rainbow Takes a Weekend on a Laptop*) and for MiRitH. *Bites
when* a scheme's public map has low-rank structure — which is what every
oil-and-vinegar trapdoor is. **This is the family `UOVEstimator` cannot reach**,
and its absence is why the blind regression's Rainbow arms could not close their
own finding with a measurement.

**Now wired up**: `sweep.py minrank q= m= n= k= r=`. Verified on a small instance
(q=16, m=n=15, k=78, r=6): BruteForce 2^143.8, SupportMinors 2^144.0,
Minors 2^144.7, KernelSearch 2^147.7, BigK 2^154.7.

`MRProblem(q, m, n, k, r)` — m×n matrices, a k-dimensional span, target rank r.

**Two honest limits.**

*The scheme → MinRank reduction is not automated, deliberately.* Deriving
(q,m,n,k,r) from a scheme's parameters **is** the attack, it differs per scheme,
and an unverified mapping is worse than none. For Rainbow the reduction is: for
x ∈ O₂ the first o₁ columns of M_x = [P₁x | … | P_mx] vanish, so
rank(M_x) ≤ m − o₁, giving a rectangular MinRank instance over the span of the
M_i. State your reduction, then pass the instance.

*It is slow at cryptographic sizes.* A k=100, r=32 instance — Rainbow-I's shape —
**ran past 10 minutes without returning**, where the whole four-set UOV sweep
takes 4m06s. Budget for it, and expect to background it.

Newer literature worth reading before trusting an old mapping:
[2025/739](https://eprint.iacr.org/2025/739) extends the rectangular MinRank
attack to UOV and its variants.

## Permuted Kernel — `PKEstimator`

`KMP`, `SBC`. Underlies **PERK**.

## Linear Equivalence — `LEEstimator`

`Leon`, `Beullens`, `BBPS`. Underlies **LESS**. Note this reference set and the ePrint
connector both record that "LESS" collides with the English word in search, which
is why the corpus expands it as a domain acronym rather than a plain token.

Both enumerated from the API; **costs not measured here.**

---

## The Magma dependency, and why it is real

Everything above is *estimation*. Actually **running** an algebraic attack —
computing a Gröbner basis to check a claimed degree of regularity, or solving a
small instance end-to-end for `validate-attack` — bottoms out in a Gröbner
engine, and **Magma's F4 is materially faster than Sage's route through
Singular** on large systems over F_q.

That is the justification for using the optional remote Magma host through the
`magma` skill.
Without it:

- **Estimation** works fully, locally, today — this file.
- **Verification of a degree-of-regularity claim** does not. Do not assert that a
  system behaves semi-regularly without computing it; record it as unverified.

---

## Verification status

Measured on this machine, `cryptographic_estimators` 2.1.1 in the original recorded `sage` env: the five UOV families across four NIST parameter sets; MQ
family applicability at q=2 and q=256; MQ family costs at n=m=44 and at n=112,
m=44; the `Lokshtanov` crash; the `Hashimoto` underdetermined-only behaviour.

**Not measured:** MinRank, PKP and LESS costs — families enumerated from the API
only. `RSDEstimator` could not be enumerated the same way (submodule path differs
from the others); it exists and imports, but its family list is unconfirmed.
