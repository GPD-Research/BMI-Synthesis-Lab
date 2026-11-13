"""The time-slip fork as a clock effect (09_clock_effect.md).

Redshift and the CMB temperature are standard; matter clocks ran ahead of the expansion clock.
Physically that is G measured in atomic units: a universal rescaling of all matter clocks is a
change of units. Stellar lifetimes t ~ M/L at fixed M scale as G^-n:
  homology, P ~ G M^2/R^4, T ~ G M/R, L ~ T^4 R/(kappa rho):
  electron scattering n = 4, Kramers n = 15/2 (checked below).
Asks: the G excess needed for a given extra effective age, and its cost in the CMB angular
scale (H ~ sqrt(G)) if it sits at 3 < z < 15.

Run:  python3 tests/clock_effect.py
"""
import numpy as np
import sympy as sp
from scipy.integrate import quad

G, M, R = sp.symbols("G M R", positive=True)
T, rho = G * M / R, M / R ** 3
N = {}
for name, kappa in (("electron scattering", 1), ("Kramers", rho * T ** sp.Rational(-7, 2))):
    N[name] = sp.simplify(sp.diff(sp.log(T ** 4 * R / (kappa * rho)), G) * G)
assert N["electron scattering"] == 4 and N["Kramers"] == sp.Rational(15, 2)
N_LO, N_HI = 4.0, 7.5
print(f"lifetime ~ G^-n, n = {N_LO:g} (massive, electron scattering) .. {N_HI:g} (low mass, Kramers)")

OM, OR = 0.315, 9.1e-5
GYR = 977.8 / 67.4
E = lambda z, g=0.0: np.sqrt((OM * (1 + z) ** 3 + OR * (1 + z) ** 4 + 1 - OM - OR) * (1 + g))
age = lambda z: quad(lambda x: 1 / ((1 + x) * E(x)), z, np.inf, limit=300)[0] * GYR

print("needed G excess (constant over the galaxy's history):")
need = {}
for z, t_eff in ((7.27, 1.38), (14.0, 0.96)):          # the 2026-11-13 claim's ages (08 S3)
    f = t_eff / age(z)
    need[z] = (f ** (1 / N_HI) - 1, f ** (1 / N_LO) - 1)
    print(f"  z = {z}: age {age(z):.2f} Gyr, wanted {t_eff} Gyr -> x{f:.2f}: "
          f"dG/G = +{need[z][0]:.2f} .. +{need[z][1]:.2f}")

print("what a recombination-capped ring-down gives (dG/G at most the CMB bound, then decaying):")
for cap in (0.002, 0.006, 0.03):
    for z in (7.27, 14.0):
        lo, hi = ((1 + cap) ** N_LO - 1) * age(z), ((1 + cap) ** N_HI - 1) * age(z)
        print(f"  cap {cap:.3f}, z = {z}: extra effective age < +{hi * 1e3:.0f} Myr (n = 7.5), +{lo * 1e3:.0f} (n = 4)")

D = lambda g: quad(lambda z: 1 / E(z, g if 3 < z < 15 else 0.0), 0, 1090, points=[3, 15], limit=400)[0]
print("distance to last scattering, G excess g at 3 < z < 15 (theta_* known to ~3e-4):")
for g in (0.03, 0.1, 0.2):
    print(f"  g = {g}: dD/D = {D(g) / D(0) - 1:+.4f}")
assert need[14.0][0] > 0.15 and abs(D(0.1) / D(0) - 1) > 30 * 3e-4
print("ALL OK")
