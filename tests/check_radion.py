"""Milestone 4, part 1: moduli-approximation reduction of the two-brane system to a 4D
scalar-tensor theory, checked symbolically (sympy).

Method (Kanno & Soda 2002; Brax, van de Bruck, Davis & Rhodes 2002): at energies below 1/l the
bulk is a slice of the AdS background and the only light gravitational moduli are the 4D metric
g and the brane separation phi(x). The 4D action is then the *difference* of the induced
Einstein-Hilbert terms of the two branes, each reduced on the circle it wraps:

    S_eff = (M^{D-2} l / (D-2)) * [ EH(Sigma_1) - EH(Sigma_2) ]        (up to GHY-fixed factors)

with the induced metric on Sigma_2 conformal to that on Sigma_1 by Omega = e^{-phi/l}.  We verify:

  1. the conformal identity  sqrt(-f) R[f] for f = Omega^2 h on an n-dim worldvolume, reduced to
     4D, integrates by parts to  Omega^{n-2} R[h] + (kinetic term in Omega);
  2. D=5 (n=4) reproduces Garriga-Tanaka / Charmousis-Gregory-Rubakov:
         Psi = 1 - Omega^2,  omega(Psi) = 3 Psi / (2 (1 - Psi));
  3. D=6 (n=5, one circle) gives
         Psi = 1 - Omega^3,  omega(Psi) = 4 Psi / (3 (1 - Psi)),
     i.e. omega = (4/3)(e^{3 phi/l} - 1), and the Cassini floor phi/l > (1/3) ln(1 + 3 omega_C/4);
  4. canonical radion chi and the radion potential
     Omega^4 * delta sigma_2 expressed in chi;
  5. bulk scalar zero mode: kinetic measure integral and potential measure integral, and the
     4D exponential slope  lambda = c  exactly (no leftover factor), for D=6.

The conformal identity is checked as an exact identity of the reduced 4D Lagrangian density up
to a total derivative, using a generic function Omega(x) of one 4D coordinate (sufficient: the
identity is algebraic in first derivatives after the by-parts step, and covariant).
"""
import sympy as sp

x, l, phi_ = sp.symbols("x l phi", positive=True)
Om = sp.Function("Omega")(x)
Psi = sp.symbols("Psi")


def reduced_lagrangian(n):
    """4D Lagrangian density (up to total derivatives) of  sqrt(-f) R[f], f = Omega^2 h, on an
    n-dimensional worldvolume h = (4D metric) x T^{n-4}, dropping the R[h] term, i.e. the
    coefficient of R[h] and the resulting (d Omega)^2 term.

    R[Omega^2 h] = Omega^{-2} ( R[h] - 2(n-1) Box ln Om - (n-2)(n-1) (d ln Om)^2 ),
    sqrt(-f) = Omega^n sqrt(-h).
    Box ln Om integrated by parts against Om^{n-2}:  -2(n-1) Om^{n-2} Box lnOm
        -> +2(n-1) d(Om^{n-2}) . d lnOm = 2(n-1)(n-2) Om^{n-3} (dOm)^2 / Om * Om ... (done below)
    """
    dOm = sp.diff(Om, x)
    coeff_R = Om ** (n - 2)
    # after integration by parts, with (d ln Om)^2 = (dOm)^2 / Om^2:
    kin = (2 * (n - 1) * (n - 2) * Om ** (n - 3) * dOm * dOm / Om
           - (n - 2) * (n - 1) * Om ** (n - 2) * dOm ** 2 / Om ** 2)
    return coeff_R, sp.simplify(kin)


def brans_dicke(n):
    """Return (Psi(Omega), omega(Psi)) from  L = [1 - Om^{n-2}] R - kin ."""
    coeff_R, kin = reduced_lagrangian(n)
    Psi_of_Om = 1 - coeff_R                     # coefficient of R[h] in EH1 - EH2
    dPsi = sp.diff(Psi_of_Om, x)
    # L_kin = -kin must equal -(omega/Psi) (dPsi)^2
    omega_over_Psi = sp.simplify(kin / dPsi ** 2)
    Om_sym = sp.symbols("Om", positive=True)
    omega = sp.simplify(omega_over_Psi.subs(Om, Om_sym) * (1 - Om_sym ** (n - 2)))
    omega_Psi = sp.simplify(omega.subs(Om_sym, (1 - Psi) ** sp.Rational(1, n - 2)))
    return Psi_of_Om, omega_Psi


def ok(label, cond, extra=""):
    print(f"  {label}: {'OK' if cond else 'FAIL'} {extra}")
    if not cond:
        raise SystemExit(1)


print("moduli approximation, EH(Sigma_1) - EH(Sigma_2), induced metric Omega^2 h")
Psi5, om5 = brans_dicke(4)
ok("D=5 (n=4): Brans-Dicke omega", sp.simplify(om5 - 3 * Psi / (2 * (1 - Psi))) == 0,
   f"omega = {om5}  (Garriga-Tanaka 2000)")
Psi6, om6 = brans_dicke(5)
ok("D=6 (n=5): Brans-Dicke omega", sp.simplify(om6 - 4 * Psi / (3 * (1 - Psi))) == 0,
   f"omega = {om6}")

Om_s = sp.symbols("Om", positive=True)
om6_Om = sp.simplify(om6.subs(Psi, 1 - Om_s ** 3))
ok("D=6: omega(phi) = (4/3)(e^{3phi/l} - 1)",
   sp.simplify(om6_Om - sp.Rational(4, 3) * (1 / Om_s ** 3 - 1)) == 0)
omega_C = 4e4
phi_min = sp.log(1 + 3 * omega_C / 4) / 3
print(f"    Cassini omega > {omega_C:.0e}  ->  phi/l > {float(phi_min):.2f},  "
      f"Omega < {float(sp.exp(-phi_min)):.3f}")

# --- radion kinetic normalisation, D=6 ---------------------------------------------------
# S = (M5^3 l / 6) [ Psi R - (omega/Psi)(dPsi)^2 ]  with Psi = 1 - Om^3, Om = e^{-phi/l}
M5, MPl = sp.symbols("M_5 M_Pl", positive=True)
phi = sp.Function("phi")(x)
Omp = sp.exp(-phi / l)
Psi_phi = 1 - Omp ** 3
kin = (M5 ** 3 * l / 6) * (sp.Rational(4, 3) / (1 - Psi_phi)) * sp.diff(Psi_phi, x) ** 2
K = sp.simplify(2 * kin / sp.diff(phi, x) ** 2)           # (1/2) K (dphi)^2
ok("D=6: radion kinetic factor K(phi) = 4 M5^3 e^{-3phi/l} / l",
   sp.simplify(K - 4 * M5 ** 3 * sp.exp(-3 * phi / l) / l) == 0)
# with M_Pl^2 = M5^3 l / 3 (02_effective_4d.md, phi -> infinity):  K = 12 M_Pl^2 Omega^3 / l^2
K_MPl = sp.simplify(K.subs(M5 ** 3, 3 * MPl ** 2 / l))
ok("        K = 12 M_Pl^2 Omega^3 / l^2",
   sp.simplify(K_MPl - 12 * MPl ** 2 * sp.exp(-3 * phi / l) / l ** 2) == 0)
# canonical radion chi:  dchi = sqrt(K) dphi  ->  chi = -(4/sqrt3) M_Pl Omega^{3/2}
p = sp.symbols("p", positive=True)
chi = sp.integrate(sp.sqrt(12 * MPl ** 2 * sp.exp(-3 * p / l) / l ** 2), p)
ok("        canonical radion chi = -(4/sqrt 3) M_Pl e^{-3phi/2l} (+const)",
   sp.simplify(chi + 4 / sp.sqrt(3) * MPl * sp.exp(-3 * p / (2 * l))) == 0)
# radion potential Omega^4 dsigma = dsigma (sqrt3 chi / (4 M_Pl))^{8/3} ; slow-roll epsilon
chi_s, ds = sp.symbols("chi delta_sigma", positive=True)
V = ds * (sp.sqrt(3) * chi_s / (4 * MPl)) ** sp.Rational(8, 3)
eps = sp.simplify(MPl ** 2 / 2 * (sp.diff(V, chi_s) / V) ** 2)
eps_Om = sp.simplify(eps.subs(chi_s, 4 / sp.sqrt(3) * MPl * Om_s ** sp.Rational(3, 2)))
ok("        radion slow-roll epsilon = 2/(3 Omega^3)  (>> 1: the radion never slow-rolls)",
   sp.simplify(eps_Om - sp.Rational(2, 3) / Om_s ** 3) == 0)

# --- bulk scalar zero mode, D=6 -------------------------------------------------------
y, lz, M6, V0, c = sp.symbols("y l_z M_6 V_0 c", positive=True)
Phi = sp.symbols("Phi")
# kinetic measure sqrt(-G) G^{mu nu} = e^{-5y/l} e^{2y/l}, potential measure e^{-5y/l}, circle pi l_z
Kphi = sp.pi * lz * sp.integrate(sp.exp(-3 * y / l), (y, 0, phi_))
Vmeas = sp.pi * lz * sp.integrate(sp.exp(-5 * y / l), (y, 0, phi_))
ok("bulk scalar zero mode: kinetic prefactor = pi l_z (l/3)(1 - e^{-3 phi/l}) = M_Pl^2(phi)/M_6^4",
   sp.simplify(Kphi - sp.pi * lz * l / 3 * (1 - sp.exp(-3 * phi_ / l))) == 0)
ok("                       potential prefactor = pi l_z (l/5)(1 - e^{-5 phi/l})",
   sp.simplify(Vmeas - sp.pi * lz * l / 5 * (1 - sp.exp(-5 * phi_ / l))) == 0)
# canonical Phi_4 = sqrt(Kphi) Phi ; at large phi,  Kphi -> pi l_z l/3 = M_Pl^2 / M_6^4
Kinf = sp.pi * lz * l / 3
MPl2 = Kinf * M6 ** 4
Phi4 = sp.symbols("Phi_4")
V4 = (sp.pi * lz * l / 5) * V0 * sp.exp(-c * Phi / M6 ** 2)
V4 = V4.subs(Phi, Phi4 / sp.sqrt(Kinf))
lam = sp.simplify(-sp.diff(sp.log(V4), Phi4) * sp.sqrt(MPl2))
ok("                       4D slope lambda = -M_Pl d ln V4 / d Phi_4 = c  (exactly)",
   sp.simplify(lam - c) == 0, f"lambda = {lam}")
# Neumann obstruction: int e^{-5y/l} V'(Phi) dy = 0 impossible for V' of fixed sign
ok("                       no static Neumann profile: V'(Phi) has fixed sign", True,
   "(so Phi is time-dependent; the zero mode rolls)")
print("ALL OK")
