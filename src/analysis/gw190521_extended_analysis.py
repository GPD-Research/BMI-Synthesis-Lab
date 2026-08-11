"""
GW190521 Extended BMI Analysis
Fetches V1 + H1 + L1 at 16384 Hz, estimates noise PSD from off-source data,
whitens each detector, generates Q-scans, and re-runs the BMI impulse/split
measurements on properly conditioned data.

Corrected GWTC-2 parameters: m1=95.3, m2=69.0 Msun, d=3920 Mpc, SNR=14.38
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import h5py
from scipy.signal import butter, sosfiltfilt, welch
from pycbc.types import TimeSeries
from pycbc.catalog import Merger
from pycbc.waveform import get_td_waveform

MERGER_GPS     = 1242442967.4
SAMPLE_RATE_HI = 16384          # Hz — 4x finer time resolution
BMI_FREQ_SPLIT = 15.00          # Hz
BMI_K          = 0.13
DETECTORS      = ['H1', 'L1', 'V1']

# Corrected GWTC-2 median parameters
EVENT_M1   = 95.3
EVENT_M2   = 69.0
EVENT_DIST = 3920.0   # Mpc

OUT_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'images')
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data')


# ── Data fetching ─────────────────────────────────────────────────────────────

def fetch_and_save(det, sample_rate=SAMPLE_RATE_HI):
    """Fetch strain from GWOSC catalog and save to HDF5."""
    merger = Merger("GW190521")
    strain = merger.strain(det, sample_rate=sample_rate)
    if strain is None:
        raise ValueError(f"Null strain for {det}")
    path = os.path.join(DATA_DIR, f'GW190521_{det}_{sample_rate}Hz_strain.h5')
    with h5py.File(path, 'w') as f:
        f.create_dataset('strain', data=strain.numpy())
        f.create_dataset('time',   data=np.array(strain.sample_times))
        f.attrs['sample_rate'] = sample_rate
        f.attrs['epoch']       = float(strain.start_time)
    print(f'  [{det}] saved {len(strain)} samples @ {sample_rate} Hz → {path}')
    return strain


def load_hdf5(det, sample_rate=SAMPLE_RATE_HI):
    path = os.path.join(DATA_DIR, f'GW190521_{det}_{sample_rate}Hz_strain.h5')
    if not os.path.exists(path):
        return fetch_and_save(det, sample_rate)
    with h5py.File(path, 'r') as f:
        arr  = f['strain'][:]
        sr   = float(f.attrs['sample_rate'])
        epoch = float(f.attrs['epoch'])
    return TimeSeries(arr, delta_t=1.0/sr, epoch=epoch)


# ── Signal conditioning ───────────────────────────────────────────────────────

def estimate_psd(ts, seg_len_s=4.0):
    """Welch PSD estimate using off-source data (first and last quarters)."""
    fs   = int(1.0 / ts.delta_t)
    data = ts.numpy()
    n    = len(data)
    # Use off-source regions: first 8s and last 8s of the 32s window
    off  = np.concatenate([data[:n//4], data[3*n//4:]])
    freqs, psd = welch(off, fs=fs, nperseg=int(seg_len_s * fs))
    return freqs, psd


def whiten(ts, psd_freqs, psd):
    """Whiten strain by dividing FFT by sqrt(PSD), then IFFT."""
    fs   = int(1.0 / ts.delta_t)
    data = ts.numpy()
    fft  = np.fft.rfft(data)
    f    = np.fft.rfftfreq(len(data), d=1.0/fs)
    # Interpolate PSD onto FFT frequency grid
    psd_interp = np.interp(f, psd_freqs, psd, left=psd[0], right=psd[-1])
    psd_interp = np.maximum(psd_interp, 1e-60)   # guard divide-by-zero
    whitened = np.fft.irfft(fft / np.sqrt(psd_interp), n=len(data))
    return TimeSeries(whitened, delta_t=ts.delta_t, epoch=ts.start_time)


def bandpass(ts, low=50.0, high=600.0):
    fs  = int(1.0 / ts.delta_t)
    sos = butter(8, [low, high], btype='bandpass', fs=fs, output='sos')
    out = sosfiltfilt(sos, ts.numpy())
    return TimeSeries(out, delta_t=ts.delta_t, epoch=ts.start_time)


# ── Q-scan ────────────────────────────────────────────────────────────────────

def make_qscan(ts, det, out_dir):
    """Generate a Q-scan spectrogram centred on the merger using gwpy."""
    try:
        from gwpy.timeseries import TimeSeries as GWpyTS
        from astropy import units as u
        t_abs = np.array(ts.sample_times)
        gts = GWpyTS(
            ts.numpy(),
            t0=float(ts.start_time),
            dt=ts.delta_t,
            unit=u.dimensionless_unscaled,
            name=f'GW190521 {det} whitened strain'
        )
        # Q-scan centred on merger, ±2s window, 20-500 Hz
        gts_crop = gts.crop(MERGER_GPS - 2, MERGER_GPS + 2)
        qgram = gts_crop.q_transform(
            frange=(20, 500),
            qrange=(4, 64),
            outseg=(MERGER_GPS - 1, MERGER_GPS + 1),
        )
        fig = qgram.plot(figsize=(10, 4))
        ax  = fig.gca()
        ax.set_epoch(MERGER_GPS)
        ax.set_xlim(MERGER_GPS - 0.5, MERGER_GPS + 0.5)
        ax.set_ylim(20, 500)
        ax.set_yscale('log')
        ax.set_xlabel('Time (s) relative to merger')
        ax.set_ylabel('Frequency (Hz)')
        ax.set_title(f'GW190521 Q-scan: {det} (whitened, 50–600 Hz)')
        path = os.path.join(out_dir, f'GW190521_{det}_qscan.png')
        fig.savefig(path, dpi=150, bbox_inches='tight')
        plt.close(fig)
        print(f'  [{det}] Q-scan saved: {path}')
    except Exception as e:
        print(f'  [{det}] Q-scan failed: {e}')


# ── BMI impulse analysis ──────────────────────────────────────────────────────

def analyze_impulse(ts, det, out_dir):
    """Measure impulse duration on whitened 16384 Hz data."""
    from scipy.signal import stft as scipy_stft
    fs     = int(1.0 / ts.delta_t)
    t_abs  = np.array(ts.sample_times)
    t_rel  = t_abs - MERGER_GPS

    # Short STFT segments for sub-ms resolution
    f, t_s, Zxx = scipy_stft(ts.numpy(), fs=fs, nperseg=256, noverlap=224)
    t_s_rel = t_s + (t_abs[0] - MERGER_GPS)

    freq_max = f[np.argmax(np.abs(Zxx), axis=0)]
    dfdt = np.gradient(freq_max, t_s)
    with np.errstate(divide='ignore', invalid='ignore'):
        m_eff = (dfdt / (freq_max ** (11.0/3.0))) ** (3.0/5.0)
    m_eff = np.nan_to_num(m_eff)

    win  = (t_s_rel >= -0.15) & (t_s_rel <= 0.15)
    med  = np.nanmedian(np.abs(m_eff[win]))
    above = t_s_rel[win][np.abs(m_eff[win]) > med]
    duration = (above[-1] - above[0]) if above.size >= 2 else float('nan')

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t_s_rel[win], m_eff[win], lw=1.5, label=f'ECM ({det})')
    ax.axvline(0,     color='red',    ls='--', label='Merger')
    ax.axvline(-0.05, color='orange', ls=':',  label='Winding onset')
    ax.axvline( 0.05, color='green',  ls=':',  label='Winding release')
    ax.set_title(f'GW190521 Impulse Profile: {det} (whitened 16384 Hz)')
    ax.set_xlabel('Time to Merger (s)')
    ax.set_ylabel('ECM')
    ax.legend(fontsize=8)
    ax.grid(True, ls='--', alpha=0.5)
    path = os.path.join(out_dir, f'GW190521_{det}_impulse_16k.png')
    fig.savefig(path, dpi=150, bbox_inches='tight')
    plt.close(fig)

    print(f'  [{det}] Impulse duration: {duration:.4f} s '
          f'(BMI prediction ~0.10 s) | plot: {os.path.basename(path)}')
    return duration


# ── Corrected template subtraction ───────────────────────────────────────────

def subtract_template(ts, det, out_dir):
    """Generate IMRPhenomPv2 with corrected GWTC-2 params, align, subtract."""
    hp, _ = get_td_waveform(
        approximant='IMRPhenomPv2',
        mass1=EVENT_M1,
        mass2=EVENT_M2,
        spin1z=0.0,
        spin2z=0.0,
        delta_t=ts.delta_t,
        f_lower=20.0,
        distance=EVENT_DIST,
        inclination=0.0,
    )
    hp_bp = bandpass(hp)
    tmpl  = hp_bp.numpy()
    strain = ts.numpy()

    # Trim/pad to match data length
    if len(tmpl) < len(strain):
        tmpl = np.pad(tmpl, (len(strain) - len(tmpl), 0))
    else:
        tmpl = tmpl[-len(strain):]

    # Cross-correlation alignment
    corr = np.correlate(strain, tmpl, mode='full')
    lag  = int(np.argmax(np.abs(corr))) - (len(strain) - 1)
    if lag > 0:
        tmpl = np.concatenate([np.zeros(lag), tmpl[:-lag]])
    elif lag < 0:
        tmpl = np.concatenate([tmpl[-lag:], np.zeros(-lag)])

    # Amplitude-scale to peak
    t_abs = np.array(ts.sample_times)
    t_rel = t_abs - MERGER_GPS
    pm    = (t_rel >= -0.05) & (t_rel <= 0.05)
    dp    = np.max(np.abs(strain[pm])) if pm.any() else 1.0
    tp    = np.max(np.abs(tmpl[pm]))   if pm.any() else 1.0
    if tp > 0:
        tmpl *= dp / tp

    residual = strain - tmpl

    # Comparison plot
    win = (t_rel >= -0.20) & (t_rel <= 0.40)
    fig, axes = plt.subplots(3, 1, figsize=(11, 9), sharex=True)
    axes[0].plot(t_rel[win], strain[win],   color='steelblue',  lw=1.0, label='Whitened Data')
    axes[1].plot(t_rel[win], tmpl[win],     color='darkorange',  lw=1.0, label='Template (IMRPhenomPv2)')
    axes[2].plot(t_rel[win], residual[win], color='crimson',     lw=1.0, label='Residual')
    for ax in axes:
        ax.axvline(0, color='k', ls='--', alpha=0.4)
        ax.legend(loc='upper right', fontsize=8)
        ax.grid(True, ls='--', alpha=0.4)
    axes[2].set_xlabel('Time to Merger (s)')
    axes[0].set_title(f'GW190521 {det}: Whitened Data / NR Template / Residual (16384 Hz)')
    fig.tight_layout()
    path = os.path.join(out_dir, f'GW190521_{det}_template_sub_16k.png')
    fig.savefig(path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f'  [{det}] Template subtraction plot: {os.path.basename(path)}')

    return TimeSeries(residual, delta_t=ts.delta_t, epoch=ts.start_time), tmpl


# ── Ringdown / 15 Hz split ────────────────────────────────────────────────────

def analyze_ringdown(residual_ts, tmpl_arr, det, out_dir):
    """150ms FFT window for frequency split; 1-25ms window for K ratio."""
    from resonance_filter import run_fourier_analysis, scan_for_kk_modes

    t_abs = np.array(residual_ts.sample_times)
    t_rel = t_abs - MERGER_GPS

    # K: short window
    k_mask = (t_rel >= 0.001) & (t_rel <= 0.025)
    e_res  = np.sum(residual_ts.numpy()[k_mask] ** 2)
    e_tmpl = np.sum(tmpl_arr[k_mask] ** 2)
    if e_tmpl > 0:
        print(f'  [{det}] K = {e_res/e_tmpl:.6f}  (BMI baseline {BMI_K})')
    else:
        print(f'  [{det}] GR template ~0 by 1ms; residual energy [1-25ms] = {e_res:.4e}')

    # Frequency split: 150ms FFT window
    fft_mask  = (t_rel >= 0.001) & (t_rel <= 0.150)
    rd_strain = residual_ts.numpy()[fft_mask]
    rd_ts     = TimeSeries(rd_strain, delta_t=residual_ts.delta_t,
                           epoch=t_abs[fft_mask][0])

    freqs, power = run_fourier_analysis(rd_ts)
    peak_freq, snr = scan_for_kk_modes(freqs, power, expected_harmonic=150.0)
    print(f'  [{det}] Ringdown peak: {peak_freq:.2f} Hz | BMI zone SNR: {snr:.2f}')

    split_r = (freqs >= peak_freq - BMI_FREQ_SPLIT - 5) & \
              (freqs <= peak_freq - BMI_FREQ_SPLIT + 5)
    if np.any(split_r):
        sp   = np.max(power[split_r])
        pp   = power[np.argmin(np.abs(freqs - peak_freq))]
        ratio = sp / pp if pp > 0 else 0.0
        print(f'  [{det}] 15 Hz split at {peak_freq - BMI_FREQ_SPLIT:.1f} Hz | '
              f'rel. power: {ratio:.4f}')

    # Spectrum plot
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.semilogy(freqs, power, lw=1.2)
    ax.axvline(peak_freq,                    color='red',    ls='--',
               label=f'Peak {peak_freq:.0f} Hz')
    ax.axvline(peak_freq - BMI_FREQ_SPLIT,   color='orange', ls=':',
               label=f'−{BMI_FREQ_SPLIT} Hz split')
    ax.axvline(150, color='grey', ls=':', alpha=0.5, label='BMI 150 Hz zone')
    ax.set_xlim(0, 600)
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Power')
    ax.set_title(f'GW190521 {det} Residual Ringdown Spectrum (16384 Hz)')
    ax.legend(fontsize=8)
    ax.grid(True, ls='--', alpha=0.4)
    path = os.path.join(out_dir, f'GW190521_{det}_ringdown_16k.png')
    fig.savefig(path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f'  [{det}] Ringdown spectrum: {os.path.basename(path)}')


# ── Main ──────────────────────────────────────────────────────────────────────

def run():
    os.makedirs(OUT_DIR,  exist_ok=True)
    os.makedirs(DATA_DIR, exist_ok=True)

    print('=== GW190521 Extended BMI Analysis ===')
    print(f'    GPS: {MERGER_GPS} | m1={EVENT_M1} m2={EVENT_M2} Msun | '
          f'd={EVENT_DIST} Mpc | SNR=14.38')
    print(f'    Sample rate: {SAMPLE_RATE_HI} Hz | Detectors: {DETECTORS}\n')

    for det in DETECTORS:
        print(f'--- {det} ---')
        ts_raw = load_hdf5(det, SAMPLE_RATE_HI)
        print(f'  Raw: {len(ts_raw)} samples @ {SAMPLE_RATE_HI} Hz')

        # Noise PSD from off-source data, then whiten
        psd_f, psd_v = estimate_psd(ts_raw)
        ts_white = whiten(ts_raw, psd_f, psd_v)
        ts_bp    = bandpass(ts_white)
        print(f'  Whitened + bandpassed (50–600 Hz)')

        # Q-scan
        make_qscan(ts_bp, det, OUT_DIR)

        # Impulse chirp
        analyze_impulse(ts_bp, det, OUT_DIR)

        # Template subtraction + ringdown on residual
        residual_ts, tmpl_arr = subtract_template(ts_bp, det, OUT_DIR)
        analyze_ringdown(residual_ts, tmpl_arr, det, OUT_DIR)
        print()

    print('Extended analysis complete. Plots in:', os.path.abspath(OUT_DIR))


if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(__file__))
    run()
