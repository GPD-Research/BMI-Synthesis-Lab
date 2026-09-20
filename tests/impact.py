"""Milestone 5: the impact (v2/04_impact.md). Numbers only; nothing is fit.

Inputs are the effective 4D theory of milestone 4 (tests/check_radion.py, tests/background_frw.py):
  * radion  phi, Omega = exp(-phi/l), kinetic factor K = 12 M_Pl^2 Omega^3 / l^2,
    canonical field chi = -(4/sqrt3) M_Pl Omega^{3/2}, potential V_rad = delta_sigma Omega^4;
  * bulk-scalar zero mode Phi_4, canonical, V = V_* exp(-c Phi_4/M_Pl);
  * mirror sector on Sigma_2 with masses Omega m, energy densities Omega^4 rho^{prop}.

Outputs:
  1. post-impact radion freeze-out: present separation Omega_0 as a function of the ratio
     r_b = (radion kinetic)/(radiation) energy at the impact; the critical ratio above which
     Sigma_2 reaches the AdS horizon; the width of the window that gives 0.003 < Omega_0 < 0.032.
  2. Delta N_eff at BBN and at the CMB from a mirror sector with impact temperature ratio x and
     warp-shifted thresholds (mirror species annihilate when the *proper* temperature T_2/Omega
     drops below their mass); the bound on x; Omega_DM/Omega_b and the baryon-asymmetry ratio
     eta_2/eta_1 that the observed value requires.
  3. dark radiation from bulk-graviton emission (Langlois, Sorbo & Rodriguez-Martinez 2002,
     hep-th/0206146, eqs. 20-26): epsilon_W and Delta N_eff, as functions of T_RH/T_t.
  4. earliest possible turnaround for delta_sigma < 0 saturating the mass-drift bound.
  5. the bulk scalar as an inflaton: (n_s, r) of power-law inflation for the slope c.
Run:  python3 tests/impact.py
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

# --- fixed inputs (not BMI parameters) -----------------------------------------------------
M_PL_GEV = 2.435e18            # reduced Planck mass
H0_KM_S_MPC = 67.4
GYR_PER_HUBBLE = 977.8 / H0_KM_S_MPC
OMEGA_M = 0.315
OMEGA_R = 9.2e-5
OMEGA_DE = 1 - OMEGA_M - OMEGA_R
OMEGA_DM_OVER_B = 5.3
OMEGA_TODAY_GRID = (0.032, 0.01, 0.003)   # Cassini bound and two smaller values
DN_EFF_MAX = 0.3
T_BBN_MEV = 1.0
T_CMB_MEV = 0.26e-6
ALPHA_LSR = 0.019              # LSR eq. 20 with full SM content, g_hat = 166.21, g_* = 106.75
LN_M_DRIFT_MAX = 0.05          # |Delta ln m_DM| since recombination (as in background_frw.py)

CHI_MAX = 4 / np.sqrt(3)       # |chi| at Omega = 1, in units of M_Pl


# ---------------------------------------------------------------------------------------------
# 1. radion freeze-out after the impact
# ---------------------------------------------------------------------------------------------
def omega_today_from_rb(rb):
    """Frozen Omega_0 for kinetic/radiation ratio r_b at the impact (analytic).

    Kinetic-dominated then radiation-dominated canonical scalar: dchi/dN = sqrt6 M_Pl (rho_kin/rho_tot)^{1/2}
    with rho_kin ~ a^-6, rho_rad ~ a^-4  =>  Delta chi = sqrt6 M_Pl asinh(sqrt r_b).
    Radion starts at |chi| = 4/sqrt3 M_Pl (Omega = 1) and freezes at |chi_0| = 4/sqrt3 M_Pl Omega_0^{3/2}.
    Returns None if the radion reaches chi = 0 (Omega = 0: Sigma_2 at the AdS horizon).
    """
    dchi = np.sqrt(6) * np.arcsinh(np.sqrt(rb))
    rest = CHI_MAX - dchi
    if rest <= 0:
        return None
    return (rest / CHI_MAX) ** (2 / 3)


def rb_from_omega_today(Omega0):
    return np.sinh(CHI_MAX * (1 - Omega0 ** 1.5) / np.sqrt(6)) ** 2


def freeze_out_numeric(rb, N_end=20.0):
    """Integrate chi(N) with rho_kin = H^2 chi'^2/2 and radiation only (M_Pl = 1); check the analytic result."""
    # units: at N=0 rho_rad = 1; chi' from rho_kin/rho_rad = rb: chi'^2 = 6 rb/(1+rb)
    chi0 = -CHI_MAX
    dchi0 = np.sqrt(6 * rb / (1 + rb))

    def rhs(N, y):
        chi, dchi = y
        rho_r = np.exp(-4 * N)
        H2 = rho_r / (3 - dchi ** 2 / 2)          # 3 H^2 = rho_r + H^2 chi'^2 / 2
        Hp_over_H = -(4 * rho_r / 3 + H2 * dchi ** 2) / (2 * H2)
        ddchi = -(3 + Hp_over_H) * dchi
        return [dchi, ddchi]

    hit = lambda N, y: y[0]
    hit.terminal = True
    sol = solve_ivp(rhs, (0, N_end), [chi0, dchi0], events=hit, rtol=1e-9, atol=1e-12, dense_output=True)
    if sol.t_events[0].size:
        return None
    chi_end = sol.y[0, -1]
    return (abs(chi_end) / CHI_MAX) ** (2 / 3)


# ---------------------------------------------------------------------------------------------
# 2. mirror sector: Delta N_eff, Omega_DM/Omega_b
# ---------------------------------------------------------------------------------------------
# coarse SM relativistic degrees of freedom (rho and s) vs temperature in MeV; each species dropped
# at T = m/3 (order of magnitude; the BBN/CMB numbers below are insensitive to this at the 10% level)
_G_TABLE = [  # (T_low in MeV, g_rho, g_s)
    (173e3 / 3, 106.75, 106.75),
    (125e3 / 3, 96.25, 96.25),
    (91e3 / 3, 95.25, 95.25),
    (80e3 / 3, 92.25, 92.25),
    (4.2e3 / 3, 86.25, 86.25),
    (1.8e3 / 3, 75.75, 75.75),
    (1.3e3 / 3, 72.25, 72.25),
    (150.0, 61.75, 61.75),        # quarks + gluons down to the QCD transition
    (105.0 / 3, 17.25, 17.25),    # gamma, e, mu, 3 nu, pions
    (0.511 / 3, 10.75, 10.75),    # gamma, e, 3 nu
    (0.0, 3.363, 3.909),          # gamma + decoupled nu with T_nu = (4/11)^{1/3} T_gamma
]


def g_of_T(T_MeV):
    for T_low, g_rho, g_s in _G_TABLE:
        if T_MeV >= T_low:
            return g_rho, g_s
    return _G_TABLE[-1][1], _G_TABLE[-1][2]


def mirror_temperature(T1_MeV, x_imp, Omega):
    """Sigma_1-frame mirror temperature T_2 when our photons are at T1.

    x_imp = T_2/T_1 at the impact (both sectors with g_s = 106.75). Entropy is conserved
    separately in each sector, so T_2/T_1 = x_imp (g_s1(T_1)/g_s2(T_2^prop))^{1/3} with the mirror
    proper temperature T_2^prop = T_2/Omega setting which mirror species are relativistic.
    """
    g_s1 = g_of_T(T1_MeV)[1]
    f = lambda T2: T2 - x_imp * T1_MeV * (g_s1 / g_of_T(T2 / Omega)[1]) ** (1 / 3)
    lo, hi = 1e-6 * x_imp * T1_MeV, 10 * x_imp * T1_MeV
    return brentq(f, lo, hi)


def delta_neff(T1_MeV, x_imp, Omega):
    T2 = mirror_temperature(T1_MeV, x_imp, Omega)
    g_rho2 = g_of_T(T2 / Omega)[0]
    rho2 = g_rho2 * T2 ** 4
    # one of our neutrino species: (7/8)*2*T_nu^4 with T_nu = T_gamma above e+- annihilation
    T_nu = T1_MeV if T1_MeV > 0.511 / 3 else (4 / 11) ** (1 / 3) * T1_MeV
    rho_one_nu = 1.75 * T_nu ** 4
    return rho2 / rho_one_nu


def x_bound(T1_MeV, Omega, dn_max=DN_EFF_MAX):
    return brentq(lambda x: delta_neff(T1_MeV, x, Omega) - dn_max, 1e-3, 1.0)


def eta_ratio_required(x_imp, Omega):
    """Omega_DM/Omega_b = Omega * (T_2/T_1)^3_{today} * eta_2/eta_1  (all in the Sigma_1 frame)."""
    T2_today = mirror_temperature(T_CMB_MEV, x_imp, Omega)   # g_s frozen below the CMB in both sectors
    ratio_n = (T2_today / T_CMB_MEV) ** 3 * g_of_T(T2_today / Omega)[1] / g_of_T(T_CMB_MEV)[1]
    return OMEGA_DM_OVER_B / (Omega * ratio_n), ratio_n


# ---------------------------------------------------------------------------------------------
# 3. dark radiation from bulk gravitons (LSR 2002)
# ---------------------------------------------------------------------------------------------
def epsilon_weyl(T_RH_over_Tt, alpha=ALPHA_LSR):
    """rho_Weyl/rho_rad after the high/low energy transition.

    High-energy reheating (T_RH >> T_t): LSR eq. 25, epsilon -> alpha/4.
    Low-energy reheating: integrate LSR eq. 23 in the rho << lambda regime,
    dC = sqrt2 alpha rho_hat_RH^{3/2} a^-3 da  =>  epsilon = (alpha/2sqrt2) sqrt(rho_RH/lambda)
    with rho_RH/lambda = (T_RH/T_t)^4.
    """
    if T_RH_over_Tt >= 1:
        return alpha / 4
    return alpha / (2 * np.sqrt(2)) * T_RH_over_Tt ** 2


def transition_temperature_TeV(l_micron, g_star=106.75):
    """T_t from rho = lambda with the 5D-reduced tension lambda = sigma_1^{(5)} = 8 M_5^3/l = 24 M_Pl^2/l^2."""
    inv_l_GeV = 0.19733e-15 / (l_micron * 1e-6)    # hbar c = 0.19733 GeV fm
    lam = 24 * M_PL_GEV ** 2 * inv_l_GeV ** 2
    return (30 * lam / (np.pi ** 2 * g_star)) ** 0.25 / 1e3


# ---------------------------------------------------------------------------------------------
# 4. future evolution with delta_sigma < 0 at the mass-drift bound
# ---------------------------------------------------------------------------------------------
def future_turnaround(Omega0, c, d_over_rho0, Omega_stop=0.5, t_max_hubble=200.0):
    """Integrate a, u = phi/l, Phi_4 forward from today (units M_Pl = 1, H0 = 1, rho_0 = 3).

    Radion (Jordan frame, Einstein-frame corrections are O(Omega^3), dropped):
        u'' + 3 H u' - (3/2) u'^2 = d e^{-u},     d = delta_sigma/rho_0  (dimensionless)
        rho_rad = 6 e^{-3u} u'^2 + 3 d e^{-4u}
    Quintessence: canonical, V = V_* e^{-c Phi}, V_* fixed so that Omega_DE(today) = OMEGA_DE
    with the field released from rest (the thawing solution of background_frw.py starts far
    earlier; today's velocity is small and the difference is irrelevant for the fate).
    Returns (t_H2_zero, t_Omega_stop, Omega_at_end) in Hubble times; None where not reached.
    """
    u0 = -np.log(Omega0)
    Vstar = 3 * OMEGA_DE   # Phi(0) = 0, from rest
    d = d_over_rho0

    def rho_tot(lna, u, du, Phi, dPhi):
        rho_m = 3 * OMEGA_M * np.exp(-3 * lna)
        rho_r = 3 * OMEGA_R * np.exp(-4 * lna)
        return rho_m + rho_r + 0.5 * dPhi ** 2 + Vstar * np.exp(-c * Phi) + 6 * np.exp(-3 * u) * du ** 2 + 3 * d * np.exp(-4 * u)

    def rhs(t, y):
        lna, u, du, Phi, dPhi = y
        rho = rho_tot(lna, u, du, Phi, dPhi)
        H = np.sqrt(max(rho, 0.0) / 3)
        ddu = -3 * H * du + 1.5 * du ** 2 + d * np.exp(-u)
        ddPhi = -3 * H * dPhi + c * Vstar * np.exp(-c * Phi)
        return [H, du, ddu, dPhi, ddPhi]

    def ev_h(t, y):
        return rho_tot(*y) - 1e-6
    ev_h.terminal = True

    def ev_omega(t, y):
        return np.exp(-y[1]) - Omega_stop
    ev_omega.terminal = True

    sol = solve_ivp(rhs, (0, t_max_hubble), [0.0, u0, 0.0, 0.0, 0.0], events=[ev_h, ev_omega],
                    rtol=1e-8, atol=1e-11, max_step=0.05)
    tH = sol.t_events[0][0] if sol.t_events[0].size else None
    tO = sol.t_events[1][0] if sol.t_events[1].size else None
    return tH, tO, np.exp(-sol.y[1, -1])


# ---------------------------------------------------------------------------------------------
# 5. bulk scalar as inflaton
# ---------------------------------------------------------------------------------------------
def power_law_inflation(c):
    """Exponential potential V ~ e^{-c Phi/M_Pl}: a ~ t^{2/c^2}; n_s - 1 = -c^2/(1 - c^2/2), r = 8 c^2."""
    return 1 - c ** 2 / (1 - c ** 2 / 2), 8 * c ** 2


if __name__ == "__main__":
    print("=== 1. radion freeze-out after the impact ===")
    rc = np.sinh(CHI_MAX / np.sqrt(6)) ** 2
    print(f"critical kinetic/radiation ratio at impact  r_c = sinh^2(4/sqrt18) = {rc:.4f}")
    print("  r_b >= r_c: Sigma_2 reaches the AdS horizon (Omega -> 0) in finite time")
    print(f"  {'Omega_0':>8} {'r_b (analytic)':>15} {'r_b/r_c - 1':>12} {'Omega_0 (numeric)':>18}")
    for Om in OMEGA_TODAY_GRID:
        rb = rb_from_omega_today(Om)
        Om_num = freeze_out_numeric(rb)
        assert Om_num is not None and abs(Om_num / Om - 1) < 0.05, (Om, Om_num)
        print(f"  {Om:8.3f} {rb:15.4f} {rb / rc - 1:12.4f} {Om_num:18.4f}")
    rb_lo, rb_hi = rb_from_omega_today(0.032), rb_from_omega_today(0.003)
    print(f"  window for 0.003 < Omega_0 < 0.032:  {rb_lo:.4f} < r_b < {rb_hi:.4f}  (width {rb_hi / rb_lo - 1:.2%})")
    assert freeze_out_numeric(1.3) is None

    print("\n=== 2. mirror sector: Delta N_eff and the baryon asymmetry ===")
    print(f"  {'Omega_0':>8} {'x_max(BBN)':>11} {'x_max(CMB)':>11} {'dN(x=1,BBN)':>12} {'T1 at mirror e+- ann. [keV]':>28}")
    for Om in OMEGA_TODAY_GRID:
        xb = x_bound(T_BBN_MEV, Om)
        xc = x_bound(T_CMB_MEV, Om)
        dn1 = delta_neff(T_BBN_MEV, 1.0, Om)
        # our temperature when the mirror proper temperature crosses m_e/3
        T1_ann = brentq(lambda T: mirror_temperature(T, xb, Om) / Om - 0.511 / 3, 1e-6, 10.0)
        print(f"  {Om:8.3f} {xb:11.3f} {xc:11.3f} {dn1:12.2f} {T1_ann * 1e3:28.1f}")
        assert dn1 > 3.0
    x_ref = x_bound(T_BBN_MEV, 0.032)
    print(f"\n  Omega_DM/Omega_b = Omega_0 (n_2/n_1)|_sym eta_2/eta_1, with x at its BBN bound:")
    print(f"  {'Omega_0':>8} {'x':>6} {'(n_2/n_1)/(eta_2/eta_1)':>24} {'eta_2/eta_1 needed':>19}")
    for Om in OMEGA_TODAY_GRID:
        xb = x_bound(T_BBN_MEV, Om)
        need, ratio_n = eta_ratio_required(xb, Om)
        print(f"  {Om:8.3f} {xb:6.3f} {ratio_n:24.4f} {need:19.0f}")
        assert need > 1e3
    print(f"  symmetric baryogenesis (eta_2 = eta_1) gives Omega_DM/Omega_b = "
          f"{OMEGA_DM_OVER_B / eta_ratio_required(x_ref, 0.032)[0]:.2e} at Omega_0 = 0.032")
    print(f"  Fork 2 (we are the IR brane) would give m^(2) = m/Omega: "
          f"Omega_DM/Omega_b = {eta_ratio_required(x_ref, 0.032)[1] / 0.032:.2f} eta_2/eta_1  -- but Cassini kills Fork 2")

    print("\n=== 3. dark radiation from bulk gravitons (LSR 2002; D=5 coefficients) ===")
    for l_um in (10.0, 1.0):
        print(f"  l = {l_um:4.1f} um: transition temperature T_t = {transition_temperature_TeV(l_um):.1f} TeV")
    for ratio in (10.0, 1.0, 0.3, 0.1):
        eps = epsilon_weyl(ratio)
        dn = eps * 10.75 / 1.75    # at BBN, before the g_* dilution of LSR eq. 26 (upper bound)
        print(f"  T_RH/T_t = {ratio:4.1f}: epsilon_W = {eps:.2e}, Delta N_eff <= {dn:.3f},  if absorbed by Sigma_2: x >= {eps ** 0.25:.2f}")
    assert epsilon_weyl(10) * 10.75 / 1.75 < 0.05

    print("\n=== 4. earliest turnaround, delta_sigma < 0 at the mass-drift bound |d| = 0.15/Omega_0 ===")
    print(f"  {'Omega_0':>8} {'|d|=|dsig|/rho_0':>17} {'c':>4} {'t(H->0) [Gyr]':>14} {'t(Omega=0.5) [Gyr]':>19} {'Omega at end':>13}")
    for Om in OMEGA_TODAY_GRID:
        d = -LN_M_DRIFT_MAX * 3 / Om   # |Delta phi|/l ~ |d| Omega/3 per Hubble time < 0.05
        for c in (0.3,):
            tH, tO, Om_end = future_turnaround(Om, c, d)
            f = lambda t: f"{t * GYR_PER_HUBBLE:14.0f}" if t is not None else f"{'-':>14}"
            print(f"  {Om:8.3f} {abs(d):17.2f} {c:4.1f} {f(tH)} {f(tO):>19} {Om_end:13.3f}")
            assert (tH is None or tH * GYR_PER_HUBBLE > 30)
    tH, tO, _ = future_turnaround(0.032, 0.3, +0.15 * 3 / 0.032)
    assert tH is None and tO is None, "delta_sigma > 0 must not turn around"
    print("  delta_sigma > 0 (same magnitude): no turnaround, Omega decreases monotonically")

    print("\n=== 5. the bulk scalar as an inflaton (power-law inflation) ===")
    for c in (0.19, 0.3, 0.5):
        ns, r = power_law_inflation(c)
        print(f"  c = {c:4.2f}: n_s = {ns:.3f}, r = {r:.2f}  (BICEP/Keck + Planck: r < 0.036)")
    c_ns = brentq(lambda c: power_law_inflation(c)[0] - 0.965, 0.05, 0.5)
    assert power_law_inflation(c_ns)[1] > 0.036
    print(f"  n_s = 0.965 needs c = {c_ns:.3f} -> r = {power_law_inflation(c_ns)[1]:.2f}: excluded; and power-law inflation never ends")
    print("\nALL OK")
