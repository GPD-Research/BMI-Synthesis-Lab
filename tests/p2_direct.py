"""P2 without the CPL projection (06_predictions.md S4d).

Fits the thawing w(z) of V = V0 exp(-c Phi) directly to DESI DR2 BAO + a compressed Planck CMB
prior (+ optionally SNe), with LCDM and CPL fitted the same way for reference. Background: flat,
N_eff = 3.044, one 0.06 eV neutrino. CMB: Gaussian in (100 theta_MC, omega_b, omega_bc) from the
DESI-release Planck+ACT-lensing base_w chains; r_d and theta_MC use the Eisenstein-Hu z_drag and
Hu-Sugiyama z_*, each rescaled by one constant fitted to CAMB's values in the DESI chains.

    python3 tests/p2_direct.py                   # BAO + CMB (the registered combination)
    python3 tests/p2_direct.py --sn SN_DATA      # also Pantheon+, Union3, DESY5 (CobayaSampler/sn_data)
    python3 tests/p2_direct.py --build DESI_ROOT # rebuild tests/data/p2_direct_bao_cmb.npz
"""
import os
import sys
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq, minimize

C_KM = 299792.458
OMG = 2.4728e-5                       # photons, T0 = 2.7255 K
NEFF = 3.044
MNU = 0.06                            # one massive neutrino [eV]
TNU = 1.6764e-4                       # T_nu0 [eV]
F_NU = 7 / 8 * (4 / 11) ** (4 / 3)
OMR = OMG * (1 + F_NU * NEFF * 2 / 3)          # photons + two massless species
OMNU_REL = OMG * F_NU * NEFF / 3               # the massive species while relativistic
XNU = MNU / (3.151 * TNU)
OMNU0 = OMNU_REL * np.sqrt(1 + XNU ** 2)
N_INIT = -8.0                         # z ~ 3000: field frozen by Hubble friction


def om_nu(a):
    return OMNU_REL * a ** -4 * np.sqrt(1 + (XNU * a) ** 2)


def om_other(a, wbc):
    """Physical density of everything but dark energy (omega = rho / rho_crit,100)."""
    return wbc * a ** -3 + OMR * a ** -4 + om_nu(a)


def p_other(a, wbc):
    """3 x pressure + density, i.e. sum (1 + w_i) rho_i, for the Raychaudhuri equation."""
    x2 = (XNU * a) ** 2
    return wbc * a ** -3 + 4 / 3 * OMR * a ** -4 + om_nu(a) * (1 + 1 / (3 * (1 + x2)))


# ---- sound horizons (DE-free; calibrated to CAMB in calibrate()) ---------------------------------
def r_s(a_end, wb, wbc):
    f = lambda la: C_KM / (np.exp(la) * 100 * np.sqrt(om_other(np.exp(la), wbc))
                           * np.sqrt(3 * (1 + 0.75 * wb / OMG * np.exp(la))))
    return quad(f, -25, np.log(a_end), epsabs=0, epsrel=1e-9, limit=200)[0]


def z_star(wb, wbc):
    wdm = wbc - wb + OMNU0
    g1 = 0.0783 * wb ** -0.238 / (1 + 39.5 * wb ** 0.763)
    g2 = 0.560 / (1 + 21.1 * wb ** 1.81)
    return 1048 * (1 + 0.00124 * wb ** -0.738) * (1 + g1 * (wdm + wb) ** g2)


def z_drag(wb, wbc):
    wm = wbc + OMNU0
    b1 = 0.313 * wm ** -0.419 * (1 + 0.607 * wm ** 0.674)
    b2 = 0.238 * wm ** 0.223
    return 1291 * wm ** 0.251 / (1 + 0.659 * wm ** 0.828) * (1 + b1 * wb ** b2)


# ---- dark energy models: return omega_DE(N) on the N grid (physical units) ------------------------
NG = np.linspace(N_INIT, 0, 3001)


def de_cpl(h, wbc, w0, wa):
    a = np.exp(NG)
    ode0 = h * h - om_other(1.0, wbc)
    return ode0 * a ** (-3 * (1 + w0 + wa)) * np.exp(-3 * wa * (1 - a))


def de_thawing(h, wbc, c):
    """Canonical field, V = V* exp(-c phi), frozen at N_INIT; V* shot to flatness."""
    if c == 0:
        return de_cpl(h, wbc, -1.0, 0.0)
    h2 = h * h
    oth = lambda N: om_other(np.exp(N), wbc) / h2           # units of 3 H0^2 (M_Pl = 1, H0 = 1)
    poth = lambda N: p_other(np.exp(N), wbc) / h2
    ode0 = 1 - oth(0.0)

    def H2(N, phi, dphi, Vs):
        return (oth(N) + Vs * np.exp(-c * phi) / 3) / (1 - dphi ** 2 / 6)

    def rhs(N, y, Vs):
        phi, dphi = y
        E2 = H2(N, phi, dphi, Vs)
        hp = -1.5 * poth(N) / E2 - dphi ** 2 / 2
        return [dphi, -(3 + hp) * dphi + c * Vs * np.exp(-c * phi) / E2]

    def solve(lnV):
        return solve_ivp(rhs, (N_INIT, 0.0), [0.0, 0.0], args=(np.exp(lnV),), rtol=1e-8, atol=1e-11,
                         dense_output=True)

    def miss(lnV):
        s = solve(lnV)
        phi, dphi = s.y[:, -1]
        E2 = H2(0.0, phi, dphi, np.exp(lnV))
        return (E2 * dphi ** 2 / 6 + np.exp(lnV - c * phi) / 3) / E2 - ode0

    lnV = brentq(miss, np.log(3 * ode0), np.log(3 * ode0) + 3.0, xtol=1e-9)
    phi, dphi = solve(lnV).sol(NG)
    E2 = H2(NG, phi, dphi, np.exp(lnV))
    return h2 * (E2 - oth(NG))


# ---- observables ---------------------------------------------------------------------------------
class Background:
    def __init__(self, h, wb, wbc, ode, cal):
        self.h, self.wb, self.wbc = h, wb, wbc
        a = np.exp(NG)
        Hz = 100 * np.sqrt(om_other(a, wbc) + ode)          # km/s/Mpc on NG
        self.z = 1 / a[::-1] - 1
        self.H = Hz[::-1]
        integrand = C_KM / self.H
        self.chi = np.concatenate([[0], np.cumsum(0.5 * (integrand[1:] + integrand[:-1]) * np.diff(self.z))])
        self.rd = cal["cal_rd"] * r_s(1 / (1 + z_drag(wb, wbc)), wb, wbc)
        zs = z_star(wb, wbc)
        self.theta100 = cal["cal_theta"] * 100 * r_s(1 / (1 + zs), wb, wbc) / self.DM(zs)

    def DM(self, z):
        return np.interp(z, self.z, self.chi)

    def DH(self, z):
        return C_KM / np.interp(z, self.z, self.H)


def bao_vector(bg, data):
    out = []
    for z, kind in zip(data["bao_z"], data["bao_kind"]):
        if kind == 0:
            v = (z * bg.DM(z) ** 2 * bg.DH(z)) ** (1 / 3)
        elif kind == 1:
            v = bg.DM(z)
        else:
            v = bg.DH(z)
        out.append(v / bg.rd)
    return np.array(out)


def chi2_terms(bg, data, sn):
    d = bao_vector(bg, data) - data["bao_mean"]
    c_bao = d @ data["bao_icov"] @ d
    x = np.array([bg.theta100, bg.wb, bg.wbc]) - data["cmb_mean"]
    c_cmb = x @ data["cmb_icov"] @ x
    c_sn = 0.0
    if sn is not None:
        mu = 5 * np.log10((1 + sn["zhel"]) * bg.DM(sn["z"]))
        r = sn["mu"] - mu
        u = sn["icov"] @ r
        c_sn = r @ u - u.sum() ** 2 / sn["isum"]
    return c_bao, c_cmb, c_sn


# ---- data ----------------------------------------------------------------------------------------
KIND = {"DV_over_rs": 0, "DM_over_rs": 1, "DH_over_rs": 2}


def load_sn(root, name):
    if name == "pantheonplus":
        t = np.genfromtxt(os.path.join(root, "PantheonPlus/Pantheon+SH0ES.dat"), names=True, dtype=None,
                          encoding=None)
        cov = np.loadtxt(os.path.join(root, "PantheonPlus/Pantheon+SH0ES_STAT+SYS.cov"), skiprows=1)
        n = len(t)
        cov = cov.reshape(n, n)
        m = t["zHD"] > 0.01
        z, zhel, mu, cov = t["zHD"][m], t["zHEL"][m], t["m_b_corr"][m], cov[np.ix_(m, m)]
    elif name == "desy5sn":
        t = np.genfromtxt(os.path.join(root, "DESY5/DES-SN5YR_HD.csv"), names=True, delimiter=",")
        cs = np.loadtxt(os.path.join(root, "DESY5/covsys_000.txt"))
        n = int(cs[0])
        cov = cs[1:].reshape(n, n) + np.diag(t["MUERR_FINAL"] ** 2)
        z, zhel, mu = t["zHD"], t["zHEL"], t["MU"]
    elif name == "union3":
        t = np.loadtxt(os.path.join(root, "Union3/lcparam_full.txt"), usecols=(1, 2, 4, 5))
        cs = np.loadtxt(os.path.join(root, "Union3/mag_covmat.txt"))
        n = int(cs[0])
        cov = cs[1:].reshape(n, n) + np.diag(t[:, 3] ** 2)
        z, zhel, mu = t[:, 0], t[:, 1], t[:, 2]
    else:
        return None
    icov = np.linalg.inv(cov)
    return dict(z=z, zhel=zhel, mu=mu, icov=icov, isum=icov.sum())


def chi2(model, p, data, sn):
    if model == "lcdm":
        h, wb, wbc = p
        ode = de_cpl(h, wbc, -1, 0)
    elif model == "cpl":
        h, wb, wbc, w0, wa = p
        if w0 + wa >= 0:
            return 1e10
        ode = de_cpl(h, wbc, w0, wa)
    else:
        h, wb, wbc, c = p
        ode = de_thawing(h, wbc, abs(c))
    return sum(chi2_terms(Background(h, wb, wbc, ode, data), data, sn))


def best(model, data, sn, start):
    r = minimize(lambda p: chi2(model, p, data, sn), start, method="Nelder-Mead",
                 options=dict(xatol=1e-6, fatol=1e-4, maxiter=6000, maxfev=6000))
    r2 = minimize(lambda p: chi2(model, p, data, sn), r.x, method="Nelder-Mead",
                  options=dict(xatol=1e-7, fatol=1e-5, maxiter=6000, maxfev=6000))
    return r2.fun, r2.x


DATA = os.path.join(os.path.dirname(__file__), "data", "p2_direct_bao_cmb.npz")
CHAINS = os.path.join(os.path.dirname(__file__), "data", "desi_dr2_w0wa.npz")
SETS = {"none": "no SNe", "pantheonplus": "Pantheon+", "union3": "Union3", "desy5sn": "DESY5"}
START = [0.68, 0.0222, 0.1417]
C_GRID = np.arange(0.2, 1.31, 0.2)
DCHI2_95_2D = 5.991


def build(root):
    import glob
    rows = []
    for f in sorted(glob.glob(os.path.join(root, "planck_w", "chain.[1-4].txt"))):
        names = open(f).readline().lstrip("#").split()
        d = np.loadtxt(f)
        d = d[int(0.3 * len(d)):]
        col = lambda k: d[:, names.index(k)]
        rows.append(np.c_[col("theta_MC_100"), col("ombh2"), col("ombh2") + col("omch2"), col("weight")])
    if len(rows) != 4:
        raise SystemExit("expected 4 Planck base_w chains in planck_w/")
    d = np.vstack(rows)
    m = np.average(d[:, :3], axis=0, weights=d[:, 3])
    cov = np.cov(d[:, :3].T, aweights=d[:, 3])
    rr, tt = [], []
    for key in list(SETS) + ["planck_w"]:
        f = os.path.join(root, key, "chain.1.txt")
        names = open(f).readline().lstrip("#").split()
        for row in np.loadtxt(f)[-3000::150]:
            g = lambda k: row[names.index(k)]
            h, wb = g("H0") / 100, g("ombh2")
            wbc = wb + g("omch2")
            wa = g("wa") if "wa" in names else 0.0
            bg = Background(h, wb, wbc, de_cpl(h, wbc, g("w"), wa), {"cal_rd": 1, "cal_theta": 1})
            rr.append(g("rdrag") / bg.rd)
            tt.append(g("theta_MC_100") / bg.theta100)
    print(f"calibration: r_d x {np.mean(rr):.5f} (scatter {np.std(rr):.1e}), "
          f"theta_MC x {np.mean(tt):.6f} (scatter {np.std(tt):.1e}), {len(rr)} chain samples")
    b = np.loadtxt(os.path.join(root, "lik", "desi_gaussian_bao_ALL_GCcomb_mean.txt"), dtype=str)
    bc = np.loadtxt(os.path.join(root, "lik", "desi_gaussian_bao_ALL_GCcomb_cov.txt"))
    np.savez_compressed(DATA, bao_z=b[:, 0].astype(float), bao_mean=b[:, 1].astype(float),
                        bao_kind=np.array([KIND[k] for k in b[:, 2]]), bao_icov=np.linalg.inv(bc),
                        cmb_mean=m, cmb_icov=np.linalg.inv(cov), cal_rd=np.mean(rr), cal_theta=np.mean(tt))
    print("wrote", DATA)


def run(key, data, sn):
    r = {"lcdm": best("lcdm", data, sn, START)}
    r["cpl"] = best("cpl", data, sn, START + [-0.75, -0.8])
    p, prof = list(r["lcdm"][1]), []
    for c in C_GRID:
        fit = minimize(lambda q: chi2("thaw", [*q, c], data, sn), p, method="Nelder-Mead",
                       options=dict(xatol=1e-7, fatol=1e-5, maxfev=2000))
        p = list(fit.x)
        prof.append((c, fit.fun, p))
    c0, f0, p0 = min(prof, key=lambda t: t[1])
    r["thaw"] = best("thaw", data, sn, [*p0, c0]) if f0 < r["lcdm"][0] else (r["lcdm"][0], [*r["lcdm"][1], 0.0])
    r["prof"] = prof
    return r


def main():
    if "--build" in sys.argv:
        build(sys.argv[sys.argv.index("--build") + 1])
        return
    from scipy.stats import chi2 as chi2dist, norm
    data = dict(np.load(DATA))
    chains = np.load(CHAINS)
    sn_root = sys.argv[sys.argv.index("--sn") + 1] if "--sn" in sys.argv else None
    keys = list(SETS) if sn_root else ["none"]
    print("BAO + CMB + | chi2 LCDM | chi2 CPL (w0, wa) | chi2 thawing (c) | thawing - CPL | LCDM - thawing")
    res = {}
    for k in keys:
        r = res[k] = run(k, data, load_sn(sn_root, k) if sn_root else None)
        (fl, _), (fc, pc), (ft, pt) = r["lcdm"], r["cpl"], r["thaw"]
        d = ft - fc
        r["level"] = chi2dist.cdf(d, 2)
        print(f"{SETS[k]:10s} | {fl:9.2f} | {fc:9.2f} ({pc[3]:+.3f}, {pc[4]:+.2f}) | {ft:9.2f} ({abs(pt[3]):.2f}) | "
              f"{d:5.2f} ({100 * r['level']:.1f}%, {norm.isf((1 - r['level']) / 2):.1f} sigma 2D) | {fl - ft:5.2f}")
        s = chains[k].astype(float)
        mean = np.average(s[:, :2], axis=0, weights=s[:, 2])
        assert abs(pc[3] - mean[0]) < 0.08 and abs(pc[4] - mean[1]) < 0.3, (k, pc[3:], mean)
        assert ft <= fl + 1e-3 and fc <= ft + 1e-3, k
    fired = [k for k in keys if res[k]["level"] > 0.95]
    print(f"\nKill criterion 2, direct fit: best thawing c outside the 95% (2D) region of the CPL best fit for "
          f"{len(fired)} of {len(keys)} ({', '.join(SETS[k] for k in fired) or 'none'})")
    assert "none" in fired
    print("ALL OK")


if __name__ == "__main__":
    main()
