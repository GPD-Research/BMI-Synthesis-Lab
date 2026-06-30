from src.data.constants import CMB_TEMPERATURE_K
from src.analysis.bridge_stress import calculate_bridge_stress
from src.analysis.interbrane_potential import calculate_interbrane_potential
import numpy as np

class BMIEngine:
    def __init__(self):
        # We define 13.8 Billion Years as our 'Present Day' baseline
        self.AGE_OF_UNIVERSE_GYR = 13.8
        print(f"BMI Engine Initialized. Temporal Anchor: {self.AGE_OF_UNIVERSE_GYR} Gyr")

    def run_simulation_by_time(self, t_gyr):
        """
        Maps Time (t) to Harmonic (N) using a Logarithmic anchor.
        t_gyr: Time in billions of years.
        """
        # Mapping: N = 10 * log10(t_gyr * 1000 + 1)
        n = 10 * np.log10((t_gyr * 1000) + 1)
        
        bridge = calculate_bridge_stress(n)
        gap_tension = calculate_interbrane_potential(n) # (Dark Energy)
        
        total_field = baryonic + dark_energy
        
        return f"Time: {t_gyr:.2f} Gyr | N={n:.2f} | Baryonic: {baryonic:.4f} | DE: {dark_energy:.4f} | Total: {total_field:.4f}"

if __name__ == "__main__":
    engine = BMIEngine()
    # Testing the model across history, present, and deep future
    epochs = [0.0004, 1.0, 5.0, 13.8, 50.0, 100.0] 
    for t in epochs:
        print(engine.run_simulation_by_time(t))
