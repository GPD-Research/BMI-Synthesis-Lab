import unittest
from src.bmi_engine import BMIEngine

class TestBMIEngine(unittest.TestCase):
    def setUp(self):
        self.engine = BMIEngine()

    def test_harmonic_calculations(self):
        # We define "known good" results to ensure the math doesn't drift
        # N=1 -> ~2.181561
        # N=5 -> ~-2.035418
        
        val_1 = float(self.engine.run_simulation(1).split('| Result: ')[1])
        val_5 = float(self.engine.run_simulation(5).split('| Result: ')[1])
        
        # Check if values are within a reasonable tolerance
        self.assertAlmostEqual(val_1, 2.181561, places=5)
        self.assertAlmostEqual(val_5, -2.035418, places=5)

if __name__ == "__main__":
    unittest.main()
