"""Milestone 5d: stabilizing the circle radius ell_z (v2/04d_circle.md).

04c_approach.md S6 found that ell_z is a flat direction of the fixed action and couples to the SM
gauge couplings (1/g_4^2 ~ ell_z). This script evaluates the finite stabilizer menu:

  option 0  the two ell_z-dependent terms ALREADY in the action: brane Casimir energy (~ 1/ell_z^4
            on the 3-brane) and the bulk-scalar term V_* = pi ell_z ell V_0/5 (~ +ell_z).
            -> a minimum exists but sits at ell_z^-1 ~ meV (excluded by LHC) and moves with the
               dark-energy roll (alpha drift O(0.1) since z~3): DEAD.
  option A  Casimir + a negative detuning of sigma_1 (one new number delta_1 < 0):
            V(l) = C_SM / l^4 + pi delta_1 l.  Minimum, modulus mass, Eot-Wash test, alpha drift,
            and the cosmological abundance of the modulus oscillation (moduli problem).
  option B  flux of a new bulk 1-form through z (+1/l) + detuning: same structure as A with a
            shallower repulsion; +2 numbers, dominated by A.
  option C  Goldberger-Wise second scalar: needs codimension-2 branes at the orbifold fixed points
            (new content) -> not in the menu without a new fork.

Conventions: natural units, eV.  M_Pl = 2.435e27 eV (reduced).  All Casimir coefficients carry a
[verify] on the O(1) factor; the conclusions below depend only on sign and scaling.
Run:  python3 tests/circle.py
"""
import numpy as np
from scipy.special import zeta

M_PL = 2.435e27          # eV
RHO_DE = (2.25e-3) ** 4  # eV^4, dark-energy density today
RHO_C = RHO_DE / 0.69    # critical density
OMEGA_DM = 0.265
T_EQ = 0.80              # eV, matter-radiation equality
GSTAR_HOT = 106.75
EOT_WASH_M_MIN = 3e-3    # eV: gravitational-strength Yukawa excluded for range > ~65 um  [verify]
HBAR_C_EV_CM = 1.9733e-5 # eV cm

# --- 1. Casimir sign from the SM on the 4-brane wrapping the circle -----------------------------
# 5D fields on S^1/Z_2 of radius l. Bosonic dof on the brane: gauge 12 x 2 = 24, Higgs 4 -> 28.
# Fermionic: 45 Weyl x 2 = 90 (no nu_R). Periodic fermions.  Vacuum energy per unit 4-volume of a
# 5D field tower with KK masses n/l, summed over the circle (Appelquist-Chodos 1983 form):
#     rho_4 = -(N_b - N_f) * 3 zeta(5) / (64 pi^6) / l^4  (orbifold: half the modes)   [verify O(1)]
N_B, N_F = 28, 90
CASIMIR_COEFF = 3 * zeta(5) / (64 * np.pi ** 6)   # ~ 5.1e-5
C_SM = -(N_B - N_F) * CASIMIR_COEFF               # > 0: repulsive, pushes l large


def V_casimir(l):
    return C_SM / l ** 4


# --- 2. Option 0: Casimir + the existing V_* = pi ell_z ell V_0 / 5 ---------------------------------
def option0(ell_over_lz_scale=1.0):
    # V(l) = C/l^4 + k l with k l_z0 = rho_DE today (V_* is the dark energy). Minimum at
    # l^5 = 4C/k. Take l_z0 as the unknown: k = rho_DE / l_z0; self-consistency l_z0 = l_min:
    # l_z0^5 = 4 C l_z0 / rho_DE  ->  l_z0^4 = 4C/rho_DE.
    l_min = (4 * C_SM / RHO_DE) ** 0.25
    inv_l_ev = 1 / l_min
    # alpha ~ 1/l_z; the minimum tracks V_*(t) ~ V(Phi(t)): d ln l / d ln V = -1/5.
    return inv_l_ev


# --- 3. Option A: Casimir + negative tension detuning ---------------------------------------------
def optionA(inv_lz):
    """Given the KK scale 1/ell_z (eV), return (delta_1 [eV^5], m_modulus [eV], V_min [eV^4])."""
    l = 1 / inv_lz
    # V = C/l^4 + pi d l ; V' = 0 -> pi d = 4C/l^5  (d < 0)
    pi_d = -4 * C_SM / l ** 5
    delta_1 = pi_d / np.pi
    Vpp = 20 * C_SM / l ** 6            # d^2V/dl^2
    # canonical field: kinetic term of the volume modulus is M_Pl^2 (d ln l)^2 x O(1) -> chi = M_Pl ln l  [verify O(1)]
    m2 = Vpp * l ** 2 / M_PL ** 2
    V_min = C_SM / l ** 4 + pi_d * l    # = -3C/l^4 : negative, must be cancelled against Lambda
    return delta_1, np.sqrt(m2), V_min


def T_osc(m):
    """Temperature at which H = m (radiation domination)."""
    # H^2 = pi^2/90 g* T^4 / M_Pl^2
    return (m * M_PL) ** 0.5 * (90 / (np.pi ** 2 * GSTAR_HOT)) ** 0.25


def modulus_abundance_ratio(m, inv_lz, dchi_over_mpl):
    """rho_chi/rho_rad at T_eq for an initial displacement dchi (in M_Pl) that starts oscillating at T_osc."""
    Tosc = T_osc(m)
    rho_chi = 0.5 * m ** 2 * (dchi_over_mpl * M_PL) ** 2
    rho_rad = 3 * m ** 2 * M_PL ** 2          # = 3 H^2 M_Pl^2 at onset
    r0 = rho_chi / rho_rad
    return r0 * Tosc / T_EQ, Tosc             # matter/radiation grows as a ~ 1/T (g* changes ignored)


def required_displacement(m):
    """dchi/M_Pl giving Omega_chi = Omega_DM (rho_chi/rho_rad = Omega_DM/Omega_m ~ 0.84 at T_eq)."""
    Tosc = T_osc(m)
    target = OMEGA_DM / 0.315
    r0 = target * T_EQ / Tosc
    return np.sqrt(6 * r0)


def alpha_oscillation_amplitude(m, rho_local_gev_cm3=0.4):
    rho = rho_local_gev_cm3 * 1e9 * HBAR_C_EV_CM ** 3     # eV^4
    dchi = np.sqrt(2 * rho) / m
    return dchi / M_PL                                     # d alpha/alpha = d ln l = dchi/M_Pl


if __name__ == "__main__":
    print("=== 1. Casimir sign ===")
    print(f"SM on the brane: N_b = {N_B}, N_f = {N_F}, N_b - N_f = {N_B - N_F} -> C_SM = {C_SM:.3e} > 0 (repulsive)")
    print("Bulk graviton (9 dof) + Phi (1) add +10 bosonic: sign unchanged.\n")

    print("=== 2. Option 0: terms already in the action ===")
    inv0 = option0()
    print(f"minimum of C/l^4 + V_*(l) at 1/ell_z = {inv0:.2e} eV  (LHC needs >~ 5e12 eV)  -> EXCLUDED")
    print("and d ln alpha / d ln V_DE = -1/5: thawing roll of O(0.3) since z~3 -> |dalpha/alpha| ~ 0.06 vs 1e-5 -> EXCLUDED\n")
    assert inv0 < 1e0

    print("=== 3. Option A: Casimir + negative detuning delta_1 of sigma_1 ===")
    M6 = 2.7e16   # eV, from M_Pl^2 = pi l_z l M_6^4/3 with l = 10 um, 1/l_z ~ 5 TeV  [verify]
    sigma1 = 8 * M6 ** 4 / (10e-4 / HBAR_C_EV_CM)  # 8 M_6^4 / ell, ell = 10 um in eV^-1
    print(f"{'1/l_z [TeV]':>12} {'delta_1/sigma_1':>16} {'m_chi [eV]':>12} {'1/m [um]':>10} {'T_osc [TeV]':>12} {'dchi/M_Pl for DM':>18} {'Eot-Wash':>9}")
    rows = {}
    for inv_tev in [1, 2, 5, 10, 30]:
        inv = inv_tev * 1e12
        d1, m, Vmin = optionA(inv)
        Tosc = T_osc(m)
        dchi = required_displacement(m)
        ok = "pass" if m > EOT_WASH_M_MIN else "FAIL"
        rows[inv_tev] = (d1, m, Tosc, dchi)
        print(f"{inv_tev:>12} {d1/sigma1:>16.2e} {m:>12.3e} {HBAR_C_EV_CM*1e4/m:>10.1f} {Tosc/1e12:>12.2f} {dchi:>18.2e} {ok:>9}")
    d1, m, Tosc, dchi = rows[10]
    print(f"\nV_min = -3 C/l^4: a negative vacuum energy of -(3 C)^(1/4)/l_z = {(3*C_SM)**0.25*1e13:.2e} eV scale,"
          " to be cancelled by Lambda_6 retuning (the CC problem, not new).")
    print(f"m_chi scales as (1/l_z)^2: m = {m:.3e} eV x (1/l_z / 10 TeV)^2.")
    # window: lower edge from Eot-Wash (m > 3e-3 eV), upper edge from |delta_1| < sigma_1
    inv_lo = 1e13 * (EOT_WASH_M_MIN / m) ** 0.5
    inv_hi = 1e13 * (sigma1 / abs(d1)) ** 0.2
    print(f"window from the two conditions: {inv_lo/1e12:.1f} TeV < 1/l_z < {inv_hi/1e12:.1f} TeV;"
          f" modulus range {HBAR_C_EV_CM*1e4/(m*(inv_hi/1e13)**2):.0f}-{HBAR_C_EV_CM*1e4/EOT_WASH_M_MIN:.0f} um")
    assert m > EOT_WASH_M_MIN
    assert rows[1][1] < EOT_WASH_M_MIN     # 1 TeV KK scale fails Eot-Wash
    assert 4e12 < inv_lo < 8e12 and 2e13 < inv_hi < 4e13
    print("\nalpha drift at the minimum: none (the minimum does not depend on phi or Phi).")

    print("\n=== 4. Cosmology of the modulus (the moduli problem) ===")
    r_O1, _ = modulus_abundance_ratio(m, 1e13, 1.0)
    print(f"O(1) displacement (thermal shift when T > 1/l_z): rho_chi/rho_rad at T_eq = {r_O1:.1e} -> overclosure by 1e{np.log10(r_O1):.0f}")
    Gamma = m ** 3 / M_PL ** 2
    print(f"decay rate m^3/M_Pl^2 = {Gamma:.1e} eV -> lifetime {6.58e-16/Gamma/3.15e7:.1e} yr: it does not decay")
    print(f"Omega_chi = Omega_DM needs dchi/M_Pl = {dchi:.1e}, i.e. |d ell_z/ell_z| = {dchi:.1e} at T ~ {Tosc/1e12:.1f} TeV")
    # thermal shift of the minimum is ~ exp(-1/(l_z T_RH)) if the KK modes are never thermal:
    x = -np.log(dchi)
    print(f"if the KK modes are never in equilibrium, the shift is ~ e^(-1/(l_z T_RH)); dchi = {dchi:.1e} needs 1/(l_z T_RH) ~ {x:.1f}"
          f" -> T_RH ~ {1e13/x/1e9:.0f} GeV (for 1/l_z = 10 TeV)")
    da = alpha_oscillation_amplitude(m)
    print(f"if chi IS the dark matter: alpha oscillates at f = {m/6.58e-16/1e12:.1e} THz with amplitude dalpha/alpha = {da:.1e} (unobservable)")
    assert r_O1 > 1e6
    assert dchi < 1e-5

    print("\n=== 5. Option B (flux) ===")
    print("V = n^2 F / l + pi delta_1 l: minimum at l^2 = n^2 F/(pi|delta_1|); modulus mass m^2 ~ 2 n^2 F/(l^3 M_Pl^2) x l^2:")
    print("same Eot-Wash / moduli-problem structure as A with two new numbers (n, F) instead of one -> dominated by A.")
    print("\nALL OK")
