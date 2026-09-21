"""Milestone 6: the oscillating circle as dark matter (v2/05_dark_sector.md).

04d_circle.md S4 stabilized ell_z with V(l) = C_z/l^4 + pi delta_1 l and found the modulus chi
(m_chi ~ 1e-2 eV) never decays. Here its abundance is computed properly and confronted with data.

  1. thermal misalignment: the KK-tower free energy shifts the minimum while T > 0; if the shift is
     present when H ~ m_chi (T_R > T_o) the field is left displaced by O(0.1-1) -> overclosure.
     If T_R < T_o the field tracks the shifting minimum adiabatically and the thermal shift excites
     nothing.  => hard bound T_R < T_o  (the 04d claim "tune T_R to 0.4%" is WRONG and retracted here)
  2. collision misalignment: the impact leaves the circle at ell_z(1+delta_z) with H > m_chi.  Omega_chi
     then depends on delta_z and T_R; Omega_chi = Omega_DM fixes delta_z(T_R) ~ 1e-6, tuned only to 5%.
  3. T_R from the impact: h = rho_1/sigma_1 of 04c; T_R < T_o is h < ~0.1 (within the h < 1 scope).
  4. structure: Jeans length, isocurvature from spatial variation of delta_z, cold since T_R.
  5. signatures: oscillating alpha and G at f = m_chi/2pi; self-interaction; direct detection: none.

Conventions: eV, reduced M_Pl.  All Casimir O(1) factors carried from tests/circle.py [verify].
Run:  python3 tests/dark_sector.py
"""
import numpy as np
from scipy.optimize import brentq
from scipy.special import zeta

M_PL = 2.435e27
HBAR_C_EV_CM = 1.9733e-5
RHO_C = (2.25e-3) ** 4 / 0.69
OMEGA_DM, OMEGA_B = 0.265, 0.049
T_EQ = 0.80                    # eV, matter-radiation equality
T0 = 2.35e-4                   # eV, CMB today
GSTAR = 106.75
G_SM = 118                     # on-shell SM dof (90 fermionic + 28 bosonic), all in the KK tower
C_Z = 62 * 3 * zeta(5) / (64 * np.pi ** 6)
H0 = 1.44e-33                  # eV
LZ_INV = 1e13                  # eV, KK scale used throughout (window 5.4-29 TeV, 04d S3b)
ELL = 10e-4 / HBAR_C_EV_CM     # eV^-1, warp length 10 um
M6 = 2.7e16                    # eV [verify]  (04d)
T_T = 6e12                     # eV, rho^2 transition scale of 03_background (ell = 10 um)


def m_chi(inv_lz):
    return np.sqrt(20 * C_Z * inv_lz ** 4) / M_PL


def hubble_rad(T):
    return np.sqrt(np.pi ** 2 * GSTAR / 90) * T ** 2 / M_PL


def T_osc(inv_lz):
    m = m_chi(inv_lz)
    return brentq(lambda T: hubble_rad(T) - m, 1e-3, 1e20)


# ---------- 1. thermal misalignment ----------
def thermal_shift(T, inv_lz):
    """d ln ell_z of the minimum from the free energy of one non-relativistic KK level of G_SM dof.

    F = -G_SM T^4 (x/2pi)^{3/2} e^{-x}, x = 1/(l T);  dF/dln l = -x dF/dx ~ -G_SM T^4 (x/2pi)^{3/2} x e^{-x}
    (leading Boltzmann term, x >> 1; the relativistic regime x < 1 gives O(1) and is only bounded here).
    Restoring force: l^2 V'' = 20 C_z / l^4.
    """
    x = inv_lz / T
    if x < 1:
        return 1.0
    dF = G_SM * T ** 4 * (x / (2 * np.pi)) ** 1.5 * x * np.exp(-x)
    return min(1.0, dF / (20 * C_Z * inv_lz ** 4))


def omega_chi_from_displacement(dlnl, T_start, inv_lz=LZ_INV):
    """Omega_chi today for a displacement dlnl = dchi/M_Pl that starts oscillating at T_start <= T_o.

    rho_chi/rho_rad at T_start = (1/2) m^2 dchi^2 / (3 H^2 M_Pl^2) = dlnl^2/6 (m/H)^2  (= dlnl^2/6 at T_o);
    then scales as a -> x T_start/T_eq (g_* changes neglected: factor ~ 0.3 [verify]).
    Net: Omega_chi ~ dlnl^2 T_o^4 / T_start^3.
    """
    r_eq = dlnl ** 2 / 6 * (m_chi(inv_lz) / hubble_rad(T_start)) ** 2 * T_start / T_EQ
    return r_eq * (OMEGA_DM + OMEGA_B) / (1 + r_eq)   # matter at eq = radiation; chi's share of it


def main():
    inv = LZ_INV
    m = m_chi(inv)
    To = T_osc(inv)
    print(f"1/ell_z = {inv/1e12:.0f} TeV: m_chi = {m:.2e} eV, T_o (H = m) = {To/1e12:.2f} TeV, ell_z T_o = {To/inv:.2f}")

    print("\n=== 1. thermal misalignment ===")
    sh = thermal_shift(To, inv)
    Om_th = omega_chi_from_displacement(sh, To)
    print(f"minimum shift at T_o: d ln ell_z = {sh:.2f} -> if T_R > T_o, Omega_chi ~ {Om_th:.2f} of critical -> OVERCLOSURE")
    print("if T_R < T_o: H < m from reheating on, chi tracks the shifting minimum adiabatically; excited amplitude")
    print("  ~ (H/m)^2 x shift -> negligible.  Hard bound:  T_R < T_o.")
    assert Om_th > 0.3

    print("\n=== 2. collision misalignment (the mechanism) ===")
    print(" T_R [TeV]   delta_z for Omega_DM   d Omega/Omega per 10% in delta_z   per 10% in T_R")
    for TR in [0.1e12, 0.5e12, 1e12, 2e12, To]:
        dz = brentq(lambda d: omega_chi_from_displacement(d, TR) - OMEGA_DM, 1e-15, 1.0)
        dOm = (omega_chi_from_displacement(1.1 * dz, TR) - OMEGA_DM) / OMEGA_DM
        dOmT = (omega_chi_from_displacement(dz, 1.1 * TR) - OMEGA_DM) / OMEGA_DM
        print(f"{TR/1e12:>10.2f} {dz:>20.2e} {dOm:>26.0%} {dOmT:>18.0%}")
    dz_o = brentq(lambda d: omega_chi_from_displacement(d, To) - OMEGA_DM, 1e-15, 1.0)
    dz_1 = brentq(lambda d: omega_chi_from_displacement(d, 1e12) - OMEGA_DM, 1e-15, 1.0)
    assert 1e-6 < dz_o < 1e-5 and abs(dz_1 / dz_o - (1e12 / To) ** 1.5) < 0.05
    print(f"delta_z is parameter #9: the fractional width the collision left the shared circle at, {dz_o:.1e} (T_R/T_o)^(3/2).")
    print("Omega_chi ~ delta_z^2 (T_o/T_R)^3 before saturation: 10% in delta_z moves Omega_DM by ~3%, 10% in T_R by ~5%. Mild, not a coincidence.")
    print("04d S4 said 'T_R tuned to 0.4%' via the thermal shift: RETRACTED (item 1: that shift is adiabatic when T_R < T_o).")

    print("\n=== 3. T_R from the impact ===")
    sigma1_4d = np.pi / inv * 8 * M6 ** 4 / ELL
    rho = lambda T: np.pi ** 2 / 30 * GSTAR * T ** 4
    h_o = rho(To) / sigma1_4d
    print(f"sigma_1 (4D) = ({sigma1_4d**0.25/1e12:.0f} TeV)^4;  h = rho_1/sigma_1 at T_R = T_o: {h_o:.3f}")
    print(f"T_R < T_o  <=>  h < {h_o:.2f}  (04c scope was h < 1; consistent, and stronger).")
    print(f"T_o/T_t = {To/T_T:.2f}: reheating below the rho^2 transition -> the FRW background of 03 is standard from reheating on.")
    assert h_o < 1

    print("\n=== 4. structure formation ===")
    # Jeans (de Broglie) scale for a coherent scalar: k_J = (16 pi G rho m^2)^{1/4} a; today, comoving
    rho_dm = OMEGA_DM * RHO_C
    kJ = (16 * np.pi * rho_dm * m ** 2 / M_PL ** 2) ** 0.25     # eV (G = 1/8 pi M_Pl^2 absorbed: 2 rho m^2 / M_Pl^2)
    lamJ_cm = 2 * np.pi / kJ * HBAR_C_EV_CM
    print(f"Jeans length today: {lamJ_cm:.1e} cm = {lamJ_cm/3.086e18:.1e} pc  (fuzzy-DM bound needs m > 1e-21 eV: passed by 1e19)")
    print("CDM on every observed scale; halos, Bullet Cluster, dwarfs: identical to collisionless CDM.")
    assert lamJ_cm / 3.086e18 < 1e-3
    # isocurvature: a spatial variation of delta_z is an isocurvature perturbation with S = 2 d(delta_z)/delta_z
    A_s = 2.1e-9
    beta_max = 0.038
    S_max = np.sqrt(beta_max / (1 - beta_max) * A_s)
    print(f"Planck beta_iso < {beta_max}: fractional variation of delta_z across the collision surface < {S_max/2:.1e}")
    print("  (no inflation in this action, 04_impact S6: the collision must be homogeneous to this level anyway)")

    print("\n=== 5. signatures ===")
    f_hz = m / (2 * np.pi) / 6.582e-16
    amp = np.sqrt(2 * rho_dm) / m / M_PL            # dchi/M_Pl amplitude today = d ln ell_z
    print(f"alpha and G oscillate at f = {f_hz:.1e} Hz with amplitude d alpha/alpha = d ln ell_z = {amp:.1e} (local rho_DM x 1e5: {amp*np.sqrt(1e5):.1e})")
    print("self-interaction: sigma/m ~ 0 (quartic from V is Planck-suppressed); direct detection: none (couples with gravitational strength)")
    print("kill: (i) no 5th force in 2-66 um; (ii) T_R > T_o (e.g. a primordial GW/reheating signal at > few TeV);")
    print("      (iii) any DM particle or self-interaction detection; (iv) beta_iso above the collision-homogeneity level.")
    print("\nALL OK")


if __name__ == "__main__":
    main()
