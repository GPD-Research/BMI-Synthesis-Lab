import sys
import os
import numpy as np

# Ensure we can import the constants
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data import constants

class FieldTensor:
    def __init__(self):
        self.c = constants.C
        self.g = constants.G
        self.rc = constants.RC
        self.n = constants.N_POWER
        
    def get_excitation_tensor(self, field_value):
        # We start with the identity matrix scaled by RC
        tensor = np.eye(4) * self.rc
        
        # Apply the field excitation logic
        # Using a much larger field_value for testing, or checking the math
        excitation_factor = (field_value ** self.n) / (self.c**2)
        
        # Apply the perturbation to the temporal component (H_00)
        tensor[0, 0] += excitation_factor
        
        return tensor

if __name__ == "__main__":
    ft = FieldTensor()
    test_tensor = ft.get_excitation_tensor(field_value=1.0e9) # Increased value for visible test
    print("Excitation Tensor (H_mu_nu) sample:")
    print(test_tensor)
    print(f"\nValue at H[0,0]: {test_tensor[0,0]}")
    print(f"Excitation Delta: {test_tensor[0,0] - ft.rc}")
