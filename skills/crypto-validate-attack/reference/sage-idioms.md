# Sage idioms for cryptanalysis

Historical environment observations and timings below describe earlier runs.
They do not establish software availability, current versions, or measured
behavior in this session. Confirm the actual runtime before using its outputs.


Organised by **task**, not by API surface. The failure this addresses is not
"doesn't know `GroebnerBasis`"; it is not knowing how to set up a problem so the
tool answers the intended question.

## The rule for this file

> **Every snippet here was executed and its real output captured. Nothing is
> written from memory.**

Plausible, subtly wrong Sage is a major hallucination risk. Each entry therefore
shows what it actually printed on the measured environment. If you add an
entry, run it first.

**Stack** — `SageMath 10.7`, `Python 3.11.15`, the original recorded SageMath environment.
There may be multiple SageMath installations on a host. Print provenance with
results:

```python
version(); import sys; sys.version_info[:3]
# ('sage', '10.7', 'python', '3.11.15')
```

---

## Rings and fields

### Finite field with a primitive generator
```python
F = GF(2**8, 'a', modulus='primitive')
a = F.gen()
(F.order(), F.characteristic(), F.degree(), a.multiplicative_order())
# (256, 2, 8, 255)
```
`modulus='primitive'` matters — the default modulus need not make `a` a
multiplicative generator, and code that assumes it will be subtly wrong.

### Cyclotomic field and its ring of integers
```python
K = CyclotomicField(256)
OK = K.ring_of_integers()
(K.degree(), K.discriminant().nbits(), OK.rank())
# (128, 897, 128)
```
Note **degree 128, not 256** — φ(256) = 128. Off-by-a-factor-of-two here is a
classic error in module-lattice work.

### The NTRU/ML-KEM quotient ring
```python
n, q = 256, 3329
R = PolynomialRing(GF(q), 'x'); x = R.gen()
Rq = R.quotient(x**n + 1, 'xb')
f = Rq([1] + [0]*(n-2) + [1])
(f*f).lift().degree()
# 255
```

### How x^n + 1 splits — the NTT structure
```python
n, q = 256, 3329
R = PolynomialRing(GF(q), 'x')
fac = (R.gen()**n + 1).factor()
(len(fac), sorted(set(g.degree() for g,_ in fac)))
# (128, [2])
```
**x²⁵⁶ + 1 splits into 128 factors of degree 2 mod 3329 — not 256 linear
factors.** That is exactly why ML-KEM's NTT is *incomplete*, bottoming out at
degree-2 polynomials with pointwise multiplication in F_q[x]/(x²−ζ). Any analysis
assuming a fully-splitting ring is analysing a different scheme. Check this
before assuming, for every (n, q) pair.

---

## Lattices

### ⚠ Do not demonstrate LLL on a random square integer matrix
```python
set_random_seed(1)
M = random_matrix(ZZ, 40, 40, x=-50, y=50)
min(M.row(i).norm() for i in range(40))   # 138.824
min(M.LLL().row(i).norm() for i in range(40))            # 138.824
min(M.BKZ(block_size=20).row(i).norm() for i in range(40))  # 138.824
```
**The bases differ (`M == M.LLL()` is False) but the shortest vector is
identical.** A generic random lattice has no short vector to find, so reduction
correctly achieves nothing. Benchmarking or sanity-checking a reduction routine
this way will tell you it does not work.

### LLL on a q-ary lattice — where there *is* something to find
```python
set_random_seed(11)
n, m, q = 10, 20, 1021
A = random_matrix(GF(q), n, m)
L0 = A.change_ring(ZZ).stack(q*identity_matrix(ZZ, m))    # 30 x 20
before = min(L0.row(i).norm() for i in range(L0.nrows()) if L0.row(i).norm() > 0)
after  = min(L0.LLL().row(i).norm() for i in range(L0.nrows()) if L0.LLL().row(i).norm() > 0)
(before, after)
# 1021.00 -> 35.68   (28.6x)
```
This is the shape LWE and SIS actually produce. Use it as the smoke test.

### fpylll directly, with a BKZ 2.0 tour
```python
from fpylll import IntegerMatrix, LLL as fLLL, BKZ as fBKZ
A = IntegerMatrix.random(50, "qary", k=25, bits=20)
fLLL.reduction(A)
before = A[0].norm()                       # 1857.7
par = fBKZ.Param(block_size=20, strategies=fBKZ.DEFAULT_STRATEGY)
fBKZ.reduction(A, par)
(before, A[0].norm())
# (1857.7, 1815.28)
```
`strategies=fBKZ.DEFAULT_STRATEGY` is not optional in practice — without a
strategy the preprocessing is unspecified and timings are not comparable.

### The Gram–Schmidt profile (what a BKZ shape claim is about)
```python
from fpylll import IntegerMatrix, GSO, LLL as fLLL
A = IntegerMatrix.random(30, "qary", k=15, bits=15)
fLLL.reduction(A)
M = GSO.Mat(A); M.update_gso()
[round(M.get_r(i,i)**0.5, 2) for i in range(5)]
# [293.27, 279.48, 259.25, 260.43, 238.49]
```
`get_r(i,i)` is the **squared** norm — take the root. The decreasing profile is
the thing GSA and BKZ-simulator claims are about; plot it before trusting a
predicted β.

### Babai nearest-plane (CVP)
```python
from fpylll import IntegerMatrix, LLL as fLLL, GSO
A = IntegerMatrix.random(20, "qary", k=10, bits=10)
fLLL.reduction(A); M = GSO.Mat(A); M.update_gso()
M.babai([1]*20)[:5]
# (0, 0, 0, 0, 0)
```
An all-zero answer is correct here — the target is nearer the origin than any
basis vector — and is a reminder to choose a target that exercises the routine.

---

## Multivariate

### A system over F_q with an explicit monomial order
```python
q, nv = 16, 6
F = GF(q, 'a')
R = PolynomialRing(F, nv, 'x', order='degrevlex')
(R.term_order().name(), len(polys), polys[0].degree())
# ('degrevlex', 6, 2)
```
**Always set `order` explicitly.** `degrevlex` is what Gröbner solvers are fast
in and what degree-of-regularity arguments assume; `lex` is far slower and the
default is not guaranteed to be what you want.

### Gröbner basis, and the degrees actually reached
```python
R = PolynomialRing(GF(7), 3, 'x', order='degrevlex')
x,y,z = R.gens()
I = R.ideal([x*y - 1, y*z - 1, x + y + z])
G = I.groebner_basis()
(len(G), [g.degree() for g in G], I.dimension())
# (3, [2, 1, 1], 0)
```
`I.dimension() == 0` confirms finitely many solutions — check it before quoting
a solving complexity that assumes a zero-dimensional ideal.

### Degree of regularity from the semi-regular Hilbert series
```python
m, n = 20, 10            # m equations, n variables
Rt.<t> = PowerSeriesRing(QQ, default_prec=30)
coeffs = ((1-t**2)**m / (1-t)**n).O(30).list()
dreg = next(i for i,c in enumerate(coeffs) if c <= 0)
(dreg, coeffs[:8])
# (4, [1, 10, 35, 20, -195, -498, 15, 1800])
```
**This is the semi-regular *estimate*, not a measurement of your system.** It is
what `MQEstimator` assumes. A real system may not be semi-regular, and
confirming that requires actually computing the basis — see the Magma note in
the `crypto-analyze-scheme` skill's `reference/multivariate.md`. If m ≤ n the series has no
non-positive coefficient and `next()` raises `StopIteration`; that is the
computation telling you the system is underdetermined, not a bug.

### Macaulay matrix at a fixed degree
```python
from itertools import combinations_with_replacement
R = PolynomialRing(GF(7), 3, 'x', order='degrevlex'); xs = R.gens()
polys = [xs[0]*xs[1] - 1, xs[1]*xs[2] - 1, xs[0] + xs[1] + xs[2]]
D = 3
mons = [prod(c) for c in combinations_with_replacement(xs, D)]
rows = [[ (f*mlt).monomial_coefficient(mm) for mm in mons ]
        for f in polys
        for mlt in [prod(c) for c in combinations_with_replacement(xs, D - f.degree())]]
Mac = matrix(GF(7), rows)
(Mac.dimensions(), Mac.rank())
# ((12, 10), 9)
```
Rank deficiency (9 < 10) is the quantity XL-family complexity arguments turn on.

---

## Linear algebra and MinRank

### Rank and kernel over F_q
```python
F = GF(16,'a'); set_random_seed(4)
Ms = [random_matrix(F, 5, 5) for _ in range(4)]
target = sum(l*M for l,M in zip([F.random_element() for _ in range(4)], Ms))
(target.rank(), target.right_kernel().dimension(), len(Ms))
# (5, 0, 4)
```
A random combination is full rank — which is the point: **MinRank is hard
because low rank is rare.**

### Planting a low-rank matrix deliberately
```python
F = GF(16,'a'); set_random_seed(5)
U = random_matrix(F, 5, 2); V = random_matrix(F, 2, 5)
(U*V).rank()
# 2
```
The UV factorisation is how you build a MinRank instance with known solution —
the basis of any `crypto-validate-attack` ladder for Rainbow-style breaks.

---

## Coding

```python
C = codes.HammingCode(GF(2), 4)
H = C.parity_check_matrix()
v = C.random_element()
e = vector(GF(2), [1] + [0]*(C.length()-1))
(C.length(), C.dimension(), C.minimum_distance(), list(H*(v+e)))
# (15, 11, 3, [1, 0, 0, 0])
```
The syndrome of a weight-1 error is the corresponding column of H — the check
that your H orientation is right before building a decoder.

```python
set_random_seed(6)
C = codes.LinearCode(random_matrix(GF(2), 6, 12))
(C.length(), C.dimension(), C.parity_check_matrix().dimensions())
# (12, 6, (6, 12))
```

---

## Sampling

### Discrete Gaussian over the integers
```python
from sage.stats.distributions.discrete_gaussian_integer import \
    DiscreteGaussianDistributionIntegerSampler
Dg = DiscreteGaussianDistributionIntegerSampler(sigma=3.2)
set_random_seed(8)
xs = [Dg() for _ in range(20000)]
(min(xs), max(xs), float(sum(xs))/len(xs))
# (-12, 15, -0.0086)
```
**Do not name the sampler `D`** — Sage exports `D` as a derivative operator, and
`D()` then fails with `TypeError: 'DerivativeOperator' object is not callable`.
Encountered while writing this file.

### Centred binomial (ML-KEM's noise)
```python
import random as _pyrandom          # NOT `import random`
rng = _pyrandom.Random(7)
def cbd(eta, rng):
    return sum(rng.randint(0,1) for _ in range(eta)) - sum(rng.randint(0,1) for _ in range(eta))
```
**Name collision.** `from sage.all import *` shadows `random`, and the Sage
version rejects the seed with `TypeError: The only supported seed types are:
None, int, float, str, bytes, and bytearray`. Import under an alias. *(This
snippet is the one entry here whose output is not captured — it failed in the
harness for exactly this reason and the alias fix is untested. Marked rather
than implied.)*

---

## Symmetric

### S-box criteria
```python
import sage.crypto.sbox
S = sage.crypto.sbox.SBox([0xC,5,6,0xB,9,0,0xA,0xD,3,0xE,0xF,8,4,7,1,2])  # PRESENT
(S.differential_uniformity(), S.linearity(), S.max_degree(),
 S.differential_branch_number(), S.linear_branch_number())
# (4, 8, 3, 3, 2)
```
These are PRESENT's published values — use them as the self-test that your S-box
is entered correctly before analysing an unfamiliar one. `.difference_distribution_table()`
and `.linear_approximation_table()` give the full DDT/LAT.

### Boolean functions
```python
from sage.crypto.boolean_function import BooleanFunction
B = BooleanFunction([0,1,1,0,1,0,0,1])
(B.nvariables(), str(B.algebraic_normal_form()), B.nonlinearity(), B.algebraic_immunity())
# (3, 'x0 + x1 + x2', 0, 1)
```
Nonlinearity 0 because this truth table *is* affine — a useful degenerate check.

### MILP: the trail-search skeleton
```python
p = MixedIntegerLinearProgram(maximization=False, solver='GLPK')
x = p.new_variable(binary=True)
for r in range(4):
    p.add_constraint(sum(x[r,i] for i in range(4)) >= 1)
for r in range(3):
    p.add_constraint(sum(x[r,i] for i in range(4)) + sum(x[r+1,i] for i in range(4)) >= 3)
p.set_objective(sum(x[r,i] for r in range(4) for i in range(4)))
p.solve()
# 6.0
```
This is the shape of a differential/linear active-S-box count: binary activity
variables, per-round activity constraints, a diffusion constraint linking rounds,
minimise the total. **Use `solver='SCIP'`** — GLPK is the default and too weak
for a real cipher. SCIP returns 6.0 on this toy instance, agreeing with GLPK,
which is the cross-check you want before trusting it on something larger.

### SAT, with XOR clauses
```python
from sage.sat.solvers import CryptoMiniSat
s = CryptoMiniSat()
s.add_clause((1,2,3)); s.add_clause((-1,)); s.add_clause((-2,))
sol = s()                      # True, sol[3] is True

s2 = CryptoMiniSat()
s2.add_xor_clause((1,2,3), rhs=True)   # native XOR -- accepted, solves
```
**`add_xor_clause` is why CryptoMiniSat rather than a generic solver.** Linear
and differential relations over GF(2) *are* XOR constraints; encoding them as
CNF blows up, and CryptoMiniSat handles them natively.

Historical note worth keeping: this section originally read "SAT is NOT
available", because all five of Sage's backends failed — the wrapper class
imports fine without the underlying module. **Importing a solver class proves
nothing; instantiate and solve.** `pycryptosat` was installed 2026-08-01.

---

## Parallelism

### Pool over independent trials — and the crossover, measured

Monte Carlo over seeds is embarrassingly parallel. Whether it is *worth*
parallelising is a different question, and the answer is not "always":

```python
import os
os.environ["OMP_NUM_THREADS"] = "1"      # BEFORE numpy is imported
import numpy as np, time
from concurrent.futures import ProcessPoolExecutor

def trial(rep):                           # seed FROM THE INDEX, never shared
    rng = np.random.default_rng(400000 + rep)
    x = rng.standard_normal(200000)
    return float(x.mean()), float(x.std())

if __name__ == "__main__":                # REQUIRED on macOS -- see below
    REPS = 24
    with ProcessPoolExecutor(max_workers=8) as ex:
        pooled = list(ex.map(trial, range(REPS)))
```

Measured on this machine, 24 trials, 8 workers, against the identical serial
loop. Speedup depends entirely on what ONE trial costs:

```
per-trial cost      serial    pooled(8)   speedup
~2 ms                0.04s      0.17s       0.3x    <- POOLING LOSES
~20 ms               0.46s      0.21s       2.1x
~230 ms              5.61s      0.92s       6.1x
~2.6 s              61.78s      8.33s       7.4x
```

`pooled == serial` exactly at every size, because each trial seeds from its own
index.

**The crossover is around 20 ms per trial.** Below it the pool costs more than
the work — process spawn is ~20 ms each. 94% of this workbench's runs finish in
under ten seconds *in total*, so most of them should not be pooled at all.
**Time one trial before reaching for a pool**; `crypto-investigate`'s compute route
carries the rule.

### ⚠ `if __name__ == "__main__":` is mandatory, not style

macOS spawns child processes rather than forking, so each child **re-imports the
module**. Without the guard, module-level pool creation runs again in every
child, recursively. Omitting it produced pages of

```
File ".../multiprocessing/spawn.py", line 122, in spawn_main
```

and no result. Encountered while writing this entry.

### Seed from the loop index, never from a shared generator

```python
def trial(rep):
    rng = np.random.default_rng(BASE + rep)   # right: independent by construction
```

A single module-level `rng` shared across workers is the classic error, and its
symptom is *statistical* rather than a crash: samples that are not independent,
giving tighter error bars and more confident p-values than the data supports.

**Stated as a rule, not as a measurement.** A shared-generator demo written for
this entry did *not* reproduce the collision predicted — 8 of 8 values came back
distinct — because the outcome depends on the start method and on how `map`
chunks work across workers. The rule stands on how RNG state works; the failure
mode was not characterised here, so do not cite this file as having shown it.

### What does not parallelise

One Gröbner basis, one lattice reduction, one SVP enumeration, one
`class_number()` — each is a single sequential algorithm and splits not at all.
Pooling helps only *across* independent instances. Four workers on four
intractable instances is still intractable: on 2026-08-06 an enumeration grid ran
to dimension 128 and could never have finished at any width. **Bound the problem
before widening it.**

## Pitfalls this file exists to record

Every one encountered while building it, none from memory:

| Pitfall | Symptom |
|---|---|
| `from sage.all import *` shadows `random`, `round`, `D` | `TypeError` on seeding; Sage types leaking into `json.dump`; `'DerivativeOperator' object is not callable` |
| `exec` with separate globals/locals dicts | comprehensions raise `NameError` on names defined in the same snippet — pass **one** dict |
| Running a `.py` under `sage` | no preparser, so `Rt.<t> = ...` is a syntax error; `from sage.repl.preparse import preparse` and wrap |
| Random square integer matrix as an LLL demo | reduction appears to do nothing, because there is nothing to find |
| Importing a SAT class | proves the class exists, not that a solver is installed — this one bit, see the SAT entry |
| `M.get_r(i,i)` from fpylll | is the **squared** norm |
| `CyclotomicField(256)` | has degree **128** |

---

## Verification status

**22 of 24 snippets executed clean** on this machine and their captured output
appears above verbatim. Two did not, and both are marked in place: the
centred-binomial entry (name collision; the alias fix is written but untested)
and the SAT entry (no solver installed — that failure is itself the finding).
