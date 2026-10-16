import scipy.constants as const
import numpy as np

G = const.G
hbar = const.hbar
c = const.c

l_p_calc = np.sqrt(G * hbar / (c**3))
planck_length_codata = const.physical_constants['Planck length'][0]

print(f"Calculated sqrt(G * hbar / c^3): {l_p_calc:.12e} m")
print(f"CODATA Planck length value:      {planck_length_codata:.12e} m")
print(f"Absolute Difference:             {abs(l_p_calc - planck_length_codata):.12e} m")
