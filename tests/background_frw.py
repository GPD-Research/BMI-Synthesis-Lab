"""Milestone 4, part 2: the FRW background of the effective 4D theory (v2/03_background.md).

Content of the 4D theory used here (all derived, see tests/check_radion.py):
  * bulk-scalar zero mode Phi_4, canonical, potential  V(Phi_4) = V_* exp(-c Phi_4/M_Pl)
    with the slope c *equal* to the ledger parameter c (no hidden factor);
  * the radion chi is a separate field with potential  V_rad = delta_sigma * Omega^4 and
    slow-roll parameter epsilon = 2/(3 Omega^3) >> 1; it is treated as a subdominant tracer
    and its allowed energy fraction is bounded by the mirror-DM mass drift (Omega = m_DM/m_DM^{(1)}).
  * matter = baryons + mirror matter (pressureless), radiation with N_eff = 3.044.

Outputs (numbers only; no fit to any dark-energy data is performed):
  1. for a grid of c: w(z) of the thawing solution, CPL (w_0, w_a) over 0 < z < 2, and the
     asymptotic attractor  w_inf = -1 + c^2/3.
  2. the radion: the maximum present-day energy fraction f_rad = rho_rad/rho_crit compatible
     with |Delta ln m_DM| < 0.05 since recombination, and the implied Gdot/G today.
Run:  python3 tests/background_frw.py
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

# --- fixed inputs (Planck 2018 background; not BMI parameters) ----------------------------
H0_KM_S_MPC = 67.4
OMEGA_M = 0.315
OMEGA_R = 9.2e-5        # photons + 3.044 neutrino species
OMEGA_DE = 1 - OMEGA_M - OMEGA_R
Z_REC = 1090.0
H0_PER_YR = H0_KM_S_MPC * 1e3 / 3.0857e22 * 3.156e7   # 1/yr
Z_DRIFT_MAX = 0.05      # |Delta ln m_DM| since recombination (CMB bound, order of magnitude)


def thawing_solution(c, ln_a_init=-14.0, phi_init=0.0):
    """Integrate a canonical exponential quintessence field from a frozen initial state.

    Units: M_Pl = 1, H0 = 1. Variables: N = ln a, y = (phi, dphi/dN).
    V(phi) = V_* exp(-c phi); V_* is fixed by shooting so that Omega_DE(today) = OMEGA_DE.
    Returns dict with z-grid, w(z), Omega_DE(z), and V_*.
    """
    def hubble2(N, phi, dphi, Vstar):
        rho_m = OMEGA_M * np.exp(-3 * N)
        rho_r = OMEGA_R * np.exp(-4 * N)
        V = Vstar * np.exp(-c * phi)
        # 3 H^2 = rho + H^2 dphi^2/2 + V   (M_Pl = 1, rho in units of 3H0^2)
        return (rho_m + rho_r + V / 3) / (1 - dphi ** 2 / 6)

    def rhs(N, y, Vstar):
        phi, dphi = y
        H2 = hubble2(N, phi, dphi, Vstar)
        V = Vstar * np.exp(-c * phi)
        dV = -c * V
        rho_m = OMEGA_M * np.exp(-3 * N)
        rho_r = OMEGA_R * np.exp(-4 * N)
        # dH/dN / H = -(1/2)(rho_m + 4/3 rho_r)/H^2 *3/... use Raychaudhuri: 
        # 2 H H' = -(3 rho_m + 4 rho_r) - H^2 dphi^2   (H' = dH/dN; rho in units of 3 H0^2 -> factor)
        Hp_over_H = -(3 * rho_m + 4 * rho_r) / (2 * H2) - dphi ** 2 / 2
        ddphi = -(3 + Hp_over_H) * dphi - dV / H2
        return [dphi, ddphi]

    def omega_de_today(lnVstar):
        Vstar = np.exp(lnVstar)
        sol = solve_ivp(rhs, (ln_a_init, 0.0), [phi_init, 0.0], args=(Vstar,),
                        rtol=1e-9, atol=1e-12, dense_output=True)
        phi, dphi = sol.y[:, -1]
        H2 = hubble2(0.0, phi, dphi, Vstar)
        V = Vstar * np.exp(-c * phi)
        return (H2 * dphi ** 2 / 2 + V) / (3 * H2) - OMEGA_DE, sol, Vstar

    lnV = brentq(lambda v: omega_de_today(v)[0], np.log(0.1 * OMEGA_DE), np.log(50 * OMEGA_DE),
                 xtol=1e-10)
    _, sol, Vstar = omega_de_today(lnV)
    z = np.linspace(0, 3, 301)
    N = -np.log(1 + z)
    phi, dphi = sol.sol(N)
    H2 = hubble2(N, phi, dphi, Vstar)
    V = Vstar * np.exp(-c * phi)
    kin = H2 * dphi ** 2 / 2
    w = (kin - V) / (kin + V)
    Ode = (kin + V) / (3 * H2)
    return dict(z=z, w=w, Ode=Ode, Vstar=Vstar, H2=H2)


def cpl_fit(z, w, zmax=2.0):
    m = z <= zmax
    a = 1 / (1 + z[m])
    A = np.vstack([np.ones_like(a), 1 - a]).T
    (w0, wa), *_ = np.linalg.lstsq(A, w[m], rcond=None)
    return w0, wa


def radion_bounds(Omega_today):
    """Radion as a subdominant field: chi'' + 3H chi' = -V'(chi), V = ds Omega^4, chi ~ Omega^{3/2}.
    In matter domination the terminal drift per Hubble time is  Delta chi ~ V'/(3 H^2) (M_Pl=1).
    With  Delta ln Omega = (2/3) Delta chi/chi  and  chi^2 = (16/3) Omega^3 M_Pl^2:
        Delta ln Omega per Hubble time = (2/3) * (8/3) V_rad / (3 H^2 chi^2) = (16/9) V_rad/(3H^2) * 3/(16 Omega^3)
                                       = f_rad / (3 Omega^3),   f_rad = V_rad/(3 M_Pl^2 H^2).
    Integrated from recombination (matter era, f_rad grows as a^3 ... ) the dominant contribution
    is the last Hubble time, so require  f_rad(today)/(3 Omega^3) < Z_DRIFT_MAX  (order of magnitude).
    Gdot/G = -(3 phidot/l) Omega^3/(1-Omega^3) with phidot/l = -dln Omega/dt.
    """
    f_rad_max = 3 * Omega_today ** 3 * Z_DRIFT_MAX
    dlnOmega_per_H = Z_DRIFT_MAX
    Gdot_over_G = 3 * Omega_today ** 3 / (1 - Omega_today ** 3) * dlnOmega_per_H * H0_PER_YR
    return f_rad_max, Gdot_over_G


if __name__ == "__main__":
    print("== bulk-scalar zero mode as thawing quintessence (slope = ledger c) ==")
    print(f"{'c':>5} {'w(z=0)':>8} {'w0_CPL':>8} {'wa_CPL':>8} {'w(z=1)':>8} {'w_inf':>7}")
    for c in [0.1, 0.3, 0.5, 0.7, 1.0, 1.3, 1.6]:
        s = thawing_solution(c)
        w0, wa = cpl_fit(s["z"], s["w"])
        w1 = np.interp(1.0, s["z"], s["w"])
        print(f"{c:5.2f} {s['w'][0]:8.3f} {w0:8.3f} {wa:8.3f} {w1:8.3f} {-1 + c**2/3:7.3f}")
    print("  (thawing branch: w0 > -1 and wa < 0 always; phantom w < -1 is impossible)")
    print("  Planck+SNe  w0 = -1.03 +/- 0.03  (constant w)  ->  c <~ 0.5")
    print("  DESI DR2 + CMB + SNe  w0 ~ -0.75, wa ~ -0.9   -> requires phantom in the past: not reachable")

    print("\n== radion (delta sigma_2 * Omega^4), bounded by mirror-DM mass drift ==")
    for Om in [0.032, 0.01, 0.003]:
        f_max, gdot = radion_bounds(Om)
        print(f"  Omega = {Om:6.3f}: f_rad(today) < {f_max:.1e}   Gdot/G < {gdot:.1e} /yr   (LLR: 1e-13 /yr)")
    print("  -> the radion cannot be the dark energy; the merger is a <~1e-4 perturbation of the background")
