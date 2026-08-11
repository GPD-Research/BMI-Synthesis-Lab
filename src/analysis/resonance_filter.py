import numpy as np
import scipy.signal as signal

def run_fourier_analysis(ringdown_ts):
    """
    Takes the isolated ringdown TimeSeries array, applies a Hanning window 
    to prevent spectral leakage, and executes a Fast Fourier Transform.
    """
    print("🔮 Initializing Fourier Analysis on post-merger spacetime...")
    
    # Extract the raw numpy array values and sampling rate (PyCBC TimeSeries)
    sample_rate = int(1.0 / ringdown_ts.delta_t)
    strain_values = ringdown_ts.numpy()
    
    # 1. Apply a Hanning window to smoothly taper the edges of our 150ms slice
    window = signal.windows.hann(len(strain_values))
    windowed_strain = strain_values * window
    
    # 2. Compute the Fast Fourier Transform (FFT)
    fft_complex = np.fft.rfft(windowed_strain)
    fft_frequencies = np.fft.rfftfreq(len(windowed_strain), d=1.0/sample_rate)
    
    # Calculate power spectral density (magnitude squared)
    fft_power = np.abs(fft_complex) ** 2
    
    print(f"✅ Spectrum generated across {len(fft_frequencies)} discrete frequency bins.")
    return fft_frequencies, fft_power

def scan_for_kk_modes(frequencies, power, expected_harmonic=180.0):
    """
    Scans the power spectrum for anomalous spikes outside standard Kerr overtones.
    Your BMI engine predicts subtle resonance near specific harmonic boundaries.
    """
    print(f"🔍 Scanning spectrum for Kaluza-Klein interface echoes near {expected_harmonic} Hz...")
    
    # Find the peak frequency in our spectrum
    peak_idx = np.argmax(power)
    peak_freq = frequencies[peak_idx]
    
    print(f"📊 Dominant Ringdown Tone identified at: {peak_freq:.2f} Hz")
    
    # Isolate a region around our theoretical BMI resonance zone
    tolerance = 15.0  # Hz
    resonance_zone = (frequencies >= expected_harmonic - tolerance) & (frequencies <= expected_harmonic + tolerance)
    
    if np.any(resonance_zone):
        zone_power = power[resonance_zone]
        zone_max = np.max(zone_power)
        background_avg = np.mean(power)
        
        snr_ratio = zone_max / background_avg
        print(f"📡 BMI Resonance Zone Signal-to-Noise Ratio: {snr_ratio:.2f}")
        return peak_freq, snr_ratio
        
    return peak_freq, 0.0
