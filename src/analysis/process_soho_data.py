import sys
import os
from sunpy.map import Map
import numpy as np
import matplotlib.pyplot as plt

# Add root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bmi_engine import BMIEngine

def process_fits_series(directory_path):
    """
    Ingests all FITS files in a directory (your JSOC export),
    applies the BMI Filter, and computes the spectral residual.
    """
    engine = BMIEngine()
    files = [f for f in os.listdir(directory_path) if f.endswith('.fits')]
    
    # We aggregate the time-series intensity/velocity from the central pixels
    # (avoiding the solar limb where atmospheric/instrumental noise is high)
    time_series = []
    
    print(f"Ingesting {len(files)} frames from JSOC...")
    
    for file in sorted(files):
        smap = Map(os.path.join(directory_path, file))
        # Extract the central 100x100 pixel patch (the "High-Resolution Zone")
        center_patch = smap.data[1500:1600, 1500:1600]
        time_series.append(np.mean(center_patch))
    
    # Apply the BMI filter (The 'womp' isolation)
    filtered_series = engine.apply_manifold_filter(np.array(time_series))
    
    return filtered_series

if __name__ == "__main__":
    # Point this to the folder where your JSOC export downloads
    data_dir = "../../data/hmi_perihelion_2026_01_03"
    
    if os.path.exists(data_dir):
        residual = process_fits_series(data_dir)
        print(f"Residual analysis complete. Peak Magnitude: {np.max(residual):.4e}")
    else:
        print(f"Waiting for JSOC export in {data_dir}...")
