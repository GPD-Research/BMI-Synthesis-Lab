"""Symbolic checks for the thick-brane fork (v2/10_thick_brane.md §2).

Metric e^{2A(y)} eta_ab dx^a dx^b + dy^2 in D = 6 (a runs over t, x1..x3 and the circle z: all five
brane directions warped, as in v2/01_action.md §3), sourced by a canonical bulk scalar W(y) with
potential U(W) that includes Lambda_6, and S = int sqrt(-G) [M^4 R/2 - (dW)^2/2 - U].

1. Null energy condition. For the null vector k = (e^{-A}, 0, 0, 0, 0, 1),
       G_MN k^M k^N = -4 A''   and   T_MN k^M k^N = W'^2,
   so a canonical scalar forces A'' = -W'^2 / (4 M^4) <= 0: A' can only decrease along y.
2. Smooth Sigma_1. A' = -tanh(y/w)/l is such a wall: W'^2 = 4 M^4 sech^2(y/w)/(l w) >= 0, its integrated
   tension -4 M^4 [A'] = 8 M^4/l is the two-sided RS value, and U -> -10 M^4/l^2 = Lambda_6 far from it.
   U is read off from A (U = W'^2/2 - 10 M^4 A'^2): a flat wall exists only for a U built to match,
   i.e. the RS tuning moves into the shape of U.
3. Sigma_2 cannot be smoothed. Across Sigma_2 (Z2 reflection at y = phi) A' runs from -1/l to +1/l,
   so int W'^2 dy = -4 M^4 * (2/l) < 0: impossible for any canonical field. A negative-tension
   brane has no smooth canonical-scalar wall.

Requires sympy. Run: python3 tests/thick_brane.py
"""
import sys

import sympy as sp

from check_background import einstein_tensor

y, w, l, M = sp.symbols("y w ell M", positive=True)
coords = sp.symbols("t x1 x2 x3 z yy")
Y = coords[5]
failures = []


def check(name, cond):
    print(("ok   " if cond else "FAIL ") + name)
    if not cond:
        failures.append(name)


A = sp.Function("A")(Y)
g = sp.diag(-sp.exp(2 * A), *[sp.exp(2 * A)] * 4, 1)
G, _ = einstein_tensor(coords, g)
k = sp.Matrix([sp.exp(-A), 0, 0, 0, 0, 1])
Gkk = sp.simplify((k.T * G * k)[0])
check("NEC: G_MN k k = -4 A''", sp.simplify(Gkk + 4 * sp.diff(A, Y, 2)) == 0)
Gyy = sp.simplify(G[5, 5])
check("G_yy = 10 A'^2", sp.simplify(Gyy - 10 * sp.diff(A, Y) ** 2) == 0)
# scalar stress tensor for W(y): T_MN k k = W'^2, T_yy = W'^2/2 - U, so for a given A'(y):
#   W'^2 = -4 M^4 A'',  U = W'^2/2 - 10 M^4 A'^2
Ap = -sp.tanh(y / w) / l
wp2 = sp.simplify(-4 * M**4 * sp.diff(Ap, y))
u = sp.simplify(wp2 / 2 - 10 * M**4 * Ap**2)
check("smooth Sigma_1: W'^2 = 4 M^4 sech^2(y/w)/(l w)", sp.simplify(wp2 - 4 * M**4 / (l * w * sp.cosh(y / w) ** 2)) == 0)
tension = sp.integrate(wp2, (y, -sp.oo, sp.oo))
check("smooth Sigma_1: integrated tension = 8 M^4/l (two-sided RS)", sp.simplify(tension - 8 * M**4 / l) == 0)
check("smooth Sigma_1: U -> Lambda_6 = -10 M^4/l^2 far from the wall", sp.simplify(sp.limit(u, y, sp.oo) + 10 * M**4 / l**2) == 0)

jump = sp.Rational(2) / l  # [A'] across Sigma_2: -1/l -> +1/l
check("Sigma_2: int W'^2 dy = -8 M^4/l < 0 (no canonical wall)", sp.simplify(-4 * M**4 * jump) < 0)

if failures:
    sys.exit(f"{len(failures)} check(s) failed")
print("thick_brane: all checks passed")
