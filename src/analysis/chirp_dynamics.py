import numpy as np
from scipy.signal import stft

def calculate_chirp_mass_trajectory(data, fs=4096):
    """
    Computes the instantaneous frequency and effective chirp mass.
    Returns: time_array, chirp_mass_trajectory
    """
    # 1. Short-Time Fourier Transform to track frequency over time
    f, t, Zxx = stft(data.value, fs=fs, nperseg=256)
    
    # 2. Extract instantaneous peak frequency
    freq_max = f[np.argmax(np.abs(Zxx), axis=0)]
    
    # 3. Calculate Chirp Mass derivative (dF/dt)
    # Using the GR relation: M_chirp = (c^3 / G) * (5/96 * pi^-8/3 * f^-11/3 * df/dt)^3/5
    # (Constants normalized for simplicity)
    dfdt = np.gradient(freq_max, t)
    
    # BMI-corrected Chirp Mass calculation
    # If the system is losing energy to the bulk, M_eff will appear to diverge
    m_chirp_eff = (dfdt / (freq_max**(11/3)))**(3/5)
    
    return t, m_chirp_eff
