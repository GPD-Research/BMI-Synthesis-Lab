"""P2 against the DESI DR2 chains (v2/06_predictions.md S4c): the chain-level test that S4b deferred.

Data: DESI DR2 public cobaya chains, model base_w_wa, DESI BAO (all) + Planck PR3 low-l TT/EE + PR4
CamSpec TTTEEE + Planck/ACT DR6 lensing, with each of Pantheon+, Union3, DESY5 and without SNe
(https://data.desi.lbl.gov/public/papers/y3/bao-cosmo-params/cobaya/base_w_wa/).
tests/data/desi_dr2_w0wa.npz holds (w0, wa, weight) of the four chains per dataset after a 30% burn-in,
thinned to <= 20000 rows (weights kept).  Rebuild with
    python3 tests/p2_chains.py --extract DIR      (DIR/{pantheonplus,union3,desy5sn,none}/chain.[1-4].txt)

Test (pre-registered kill criteria 01_action.md S6.2 and S6.3, as framed in 06_predictions.md S4b):
  - credible level of the thawing curve (w0, wa)(c) under the 2D (w0, wa) posterior, by weighted KDE:
    level(p) = posterior mass at density above rho(p).  Where fewer than MIN_TAIL samples lie below rho(p) the tail
    is unresolved and the resolution limit is reported as a lower bound.  Reported as a 2D Delta chi^2 = -2 ln(1 - level)
    and as an equivalent two-sided Gaussian n-sigma.  Same for LCDM (-1, 0) as reference.
  - criterion 3 (phantom crossing): posterior mass with w(a) >= -1 on all of 0 < z < 2.5 (CPL), i.e.
    w0 >= -1 and w0 + wa (1 - a_min) >= -1.  Its complement is the CPL preference for crossing.
CPL projection of the curve: least-squares fit of w(z) over 0 < z < 1, as in tests/predictions.py.
That projection is the remaining approximation: the curve is not refitted to the data.

Run:  python3 tests/p2_chains.py
"""
import os
import sys
import glob
import numpy as np
from scipy.stats import gaussian_kde, chi2, norm

sys.path.insert(0, os.path.dirname(__file__))
from background_frw import thawing_solution, cpl_fit  # noqa: E402

DATA = os.path.join(os.path.dirname(__file__), "data", "desi_dr2_w0wa.npz")
SETS = {"pantheonplus": "Pantheon+", "union3": "Union3", "desy5sn": "DESY5", "none": "no SNe"}
PAPER = {"pantheonplus": (-0.838, -0.62), "union3": (-0.667, -1.09), "desy5sn": (-0.752, -0.86)}
Z_CROSS_MAX = 2.5
BURN = 0.3
NMAX = 20000
MIN_TAIL = 30


def extract(root):
    out = {}
    for key in SETS:
        rows = []
        for f in sorted(glob.glob(os.path.join(root, key, "chain.[1-4].txt"))):
            names = open(f).readline().lstrip("#").split()
            d = np.loadtxt(f)
            d = d[int(BURN * len(d)):]
            rows.append(d[:, [names.index("w"), names.index("wa"), names.index("weight")]])
        if len(rows) != 4:
            raise SystemExit(f"{key}: expected 4 chains, found {len(rows)}")
        d = np.vstack(rows)
        step = max(1, int(np.ceil(len(d) / NMAX)))
        out[key] = d[::step].astype(np.float32)
        print(f"{key}: {len(d)} rows after burn-in, kept {len(out[key])} (every {step})")
    np.savez_compressed(DATA, **out)
    print("wrote", DATA)


def weighted_stats(x, w):
    m = np.average(x, axis=0, weights=w)
    c = np.cov(x.T, aweights=w)
    return m, np.sqrt(np.diag(c)), c[0, 1] / np.sqrt(c[0, 0] * c[1, 1])


def levels(samples, weights, points):
    """Credible level of each point; where fewer than MIN_TAIL samples lie below its density the
    tail is unresolved and the level is replaced by the resolution limit (a lower bound)."""
    kde = gaussian_kde(samples.T, weights=weights)
    rho_s = kde(samples.T)
    rho_p = kde(np.atleast_2d(points).T)
    wsum = weights.sum()
    floor = 1 - weights[np.argsort(rho_s)[:MIN_TAIL]].sum() / wsum
    lev = np.array([weights[rho_s > r].sum() / wsum for r in rho_p])
    ok = np.array([(rho_s <= r).sum() >= MIN_TAIL for r in rho_p])
    return np.where(ok, lev, floor), ok, lev


def gauss_dchi2(samples, weights, points):
    m = np.average(samples, axis=0, weights=weights)
    ci = np.linalg.inv(np.cov(samples.T, aweights=weights))
    d = np.atleast_2d(points) - m
    return np.einsum("ij,jk,ik->i", d, ci, d)


def to_sigma(level):
    level = np.minimum(level, 1 - 1e-12)
    return -2 * np.log(1 - level), np.sqrt(chi2.ppf(level, 1))


def thawing_curve():
    cs = np.linspace(0.05, 1.8, 36)
    curve = []
    for c in cs:
        s = thawing_solution(c)
        curve.append(cpl_fit(s["z"], s["w"], zmax=1.0))
    return cs, np.array(curve)


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--extract":
        extract(sys.argv[2])
        return
    data = np.load(DATA)
    cs, curve = thawing_curve()
    a_min = 1 / (1 + Z_CROSS_MAX)
    print("=== P2 vs DESI DR2 chains (BAO + CMB [+ SNe]), base_w_wa ===")
    print(f"curve: c = {cs[0]:.2f}-{cs[-1]:.2f}, w_a/(1+w_0) = {curve[0,1]/(1+curve[0,0]):.2f} .. {curve[-1,1]/(1+curve[-1,0]):.2f}")
    res = {}
    for key, label in SETS.items():
        d = data[key].astype(float)
        x, w = d[:, :2], d[:, 2]
        m, s, rho = weighted_stats(x, w)
        lev_c, ok_c, raw_c = levels(x, w, curve)
        i = int(np.argmin(raw_c))
        (lev_l,), (ok_l,), (raw_l,) = levels(x, w, [[-1.0, 0.0]])
        g_c, g_l = gauss_dchi2(x, w, curve), gauss_dchi2(x, w, [[-1.0, 0.0]])[0]
        no_cross = (x[:, 0] >= -1) & (x[:, 0] + x[:, 1] * (1 - a_min) >= -1)
        p_nc = w[no_cross].sum() / w.sum()
        ok_x = no_cross.sum() >= MIN_TAIL
        sig_cross = norm.isf((p_nc if ok_x else np.sort(w)[-MIN_TAIL:].sum() / w.sum()) / 2)
        print(f"\n{label:>9}: w0 = {m[0]:.3f} +- {s[0]:.3f}, wa = {m[1]:.2f} +- {s[1]:.2f}, rho = {rho:+.3f}")
        if key in PAPER:
            print(f"           paper: w0 = {PAPER[key][0]}, wa = {PAPER[key][1]}")
        for name, lev, ok, gg, cc in (("curve", lev_c[i], ok_c[i], g_c.min(), f" (best c = {cs[i]:.2f})"),
                                      ("LCDM ", lev_l, ok_l, g_l, "")):
            dchi, sig = to_sigma(lev)
            q = "" if ok else ">"
            print(f"           {name}: level {q}{lev:.4f}  Delta chi^2_2D {q or '='} {dchi:.1f} ({q}{sig:.1f} sigma);"
                  f" Gaussian {gg:.1f}{cc}")
        q = "" if ok_x else " (no-crossing tail unresolved: the chains cannot go beyond this)"
        print(f"           P(w >= -1 on 0<z<{Z_CROSS_MAX}) = {p_nc:.2e} -> crossing preferred at"
              f" {'' if ok_x else '>'}{sig_cross:.1f} sigma{q}")
        res[key] = dict(rho=rho, lev_c=lev_c[i], lev_l=lev_l, raw_c=raw_c[i], raw_l=raw_l, g_c=g_c.min(), g_l=g_l, c=cs[i], sig_cross=sig_cross, ok_x=ok_x, mean=m)
    out95 = [k for k in SETS if res[k]["lev_c"] > 0.95]
    print("\nKill criterion 2 (curve outside the 95% region for every c):",
          f"fires for {len(out95)} of {len(SETS)} ({', '.join(SETS[k] for k in out95) or 'none'});"
          " 'no SNe' is DESI + Planck, the combination 01_action.md S6.2 names")
    crit3 = [k for k in SETS if res[k]["sig_cross"] > 5 and res[k]["ok_x"]]
    undec = [k for k in SETS if not res[k]["ok_x"] and res[k]["sig_cross"] < 5]
    print("Kill criterion 3 (phantom crossing > 5 sigma):",
          f"fires for {len(crit3)} of {len(SETS)}; undecidable from the chains for {len(undec)}"
          f" (resolution limit {min(res[k]['sig_cross'] for k in SETS):.1f}-{max(res[k]['sig_cross'] for k in SETS):.1f} sigma)")
    better = [k for k in SETS if res[k]["raw_c"] < res[k]["raw_l"] and res[k]["g_c"] < res[k]["g_l"]]
    print(f"Curve closer than LCDM (KDE, unresolved tails included, and Gaussian) for {len(better)} of {len(SETS)}:",
          ", ".join(SETS[k] for k in better) or "none")
    print("Correlations from the chains (S4b used rho in [-0.95, -0.8]):",
          ", ".join(f"{SETS[k]} {res[k]['rho']:+.2f}" for k in SETS))
    for k in PAPER:
        assert abs(res[k]["mean"][0] - PAPER[k][0]) < 0.02 and abs(res[k]["mean"][1] - PAPER[k][1]) < 0.08, k
    print("\nALL OK")
    return res


if __name__ == "__main__":
    main()
