"""Minimum number of differentially active S-boxes in round-reduced PRESENT.

Known-answer test: the published bound is >= 10 active S-boxes over 5 rounds
(Mouha, Wang, Gu, Preneel -- the MILP-for-differential-cryptanalysis paper).
If this model reproduces it, the idiom is trustworthy.
"""
from sage.all import MixedIntegerLinearProgram
import sys, time

# PRESENT bit permutation: P(i) = 16*i mod 63, with P(63) = 63.
def pbox(i):
    return 63 if i == 63 else (16 * i) % 63

# PRESENT S-box differential branch number = 3 (verified separately via
# sage.crypto.sbox: differential_branch_number() -> 3)
BN = 3

def min_active(rounds, solver="SCIP"):
    p = MixedIntegerLinearProgram(maximization=False, solver=solver)
    x = p.new_variable(binary=True)   # x[r,i]  : bit i active entering round r
    a = p.new_variable(binary=True)   # a[r,j]  : S-box j active in round r

    # non-trivial input difference
    p.add_constraint(sum(x[0, i] for i in range(64)) >= 1)

    for r in range(rounds):
        for j in range(16):
            ins = [x[r, 4*j + k] for k in range(4)]
            # a is 1 iff any input nibble bit is active
            for b in ins:
                p.add_constraint(a[r, j] >= b)
            p.add_constraint(a[r, j] <= sum(ins))
            # outputs of this S-box, after the bit permutation, are inputs to r+1
            outs = [x[r+1, pbox(4*j + k)] for k in range(4)]
            # branch number: active S-box forces >= BN active in+out bits
            p.add_constraint(sum(ins) + sum(outs) >= BN * a[r, j])
            # ...and BOTH sides must be nonzero, or the branch-number
            # constraint is satisfiable with 3 input bits and no output,
            # so nothing propagates and every round count answers 1.
            p.add_constraint(sum(outs) >= a[r, j])
            p.add_constraint(sum(ins) >= a[r, j])
            # an inactive S-box has no active outputs
            for b in outs:
                p.add_constraint(b <= a[r, j])

    p.set_objective(sum(a[r, j] for r in range(rounds) for j in range(16)))
    return p.solve()

if __name__ == "__main__":
    solver = sys.argv[1] if len(sys.argv) > 1 else "SCIP"
    print("solver:", solver)
    for R in range(1, 8):
        t0 = time.time()
        try:
            v = min_active(R, solver)
            print("  %d rounds -> %2d active S-boxes   (%.1fs)"
                  % (R, int(round(v)), time.time()-t0))
        except Exception as e:
            print("  %d rounds -> ERROR %s" % (R, str(e)[:70]))
