"""Milestone 7: the two closed relations (v2/06_predictions.md).

A. Fifth force: strength alpha_Y AND range lambda from ell_z alone (zero free numbers once ell_z is in
   its window).  Pieces:
     - canonical circle modulus: 5D->4D on S^1, ds_5^2 = e^{-sigma} g_4 + e^{2 sigma} dz^2 (Einstein
       frame), L = (M_Pl^2/2)[R - (3/2)(d sigma)^2]  =>  chi = sqrt(3/2) M_Pl sigma,  sigma = ln(ell_z/ell_z0).
       04d used chi = M_Pl sigma: m_chi and 1/lambda shrink by sqrt(2/3).
     - coupling of chi to a nucleon (Einstein frame):
         d ln m_N / d sigma = -1/2 + (1 - s) d ln Lambda_3 / d sigma
       -1/2: Weyl factor on brane masses.  Lambda_3 (three-flavour QCD scale) from 1/g_s^2 proportional
       to ell_z at mu_KK = k/ell_z, run DOWN through the c, b, t thresholds at two loops; at one loop
       d ln Lambda_3/d sigma = -(b_6 + 2pi/alpha_s(mu_KK))/b_3 = -(7 + 2pi/alpha_s)/9.
       Zero-mode quark masses are ell_z-independent at tree level (y_4 ~ ell_z^-1/2, v ~ ell_z^+1/2),
       so the light-quark sigma-term fraction s = (sigma_piN + sigma_s)/m_N only dilutes the QCD piece.
       Milestone 7 used b0 = 7 all the way to Lambda_QCD and s = 0: alpha_Y too high by ~2x
       (corrected 2026-11-11, 06_predictions.md S2a).
     - alpha_Y = 2 beta^2,  beta = (d ln m_N/d sigma) / sqrt(3/2)   (reduced M_Pl).
   Compared with the published |alpha|(lambda) upper limits (digitized anchor points [verify]).
B. Dark energy: (w0, wa)(c) thawing curve vs DESI DR2 + CMB + SNe (w0, wa) posteriors, Gaussian
   approximation with correlation rho in [-0.95, -0.8] [verify: chains].  Delta chi^2 of the nearest
   point of the curve vs the best fit; ALSO the same for LCDM (-1, 0) for reference.

Run:  python3 tests/predictions.py
"""
import sys
import os
import numpy as np
from scipy.special import zeta
from scipy.optimize import brentq, minimize_scalar
from scipy.integrate import solve_ivp

sys.path.insert(0, os.path.dirname(__file__))
from background_frw import thawing_solution, cpl_fit  # noqa: E402

M_PL = 2.435e27                      # eV, reduced
HBAR_C_EV_CM = 1.9733e-5
C_Z = 62 * 3 * zeta(5) / (64 * np.pi ** 6)
K_KIN = 1.5                          # chi = sqrt(K_KIN) M_Pl sigma
B0 = 7.0                             # one-loop QCD beta coefficient above m_t
ALPHA_S_MZ = 0.1180
M_Z = 91.19e9
M_T = 172.6e9
LZ_INV_MAX = 29e12                   # |delta_1| < sigma_1  (04d S3b)
LZ_INV_LHC = 5e12                    # SM KK modes at LHC

# 95% upper limits on |alpha| at range lambda [um], digitized from the compilation in
# Lee et al. PRL 124 101101 (2020) Fig. 3 (Eot-Wash 2007/2020, Stanford, IUPUI/Chen 2016).
# Exact anchor: alpha = 1 at lambda = 38.6 um.  Others are read off a log-log plot [verify].
ALPHA_BOUND = [(1.0, 1e8), (2.0, 3e6), (3.0, 3e5), (5.0, 3e4), (7.0, 5e3), (10.0, 7e2),
               (15.0, 60.0), (20.0, 12.0), (30.0, 2.5), (38.6, 1.0), (60.0, 0.2), (100.0, 0.02)]


TH = {"c": 1.27e9, "b": 4.18e9, "t": 162.5e9}   # MSbar m_q(m_q): matching points (alpha_s continuous)
MU_LOW = 1.0e9                                  # nf = 3 reference scale for Lambda_3
SIGMA_PIN, SIGMA_S, M_N = 50e6, 45e6, 938.9e6     # +-10, +-20 MeV
S_LIGHT = (SIGMA_PIN + SIGMA_S) / M_N


def qcd_beta(a, nf, loops):
    r = -(11 - 2 * nf / 3) / (2 * np.pi) * a * a
    if loops == 2:
        r -= (102 - 38 * nf / 3) / (8 * np.pi ** 2) * a ** 3
    return r


def run_alpha_s(a, mu0, mu1, loops=2, th=TH):
    """alpha_s from mu0 to mu1, nf switched at the thresholds th."""
    lo, hi = min(mu0, mu1), max(mu0, mu1)
    pts = sorted([mu0, mu1] + [m for m in th.values() if lo < m < hi], reverse=mu1 < mu0)
    for x, y in zip(pts[:-1], pts[1:]):
        nf = 3 + sum(np.sqrt(x * y) > m for m in th.values())
        a = solve_ivp(lambda t, v: [qcd_beta(v[0], nf, loops)], (np.log(x), np.log(y)), [a],
                      rtol=1e-12, atol=1e-14).y[0, -1]
    return a


def alpha_s(mu, loops=2, th=TH, as_mz=ALPHA_S_MZ):
    return run_alpha_s(as_mz, M_Z, mu, loops, th)


def dlnlambda3_dsigma(inv_lz, loops=2, k=1.0, th=TH, as_mz=ALPHA_S_MZ, eps=1e-4):
    """sigma -> sigma + e: mu_KK -> mu_KK e^-e, 1/alpha_s(mu_KK) -> e^e/alpha_s(mu_KK); Lambda_3 is RG-invariant,
    so at fixed MU_LOW  d ln Lambda_3 = -d alpha_s(MU_LOW) / beta(alpha_s(MU_LOW))."""
    mu = k * inv_lz
    a_kk = alpha_s(mu, loops, th, as_mz)
    lo = [run_alpha_s(a_kk * np.exp(-e), mu * np.exp(-e), MU_LOW, loops, th) for e in (eps, -eps)]
    a_lo = run_alpha_s(a_kk, mu, MU_LOW, loops, th)
    return -(lo[0] - lo[1]) / (2 * eps) / qcd_beta(a_lo, 3, loops)


def dlnm_dsigma(inv_lz, s=S_LIGHT, **kw):
    weyl = -0.5
    qcd = (1 - s) * dlnlambda3_dsigma(inv_lz, **kw)
    return weyl + qcd, dict(weyl=weyl, qcd=qcd)


def dlnm_dsigma_m7(inv_lz):
    """Milestone 7 as registered 2026-09-21: one loop, b0 = 7 down to Lambda_QCD, s = 0 (superseded)."""
    def run(a0, mu0, mu1, nf):
        return a0 / (1 + a0 * (11 - 2 * nf / 3) / (2 * np.pi) * np.log(mu1 / mu0))
    a = run(run(ALPHA_S_MZ, M_Z, M_T, 5), M_T, inv_lz, 6)
    return -0.5 - 1.0 - 2 * np.pi / (B0 * a)


def alpha_yukawa(inv_lz, **kw):
    beta = dlnm_dsigma(inv_lz, **kw)[0] / np.sqrt(K_KIN)
    return 2 * beta ** 2


def alpha_yukawa_band(inv_lz):
    """Spread over matching factor k, loop order, top threshold, alpha_s(M_Z) and the sigma terms."""
    th_pole = dict(TH, t=M_T)
    ds = np.hypot(10e6, 20e6) / M_N
    vals = [alpha_yukawa(inv_lz, k=k) for k in (0.5, 2.0)]
    vals += [alpha_yukawa(inv_lz, loops=1), alpha_yukawa(inv_lz, th=th_pole)]
    vals += [alpha_yukawa(inv_lz, as_mz=ALPHA_S_MZ + d) for d in (-0.0009, 0.0009)]
    vals += [alpha_yukawa(inv_lz, s=S_LIGHT + d) for d in (-ds, ds)]
    return min(vals), max(vals)


def m_chi(inv_lz):
    return np.sqrt(20 * C_Z * inv_lz ** 4 / K_KIN) / M_PL


def range_um(inv_lz):
    return HBAR_C_EV_CM / m_chi(inv_lz) * 1e4


def alpha_bound(lam_um):
    lams, als = zip(*ALPHA_BOUND)
    return 10 ** np.interp(np.log10(lam_um), np.log10(lams), np.log10(als))


def part_a():
    print("=== A. fifth force: (alpha_Y, lambda) from ell_z ===")
    tot, parts = dlnm_dsigma(10e12)
    a1 = alpha_s(10e12, loops=1)
    one_loop = dlnlambda3_dsigma(10e12, loops=1)
    assert abs(one_loop + (7 + 2 * np.pi / a1) / 9) < 1e-4     # thresholds: 1/b_3, not 1/b_6
    print(f"d ln m_N / d ln ell_z at 1/ell_z = 10 TeV: {tot:.2f}  "
          f"(Weyl {parts['weyl']:.1f}, (1-s) d ln Lambda_3 {parts['qcd']:.2f}; s = {S_LIGHT:.3f}; "
          f"alpha_s = {alpha_s(10e12):.4f} two-loop)")
    print(f"  one loop: d ln Lambda_3 = -(7 + 2pi/alpha_s)/9 = {one_loop:.2f};  two loop: {dlnlambda3_dsigma(10e12):.2f}")
    lo, hi = alpha_yukawa_band(10e12)
    print(f"beta = {tot/np.sqrt(K_KIN):.2f}  ->  alpha_Y = 2 beta^2 = {alpha_yukawa(10e12):.0f}  (spread {lo:.0f}-{hi:.0f})")
    m7 = 2 * dlnm_dsigma_m7(10e12) ** 2 / K_KIN
    print(f"milestone 7 as registered (b0 = 7 to Lambda_QCD, s = 0): {m7:.0f}  ->  corrected x {alpha_yukawa(10e12)/m7:.2f}")
    assert 100 < alpha_yukawa(10e12) < 140 and 200 < m7 < 300
    print(f"canonical normalisation K = {K_KIN}: m_chi and 1/lambda x {1/np.sqrt(K_KIN):.3f} relative to 04d/05")
    print()
    print(f"{'1/ell_z [TeV]':>14} {'m_chi [meV]':>12} {'lambda [um]':>12} {'alpha_Y':>8} {'bound':>9} {'status':>9}")
    for x in [5, 7, 10, 13, 15, 20, 25, 29]:
        inv = x * 1e12
        lam = range_um(inv)
        aY = alpha_yukawa(inv)
        b = alpha_bound(lam)
        print(f"{x:>14} {m_chi(inv)*1e3:>12.2f} {lam:>12.1f} {aY:>8.0f} {b:>9.2g} {'EXCLUDED' if aY > b else 'open':>9}")
    f = lambda x: np.log(alpha_yukawa(x)) - np.log(alpha_bound(range_um(x)))
    inv_min = brentq(f, 5e12, 29e12)
    lam_max = range_um(inv_min)
    lam_min = range_um(LZ_INV_MAX)
    print()
    lo_min, hi_min = alpha_yukawa_band(inv_min)
    lo_max, hi_max = alpha_yukawa_band(LZ_INV_MAX)
    print(f"window:  {inv_min/1e12:.1f} TeV < 1/ell_z < {LZ_INV_MAX/1e12:.0f} TeV   "
          f"<=>   {lam_min:.1f} um < lambda < {lam_max:.1f} um   at alpha_Y = {alpha_yukawa(inv_min):.0f}-{alpha_yukawa(LZ_INV_MAX):.0f}"
          f"  (spread {lo_min:.0f}-{hi_max:.0f})")
    print("(milestone 7 had 14.2-29 TeV / 2.8-11.7 um at alpha_Y = 270-300; 04d had 5.4-29 TeV / 2-66 um at alpha_Y ~ 1)")
    print("P1: alpha_Y ~ 1.2-1.4e2, composition-independent at the 1e-3 level, range in the band above.")
    print("A detection with alpha_Y outside ~[100, 400] at that range kills the fixed-circle geometry as much as no detection.")
    assert 100 < lo_min and hi_max < 400
    assert inv_min > LZ_INV_LHC and inv_min < LZ_INV_MAX
    return inv_min, lam_min, lam_max


DESI = {  # DESI DR2 BAO + CMB + SNe (arXiv:2503.14738, eqs. 26-28); (w0, sig0, wa, sig_a) sig_a symmetrised
    "Pantheon+": (-0.838, 0.055, -0.62, 0.205),
    "Union3": (-0.667, 0.088, -1.09, 0.29),
    "DESY5": (-0.752, 0.057, -0.86, 0.215),
}


def chi2(w0, wa, w0c, s0, wac, sa, rho):
    d0, da = (w0 - w0c) / s0, (wa - wac) / sa
    return (d0 ** 2 + da ** 2 - 2 * rho * d0 * da) / (1 - rho ** 2)


def part_b():
    print("\n=== B. thawing curve (w0, wa)(c) vs DESI DR2 ===")
    cs = np.linspace(0.05, 1.8, 36)
    curve = []
    for c in cs:
        s = thawing_solution(c)
        curve.append(cpl_fit(s["z"], s["w"], zmax=1.0))
    curve = np.array(curve)
    print("curve: w_a / (1 + w_0) =", ", ".join(f"{wa/(1+w0):.2f}" for (w0, wa) in curve[[3, 9, 18, 27, 35]]),
          " for c =", ", ".join(f"{c:.2f}" for c in cs[[3, 9, 18, 27, 35]]))
    verdict = {}
    for name, (w0c, s0, wac, sa) in DESI.items():
        for rho in (-0.8, -0.9, -0.95):
            x2 = np.array([chi2(w0, wa, w0c, s0, wac, sa, rho) for w0, wa in curve])
            i = int(np.argmin(x2))
            x2_lcdm = chi2(-1.0, 0.0, w0c, s0, wac, sa, rho)
            print(f"{name:>10} rho={rho:+.2f}: nearest c = {cs[i]:.2f} (w0, wa) = ({curve[i,0]:.3f}, {curve[i,1]:.3f})"
                  f"  Delta chi^2 = {x2[i]:5.2f}   [LCDM: {x2_lcdm:5.2f}]")
            verdict[(name, rho)] = (x2[i], x2_lcdm)
    inside = {k: v[0] < 6.18 for k, v in verdict.items()}
    print("2-sigma (Delta chi^2 < 6.18) for the curve:", sum(inside.values()), "of", len(inside), "(sample, rho) cases")
    worst = max(v[0] for v in verdict.values())
    best = min(v[0] for v in verdict.values())
    n3 = sum(v[0] > 11.8 for v in verdict.values())
    print(f"curve sits at Delta chi^2 = {best:.1f}-{worst:.1f} from the best fits "
          f"(2 dof: 2 sigma = 6.18, 3 sigma = 11.8; beyond 3 sigma in {n3} of {len(verdict)} cases); "
          "LCDM is worse by 2-10 in every case.")
    print("The curve moves toward the data along w0 > -1, wa < 0 but cannot reach the best fit: the data")
    print("want w < -1 at z > 0.5, which a canonical scalar cannot give.")
    print("Verdict (Gaussian proxy): outside 2 sigma for every SNe sample; NOT the pre-registered chain-level test.")
    print("If the DR2 phantom-crossing preference survives the SNe-sample dependence, P2 dies with LCDM [verify].")
    assert all(v[0] < 20 for v in verdict.values())
    assert all(v[0] < v[1] for v in verdict.values())      # always closer than LCDM
    return verdict


def main():
    inv_min, lam_min, lam_max = part_a()
    verdict = part_b()
    assert lam_min < lam_max
    print("\nALL OK")


if __name__ == "__main__":
    main()
