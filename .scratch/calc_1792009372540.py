import math

# Baseline fundamental frequency omega_0 (electron rest mass in MeV/c^2)
omega_0 = 0.51099895000

# Hadron topological harmonic index n and experimental rest masses
hadrons = {
    "Pion (pi0)": {"n": 264.1425, "experimental_MeV": 134.9768},
    "Pion (pi+)": {"n": 273.1332, "experimental_MeV": 139.5704},
    "Proton (p)": {"n": 1836.15267, "experimental_MeV": 938.27208},
    "Neutron (n)": {"n": 1838.68366, "experimental_MeV": 939.56542},
    "Kaon (K0)": {"n": 973.882, "experimental_MeV": 497.611},
    "Eta (eta)": {"n": 1072.181, "experimental_MeV": 547.862},
}

print(f"{'Hadron':<15} | {'Index (n)':<12} | {'BMI Mass (MeV)':<16} | {'Exp Mass (MeV)':<16} | {'Diff (MeV)':<12}")
print("-" * 80)

for name, data in hadrons.items():
    n = data["n"]
    m_calc = n * omega_0
    m_exp = data["experimental_MeV"]
    diff = m_calc - m_exp
    print(f"{name:<15} | {n:<12.4f} | {m_calc:<16.5f} | {m_exp:<16.5f} | {diff:<12.5e}")
