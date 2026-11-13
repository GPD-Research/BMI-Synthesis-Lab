"""z_t fork (ledger.md): what the source-frame CMB temperature allows.

Fork: 1 + z_obs = (1 + z_exp)(1 + z_t), z_t -> 0 nearby. The CMB at the source is at
T0 (1 + z_exp), so a measured T gives the curve directly: 1 + z_t = T0 (1 + z_obs) / T.
Data: tests/data/tcmb_z.csv (SZ, molecular/atomic absorbers, HFLS3 water at z = 6.34).
Asymmetric errors: the side facing the model is used.

Shapes for ln(1 + z_t):
  zero        ΛCDM
  power       beta ln(1 + z)                      (the usual T ∝ (1 + z)^{1 - beta})
  threshold   A max(0, ln((1 + z)/(1 + z_th)))   (smooth nearby, off beyond z_th; the fork as stated)
Then: the largest extra age the data allow at the redshifts the fork cares about.

Run:  python3 tests/zt_tcmb.py
"""
import os
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar

DATA = os.path.join(os.path.dirname(__file__), "data", "tcmb_z.csv")
T0 = 2.72548
H0, OM, OR = 67.4, 0.315, 9.1e-5
GYR = 977.8 / H0
REG_ZTH, REG_1PZT14 = 3.0, 2.2


def load():
    rows = [l.split(",") for l in open(DATA) if l.strip() and not l.startswith(("#", "z,"))]
    z, T, lo, hi = (np.array([float(r[i]) for r in rows]) for i in range(4))
    return z, T, lo, hi, np.array([r[4] for r in rows])


def chi2(lnzt, z, T, lo, hi):
    model = T0 * (1 + z) / np.exp(lnzt)
    sig = np.where(T > model, lo, hi)
    return float(np.sum(((T - model) / sig) ** 2))


def age(z):
    E = lambda a: np.sqrt(OM / a ** 3 + OR / a ** 4 + 1 - OM - OR)
    return quad(lambda a: 1 / (a * E(a)), 0, 1 / (1 + z), limit=200)[0] * GYR


def fit1(shape, z, T, lo, hi):
    f = lambda p: chi2(shape(p, z), z, T, lo, hi)
    r = minimize_scalar(f, bounds=(-1, 3), method="bounded", options={"xatol": 1e-7})
    best, c0 = r.x, r.fun
    up = minimize_scalar(lambda p: (f(p) - c0 - 4) ** 2 if p > best else 1e9,
                         bounds=(best, 3), method="bounded", options={"xatol": 1e-7}).x
    return best, c0, up                                    # up: 2-sigma upper end (Δχ² = 4)


def main():
    z, T, lo, hi, kind = load()
    n = len(z)
    c_zero = chi2(np.zeros(n), z, T, lo, hi)
    print(f"{n} points; ΛCDM (z_t = 0): chi2 = {c_zero:.1f}")

    power = lambda b, z: b * np.log1p(z)
    b, cb, bup = fit1(power, z, T, lo, hi)
    print(f"power:     beta = {b:+.4f}, 2-sigma upper {bup:+.4f}, chi2 = {cb:.1f}")
    assert abs(b) < 0.05, "beta should be consistent with the published ~0.01 +- 0.013"

    print("threshold: z_th | best A | 2-sigma A_max | z_t max at z = 1, 2.5, 6.34 | data above z_th")
    out = {}
    for zth in (0.5, 1.0, 1.3, 2.0, 3.0):
        thr = lambda A, z, zth=zth: A * np.maximum(0, np.log((1 + z) / (1 + zth)))
        A, cA, Aup = fit1(thr, z, T, lo, hi)
        zt = [float(np.expm1(thr(Aup, np.array([zz])))[0]) for zz in (1.0, 2.5, 6.34)]
        out[zth] = (Aup, zt)
        print(f"           {zth:4} | {A:+.3f} | {Aup:.3f} | {zt[0]:.3f} {zt[1]:.3f} {zt[2]:.3f} | {int(np.sum(z > zth))}")

    print("extra age allowed (2 sigma), from the source temperature alone:")
    for zobs, zth in ((2.5, 1.3), (6.34, 1.3), (6.34, 3.0), (14.0, 1.3), (14.0, 3.0)):
        Aup = out[zth][0]
        zt = float(np.expm1(Aup * max(0.0, np.log((1 + zobs) / (1 + zth)))))
        zexp = (1 + zobs) / (1 + zt) - 1
        print(f"  z_obs = {zobs}, threshold {zth}: z_t < {zt:.3f}, age {age(zobs) * 1e3:.0f} -> "
              f"{age(zexp) * 1e3:.0f} Myr (+{(age(zexp) - age(zobs)) * 1e3:.0f} Myr)")

    # the single z = 6.34 point on its own (the only test of 'off at very long distance')
    i = kind == "h2o"
    zt634 = T0 * (1 + 6.34) / (T[i][0] - 2 * lo[i][0]) - 1
    print(f"HFLS3 alone, 2 sigma: z_t(6.34) < {zt634:.2f} (T > {T[i][0] - 2 * lo[i][0]:.1f} K)")
    assert out[1.3][1][2] < 0.2 and out[3.0][1][2] > 0.5

    # pre-registered claim (2026-11-13, 08_zt_tcmb.md S3): threshold at z = 3, amplitude fixed by
    # 1 + z_t(14) = 2.2 (a z_obs = 14 galaxy gets ~1 Gyr), nothing fitted to the temperatures
    A = np.log(REG_1PZT14) / np.log(15 / (1 + REG_ZTH))
    print(f"registered: z_th = {REG_ZTH}, A = {A:.3f}")
    print("  z_obs | z_t | T_CMB LCDM -> registered | age LCDM -> registered")
    for zz in (3.19, 4.62, 6.34, 7.27, 10.0, 14.0):
        zt = float(np.expm1(A * max(0.0, np.log((1 + zz) / (1 + REG_ZTH)))))
        zexp = (1 + zz) / (1 + zt) - 1
        print(f"  {zz:5} | {zt:.2f} | {T0 * (1 + zz):5.1f} -> {T0 * (1 + zexp):5.1f} K | "
              f"{age(zz) * 1e3:4.0f} -> {age(zexp) * 1e3:4.0f} Myr")
    reg = A * np.maximum(0, np.log((1 + z) / (1 + REG_ZTH)))
    dchi = chi2(reg, z, T, lo, hi) - c_zero
    print(f"  current data: chi2(registered) - chi2(LCDM) = {dchi:+.2f} (HFLS3 carries it)")
    assert 0 < dchi < 4, "registered curve should be mildly disfavoured but allowed by today's data"
    print("ALL OK")


if __name__ == "__main__":
    main()
