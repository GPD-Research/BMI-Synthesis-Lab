"""
BMI FAR Spectral Plots for Appendix J
======================================
Generates three publication-quality figures from the 100-trial FAR run:

  1. far_spectral_envelope_L1.png  — L1 ringdown spectrum of GW190521 overlaid
       on the null distribution (5th–95th percentile shaded band + median)
  2. far_split_distribution_L1.png — 15 Hz split power histogram (null vs event)
       with Gaussian fit and sigma annotation
  3. far_snr_vs_split_L1.png       — Scatter of BMI zone SNR vs split power for
       all null trials, with event marked

Run from repo root:
    python3 src/analysis/bmi_far_spectral_plots.py
"""

import os
import sys
import glob
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import h5py
from scipy.signal import butter, sosfiltfilt, welch
from scipy.signal.windows import hann
from scipy.stats import norm

# ── constants ─────────────────────────────────────────────────────────────────
MERGER_GPS     = 1242442967.4
SAMPLE_RATE    = 16384
BANDPASS_LOW   = 50.0
BANDPASS_HIGH  = 600.0
RD_WIN         = (0.001, 0.150)   # ringdown FFT window
BMI_SPLIT_HZ   = 15.0
REPO_ROOT      = os.path.join(os.path.dirname(__file__), '..', '..')
DATA_DIR       = os.path.join(REPO_ROOT, 'data')
FAR_DIR        = os.path.join(REPO_ROOT, 'assets', 'GW_Analysis', 'FAR_GW190521')
OUT_DIR        = FAR_DIR


# ── signal conditioning ────────────────────────────────────────────────────────

def load_and_condition(h5_path, ref_gps=None):
    """Load HDF5 strain, whiten, bandpass, return (strain_array, sample_times)."""
    with h5py.File(h5_path, 'r') as f:
        arr   = f['strain'][:]
        sr    = float(f.attrs['sample_rate'])
        epoch = float(f.attrs['epoch'])
    t_abs = epoch + np.arange(len(arr)) / sr

    # Welch PSD from off-source quarters
    n = len(arr)
    off = np.concatenate([arr[:n//4], arr[3*n//4:]])
    psd_f, psd_v = welch(off, fs=sr, nperseg=int(4.0 * sr))

    # Whiten
    fft   = np.fft.rfft(arr)
    f_rfft = np.fft.rfftfreq(n, d=1.0/sr)
    psd_i  = np.interp(f_rfft, psd_f, psd_v, left=psd_v[0], right=psd_v[-1])
    psd_i  = np.maximum(psd_i, 1e-60)
    white  = np.fft.irfft(fft / np.sqrt(psd_i), n=n)

    # Bandpass
    sos    = butter(8, [BANDPASS_LOW, BANDPASS_HIGH], btype='bandpass',
                    fs=sr, output='sos')
    bp     = sosfiltfilt(sos, white)

    return bp, t_abs, sr


def compute_ringdown_spectrum(strain, t_abs, sr, ref_gps):
    """Extract 150 ms post-GPS ringdown and return (freqs, power)."""
    t_rel = t_abs - ref_gps
    mask  = (t_rel >= RD_WIN[0]) & (t_rel <= RD_WIN[1])
    if mask.sum() < 16:
        return None, None
    rd  = strain[mask]
    win = hann(len(rd))
    fft_c = np.fft.rfft(rd * win)
    freqs  = np.fft.rfftfreq(len(rd), d=1.0/sr)
    power  = np.abs(fft_c) ** 2
    return freqs, power


# ── collect spectra ────────────────────────────────────────────────────────────

def collect_null_spectra():
    """Return list of (freqs, power) for all 100 trial L1 files."""
    files = sorted(glob.glob(
        os.path.join(DATA_DIR, 'FAR_GW190521_trial_*_L1_16384Hz_strain.h5')
    ))
    print(f'Found {len(files)} trial L1 files')
    spectra = []
    for fp in files:
        trial_num = os.path.basename(fp).split('_trial_')[1].split('_')[0]
        ref_gps_guess = MERGER_GPS  # noise trials: use data centre
        strain, t_abs, sr = load_and_condition(fp)
        ref_gps = float(t_abs[len(t_abs)//2])
        freqs, power = compute_ringdown_spectrum(strain, t_abs, sr, ref_gps)
        if freqs is not None:
            spectra.append((freqs, power))
    print(f'  Valid ringdown spectra: {len(spectra)}')
    return spectra


def get_event_spectrum():
    """Return (freqs, power) for the GW190521 L1 event."""
    fp = os.path.join(DATA_DIR, 'GW190521_L1_16384Hz_strain.h5')
    strain, t_abs, sr = load_and_condition(fp)
    return compute_ringdown_spectrum(strain, t_abs, sr, MERGER_GPS)


# ── load FAR summary stats ─────────────────────────────────────────────────────

def load_far_stats():
    report_path = os.path.join(FAR_DIR, 'far_report.json')
    with open(report_path) as f:
        report = json.load(f)
    null_splits, null_snrs = [], []
    for trial_dir in sorted(glob.glob(os.path.join(FAR_DIR, 'trial_*'))):
        sp = os.path.join(trial_dir, 'summary.json')
        if not os.path.exists(sp):
            continue
        with open(sp) as f:
            s = json.load(f)
        det = s.get('detectors', {}).get('L1', {})
        if 'error' not in det:
            if det.get('split_rel_power') is not None:
                null_splits.append(det['split_rel_power'])
            if det.get('bmi_zone_snr') is not None:
                null_snrs.append(det['bmi_zone_snr'])
    return np.array(null_splits), np.array(null_snrs), report


# ── Figure 1: Spectral envelope ────────────────────────────────────────────────

def plot_spectral_envelope(null_spectra, ev_freqs, ev_power):
    # Interpolate all null spectra onto a common frequency grid
    common_f = ev_freqs
    null_matrix = []
    for f, p in null_spectra:
        p_interp = np.interp(common_f, f, p, left=0, right=0)
        null_matrix.append(p_interp)
    null_matrix = np.array(null_matrix)

    p5   = np.percentile(null_matrix, 5,  axis=0)
    p25  = np.percentile(null_matrix, 25, axis=0)
    p50  = np.percentile(null_matrix, 50, axis=0)
    p75  = np.percentile(null_matrix, 75, axis=0)
    p95  = np.percentile(null_matrix, 95, axis=0)

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.fill_between(common_f, p5, p95, alpha=0.15, color='steelblue',
                    label='Null 5th–95th percentile')
    ax.fill_between(common_f, p25, p75, alpha=0.30, color='steelblue',
                    label='Null 25th–75th percentile')
    ax.semilogy(common_f, p50, color='steelblue', lw=1.5,
                linestyle='--', label='Null median')
    ax.semilogy(common_f, ev_power, color='crimson', lw=2.0,
                label='GW190521 L1 event', zorder=5)

    # Mark GW190521 event peak and 15 Hz split
    peak_idx  = int(np.argmax(ev_power))
    peak_freq = float(common_f[peak_idx])
    split_freq = peak_freq - BMI_SPLIT_HZ
    ax.axvline(peak_freq,   color='crimson', ls='--', alpha=0.7, lw=1.2,
               label=f'Event peak: {peak_freq:.0f} Hz')
    ax.axvline(split_freq,  color='orange',  ls=':',  alpha=0.9, lw=1.5,
               label=f'−{BMI_SPLIT_HZ:.0f} Hz split: {split_freq:.0f} Hz')
    ax.axvspan(135, 165, alpha=0.07, color='green', label='BMI 150 Hz zone')

    ax.set_xlim(50, 600)
    ax.set_xlabel('Frequency (Hz)', fontsize=12)
    ax.set_ylabel('Power (arbitrary units)', fontsize=12)
    ax.set_title('GW190521 L1 Ringdown Spectrum vs. 100-Trial Null Distribution\n'
                 '(whitened, bandpassed 50–600 Hz, 150 ms post-merger window)',
                 fontsize=11)
    ax.legend(fontsize=8, loc='upper right')
    ax.grid(True, ls='--', alpha=0.4)

    path = os.path.join(OUT_DIR, 'far_spectral_envelope_L1.png')
    fig.tight_layout()
    fig.savefig(path, dpi=180, bbox_inches='tight')
    plt.close(fig)
    print(f'Saved: {path}')


# ── Figure 2: Split power + SNR distributions ─────────────────────────────────

def plot_split_distribution(null_splits, null_snrs, report):
    ev_split = report['per_detector']['L1']['event_split_power']
    ev_snr   = report['per_detector']['L1']['event_bmi_snr']
    g_sig_s  = report['per_detector']['L1']['gaussian_sigma_split']
    g_sig_r  = report['per_detector']['L1']['gaussian_sigma_snr']
    e_sig    = report['per_detector']['L1']['empirical_sigma_split']

    fig = plt.figure(figsize=(14, 5))
    gs  = gridspec.GridSpec(1, 2, figure=fig, wspace=0.35)

    # ── panel A: split power ──
    ax1 = fig.add_subplot(gs[0])
    n, bins, _ = ax1.hist(null_splits, bins=25, color='steelblue', alpha=0.7,
                           edgecolor='white', lw=0.5, label='Null (100 trials)')
    mu, sd = np.mean(null_splits), np.std(null_splits)
    x = np.linspace(max(0, mu - 4*sd), mu + 5*sd, 300)
    ax1.plot(x, len(null_splits) * (bins[1]-bins[0]) * norm.pdf(x, mu, sd),
             'k--', lw=1.5, label=f'Gaussian fit\n$\\mu={mu:.3f}$, $\\sigma={sd:.3f}$')
    ax1.axvline(ev_split, color='crimson', lw=2.5,
                label=f'GW190521: {ev_split:.3f}\n'
                      f'Gaussian {g_sig_s:.2f}$\\sigma$\n'
                      f'Empirical {e_sig:.2f}$\\sigma$')
    ax1.set_xlabel('15 Hz Split Relative Power', fontsize=11)
    ax1.set_ylabel('Count', fontsize=11)
    ax1.set_title('L1: 15 Hz Split Power\nNull Distribution vs. GW190521', fontsize=10)
    ax1.legend(fontsize=8)
    ax1.grid(True, ls='--', alpha=0.4)
    ax1.annotate(f'{g_sig_s:.2f}σ', xy=(ev_split, 1), xytext=(ev_split+0.02, 4),
                 fontsize=12, color='crimson', fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color='crimson', lw=1.5))

    # ── panel B: BMI zone SNR ──
    ax2 = fig.add_subplot(gs[1])
    mu2, sd2 = np.mean(null_snrs), np.std(null_snrs)
    n2, bins2, _ = ax2.hist(null_snrs, bins=25, color='steelblue', alpha=0.7,
                              edgecolor='white', lw=0.5, label='Null (100 trials)')
    x2 = np.linspace(max(0, mu2 - 4*sd2), mu2 + 5*sd2, 300)
    ax2.plot(x2, len(null_snrs) * (bins2[1]-bins2[0]) * norm.pdf(x2, mu2, sd2),
             'k--', lw=1.5, label=f'Gaussian fit\n$\\mu={mu2:.2f}$, $\\sigma={sd2:.2f}$')
    ax2.axvline(ev_snr, color='crimson', lw=2.5,
                label=f'GW190521: {ev_snr:.2f}\n'
                      f'Gaussian {g_sig_r:.2f}$\\sigma$')
    ax2.set_xlabel('BMI 150 Hz Zone SNR', fontsize=11)
    ax2.set_ylabel('Count', fontsize=11)
    ax2.set_title('L1: BMI 150 Hz Zone SNR\nNull Distribution vs. GW190521', fontsize=10)
    ax2.legend(fontsize=8)
    ax2.grid(True, ls='--', alpha=0.4)
    ax2.annotate(f'{g_sig_r:.2f}σ', xy=(ev_snr, 1), xytext=(ev_snr+0.5, 4),
                 fontsize=12, color='crimson', fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color='crimson', lw=1.5))

    fig.suptitle('GW190521 BMI Signature — L1 FAR Null Distributions (N=100)',
                 fontsize=12, fontweight='bold')
    path = os.path.join(OUT_DIR, 'far_split_distribution_L1.png')
    fig.savefig(path, dpi=180, bbox_inches='tight')
    plt.close(fig)
    print(f'Saved: {path}')


# ── Figure 3: SNR vs split scatter ────────────────────────────────────────────

def plot_snr_vs_split(null_splits, null_snrs, report):
    ev_split = report['per_detector']['L1']['event_split_power']
    ev_snr   = report['per_detector']['L1']['event_bmi_snr']

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.scatter(null_splits, null_snrs, s=20, alpha=0.5, color='steelblue',
               label='Null trials (N=100)', zorder=2)
    ax.scatter([ev_split], [ev_snr], s=150, color='crimson', marker='*',
               zorder=5, label=f'GW190521 event\n({ev_split:.3f}, {ev_snr:.2f})')

    # Quadrant lines at null medians
    ax.axvline(np.median(null_splits), color='grey', ls=':', alpha=0.6, lw=1)
    ax.axhline(np.median(null_snrs),   color='grey', ls=':', alpha=0.6, lw=1)

    ax.set_xlabel('15 Hz Split Relative Power', fontsize=12)
    ax.set_ylabel('BMI 150 Hz Zone SNR', fontsize=12)
    ax.set_title('L1: BMI Zone SNR vs. 15 Hz Split Power\n'
                 'GW190521 Event vs. 100-Trial Null Distribution', fontsize=11)
    ax.legend(fontsize=9)
    ax.grid(True, ls='--', alpha=0.4)

    # Annotate event position
    ax.annotate('GW190521\n4.56σ', xy=(ev_split, ev_snr),
                xytext=(ev_split - 0.25, ev_snr + 3),
                fontsize=10, color='crimson', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='crimson', lw=1.5))

    path = os.path.join(OUT_DIR, 'far_snr_vs_split_L1.png')
    fig.tight_layout()
    fig.savefig(path, dpi=180, bbox_inches='tight')
    plt.close(fig)
    print(f'Saved: {path}')


# ── main ───────────────────────────────────────────────────────────────────────

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    print('=== BMI FAR Spectral Plots for Appendix J ===\n')

    print('Loading null spectra from 100 trial L1 files...')
    null_spectra = collect_null_spectra()

    print('\nLoading GW190521 event spectrum...')
    ev_freqs, ev_power = get_event_spectrum()

    print('\nLoading FAR summary statistics...')
    null_splits, null_snrs, report = load_far_stats()
    print(f'  Null trials with L1 split: {len(null_splits)}')

    print('\nGenerating Figure 1: Spectral envelope...')
    plot_spectral_envelope(null_spectra, ev_freqs, ev_power)

    print('Generating Figure 2: Split power + SNR distributions...')
    plot_split_distribution(null_splits, null_snrs, report)

    print('Generating Figure 3: SNR vs split scatter...')
    plot_snr_vs_split(null_splits, null_snrs, report)

    print('\nAll plots saved to:', os.path.abspath(OUT_DIR))


if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(__file__))
    main()
