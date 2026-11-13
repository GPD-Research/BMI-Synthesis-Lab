"""Attractive radion (dsigma2 < 0) in H(z): how much of the LLR-allowed range BAO + CMB leave.

radion_llr.py found |dsigma2| < 3.3e4 rho0 at Omega_0 = 0.032 from LLR, with the radion carrying
f_rad ~ -3.5% of the critical density today. Here its energy history f(z) (from rest at z ~ 3000,
Omega(t0) = Omega_0 imposed) is added to the direct-fit background of p2_direct.py, the cosmological
constant retuned for flatness, and (h, omega_b, omega_bc) profiled against DESI DR2 BAO + the
compressed CMB. Moduli approximation, radion on a fixed LCDM background (its back-reaction on the
matter era is < f_rad).

Run:  python3 tests/radion_hz.py
"""
import os
import sys
import warnings
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

sys.path.insert(0, os.path.dirname(__file__))
import radion_llr as R  # noqa: E402
import p2_direct as P   # noqa: E402

OM0 = 0.032


def history(v, om0=OM0):
    """f(N) = rho_rad / rho_crit,0 on P.NG, for Omega(t0) = om0."""
    lo, hi = np.log(om0) - 8, np.log(R.OM_MAX)
    f = lambda l: (lambda r: 1.0 if r is None else r[0] - om0)(R.run(v, np.exp(l)))
    if f(lo) > 0 or f(hi) < 0:
        return None
    for _ in range(40):
        m = 0.5 * (lo + hi)
        lo, hi = (lo, m) if f(m) > 0 else (m, hi)
    V = lambda x: 3 * v * R.omega(x) ** 4

    def H2(N, x, p):
        a = np.exp(N)
        return (3 * (R.OM * a ** -3 + R.OR * a ** -4 + R.OL) + V(x)) / (3 - p * p / 2)

    def rhs(N, y):
        x, p = y
        a = np.exp(N)
        h2 = H2(N, x, p)
        eps = (3 * (R.OM * a ** -3 + 4 / 3 * R.OR * a ** -4) + h2 * p * p) / (2 * h2)
        return [p, -(3 - eps) * p - (8 / 3) * V(x) / x / h2]

    s = solve_ivp(rhs, [R.N0, 0], [-(4 / np.sqrt(3)) * np.exp(lo) ** 1.5, 0.0], rtol=1e-9,
                  atol=1e-14, method="LSODA", dense_output=True)
    N = np.clip(P.NG, R.N0, 0)
    x, p = s.sol(N)
    return np.where(P.NG < R.N0, 0.0, (H2(N, x, p) * p * p / 2 + V(x)) / 3)


def chi2_min(fz, data):
    def c2(q):
        h, wb, wbc = q
        ode = (h * h - P.om_other(1.0, wbc)) + h * h * (fz - fz[-1])
        if np.any(P.om_other(np.exp(P.NG), wbc) + ode <= 0):
            return 1e10
        return sum(P.chi2_terms(P.Background(h, wb, wbc, ode, data), data, None))
    r = minimize(c2, P.START, method="Nelder-Mead", options={"xatol": 1e-6, "fatol": 1e-4, "maxiter": 4000})
    return r.fun


def main():
    warnings.simplefilter("ignore")
    data = dict(np.load(P.DATA, allow_pickle=True))
    c0 = chi2_min(np.zeros_like(P.NG), data)
    print(f"Omega_0 = {OM0}; LCDM chi2 (BAO + CMB) = {c0:.2f}")
    print("|dsigma2|/rho0 | f_rad today | dchi2")
    rows = []
    for v in (1e2, 1e3, 3e3, 1e4, 3.3e4):
        fz = history(-v)
        if fz is None:
            print(f"{v:9.3g} | no solution"); continue
        d = chi2_min(fz, data) - c0
        rows.append((v, fz[-1], d))
        print(f"{v:9.3g} | {fz[-1]:+.2e} | {d:+.2f}", flush=True)
    ok = [r for r in rows if r[2] < 4]
    print(f"allowed (dchi2 < 4): |dsigma2| up to {max(r[0] for r in ok):.3g} rho0, |f_rad| up to {max(-r[1] for r in ok):.2e}")
    assert all(abs(r[2]) < 1 for r in rows) and -rows[-1][1] < 5e-3
    print("ALL OK")


if __name__ == "__main__":
    main()
