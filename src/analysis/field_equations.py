import sys
import os
import numpy as np

# Ensure we can import the constants
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data import constants

class FieldTensor:
    def __init__(self, position=None):
        # The position (t, x, y, z) is the "state" of our observer
        self._position = np.array(position) if position is not None else np.zeros(4)
        self.base_metric = np.eye(4)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = np.array(value)

    @property
    def excitation(self):
        """
        Calculates the excitation based on the current position state.
        By accessing .excitation, the math is triggered dynamically.
        """
        t, x, y, z = self._position
        # Example: Using a scalar field function dependent on spatial displacement
        r = np.sqrt(x**2 + y**2 + z**2)
        # Placeholder for your physical field excitation logic
        return 12.1265 * np.exp(-r)

    @property
    def tensor(self):
        """The total tensor, combining the metric and the dynamic excitation."""
        mat = self.base_metric.copy()
        mat[0, 0] += self.excitation
        return mat
        
