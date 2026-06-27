# Constants for the BMI framework
C = 299792458  # Speed of light (m/s)
H0 = 67.4      # Hubble constant (km/s/Mpc) [cite: 70]
OMEGA_M0 = 0.315 # Matter density parameter [cite: 70]
OMEGA_L0 = 0.685 # Dark energy/cosmological constant density [cite: 70]
RC = 1.0         # Default Critical curvature threshold (to be calibrated) [cite: 104]
"""
src/data/constants.py
Physical constants and cosmological parameters for BMI Synthesis calculations.
"""

# --- Fundamental Physical Constants ---
C = 299792458.0      # Speed of light [m/s]
G = 6.67430e-11      # Gravitational constant [m^3 kg^-1 s^-2]

# --- Cosmological Parameters (Baseline: Lambda-CDM) ---
# Hubble constant [km/s/Mpc]
H0 = 67.4            
# Matter density parameter [dimensionless]
OMEGA_M0 = 0.315     
# Dark energy density parameter [dimensionless]
OMEGA_L0 = 0.685     

# --- BMI Framework Specifics ---
# Critical curvature threshold [dimensionless]
RC = 1.0             
# Screening gate index (sharpness of transition) [dimensionless]
N_POWER = 2.0
