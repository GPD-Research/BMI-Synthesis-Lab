"""Symbolic check of the D=6 brane field equation and two-brane Friedmann equation (v2/02_effective_4d.md §3,
v2/04c_approach.md §1).

1. Gauss equation on a codimension-one brane with worldvolume dimension d (d = 5 for BMI):
   with the Z2 junction condition K_ab = -(kappa^2/2)(S_ab - S gamma_ab/(d-1)), S_ab = -sigma gamma_ab + tau_ab,
   the quadratic-in-K terms K K_ab - K_ac K^c_b - 1/2 gamma_ab (K^2 - K.K) equal
       8 pi G_d tau_ab + kappa^4 pi_ab   (+ a constant cancelled by Lambda_D at the RS tuning),
   with 8 pi G_d = (d-2) kappa^4 sigma / (4(d-1)) and
       pi_ab = -1/4 tau_ac tau^c_b + tau tau_ab/(4(d-1)) + 1/8 gamma_ab (tau.tau - tau^2/(d-1)).
   d = 4 reproduces Shiromizu-Maeda-Sasaki (1/6, 1/12, 1/3); d = 5 gives 3/16, 1/16, 1/4.
   These products are even in K, so the result does not depend on the sign convention for the normal.
2. Direct Israel computation for a brane at r = R(tau) in planar Schwarzschild-AdS_{n+2} (n = 4: the 6D bulk
   with the circle expanding with the brane): the bulk metric solves the vacuum equations, K^i_j =
   sqrt(h + Rdot^2)/R, and squaring the junction condition gives 04c's H^2 = (kappa^2 rho/(n l))(1 + rho/2 sigma)
   + mu/R^{n+1}; the Gauss equation of part 1 gives the same rho and rho^2 terms (cross-check of pi_ab).
3. Convention-free tension: eliminating kappa between 8 pi G_d and the tuning sigma = 2(d-1)/(kappa^2 l) gives
   sigma = (d-1)(d-2) / (8 pi G_d l^2); reduced on the circle, sigma_1^{(5)} = 12 M_Pl^2 / l^2 (not 24).
   The A'' (delta-function) part of G^a_b for e^{-2A(y)} eta + dy^2 shows that 2(D-2) M^{D-2}/l is the tension of
   a brane with bulk on both sides; a brane bounding an interval (v2: 0 <= y <= phi) carries half, (D-2) M^{D-2}/l.

Requires sympy. Run: python3 tests/check_brane_eq.py
"""
import sys

import sympy as sp

kap, sig, l = sp.symbols("kappa sigma ell", positive=True)


def gauss_terms(d):
    t = sp.Matrix(d, d, lambda i, j: sp.Symbol(f"t{min(i, j)}{max(i, j)}"))
    syms = sorted(t.free_symbols, key=str)
    I = sp.eye(d)
    S = -sig * I + t
    K = -kap**2 / 2 * (S - S.trace() * I / (d - 1))
    trK = K.trace()
    Q = trK * K - K * K - I * (trK**2 - (K * K).trace()) / 2
    eps = sp.Symbol("eps")
    Qe = Q.subs({s: eps * s for s in syms}, simultaneous=True).applyfunc(sp.expand)
    Q1 = Qe.applyfunc(lambda e: e.coeff(eps, 1))
    Q2 = Qe.applyfunc(lambda e: e.coeff(eps, 2))
    c1 = sp.simplify(Q1[0, 1] / t[0, 1])
    ok_lin = (Q1 - c1 * t).applyfunc(sp.expand) == sp.zeros(d)
    A, B, C, E = sp.symbols("A B C E")
    ans = A * t * t + B * t.trace() * t + I * (C * (t * t).trace() + E * t.trace()**2)
    eqs = []
    for e in (kap**4 * ans - Q2).applyfunc(sp.expand):
        if e != 0:
            eqs += sp.Poly(e, *syms).coeffs()
    sol = sp.solve(eqs, [A, B, C, E], dict=True)
    return c1, ok_lin, sol[0] if len(sol) == 1 else None


def christoffel_einstein(coords, g):
    D = len(coords)
    ginv = g.inv()
    Gam = [[[sp.simplify(sum(ginv[a, e] * (sp.diff(g[e, b], coords[c]) + sp.diff(g[e, c], coords[b])
                                             - sp.diff(g[b, c], coords[e])) for e in range(D)) / 2)
             for c in range(D)] for b in range(D)] for a in range(D)]
    Ric = sp.Matrix(D, D, lambda b, c: sp.simplify(sum(
        sp.diff(Gam[a][b][c], coords[a]) - sp.diff(Gam[a][b][a], coords[c])
        + sum(Gam[a][a][e] * Gam[e][b][c] - Gam[a][c][e] * Gam[e][b][a] for e in range(D)) for a in range(D))))
    Rs = sp.simplify(sum(ginv[a, b] * Ric[a, b] for a in range(D) for b in range(D)))
    return (Ric - Rs * g / 2).applyfunc(sp.simplify), ginv


def israel_moving_brane(n):
    D = n + 2
    t, r, mu = sp.symbols("t r mu", positive=True)
    xs = sp.symbols(f"x1:{n + 1}")
    h = r**2 / l**2 - mu / r**(n - 1)
    g = sp.diag(-h, 1 / h, *([r**2] * n))
    G, _ = christoffel_einstein([t, r] + list(xs), g)
    ok_bulk = (G - sp.Rational((D - 1) * (D - 2), 2) / l**2 * g).applyfunc(sp.simplify) == sp.zeros(D)
    R, Rd, rho, p = sp.symbols("R Rdot rho p", positive=True)
    hR = h.subs(r, R)
    Td = sp.sqrt(hR + Rd**2) / hR                       # -h Tdot^2 + Rdot^2/h = -1
    n_low = sp.Matrix([-Rd, Td] + [0] * n)
    gR = g.subs(r, R)
    ok_norm = sp.simplify((n_low.T * gR.inv() * n_low)[0] - 1) == 0
    n_up_r = sp.simplify((gR.inv() * n_low)[1])
    Kij = sp.simplify(n_up_r * sp.diff(g[2, 2], r).subs(r, R) / 2 / R**2)
    ok_K = sp.simplify(Kij - sp.sqrt(hR + Rd**2) / R) == 0
    H2 = (kap**2 * (sig + rho) / (2 * n))**2 - hR / R**2
    tuned = {sig: 2 * n / (kap**2 * l)}
    target = kap**2 * rho / (n * l) * (1 + rho / (2 * sig)) + mu / R**(n + 1)
    ok_fried = sp.simplify((H2 - target).subs(tuned)) == 0
    d = n + 1
    tau = sp.diag(-rho, *([p] * n))
    I = sp.eye(d)
    pi = -tau * tau / 4 + tau.trace() * tau / (4 * (d - 1)) + I * ((tau * tau).trace() - tau.trace()**2 / (d - 1)) / 8
    G00 = (d - 2) * kap**4 * sig / (4 * (d - 1)) * tau[0, 0] + kap**4 * pi[0, 0]
    H2_gauss = -2 * G00 / (n * (n - 1))
    ok_gauss = sp.simplify(H2_gauss - (kap**4 * sig * rho / (2 * n**2) + kap**4 * rho**2 / (4 * n**2))) == 0
    return ok_bulk, ok_norm, ok_K, ok_fried, ok_gauss


def delta_part_6d():
    D = 6
    y = sp.Symbol("y")
    A = sp.Function("A")(y)
    coords = list(sp.symbols(f"x0:{D - 1}")) + [y]
    g = sp.diag(*([-sp.exp(-2 * A)] + [sp.exp(-2 * A)] * (D - 2) + [1]))
    G, ginv = christoffel_einstein(coords, g)
    G11 = sp.expand(sp.simplify((ginv * G)[1, 1]))
    return G11.coeff(sp.Derivative(A, (y, 2)))


def main():
    failed = False
    expect = {4: (sp.Rational(1, 6), {"A": -sp.Rational(1, 4), "B": sp.Rational(1, 12), "C": sp.Rational(1, 8), "E": -sp.Rational(1, 24)}),
              5: (sp.Rational(3, 16), {"A": -sp.Rational(1, 4), "B": sp.Rational(1, 16), "C": sp.Rational(1, 8), "E": -sp.Rational(1, 32)})}
    for d in (4, 5):
        c1, ok_lin, sol = gauss_terms(d)
        got = {str(k): v for k, v in (sol or {}).items()}
        ok = ok_lin and sp.simplify(c1 / (kap**4 * sig) - expect[d][0]) == 0 and got == expect[d][1]
        print(f"d={d}: 8 pi G_d = {c1}; pi_ab = {got['A']} tau tau + {got['B']} tau tau_ab "
              f"+ gamma ({got['C']} tau.tau + {got['E']} tau^2)  {'OK' if ok else 'FAIL'}")
        failed |= not ok
    for n in (3, 4):
        oks = israel_moving_brane(n)
        print(f"n={n} moving brane in SAdS_{n + 2}: bulk eq, n.n=1, K^i_j, 04c Friedmann, Gauss cross-check: "
              f"{' '.join('OK' if o else 'FAIL' for o in oks)}")
        failed |= not all(oks)
    d = 5
    G5 = sp.Rational(d - 2, 4 * (d - 1)) * kap**4 * sig
    k2 = sp.solve(sp.Eq(sig, 2 * (d - 1) / (kap**2 * l)), kap**2)[0]
    free = sp.simplify(sig * G5.subs(kap**4, k2**2) * l**2)
    ok_free = free == (d - 1) * (d - 2)
    print(f"convention-free: sigma * 8 pi G_5 * l^2 = {free} -> sigma_1^(5) = {free} M_Pl^2 / l^2  {'OK' if ok_free else 'FAIL'}")
    cA = delta_part_6d()
    ok_delta = cA == -4
    print(f"D=6: G^a_b contains {cA} A''; A = |y|/l gives A'' = 2 delta/l -> two-sided tension 8 M^4/l, "
          f"one-sided (interval) 4 M^4/l  {'OK' if ok_delta else 'FAIL'}")
    failed |= not (ok_free and ok_delta)
    print("ALL OK" if not failed else "FAILED")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
