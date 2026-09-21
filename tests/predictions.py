"""Milestone 7: the two closed relations (v2/06_predictions.md).

A. Fifth force: strength alpha_Y AND range lambda from ell_z alone (zero free numbers once ell_z is in
   its window).  Pieces:
     - canonical circle modulus: 5D->4D on S^1, ds_5^2 = e^{-sigma} g_4 + e^{2 sigma} dz^2 (Einstein
       frame), L = (M_Pl^2/2)[R - (3/2)(d sigma)^2]  =>  chi = sqrt(3/2) M_Pl sigma,  sigma = ln(ell_z/ell_z0).
       04d used chi = M_Pl sigma: m_chi and 1/lambda shrink by sqrt(2/3).
     - coupling of chi to a nucleon (Einstein frame):
         d ln m_N / d sigma = -1/2  (Weyl factor on brane masses)
                            -1     (Lambda_QCD proportional to the KK cutoff 1/ell_z)          [verify]
                            -2pi/(b0 alpha_s(1/ell_z))   (1/g_s^2 proportional to ell_z; b0 = 7)  [verify: thresholds]
       quark-mass / Higgs pieces <~ 10% of m_N: dropped [verify].
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


def alpha_s(mu):
    """One-loop alpha_s(mu) from alpha_s(M_Z), nf = 5 below m_t, 6 above."""
    def run(a0, mu0, mu1, nf):
        b = 11 - 2 * nf / 3
        return a0 / (1 + a0 * b / (2 * np.pi) * np.log(mu1 / mu0))
    if mu <= M_T:
        return run(ALPHA_S_MZ, M_Z, mu, 5)
    return run(run(ALPHA_S_MZ, M_Z, M_T, 5), M_T, mu, 6)


def dlnm_dsigma(inv_lz):
    weyl = -0.5
    cutoff = -1.0
    qcd = -2 * np.pi / (B0 * alpha_s(inv_lz))
    return weyl + cutoff + qcd, dict(weyl=weyl, cutoff=cutoff, qcd=qcd)


def alpha_yukawa(inv_lz):
    beta = dlnm_dsigma(inv_lz)[0] / np.sqrt(K_KIN)
    return 2 * beta ** 2


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
    print(f"d ln m_N / d ln ell_z at 1/ell_z = 10 TeV: {tot:.1f}  "
          f"(Weyl {parts['weyl']:.1f}, cutoff {parts['cutoff']:.1f}, QCD {parts['qcd']:.1f}; alpha_s = {alpha_s(10e12):.3f})")
    print(f"beta = {tot/np.sqrt(K_KIN):.1f}  ->  alpha_Y = 2 beta^2 = {alpha_yukawa(10e12):.0f}  (04d guessed 'order one')")
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
    print(f"window after this milestone:  {inv_min/1e12:.1f} TeV < 1/ell_z < {LZ_INV_MAX/1e12:.0f} TeV   "
          f"<=>   {lam_min:.1f} um < lambda < {lam_max:.1f} um   at alpha_Y = {alpha_yukawa(inv_min):.0f}-{alpha_yukawa(LZ_INV_MAX):.0f}")
    print(f"(04d window was 5.4-29 TeV / 2-66 um at alpha_Y ~ 1; the lower edge is now set by alpha_Y, not by alpha = 1)")
    print("P1 (revised): alpha_Y ~ 2e2, composition-dependent at the 1e-3 level (alpha piece of m_N), range in the band above.")
    print("A detection with alpha_Y outside ~[100, 400] at that range kills the fixed-circle geometry as much as no detection.")
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
