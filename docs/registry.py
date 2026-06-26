# BMI Theory Variable Registry
# Dimensions in units of Energy [E] (ħ=c=1)

REGISTRY = {
    "S": {"dim": 0, "desc": "Total action"},
    "M_Pl": {"dim": 1, "desc": "Planck Mass"},
    "phi_vev": {"dim": 1, "desc": "Higgs VEV"},
    "m_nu": {"dim": 1, "desc": "Neutrino Mass"},
    "V2": {"dim": -2, "desc": "Bridge Volume"},
    "R_bridge": {"dim": -1, "desc": "Compactification radius"},
    "dPhi_dx": {"dim": 2, "desc": "Scalar potential field gradient"},
    "T_shear": {"dim": 4, "desc": "Hyperspatial shear tensor"},
    "G_R": {"dim": 0, "desc": "Curvature-Gate Function"},
    "mu": {"dim": 0, "desc": "Coupling magnitude"}
}

def get_dim(symbol):
    return REGISTRY.get(symbol, {}).get("dim")
