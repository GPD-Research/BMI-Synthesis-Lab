import sympy as sp

phi, m, phi_0 = sp.symbols('phi m phi_0', real=True)
V = sp.Rational(1, 2) * m**2 * (phi - phi_0)**2

dV_dphi = sp.diff(V, phi)
dV_at_phi0 = dV_dphi.subs(phi, phi_0)

print(f"V(phi) = {V}")
print(f"dV/dphi = {dV_dphi}")
print(f"dV/dphi evaluated at phi = phi_0: {dV_at_phi0}")
