"""Milestone 5b: scan of post-impact initial data (v2/04b_initial_conditions.md).

The action is Z_2-symmetric at the collision and the matching through Omega = 1 is not solved
(04_impact.md §0), so the impact hands the 4D equations a set of *initial data* that the action
does not fix. This script enumerates that data, runs each configuration forward with the
milestone-4/5 machinery (tests/impact.py) and scores it against observation. Nothing is fit:
each configuration is a point, and the output is which points survive and what they cost.

Initial data (post-impact, Sigma_1 frame):
  r_b        radion kinetic / radiation energy ratio            -> Omega_0 (freeze-out)
  f_2        fraction of the impact radiation deposited on Sigma_2 -> x = T_2/T_1 = (f_2/(1-f_2))^{1/4}
  eta_1      net baryon number per photon pre-loaded on Sigma_1  (must equal the observed 6.1e-10)
  eta_2      net baryon number per photon pre-loaded on Sigma_2  (mirror SM only)
  P_relic    Omega_0 m_relic^prop n_relic / n_gamma,2 : a cold non-thermal relic pre-loaded on Sigma_2
             that survived the impact (higher-dimensional or non-SM Sigma_2 content); one number
  content    'mirror-SM' | 'cold relic' | 'none' (Sigma_2 empty / at the horizon)

Scores (pass/fail):
  Cassini      Omega_0 < 0.032 (or Sigma_2 gone: Omega_0 < 1e-4, RS2 limit)
  N_eff        Delta N_eff(BBN) < 0.3 and Delta N_eff(CMB) < 0.3
  eta_B        eta_1 = 6.1e-10 (initial datum; always satisfiable, always costs one number)
  DM           Omega_DM/Omega_b = 5.3 within 10% (or DM borrowed, flagged)
  drift        |Delta ln m_DM| < 0.05 since recombination (satisfied by parameter #4, 03_background.md §3.1)
  dissipative  mirror-baryon DM is dissipative (atomic); flagged, judged in milestone 6
Run:  python3 tests/scan_initial_conditions.py
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from impact import (DN_EFF_MAX, OMEGA_DM_OVER_B, T_BBN_MEV, T_CMB_MEV, delta_neff,   # noqa: E402
                    eta_ratio_required, omega_today_from_rb, rb_from_omega_today, x_bound)

ETA_B_OBS = 6.1e-10
OMEGA_CASSINI = 0.032
OMEGA_GONE = 1e-4          # below this Sigma_2 is at the horizon for every purpose: RS2 limit
DM_TOL = 0.10


def x_from_f2(f2):
    """T_2/T_1 at the impact for a fraction f2 of the radiation on Sigma_2 (equal g_* both sectors)."""
    return (f2 / (1 - f2)) ** 0.25


def f2_from_x(x):
    return x ** 4 / (1 + x ** 4)


def score(content, rb, f2, eta2_over_eta1=1.0, P_relic=0.0):
    """Return dict of pass/fail flags, the derived quantities, and the number of initial data used."""
    out = {"content": content, "r_b": rb, "f_2": f2}
    Om = omega_today_from_rb(rb)
    if Om is None or Om < OMEGA_GONE:
        out.update(Omega_0=0.0, x=None, dN_BBN=0.0, dN_CMB=0.0, DM_ratio=None)
        out["Cassini"] = True
        out["N_eff"] = True
        out["DM"] = None                                # borrowed
        out["cost"] = 2 if content == "none" else None  # r_b, eta_1; other content is meaningless
        out["note"] = "RS2 limit: no Sigma_2, DM borrowed"
        return out
    x = x_from_f2(f2)
    out.update(Omega_0=Om, x=x)
    out["Cassini"] = bool(Om < OMEGA_CASSINI)
    dnb = delta_neff(T_BBN_MEV, x, Om)
    dnc = delta_neff(T_CMB_MEV, x, Om)
    out.update(dN_BBN=dnb, dN_CMB=dnc)
    out["N_eff"] = bool(dnb < DN_EFF_MAX and dnc < DN_EFF_MAX)
    if content == "mirror-SM":
        need, ratio_n = eta_ratio_required(x, Om)
        dm = OMEGA_DM_OVER_B * eta2_over_eta1 / need
        out["DM_ratio"] = dm
        out["DM"] = bool(abs(dm / OMEGA_DM_OVER_B - 1) < DM_TOL)
        out["cost"] = 4              # r_b, f_2, eta_1, eta_2
        out["note"] = f"eta_2/eta_1 = {eta2_over_eta1:.0f}; mirror baryons are dissipative DM (flag)"
    elif content == "cold relic":
        # Omega_relic/Omega_b = P_relic * (n_gamma,2/n_gamma,1) / (m_p eta_1); P_relic in units of m_p eta_1
        _, ratio_n = eta_ratio_required(x, Om)
        dm = P_relic * ratio_n
        out["DM_ratio"] = dm
        out["DM"] = bool(abs(dm / OMEGA_DM_OVER_B - 1) < DM_TOL)
        out["cost"] = 4              # r_b, f_2, eta_1, P_relic
        out["note"] = f"P_relic = {P_relic:.3g} m_p eta_1; relic mass/abundance not from the action"
    else:
        out["DM_ratio"] = None
        out["DM"] = None
        out["cost"] = 3              # r_b, f_2, eta_1
        out["note"] = "Sigma_2 present, empty of baryons: DM borrowed"
    return out


def viable(s):
    return s["Cassini"] and s["N_eff"] and (s["DM"] is not False)


def fmt(s):
    x = f"{s['x']:.3f}" if s["x"] is not None else "  -  "
    dm = f"{s['DM_ratio']:.2f}" if s["DM_ratio"] is not None else "borrowed"
    flag = lambda v: "pass" if v else ("fail" if v is False else "  - ")
    return (f"{s['content']:>10} {s['r_b']:7.4f} {s['Omega_0']:8.4f} {x:>6} {s['dN_BBN']:7.2f} {s['dN_CMB']:7.2f} "
            f"{dm:>8} {flag(s['Cassini']):>7} {flag(s['N_eff']):>5} {flag(s['DM']):>4} {str(s['cost']):>4}  {s['note']}")


HEADER = (f"{'content':>10} {'r_b':>7} {'Omega_0':>8} {'x':>6} {'dN_BBN':>7} {'dN_CMB':>7} "
          f"{'DM/b':>8} {'Cassini':>7} {'N_eff':>5} {'DM':>4} {'cost':>4}  note")


if __name__ == "__main__":
    rb_cas = rb_from_omega_today(OMEGA_CASSINI)
    rb_mid = rb_from_omega_today(0.01)
    rb_over = 1.30

    print("=== A. named configurations ===")
    print(HEADER)
    configs = [
        # the action's own null hypothesis: symmetric impact, symmetric baryon number
        ("mirror-SM", rb_mid, f2_from_x(1.0), dict(eta2_over_eta1=1.0)),
        # asymmetric energy deposition only
        ("mirror-SM", rb_mid, f2_from_x(0.44), dict(eta2_over_eta1=1.0)),
        # asymmetric energy + pre-loaded asymmetry on Sigma_2 (the "pre-loaded manifold")
        ("mirror-SM", rb_mid, f2_from_x(0.44), dict(eta2_over_eta1=eta_ratio_required(0.44, 0.01)[0])),
        ("mirror-SM", rb_cas, f2_from_x(0.40), dict(eta2_over_eta1=eta_ratio_required(0.40, OMEGA_CASSINI)[0])),
        # Sigma_2 with too much radiation, right asymmetry
        ("mirror-SM", rb_mid, f2_from_x(0.6), dict(eta2_over_eta1=2000.0)),
        # pre-loaded cold relic on Sigma_2 (higher-dimensional / non-SM content)
        ("cold relic", rb_mid, f2_from_x(0.3), dict(P_relic=OMEGA_DM_OVER_B / eta_ratio_required(0.3, 0.01)[1])),
        ("cold relic", rb_mid, f2_from_x(0.01), dict(P_relic=OMEGA_DM_OVER_B / eta_ratio_required(0.01, 0.01)[1])),
        # Sigma_2 present but empty
        ("empty", rb_mid, f2_from_x(0.3), {}),
        # overshoot: no Sigma_2 today
        ("none", rb_over, 0.5, {}),
    ]
    results = []
    for content, rb, f2, kw in configs:
        s = score(content, rb, f2, **kw)
        results.append(s)
        print(fmt(s))
    sym = results[0]
    assert not viable(sym) and sym["dN_BBN"] > 3, "the Z_2-symmetric impact must fail"
    assert not viable(results[1]) and results[1]["DM"] is False, "energy asymmetry alone must fail on DM"
    assert viable(results[2]) and viable(results[3]), "pre-loaded asymmetry must pass numerically"
    assert not viable(results[4]) and results[4]["N_eff"] is False
    assert viable(results[5]) and viable(results[6])
    assert viable(results[7]) and viable(results[8])

    print("\n=== B. mirror-SM viability map: x = T_2/T_1 (rows) vs eta_2/eta_1 (cols), Omega_0 = 0.01 ===")
    print("    # = viable band (Cassini, N_eff, DM within a factor 2 of 5.3);  n = N_eff fails;  d = DM off;  . = both fail")
    etas = np.logspace(0, 5, 21)
    xs = np.linspace(0.1, 1.0, 19)
    print(f"{'x':>6} | " + " ".join(f"{e:6.0f}" for e in etas[::4]) + "   (eta_2/eta_1, every 4th column labelled)")
    n_viable = 0
    for x in xs:
        row = []
        for e in etas:
            s = score("mirror-SM", rb_mid, f2_from_x(x), eta2_over_eta1=e)
            ok_n, ok_d = s["N_eff"], abs(np.log(s["DM_ratio"] / OMEGA_DM_OVER_B)) < np.log(2)
            ch = "#" if (ok_n and ok_d) else ("n" if not ok_n and ok_d else ("d" if ok_n else "."))
            n_viable += ch == "#"
            row.append(ch)
        print(f"{x:6.2f} | " + " ".join(row))
    assert n_viable > 0
    # the viable band: eta_2/eta_1 required as a function of x, at the N_eff bound
    print("\n  eta_2/eta_1 that gives Omega_DM/Omega_b = 5.3 exactly:")
    print(f"  {'Omega_0':>8} {'x_max(N_eff)':>13} {'eta_2/eta_1 at x_max':>21} {'at x = 0.2':>11} {'at x = 0.1':>11}")
    for Om in (OMEGA_CASSINI, 0.01, 0.003):
        xm = min(x_bound(T_BBN_MEV, Om), x_bound(T_CMB_MEV, Om))
        print(f"  {Om:8.3f} {xm:13.3f} {eta_ratio_required(xm, Om)[0]:21.0f} {eta_ratio_required(0.2, Om)[0]:11.0f} {eta_ratio_required(0.1, Om)[0]:11.0f}")

    print("\n=== C. what the pre-loaded picture must still supply ===")
    x_ref = min(x_bound(T_BBN_MEV, 0.01), x_bound(T_CMB_MEV, 0.01))
    need = eta_ratio_required(x_ref, 0.01)[0]
    print(f"  Sigma_2 pre-loaded with net baryon number eta_2 = {need:.0f} eta_1 = {need * ETA_B_OBS:.1e} per mirror photon")
    print(f"  i.e. after the annihilation era on Sigma_2 about 1 baryon in {1 / (need * ETA_B_OBS):.0f} survives, vs 1 in {1 / ETA_B_OBS:.0e} on Sigma_1")
    print(f"  Sigma_1 pre-loaded with eta_1 = {ETA_B_OBS:.1e}: the sign is a coin toss (50/50 matter), the size is an initial datum")
    print("  Neither number is produced by the action; both are initial data of the collision.")
    print("\nALL OK")
