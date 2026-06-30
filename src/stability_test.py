import numpy as np
from src.analysis.field_equations import calculate_baryonic_field
from src.analysis.dark_energy_calc import calculate_dark_energy_influence

def run_sensitivity_sweep():
    # We will test a range of decay rates to see if the 'Stability' 
    # of the system is an invariant or just a lucky guess.
    
    # We define n at 13.8 Gyr based on our current log logic
    # n = 10 * log10(13.8 * 1000 + 1) approx 41.4
    n_now = 41.4
    
    print(f"{'Decay Rate':<15} | {'Total Field @ 13.8 Gyr':<25}")
    print("-" * 45)
    
    # Test rates from 0.1 to 0.5
    for rate in np.linspace(0.1, 0.5, 5):
        # We temporarily override the logic to test the sensitivity
        baryonic = calculate_baryonic_field(n_now)
        # Re-calculating DE with the test rate
        de = 1.0 * np.exp(-rate * n_now) 
        total = baryonic + de
        print(f"{rate:<15.2f} | {total:<25.4f}")

if __name__ == "__main__":
    run_sensitivity_sweep()
    
