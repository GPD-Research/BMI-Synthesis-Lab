# 04b — Initial conditions: which post-impact configurations give this universe

Milestone 5b. Script: `tests/scan_initial_conditions.py`. Companion to `04_impact.md`.

## 0. What is being scanned, and what is not

The question asked: *test configurations of the two manifolds before the collision and report
which produce a universe consistent with observation.* Two limits on what can honestly be done:

1. **The collision is not solved.** The matching through $\Omega = 1$ (`04_impact.md` §0) is open,
   so nothing here evolves a *pre*-collision state through the impact. What the impact hands the
   4D equations is a set of numbers; the scan is over those numbers.
2. **The action does not fix them.** The bulk + brane action is $\mathbb Z_2$-symmetric under
   $\Sigma_1 \to \Sigma_2$ and contains no CP-odd term, so it cannot produce an
   asymmetric energy split, a baryon number, or a sign. Whatever the two manifolds carried before
   the impact — energy, matter, antimatter — passes through as **initial data**. This is the
   statement in the last user note ("the other universe isn't symmetrical with ours necessarily")
   made precise: the *action* is symmetric, the *initial data* need not be.

So every survivor below is a *conditionally viable* configuration, not a prediction. The cost
column counts the initial data it needs; nothing in this file changes the ledger's balance
$0-7=-7$, and no configuration is adopted.

## 1. The post-impact initial-data space

In the $\Sigma_1$ frame, right after the impact reheats both branes:

| datum | meaning | maps to | fixed by action? |
|---|---|---|---|
| `r_b` | radion kinetic / radiation energy ratio | $\Omega_0$ by freeze-out (`04_impact.md` §1) | no — replaces $\phi_0$ (#3) |
| `f_2` | fraction of the radiation deposited on $\Sigma_2$ | $x = T_2/T_1 = (f_2/(1-f_2))^{1/4}$ | no — replaces $T_2/T_1$ (#7) |
| `\eta_1` | net baryon number per photon on $\Sigma_1$ | must be the observed $6.1\times10^{-10}$ | no — borrowed today (ΛCDM) |
| `\eta_2` | net baryon number per photon on $\Sigma_2$ | $\Omega_{DM}/\Omega_b$ if mirror baryons are the DM | no — **new** |
| `P_relic` | $\Omega_0\, m^{\mathrm{prop}}\, n / n_\gamma$ of a cold, non-thermal relic pre-loaded on $\Sigma_2$ that survived the impact | $\Omega_{DM}/\Omega_b$ if the relic is the DM | no — **new**, one product |
| content | $\Sigma_2$ = mirror SM (3+1), or a higher-dimensional/other sector carrying a cold relic, or empty | which of the two DM routes above is open | discrete choice, `01_action.md` §1 |

The **matter/antimatter sign** on each brane is a $\mathbb Z_2$ coin on each side. It is not scored
because nothing observable depends on it: charged fields are brane-localised (`02b_localization.md`),
so $\Sigma_2$'s matter cannot annihilate ours. "The Big Bang as a matter–antimatter annihilation"
therefore reads, in this model, as *each brane's* pre-loaded excess surviving *its own* annihilation
era: the plasma inherits the pre-loaded net number and no baryogenesis dynamics is needed on either
side. That is a simplification, and it is exactly why `\eta_1`, `\eta_2` are pure initial data.

A pre-loaded *thermal* energy density on $\Sigma_2$ is not a separate datum: once the impact
re-thermalises it, it is part of `f_2`. Pre-loaded *non-relativistic* matter that stays out of
equilibrium is `P_relic`.

## 2. Scores

| test | criterion | source |
|---|---|---|
| Cassini | $\Omega_0 < 0.032$; or $\Omega_0 < 10^{-4}$ (RS2 limit: $\Sigma_2$ at the horizon, no mirror sector) | `03_background.md` §1 |
| $N_{\text{eff}}$ | $\Delta N_{\text{eff}} < 0.3$ at BBN and CMB, warped mirror thresholds at $T_2/\Omega$, coarse $g_*$ [verify] | `04_impact.md` §2 |
| $\eta_B$ | $\eta_1 = 6.1\times10^{-10}$ — always satisfiable, always costs one datum | — |
| DM | $\Omega_{DM}/\Omega_b = 5.3 \pm 10\%$, or DM borrowed (flagged) | `04_impact.md` §3 |
| drift | $\lvert\Delta \ln m_{DM}\rvert < 0.05$ since recombination — satisfied by the bound on #4, not by initial data | `03_background.md` §3.1 |
| dissipative | mirror-baryon DM is atomic and dissipative; disk/Bullet-type bounds are milestone 6 — flagged, not scored | — |

## 3. Results (`tests/scan_initial_conditions.py`, section A)

| $\Sigma_2$ content | $\Omega_0$ | $x$ | $\Delta N_{\text{eff}}$ BBN / CMB | $\Omega_{DM}/\Omega_b$ | verdict | initial data |
|---|---|---|---|---|---|---|
| mirror SM, symmetric ($x=1$, $\eta_2=\eta_1$) — **the action's null** | 0.010 | 1.00 | 5.3 / 7.4 | 0.01 | dead | 4 |
| mirror SM, energy asymmetry only ($\eta_2=\eta_1$) | 0.010 | 0.44 | 0.20 / 0.28 | 0.002 | dead (DM) | 4 |
| mirror SM, energy + pre-loaded $\eta_2 = 6222\,\eta_1$ | 0.010 | 0.44 | 0.20 / 0.28 | 5.3 | **viable**, dissipative-DM flag | 4 |
| mirror SM, energy + pre-loaded $\eta_2 = 2588\,\eta_1$ | 0.032 | 0.40 | 0.16 / 0.19 | 5.3 | **viable**, dissipative-DM flag | 4 |
| mirror SM, $x = 0.6$, $\eta_2 = 2000\,\eta_1$ | 0.010 | 0.60 | 0.68 / 0.96 | 4.3 | dead ($N_{\text{eff}}$) | 4 |
| cold relic on $\Sigma_2$, `P_relic` $= 196\, m_p\eta_1$ | 0.010 | 0.30 | 0.05 / 0.06 | 5.3 | **viable** | 4 |
| cold relic, $x = 0.01$ (cold $\Sigma_2$), `P_relic` $= 5\times10^6\, m_p\eta_1$ | 0.010 | 0.01 | 0 / 0 | 5.3 | **viable** | 4 |
| $\Sigma_2$ present, no baryons | 0.010 | 0.30 | 0.05 / 0.06 | borrowed | viable, says nothing about DM | 3 |
| overshoot, $r_b > r_c$: no $\Sigma_2$ today (RS2) | 0 | — | 0 / 0 | borrowed | viable, says nothing about DM | 2 |

Section B of the script prints the $(x,\ \eta_2/\eta_1)$ map for the mirror-SM content. The viable
band is a thin diagonal: $\eta_2/\eta_1 \approx 5.3/(0.10\,\Omega_0\,x^3)$ up to the $N_{\text{eff}}$
wall at $x = 0.45$. The minimum asymmetry sits *on* that wall:

| $\Omega_0$ | `x_max` | $\eta_2/\eta_1$ needed at `x_max` | at $x=0.2$ | at $x=0.1$ |
|---|---|---|---|---|
| 0.032 | 0.449 | 1834 | 20 703 | 165 625 |
| 0.010 | 0.449 | 5869 | 66 250 | 530 000 |
| 0.003 | 0.449 | 19 562 | 220 833 | 1 766 667 |

## 4. Reading the map

**What works.** Three families produce this universe:

- **(i) Pre-loaded asymmetric mirror SM.** $\Sigma_2$ carries the mirror SM and arrives at the
  impact with a net baryon number $\eta_2 \approx (2$–$20)\times10^3\,\eta_1 \approx
  10^{-6}$–$10^{-5}$ per mirror photon, and takes less than $\approx 4\%$ of the impact energy
  ($f_2 < 0.04$, i.e. $x < 0.45$). It is viable, and it is the user's "pre-loaded manifold"
  picture made quantitative. Its price: `\eta_2` is a new datum, and because it enters as
  $\eta_2 x^3 \Omega_0$ it must be *tuned against* `f_2` and `r_b` to hit $5.3$ within 10% — the
  map's band is thin. Nothing in the action correlates the three. And the DM it delivers is
  30 MeV mirror hydrogen at $T_2 \approx 0.4\,T_1$: dissipative, atomic dark matter, which
  milestone 6 must confront with disk-thickness / Bullet-Cluster bounds (generically it can be at
  most a few % of the DM unless the mirror sector is much colder than $N_{\text{eff}}$ alone
  requires — see the $x=0.1$ column: then $\eta_2/\eta_1 \gtrsim 10^5$).
- **(ii) Cold relic on $\Sigma_2$.** Any stable, non-thermal remnant of the other manifold that
  survived the impact with $\Omega_0 m^{\mathrm{prop}} n/n_\gamma \approx 200\,m_p\eta_1$
  (at $x=0.3$). Viable for *any* $x$, with no dissipative flag if the relic is not atomic. Price:
  one product datum `P_relic` that the action does not produce, and a $\Sigma_2$ content that is
  not the mirror SM (exit (a)/(b) of `04_impact.md` §3). This is generic — it has no BMI content
  beyond the $\Omega_0$ factor in the mass.
- **(iii) No mirror dark matter.** $\Sigma_2$ empty of baryons, or gone (RS2 overshoot). Cheapest
  (2–3 data), passes everything, and says nothing about dark matter (exit (e)).

**What does not work.** The action's own null configuration (symmetric impact, symmetric
baryon number) is dead on $N_{\text{eff}}$ and on DM simultaneously. Energy asymmetry alone fixes
$N_{\text{eff}}$ and leaves DM short by $\sim 3000$. There is no configuration in which the
mirror SM is the dark matter *without* a pre-loaded asymmetry $\eta_2 \gg \eta_1$; the higher-
dimensional fallback for $\Sigma_2$ does not change this unless it carries a cold relic (family ii).

**What this is not.** No row is a prediction. Families (i) and (ii) each need exactly one
number the action cannot produce (`\eta_2` or `P_relic`), on top of the two the impact already
left undetermined (`r_b`, `f_2`) and the one we borrow (`\eta_1`). Relative to the ledger, taking
(i) or (ii) would be **+1 parameter** (#8), with #3 and #7 re-labelled as initial data rather
than constants. Neither is taken here.

## 5. What would make one of these a derivation rather than a choice

- A pre-collision solution for $\Sigma_2$ (a static or slowly rolling brane in the AdS$_6$ slice
  with its own thermal history) that *fixes* its energy content and net charge at the moment of
  impact. Then `f_2` and `\eta_2` would be outputs. This requires the matching through $\Omega=1$.
- A reason the three data are correlated ($\eta_2 x^3 \Omega_0 \approx 53$): e.g. if the impact
  energy split and the radion kick are both set by a single collision velocity, `r_b` and `f_2`
  collapse to one number. That is a kinematic calculation on the fixed action, not a new
  parameter, and is the first thing to try when the matching is available.
- Milestone 6 bounds on dissipative mirror DM: if they exclude family (i) at $x$ near $0.45$,
  the mirror-SM route survives only with $\eta_2/\eta_1 \gtrsim 10^5$ and a cold $\Sigma_2$.

## 6. Approximations carried [verify]

Coarse step-function $g_*$ for the mirror thresholds (`04_impact.md` §2); equal $g_*$ on both
sectors at the impact when converting `f_2` to $x$; freeze-out of $\Omega_0$ in pure radiation
(`04_impact.md` §1); 10% tolerance on $\Omega_{DM}/\Omega_b$ stands in for the full ΛCDM fit.
