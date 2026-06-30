import numpy as np
from src.data.constants import RESONANCE_DAMPING_FACTOR, CMB_TEMPERATURE_K

def calculate_bridge_stress(n):
    """
    Calculates the field resonance for a given harmonic n.
    Theory: Field(n) = A * e^(-damping * n) * sin(n)
    """
    present_day_n = 41.4
    dynamic_amplitude = CMB_TEMPERATURE_K * (present_day_n / (1 + n))
    
    decay = np.exp(-RESONANCE_DAMPING_FACTOR * n)
    oscillation = np.sin(n)
    
    return dynamic_amplitude * decay * oscillation
