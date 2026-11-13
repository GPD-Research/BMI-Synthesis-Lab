# 08 — The $z_t$ fork against the source-frame CMB temperature (first look)

Data analysis, no derivation: $z_t$ has no mechanism in the action (`ledger.md`, fork row) and
stays an untaken fork. Question: how large can a non-expansion redshift be, given the CMB
temperature measured *at* distant sources? Numbers: `tests/zt_tcmb.py`; data
`tests/data/tcmb_z.csv` (47 points, sources in its header).

The fork, $1+z_{\text{obs}} = (1+z_{\text{exp}})(1+z_t)$, puts the CMB at the source at $T_0(1+z_{\text{exp}})$,
so each measurement gives $1+z_t = T_0(1+z_{\text{obs}})/T$ directly, independent of any
time–distance model.

| data | $z$ | role |
|---|---|---|
| FIRAS | 0 | $T_0$ |
| SZ: Luzzi 2009 (13 clusters), Hurier 2014 (Planck stack, 18 bins) | 0.02–0.97 | the nearby, "smooth" region |
| molecular/atomic absorbers: Muller 2013 (PKS 1830−211), Klimenko 2021 (CO, C I; supersedes Noterdaeme 2011 for the same systems), older C I/C II | 0.89–3.29 | the "accurate at long distance" region |
| HFLS3 water absorption, Riechers 2022: $16.4$–$30.2$ K (1σ) | 6.34 | the only point in the "very long distance" region |

## Results

| shape of $\ln(1+z_t)$ | best fit | 2σ ceiling |
|---|---|---|
| none (ΛCDM) | $\chi^2 = 31.8$ / 47 | — |
| power, $\beta\ln(1+z)$ | $\beta = +0.008$, $\chi^2 = 31.4$ | $\beta < 0.034$; $z_t < 7\%$ at $z = 6.34$ |
| threshold at $z_{\text{th}} = 1.3$ (≈ 9 Gly lookback) | $A < 0$ (no signal) | $z_t < 5\%$ at $z = 2.5$, $< 15\%$ at $6.34$ |
| threshold at $z_{\text{th}} = 3$ | no signal | $z_t < 0.91$ at $z = 6.34$ — set by HFLS3 alone |

Extra age the temperature data allow (2σ):

| $z_{\text{obs}}$ | ΛCDM age | threshold 1.3 | threshold 3 |
|---|---|---|---|
| 2.5 | 2.61 Gyr | +0.20 Gyr | 0 (no data above, by construction) |
| 6.34 | 0.86 Gyr | +0.20 Gyr | up to +1.4 Gyr |
| 14 (extrapolated) | 0.30 Gyr | +0.12 Gyr | up to +2.1 Gyr |

**Reading.** No sign of $z_t$ anywhere. If the drift switches on near 9 Gly, as first stated,
the absorbers at $z \approx 1.7$–$3.3$ already cap it at a few percent and the extra time at about
200 Myr — not the ~1 Gyr a mature spiral at $z \sim 14$ would need. If it switches on only past
$z \approx 3$, the data say almost nothing: one measurement (HFLS3) carries the whole constraint and
still allows over a Gyr. That is where the test lives, and it is a data-starved regime.

## What would decide it

1. More source-frame temperatures at $z > 4$: CMB-pumped water/CO absorption in other dusty
   starbursts (the HFLS3 method), and [C I]/CO excitation in JWST/ALMA-era systems.
2. The chemical-clock per-galaxy test of the ledger row (red-giant-branch light, Type Ia iron),
   with the temperature measured in the same galaxy.
3. Not done here, owed before any claim: DESI Ly$\alpha$ BAO at $z \approx 2.3$ and distance duality,
   which constrain $z_t$ through distances rather than temperature. A $z_t$ that only switches on
   past $z \approx 3$ also escapes most of these.

Caveats: the absorber temperatures depend on collisional and UV-pumping corrections
(Klimenko's model); HFLS3 is a 1σ range entered as a Gaussian; Luzzi and Hurier are both SZ and
partly overlap in clusters. None of this changes the order of magnitude.

## 3. Pre-registered claim (2026-11-13)

Registered before any new data, so the threshold cannot later move to wherever the data are
thin. Nothing here is fitted to the temperatures; the amplitude is fixed by the galaxy-age motivation alone.

$$
\ln(1+z_t) = A\,\max\!\left(0,\ \ln\frac{1+z}{1+z_{th}}\right),\qquad
z_{th} = 3,\qquad A = \frac{\ln 2.2}{\ln(15/4)} = 0.597 ,
$$
i.e. no drift out to $z = 3$ ($\approx 11.5$ Gly lookback), and $1+z_t = 2.2$ at $z = 14$, the size
that gives a $z_{\text{obs}} = 14$ galaxy about 1 Gyr. Range of the claim: $3 \le z \le 15$. The curve
cannot continue to $z \approx 1100$ unchanged (it would move recombination); its saturation above
$z \approx 15$ is unspecified and owed, and the CMB acoustic scale will bound it.

| $z_{\text{obs}}$ | $z_t$ | CMB temperature at the source: ΛCDM → claim | time since the Big Bang: ΛCDM → claim |
|---|---|---|---|
| 4.62 | 0.22 | 15.3 → 12.5 K | 1.29 → 1.74 Gyr |
| 6.34 | 0.44 | 20.0 → 13.9 K | 0.86 → 1.49 Gyr |
| 7.27 | 0.54 | 22.5 → 14.6 K | 0.72 → 1.38 Gyr |
| 10 | 0.83 | 30.0 → 16.4 K | 0.47 → 1.16 Gyr |
| 14 | 1.20 | 40.9 → 18.6 K | 0.30 → 0.96 Gyr |

Today's data: $\Delta\chi^2 = +1.85$ against ΛCDM, carried entirely by HFLS3 (claim 13.9 K vs 16.4–30.2 K
at 1σ): mildly disfavoured, allowed. **Kills:** (i) any source-frame temperature at $z > 4$ that
excludes the claimed value at $3\sigma$; (ii) two or more such measurements each at $2\sigma$; (iii) a
galaxy at $z > 4$ whose chemical clock (`ledger.md`: red-giant-branch light, Type Ia iron) is young
while its temperature matches ΛCDM is neutral, but a ΛCDM-temperature galaxy with an old clock
kills the claim and points to astrophysics. **Confirms** (not decides): a temperature deficit of
the claimed size at $z > 4$ in two independent systems, with the same galaxy's clock agreeing.
Natural first target: the quiescent galaxy RUBIES-UDS-QG-z7 at $z = 7.27$ (arXiv:2606.21361), where
the claim gives 14.6 K and 1.38 Gyr instead of 22.5 K and 0.72 Gyr.
