"""
BMI Universal GW Analyzer
=========================
A single self-contained pipeline for any LVK event or noise segment.

Usage
-----
  # Analyze a catalog event (auto-detects all parameters):
  python3 bmi_gw_analyzer.py --event GW190521

  # Falsification: run identical pipeline on a noise-only segment:
  python3 bmi_gw_analyzer.py --gps 1242442903 --duration 32 --label noise_pre_GW190521

  # Override sample rate or restrict detectors:
  python3 bmi_gw_analyzer.py --event GW150914 --sample-rate 4096 --detectors H1 L1

Output
------
  assets/GW_Analysis/<label>/
      summary.json          — all numerical results
      <det>_qscan.png
      <det>_impulse.png
      <det>_template_sub.png
      <det>_ringdown.png
"""

import argparse
import json
import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import h5py
from dataclasses import dataclass, field, asdict
from typing import Optional, List, Tuple

from scipy.signal import butter, sosfiltfilt, welch, stft as scipy_stft
from pycbc.types import TimeSeries
from pycbc.waveform import get_td_waveform

# ── BMI constants ──────────────────────────────────────────────────────────────
BMI_FREQ_SPLIT = 15.00   # Hz — from GW250114 baseline
BMI_K_BASELINE = 0.13

ALL_DETECTORS  = ['H1', 'L1', 'V1', 'K1']

REPO_ROOT = os.path.join(os.path.dirname(__file__), '..', '..')
DATA_DIR  = os.path.join(REPO_ROOT, 'data')
OUT_ROOT  = os.path.join(REPO_ROOT, 'assets', 'GW_Analysis')


# ── Event configuration ────────────────────────────────────────────────────────

@dataclass
class EventConfig:
    label:        str
    merger_gps:   float
    duration:     float        = 32.0       # seconds of data to fetch
    sample_rate:  int          = 16384
    m1:           Optional[float] = None
    m2:           Optional[float] = None
    distance_mpc: Optional[float] = None
    chirp_mass:   Optional[float] = None
    snr:          Optional[float] = None
    detectors:    List[str]    = field(default_factory=list)
    # analysis windows (auto-set from event type)
    bandpass_low:  float = 50.0
    bandpass_high: float = 600.0
    impulse_half_window: float = 0.15   # seconds either side of merger
    ringdown_k_window:   Tuple[float, float] = (0.001, 0.025)  # short: K ratio
    ringdown_fft_window: Tuple[float, float] = (0.001, 0.150)  # wider: FFT resolution
    is_noise_segment: bool = False


def resolve_event(args) -> EventConfig:
    """
    Build an EventConfig from CLI args.
    If --event is given, pull catalog parameters and auto-tune windows.
    If --gps is given, create a noise-segment config.
    """
    if args.event:
        return _from_catalog(args.event, args.sample_rate, args.detectors)
    else:
        cfg = EventConfig(
            label=args.label or f'noise_{int(args.gps)}',
            merger_gps=args.gps,
            duration=args.duration,
            sample_rate=args.sample_rate or 4096,
            is_noise_segment=True,
        )
        if args.detectors:
            cfg.detectors = args.detectors
        return cfg


def _from_catalog(event_name: str, override_sr: Optional[int],
                  override_dets: Optional[List[str]]) -> EventConfig:
    from pycbc.catalog import Merger
    m = Merger(event_name)

    m1   = float(m.mass1)
    m2   = float(m.mass2)
    mchirp = float(m.mchirp)
    dist = float(m.distance)
    snr  = float(m.snr)
    gps  = float(m.time)

    # Auto-tune analysis windows from chirp mass:
    # Heavy (>50 Msun): short burst, fine ringdown window
    # Light (<50 Msun): long chirp, wider ringdown window
    if mchirp >= 50.0:
        sr               = 16384
        impulse_hw       = 0.15
        bp_high          = 600.0
        rd_k_win         = (0.001, 0.025)
        rd_fft_win       = (0.001, 0.150)
    else:
        sr               = 4096
        impulse_hw       = 2.0
        bp_high          = 500.0
        rd_k_win         = (0.010, 0.500)
        rd_fft_win       = (0.010, 1.000)

    if override_sr:
        sr = override_sr

    cfg = EventConfig(
        label=event_name,
        merger_gps=gps,
        m1=m1, m2=m2,
        distance_mpc=dist,
        chirp_mass=mchirp,
        snr=snr,
        sample_rate=sr,
        bandpass_high=bp_high,
        impulse_half_window=impulse_hw,
        ringdown_k_window=rd_k_win,
        ringdown_fft_window=rd_fft_win,
    )

    if override_dets:
        cfg.detectors = override_dets
    else:
        cfg.detectors = _probe_detectors(event_name, sr)

    return cfg


def _probe_detectors(event_name: str, sample_rate: int) -> List[str]:
    """Try each detector; keep those that return valid data."""
    from pycbc.catalog import Merger
    m = Merger(event_name)
    available = []
    for det in ALL_DETECTORS:
        try:
            ts = m.strain(det, sample_rate=sample_rate)
            if ts is not None and len(ts) > 0:
                available.append(det)
                print(f'  Detector {det}: available ({len(ts)} samples)')
        except Exception:
            pass
    return available


# ── Data fetching with HDF5 cache ──────────────────────────────────────────────

def fetch_strain(cfg: EventConfig, det: str) -> TimeSeries:
    """Return strain TimeSeries, using local HDF5 cache when available."""
    cache_path = os.path.join(
        DATA_DIR,
        f'{cfg.label}_{det}_{cfg.sample_rate}Hz_strain.h5'
    )
    if os.path.exists(cache_path):
        return _load_hdf5(cache_path)

    if cfg.is_noise_segment:
        ts = _fetch_noise_segment(cfg, det)
    else:
        from pycbc.catalog import Merger
        ts = Merger(cfg.label).strain(det, sample_rate=cfg.sample_rate)
        if ts is None:
            raise RuntimeError(f'No data for {det}')

    _save_hdf5(ts, cache_path, cfg.sample_rate)
    print(f'  [{det}] fetched and cached: {cache_path}')
    return ts


def _fetch_noise_segment(cfg: EventConfig, det: str) -> TimeSeries:
    """Fetch an arbitrary GPS segment directly from GWOSC HDF5 files."""
    from gwosc.locate import get_urls
    import urllib.request

    t_centre = int(cfg.merger_gps)
    half     = int(cfg.duration / 2)
    t_start  = t_centre - half
    t_end    = t_centre + half

    urls = get_urls(det, t_start, t_end, sample_rate=cfg.sample_rate)
    if not urls:
        raise RuntimeError(
            f'No GWOSC data for {det} at GPS {t_centre} '
            f'(sample_rate={cfg.sample_rate}). '
            f'The detector may not have been observing at this time.'
        )

    # Download the first covering file to a temp cache
    url  = urls[0]
    fname = url.split('/')[-1]
    cache = os.path.join(DATA_DIR, 'gwosc_cache', fname)
    os.makedirs(os.path.dirname(cache), exist_ok=True)

    if not os.path.exists(cache):
        print(f'  [{det}] Downloading {fname} …')
        urllib.request.urlretrieve(url, cache)
        print(f'  [{det}] Saved to {cache}')

    # Read the 32-second slice centred on our GPS from the 4096-second file
    with h5py.File(cache, 'r') as f:
        # GWOSC HDF5 layout: /strain/Strain
        strain_ds = f['strain']['Strain']
        file_sr   = int(f['strain']['Strain'].attrs.get(
                        'Xspacing', 1.0) ** -1 if 'Xspacing' in
                        f['strain']['Strain'].attrs else cfg.sample_rate)
        # Fall back: read attributes from the meta group
        try:
            file_sr = int(round(1.0 / float(
                f['strain']['Strain'].attrs['Xspacing'])))
        except Exception:
            file_sr = cfg.sample_rate

        file_start = float(f['meta']['GPSstart'][()])
        idx_start  = int((t_start - file_start) * file_sr)
        idx_end    = int((t_end   - file_start) * file_sr)
        idx_start  = max(0, idx_start)
        idx_end    = min(len(strain_ds), idx_end)
        arr = strain_ds[idx_start:idx_end]

    return TimeSeries(arr.astype(np.float64),
                      delta_t=1.0/file_sr,
                      epoch=file_start + idx_start / file_sr)


def _save_hdf5(ts: TimeSeries, path: str, sample_rate: int):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with h5py.File(path, 'w') as f:
        f.create_dataset('strain', data=ts.numpy())
        f.create_dataset('time',   data=np.array(ts.sample_times))
        f.attrs['sample_rate'] = sample_rate
        f.attrs['epoch']       = float(ts.start_time)


def _load_hdf5(path: str) -> TimeSeries:
    with h5py.File(path, 'r') as f:
        arr   = f['strain'][:]
        sr    = float(f.attrs['sample_rate'])
        epoch = float(f.attrs['epoch'])
    return TimeSeries(arr, delta_t=1.0/sr, epoch=epoch)


# ── Signal conditioning ────────────────────────────────────────────────────────

def condition_strain(ts: TimeSeries, cfg: EventConfig) -> TimeSeries:
    """Estimate noise PSD from off-source quarters, whiten, bandpass."""
    psd_f, psd_v = _estimate_psd(ts)
    ts_w = _whiten(ts, psd_f, psd_v)
    ts_bp = _bandpass(ts_w, cfg.bandpass_low, cfg.bandpass_high)
    return ts_bp


def _estimate_psd(ts: TimeSeries) -> Tuple[np.ndarray, np.ndarray]:
    fs   = int(1.0 / ts.delta_t)
    data = ts.numpy()
    n    = len(data)
    off  = np.concatenate([data[:n//4], data[3*n//4:]])
    freqs, psd = welch(off, fs=fs, nperseg=int(4.0 * fs))
    return freqs, psd


def _whiten(ts: TimeSeries, psd_f, psd_v) -> TimeSeries:
    fs   = int(1.0 / ts.delta_t)
    data = ts.numpy()
    fft  = np.fft.rfft(data)
    f    = np.fft.rfftfreq(len(data), d=1.0/fs)
    psd_i = np.interp(f, psd_f, psd_v, left=psd_v[0], right=psd_v[-1])
    psd_i = np.maximum(psd_i, 1e-60)
    white = np.fft.irfft(fft / np.sqrt(psd_i), n=len(data))
    return TimeSeries(white, delta_t=ts.delta_t, epoch=ts.start_time)


def _bandpass(ts: TimeSeries, low: float, high: float) -> TimeSeries:
    fs  = int(1.0 / ts.delta_t)
    sos = butter(8, [low, high], btype='bandpass', fs=fs, output='sos')
    out = sosfiltfilt(sos, ts.numpy())
    return TimeSeries(out, delta_t=ts.delta_t, epoch=ts.start_time)


# ── Q-scan ─────────────────────────────────────────────────────────────────────

def make_qscan(ts: TimeSeries, cfg: EventConfig, det: str, out_dir: str):
    try:
        from gwpy.timeseries import TimeSeries as GWpyTS
        from astropy import units as u
        gts = GWpyTS(
            ts.numpy(), t0=float(ts.start_time),
            dt=ts.delta_t, unit=u.dimensionless_unscaled,
            name=f'{cfg.label} {det}'
        )
        t0, t1 = cfg.merger_gps - 2, cfg.merger_gps + 2
        qgram = gts.crop(t0, t1).q_transform(
            frange=(cfg.bandpass_low, cfg.bandpass_high),
            qrange=(4, 64),
            outseg=(cfg.merger_gps - 0.5, cfg.merger_gps + 0.5),
        )
        fig = qgram.plot(figsize=(10, 4))
        ax  = fig.gca()
        ax.set_epoch(cfg.merger_gps)
        ax.set_xlim(cfg.merger_gps - 0.5, cfg.merger_gps + 0.5)
        ax.set_yscale('log')
        ax.set_xlabel('Time relative to GPS merger (s)')
        ax.set_ylabel('Frequency (Hz)')
        ax.set_title(f'{cfg.label} Q-scan: {det}')
        path = os.path.join(out_dir, f'{det}_qscan.png')
        fig.savefig(path, dpi=150, bbox_inches='tight')
        plt.close(fig)
        return path
    except Exception as e:
        print(f'  [{det}] Q-scan skipped: {e}')
        return None


# ── Impulse analysis ───────────────────────────────────────────────────────────

def analyze_impulse(ts: TimeSeries, cfg: EventConfig, det: str,
                    out_dir: str) -> Optional[float]:
    fs    = int(1.0 / ts.delta_t)
    t_abs = np.array(ts.sample_times)
    t_rel = t_abs - cfg.merger_gps

    nperseg = min(256, len(ts) // 8)
    f, t_s, Zxx = scipy_stft(ts.numpy(), fs=fs, nperseg=nperseg,
                              noverlap=int(nperseg * 0.875))
    t_s_rel = t_s + (t_abs[0] - cfg.merger_gps)

    freq_max = f[np.argmax(np.abs(Zxx), axis=0)]
    dfdt = np.gradient(freq_max, t_s)
    with np.errstate(divide='ignore', invalid='ignore'):
        m_eff = (dfdt / (freq_max ** (11.0/3.0))) ** (3.0/5.0)
    m_eff = np.nan_to_num(m_eff)

    hw  = cfg.impulse_half_window
    win = (t_s_rel >= -hw) & (t_s_rel <= hw)

    duration = None
    if win.sum() >= 4:
        med   = np.nanmedian(np.abs(m_eff[win]))
        above = t_s_rel[win][np.abs(m_eff[win]) > med]
        if above.size >= 2:
            duration = float(above[-1] - above[0])

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t_s_rel[win], m_eff[win], lw=1.5, label=f'ECM ({det})')
    ax.axvline(0, color='red', ls='--', label='Merger / reference GPS')
    ax.set_title(f'{cfg.label} Impulse/Chirp Profile: {det}')
    ax.set_xlabel('Time to GPS reference (s)')
    ax.set_ylabel('Effective Chirp Mass')
    ax.legend(fontsize=8)
    ax.grid(True, ls='--', alpha=0.5)
    path = os.path.join(out_dir, f'{det}_impulse.png')
    fig.savefig(path, dpi=150, bbox_inches='tight')
    plt.close(fig)

    print(f'  [{det}] Impulse duration: '
          f'{duration:.4f} s' if duration else f'  [{det}] Impulse: undetermined')
    return duration


# ── Template subtraction ───────────────────────────────────────────────────────

def subtract_template(ts: TimeSeries, cfg: EventConfig,
                      det: str, out_dir: str) -> Tuple[TimeSeries, np.ndarray]:
    """
    Generate best-fit IMRPhenomPv2 template from catalog params (if available),
    align by cross-correlation, amplitude-scale, subtract.
    Falls back to zero template (residual = data) for noise segments or
    events without catalog params.
    """
    strain = ts.numpy()
    t_abs  = np.array(ts.sample_times)
    t_rel  = t_abs - cfg.merger_gps

    if cfg.is_noise_segment or cfg.m1 is None:
        print(f'  [{det}] No template available — residual = raw data')
        tmpl = np.zeros_like(strain)
    else:
        hp, _ = get_td_waveform(
            approximant='IMRPhenomPv2',
            mass1=cfg.m1, mass2=cfg.m2,
            spin1z=0.0, spin2z=0.0,
            delta_t=ts.delta_t, f_lower=20.0,
            distance=cfg.distance_mpc, inclination=0.0,
        )
        hp_bp = _bandpass(hp, cfg.bandpass_low, cfg.bandpass_high)
        tmpl  = hp_bp.numpy()

        # Trim or zero-pad to match data length
        if len(tmpl) < len(strain):
            tmpl = np.pad(tmpl, (len(strain) - len(tmpl), 0))
        else:
            tmpl = tmpl[-len(strain):]

        # Cross-correlation time alignment
        corr = np.correlate(strain, tmpl, mode='full')
        lag  = int(np.argmax(np.abs(corr))) - (len(strain) - 1)
        if lag > 0:
            tmpl = np.concatenate([np.zeros(lag), tmpl[:-lag]])
        elif lag < 0:
            tmpl = np.concatenate([tmpl[-lag:], np.zeros(-lag)])

        # Amplitude-scale to merger peak
        pm = (t_rel >= -0.05) & (t_rel <= 0.05)
        dp = np.max(np.abs(strain[pm])) if pm.any() else 1.0
        tp = np.max(np.abs(tmpl[pm]))   if pm.any() else 1.0
        if tp > 0:
            tmpl *= dp / tp

    residual = strain - tmpl

    # Comparison plot
    hw  = cfg.impulse_half_window * 2
    win = (t_rel >= -hw * 0.5) & (t_rel <= hw)
    fig, axes = plt.subplots(3, 1, figsize=(11, 9), sharex=True)
    axes[0].plot(t_rel[win], strain[win],   color='steelblue',  lw=1.0,
                 label='Whitened Data')
    axes[1].plot(t_rel[win], tmpl[win],     color='darkorange',  lw=1.0,
                 label='NR Template' if cfg.m1 else 'Template (none)')
    axes[2].plot(t_rel[win], residual[win], color='crimson',     lw=1.0,
                 label='Residual')
    for ax in axes:
        ax.axvline(0, color='k', ls='--', alpha=0.4)
        ax.legend(loc='upper right', fontsize=8)
        ax.grid(True, ls='--', alpha=0.4)
    axes[2].set_xlabel('Time to GPS reference (s)')
    axes[0].set_title(f'{cfg.label} {det}: Data / Template / Residual')
    fig.tight_layout()
    path = os.path.join(out_dir, f'{det}_template_sub.png')
    fig.savefig(path, dpi=150, bbox_inches='tight')
    plt.close(fig)

    return TimeSeries(residual, delta_t=ts.delta_t, epoch=ts.start_time), tmpl


# ── Ringdown / 15 Hz split / K ────────────────────────────────────────────────

def analyze_ringdown(residual_ts: TimeSeries, tmpl_arr: np.ndarray,
                     cfg: EventConfig, det: str,
                     out_dir: str) -> dict:
    """
    Returns dict with: peak_freq, bmi_zone_snr, split_hz, split_rel_power, K.
    Uses two windows: short for K, longer for FFT frequency resolution.
    """
    from scipy.signal.windows import hann

    fs     = int(1.0 / residual_ts.delta_t)
    t_abs  = np.array(residual_ts.sample_times)
    t_rel  = t_abs - cfg.merger_gps
    data   = residual_ts.numpy()

    results = {
        'detector': det,
        'K': None, 'K_note': '',
        'peak_freq_hz': None,
        'bmi_zone_snr': None,
        'split_candidate_hz': None,
        'split_rel_power': None,
    }

    # --- K coupling (short window) ---
    k0, k1 = cfg.ringdown_k_window
    k_mask = (t_rel >= k0) & (t_rel <= k1)
    if k_mask.sum() >= 4:
        e_res  = float(np.sum(data[k_mask] ** 2))
        e_tmpl = float(np.sum(tmpl_arr[k_mask] ** 2))
        if e_tmpl > 0:
            K = e_res / e_tmpl
            results['K'] = K
            results['K_note'] = f'residual/template [{k0*1000:.0f}-{k1*1000:.0f}ms]'
            print(f'  [{det}] K = {K:.6f}  (BMI baseline {BMI_K_BASELINE})')
        else:
            results['K_note'] = 'template ~0 in window; GR ringdown fully decayed'
            results['residual_energy'] = e_res
            print(f'  [{det}] GR template ~0 in [{k0*1e3:.0f}–{k1*1e3:.0f}ms]; '
                  f'residual energy = {e_res:.4e} (non-GR excess candidate)')

    # --- FFT / 15 Hz split (wider window) ---
    f0, f1 = cfg.ringdown_fft_window
    fft_mask = (t_rel >= f0) & (t_rel <= f1)
    if fft_mask.sum() < 16:
        print(f'  [{det}] Insufficient ringdown samples for FFT')
        return results

    rd  = data[fft_mask]
    win = hann(len(rd))
    fft_c  = np.fft.rfft(rd * win)
    freqs  = np.fft.rfftfreq(len(rd), d=1.0/fs)
    power  = np.abs(fft_c) ** 2

    peak_idx  = int(np.argmax(power))
    peak_freq = float(freqs[peak_idx])
    peak_pow  = float(power[peak_idx])

    # BMI resonance zone SNR (±15 Hz around 150 Hz)
    zone = (freqs >= 135) & (freqs <= 165)
    zone_snr = float(np.max(power[zone]) / np.mean(power)) if zone.any() else 0.0

    # 15 Hz sub-harmonic split search (±5 Hz tolerance)
    target = peak_freq - BMI_FREQ_SPLIT
    split_r = (freqs >= target - 5) & (freqs <= target + 5)
    split_ratio = 0.0
    if np.any(split_r) and peak_pow > 0:
        split_ratio = float(np.max(power[split_r]) / peak_pow)

    results.update({
        'peak_freq_hz': peak_freq,
        'bmi_zone_snr': zone_snr,
        'split_candidate_hz': float(target),
        'split_rel_power': split_ratio,
    })

    print(f'  [{det}] Ringdown peak: {peak_freq:.1f} Hz | '
          f'BMI 150Hz zone SNR: {zone_snr:.2f} | '
          f'15Hz split rel. power: {split_ratio:.4f}')

    # Spectrum plot
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.semilogy(freqs, power, lw=1.0, color='navy', alpha=0.8)
    ax.axvline(peak_freq, color='red',    ls='--',
               label=f'Peak {peak_freq:.0f} Hz')
    ax.axvline(target,    color='orange', ls=':',
               label=f'−{BMI_FREQ_SPLIT} Hz split ({target:.0f} Hz)')
    ax.axvspan(135, 165,  alpha=0.08, color='green', label='BMI 150 Hz zone')
    ax.set_xlim(0, cfg.bandpass_high)
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Power')
    ax.set_title(f'{cfg.label} {det} Residual Ringdown Spectrum')
    ax.legend(fontsize=8)
    ax.grid(True, ls='--', alpha=0.4)
    path = os.path.join(out_dir, f'{det}_ringdown.png')
    fig.savefig(path, dpi=150, bbox_inches='tight')
    plt.close(fig)

    return results


# ── Main pipeline ──────────────────────────────────────────────────────────────

def run(cfg: EventConfig):
    out_dir = os.path.join(OUT_ROOT, cfg.label)
    os.makedirs(out_dir,  exist_ok=True)
    os.makedirs(DATA_DIR, exist_ok=True)

    print(f'\n{"="*60}')
    print(f'BMI GW Analyzer: {cfg.label}')
    print(f'  GPS reference: {cfg.merger_gps}')
    if not cfg.is_noise_segment:
        print(f'  m1={cfg.m1} m2={cfg.m2} Msun | '
              f'd={cfg.distance_mpc:.0f} Mpc | SNR={cfg.snr:.2f}')
    else:
        print(f'  Mode: NOISE / FALSIFICATION segment')
    print(f'  Sample rate: {cfg.sample_rate} Hz | '
          f'Bandpass: {cfg.bandpass_low}–{cfg.bandpass_high} Hz')
    print(f'  Detectors: {cfg.detectors}')
    print(f'{"="*60}\n')

    all_results = {
        'label':      cfg.label,
        'merger_gps': cfg.merger_gps,
        'is_noise':   cfg.is_noise_segment,
        'config':     asdict(cfg),
        'detectors':  {},
    }

    for det in cfg.detectors:
        print(f'--- {det} ---')
        try:
            ts_raw = fetch_strain(cfg, det)
            print(f'  Raw: {len(ts_raw)} samples @ {cfg.sample_rate} Hz')

            ts = condition_strain(ts_raw, cfg)
            print(f'  Whitened + bandpassed')

            qscan_path   = make_qscan(ts, cfg, det, out_dir)
            impulse_dur  = analyze_impulse(ts, cfg, det, out_dir)
            residual_ts, tmpl_arr = subtract_template(ts, cfg, det, out_dir)
            rd_results   = analyze_ringdown(residual_ts, tmpl_arr, cfg, det, out_dir)

            all_results['detectors'][det] = {
                'impulse_duration_s': impulse_dur,
                **rd_results,
            }
        except Exception as e:
            print(f'  [{det}] ERROR: {e}')
            all_results['detectors'][det] = {'error': str(e)}
        print()

    # Save JSON summary
    summary_path = os.path.join(out_dir, 'summary.json')
    with open(summary_path, 'w') as fh:
        json.dump(all_results, fh, indent=2, default=str)

    print(f'Results saved to: {out_dir}')
    print(f'Summary JSON:     {summary_path}')
    return all_results


# ── CLI ────────────────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(
        description='BMI Universal GW Analyzer',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument('--event',    type=str,
                      help='LVK catalog event name, e.g. GW190521')
    mode.add_argument('--gps',      type=float,
                      help='GPS start time for a noise/falsification segment')

    p.add_argument('--duration',    type=float, default=32.0,
                   help='Duration in seconds (noise mode only, default 32)')
    p.add_argument('--label',       type=str,
                   help='Output label (noise mode); defaults to noise_<GPS>')
    p.add_argument('--sample-rate', type=int, dest='sample_rate',
                   help='Override sample rate (Hz)')
    p.add_argument('--detectors',   type=str, nargs='+',
                   help='Override detector list, e.g. H1 L1')

    args = p.parse_args()

    # Resolve sys.path so resonance_filter imports work when called directly
    sys.path.insert(0, os.path.dirname(__file__))

    cfg = resolve_event(args)
    run(cfg)


if __name__ == '__main__':
    main()
