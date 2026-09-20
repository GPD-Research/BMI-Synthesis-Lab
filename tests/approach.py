"""Milestone 5c: the approach to Omega = 1 without the moduli approximation (v2/04c_approach.md).

Exact two-brane cosmology in a static Schwarzschild-AdS bulk (Birkhoff: Bowcock, Charmousis &
Gregory 2000). Each Z_2 brane with n isotropic spatial dimensions moves in
    ds^2 = -f dt^2 + dr^2/f + (r/l)^2 dx_n^2 ,   f = r^2/l^2 - mu / r^(n-1),
and its induced FRW scale factor R(tau) obeys the junction condition (units l = kappa^2 = 1)
    sqrt(f/R^2 + H^2) = (sigma_1 + s rho) / (2n),   s = +1 (Sigma_1, tension +sigma_1),
                                                     s = -1 (Sigma_2, tension -sigma_1),
with sigma_1 = 2n (the RS tuning; n = 4 gives 8 M_6^4/l) and rho = A / R^(n+1) (radiation).
There is no independent radion: the separation Omega = R_2/R_1 at equal bulk time follows from
(A_1, A_2, mu).  Dimensionless collision data:
    f   = A_2/A_1        radiation on Sigma_2 / radiation on Sigma_1 at coincidence,
    eps = n mu / A_1     dark radiation (bulk mass) / radiation on Sigma_1 (both ~ R^-(n+1)),
    h   = rho_1 / sigma_1 at coincidence   (high-energy parameter).
Low-energy prediction (derived in 04c §2):  Omega_inf^(n-1) = (eps - f) / (1 + eps).

n = 4: the 6D action with the circle expanding with the brane (isotropic 4-brane).
n = 3: the 5D two-brane system (no circle) — the 3+1 exact case for comparison.
Run:  python3 tests/approach.py
"""
import numpy as np
from scipy.integrate import solve_ivp

OMEGA_CASSINI = 0.032
OMEGA_GONE = 1e-4


def brane_rhs(n, s, A, mu):
    """Bulk-time ODE for u = ln R of one expanding brane: dR/dt = sqrt(V) * dtau/dt.

    V(R) = (dR/dtau)^2 from the junction condition; dt/dtau = R (sigma + s rho) / (2n f).
    """
    sigma = 2 * n

    def V(R):
        rho = A / R ** (n + 1)
        fR = R ** 2 - mu / R ** (n - 1)
        return R ** 2 * ((sigma + s * rho) / (2 * n)) ** 2 - fR

    def rhs(t, y):
        R = np.exp(min(y[0], 120.0))
        rho = A / R ** (n + 1)
        fR = R ** 2 - mu / R ** (n - 1)
        v = max(V(R), 0.0)
        return [np.sqrt(v) * 2 * n * fR / (R * R * (sigma + s * rho))]

    return rhs, V


def run_brane(n, s, A, mu, R0=1.0, t_end=2e4):
    """Returns (t, R) arrays and a flag telling whether the brane stopped expanding (V -> 0)."""
    rhs, V = brane_rhs(n, s, A, mu)
    if V(R0) < 0:
        return None          # junction condition has no real solution: brane cannot exist here

    def turnaround(t, y):
        return V(np.exp(y[0])) - 1e-14

    turnaround.terminal = True

    def too_large(t, y):
        return y[0] - 100.0

    too_large.terminal = True
    sol = solve_ivp(rhs, (0, t_end), [np.log(R0)], events=[turnaround, too_large], rtol=1e-9,
                    atol=1e-12, dense_output=True)
    stopped = len(sol.t_events[0]) > 0
    return sol, stopped


def omega_of_bulk_time(n, f, eps, h, t_end=2e4, npts=400):
    """Omega(t) = R_2/R_1 at equal bulk time, starting from coincidence R_1 = R_2 = 1."""
    sigma = 2 * n
    A1 = h * sigma
    A2 = f * A1
    mu = eps * A1 / n
    r1 = run_brane(n, +1, A1, mu, t_end=t_end)
    r2 = run_brane(n, -1, A2, mu, t_end=t_end)
    if r1 is None or r2 is None:
        return None, None, "no real trajectory for Sigma_2 at coincidence"
    (s1, _), (s2, stopped) = r1, r2
    t_stop = min(s1.t[-1], s2.t[-1])
    ts = np.geomspace(1e-3, t_stop, npts)
    R1 = np.exp(s1.sol(ts)[0])
    R2 = np.exp(s2.sol(ts)[0])
    Om = R2 / R1
    if np.any(Om > 1 + 1e-9):
        note = "branes cross (Omega > 1): Sigma_2 overtakes Sigma_1, ordering lost"
    elif stopped:
        note = "Sigma_2 stops expanding and falls to the bulk horizon"
    else:
        note = "ok"
    return ts, Om, note


def omega_inf_closed(n, f, eps):
    x = (eps - f) / (1 + eps)
    return x ** (1 / (n - 1)) if x > 0 else 0.0


def eps_window(n, f, Omega_max=OMEGA_CASSINI):
    """eps range giving 0 < Omega_inf < Omega_max at low energy (closed form)."""
    lo = f
    hi = (f + Omega_max ** (n - 1)) / (1 - Omega_max ** (n - 1))
    return lo, hi


if __name__ == "__main__":
    print("=" * 96)
    print("1. exact two-brane solution vs closed form  (h = 0.01: low energy at coincidence)")
    print("=" * 96)
    for n in (4, 3):
        print(f"\n--- n = {n} ({'6D, isotropic 4-brane' if n == 4 else '5D, 3-brane'}) ---")
        print(f"{'f':>8} {'eps':>10} {'Omega_num':>11} {'Omega_closed':>13}  note")
        for f, eps in [(0.02, 0.05), (0.02, 0.0201), (0.02, 0.02000001), (0.02, 0.019), (0.0, 0.05), (0.02, 0.5)]:
            ts, Om, note = omega_of_bulk_time(n, f, eps, h=0.01)
            Om_num = float(Om[-1]) if Om is not None else float("nan")
            Om_cl = omega_inf_closed(n, f, eps)
            print(f"{f:8.4f} {eps:10.6f} {Om_num:11.5f} {Om_cl:13.5f}  {note}")
            if Om is not None and note == "ok" and eps > f * 1.001:
                assert abs(Om_num - Om_cl) < 0.05 * max(Om_cl, 1e-3) + 2e-3, (n, f, eps, Om_num, Om_cl)

    print("\n" + "=" * 96)
    print("2. the Cassini window in eps for given f (closed form, low energy)")
    print("=" * 96)
    for n in (4, 3):
        print(f"\n--- n = {n} ---")
        print(f"{'f':>8} {'eps_min (= f)':>14} {'eps_max':>12} {'width/f':>12}")
        for f in (0.04, 0.01, 1e-3, 1e-4):
            lo, hi = eps_window(n, f)
            print(f"{f:8.4f} {lo:14.6e} {hi:12.6e} {(hi - lo) / f:12.3e}")

    print("\n" + "=" * 96)
    print("3. high energy at coincidence (h = 1 and h = 10): does the closed form survive?")
    print("=" * 96)
    for n in (4, 3):
        print(f"\n--- n = {n} ---")
        print(f"{'h':>6} {'f':>8} {'eps':>10} {'Omega_num':>11} {'Omega_closed':>13}  note")
        for h in (1.0, 10.0):
            for f, eps in [(0.02, 0.05), (0.02, 0.019), (0.5, 0.6), (0.5, 0.3)]:
                ts, Om, note = omega_of_bulk_time(n, f, eps, h=h)
                Om_num = float(Om[-1]) if Om is not None else float("nan")
                print(f"{h:6.1f} {f:8.4f} {eps:10.6f} {Om_num:11.5f} {omega_inf_closed(n, f, eps):13.5f}  {note}")

    # deterministic verdicts used in 04c_approach.md
    ts, Om, note = omega_of_bulk_time(4, 0.02, 0.019, h=0.01)
    assert note != "ok" or Om[-1] < OMEGA_GONE, "eps < f must lose Sigma_2"
    lo, hi = eps_window(4, 0.01)
    assert (hi - lo) / lo < 4e-3, "n=4 Cassini window at f=0.01 must be a <0.4% relative tuning of eps"
    lo3, hi3 = eps_window(3, 0.01)
    assert (hi3 - lo3) / lo3 < 0.11, "n=3 Cassini window at f=0.01 must be a <11% relative tuning of eps"
    ts, Om, note = omega_of_bulk_time(4, 0.5, 0.6, h=10.0)
    assert note.startswith("branes cross"), "h = 10 must lose the brane ordering"
    print("\nALL OK")
