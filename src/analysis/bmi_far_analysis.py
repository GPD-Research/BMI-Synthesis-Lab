"""
BMI False-Alarm Rate (FAR) Analysis
====================================
Scans quiet-time off-source blocks near a target event, runs each through
the identical BMI analysis pipeline, builds a null distribution, and reports
the sigma significance of the event's 15 Hz split signature.

Usage
-----
  # 10 off-source trials for GW190521, using L1+V1 as key detectors:
  python3 bmi_far_analysis.py --event GW190521 --n-trials 10 --detectors L1 V1

  # Faster scan with 5 trials and H1+L1:
  python3 bmi_far_analysis.py --event GW190521 --n-trials 5 --detectors H1 L1

Output
------
  assets/GW_Analysis/FAR_GW190521/
      trial_<label>/         — per-trial plots and summary.json
      far_distribution.png   — null distribution with event overlay
      far_report.json        — sigma, p-value, per-detector statistics
"""

import argparse
import json
import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import norm

# Ensure bmi_gw_analyzer is importable
sys.path.insert(0, os.path.dirname(__file__))
import bmi_gw_analyzer as bmi

REPO_ROOT = os.path.join(os.path.dirname(__file__), '..', '..')
OUT_ROOT  = os.path.join(REPO_ROOT, 'assets', 'GW_Analysis')


# ── Segment discovery ──────────────────────────────────────────────────────────

def find_quiet_segments(event_gps: float, detectors: list,
                        sample_rate: int, n_trials: int,
                        max_search_days: int = 60) -> list:
    """
    Scan for quiet GPS targets where the requested detectors have GWOSC data.
    Uses 512s steps so multiple targets map to the same 4096s GWOSC file
    (avoiding redundant downloads) while staying statistically independent
    (windows are 32s, so 512s spacing gives zero overlap).
    Prefers targets where ALL detectors are available; falls back to any
    target where AT LEAST 2 of the requested detectors are available.
    Skips the ±2-hour window around the event itself.
    """
    from gwosc.locate import get_urls

    step      = 512          # 512s ≈ 8.5 min — packs ~7 trials per 4096s file
    max_off   = max_search_days * 86400
    skip_zone = 7200         # ±2 h around event

    # Generate offsets, nearest-first, skipping the ±2h zone
    offsets = sorted(
        [s for s in range(-max_off, max_off + 1, step)
         if abs(s) > skip_zone],
        key=abs
    )

    candidates = []   # (gps, det_list)
    seen_gps   = set()

    for offset in offsets:
        if len(candidates) >= n_trials:
            break
        t = int(event_gps + offset)
        if t in seen_gps:
            continue

        avail = []
        for det in detectors:
            try:
                urls = get_urls(det, t - 16, t + 16, sample_rate=sample_rate)
                if urls:
                    avail.append(det)
            except Exception:
                pass

        # Accept if all detectors available (preferred) or at least 2
        if len(avail) == len(detectors):
            candidates.append((t, avail))
            seen_gps.add(t)
            print(f'  [3-det] GPS {t} ({offset/86400:+.2f}d): {avail}')
        elif len(avail) >= 2:
            candidates.append((t, avail))
            seen_gps.add(t)
            print(f'  [2-det] GPS {t} ({offset/86400:+.2f}d): {avail}')

    return candidates[:n_trials]


# ── Run pipeline on a single trial ────────────────────────────────────────────

def run_trial(event_label: str, trial_gps: int, trial_label: str,
              detectors: list, sample_rate: int,
              bandpass_low: float, bandpass_high: float,
              ringdown_k_window: tuple, ringdown_fft_window: tuple) -> dict:
    """Build a noise EventConfig for this trial and run the BMI pipeline."""
    cfg = bmi.EventConfig(
        label=trial_label,
        merger_gps=float(trial_gps),
        duration=32.0,
        sample_rate=sample_rate,
        is_noise_segment=True,
        detectors=detectors,
        bandpass_low=bandpass_low,
        bandpass_high=bandpass_high,
        ringdown_k_window=ringdown_k_window,
        ringdown_fft_window=ringdown_fft_window,
    )
    results = bmi.run(cfg)
    return results


# ── Statistics ────────────────────────────────────────────────────────────────

def compute_far_stats(event_summary: dict, trial_summaries: list,
                      detectors: list) -> dict:
    """
    For each detector, collect the null distribution of:
      - bmi_zone_snr
      - split_rel_power
    Then compute empirical p-value and Gaussian sigma for the event values.
    """
    report = {'per_detector': {}}

    for det in detectors:
        # Event values
        ev_det   = event_summary.get('detectors', {}).get(det, {})
        ev_snr   = ev_det.get('bmi_zone_snr')
        ev_split = ev_det.get('split_rel_power')

        # Null distributions
        null_snr   = []
        null_split = []
        for ts in trial_summaries:
            td = ts.get('detectors', {}).get(det, {})
            if 'error' not in td:
                if td.get('bmi_zone_snr') is not None:
                    null_snr.append(td['bmi_zone_snr'])
                if td.get('split_rel_power') is not None:
                    null_split.append(td['split_rel_power'])

        def _sigma(val, null):
            if val is None or len(null) < 2:
                return None, None
            arr  = np.array(null, dtype=float)
            mu, sigma = float(np.mean(arr)), float(np.std(arr))
            if sigma == 0:
                return None, None
            z = (val - mu) / sigma
            # Empirical p-value: fraction of null >= event value
            p_emp = float(np.mean(arr >= val))
            p_emp = max(p_emp, 0.5 / len(arr))   # floor at 0.5/N
            sigma_emp = float(norm.isf(p_emp))
            return z, sigma_emp

        z_snr,   sig_snr   = _sigma(ev_snr,   null_snr)
        z_split, sig_split = _sigma(ev_split, null_split)

        report['per_detector'][det] = {
            'event_bmi_snr':       ev_snr,
            'event_split_power':   ev_split,
            'null_snr_mean':       float(np.mean(null_snr))   if null_snr   else None,
            'null_snr_std':        float(np.std(null_snr))    if null_snr   else None,
            'null_split_mean':     float(np.mean(null_split)) if null_split else None,
            'null_split_std':      float(np.std(null_split))  if null_split else None,
            'n_trials':            len(null_snr),
            'gaussian_sigma_snr':  z_snr,
            'gaussian_sigma_split': z_split,
            'empirical_sigma_snr':  sig_snr,
            'empirical_sigma_split': sig_split,
        }

        if sig_split is not None:
            print(f'  [{det}] split power: event={ev_split:.4f} | '
                  f'null={np.mean(null_split):.4f}±{np.std(null_split):.4f} | '
                  f'Gaussian σ={z_split:.2f} | empirical σ={sig_split:.2f}')
        if sig_snr is not None:
            print(f'  [{det}] BMI SNR:     event={ev_snr:.2f} | '
                  f'null={np.mean(null_snr):.2f}±{np.std(null_snr):.2f} | '
                  f'Gaussian σ={z_snr:.2f} | empirical σ={sig_snr:.2f}')

    return report


# ── Plots ─────────────────────────────────────────────────────────────────────

def plot_far_distributions(event_summary: dict, trial_summaries: list,
                           detectors: list, event_label: str,
                           out_dir: str):
    """Plot null distributions with event value marked for each detector."""
    metrics = [('split_rel_power', '15 Hz Split Relative Power'),
               ('bmi_zone_snr',    'BMI 150 Hz Zone SNR')]

    n_det = len(detectors)
    fig, axes = plt.subplots(n_det, 2, figsize=(12, 4 * n_det), squeeze=False)

    for row, det in enumerate(detectors):
        for col, (metric, metric_label) in enumerate(metrics):
            ax = axes[row][col]

            null_vals = []
            for ts in trial_summaries:
                td = ts.get('detectors', {}).get(det, {})
                v  = td.get(metric)
                if v is not None and 'error' not in td:
                    null_vals.append(v)

            ev_det = event_summary.get('detectors', {}).get(det, {})
            ev_val = ev_det.get(metric)

            if null_vals:
                ax.hist(null_vals, bins='auto', color='steelblue',
                        alpha=0.7, label=f'Null ({len(null_vals)} trials)')
                mu, sd = np.mean(null_vals), np.std(null_vals)
                x = np.linspace(min(null_vals) - sd, max(null_vals) + 2*sd, 200)
                ax.plot(x, len(null_vals) * (x[1]-x[0]) *
                        norm.pdf(x, mu, sd), 'k--', lw=1.2,
                        label='Gaussian fit')

            if ev_val is not None:
                ax.axvline(ev_val, color='crimson', lw=2,
                           label=f'{event_label}: {ev_val:.4f}')

            ax.set_title(f'{det} — {metric_label}')
            ax.set_xlabel(metric_label)
            ax.set_ylabel('Count')
            ax.legend(fontsize=7)
            ax.grid(True, ls='--', alpha=0.4)

    fig.suptitle(f'BMI FAR Distribution: {event_label}', fontsize=13,
                 fontweight='bold')
    fig.tight_layout()
    path = os.path.join(out_dir, 'far_distribution.png')
    fig.savefig(path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f'\nFAR distribution plot: {path}')
    return path


# ── Main ──────────────────────────────────────────────────────────────────────

def run_far(event_name: str, detectors: list, n_trials: int,
            sample_rate: int):

    far_dir = os.path.join(OUT_ROOT, f'FAR_{event_name}')
    os.makedirs(far_dir, exist_ok=True)

    print(f'\n{"="*60}')
    print(f'BMI FAR Analysis: {event_name}')
    print(f'  Detectors: {detectors} | Trials: {n_trials} | SR: {sample_rate} Hz')
    print(f'{"="*60}\n')

    # ── 1. Load event config to get analysis windows and GPS ──
    _sr = sample_rate  # capture for closure
    class _FakeArgs:
        event        = event_name
        gps          = None
        sample_rate  = _sr
        detectors    = None
        duration     = 32.0
        label        = None
    event_cfg = bmi.resolve_event(_FakeArgs())
    # Override detectors to the requested set
    event_cfg.detectors = detectors
    event_gps = event_cfg.merger_gps

    # ── 2. Load event summary (run pipeline if not already done) ──
    event_summary_path = os.path.join(OUT_ROOT, event_name, 'summary.json')
    if os.path.exists(event_summary_path):
        with open(event_summary_path) as f:
            event_summary = json.load(f)
        print(f'Loaded existing event summary: {event_summary_path}')
    else:
        print(f'Running event pipeline for {event_name} first...')
        event_summary = bmi.run(event_cfg)

    # ── 3. Find quiet-time segments ──
    print(f'\nScanning for {n_trials} quiet segments...')
    quiet_gps_list = find_quiet_segments(
        event_gps, detectors, event_cfg.sample_rate, n_trials
    )
    if not quiet_gps_list:
        print('ERROR: No valid quiet segments found.')
        return

    print(f'\nFound {len(quiet_gps_list)} segments. Running trials...\n')
    n_3det = sum(1 for _, d in quiet_gps_list if len(d) == 3)
    n_2det = sum(1 for _, d in quiet_gps_list if len(d) == 2)
    print(f'  3-detector: {n_3det}  |  2-detector: {n_2det}\n')

    # ── 4. Run each trial ──
    trial_summaries = []
    for i, (t_gps, trial_dets) in enumerate(quiet_gps_list):
        label = f'FAR_{event_name}_trial_{i+1:02d}'
        trial_out = os.path.join(far_dir, f'trial_{i+1:02d}')
        os.makedirs(trial_out, exist_ok=True)

        summary_path = os.path.join(trial_out, 'summary.json')
        if os.path.exists(summary_path):
            with open(summary_path) as f:
                summary = json.load(f)
            print(f'Trial {i+1:02d} (GPS {t_gps}): loaded from cache')
        else:
            print(f'\n--- Trial {i+1:02d} / {len(quiet_gps_list)} '
                  f'(GPS {t_gps}, {trial_dets}) ---')
            try:
                # Temporarily redirect bmi output dir to our trial subdir
                orig_out = bmi.OUT_ROOT
                bmi.OUT_ROOT = far_dir
                summary = run_trial(
                    event_label=event_name,
                    trial_gps=t_gps,
                    trial_label=label,
                    detectors=trial_dets,
                    sample_rate=event_cfg.sample_rate,
                    bandpass_low=event_cfg.bandpass_low,
                    bandpass_high=event_cfg.bandpass_high,
                    ringdown_k_window=event_cfg.ringdown_k_window,
                    ringdown_fft_window=event_cfg.ringdown_fft_window,
                )
                bmi.OUT_ROOT = orig_out
                # Save to trial subdir
                with open(summary_path, 'w') as f:
                    json.dump(summary, f, indent=2, default=str)
            except Exception as e:
                print(f'  Trial {i+1:02d} failed: {e}')
                bmi.OUT_ROOT = orig_out
                summary = {'error': str(e), 'detectors': {}}

        trial_summaries.append(summary)

    # ── 5. Compute FAR statistics ──
    print(f'\n{"="*60}')
    print(f'FAR Statistics: {event_name}')
    print(f'{"="*60}')
    far_report = compute_far_stats(event_summary, trial_summaries, detectors)
    far_report['event']       = event_name
    far_report['n_trials']    = len(trial_summaries)
    far_report['trial_gps']   = [t for t, _ in quiet_gps_list]
    far_report['n_3det']      = n_3det
    far_report['n_2det']      = n_2det

    # ── 6. Plot distributions ──
    plot_far_distributions(event_summary, trial_summaries, detectors,
                           event_name, far_dir)

    # ── 7. Save report ──
    report_path = os.path.join(far_dir, 'far_report.json')
    with open(report_path, 'w') as f:
        json.dump(far_report, f, indent=2, default=str)
    print(f'FAR report: {report_path}')

    # ── 8. Print summary ──
    print(f'\n{"="*60}')
    print(f'SIGNIFICANCE SUMMARY — {event_name}')
    print(f'{"="*60}')
    for det, stats in far_report['per_detector'].items():
        sig_s = stats.get('empirical_sigma_split')
        sig_n = stats.get('empirical_sigma_snr')
        print(f'  {det}  |  15Hz split: {sig_s:.2f}σ  |  '
              f'BMI SNR: {sig_n:.2f}σ'
              if sig_s and sig_n
              else f'  {det}  |  insufficient data')

    return far_report


def main():
    p = argparse.ArgumentParser(description='BMI False-Alarm Rate Analysis')
    p.add_argument('--event',    required=True,
                   help='Event name (e.g. GW190521)')
    p.add_argument('--n-trials', type=int, default=10,
                   help='Number of off-source trials (default 10)')
    p.add_argument('--detectors', nargs='+', default=['L1', 'V1'],
                   help='Detectors to analyse (default: L1 V1)')
    p.add_argument('--sample-rate', type=int, dest='sample_rate', default=None,
                   help='Override sample rate (Hz)')
    args = p.parse_args()

    run_far(
        event_name=args.event,
        detectors=args.detectors,
        n_trials=args.n_trials,
        sample_rate=args.sample_rate,
    )


if __name__ == '__main__':
    main()
