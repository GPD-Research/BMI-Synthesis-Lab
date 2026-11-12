# BMI v2 — Parameter Ledger (live)

Every quantity that v2 needs from outside the action is listed here. `tests/check_ledger.py`
fails CI if a symbol declared as a parameter appears in `v2/*.md` without a row in the table
below, or if the number of rows exceeds the budget.

**Budget: 9 parameters, 0 free functions.** (ΛCDM: 6. SM: 19.) Raised from 7 in milestone 5d
(circle stabilizer, `04d_circle.md` §3) and from 8 in milestone 6 (dark-matter misalignment,
`05_dark_sector.md` §2); every raise is logged here.

**FROZEN at 9 (2026-09-21, after milestone 7).** No row #10 is admitted except under the provisional-tenth rule below:
a result that needs a tenth number is a forced miss and goes to `RETRACTED.md`. No new derivation
milestone opens until P1 or P2 below is tested — an inverse-square-law measurement at
$3$–$13\,\mu$m, or the chain-level DESI DR2 comparison. Permitted meanwhile: closing `[verify]`
items, corrections that do not add symbols, and confronting P1/P2 with new data.

**Provisional tenth (2026-11-11, after P2 was killed).** The freeze is lifted for **one** provisional
tenth number, under these rules, decided before any calculation on it:
1. *Candidate:* inter-brane energy exchange (fork below), the only one-number route in this geometry
   to an effective $w < -1$. It is registered here, with its derivation target and kill tests, before
   it is computed.
2. *Admitted* only if it fixes or predicts at least one of the nine — a row moves from "open" to
   "derived", or a new relation ties existing rows. Only then does it get a Parameters row, count
   toward the budget, and feed predictions. (The expectation is two or three; that is a hypothesis.)
3. *Paused*, not rejected, if it fits but connects to none of the nine. A paused number stays on
   record with its derivation and kill tests, is **not** assumed, gets no Parameters row, and nothing
   downstream (predictions, other derivations, the balance) may use it. It is re-opened if a later
   result elsewhere in the theory maps onto it.
4. *Dead* only by data: a kill test below fails, admitted or paused. Failing to connect alone never
   kills it, and pausing never shields it from a kill.
5. The budget stays 9 until rule 2 is met.

Discrete choices (not parameters), all recorded with alternatives in `01_action.md`: Fork 1
(we are the UV brane); one compact bulk direction; exponential bulk potential; mirror Standard
Model on $\Sigma_2$ (**as the dark matter: dead**, `04_impact.md` §3 — it still exists as a
subdominant sector); $\Phi$-independent tensions.

Ledger balance = (un-fitted numerical predictions confirmed) − (parameters). Update the
balance line whenever a row or a prediction changes.

## Parameters

Symbol column is the exact LaTeX macro as it appears in the manuscript, without `$`.

| # | symbol | meaning | fixed by | status |
|---|---|---|---|---|
| 1 | `M_5` | effective 5D Planck mass, $M_5^3 = \pi\ell_z M_6^4$ | $G_N$ with #2, #3 | open |
| 2 | `\ell` | bulk warp length; fixes $\Lambda_6$ and the RS-tuned $\sigma_1$ | $G_N$ with #1, #3 (the CC tuning is stated in `01_action.md` §3, not hidden) | open |
| 3 | `\phi_0` | present brane separation | $M_{Pl}^2 = \tfrac13 M_5^3 \ell (1-e^{-3\phi_0/\ell})$: one relation among #1–#3; Cassini requires $\phi_0/\ell \gtrsim 3.4$ (`03_background.md` §1); equals the image of the post-impact kinetic ratio $r_b$ in the moduli approximation (`04_impact.md` §1); in the exact two-brane solution $r_b$ does not exist and $\Omega_0^3 = (\epsilon - f)/(1+\epsilon)$ from the collision data, with Cassini requiring $\epsilon - f \lesssim 3\times10^{-5}$ (`04c_approach.md` §2, §4; coincidence sharpened) | bounded |
| 4 | `\sigma_2` | tension of $\Sigma_2$; only the detuning $\delta\sigma_2 = \sigma_2 + \sigma_1$ is physical | $\lvert\delta\sigma_2\rvert < 0.15\,\rho_0/\Omega_0$ (DM-mass drift); sign not fixed by the impact (`04_impact.md` §5) | bounded, sign open |
| 5 | `V_0` | bulk potential scale | dark-energy density today | open |
| 6 | `c` | bulk potential slope | $w_0, w_a$ **and** $\dot\phi$; one number, two observables | open |
| 7 | `T_2/T_1` | sector temperature ratio at reheating | **not derivable**: the action is $\mathbb Z_2$-symmetric at the collision, so its null value is 1, which gives $\Delta N_{\text{eff}} \approx 6$ (excluded); bounded $< 0.45$ by the CMB (`04_impact.md` §2) | bounded, null excluded |
| 8 | `\delta_1` | detuning of $\sigma_1$ from its RS value, $\delta_1 < 0$; stabilizes the circle against the SM Casimir repulsion (`04d_circle.md` §3); taken milestone 5d | $\ell_z^5 = 4C_{\rm SM}/\pi\lvert\delta_1\rvert$; Eöt-Wash at the computed $\alpha_Y \approx 120$ (`06_predictions.md` §4a; supersedes 5d's $\alpha = 1$ edge) and $\lvert\delta_1\rvert < \sigma_1$ give $13\ \mathrm{TeV} < \ell_z^{-1} < 29\ \mathrm{TeV}$; the $-(3\ \mathrm{TeV})^4$ vacuum energy at the minimum is absorbed in the $\Lambda_6$ retuning of #2 | bounded two-sided |
| 9 | `\delta_z` | fractional offset of the circle from its minimum left by the impact, $\ell_z^{\rm(impact)} = \bar\ell_z(1+\delta_z)$; the misalignment that makes the oscillating circle the dark matter (`05_dark_sector.md` §2); taken milestone 6 | $\Omega_\chi = \Omega_{DM}$: $\delta_z \approx 3\times10^{-6}(T_R/T_o)^{3/2}$; spatially uniform to $5\times10^{-6}$ (Planck $\beta_{\rm iso}$) | fitted to $\Omega_{DM}$; sign irrelevant |

## Pending integration constants (not parameters yet)

| symbol | meaning | must be computed in | bound now |
|---|---|---|---|
| `\mathcal C` | dark-radiation constant, $\rho_E = \mathcal C/a^4$; the Schwarzschild–AdS bulk mass | **re-opened, milestone 5c**: emission drives it to $\rho_E/\rho_{\text{rad}} \to \alpha/4 \approx 5\times10^{-3}$ (`04_impact.md` §4), but the exact two-brane solution requires $\epsilon \ge f$ — the collision must already deposit at least as much bulk mass as $\Sigma_2$ energy (`04c_approach.md` §3) — so it is collision data, not an emission output; $\Delta N_{\text{eff}}$ from $\rho_E$ is at least that of the mirror sector | bounded below by $f$, above by $N_{\text{eff}}$ |
| `c_\nu` | universal bulk mass of bulk gauge singlets (`02b_localization.md` §6); only admitted as *one* number for all species | taken only if a neutrino-sector milestone is opened | none yet |
| `\eta_2` or `P_relic` | pre-loaded net baryon number (mirror SM) or cold-relic abundance on $\Sigma_2$ — the one number that makes mirror-side dark matter viable (`04b_initial_conditions.md` §4) | **not taken**: milestone 6 chose the oscillating circle; $\Sigma_2$ matter must be subdominant | $\eta_2/\eta_1 \approx 2\text{–}20\times10^3$ or `P_relic` $\approx 200\,m_p\eta_1$ |
| (fork, not a symbol) | a feature in $V(\Phi)$ — bump or negative minimum — that would end acceleration via the dark-energy scalar (`03_background.md` §3.4); one shape choice + 1 scale | milestone 7's proxy test (`06_predictions.md` §4b) left the exponential outside $2\sigma$ but not dead; taken only if the chain-level test kills it. *2026-11-11: the chain test killed it* (`06` §4c); still not taken — the registered first step is menu item (a)/(b) of `01_action.md` §2.1, and the decision is open | — |
| (fork, not a symbol) | **inter-brane energy exchange** (from the 2T+5S sketch, 2026-11-11): a coupling that lets $\Sigma_1$ matter or vacuum energy flow into the bulk/$\Sigma_2$. The only consistent route in this geometry to an effective $w$ crossing $-1$, which P2 forbids. Price: one coupling (+1, so it would be a tenth number; under the freeze rule it can be taken only if that rule is revisited). Kill: the exchange feeds $\mathcal C$, so $\Delta N_{\text{eff}}$ and the $\rho_E$ bound above must hold with a time-dependent $\mathcal C$; dark-matter dilution must stay $a^{-3}$ within CMB/LSS limits | second P2 fallback, after the $V(\Phi)$ feature; considered only if the chain-level test kills thawing **and** the DESI posterior prefers a crossing. *2026-11-11: thawing killed; the CPL posterior prefers a crossing at $\gtrsim 2.5\sigma$ (chain-resolution limit), not established* | **dead** (2026-11-11, `07_exchange.md`): the only channel with leverage is a $\Phi$-dependent DM mass, which the stabilizer locks to the circle ($d\ln m_\chi = -3\,d\bar\sigma$), so quasar $\mu$/$\alpha$ bounds cap the exchange at $\lvert\Delta w\rvert < 10^{-8}$; fixes none of the nine |
| (fork, not a symbol) | **relative velocity of $\Sigma_2$ matter at the impact** (from the 2T+5S "brane shear", 2026-11-11): sliding of tension-only branes is pure gauge, so the physical remnant is a bulk flow of $\Sigma_2$ content set by the collision (+1 collision datum unless computed from $\epsilon, f, h$); a candidate source of a low-$\ell$ CMB axis. Kill: CMB bounds on anisotropic expansion at decoupling; it cannot also explain an $H_0$ anisotropy (an $a^{-6}$ term visible today would dominate BBN) | inert until the action gives a primordial spectrum (`04_impact.md` §6) | not taken |
| (fork, not a symbol) | **non-expansion redshift** (the 2T+5S "timeline offset", restated in one time, 2026-11-11): observed redshift $= (1+z_{\text{exp}})(1+z_t) - 1$ with $z_t \to 0$ nearby and growing at large distance, so distant objects are older than the age inferred from the observed redshift. The time and distance versions are one claim, because $z_t$ shifts both maps. No mechanism in the action: a free function, not admissible as physics until the geometry produces it. Its curve is read from data, not fitted to it: the CMB temperature measured *at the source* (line excitation, SZ) gives $1+z_t$ directly as the ratio of the FRW temperature at the observed redshift to the measured one; stellar-population ages are a model-dependent lower bound. Kill: the source-frame CMB temperature at $z \sim 2\text{–}3$ (few-% precision), DESI Ly$\alpha$ BAO at $z \approx 2.3$, distance duality. Sharp per-galaxy test (2026-11-11): chemical clocks that no massive-star channel can shortcut — red-giant-branch light (low-mass stars, $\gtrsim 1$ Gyr) and Type Ia iron (Fe above the core-collapse O/Fe; hard floor $\sim$40–100 Myr, bulk $\sim$1 Gyr); not red supergiants or core-collapse/r-process elements, which appear within $\sim$10–30 Myr. It bites only where the FRW age is $\lesssim 0.5$ Gyr ($z \gtrsim 10$). Two-sided: the clock's minimum age and the source-frame CMB temperature of the *same* galaxy each give $z_t$ and must agree; an old clock with the FRW temperature kills $z_t$ and points to astrophysics | data compilation, no derivation | not taken |
| (fork, taken as #8) | **circle stabilizer** (`04d_circle.md`): of the menu, the terms already in the action fail (minimum at meV, $\alpha$ tracks dark energy); flux costs 2 numbers + a field; Goldberger–Wise needs codimension-2 branes. Casimir + $\delta_1$ taken. Milestone 6 took the oscillating-circle DM family: `T_R` is **not** a parameter (the thermal route is closed, `05_dark_sector.md` §1) but is bounded, $T_R < T_o \approx 2.7$ TeV, i.e. $h < 0.07$ at the impact; the tuned number is `\delta_z` (#9) | taken | $T_R < T_o$ |
| (fork, not a symbol) | **unified sector at coincidence** (`00_axiom.md`, pre-action layer): at $\Omega = 1$ the branes coincide and one gauge group $G_U \supset$ SM × mirror lives on the merged brane, splitting into the two sectors as they separate. Would give cross-sector annihilation during overlap, and a vacuum-level (not action-level) $\mathbb Z_2$ breaking that could produce $T_2 \ne T_1$, $\eta_2 \ne \eta_1$. Price: one discrete choice ($G_U$ and its breaking pattern) + the overlap duration. Kill: must reproduce SU(3)×SU(2)×U(1) with the observed chiral content on $\Sigma_1$ and keep $\Sigma_2$ dark today; must give $\Delta N_{\text{eff}} < 0.3$ and $\eta_1 = 6\times10^{-10}$ without a hidden efficiency function; must not reintroduce a bulk gauge field (`02b_localization.md`) | taken only if the 5b families all die in milestone 6, or if a computable $G_U$ is exhibited; not taken | — |

Milestone 5 computed `\mathcal C`; milestone 5c re-opened it as collision data and found the
circle modulus unstabilized; milestone 5d stabilized it at the cost of #8; milestone 6 made
its oscillation the dark matter at the cost of #9. Budget 9.

## Borrowed (not counted, not derived)

$G_N$, $\hbar$, $c$, ΛCDM's six parameters, the Standard Model on $\Sigma_1$.

## Symbols exempt from the check

Coordinates, indices, fields and derived quantities are not parameters. The check-script
allowlist lives in `tests/ledger_allowlist.txt`; add to it only for fields and derived
quantities, never for a new constant.

## Predictions (un-fitted, pre-registered)

| # | quantity | predicted value | data | status |
|---|---|---|---|---|
| P1 | Yukawa force from the circle modulus, strength and range both from the action (`04d_circle.md` §3c registered 2026-09-20 as a window; strength and normalisation computed in `06_predictions.md` §1–2, 2026-09-21; strength corrected 2026-11-11, `06` §2a) | $\alpha_Y = 2\beta^2 = 120$–$130$, spread $110$–$150$ (QCD running of $1/g_s^2 \propto \ell_z$ through the thresholds to $\Lambda_3$; composition-independent to $10^{-3}$), $\lambda = m_\chi^{-1}$ with $2.8\,\mu\mathrm m < \lambda < 13\,\mu\mathrm m$ ⇔ $13 < \ell_z^{-1}/\mathrm{TeV} < 29$ | Eöt-Wash 2020 removed $\lambda > 13\,\mu$m at this strength (`06` §4a); current limits $1$–$3\times10^3\times$ above the segment | open — a detection on the segment confirms; off it, or a null to $\alpha \sim 10^2$ at $3\,\mu$m, kills the fixed circle |
| P2 | thawing dark energy, $w_a = -1.5\,(1+w_0)$ at small $c$ ($-1.15$ at $c = 1.8$), $w > -1$ at all $z$ (`03_background.md` §2, registered as a prediction in `06_predictions.md` §4b, 2026-09-21) | one relation among $(w_0, w_a)$; $V_0, c$ fix three observables | DESI DR2 chains (BAO + CMB, alone and + Pantheon+/Union3/DESY5): curve outside the 95% region for every $c$ — $98.1\%$ to $>99.8\%$ (`06` §4c, 2026-11-11); ΛCDM as far or farther; direct fit without the projection (`06` §4d): BAO + CMB best $c = 0$, $\Delta\chi^2 = 8.35$ from CPL | **killed** — `01_action.md` kill criterion 2 fired; `RETRACTED.md` N4 |

Constraints derived so far (not predictions; they use data to bound the ledger):
$\phi_0/\ell \gtrsim 3.4$ (Cassini); $|\dot G/G| \lesssim 3\times10^{-16}\,\mathrm{yr}^{-1}$ forced by the DM-mass drift bound (`03_background.md` §3.1)
(passes LLR); $\rho^2$ Friedmann corrections only above $T_t \approx 6$ TeV for $\ell = 10\,\mu$m
(table-top $\ell$ bound); $T_2/T_1 < 0.45$ (CMB $N_{\text{eff}}$).
Forced consequence, tested and failed (`04_impact.md` §3): mirror-sector masses are $\Omega m$
with $\Omega \lesssim 0.032$, so $\Omega_{DM}/\Omega_b = 5.3$ needs $\eta_2/\eta_1 \gtrsim 1600$;
the action has no mechanism — mirror SM is not the dark matter.
Initial-condition scan (`04b_initial_conditions.md`): the action's null configuration is dead; every
viable configuration with mirror-side dark matter needs one pre-loaded datum (`\eta_2` or `P_relic`)
tuned against `r_b`, `f_2`; configurations without mirror DM pass and say nothing.

## Balance

**0 − 9 = −9.** Milestone 3 passed kill criterion 1 (GR + ΛCDM recovered) without changing
the balance. Milestone 5 kept $\mathcal C$ out of the budget (computed, $\Delta N_{\text{eff}}
\lesssim 0.03$ — a confirmed un-fitted *bound*, not a confirmed prediction, so it does not
count) and closed the mirror-DM branch. Milestone 5d spent #8 on the circle and registered
the first falsifiable prediction (P1, a fifth force in a two-sided range window); it counts
only if found. Milestone 6 spent #9 on the dark-matter misalignment and added no prediction
(its phenomenology is CDM's; its only handle is P1). Milestone 7 (`06_predictions.md`) computed
P1 to a strength and range (a segment in the $(\alpha,\lambda)$ plane, half of `04d`'s range
already removed by Eöt-Wash 2020), registered P2, and found that the Cassini–$N_{\text{eff}}$,
$\dot G/G$–$w$, and GW-distance relations leak or are null. **Neither prediction is confirmed: the
balance did not move.** By the rule above the branch closes; the proposal in `06` §5 is to freeze
the budget at 9 and wait for the two tests rather than derive further. **Decision taken
2026-09-21: frozen at 9** (banner above). The branch is not closed; it is suspended pending P1/P2.
