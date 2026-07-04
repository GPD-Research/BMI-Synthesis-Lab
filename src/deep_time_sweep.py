import matplotlib.pyplot as plt
import sys
import os
import numpy as np

# Path fix: Ensure Python can see the root directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bmi_engine import BMIEngine

def analyze_convergence(field_values):
    """Calculates the convergence envelope (gamma)."""
    # Ensure field_values is an array of floats
    field_values = np.array(field_values, dtype=float)
    final_state = field_values[-1]
    residuals = np.abs(field_values - final_state)
    
    # Avoid log(0)
    residuals = np.where(residuals == 0, 1e-9, residuals)
    log_residuals = np.log(residuals)
    t = np.arange(len(field_values))
    
    if len(t) > 1:
        gamma, log_c = np.polyfit(t, log_residuals, 1)
        return -gamma, np.exp(log_c)
    return 0, 0

def deep_time_sweep(start_t, end_t, steps):
    engine = BMIEngine()
    time_points = np.linspace(start_t, end_t, steps)
    history = []
    
    print(f"--- Initiating Deep Time Sweep (t={start_t} to {end_t}) ---")
    
    for t in time_points:
        val = engine.run_simulation_by_time(t)
        history.append(val)
        
    history = np.array(history)
    gamma, C = analyze_convergence(history)
    
    print(f"Sweep Complete.")
    print(f"Observed Decay Constant (gamma): {gamma:.6f}")
    print(f"Stability Envelope (C): {C:.6f}")
    
    return history, gamma

import matplotlib.pyplot as plt

def plot_crystallization(history, start_t, end_t):
    print("Generating Crystallization Envelope (Microscope Mode)...")
    
    # 1. Calculate the Envelope
    window = 100 # Adjust window size for granularity
    # Create rolling max and min to see the "bounds" of the chaos
    # We use a sliding window to capture the peaks and valleys
    envelopes = []
    for i in range(len(history) - window):
        chunk = history[i : i + window]
        envelopes.append((np.max(chunk), np.min(chunk)))
    
    envelopes = np.array(envelopes)
    time_axis = np.linspace(start_t, end_t, len(envelopes)) * (0.001 if end_t >= 1000 else 1.0)
    
    # 2. Plotting the Envelope
    plt.figure(figsize=(12, 6))
    plt.fill_between(time_axis, envelopes[:, 0], envelopes[:, 1], color='blue', alpha=0.1, label="Oscillation Envelope")
    plt.plot(time_axis, envelopes[:, 0], color='blue', alpha=0.3, linewidth=0.5)
    plt.plot(time_axis, envelopes[:, 1], color='blue', alpha=0.3, linewidth=0.5)
    
    # 3. Add a trend line for the center
    plt.plot(time_axis, np.mean(envelopes, axis=1), color='darkred', linewidth=1.5, label="Mean Field State")
    
    plt.axvline(x=13.8 * (0.001 if end_t >= 1000 else 1.0), color='k', linestyle='--', label="Present Day")
    
    plt.title("The Crystallization Envelope: Narrowing of Chaos over Deep Time")
    plt.xlabel(f"Time ({'Tyr' if end_t >= 1000 else 'Gyr'})")
    plt.ylabel("Field Intensity Amplitude")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    output_path = os.path.join(os.getcwd(), "crystallization_envelope.png")
    plt.savefig(output_path)
    plt.close()
    print(f"Success! Envelope chart saved to: {output_path}")

def early_universe_sweep():
    """
    Sweeps the first 100 years of the universe with logarithmic precision.
    Focuses on the 30-second to 1-year mark.
    """
    # Create log-scale time points from 1e-16 (seconds) to 1 (year)
    # 1 year in Gyr = 1/1e9 = 1e-9
    time_points = np.logspace(-16, -9, 1000) 
    
    engine = BMIEngine()
    history = []
    
    print("--- Initiating Early Universe Sweep (T=0 to T=1 Year) ---")
    
    for t in time_points:
        val = engine.run_simulation_by_time(t)
        history.append(val)
        
    # Plotting this requires log-scale axes
    plt.figure(figsize=(10, 6))
    plt.semilogx(time_points, history, label="Early Field Activity")
    plt.title("The Big Bang Interaction: Field Dynamics at T < 1 Year")
    plt.xlabel("Time (Gyr - Log Scale)")
    plt.ylabel("Field Intensity")
    plt.grid(True, which="both", alpha=0.3)
    plt.savefig("early_universe.png")
    print("Chart saved as 'early_universe.png'")

if __name__ == "__main__":
    early_universe_sweep()

if __name__ == "__main__":
    # --- EXPERIMENT SELECTOR ---
    # Comment out the experiment you do NOT want to run.

    # EXPERIMENT A: Deep Time Stability (The 10,000 Year/Trillion Year Sweep)
    data, decay_rate = deep_time_sweep(start_t=0, end_t=10000, steps=10000)
    plot_crystallization(data, 0, 10000)
    
    # EXPERIMENT B: Early Universe Dynamics (Logarithmic Sweep: T < 1 Year)
    # Uncomment the line below to run the Big Bang analysis
    # early_universe_sweep()
