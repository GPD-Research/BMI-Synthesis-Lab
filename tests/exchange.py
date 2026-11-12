"""Provisional tenth (ledger.md, 2026-11-11 rule): inter-brane / dark-sector energy exchange.

Einstein frame of 06_predictions.md S1: ds_5^2 = e^{-s} g_4 + e^{2s} dz^2, s = ln(ell_z/ell_z0),
chi = sqrt(3/2) M_Pl s.  A brane-frame term ell_z^n becomes e^{(n-2)s} in this frame.

A. The coupling already in the action: V_* proportional to ell_z (03 S2) -> e^{-s} e^{-c Phi}. Its
   effect on the DM (the chi condensate) is a mass shift and a tadpole of order (H0/m_chi)^2.
B. A tenth coupling that makes m_DM depend on Phi must act through the stabilizer
   U = C_z e^{-6s} - pi |delta_1| e^{-s} (brane frame C_z/ell^4 + pi delta_1 ell): changing
   delta_1 (or C_z) moves the minimum s_bar, and s_bar sets alpha, mu = m_p/m_e and G.
   Lock: d ln m_chi = -3 d s_bar (C_z fixed).  Then the quasar mu and alpha bounds cap the
   DM-mass drift, hence any exchange-induced shift of w.

Run:  python3 tests/exchange.py
"""
import sympy as sp

s, C, d = sp.symbols("s C d", positive=True)

# brane-frame exponent n -> Einstein-frame exponent n - 2
assert sp.simplify(sp.exp(1 * s) * sp.exp(-2 * s) - sp.exp(-s)) == 0

U = C * sp.exp(-6 * s) - d * sp.exp(-s)
sbar = sp.log(6 * C / d) / 5
assert sp.simplify(sp.diff(U, s).subs(s, sbar)) == 0
m2 = sp.simplify(sp.diff(U, s, 2).subs(s, sbar))          # (3/2) M_Pl^2 m_chi^2
lock = sp.simplify(sp.diff(sp.log(m2) / 2, d) / sp.diff(sbar, d))
assert sp.simplify(lock + 3) == 0, lock                    # d ln m_chi / d s_bar = -3
print(f"stabilizer: e^(5 s_bar) = 6 C/|d1|,  d ln m_chi / d s_bar = {lock}")

# A: coupling in the action
H0 = 1.44e-33          # eV
M_PL = 2.435e27        # eV
M_CHI = 1.0e-2 * (2 / 3) ** 0.5
OMEGA_DE = 0.685
rho_de = 3 * OMEGA_DE * H0 ** 2 * M_PL ** 2
dm2 = (2 / 3) * rho_de / M_PL ** 2 / M_CHI ** 2            # d^2/dchi^2 of rho_de e^{-sqrt(2/3)chi/M}
print(f"A: in-action DM-DE coupling: delta m^2/m^2 = {dm2:.1e}, alpha drift of the same order")
assert dm2 < 1e-55

# B: tenth coupling through the stabilizer, capped by mu and alpha (quasar bounds, [verify])
DLNMU_DS = 0.90 * (-9.76)          # (1 - s_piN) d ln Lambda_3 / d s; m_e and the Weyl -1/2 cancel
DLNALPHA_DS = -1.0
MU_BOUND = 1e-7                    # |dmu/mu|, z ~ 0.9 methanol/ammonia
ALPHA_BOUND = 1e-5                 # |dalpha/alpha|, z ~ 1-3
ds = min(MU_BOUND / abs(DLNMU_DS), ALPHA_BOUND / abs(DLNALPHA_DS))
dlnm = 3 * ds
OMEGA_DM = 0.265
dw = OMEGA_DM / OMEGA_DE * dlnm / 3 / 0.64                 # per e-fold since z ~ 0.9
print(f"B: |ds_bar| < {ds:.1e}  ->  |d ln m_DM| < {dlnm:.1e}  ->  |Delta w| < {dw:.0e}")
NEED = 0.3                                                 # DESI CPL: w ~ -1.3 at z ~ 1
print(f"   DESI needs |Delta w| ~ {NEED}: short by {NEED / dw:.0e}")
assert NEED / dw > 1e5
print("ALL OK")
