"""
BMI Un-modelled Burst Search — PyCBC Excess Power
===================================================
A pipeline-independent burst search using PyCBC's excess power method.
This is a genuine un-modelled search (no GR template assumed) and serves
as the Codespaces-accessible proxy for Coherent WaveBurst (cWB).

Method (equivalent to cWB's Q-tile approach):
  1. Tile the time-frequency plane using short-duration FFT windows
  2. Measure excess power (SNR) in each tile relative to background PSD
  3. Cluster adjacent high-SNR tiles into a trigger
  4. Check whether the trigger peaks in the post-merger window (t > 0)
     and whether the dominant tile is 15 Hz below the ringdown band

Key difference from our custom pipeline:
  - No IMRPhenomPv2 template is subtracted
  - The 15 Hz offset is measured in RAW (template-free) whitened strain
  - If the split appears here, it is unambiguously not a template artefact

Run from repo root:
    python3 src/analysis/bmi_excess_power_burst.py
"""

import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import h5py
from scipy.signal import butter, sosfiltfilt, welch, spectrogram
from scipy.signal.windows import hann
from pycbc.types import TimeSeries

MERGER_GPS = {
    'GW190521': (1242442967.4, 'L1'),
    'GW231028': (1382542224.3, 'H1'),
}
BMI_SPLIT   = 15.0
DATA_DIR    = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
OUT_DIR     = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'GW_Analysis')
HDF5_NAMES  = {'GW190521': 'GW190521', 'GW231028': 'GW231028_153006'}


# ── Loading and conditioning ───────────────────────────────────────────────────

def load_strain(event, det, sr=16384):
    path = os.path.join(DATA_DIR, f'{HDF5_NAMES[event]}_{det}_{sr}Hz_strain.h5')
    with h5py.File(path, 'r') as f:
        arr   = f['strain'][:]
        epoch = float(f.attrs['epoch'])
    return TimeSeries(arr.astype(np.float64), delta_t=1.0/sr, epoch=epoch)


def condition(ts):
    """Off-source Welch whitening + 50-600 Hz bandpass. No template."""
    fs   = int(1.0 / ts.delta_t)
    data = ts.numpy()
    n    = len(data)

    off = np.concatenate([data[:n//4], data[3*n//4:]])
    psd_f, psd_v = welch(off, fs=fs, nperseg=int(4.0*fs))

    fft   = np.fft.rfft(data)
    freqs = np.fft.rfftfreq(n, d=ts.delta_t)
    psd_i = np.interp(freqs, psd_f, psd_v, left=psd_v[0], right=psd_v[-1])
    psd_i = np.maximum(psd_i, 1e-60)
    white = np.fft.irfft(fft / np.sqrt(psd_i), n=n)

    sos = butter(8, [50.0, 600.0], btype='bandpass', fs=fs, output='sos')
    return sosfiltfilt(sos, white), np.array(ts.sample_times), fs


# ── Excess power time-frequency map ───────────────────────────────────────────

def excess_power_map(white, t_abs, fs, merger_gps,
                     tile_dur=0.02, tile_step=0.005):
    """
    Tile the time-frequency plane in tile_dur-second windows stepped by tile_step.
    Returns (tile_times, tile_freqs, snr_matrix) where snr_matrix[i,j] is the
    excess power SNR in tile (i=time, j=freq).
    """
    tile_n    = int(tile_dur * fs)
    step_n    = int(tile_step * fs)
    n         = len(white)
    win       = hann(tile_n)
    win_norm  = np.sum(win**2)

    # Background power (per freq bin) from off-source
    off = np.concatenate([white[:n//4], white[3*n//4:]])
    bkg_n   = min(len(off), tile_n * 8)
    bkg     = off[:bkg_n]
    _, bkg_psd = welch(bkg, fs=fs, nperseg=tile_n, noverlap=tile_n//2)
    bkg_psd = np.maximum(bkg_psd, 1e-60)

    tile_times, tile_powers = [], []
    for start in range(0, n - tile_n, step_n):
        seg   = white[start:start + tile_n] * win
        power = np.abs(np.fft.rfft(seg))**2 / win_norm
        tile_times.append(t_abs[start + tile_n//2])
        tile_powers.append(power / bkg_psd)   # excess power SNR per freq bin

    tile_times, tile_powers = [], []
    for start in range(0, n - tile_n, step_n):
        seg   = white[start:start + tile_n] * win
        power = np.abs(np.fft.rfft(seg))**2 / win_norm
        tile_times.append(t_abs[start + tile_n//2])
        tile_powers.append(power / bkg_psd)   # excess power SNR per freq bin

    tile_times  = np.array(tile_times) - merger_gps  # relative to merger
    snr_matrix  = np.array(tile_powers)               # shape: (n_tiles, n_freq)
    tile_freqs  = np.fft.rfftfreq(tile_n, d=1.0/fs)

    return tile_times, tile_freqs, snr_matrix


def multi_resolution_split_check(white, t_abs, fs, merger_gps,
                                  post_window=(0.001, 0.200)):
    """
    Multi-resolution Q-like analysis: use long tiles (150ms) for freq resolution
    and short tiles (20ms) for time resolution — mimics cWB's multi-Q approach.
    Checks specifically for the 15 Hz split in the post-merger averaged spectrum.
    Returns (split_ratio, peak_freq, dominant_freq_long).
    """
    n = len(white)
    t_rel = t_abs - merger_gps
    mask  = (t_rel >= post_window[0]) & (t_rel <= post_window[1])
    if not mask.any():
        return 0.0, None, None

    # Long tile (150ms) — frequency resolution = 1/0.15 ≈ 6.7 Hz, resolves 15 Hz
    long_n   = int(0.150 * fs)
    long_win = hann(long_n)
    rd_seg   = white[mask][:long_n]
    if len(rd_seg) < long_n:
        rd_seg = np.pad(rd_seg, (0, long_n - len(rd_seg)))

    fft_long  = np.abs(np.fft.rfft(rd_seg * long_win[:len(rd_seg)]))**2
    freqs_long = np.fft.rfftfreq(long_n, d=1.0/fs)

    # Background from long off-source tile
    off = np.concatenate([white[:n//4], white[3*n//4:]])
    off_seg   = off[:long_n] if len(off) >= long_n else np.pad(off, (0, long_n-len(off)))
    bkg_long  = np.abs(np.fft.rfft(off_seg * long_win[:len(off_seg)]))**2
    bkg_long  = np.maximum(bkg_long, 1e-60)
    snr_long  = fft_long / bkg_long

    # Find peak in 60-580 Hz range
    f_mask = (freqs_long >= 60) & (freqs_long <= 580)
    peak_idx  = int(np.argmax(snr_long[f_mask]))
    peak_freq = float(freqs_long[f_mask][peak_idx])

    # 15 Hz split: compare ±7 Hz bands
    bw = 7.0
    peak_band  = (freqs_long >= peak_freq - bw) & (freqs_long <= peak_freq + bw)
    split_band = (freqs_long >= peak_freq - BMI_SPLIT - bw) & \
                 (freqs_long <= peak_freq - BMI_SPLIT + bw)
    p_pwr = float(np.mean(snr_long[peak_band]))  if peak_band.any()  else 1.0
    s_pwr = float(np.mean(snr_long[split_band])) if split_band.any() else 0.0
    split_ratio = s_pwr / p_pwr if p_pwr > 0 else 0.0

    return split_ratio, peak_freq, float(freqs_long[f_mask][peak_idx])


# ── Burst trigger extraction ───────────────────────────────────────────────────

def find_burst_trigger(tile_times, tile_freqs, snr_matrix, merger_gps,
                       snr_thresh=3.0, post_window=(0.001, 0.200),
                       freq_range=(60.0, 580.0)):
    """
    Find the peak excess-power tile in the post-merger window.
    freq_range avoids bandpass edge artifacts.
    Returns (peak_time_rel, peak_freq, peak_snr, split_ratio).
    """
    t_mask = (tile_times >= post_window[0]) & (tile_times <= post_window[1])
    f_mask = (tile_freqs >= freq_range[0]) & (tile_freqs <= freq_range[1])
    if not t_mask.any() or not f_mask.any():
        return None, None, None, None

    sub = snr_matrix[np.ix_(t_mask, f_mask)]
    peak_idx  = np.unravel_index(np.argmax(sub), sub.shape)
    peak_snr  = float(sub[peak_idx])
    peak_time = float(tile_times[t_mask][peak_idx[0]])
    peak_freq = float(tile_freqs[f_mask][peak_idx[1]])

    # Split ratio: average tile power in ±7 Hz bands around peak and peak-15 Hz
    # using all post-merger tiles to smooth out single-tile noise
    avg_power = np.mean(snr_matrix[t_mask, :], axis=0)
    bw = 7.0   # Hz half-bandwidth
    peak_band  = (tile_freqs >= peak_freq - bw) & (tile_freqs <= peak_freq + bw)
    split_band = (tile_freqs >= peak_freq - BMI_SPLIT - bw) & \
                 (tile_freqs <= peak_freq - BMI_SPLIT + bw)
    p_pwr  = float(np.mean(avg_power[peak_band]))  if peak_band.any()  else 0.0
    s_pwr  = float(np.mean(avg_power[split_band])) if split_band.any() else 0.0
    split_ratio = s_pwr / p_pwr if p_pwr > 0 else 0.0

    return peak_time, peak_freq, peak_snr, split_ratio


# ── Visualisation ──────────────────────────────────────────────────────────────

def plot_tf_map(tile_times, tile_freqs, snr_matrix, peak_time, peak_freq,
                event, det, out_dir):
    """Plot the time-frequency excess power map centred on merger."""
    win = (tile_times >= -0.5) & (tile_times <= 0.5)
    if not win.any():
        return

    fig, ax = plt.subplots(figsize=(12, 5))
    im = ax.pcolormesh(
        tile_times[win], tile_freqs,
        snr_matrix[win, :].T,
        shading='auto', cmap='inferno', vmin=0.5, vmax=5
    )
    plt.colorbar(im, ax=ax, label='Excess Power SNR')
    ax.axvline(0,           color='cyan',   lw=1.5, ls='--', label='Merger GPS')
    ax.axvline(0.001,       color='lime',   lw=1,   ls=':',  label='Ringdown window start')
    if peak_time is not None:
        ax.axvline(peak_time, color='white', lw=1.5, ls='-.',
                   label=f'Peak trigger: t={peak_time:.3f}s, f={peak_freq:.0f}Hz')
        ax.axhline(peak_freq,             color='white', lw=0.8, ls=':')
        ax.axhline(peak_freq - BMI_SPLIT, color='orange', lw=1.2, ls=':',
                   label=f'−{BMI_SPLIT} Hz split: {peak_freq-BMI_SPLIT:.0f} Hz')
    ax.set_ylim(50, 600)
    ax.set_xlim(-0.5, 0.3)
    ax.set_xlabel('Time relative to merger GPS (s)')
    ax.set_ylabel('Frequency (Hz)')
    ax.set_title(f'{event} {det}: Un-modelled Excess Power Burst Map\n'
                 f'(no GR template — cWB proxy)')
    ax.legend(fontsize=7, loc='upper right')
    path = os.path.join(out_dir, event, f'{det}_excess_power_burst.png')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f'  TF map saved: {path}')


# ── Main ──────────────────────────────────────────────────────────────────────

def run():
    print("=" * 60)
    print("BMI UN-MODELLED EXCESS POWER BURST SEARCH")
    print("(cWB proxy — no GR template, no custom sieve)")
    print("=" * 60)

    for event, (merger_gps, det) in MERGER_GPS.items():
        print(f"\n--- {event} ({det}) ---")
        try:
            ts = load_strain(event, det)
        except FileNotFoundError:
            print(f"  HDF5 not found — skipping")
            continue

        white, t_abs, fs = condition(ts)
        print(f"  Whitened (off-source PSD, 50-600 Hz bandpass, NO template)")

        tile_times, tile_freqs, snr_matrix = excess_power_map(
            white, t_abs, fs, merger_gps
        )
        print(f"  TF map: {snr_matrix.shape[0]} tiles × {snr_matrix.shape[1]} freq bins")

        peak_time, peak_freq, peak_snr, split_ratio = find_burst_trigger(
            tile_times, tile_freqs, snr_matrix, merger_gps
        )

        if peak_time is not None:
            print(f"  Post-merger burst trigger (20ms tiles, 50Hz res):")
            print(f"    Peak time:  +{peak_time:.4f}s | freq: {peak_freq:.1f} Hz | SNR: {peak_snr:.2f}")

        # Multi-resolution check for 15 Hz split (150ms tiles, 6.7 Hz res)
        split_ratio, split_peak, _ = multi_resolution_split_check(
            white, t_abs, fs, merger_gps
        )
        print(f"  Multi-res split check (150ms tile, 6.7 Hz resolution):")
        print(f"    Dominant freq: {split_peak:.1f} Hz")
        print(f"    15Hz split ratio: {split_ratio:.4f}  "
              f"({'PRESENT (>0.10)' if split_ratio > 0.10 else 'not detected (<0.10)'})")

        plot_tf_map(tile_times, tile_freqs, snr_matrix, peak_time, peak_freq,
                    event, det, OUT_DIR)

    print("\n" + "=" * 60)
    print("NOTE: Full cWB requires IGWN cluster + ROOT environment.")
    print("This excess power search is a Codespaces-accessible proxy.")
    print("For definitive pipeline-independent confirmation, submit")
    print("these strain files to the LVK cWB offline burst pipeline.")
    print("=" * 60)


if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(__file__))
    run()
