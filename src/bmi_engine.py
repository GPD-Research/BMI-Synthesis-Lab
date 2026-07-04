import sys
import os

# Add src to path to ensure we can import our analysis modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from analysis.bridge_tensor_calibration import calculate_interface_tensor

class BMIEngine:
    def __init__(self, k_coeff=0.13, l_scale=1e-15):
        self.k_coeff = k_coeff
        self.l_scale = l_scale
        self.resonance_hz = 15.0
        self.bridge_magnitude = self._initialize_bridge_magnitude()

    def _initialize_bridge_magnitude(self):
        """Automatically import the magnitude from our calibration tool."""
        return calculate_interface_tensor(self.k_coeff, self.l_scale, self.resonance_hz)

    def apply_manifold_filter(self, spectral_data):
        """
        Applies the BMI filter to raw solar data.
        Spectral data is adjusted by the interaction magnitude constant.
        """
        # This will be the hook for filtering the SOHO/SDO HDF5 stream
        filtered_data = spectral_data / self.bridge_magnitude
        return filtered_data

    def status(self):
        return f"Engine Active. Bridge Magnitude: {self.bridge_magnitude:.4e}"

if __name__ == "__main__":
    engine = BMIEngine()
    print(engine.status())
