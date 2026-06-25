import numpy as np

class BMIValidator:
    def __init__(self, R_c=1.0, n=2.0):
        """
        Initialize the BMI Validator with critical curvature and power index.
        R_c: Critical curvature threshold
        n: Power index for the screening gate
        """
        self.R_c = R_c
        self.n = n

    def g_eff(self, R):
        """
        The screening gate function: g_eff(R) = 1 / (1 + (R/R_c)^n)
        """
        return 1 / (1 + (R / self.R_c)**self.n)

    def verify_limits(self):
        # High curvature limit (R >> R_c) should approach 0
        high_R = 1e6 * self.R_c
        # Low curvature limit (R << R_c) should approach 1
        low_R = 1e-6 * self.R_c
        
        print(f"Testing g_eff(R) limits (R_c={self.R_c}, n={self.n}):")
        print(f"g_eff(High R): {self.g_eff(high_R):.2e} (Expected: ~0)")
        print(f"g_eff(Low R):  {self.g_eff(low_R):.2f} (Expected: ~1)")

if __name__ == "__main__":
    validator = BMIValidator(R_c=1.0, n=2.0)
    validator.verify_limits()
