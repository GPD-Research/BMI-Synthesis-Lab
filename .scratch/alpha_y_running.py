import numpy as np
import sys
import os

# Insert project root for relative import of tests.predictions
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from tests.predictions import range_um, alpha_bound, alpha_yukawa

# Constants and inputs
alpha_s_MZ = 0.1180
M_Z = 91.1876e9  # GeV -> eV
m_c = 1.27e9     # GeV -> eV
m_b = 4.18e9
m_t = 162.5e9
m_N = 938.9e6
sigma_piN = 50e6       # MeV -> eV
sigma_piN_err = 10e6
sigma_s = 45e6
sigma_s_err = 20e6

# Matching scale factors
k_central = 1.0
k_var = [0.5, 2.0]
inv_lz_vec = [10, 14, 29]  # in TeV
inv_lz_eV = [x * 1e12 for x in inv_lz_vec]

def get_s(sigma_piN, sigma_s, m_N):
    return (sigma_piN + sigma_s) / m_N

def compute_all(inv_lz_eV, k, sigma_piN, sigma_piN_err, sigma_s, sigma_s_err):
    # Central point: inv_lz = 10 TeV
    inv_lz = inv_lz_eV[0] * k

    def mN_sigma(sigma):
        lz = np.exp(sigma) / inv_lz
        inv_lz_shift = 1.0 / lz
        from tests.predictions import dlnm_dsigma
        tot, parts = dlnm_dsigma(inv_lz_shift)
        return tot, parts

    tot0, parts0 = mN_sigma(0)
    weyl = parts0["weyl"]
    cutoff = parts0["cutoff"]
    qcd = parts0["qcd"]
    dlnmN_dsigma = tot0

    s_central = get_s(sigma_piN, sigma_s, m_N)
    ds_s = np.sqrt(sigma_piN_err ** 2 + sigma_s_err ** 2) / m_N

    light_quark_part = s_central * weyl
    lambda3_part = (1 - s_central) * (cutoff + qcd)
    lambda3_from_coupling = (1 - s_central) * cutoff
    lambda3_from_thresholds = (1 - s_central) * qcd

    K_KIN = 1.5
    beta = dlnmN_dsigma / np.sqrt(K_KIN)
    alphaY = 2 * beta ** 2

    # Error propagation for s
    d_dlnmN_dsigma = abs(weyl - cutoff - qcd) * ds_s
    d_beta = d_dlnmN_dsigma / np.sqrt(K_KIN)
    d_alphaY = 4 * abs(beta) * d_beta

    print(f"RESULT: weyl={weyl:.4f}±0")
    print(f"RESULT: lambda3_part={lambda3_part:.4f}±{abs((cutoff + qcd) * ds_s):.4f}")
    print(f"RESULT: lambda3_from_coupling={lambda3_from_coupling:.4f}±{abs(cutoff * ds_s):.4f}")
    print(f"RESULT: lambda3_from_thresholds={lambda3_from_thresholds:.4f}±{abs(qcd * ds_s):.4f}")
    print(f"RESULT: light_quark_part={light_quark_part:.4f}±{abs(weyl * ds_s):.4f}")
    print(f"RESULT: dlnmN_dsigma_10TeV={dlnmN_dsigma:.4f}±{d_dlnmN_dsigma:.4f}")
    print(f"RESULT: beta_10TeV={beta:.4f}±{d_beta:.4f}")
    print(f"RESULT: alphaY_10TeV={alphaY:.1f}±{d_alphaY:.1f}")

    return {
        "alphaY_10TeV": alphaY,
        "d_alphaY_10TeV": d_alphaY,
        "beta_10TeV": beta,
        "dlnmN_dsigma_10TeV": dlnmN_dsigma,
        "lambda3_part": lambda3_part,
        "lambda3_from_coupling": lambda3_from_coupling,
        "lambda3_from_thresholds": lambda3_from_thresholds,
        "light_quark_part": light_quark_part,
        "weyl": weyl,
    }

def alphaY_at_inv_lz(inv_lz):
    from tests.predictions import dlnm_dsigma
    K_KIN = 1.5
    tot, _ = dlnm_dsigma(inv_lz)
    beta = tot / np.sqrt(K_KIN)
    alphaY = 2 * beta ** 2
    return alphaY

def print_alphaY_all(inv_lz_eV):
    for val, name in zip(inv_lz_eV[1:], ["14TeV", "29TeV"]):
        aY = alphaY_at_inv_lz(val)
        print(f"RESULT: alphaY_{name}={aY:.1f}±0")

def print_alphaY_k(inv_lz_eV, k_var):
    for k in k_var:
        aY = alphaY_at_inv_lz(inv_lz_eV[0] * k)
        print(f"RESULT: alphaY_10TeV_k{k}={aY:.1f}±0")

def print_alphaY_1loop():
    aY = alpha_yukawa(10e12)
    print(f"RESULT: alphaY_1loop_10TeV={aY:.1f}±0")

def window_edges():
    from scipy.optimize import brentq
    def f(inv_lz):
        return np.log(alphaY_at_inv_lz(inv_lz)) - np.log(alpha_bound(range_um(inv_lz)))
    inv_min = brentq(f, 5e12, 29e12)
    lambda_max = range_um(inv_min)
    lambda_min = range_um(29e12)
    aY_low = alphaY_at_inv_lz(inv_min)
    aY_high = alphaY_at_inv_lz(29e12)
    print(f"RESULT: invlz_min_TeV={inv_min/1e12:.2f}±0")
    print(f"RESULT: lambda_max_um={lambda_max:.2f}±0")
    print(f"RESULT: alphaY_window_low={aY_low:.1f}±0")
    print(f"RESULT: alphaY_window_high={aY_high:.1f}±0")

if __name__ == "__main__":
    print_alphaY_1loop()
    compute_all(inv_lz_eV, 1.0, sigma_piN, sigma_piN_err, sigma_s, sigma_s_err)
    print_alphaY_all(inv_lz_eV)
    print_alphaY_k(inv_lz_eV, k_var)
    window_edges()