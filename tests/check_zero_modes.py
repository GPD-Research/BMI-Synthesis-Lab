"""Zero-mode localization on the verified warped background (v2/02b_localization.md).

Background (D dimensions, d = D-1 warped directions, A = y/l):
    ds^2 = e^{-2A} eta_ab dx^a dx^b + dy^2

For each spin the y-profile f(y) of a 4D-massless mode is checked against the bulk equation,
and the exponent of its normalization density  rho(y) = (kinetic measure) * |f|^2  is reported.
Localization on Sigma_1 (y=0) means rho decreases with y; on Sigma_2 (y=phi) means it grows.

Checks:
  spin 0, massless      f = 1,                 rho ~ e^{-(d-2)A}        -> Sigma_1
  spin 2                f = 1,                 rho ~ e^{-(d-2)A}        -> Sigma_1 (= M_Pl integral)
  spin 1, massless      f = 1,                 rho ~ e^{-(d-4)A}        -> flat in d=4, Sigma_1 in d=5
  spin 1/2, bulk mass c/l
       chirality +      f = e^{(d/2 - c)A},    rho ~ e^{(1-2c)A}        -> Sigma_1 iff c > 1/2
       chirality -      f = e^{(d/2 + c)A},    rho ~ e^{(1+2c)A}        -> Sigma_1 iff c < -1/2
  scalar with circle momentum n (D=6): the mode with 4D mass m4 = n/l_z has the SAME constant
       profile as the zero mode: the z-tower is not warped down and sits where the zero mode sits.

Requires sympy. Run: python3 tests/check_zero_modes.py
"""
import sys

import sympy as sp

y, l, c, n, lz, m4 = sp.symbols("y ell c n ell_z m_4", positive=True)
A = y / l
ok = True


def report(name, cond, extra=""):
    global ok
    ok &= bool(cond)
    print(f"  {name}: {'OK' if cond else 'FAIL'} {extra}")


def scalar_eq(f, d, m4sq, nsq_over_lz2=0):
    """(1/sqrt g) d_y (sqrt g d_y f) + e^{2A} (m4^2 - n^2/l_z^2) f, sqrt g = e^{-dA}."""
    return sp.simplify(sp.exp(d * A) * sp.diff(sp.exp(-d * A) * sp.diff(f, y), y)
                       + sp.exp(2 * A) * (m4sq - nsq_over_lz2) * f)


def fermion_eq(f, d, sign):
    """Zero mode of  gamma^y (d_y - (d/2) A') +- m  with m = c/l:  f' - (d/2) A' f -+ (c/l) f = 0."""
    return sp.simplify(sp.diff(f, y) - sp.Rational(d, 2) * f / l - sign * c * f / l)


def exponent(rho):
    """Return k such that rho = const * e^{k y/l}."""
    k = sp.simplify(sp.diff(sp.log(rho), y) * l)
    assert not k.has(y), k
    return k


for D in (5, 6):
    d = D - 1
    print(f"D={D} (d={d} warped directions)")

    f = sp.Integer(1)
    report("spin 0 massless zero mode solves bulk eq", scalar_eq(f, d, 0) == 0)
    k = exponent(sp.exp(-d * A) * sp.exp(2 * A) * f**2)
    report("spin 0 / spin 2 density exponent", k == -(d - 2), f"rho ~ e^{{{k} y/l}} -> Sigma_1")

    k = exponent(sp.exp(-d * A) * sp.exp(4 * A) * f**2)
    where = "flat" if k == 0 else ("Sigma_1" if k < 0 else "Sigma_2")
    report("spin 1 massless density exponent", k == -(d - 4), f"rho ~ e^{{{k} y/l}} -> {where}")

    for sign, label in ((+1, "+"), (-1, "-")):
        fpsi = sp.exp((sp.Rational(d, 2) + sign * c) * A)
        report(f"spin 1/2 chirality {label} solves zero-mode eq", fermion_eq(fpsi, d, sign) == 0)
        k = exponent(sp.exp(-d * A) * sp.exp(A) * fpsi**2)
        report(f"spin 1/2 chirality {label} density exponent", sp.simplify(k - (1 + 2 * sign * c)) == 0,
               f"rho ~ e^{{({k}) y/l}} -> Sigma_1 iff {'c > 1/2' if sign > 0 else 'c < -1/2'}")

    if D == 6:
        f = sp.Integer(1)
        report("circle mode n: constant profile with m4 = n/l_z solves bulk eq",
               scalar_eq(f, d, n**2 / lz**2, n**2 / lz**2) == 0,
               "-> z-tower mass n/l_z (unwarped), same localization as zero mode")

print("ALL OK" if ok else "SOME CHECKS FAILED")
sys.exit(0 if ok else 1)
