"""
BMI LVK Strain Pipeline — GW190521 Analysis
Loads O3 public HDF5 strain files, analyzes the ~0.1s impulse chirp profile,
isolates the ringdown, and checks for the 15 Hz frequency split and K=0.13 coupling.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')  # non-interactive backend for codespace/server environments
import matplotlib.pyplot as plt
import h5py
from scipy.signal import stft, butter, sosfiltfilt
from pycbc.types import TimeSeries

# GW190521 merger GPS time (GWTC-2)
MERGER_GPS = 1242442967.4
# BMI baseline constants from GW250114 analysis
BMI_FREQ_SPLIT_HZ = 15.00
BMI_COUPLING_K    = 0.13

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'images')


def bandpass(ts, low_hz=50.0, high_hz=500.0):
    """Bandpass filter strain to isolate the GW signal band."""
    fs  = int(1.0 / ts.delta_t)
    sos = butter(8, [low_hz, high_hz], btype='bandpass', fs=fs, output='sos')
    filtered = sosfiltfilt(sos, ts.numpy())
    return TimeSeries(filtered, delta_t=ts.delta_t, epoch=ts.start_time)


def subtract_nr_template(ts):
    """
    Generate an IMRPhenomPv2 template for GW190521 (median GWTC-2 params),
    bandpass it, cross-correlation align it to the data, amplitude-scale it,
    subtract it, and return (residual_ts, template_array).
    IMRPhenomPv2 is used as the analytic NR proxy (NRSur7dq4 requires large
    surrogate data files not available in this environment).
    """
    from pycbc.waveform import get_td_waveform

    hp, _ = get_td_waveform(
        approximant='IMRPhenomPv2',
        mass1=85.4,
        mass2=65.6,
        spin1z=0.69,
        spin2z=0.0,
        delta_t=ts.delta_t,
        f_lower=20.0,
        distance=5300.0,   # Mpc — median GWTC-2 luminosity distance
        inclination=0.0,
    )

    # Bandpass template to same band as data
    hp_bp = bandpass(hp)
    tmpl  = hp_bp.numpy()
    strain = ts.numpy()

    # Pad or trim template to match data length
    if len(tmpl) < len(strain):
        tmpl = np.pad(tmpl, (len(strain) - len(tmpl), 0))
    else:
        tmpl = tmpl[-len(strain):]

    # Find best time alignment via cross-correlation
    corr = np.correlate(strain, tmpl, mode='full')
    lag  = int(np.argmax(np.abs(corr))) - (len(strain) - 1)
    if lag > 0:
        tmpl = np.concatenate([np.zeros(lag), tmpl[:-lag]])
    elif lag < 0:
        tmpl = np.concatenate([tmpl[-lag:], np.zeros(-lag)])

    # Amplitude-scale template to match data peak in ±0.05s merger window
    t_abs = np.array(ts.sample_times)
    t_rel = t_abs - MERGER_GPS
    peak_mask = (t_rel >= -0.05) & (t_rel <= 0.05)
    data_peak = np.max(np.abs(strain[peak_mask])) if peak_mask.any() else 1.0
    tmpl_peak = np.max(np.abs(tmpl[peak_mask]))    if peak_mask.any() else 1.0
    if tmpl_peak > 0:
        tmpl *= (data_peak / tmpl_peak)

    residual = strain - tmpl
    return TimeSeries(residual, delta_t=ts.delta_t, epoch=ts.start_time), tmpl


def load_hdf5_strain(path):
    """Load saved HDF5 strain file and return a PyCBC TimeSeries."""
    with h5py.File(path, 'r') as f:
        strain_arr  = f['strain'][:]
        sample_rate = float(f.attrs['sample_rate'])
        epoch       = float(f.attrs['epoch'])
    return TimeSeries(strain_arr, delta_t=1.0 / sample_rate, epoch=epoch)


def analyze_impulse_chirp(ts, det, out_dir):
    """
    GW190521 BMI chirp analysis: targets the ±0.15s window around merger
    to confirm the abrupt ~0.1s winding-mode-unpinning impulse.
    """
    fs = int(1.0 / ts.delta_t)
    strain = ts.numpy()
    t_abs  = np.array(ts.sample_times)
    t_rel  = t_abs - MERGER_GPS          # seconds relative to merger

    # STFT with short segments for time resolution on the fast impulse
    f, t_stft, Zxx = stft(strain, fs=fs, nperseg=128, noverlap=96)
    t_stft_rel = t_stft + (t_abs[0] - MERGER_GPS)

    freq_max = f[np.argmax(np.abs(Zxx), axis=0)]
    dfdt     = np.gradient(freq_max, t_stft)
    with np.errstate(divide='ignore', invalid='ignore'):
        m_eff = (dfdt / (freq_max ** (11.0 / 3.0))) ** (3.0 / 5.0)
    m_eff = np.nan_to_num(m_eff)

    # Focus on the ±0.15s impulse window
    mask = (t_stft_rel >= -0.15) & (t_stft_rel <= 0.15)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(t_stft_rel[mask], m_eff[mask], label=f'ECM ({det})', linewidth=2)
    ax.axvline(0.0,   color='red',    linestyle='--', label='Merger (t=0)')
    ax.axvline(-0.05, color='orange', linestyle=':',  label='Winding Onset (-0.05s)')
    ax.axvline( 0.05, color='green',  linestyle=':',  label='Winding Release (+0.05s)')
    ax.set_title(f'GW190521 BMI Impulse Chirp Profile: {det}')
    ax.set_xlabel('Time to Merger (s)')
    ax.set_ylabel('Effective Chirp Mass (ECM)')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.5)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f'GW190521_{det}_impulse_chirp.png')
    fig.savefig(path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f'  [{det}] Impulse chirp plot saved: {path}')

    # Report the impulse duration (above-median ECM region)
    med = np.nanmedian(np.abs(m_eff[mask]))
    above = t_stft_rel[mask][np.abs(m_eff[mask]) > med]
    if above.size >= 2:
        duration = above[-1] - above[0]
        print(f'  [{det}] Estimated impulse duration: {duration:.3f} s '
              f'(BMI prediction: ~0.10 s)')


def analyze_ringdown(ts, det, out_dir):
    """
    Isolate the 150 ms post-merger ringdown window, run FFT, and check
    for the 15 Hz sub-harmonic split and K=0.13 energy coupling.
    """
    from resonance_filter import run_fourier_analysis, scan_for_kk_modes

    fs      = int(1.0 / ts.delta_t)
    t_abs   = np.array(ts.sample_times)
    t_rel   = t_abs - MERGER_GPS

    # Ringdown window: +0.01s to +0.16s after merger (150 ms)
    mask = (t_rel >= 0.01) & (t_rel <= 0.16)
    if mask.sum() < 10:
        print(f'  [{det}] WARNING: insufficient ringdown samples — skipping.')
        return

    rd_strain = ts.numpy()[mask]
    rd_ts = TimeSeries(rd_strain, delta_t=ts.delta_t,
                       epoch=t_abs[mask][0])

    # FFT via resonance_filter
    freqs, power = run_fourier_analysis(rd_ts)

    # Scan for 15 Hz split (±15 Hz around 150 Hz ringdown region)
    peak_freq, snr = scan_for_kk_modes(freqs, power,
                                        expected_harmonic=150.0)
    print(f'  [{det}] Ringdown dominant tone: {peak_freq:.2f} Hz | '
          f'BMI resonance zone SNR: {snr:.2f}')

    # Check for 15 Hz sub-harmonic split
    split_region = (freqs >= peak_freq - BMI_FREQ_SPLIT_HZ - 5) & \
                   (freqs <= peak_freq - BMI_FREQ_SPLIT_HZ + 5)
    if np.any(split_region):
        split_power = np.max(power[split_region])
        peak_power  = power[np.argmin(np.abs(freqs - peak_freq))]
        split_ratio = split_power / peak_power if peak_power > 0 else 0.0
        print(f'  [{det}] 15 Hz split candidate at '
              f'{peak_freq - BMI_FREQ_SPLIT_HZ:.1f} Hz | '
              f'relative power: {split_ratio:.4f}')

    # K=0.13 coupling: compare energy in ringdown vs. total burst window
    total_mask = (t_rel >= -0.05) & (t_rel <= 0.16)
    e_total    = np.sum(ts.numpy()[total_mask] ** 2)
    e_ringdown = np.sum(rd_strain ** 2)
    k_measured = e_ringdown / e_total if e_total > 0 else 0.0
    print(f'  [{det}] Measured coupling K = {k_measured:.4f} '
          f'(BMI baseline K = {BMI_COUPLING_K})')

    # Plot ringdown spectrum
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.semilogy(freqs, power, linewidth=1.2, label='Ringdown PSD')
    ax.axvline(peak_freq, color='red', linestyle='--',
               label=f'Peak: {peak_freq:.1f} Hz')
    ax.axvline(peak_freq - BMI_FREQ_SPLIT_HZ, color='orange', linestyle=':',
               label=f'Δf=-{BMI_FREQ_SPLIT_HZ} Hz split')
    ax.set_title(f'GW190521 Ringdown Spectrum: {det}')
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Power')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_xlim(0, 500)
    path = os.path.join(out_dir, f'GW190521_{det}_ringdown_spectrum.png')
    fig.savefig(path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f'  [{det}] Ringdown spectrum saved: {path}')


def run(h5_dir='data'):
    """Run the full GW190521 BMI strain pipeline."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print('=== BMI LVK Pipeline: GW190521 ===')
    print(f'    Merger GPS: {MERGER_GPS}')
    print(f'    BMI Δf baseline: {BMI_FREQ_SPLIT_HZ} Hz | K: {BMI_COUPLING_K}\n')

    for det in ['H1', 'L1']:
        h5_path = os.path.join(h5_dir, f'GW190521_{det}_strain.h5')
        if not os.path.exists(h5_path):
            print(f'[{det}] HDF5 file not found: {h5_path}')
            continue

        print(f'--- {det} ---')
        ts = load_hdf5_strain(h5_path)
        print(f'  Loaded {len(ts)} samples @ {1.0/ts.delta_t:.0f} Hz, '
              f'epoch={float(ts.start_time):.1f}')

        ts = bandpass(ts)
        print(f'  Bandpass applied: 50–500 Hz')

        analyze_impulse_chirp(ts, det, OUTPUT_DIR)

        print(f'  Subtracting IMRPhenomPv2 NR template...')
        residual_ts, tmpl_arr = subtract_nr_template(ts)

        # Save data vs template vs residual comparison plot
        t_abs = np.array(ts.sample_times)
        t_rel = t_abs - MERGER_GPS
        win   = (t_rel >= -0.15) & (t_rel <= 0.30)
        fig, axes = plt.subplots(3, 1, figsize=(11, 9), sharex=True)
        axes[0].plot(t_rel[win], ts.numpy()[win],       color='steelblue',  lw=1.2, label='Bandpassed Data')
        axes[1].plot(t_rel[win], tmpl_arr[win],         color='darkorange',  lw=1.2, label='NR Template (IMRPhenomPv2)')
        axes[2].plot(t_rel[win], residual_ts.numpy()[win], color='crimson', lw=1.2, label='Residual (Data − Template)')
        for ax in axes:
            ax.axvline(0, color='k', linestyle='--', alpha=0.4)
            ax.legend(loc='upper right', fontsize=8)
            ax.grid(True, linestyle='--', alpha=0.4)
        axes[2].set_xlabel('Time to Merger (s)')
        axes[0].set_title(f'GW190521 {det}: Data / NR Template / Residual')
        fig.tight_layout()
        cmp_path = os.path.join(OUTPUT_DIR, f'GW190521_{det}_template_subtraction.png')
        fig.savefig(cmp_path, dpi=150, bbox_inches='tight')
        plt.close(fig)
        print(f'  [{det}] Template subtraction plot saved: {cmp_path}')

        analyze_ringdown(residual_ts, det, OUTPUT_DIR)
        print()

    print('Pipeline complete. Plots saved to:', os.path.abspath(OUTPUT_DIR))


if __name__ == '__main__':
    # Accept optional data directory argument
    data_dir = sys.argv[1] if len(sys.argv) > 1 else 'data'
    run(h5_dir=data_dir)
