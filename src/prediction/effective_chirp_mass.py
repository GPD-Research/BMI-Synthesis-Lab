```python
# src/prediction/effective_chirp_mass.py
import numpy as np

def effective_chirp_mass_time_series(start_time, end_time, step_size):
    """
    Generate a time series of effective chirp mass.

    Parameters:
    start_time (float): Start time of the time series.
    end_time (float): End time of the time series.
    step_size (float): Time step between consecutive points.

    Returns:
    np.ndarray: Time series of effective chirp mass values.
    """
    times = np.arange(start_time, end_time, step_size)
    chirp_masses = np.zeros_like(times)
    # Placeholder for the actual computation
    for i in range(len(times)):
        # Here you would implement the actual computation based on the BMI model
        chirp_masses[i] = times[i] * 100  # Example computation

    return times, chirp_masses

if __name__ == "__main__":
    start_time = 0
    end_time = 10
    step_size = 0.1
    times, chirp_masses = effective_chirp_mass_time_series(start_time, end_time, step_size)
    print(f"Times: {times}")
    print(f"Effective Chirp Masses: {chirp_masses}")
```