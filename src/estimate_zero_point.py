import numpy as np

def calculate_time_to_zero(decay_rate, threshold=0.01):
    """
    Calculates the harmonic N where Dark Energy drops below the threshold.
    """
    # derived from: threshold = exp(-rate * n) -> n = -ln(threshold) / rate
    n = -np.log(threshold) / decay_rate
    return n

if __name__ == "__main__":
    rate = 0.2
    # Threshold 0.01 = 1% of initial strength
    limit = 0.01
    n_steps = calculate_time_to_zero(rate, limit)
    
    print(f"--- Research Prediction ---")
    print(f"Decay Rate: {rate}")
    print(f"At a threshold of {limit*100}% of initial strength:")
    print(f"The system reaches expansion-stop at N ≈ {n_steps:.2f}")
