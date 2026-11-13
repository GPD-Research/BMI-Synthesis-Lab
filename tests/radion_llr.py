"""Ledger #4 re-derived with the oscillating-circle dark matter (milestone 6).

03_background.md S3.1 bounded the radion by the *mirror*-DM mass drift (m_DM ~ Omega). Since
milestone 6 the dark matter is the circle modulus chi, whose minimum does not depend on phi
(04d_circle.md S3d), so that bound is gone. What remains for the radion today:
  - Cassini: Omega_0 < 0.032 (unchanged);
  - LLR: |Gdot/G| = 3 Omega^3/(1 - Omega^3) |dln Omega/dt| < 1.5e-13 /yr;
  - the moduli approximation: Omega < 0.5 throughout (no collision before today).
Integrates the canonical radion chi_r = -(4/sqrt3) M_Pl Omega^{3/2}, V = dsigma2 Omega^4, with
matter, radiation and a cosmological constant (the thawing field at c -> 0), from rest at
z ~ 3000; Omega_i is solved so that Omega(today) = Omega_0. Units M_Pl = H0 = 1; v = dsigma2/rho0.

Run:  python3 tests/radion_llr.py
"""
import warnings
import numpy as np
from scipy.integrate import solve_ivp

OM, OR = 0.315, 9.1e-5
OL = 1 - OM - OR
H0YR = 67.4 / 977.8e9
LLR = 1.5e-13
OM_MAX = 0.5
N0 = -8.0


def omega(x):
    return (np.sqrt(3) * abs(x) / 4) ** (2 / 3)


def run(v, om_i):
    def V(x):
        return 3 * v * omega(x) ** 4

    def rhs(N, y):
        x, p = y
        a = np.exp(N)
        rb = 3 * (OM * a ** -3 + OR * a ** -4 + OL)
        H2 = (rb + V(x)) / (3 - p * p / 2)
        eps = (3 * (OM * a ** -3 + 4 / 3 * OR * a ** -4) + H2 * p * p) / (2 * H2)
        return [p, -(3 - eps) * p - (8 / 3) * V(x) / x / H2]

    hit = lambda N, y: omega(y[0]) - OM_MAX
    hit.terminal = True
    s = solve_ivp(rhs, [N0, 0], [-(4 / np.sqrt(3)) * om_i ** 1.5, 0.0], rtol=1e-9, atol=1e-14,
                  method="LSODA", events=hit)
    if s.status != 0 or not np.all(np.isfinite(s.y[:, -1])):
        return None
    x, p = s.y[:, -1]
    H2 = (3 + 3 * v * omega(x) ** 4) / (3 - p * p / 2)
    om = omega(x)
    gdot = 3 * om ** 3 / (1 - om ** 3) * (2 / 3) * p / x * np.sqrt(H2) * H0YR
    return om, gdot, v * om ** 4


def solve(v, om0):
    lo, hi = np.log(om0) - 8, np.log(OM_MAX)
    f = lambda l: (lambda r: 1.0 if r is None else r[0] - om0)(run(v, np.exp(l)))
    if f(lo) > 0 or f(hi) < 0:
        return None
    for _ in range(30):
        m = 0.5 * (lo + hi)
        lo, hi = (lo, m) if f(m) > 0 else (m, hi)
    return run(v, np.exp(lo))


def bound(om0, sgn):
    lo, hi = 2.0, 6.0
    for _ in range(14):
        m = 0.5 * (lo + hi)
        r = solve(sgn * 10 ** m, om0)
        lo, hi = (m, hi) if (r is not None and abs(r[1]) < LLR) else (lo, m)
    r = solve(sgn * 10 ** lo, om0)
    return 10 ** lo, r, "LLR" if r is not None and abs(r[1]) > 0.5 * LLR else "no solution"


def main():
    warnings.simplefilter("ignore")
    om0 = 0.032
    b, r, why = bound(om0, -1)
    print(f"attractive (dsigma2 < 0), Omega_0 = {om0}: |dsigma2| < {b:.3g} rho0 (set by {why}); "
          f"radion potential today {r[2]:+.2e} (net energy: radion_hz.py); old mirror-DM bound {0.15 / om0:.3g} rho0", flush=True)
    assert why == "LLR" and b > 1e3 * 0.15 / om0
    # repulsive: the radion runs to small Omega and Gdot/G stays far below LLR wherever Omega_0 is reachable
    worst = max(abs(x[1]) for x in (solve(v, om0) for v in (1e1, 1e2, 3e2)) if x is not None)
    print(f"repulsive (dsigma2 > 0): max |Gdot/G| = {worst:.1e} /yr over reachable cases -> LLR not binding")
    assert worst < 0.5 * LLR
    print("ALL OK")


if __name__ == "__main__":
    main()
