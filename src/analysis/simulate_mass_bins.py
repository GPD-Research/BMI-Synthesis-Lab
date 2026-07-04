import numpy as np
import matplotlib.pyplot as plt
from pycbc.waveform import get_td_waveform
from scipy.signal import stft

def calculate_m_eff_for_waveform(mass, delta_t=1/4096):
    """Generates a GR waveform and calculates its effective Chirp Mass trajectory."""
    hp, _ = get_td_waveform(approximant="IMRPhenomD",
                            mass1=mass,
                            mass2=mass,
                            delta_t=delta_t,
                            f_lower=30.0)
    
    # Run the same STFT pipeline used in your LVK analysis
    fs = int(1/delta_t)
    f, t, Zxx = stft(hp.numpy(), fs=fs, nperseg=256)
    freq_max = f[np.argmax(np.abs(Zxx), axis=0)]
    dfdt = np.gradient(freq_max, t)
    
    with np.errstate(divide='ignore', invalid='ignore'):
        m_eff = (dfdt / (freq_max**(11/3)))**(3/5)
    
    return t - t[-1], np.nan_to_num(m_eff)

def run_simulations():
    masses = [20, 35, 50, 70] # Range of binary masses in M_sun
    plt.figure(figsize=(10, 6))
    
    print("--- Running GR Mass-Bin Baselines ---")
    for m in masses:
        t, m_eff = calculate_m_eff_for_waveform(m)
        
        # Only plot the final 0.5s pre-merger to match your BMI analysis
        mask = (t >= -0.5)
        plt.plot(t[mask], m_eff[mask], label=f'GR Baseline {m} M_sun', alpha=0.6)
        
        # Print stability index for these GR baselines
        runaway = np.std(m_eff[mask])
        print(f'Mass {m} M_sun Stability Index: {runaway:.6f}')
        
    plt.axhline(0, color='black', linestyle='--')
    plt.title('Control Surface: Standard GR Chirp Mass Stability')
    plt.xlabel('Time to Merger (s)')
    plt.ylabel('Effective Chirp Mass')
    plt.legend()
    plt.grid(True)
    plt.show()
    print("--- Simulation Complete ---")

if __name__ == '__main__':
    run_simulations()
