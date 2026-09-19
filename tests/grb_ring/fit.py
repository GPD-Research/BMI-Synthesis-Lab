"""Circle vs. log-spiral shape test for the 9 GRBs of Balazs et al. 2015 (Table 1).

All fits use the orthogonal (geometric) point-to-curve distance in a gnomonic
tangent-plane projection (degrees) centred on the sample centroid.

Models (k = free parameters):
  circle        k=3  (cx, cy, r)
  golden spiral k=4  (cx, cy, a, th0)  pitch fixed: r = a exp(b th), b = ln(phi)/(pi/2), both chiralities tried
  log spiral    k=5  (cx, cy, a, th0, b)
  Spirals are single arcs of <= TURNS turns starting at th0 (an unbounded tight spiral is space-filling).
  ellipse       k=5  (cx, cy, A, B, angle)   -- the paper's own description (43 x 30 deg)
BIC = n ln(RSS/n) + k ln n. Null: 9 uniform-random sky points in the same footprint.
"""
import sys, numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(20150702)
PHI = (1 + 5 ** 0.5) / 2
B_GOLDEN = np.log(PHI) / (np.pi / 2)

grb = np.array([  # l, b  (deg)
    [149.05, -42.52], [114.45, -17.20], [118.43, -42.96], [123.46, -39.99],
    [150.37, -28.43], [106.53, -41.28], [101.39, -32.53], [123.85, -12.65],
    [142.92, -20.54]])


def to_unit(lb):
    l, b = np.radians(lb[:, 0]), np.radians(lb[:, 1])
    return np.stack([np.cos(b) * np.cos(l), np.cos(b) * np.sin(l), np.sin(b)], 1)


def gnomonic(lb):
    v = to_unit(lb)
    c = v.mean(0); c /= np.linalg.norm(c)
    e1 = np.cross([0, 0, 1], c); e1 /= np.linalg.norm(e1)
    e2 = np.cross(c, e1)
    d = v @ c
    return np.degrees(np.stack([(v @ e1) / d, (v @ e2) / d], 1))


# ---------- residual functions (geometric distance) ----------
def circle_rss(p, xy):
    cx, cy, r = p
    return np.sum((np.hypot(xy[:, 0] - cx, xy[:, 1] - cy) - abs(r)) ** 2)


def ellipse_rss(p, xy, n=720):
    cx, cy, A, B, ang = p
    t = np.linspace(0, 2 * np.pi, n, endpoint=False)
    ca, sa = np.cos(ang), np.sin(ang)
    ex, ey = abs(A) * np.cos(t), abs(B) * np.sin(t)
    curve = np.stack([cx + ex * ca - ey * sa, cy + ex * sa + ey * ca], 1)
    d2 = ((xy[:, None, :] - curve[None]) ** 2).sum(-1)
    return d2.min(1).sum()


TURNS = 1.0  # spiral is a single-sweep arc of at most this many turns (prevents space-filling fits)


def spiral_rss(p, xy, b, n=800):
    cx, cy, a, th0 = p
    a = abs(a) + 1e-9
    th = np.linspace(0, TURNS * 2 * np.pi, n)
    r = a * np.exp(b * th)
    th = th + th0
    curve = np.stack([cx + r * np.cos(th), cy + r * np.sin(th)], 1)
    d2 = ((xy[:, None, :] - curve[None]) ** 2).sum(-1)
    return d2.min(1).sum()


def fit(fun, x0s, args=()):
    best = None
    for x0 in x0s:
        r = minimize(fun, x0, args=args, method="Nelder-Mead",
                     options=dict(xatol=1e-3, fatol=1e-5, maxiter=800))
        if best is None or r.fun < best.fun:
            best = r
    return best.fun, best.x


def fit_all(xy, spiral_starts=6):
    c0 = xy.mean(0)
    r0 = np.hypot(*(xy - c0).T).mean()
    out = {}
    out["circle"] = fit(circle_rss, [[*c0, r0], [*(c0 + 3), r0 * 1.3], [*(c0 - 3), r0 * 0.7]], (xy,))
    out["ellipse"] = fit(ellipse_rss, [[*c0, r0, r0, 0], [*c0, 1.3 * r0, 0.7 * r0, 0.5],
                                        [*c0, 1.3 * r0, 0.7 * r0, -0.8]], (xy,))
    # spirals: multiple centre starts + both chiralities (b>0 / b<0)
    starts = [[*(c0 + rng.normal(0, r0 * 0.4, 2)), r0 * np.exp(rng.uniform(-1.5, 0.5)), rng.uniform(0, 2 * np.pi)]
              for _ in range(spiral_starts)] + [[*c0, r0, t] for t in np.linspace(0, 2 * np.pi, 8, endpoint=False)]
    g = [fit(spiral_rss, starts, (xy, sgn * B_GOLDEN)) for sgn in (1, -1)]
    out["golden"] = min(g, key=lambda t: t[0])
    # free-pitch log spiral: outer 1-D search over b (fit is robust that way)
    best = (np.inf, None)
    for b in np.concatenate([np.geomspace(0.04, 1.0, 5), -np.geomspace(0.04, 1.0, 5)]):
        f, x = fit(spiral_rss, starts[:6], (xy, b))
        if f < best[0]:
            best = (f, np.append(x, b))
    # local refine of b
    f0, x0 = best
    def free(p):
        return spiral_rss(p[:4], xy, p[4]) if abs(p[4]) > 1e-3 else 1e9
    r = minimize(free, x0, method="Nelder-Mead", options=dict(xatol=1e-3, fatol=1e-5, maxiter=800))
    out["logspiral"] = (min(r.fun, f0), r.x if r.fun < f0 else x0)
    return out


K = dict(circle=3, golden=4, logspiral=5, ellipse=5)


def bic(rss, k, n):
    return n * np.log(max(rss, 1e-12) / n) + k * np.log(n)


def summarize(out, n):
    return {m: (out[m][0], np.sqrt(out[m][0] / n), bic(out[m][0], K[m], n)) for m in out}


def one_null(args):
    seed, lo_l, hi_l, lo_b, hi_b, n = args
    global rng
    rng = np.random.default_rng(1000 + seed)
    sinb = rng.uniform(np.sin(np.radians(lo_b)), np.sin(np.radians(hi_b)), n)
    pts = np.stack([rng.uniform(lo_l, hi_l, n), np.degrees(np.arcsin(sinb))], 1)
    return summarize(fit_all(gnomonic(pts), spiral_starts=4), n)


if __name__ == "__main__":
    n_null = int(sys.argv[1]) if len(sys.argv) > 1 else 500
    xy = gnomonic(grb)
    n = len(xy)
    obs = fit_all(xy, spiral_starts=12)
    S = summarize(obs, n)
    print("OBSERVED (tangent-plane degrees)")
    for m in ["circle", "golden", "logspiral", "ellipse"]:
        rss, rms, B = S[m]
        print(f"  {m:10s} k={K[m]}  RSS={rss:7.3f}  RMS={rms:5.3f} deg  BIC={B:7.2f}  params={np.round(obs[m][1],3)}")
    dB = {m: S[m][2] - S["circle"][2] for m in ["golden", "logspiral", "ellipse"]}
    print("  dBIC vs circle (negative = beats circle):", {m: round(v, 2) for m, v in dB.items()})

    # footprint for null: box around the points in galactic coords, padded 5 deg
    lo_l, hi_l = grb[:, 0].min() - 5, grb[:, 0].max() + 5
    lo_b, hi_b = grb[:, 1].min() - 5, grb[:, 1].max() + 5
    print(f"\nNULL: {n_null} sets of 9 uniform points in l=[{lo_l:.0f},{hi_l:.0f}] b=[{lo_b:.0f},{hi_b:.0f}]")
    null = {m: [] for m in dB}
    null_abs = {m: [] for m in K}
    from multiprocessing import Pool
    with Pool() as pool:
        for i, s in enumerate(pool.imap_unordered(one_null, [(seed, lo_l, hi_l, lo_b, hi_b, n) for seed in range(n_null)])):
            for m in dB:
                null[m].append(s[m][2] - s["circle"][2])
            for m in K:
                null_abs[m].append(s[m][1])
            if (i + 1) % 50 == 0:
                print(f"  ...{i+1}", flush=True)
    for m in dB:
        arr = np.array(null[m])
        p = np.mean(arr <= dB[m])
        print(f"  {m:10s} obs dBIC={dB[m]:6.2f}   null: median={np.median(arr):6.2f}  "
              f"P(null dBIC <= obs)={p:.3f}   P(null beats circle at all)={np.mean(arr<0):.3f}")
    print("\nHow special is the observed fit quality itself? P(null RMS <= obs RMS):")
    for m in K:
        arr = np.array(null_abs[m])
        print(f"  {m:10s} obs RMS={S[m][1]:.3f}  P={np.mean(arr <= S[m][1]):.4f}")
    np.save("/home/ubuntu/grbring/null.npy", {"dB": null, "rms": null_abs, "obs": S}, allow_pickle=True)
