# 09 — The time-slip fork as a clock effect

The intended version of the `z_t` fork (2026-11-13) is a **clock effect**, not a redshift effect:
redshift and the CMB temperature are standard, but matter's clocks — stars — ran ahead of the
expansion clock, so distant galaxies had more time to mature than $t(z)$. The configuration (a
time-like entity, a phenomenological slip, a dimension) is not worked out; this file asks only what
size such an effect needs and what bounds it. Data analysis, no derivation; untaken fork.
Numbers: `tests/clock_effect.py`.

## 1. What a clock effect is physically

A uniform speed-up of every matter clock (atoms, nuclei, stars) relative to the expansion is a
change of units and is unobservable — the "pure perspective" case. It becomes physics only as a
dimensionless mismatch between matter and gravity: $G$ measured in atomic units,
$G m_p^2/\hbar c$. The stellar clock is steep in it. Homology (pressure $\sim GM^2/R^4$, $T \sim GM/R$,
$L \sim T^4R/\kappa\rho$) gives main-sequence lifetimes $t \propto G^{-n}$ with $n = 4$ (massive stars,
electron scattering) to $n = 7.5$ (low-mass stars, Kramers opacity). A modest $G$ excess
therefore buys a lot of stellar time.

## 2. Size needed

For the ages of the 2026-11-13 claim (`08_zt_tcmb.md` §3), with the excess held over the galaxy's history:

| $z$ | ΛCDM age | wanted | speed-up | $\Delta G/G$ needed |
|---|---|---|---|---|
| 7.27 | 0.72 Gyr | 1.38 Gyr | ×1.9 | $+0.09$ to $+0.18$ |
| 14 | 0.29 Gyr | 0.96 Gyr | ×3.3 | $+0.17$ to $+0.34$ |

## 3. What bounds it

- **BBN:** $G$ at BBN over $G$ today $= 0.99^{+0.06}_{-0.05}$ (2σ; arXiv:1910.10730).
- **Recombination:** $G$ at recombination exceeds $G$ today by $< 0.19\%$ (95%, Planck + BAO, scalar–tensor;
  arXiv:1702.00742), $< 0.56\%$ (arXiv:1602.00809); $\pm 3\%$ (1σ) in an extended-quintessence model
  (arXiv:2101.11875). These assume a monotone $G(t)$. *Corrected 2026-11-13: an earlier draft quoted
  "1.5–6%" from a garbled abstract.*
- **Ring-down from a recombination-capped state** (the picture of 2026-11-13: convergence mostly
  stabilized by recombination, minor ring-down to $\approx 11$ Gly): with $\Delta G/G$ never above the
  recombination bound, the extra effective age at $z = 7.27$ is $< 11$ Myr (cap 0.2%), $< 33$ Myr
  (0.6%), $< 0.18$ Gyr (3%), all $n = 7.5$.
- **The CMB angular scale:** $H \propto \sqrt G$, so an excess $g$ at $3 < z < 15$ shortens the distance to
  last scattering: $-0.4\%$ for $g = 0.03$, $-1.3\%$ for $g = 0.1$, $-2.5\%$ for $g = 0.2$, against
  the CMB acoustic angle, known to $3\times10^{-4}$. Other parameters can absorb part of it; whether BAO at $z < 2.3$ lets
  them is a fit, not done.
- **v2 cannot supply it.** The circle sets $G$ together with $\alpha$ and $\mu$ (`07_exchange.md` §2),
  which quasar spectra fix far below 10%; the radion moves $G$ by $3\Omega^3\Delta\phi/\ell < 10^{-4}\Delta\phi/\ell$.
  A physical clock effect needs a new gravitational scalar — e.g. a scalar–tensor theory relaxing toward GR
  over cosmic time (the Damour–Nordtvedt attractor, the established form of "imperfect convergence that
  stabilizes" [verify: reference from memory]).

## 3a. A ring-down fitted (2026-11-13)

`tests/g_ringdown.py`: $G$ over $G$ today $= 1 + A\,e^{-p x}$ times an oscillation of period $\lambda$, with $x$ the e-folds since
recombination, $H \propto \sqrt G$, fitted to DESI DR2 BAO + the compressed CMB of `06` §4d (which does
not see $G$ *at* recombination; the bounds above do). Stellar speed-up is the mean of $G^n$ (in units of today's $G$) over the
time since recombination.

| $A$ at recombination | period (e-folds) | decay $p$ | $\Delta\chi^2$ vs ΛCDM | speed-up at $z = 7.27$ ($n = 4$, $7.5$) | at $z = 14$ |
|---|---|---|---|---|---|
| 0.03 | 1.5 | 0.5 | $+0.25$ | 1.004, 1.007 | 0.997, 0.995 |
| 0.1 | 1.5 | 0.5 | $+0.80$ | 1.012, 1.024 | 0.991, 0.985 |
| 0.3 | 1.5 | 0.5 | $+1.94$ | 1.041, 1.089 | 0.979, 0.980 |
| 0.3 | 0.5 | 1.0 | $-0.56$ | 0.999, 1.000 | 1.000, 1.003 |

(full grid in the script with `--full`). Even an amplitude of 30% at recombination — 50–150×
the published bound — buys at most 9% more stellar time by $z = 7.27$, because seven e-folds of
decay separate recombination from the galaxies, and swings average out. The galaxies need a
speed-up of ×1.9–3.3 (§2). A ring-down that starts at recombination cannot supply it, whatever
its period; what would is a $G$ excess of 10–30% *present at* $z \approx 7$–14.

## 3b. The per-galaxy probe (2026-11-13)

Type Ia iron is a $G$-clock as well as an age clock: the delay is the progenitor's lifetime
($\propto G^{-n}$) plus, for double white dwarfs, the gravitational-wave inspiral ($\propto G^{-3}$ at fixed
separation and masses). Iron above the core-collapse O/Fe ratio in a galaxy whose age is fixed by
its redshift therefore bounds $G$ — or the elapsed time — at that epoch. First data:
arXiv:2503.11457 (deep NIRSpec, 7 galaxies at $z = 9$–12) finds Fe enhancement in GS-z11-0 at $z = 11.12$,
$[\mathrm{O/Fe}] = -0.68^{+0.37}_{-0.55}$ ($\approx 2\sigma$ beyond solar), when the ΛCDM age is $\approx 0.4$ Gyr. The authors
explain it with pair-instability supernovae/hypernovae (first-generation very massive stars) or Type Ia
with a 30–50 Myr delay. The discriminator between those channels is the iron-peak pattern
(Mn, Ni, odd–even ratios) [verify: from memory], which integrated spectra at $z \approx 11$ do not yet resolve.

## 4. Reading

The clock version has the same shape of answer as the redshift version. A small effect is
allowed: tens to a few hundred Myr of extra stellar time at $z \approx 7$–14. The ~1 Gyr at $z \approx 14$
needs $G$ 17–34% high *after* recombination — larger than at recombination itself, so a bump rather
than a ring-down — and costs $\gtrsim 1\%$ in the CMB distance that would have to be absorbed elsewhere.
A side effect worth noting: a higher $G$ also speeds structure growth, which bears on the "too
massive, too early" side of the JWST question.

Tests specific to the clock version: chemical clocks (`ledger.md`: red-giant-branch light, Type Ia
iron) at $z \gtrsim 7$; the CMB + BAO fit with a $G(z)$ bump; time dilation of distant events is
*not* a test (a $G$ change leaves atomic clocks, hence redshift and time dilation, standard).
