import scipy.constants as const
import numpy as np

G = const.G
hbar = const.hbar
c = const.c
planck_length_codata = const.Planck_length

l_p_calc = np.sqrt(G * hbar / (c**3))

print(f"Calculated sqrt(G * hbar / c^3): {l_p_calc:.6e} m")
print(f"CODATA Planck length value:      {planck_length_codata:.6e} m")
print(f"Difference: {l_p_calc - planck_length_codata:.6e} m")
