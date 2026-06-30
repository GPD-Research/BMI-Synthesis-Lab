import numpy as np
from src.data.constants import RESONANCE_DAMPING_FACTOR, CMB_TEMPERATURE_K

def calculate_baryonic_field(n):
    """
    Calculates the field resonance for a given harmonic n.
    Theory: Field(n) = A * e^(-damping * n) * sin(n)
    """
    # Assuming A is normalized to CMB Temperature
    amplitude = CMB_TEMPERATURE_K
    decay = np.exp(-RESONANCE_DAMPING_FACTOR * n)
    oscillation = np.sin(n)
    
    return amplitude * decay * oscillation
    
