# Attack families: symmetric and hash

Block ciphers, permutations, and hash functions. Load this checklist for the
symmetric-family coverage phase of `crypto-analyze-scheme`. The same rule as
`lattice.md` and `multivariate.md` applies:

> **Walk every family. Check each family's preconditions *before* running it.
> Report the cheapest, not the familiar one.**

This domain differs from the other two in one important way: **there is no
estimator.** For lattice and multivariate, a library computes the number. Here
you build a model and solve it, so the checklist is about *setting the model up
correctly* — and a wrong model returns a confident wrong number rather than an
error.

---

## The known-answer test that validates the whole approach

Before trusting any model, reproduce a published bound. PRESENT's minimum count
of differentially active S-boxes is the standard one. Measured on this machine:

| rounds | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| min active S-boxes | 1 | 2 | 4 | 6 | **10** | 12 | 14 |

**5 rounds → 10** matches the published bound. Any change to the model should be
re-checked against this table; a model that no longer produces it is broken,
whatever it says about your cipher.

---

## MILP: differential/linear trail search

### The model

Binary activity variables per bit and per S-box, branch-number constraints, the
cipher's linear layer wiring round *r*'s outputs to round *r+1*'s inputs,
minimise total activity. Full working script: `scripts/present_milp.py`,
shipped with the `crypto-validate-attack` skill.

```python
from sage.all import MixedIntegerLinearProgram

def pbox(i):                       # PRESENT: P(i) = 16i mod 63, P(63) = 63
    return 63 if i == 63 else (16 * i) % 63

BN = 3                             # PRESENT S-box differential branch number

p = MixedIntegerLinearProgram(maximization=False, solver="SCIP")
x = p.new_variable(binary=True)    # x[r,i] : bit i active entering round r
a = p.new_variable(binary=True)    # a[r,j] : S-box j active in round r

p.add_constraint(sum(x[0, i] for i in range(64)) >= 1)      # non-trivial input

for r in range(rounds):
    for j in range(16):
        ins  = [x[r, 4*j + k] for k in range(4)]
        outs = [x[r+1, pbox(4*j + k)] for k in range(4)]
        for b in ins:
            p.add_constraint(a[r, j] >= b)                  # active iff any input
        p.add_constraint(a[r, j] <= sum(ins))
        p.add_constraint(sum(ins) + sum(outs) >= BN * a[r, j])
        p.add_constraint(sum(outs) >= a[r, j])              # <-- see pitfall
        p.add_constraint(sum(ins)  >= a[r, j])              # <-- see pitfall
        for b in outs:
            p.add_constraint(b <= a[r, j])                  # inactive => no output

p.set_objective(sum(a[r, j] for r in range(rounds) for j in range(16)))
p.solve()
```

### ⚠ The pitfall that makes a wrong model look right

**The branch-number constraint alone does not force propagation.** With
`sum(ins) + sum(outs) >= 3·a`, the solver satisfies it using **three input bits
and zero output bits** — nothing reaches the next round, and the model reports
**1 active S-box for every round count**, from 1 round to 7.

That is the failure mode to fear here: not an exception, not an infinity, but a
plausible small number that is silently, completely wrong. The fix is to force
both sides nonzero:

```python
p.add_constraint(sum(outs) >= a[r, j])
p.add_constraint(sum(ins)  >= a[r, j])
```

Encountered while building this file, not recalled. **This is precisely why the
known-answer test above is mandatory** — the broken model produced a clean,
confident, monotone-looking answer and only the published bound exposed it.

### Solver: use SCIP, and here is the measurement

Same model, same answers, wildly different cost:

| rounds | SCIP | GLPK | ratio |
|---|---|---|---|
| 5 | 0.3 s | 11.4 s | 38× |
| 6 | 0.5 s | 53.5 s | 107× |
| 7 | **0.6 s** | **278.0 s** | **463×** |

GLPK's cost is growing explosively while SCIP's is nearly flat. At the 10+ round
counts a real analysis needs, GLPK is not viable and SCIP is still comfortable.
Both give identical answers, so **GLPK remains useful as a cross-check on small
instances** — agreement between two solvers is cheap evidence the model is not
solver-specific.

### Obligations

- [ ] **Reproduce a published bound for a known cipher before trusting the
      model.** Non-negotiable — see the pitfall above.
- [ ] Both propagation constraints present (`sum(ins) >= a`, `sum(outs) >= a`)
- [ ] Non-trivial input difference forced
- [ ] Branch number correct for *this* S-box — compute it, do not assume 3
      (`sage.crypto.sbox.SBox(...).differential_branch_number()`)
- [ ] Active-S-box count converted to a probability bound using the S-box's
      **actual** maximum differential probability, not 2^−2 by default
- [ ] Linear trails use the **linear** branch number, which differs — PRESENT's
      is 2 where its differential branch number is 3

---

## SAT: characteristic search with XOR clauses

CryptoMiniSat handles **XOR clauses natively**, which is the reason to prefer it:
linear and differential relations over GF(2) *are* XOR constraints, and CNF
encoding of an XOR over k variables costs 2^(k−1) clauses.

```python
from pycryptosat import Solver
s = Solver()
s.add_xor_clause([1, 2, 3], rhs=True)     # x1 ^ x2 ^ x3 = 1
sat, sol = s.solve()
```

Verified beyond a toy: a 40-variable, 60-clause random XOR system solves
correctly. Sage's wrapper (`sage.sat.solvers.CryptoMiniSat`) exposes the same
`add_xor_clause`.

**Bites when** the target has heavy GF(2)-linear structure — ARX ciphers, LFSR
and stream-cipher initialisations, and the key-schedule relations that MILP
models usually abstract away.

---

## S-box analysis

Everything below is a one-liner and should be run before any trail search, since
the trail-search model depends on these numbers.

```python
import sage.crypto.sbox
S = sage.crypto.sbox.SBox([0xC,5,6,0xB,9,0,0xA,0xD,3,0xE,0xF,8,4,7,1,2])  # PRESENT
(S.differential_uniformity(), S.linearity(), S.max_degree(),
 S.differential_branch_number(), S.linear_branch_number())
# (4, 8, 3, 3, 2)
```

Those are PRESENT's published values — use them as the self-test that the S-box
is entered correctly. `.difference_distribution_table()` and
`.linear_approximation_table()` give the full DDT and LAT.

**Note the branch numbers differ: differential 3, linear 2.** Using one where the
other belongs is a silent modelling error, and the MILP obligations above call
it out for that reason.

---

## Families documented but **not measured here**

Marked rather than implied. Each is real and current; none has been exercised on
this machine.

- **Integral / division property.** The modern route to integral distinguishers,
  and itself usually a MILP or SAT model. *Bites when* the cipher has low
  algebraic degree per round.
- **Boomerang and rectangle.** Combine two short differentials. *Bites when* good
  short trails exist but no good long one — a switching-effect analysis needs the
  DDT, not just active-S-box counts.
- **Impossible differential.** Miss-in-the-middle. *Bites when* the diffusion is
  slow enough that some difference provably cannot occur.
- **Meet-in-the-middle / biclique.** *Bites when* the key schedule is weak or
  round keys are reused.
- **Algebraic.** Model the cipher as a polynomial system and hand it to the
  multivariate families — see `multivariate.md`. *Bites when* the S-box has low
  algebraic degree and the round count is small. This is also where the Magma
  dependency reappears.
- **Rebound (hash-specific).** *Bites when* attacking a permutation-based hash
  where the attacker controls the internal state.
- **Length extension.** Structural, no computation needed: *bites when* a
  Merkle–Damgård hash is used as a MAC by prefixing the key. Check the
  construction, not the compression function.

Related and already recorded elsewhere: second-preimage strength under
Merkle–Damgård degrades with message length — SHA-256 on a gigabyte message is
**232 bits, not 256** (the `crypto-analyze-paper` skill's `reference/hash.md`, from
SP 800-107r1 App. A).

---

## Verification status

Measured on this machine, SageMath 10.7, SCIP via `pyscipopt` 6.2.1 and GLPK:

- The PRESENT active-S-box table for 1–7 rounds, reproducing the published
  5-round bound of 10.
- The propagation pitfall, by observing the broken model return 1 for every
  round count.
- The SCIP/GLPK timing comparison, both producing identical answers.
- PRESENT S-box criteria against published values.
- CryptoMiniSat XOR solving on a 40-variable system.

**Not measured:** every family in the "documented but not measured" section
above, and any cipher other than PRESENT.
