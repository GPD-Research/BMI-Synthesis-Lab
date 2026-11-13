"""09_clock_effect.md S3a. B: damped ring-down G(z) from recombination, vs DESI DR2 BAO + compressed CMB; stellar speed-up."""
import os, sys, numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import p2_direct as P
from scipy.optimize import minimize
data = dict(np.load(P.DATA, allow_pickle=True))
NG = P.NG
def g_of(z, A, lam, p, phase):
    # ln a measured from recombination; amplitude decays as (a/a_rec)^-p; period lam in e-folds
    N = -np.log1p(z); Nrec = -np.log(1091.0)
    x = np.clip(N - Nrec, 0, None)
    return np.where(N > Nrec, A * np.exp(-p * x) * np.cos(2 * np.pi * x / lam + phase), 0.0)
class BG(P.Background):
    def __init__(self, h, wb, wbc, ring, cal):
        self.h, self.wb, self.wbc = h, wb, wbc
        a = np.exp(NG); z = 1 / a - 1
        ode = P.de_cpl(h, wbc, -1, 0)
        Hz = 100 * np.sqrt((P.om_other(a, wbc) + ode) * (1 + g_of(z, *ring)))
        self.z = 1 / a[::-1] - 1; self.H = Hz[::-1]
        ig = P.C_KM / self.H
        self.chi = np.concatenate([[0], np.cumsum(0.5 * (ig[1:] + ig[:-1]) * np.diff(self.z))])
        self.rd = cal["cal_rd"] * P.r_s(1 / (1 + P.z_drag(wb, wbc)), wb, wbc)
        zs = P.z_star(wb, wbc)
        self.theta100 = cal["cal_theta"] * 100 * P.r_s(1 / (1 + zs), wb, wbc) / self.DM(zs)
def chi2(p, ring):
    return sum(P.chi2_terms(BG(*p, ring, data), data, None))
def prof(ring):
    r = minimize(lambda p: chi2(p, ring), P.START, method="Nelder-Mead", options={"xatol":1e-6,"fatol":1e-4,"maxiter":3000})
    return r.fun
c0 = prof((0, 1, 0, 0))
from scipy.integrate import quad
OM, OR = 0.315, 9.1e-5; GYR = 977.8 / 67.4
E = lambda z: np.sqrt(OM*(1+z)**3 + OR*(1+z)**4 + 1-OM-OR)
def speed(z, ring, n):
    t = quad(lambda x: 1/((1+x)*E(x)), z, 1091, limit=400)[0]
    te = quad(lambda x: (1 + float(g_of(np.array([x]), *ring)[0]))**n / ((1+x)*E(x)), z, 1091, limit=400)[0]
    return te / t   # stellar-time multiplier over the post-recombination interval
print(f"LCDM chi2 = {c0:.2f}")
print("A_rec | period (e-folds) | decay p | dchi2 | speed-up z=7.27 (n=4, 7.5) | z=14")
FULL = "--full" in sys.argv
cases = [(A, lam, pd) for A in (0.03, 0.1, 0.3) for lam in (0.5, 1.5) for pd in (0.5, 1.0)] if FULL \
    else [(0.3, 1.5, 0.5)]
worst = 0.0
for A, lam, pdec in cases:
    if True:
        if True:
            ring = (A, lam, pdec, 0.0)
            d = prof(ring) - c0
            print(f"{A:5} | {lam:4} | {pdec:3} | {d:7.2f} | {speed(7.27, ring, 4):.3f} {speed(7.27, ring, 7.5):.3f} | {speed(14, ring, 4):.3f} {speed(14, ring, 7.5):.3f}", flush=True)
            worst = max(worst, speed(7.27, ring, 7.5), speed(14, ring, 7.5))
assert worst < 1.2, "a recombination ring-down should not reach the x1.9 the galaxies need"
print("ALL OK")
