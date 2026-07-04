import sys
import numpy as np
import matplotlib.pyplot as plt
from fetch_gw250114 import fetch_validated_data
from scipy.signal import stft

def analyze_chirp_dynamics(data, det):
    """
    Focused BMI Analysis: Targets the -0.4s to 0.0s window 
    to map the pre-merger coupling decay.
    """
    # Using nperseg=256 for optimal resolution in the final seconds
    fs = 4096
    f, t, Zxx = stft(data.value, fs=fs, nperseg=256)
    
    freq_max = f[np.argmax(np.abs(Zxx), axis=0)]
    dfdt = np.gradient(freq_max, t)
    
    with np.errstate(divide='ignore', invalid='ignore'):
        m_eff = (dfdt / (freq_max**(11/3)))**(3/5)
    m_eff = np.nan_to_num(m_eff)
    
    # Target the [-0.4s, 0.0s] window for the pre-event phase
    mask = (t >= (t[-1] - 0.4)) & (t <= t[-1])
    
    plt.figure(figsize=(10, 5))
    plt.plot(t[mask] - t[-1], m_eff[mask], label=f'Effective Chirp Mass ({det})', linewidth=2)
    
    # Highlight the specific interaction zone you identified
    plt.axvline(-0.25, color='orange', linestyle=':', label='Onset of Coupling (-0.25s)')
    plt.axvline(-0.13, color='green', linestyle=':', label='Stabilization/Reduction (-0.13s)')
    
    plt.title(f'BMI Pre-Event Coupling Phase: {det}')
    plt.xlabel('Time to Merger (s)')
    plt.ylabel('Effective Chirp Mass (ECM)')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.show()

    # Calculate the slope of the "reduction"
    reduction_mask = (t >= (t[-1] - 0.25)) & (t <= (t[-1] - 0.13))
    slope = np.polyfit(t[reduction_mask], m_eff[reduction_mask], 1)[0]
    print(f'[{det}] Coupling Reduction Slope: {slope:.4f} ECM/s')

def run():
    print("--- Running High-Precision BMI Pre-Event Analysis ---")
    for det in ['H1', 'L1']:
        try:
            data = fetch_validated_data(det)
            analyze_chirp_dynamics(data, det)
        except Exception as e:
            print(f"Error processing {det}: {e}")

if __name__ == '__main__':
    run()
