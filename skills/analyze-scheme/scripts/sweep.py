#!/usr/bin/env sage-python
"""Walk every attack family for a hard problem, and report what applies.

The point of this script is that **an exception is a result, not an error**.
Several families announce their own preconditions by raising -- MITM says "Need
728 samples but only 512 available", Arora-Ge overflows a double because its
cost is astronomical at binomial noise, Lokshtanov raises a math domain error
over large fields. A sweep that lets any of those abort loses the finding, and a
sweep that swallows them silently loses it too. Both are reported here.

Run with an available SageMath executable and compatible estimator packages:

    sage --python sweep.py lwe ML-KEM-512
    sage --python sweep.py lwe n=512 q=3329 eta=3
    sage --python sweep.py uov n=112 m=44 q=256
    sage --python sweep.py mq  n=112 m=44 q=256
    sage --python sweep.py subfield n=254 m=57 q=2 r=7

`lwe` additionally reports the cost-model spread, because a single number is not
a reportable answer -- see ../reference/lattice.md.
"""
import sys, math, time

# Respect the caller's Sage configuration. In a sandbox, the caller can set
# DOT_SAGE to an explicit writable directory before invoking SageMath. Do not
# override a user-supplied path or assume an application-specific home.

# Named sets, so the common case needs no parameter typing and no transcription
# error. Sources: FIPS 203 (ML-KEM), NIST UOV submission.
NAMED_LWE = {
    "ML-KEM-512":  dict(n=512,  q=3329, eta=3, m=512),
    "ML-KEM-768":  dict(n=768,  q=3329, eta=2, m=768),
    "ML-KEM-1024": dict(n=1024, q=3329, eta=2, m=1024),
}
NAMED_UOV = {
    "ov-Is":  dict(n=160, m=64, q=16),
    "ov-Ip":  dict(n=112, m=44, q=256),
    "ov-III": dict(n=184, m=72, q=256),
    "ov-V":   dict(n=244, m=96, q=256),
}

LWE_FAMILIES = ["primal_usvp", "primal_bdd", "primal_hybrid", "dual",
                "dual_hybrid", "arora_gb", "coded_bkw", "mitm",
                "exhaustive_search"]
COST_MODELS = ["ADPS16", "MATZOV", "BDGL16", "CheNgu12"]


def _cost(x):
    """Estimator cost -> float, or a string explaining why there is no number.

    cryptographic_estimators returns the STRING '--' for an inadmissible
    family. Sorting raw output therefore dies with
    `TypeError: '<' not supported between instances of 'str' and 'float'`.
    Five of six analysts in the blind regression hit this. The '--' is a
    precondition finding, not an error.
    """
    if isinstance(x, str):
        return None
    try:
        v = float(x)
    except (TypeError, ValueError, OverflowError):
        return None
    return None if (v != v or v == float("inf")) else v


def _families(E):
    """Per-family costs, tolerating families that RAISE rather than return '--'.

    `E.estimate()` evaluates every family and propagates the first exception, so
    one broken family loses all the others. Measured: at q>=256 `Lokshtanov`
    raises `math domain error` and takes eight perfectly good MQ estimates down
    with it -- which is what made a lifted scheme over F_256 or F_512 look
    uncostable in its full field when in fact the cheapest family was fine.

    The same failure recurs with `memory_access` penalties: `KipnisShamir` at
    2^1766 overflows as soon as any non-constant model is applied, which killed
    three of the four rows of the memory-access spread -- hiding that the
    cheapest UOV attack moves from 2^185.2 under free memory to 2^253.1 under
    square-root access. That spread is the entire reason the block is printed.

    Returns (rows, skipped) with rows as (name, time, memory); memory is None if
    it alone could not be evaluated. Skipped families are RETURNED, never
    swallowed: a family that cannot be evaluated is a finding about coverage,
    and a "cheapest attack" computed over a silently reduced set is a lower
    bound pretending to be an answer.
    """
    rows, skipped = [], []
    for a in E.algorithms():
        name = a.__class__.__name__
        try:
            c = _cost(a.time_complexity())
        except Exception as exc:
            skipped.append((name, "raised %s: %s"
                            % (type(exc).__name__, str(exc)[:40])))
            continue
        if c is None:
            skipped.append((name, "inadmissible (estimator returned '--')"))
            continue
        # A family with a usable time and an unusable memory figure still
        # belongs in the table; losing the row would overstate the cheapest cost.
        try:
            mem = _cost(a.memory_complexity())
        except Exception:
            mem = None
        rows.append((name, c, mem))
    rows.sort(key=lambda t: t[1])
    return rows, skipped


def _l2(x):
    try:
        v = float(x)
    except (TypeError, ValueError, OverflowError):
        return None
    if v <= 0 or math.isinf(v):
        return math.inf if v > 0 else None
    return math.log2(v)


def sweep_lwe(kw):
    from estimator import LWE, ND, RC
    # eta_s and eta_e are separate. A single `eta` cannot express a scheme
    # whose secret and error distributions differ, and silently analyses only
    # the key-recovery instance.
    eta_s = kw.get("eta_s", kw.get("eta"))
    eta_e = kw.get("eta_e", kw.get("eta"))
    p = LWE.Parameters(n=kw["n"], q=kw["q"], m=kw.get("m", kw["n"]),
                       Xs=ND.CenteredBinomial(eta_s),
                       Xe=ND.CenteredBinomial(eta_e))
    if eta_s != eta_e:
        print("note: Xs=CBD(%d), Xe=CBD(%d) -- asymmetric" % (eta_s, eta_e))
    print("instance: %s" % p)
    print()
    rows, notes = [], []
    for name in LWE_FAMILIES:
        fn = getattr(LWE, name, None)
        if fn is None:
            notes.append((name, "absent from this estimator version"))
            continue
        t0 = time.time()
        try:
            r = (fn(p, red_cost_model=RC.MATZOV)
                 if name.startswith(("primal", "dual")) else fn(p))
            lg = _l2(r["rop"])
            if lg is None or lg == math.inf:
                notes.append((name, "returned non-finite cost"))
            else:
                # Some families silently REWRITE the instance: coded_bkw
                # consumed m = 2^166.8 samples against 512 declared and
                # rewrote Xe. A cost obtained on a different instance is not
                # a cost for your instance.
                used_m = r.get("m")
                if used_m is not None and float(used_m) > 4 * kw.get("m", kw["n"]):
                    notes.append((name, "REWROTE THE INSTANCE: used m=2^%.1f samples "
                                        "against %d declared -- cost 2^%.1f is for a "
                                        "different problem"
                                  % (math.log2(float(used_m)), kw.get("m", kw["n"]), lg)))
                else:
                    rows.append((name, lg, r.get("beta"), time.time() - t0))
        except Exception as exc:                     # the exception IS the answer
            notes.append((name, "%s: %s" % (type(exc).__name__, str(exc)[:88])))

    rows.sort(key=lambda t: t[1])
    print("APPLICABLE FAMILIES (RC.MATZOV)")
    for name, lg, beta, secs in rows:
        print("   %-18s 2^%-7.1f %s  (%.1fs)"
              % (name, lg, ("beta=%s" % beta) if beta else "", secs))
    if notes:
        print()
        print("PRECONDITION NOT MET -- these are findings, not failures")
        for name, why in notes:
            print("   %-18s %s" % (name, why))

    if rows:
        cheapest = rows[0]
        print()
        print("cheapest: %s at 2^%.1f" % (cheapest[0], cheapest[1]))
        if cheapest[0].startswith("dual"):
            print("   ** A DUAL ATTACK IS CHEAPEST. The dual-sieve cost model is")
            print("      disputed (eprint 2023/302). Report the cheapest PRIMAL")
            print("      cost alongside it as the defensible number.")
            primal = [r for r in rows if r[0].startswith("primal")]
            if primal:
                print("      cheapest primal: %s at 2^%.1f" % (primal[0][0], primal[0][1]))

    print()
    print("COST-MODEL SPREAD (primal_usvp) -- never report a bare lambda")
    for cm in COST_MODELS:
        try:
            r = LWE.primal_usvp(p, red_cost_model=getattr(RC, cm))
            print("   %-10s 2^%.1f" % (cm, _l2(r["rop"])))
        except Exception as exc:
            print("   %-10s %s" % (cm, str(exc)[:60]))
    print("   (ADPS16 is core-SVP -- the convention NIST submissions quote.)")


def sweep_uov(kw):
    from cryptographic_estimators.UOVEstimator import UOVEstimator
    from cryptographic_estimators.UOVEstimator.uov_algorithm import UOVAlgorithm

    print("UOV n=%(n)d m=%(m)d q=%(q)d" % kw)
    print()
    print("   !! UOVEstimator hard-codes oil dimension = m and assumes a SINGLE")
    print("      layer over the full field. It does not model Rainbow-style")
    print("      layering, subfield-lifted coefficients (LUOV/QR-UOV), MAYO or")
    print("      SNOVA. If your target is any of those, these numbers describe a")
    print("      DIFFERENT SCHEME. See SKILL.md step 3a.")
    print()

    E = UOVEstimator(n=kw["n"], m=kw["m"], q=kw["q"])
    rows, notes = _families(E)

    # Families whose constructor raised are silently ABSENT from the estimator.
    # Recovering them is what makes step 3's completeness obligation meetable.
    offered = {r[0] for r in rows} | {n for n, _ in notes}
    for cls in UOVAlgorithm.__subclasses__():
        if cls.__name__ not in offered:
            notes.append((cls.__name__, "excluded by the estimator at this shape "
                                        "-- usually an n/m ratio guard"))

    print("   %-20s %-11s %s" % ("family", "time", "memory"))
    for name, t, mem in rows:
        print("   %-20s 2^%-9.1f %s" % (name, t, ("2^%.1f" % mem) if mem else "--"))

    if notes:
        print()
        print("   PRECONDITION NOT MET -- findings, not failures")
        for name, why in notes:
            print("      %-20s %s" % (name, why))

    if rows:
        print()
        print("   cheapest: %s at 2^%.1f" % (rows[0][0], rows[0][1]))
        if rows[0][1] < 64:
            print("      ** IMPLAUSIBLY CHEAP. A sub-2^64 attack on a scheme")
            print("         claiming any NIST category is far more likely a")
            print("         MODELLING ERROR than a break -- the estimator has")
            print("         accepted parameters it cannot correctly model.")
            print("         Do NOT report this as a break. Go back to step 3a.")
        if rows[0][2] and rows[0][2] > 100:
            print("      ** memory is 2^%.1f -- check feasibility before calling"
                  " this the cheapest attack." % rows[0][2])

    # The multivariate analogue of the lattice cost-model spread. On ov-Ip the
    # cheapest cost moves 2^134.5 -> 2^184.4 across these, a 50-bit swing that
    # flips a category-1 verdict. Never report a single multivariate number.
    print()
    print("   MEMORY-ACCESS SPREAD -- never report a bare multivariate cost")
    for ma, label in [(0, "constant"), (1, "logarithmic"), (3, "cube-root"), (2, "square-root")]:
        try:
            r2, _ = _families(UOVEstimator(n=kw["n"], m=kw["m"], q=kw["q"],
                                           memory_access=ma))
            if r2:
                print("      %-12s %-20s 2^%.1f" % (label, r2[0][0], r2[0][1]))
            else:
                print("      %-12s no family evaluated" % label)
        except Exception as exc:
            print("      %-12s %s: %s" % (label, type(exc).__name__, str(exc)[:44]))


def sweep_mq(kw):
    from cryptographic_estimators.MQEstimator import MQEstimator
    from cryptographic_estimators.MQEstimator.mq_algorithm import MQAlgorithm
    ALL = {c.__name__: c for c in MQAlgorithm.__subclasses__()}
    print("MQ n=%(n)d m=%(m)d q=%(q)d" % kw)
    print()
    rows, notes = [], []
    for name, cls in ALL.items():
        try:
            # excluded_algorithms takes CLASSES, not names
            E = MQEstimator(n=kw["n"], m=kw["m"], q=kw["q"],
                            excluded_algorithms=[c for n2, c in ALL.items() if n2 != name])
            e = E.estimate()
            if not e:
                notes.append((name, "not offered for this shape/field"))
                continue
            v = list(e.values())[0]["estimate"]
            t, mem = _cost(v["time"]), _cost(v.get("memory"))
            if t is None:
                notes.append((name, "estimator returned %r" % v["time"]))
            else:
                rows.append((name, t, mem))
        except Exception as exc:
            notes.append((name, "%s: %s" % (type(exc).__name__, str(exc)[:64])))
    rows.sort(key=lambda r: r[1])
    print("   %-20s %-11s %s" % ("family", "time", "memory"))
    for name, t, mem in rows:
        print("   %-20s 2^%-9.1f %s" % (name, t, ("2^%.1f" % mem) if mem else "--"))
    if notes:
        print()
        print("PRECONDITION NOT MET")
        for name, why in notes:
            print("   %-20s %s" % (name, why))
    if rows:
        print()
        print("cheapest: %s at 2^%.1f" % (rows[0][0], rows[0][1]))
        f5 = [r for r in rows if r[0] == "F5"]
        if f5 and f5[0][1] - rows[0][1] > 10:
            print("   ** F5 (the obvious Groebner attack) is 2^%.1f -- %.0f bits"
                  " worse than the cheapest family. Do not quote it alone."
                  % (f5[0][1], f5[0][1] - rows[0][1]))


def sweep_minrank(kw):
    """MinRank cost. Takes the MinRank instance directly -- NOT a scheme.

    MinRank is the family that actually broke Rainbow (Beullens,
    eprint 2022/214) and MiRitH, and it is what UOVEstimator cannot reach.

    **The scheme -> MinRank reduction is deliberately NOT automated here.**
    Deriving (q, m, n, k, r) from a scheme's parameters is the substance of the
    attack, it differs per scheme, and this project's rule is that an unverified
    mapping is worse than none. Do the reduction yourself, state it, and pass the
    instance. For Rainbow the reduction is: for x in O2 the first o1 columns of
    M_x = [P_1 x | ... | P_m x] vanish, so rank(M_x) <= m - o1, giving a
    rectangular MinRank instance over the span of the M_i.

    Warning: this is SLOW at cryptographic sizes -- a k=100, r=32 instance ran
    past 10 minutes without returning. Budget for it.
    """
    from cryptographic_estimators.MREstimator import MREstimator
    print("MinRank q=%(q)d m=%(m)d n=%(n)d k=%(k)d r=%(r)d" % kw)
    print("   (instance as supplied -- the scheme reduction is YOUR claim, not the tool's)")
    print()
    E = MREstimator(q=kw["q"], m=kw["m"], n=kw["n"], k=kw["k"], r=kw["r"])
    rows, notes = _families(E)
    print("   %-18s %-11s %s" % ("family", "time", "memory"))
    for name, t, mem in rows:
        print("   %-18s 2^%-9.1f %s" % (name, t, ("2^%.1f" % mem) if mem else "--"))
    if notes:
        print()
        print("   PRECONDITION NOT MET")
        for name, why in notes:
            print("      %-18s %s" % (name, why))
    if rows:
        print()
        print("   cheapest: %s at 2^%.1f" % (rows[0][0], rows[0][1]))


def sweep_subfield(kw):
    """Cost a lifted scheme over its coefficient subfield -- and say what that buys.

    Schemes like LUOV and QR-UOV shrink their public key by restricting central-map
    coefficients to a proper subfield F_q while operating over F_{q^r}. That makes a
    much smaller system available to the attacker, and NOTHING ELSE in this toolchain
    can express it -- which is why the blind regression's LUOV arms could only reach
    their answer by recall.

    The number alone is dangerous. A solution found in the subfield is only a forgery
    if the TARGET also lies in the subfield, and for a uniform target it does not:
    the probability is q^-m(r-1)/... -- computed below. In the blind test one analyst
    correctly refused to quote the subfield cost as a break for exactly this reason
    while another headlined it. This function prints both numbers so that divergence
    cannot recur.
    """
    from cryptographic_estimators.MQEstimator import MQEstimator
    n, m, q, r = kw["n"], kw["m"], kw["q"], kw["r"]
    full = q ** r
    print("Lifted scheme: n=%d m=%d over F_%d^%d = F_%d, coefficients in F_%d"
          % (n, m, q, r, full, q))
    print()

    for label, field in (("full field  F_%d" % full, full), ("SUBFIELD    F_%d" % q, q)):
        try:
            rows, skipped = _families(MQEstimator(n=n, m=m, q=field))
        except Exception as exc:
            print("   %-18s ERROR %s" % (label, str(exc)[:60]))
            continue
        if rows:
            print("   %-18s cheapest %-18s 2^%.1f" % (label, rows[0][0], rows[0][1]))
        else:
            print("   %-18s no family returned a cost" % label)
        # Say what was not counted. The gap between "cheapest of nine" and
        # "cheapest of the eight that evaluated" is exactly the kind of silent
        # narrowing that makes a security level look better than it is.
        for name, why in skipped:
            print("   %-18s   skipped %-12s %s" % ("", name, why))

    # The guard. A uniform target in F_{q^r}^m lands in F_q^m with probability
    # q^-m(r-1); quoting the subfield cost without this is the false break.
    exponent = m * (r - 1) * math.log2(q)
    print()
    print("   ** THE SUBFIELD COST IS NOT A FORGERY COST.")
    print("      A solution in F_%d is only useful if the TARGET lies in F_%d too." % (q, q))
    print("      For a uniform target in F_%d^%d that happens with probability" % (full, m))
    print("      q^-m(r-1) = 2^-%.1f." % exponent)
    print("      Report the subfield cost as a STRUCTURAL finding -- evidence the")
    print("      lifting is exploitable -- not as a break, unless you can also show")
    print("      the target is reachable. See SKILL.md step 3a.")


_SDA_DMAX = 200


def _ser_mul(a, b):
    out = [0] * (_SDA_DMAX + 1)
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b):
            if i + j > _SDA_DMAX:
                break
            out[i + j] += x * y
    return out


def _ser_binom_neg(step, power):
    """(1 - t^step)^power, truncated."""
    from math import comb
    s = [0] * (_SDA_DMAX + 1)
    for i in range(power + 1):
        if step * i > _SDA_DMAX:
            break
        s[step * i] = ((-1) ** i) * comb(power, i)
    return s


def _ser_inv_pow(step, power):
    """1 / (1 - t^step)^power, truncated."""
    from math import comb
    s = [0] * (_SDA_DMAX + 1)
    j = 0
    while step * j <= _SDA_DMAX:
        s[step * j] = comb(j + power - 1, power - 1) if power > 0 else int(j == 0)
        j += 1
    return s


def _d0(nvars, neq, q):
    """Operating degree of XL, by the regime the field size puts us in.

    Ding et al. give two series. Small field (operating degree above the field
    size):  [t^d] (1-t^q)^n (1-t^2)^m / ((1-t)^(n+1) (1-t^2q)^m).
    Large field: [t^d] (1-t)^(m-n-1) (1+t)^m.

    The paper writes `<= 0` for the first and `< 0` for the second. Empirically
    `<= 0` reproduces its own Table 5 for both -- on (3,V) the coefficient at
    d=38 is exactly zero (C(75,37) = C(75,38)) and a strict test would give 39,
    where the paper gives 38. Using `<= 0` throughout.
    """
    from math import comb
    e = neq - nvars - 1
    d_large = None
    if e >= 0:
        a = [0] * (_SDA_DMAX + 1)
        for i in range(min(e, _SDA_DMAX) + 1):
            a[i] = ((-1) ** i) * comb(e, i)
        b = [0] * (_SDA_DMAX + 1)
        for i in range(min(neq, _SDA_DMAX) + 1):
            b[i] = comb(neq, i)
        for d, c in enumerate(_ser_mul(a, b)):
            if d > 0 and c <= 0:
                d_large = d
                break
    if d_large is not None and d_large <= q:
        return d_large
    s = _ser_mul(_ser_mul(_ser_binom_neg(q, nvars), _ser_binom_neg(2, neq)),
                 _ser_mul(_ser_inv_pow(1, nvars + 1), _ser_inv_pow(2 * q, neq)))
    for d, c in enumerate(s):
        if d > 0 and c <= 0:
            return d
    return d_large


def _xl_cost(m, q):
    """Ding et al. Theorem 2: min_k q^k * 3 * C(m-k+D0,D0)^2 * C(m-k,2).

    Field multiplications for XL-with-block-Wiedemann on a DETERMINED quadratic
    system of m equations over F_q, hybridised by guessing k variables.

    Validated against the paper's Table 5 before use: every k and D0 it selects
    matches the published row exactly on all six parameter sets, and five of six
    complexities reproduce to the paper's own rounding-up. (3,IV) comes out at
    2^203.3 against a published 2^202 with identical k and D0, so that gap is in
    their arithmetic, not in this model.
    """
    from math import comb, log2
    best = None
    for k in range(0, m):
        D = _d0(m - k, m, q)
        if D is None:
            continue
        c = (q ** k) * 3 * comb(m - k + D, D) ** 2 * comb(m - k, 2)
        if c > 0 and (best is None or c < best[0]):
            best = (c, k, D)
    return (log2(best[0]), best[1], best[2]) if best else (None, None, None)


def _thomae_wolf(m, variables):
    """Theorem 1. Underdetermined m x variables -> determined square system.

    m - floor(w) + 1 equations, dropping to m - floor(w) ONLY when floor(w)
    divides m. Getting that condition wrong is invisible on most parameter sets
    -- floor(w) = 1 divides everything -- and shifts the system by one equation
    exactly when floor(w) does not divide m, which understates the cost. It was
    caught against the paper's (3,IV) row: 61 x 180 reduces to 60 x 60, not
    59 x 59, because 2 does not divide 61.
    """
    w = variables // m
    if w <= 0:
        return m
    return m - w if m % w == 0 else m - w + 1


def sweep_sda(kw):
    """Subfield Differential Attack on a lifted scheme -- the model nothing else has.

    `subfield` prices the NAIVE restriction to F_q and correctly refuses to call it
    a forgery, because a solution in F_q^n hits a uniform target in F_{q^r}^m with
    probability q^-m(r-1). That guard is real but it is not the end of the story,
    and stopping there UNDERSTATES the attack.

    Ding et al. (2nd PQC Standardization Conference, "New Attacks on Lifted
    Unbalanced Oil Vinegar") remove the obstacle with a SHIFT. Pick an arbitrary
    x' in K^n and look for x-bar in an INTERMEDIATE subfield F_{q^d}, d | r, with
    P(x' + x-bar) = h. The shift absorbs whatever part of the target does not lie
    in the subfield, so there is no reachability penalty at all; the failure
    probability is exp(-q^{d*n - r*m}), negligible whenever d*n > r*m.

    Writing K = F_{q^d}[t]/f(t) with deg f = s = r/d and comparing coefficients of
    t^0..t^{s-1}: the quadratic part has F_q coefficients and therefore stays in
    the constant term, so the higher coefficients give (s-1)m LINEAR equations.
    What is left is m equations in n-(s-1)m variables over F_{q^d}, which
    Thomae-Wolf reduces to a square system of m - floor((n-(s-1)m)/m).

    THIS IS WHY d MATTERS AND WHY r's FACTORISATION IS A DESIGN PARAMETER. A prime
    r offers only d in {1, r} -- the naive case and no reduction at all.

    That is not a hypothetical. The round-2 LUOV sets this attack broke use
    composite r (8, 48, 64, 80); the LUOV team's RESPONSE was to republish with
    prime r (7, 47, 61, 79) precisely "to avoid the existence of a sufficiently
    large intermediate field to perform SDA" (2019/1490 sec 5). So a prime r here
    is a designed defence, not an oversight -- and the same paper notes the fix is
    "very new and untested", and that a variant over special subsets of F_2^r
    rather than subfields might reach it anyway. Report the refusal below as
    "no intermediate subfield", never as "secure".

    Calibration against the paper's Table 4, run before this was trusted: the
    reduction reproduces the published system shapes on 4 of 6 rows exactly. Two
    rows (R2-IV's 259, R3-V's 131) are inconsistent with the paper's own formula
    and look like typos; the reduced square systems agree regardless. Costs land
    within 4-8 bits of the published log2 complexities, differing in both
    directions because this uses the estimator's current families (Crossbred, PXL)
    rather than the paper's XL-with-block-Wiedemann. Treat the family label as
    more reliable than the last bit of the exponent.
    """
    from cryptographic_estimators.MQEstimator import MQEstimator
    n, m, q, r = kw["n"], kw["m"], kw["q"], kw["r"]
    print("Subfield differential attack: n=%d m=%d over F_%d^%d, coefficients in F_%d"
          % (n, m, q, r, q))
    print("   (Ding et al., 2nd PQC Standardization Conference)")
    print()

    divisors = [d for d in range(2, r) if r % d == 0]
    if not divisors:
        print("   r=%d is PRIME -- the only subfields are F_%d and K itself." % (r, q))
        print("   No intermediate subfield exists, so the shifted attack has no")
        print("   d to work with. Price the naive restriction with `subfield`;")
        print("   its reachability guard is then the whole story.")
        return

    print("   %-4s %-10s %-3s %-14s %-16s %s"
          % ("d", "field", "s", "system", "cheapest", "failure prob"))
    best = None
    for d in divisors:
        exponent = d * n - r * m
        field = q ** d
        if exponent <= 0:
            print("   %-4d F_%-8d %-3d INFEASIBLE -- d*n-r*m = %d <= 0"
                  % (d, field, r // d, exponent))
            continue
        s = r // d
        variables = n - (s - 1) * m
        if variables <= 0:
            print("   %-4d F_%-8d %-3d no variables left after linearisation"
                  % (d, field, s))
            continue
        m2 = _thomae_wolf(m, variables)
        if m2 < 2:
            print("   %-4d F_%-8d %-3d reduces below two equations" % (d, field, s))
            continue
        cost, k, D = _xl_cost(m2, field)
        if cost is None:
            print("   %-4d F_%-8d %-3d no operating degree found" % (d, field, s))
            continue
        name = "XL/Wiedemann k=%d D0=%d" % (k, D)
        print("   %-4d F_%-8d %-3d %-14s %-22s exp(-%d^%d)"
              % (d, field, s, "%dx%d" % (m2, m2), "2^%.1f  %s" % (cost, name),
                 q, exponent))
        if best is None or cost < best[1]:
            best = (d, cost, name)

    print()
    if best is None:
        print("   No feasible d. The lifting is not exploitable this way at these")
        print("   parameters -- which is a finding, not a failure.")
        return
    print("   cheapest: d=%d at 2^%.1f (%s)" % (best[0], best[1], best[2]))
    print("   ** Unlike the naive subfield cost, this IS a forgery cost. The shift")
    print("      removes the target-reachability obstacle -- that is the whole point")
    print("      of the construction. Compare against the full-field cost from")
    print("      `uov` or `subfield` to state what the lifting actually costs.")


def parse(argv):
    kw = {}
    for tok in argv:
        if "=" in tok:
            k, v = tok.split("=", 1)
            kw[k] = int(v)
    return kw


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        print("named LWE sets:", ", ".join(NAMED_LWE))
        print("named UOV sets:", ", ".join(NAMED_UOV))
        return 2
    kind, rest = sys.argv[1].lower(), sys.argv[2:]

    if kind == "lwe":
        kw = NAMED_LWE.get(rest[0]) if rest and rest[0] in NAMED_LWE else parse(rest)
        if rest and rest[0] in NAMED_LWE:
            print("named set: %s" % rest[0])
        sweep_lwe(kw)
    elif kind == "uov":
        kw = NAMED_UOV.get(rest[0]) if rest and rest[0] in NAMED_UOV else parse(rest)
        sweep_uov(kw)
    elif kind == "mq":
        sweep_mq(parse(rest))
    elif kind == "minrank":
        kw = parse(rest)
        missing = [k for k in ("q", "m", "n", "k", "r") if k not in kw]
        if missing:
            print("minrank needs q= m= n= k= r=; missing %s" % ", ".join(missing))
            return 2
        sweep_minrank(kw)
    elif kind == "subfield":
        kw = parse(rest)
        missing = [k for k in ("n", "m", "q", "r") if k not in kw]
        if missing:
            print("subfield needs n=, m=, q= (base field), r= (extension degree);"
                  " missing %s" % ", ".join(missing))
            return 2
        sweep_subfield(kw)
    elif kind == "sda":
        kw = parse(rest)
        missing = [k for k in ("n", "m", "q", "r") if k not in kw]
        if missing:
            print("sda needs n=, m=, q= (base field), r= (extension degree);"
                  " missing %s" % ", ".join(missing))
            return 2
        sweep_sda(kw)
    else:
        print("unknown problem type %r -- expected lwe, uov, mq, minrank, subfield or sda" % kind)
        return 2

    print()
    import sage.version
    print("provenance: SageMath %s | estimators pinned, see docs/ENVIRONMENTS.md"
          % sage.version.version)
    return 0


if __name__ == "__main__":
    sys.exit(main())
