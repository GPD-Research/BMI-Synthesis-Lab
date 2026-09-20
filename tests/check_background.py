"""Symbolic check of the warped background used in v2/01_action.md and v2/02_effective_4d.md.

Verifies, for a codimension-one warped metric in D dimensions

    ds^2 = e^{-2y/l} eta_ab dx^a dx^b + dy^2            (a runs over D-1 directions)

that the bulk Einstein equation  G_AB = -(Lambda/M^{D-2}) G_AB  holds with
    Lambda = -(D-1)(D-2)/2 * M^{D-2} / l^2,
that the boundary condition  2 M^{D-2} (K_ab - gamma_ab K) = -S_ab  with  S_ab = -sigma gamma_ab
gives  sigma = 2 (D-2) M^{D-2} / l,
and that the 4D Planck mass from integrating the warp over an interval 0..phi is
    M_Pl^2 = M^{D-2} * Vol(extra compact dims) * l/(D-2) * (1 - e^{-(D-2) phi / l}).

It also demonstrates that the *partially* warped metric with an unwarped circle,
    ds^2 = e^{-2y/l} eta_{mu nu} dx dx + dy^2 + dz^2,
is NOT a solution of the D=6 vacuum equations with a cosmological constant.

Requires sympy. Run: python3 tests/check_background.py
"""
import sys

import sympy as sp


def einstein_tensor(coords, g):
    n = len(coords)
    ginv = g.inv()
    Gamma = [[[sp.simplify(sum(ginv[a, d] * (sp.diff(g[d, b], coords[c]) + sp.diff(g[d, c], coords[b])
                                             - sp.diff(g[b, c], coords[d])) for d in range(n)) / 2)
               for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n)
    for b in range(n):
        for c in range(n):
            s = 0
            for a in range(n):
                s += sp.diff(Gamma[a][b][c], coords[a]) - sp.diff(Gamma[a][b][a], coords[c])
                for d in range(n):
                    s += Gamma[a][a][d] * Gamma[d][b][c] - Gamma[a][c][d] * Gamma[d][b][a]
            Ric[b, c] = sp.simplify(s)
    R = sp.simplify(sum(ginv[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    return sp.simplify(Ric - R * g / 2), R


def check_full_warp(D):
    y, l, M = sp.symbols("y ell M", positive=True)
    xs = sp.symbols(f"x0:{D-1}")
    coords = list(xs) + [y]
    eta = sp.diag(*([-1] + [1] * (D - 2)))
    g = sp.zeros(D)
    g[:D - 1, :D - 1] = sp.exp(-2 * y / l) * eta
    g[D - 1, D - 1] = 1
    G, R = einstein_tensor(coords, g)
    Lam = -sp.Rational((D - 1) * (D - 2), 2) * M ** (D - 2) / l ** 2
    resid = sp.simplify(G + Lam / M ** (D - 2) * g)
    ok_bulk = resid == sp.zeros(D)

    # Boundary at y=0, outward normal n = -d/dy (pointing out of the interval y>0).
    # K_ab = -(1/2) n^y d_y gamma_ab = +(1/2) d_y gamma_ab = -(1/l) gamma_ab.
    gam = g[:D - 1, :D - 1]
    K = -gam / l
    trK = sp.simplify(sum(gam.inv()[a, b] * K[a, b] for a in range(D - 1) for b in range(D - 1)))
    lhs = sp.simplify(2 * M ** (D - 2) * (K - gam * trK))
    sigma = sp.symbols("sigma")
    sol = sp.solve(sp.Eq(lhs[1, 1], sigma * gam[1, 1]), sigma)  # -S_ab = +sigma gamma_ab
    ok_sigma = sp.simplify(sol[0] - 2 * (D - 2) * M ** (D - 2) / l) == 0

    # 4D Planck mass: sqrt(-G) R_D contains e^{-(D-1)y/l} * e^{2y/l} R_4 = e^{-(D-3)y/l} R_4
    phi = sp.symbols("phi", positive=True)
    integ = sp.integrate(sp.exp(-(D - 3) * y / l), (y, 0, phi))
    ok_mpl = sp.simplify(integ - l / (D - 3) * (1 - sp.exp(-(D - 3) * phi / l))) == 0
    return ok_bulk, ok_sigma, ok_mpl, Lam, sol[0], integ


def check_partial_warp_6d():
    y, z, l, M, Lam = sp.symbols("y z ell M Lambda", real=True)
    xs = sp.symbols("x0:4")
    coords = list(xs) + [y, z]
    g = sp.zeros(6)
    g[:4, :4] = sp.exp(-2 * y / l) * sp.diag(-1, 1, 1, 1)
    g[4, 4] = 1
    g[5, 5] = 1
    G, R = einstein_tensor(coords, g)
    # Try to solve G_AB = -Lam/M^4 g_AB from the (11) and (zz) components simultaneously.
    e1 = sp.simplify(G[1, 1] + Lam / M ** 4 * g[1, 1])
    e2 = sp.simplify(G[5, 5] + Lam / M ** 4 * g[5, 5])
    s1 = sp.solve(e1, Lam)
    s2 = sp.solve(e2, Lam)
    return s1, s2


def main():
    failed = False
    for D in (5, 6):
        ok_bulk, ok_sigma, ok_mpl, Lam, sig, integ = check_full_warp(D)
        print(f"D={D}: Lambda = {Lam}, sigma = {sig}, int e^-(D-3)y/l dy = {sp.simplify(integ)}")
        print(f"      bulk eq {'OK' if ok_bulk else 'FAIL'}, tension {'OK' if ok_sigma else 'FAIL'}, "
              f"Planck integral {'OK' if ok_mpl else 'FAIL'}")
        failed |= not (ok_bulk and ok_sigma and ok_mpl)
    s1, s2 = check_partial_warp_6d()
    print(f"D=6 with unwarped circle: Lambda from (xx) = {s1}, from (zz) = {s2}")
    if s1 == s2:
        print("      unexpected: partially warped metric solves the vacuum equations")
        failed = True
    else:
        print("      confirmed: NOT a vacuum solution (needs a source); 01_action.md §3 metric corrected")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
