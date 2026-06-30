from src.data.constants import CMB_TEMPERATURE_K
from src.analysis.field_equations import calculate_baryonic_field

class BMIEngine:
    def __init__(self):
        self.manifold_state = "stable"
        print(f"BMI Engine Initialized. Base Temperature: {CMB_TEMPERATURE_K}K")

    def run_simulation(self, n):
        result = calculate_baryonic_field(n)
        return f"Harmonic N={n} | Result: {result:.6f}"

if __name__ == "__main__":
    engine = BMIEngine()
    # Test for harmonics 1, 5, and 10
    for i in [1, 5, 10]:
        print(engine.run_simulation(i))
