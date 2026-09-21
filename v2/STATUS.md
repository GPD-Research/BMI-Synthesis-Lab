# v2 status — after milestone 6

One page. What is fixed, what is derived, what is still open, what could kill it next.
Details and derivations live in the numbered files; this only points.

## 1. The Lagrangian (fixed, `01_action.md` §2)

$$
S = \int d^6X \sqrt{-G}\left[\tfrac{M_6^4}{2} R_6 - \Lambda_6 - \tfrac12 (\partial\Phi)^2 - V(\Phi)\right]
+ \sum_{i=1,2} \int_{\Sigma_i} d^5\xi \sqrt{-\gamma_i}\left[-\sigma_i + \mathcal L_{\text{matter},i}\right]
+ M_6^4 \sum_i \int_{\Sigma_i} [K_i],
\qquad
V(\Phi) = V_0\, e^{-c\,\Phi/M_6^2}.
$$

Matter on $\Sigma_1$ = Standard Model, on $\Sigma_2$ = mirror Standard Model **[choice]**. No free
functions. Nothing in milestone 3 changed this action; milestone 3 changed the *solution* of it
(background metric, §3 below). A "revised Lagrangian" is therefore not needed — what is still
missing is its *effective 4D form* (§4).

## 2. Parameter budget (7, `ledger.md`)

$M_5,\ \ell,\ \phi_0,\ \sigma_2,\ V_0,\ c,\ T_2/T_1$. Balance $0 - 7 = -7$: no un-fitted
number has been predicted yet. The dark-radiation constant $\mathcal C$ is collision data
bounded below by the $\Sigma_2$ energy (milestone 5c), not a parameter; $\phi_0$ is fixed by
the collision data $(\epsilon, f)$ (`04c_approach.md`), with `r_b` of milestone 5 as its
moduli-approximation shadow;
$T_2/T_1$ is not derivable from the action (its $\mathbb Z_2$-symmetric null value 1 is
excluded) and stays a parameter, bounded $< 0.45$.

## 3. Derived so far (`02_effective_4d.md`)

| item | status |
|---|---|
| background metric $ds^2 = e^{-2y/\ell}(\eta_{\mu\nu}dx^\mu dx^\nu + dz^2) + dy^2$, $\ell^{-2} = -\Lambda_6/10M_6^4$ | verified symbolically (`tests/check_background.py`) |
| brane tensions $\sigma_1 = 8M_6^4/\ell = -\sigma_2$ | verified |
| $M_{Pl}^2(\phi) = \tfrac13 M_5^3 \ell\,(1 - e^{-3\phi/\ell})$ | verified |
| $\dot G/G \approx -(3\dot\phi/\ell)\,e^{-3\phi/\ell}$ | derived; $\lesssim 3\times10^{-16}\,\mathrm{yr}^{-1}$ once the DM-mass drift bound is imposed — **kill criterion 2 passed** |
| brane field equation $G_{\mu\nu} = 8\pi G_N T_{\mu\nu} + (8\pi G_N/\sigma_1)\hat\pi_{\mu\nu} - E_{\mu\nu} + \Theta_{\mu\nu}$ | structure derived; $D=6$ coefficients of $\hat\pi$ **[verify]** |
| GR + ΛCDM recovered for $\dot\phi \to 0$, low energy | yes — **kill criterion 1 passed** |
| Brans–Dicke $\omega = \tfrac43(e^{3\phi/\ell}-1)$; Cassini: $\phi_0/\ell \gtrsim 3.4$, $\Omega_0 \lesssim 0.032$ | derived in 6D (`03_background.md` §1, `tests/check_radion.py`) |
| radion $K(\phi) = 12M_{Pl}^2\Omega^3/\ell^2$, canonical $\chi \propto \Omega^{3/2}$, $\epsilon_\chi = 2/3\Omega^3$ | derived: the radion never slow-rolls |
| bulk scalar: no static profile; rolling zero mode is canonical quintessence $V_* e^{-c\Phi_4/M_{Pl}}$ with slope exactly $c$ | derived (`03_background.md` §2) |
| thawing $w(z)$ family in $c$; $w>-1$, $w_a<0$; $w_a \approx -1.5(1+w_0)$ | computed (`tests/background_frw.py`) |

Two errors in `01_action.md` were found and corrected in place (unwarped circle was not a
vacuum solution; $M_{Pl}$ exponent was the 5D one). Both are recorded in `02_effective_4d.md` §0.

## 4. The effective 4D Lagrangian (now closed, `03_background.md`)

$$
S_{\text{eff}} = \int d^4x\sqrt{-g}\left[\tfrac{M_{Pl}^2(\phi)}{2}R - \tfrac{K(\phi)}{2}(\partial\phi)^2 - \delta\sigma_2^{(5)}\Omega^4
 - \tfrac12(\partial\Phi_4)^2 - V_* e^{-c\Phi_4/M_{Pl}}\right] + S_{SM}[g] + S_{\text{mirror}}[\Omega^2 g]
$$

with $M_{Pl}^2(\phi) = \tfrac13 M_5^3\ell(1-\Omega^3)$, $K = 12M_{Pl}^2\Omega^3/\ell^2$,
$V_* = \pi\ell_z\ell V_0/5$, $\Omega = e^{-\phi/\ell}$. Two scalars, not one: the radion $\phi$
(merger) and the bulk scalar $\Phi_4$ (dark energy). Outside it: $E_{\mu\nu} = \mathcal C/a^4$
with $\mathcal C$ now fixed to $\rho_E/\rho_{\text{rad}} \lesssim 5\times10^{-3}$
(`04_impact.md` §4) and the order-$\ell^2 R^2$ corrections.

**Background result.** The CMB bound on mirror-DM mass drift forces the radion's energy
fraction today to $f_{\text{rad}} < 5\times10^{-6}$: the merger is a spectator, dark energy is
the bulk scalar alone, and "dark energy = inter-brane potential" (v1 Ch 7.4) is dead
(`03_background.md` §4).

## 5. Forced consequence found (the first real kill risk)

$\Sigma_2$ sits at the IR end of the warp, so every mirror-sector mass is
$\Omega\, m$ with $\Omega = e^{-\phi/\ell} \lesssim 0.032$:

- mirror proton $\lesssim 30$ MeV, mirror electron $\lesssim 16$ keV;
- $\Omega_{DM}/\Omega_b = 5.3$ then requires $n_2/n_1 \gtrsim 165$ — the impact must
  deposit far more baryon number on $\Sigma_2$ than on $\Sigma_1$;
- DM masses drift with $\phi(t)$; CMB requires $|\Delta\phi| \lesssim 0.03\,\ell$ since
  recombination, i.e. the merger is essentially stalled over the last 13.8 Gyr —
  milestone 4 shows the action *can* satisfy this (radion spectator, §4) but it does not
  *predict* it: $|\delta\sigma_2|$ small enough is a condition on parameter #4.

This is not generic mirror-matter phenomenology; it is what BMI + Fork 1 forces. **Milestone 5
result: it fails.** With $T_2/T_1 < 0.45$ (CMB $N_{\text{eff}}$; the warped mirror $e^\pm$ stay
relativistic through BBN) and separate entropy histories,
$\Omega_{DM}/\Omega_b \approx 0.10\,\Omega_0\,\eta_2/\eta_1$, so the observed 5.3 needs a
mirror baryon asymmetry $\eta_2/\eta_1 \gtrsim 1600$ that nothing in the action produces
(`04_impact.md` §3). The mirror SM is not the dark matter. The pre-registered fallback
(higher-dimensional $\Sigma_2$) does not fix it — the missing factor is $\Omega_0$ in the
mass, not the equation of state. Exits with their prices are tabulated in `04_impact.md` §3;
the two honest ones are (c) a collision-driven asymmetry (a mechanism the action lacks;
proposed milestone 5b) or (e) BMI is silent on dark matter. **Decision pending.**

**Milestone 5b (initial-condition scan, `04b_initial_conditions.md`).** The action is
$\mathbb Z_2$-symmetric at the impact, so the two manifolds' pre-collision content passes through
as initial data (`r_b`, `f_2`, `\eta_1`, `\eta_2` or `P_relic`); those were scanned and scored
against Cassini, BBN/CMB $N_{\text{eff}}$ and $\Omega_{DM}/\Omega_b$. The action's null
configuration is dead. Viable families: (i) mirror SM pre-loaded with
$\eta_2 \approx (2\text{–}20)\times10^3\,\eta_1$ and $< 4\%$ of the impact energy — the
"pre-loaded manifold" picture, viable but tuned to a thin band and delivering dissipative 30 MeV
mirror-atom DM (milestone 6 risk); (ii) a cold non-thermal relic on $\Sigma_2$ — viable, generic;
(iii) no mirror DM (empty $\Sigma_2$ or RS2 overshoot) — viable, silent. Every mirror-DM survivor
costs one number the action does not produce (+1 parameter if taken). None adopted.

## 5c. The impact (`04_impact.md`)

| quantity | result |
|---|---|
| $\mathcal C$ | computed: fixed point $\rho_E/\rho_{\text{rad}} \to \alpha/4 \approx 5\times10^{-3}$ (Langlois–Sorbo–Rodríguez-Martínez), $\Delta N_{\text{eff}} \lesssim 0.03$; $\propto (T_{RH}/T_t)^2$ below $T_t \approx 6$ TeV ($\ell = 10\,\mu$m) |
| $\phi_0$ | $\Omega_0 = [1 - \tfrac{3}{2\sqrt2}\mathrm{asinh}\sqrt{r_b}]^{2/3}$; Cassini needs $r_b$ within 1.5% of the overshoot value $r_c = 1.186$ (coincidence problem); overshoot $\Rightarrow$ RS2, no mirror sector, also allowed by data |
| $T_2/T_1$ | not derivable ($\mathbb Z_2$-symmetric collision); null $x=1$ gives $\Delta N_{\text{eff}} \approx 6$, excluded; $x < 0.45$; possible floor $x \gtrsim 0.1$–0.26 from graviton transfer to $\Sigma_2$ [verify] |
| $n_2/n_1$ | needs $\eta_2/\eta_1 \gtrsim 1600$: mirror-DM branch closed |
| sign $\delta\sigma_2$ | not fixed ($\lvert V_{\text{rad}}\rvert \lesssim 10^{-36}$ of the impact energy); if attractive at its bound, earliest second impact $\gtrsim 200$ Gyr |
| $(n_s, r)$ | not produced: bulk scalar gives $r = 8c^2 \ge 0.28$; radion is not ekpyrotic; $n_s$, `A_s` stay borrowed |

## 5d. The approach to $\Omega = 1$ without the moduli approximation (`04c_approach.md`)

| result | status |
|---|---|
| bulk between the branes is static Schwarzschild–AdS (Birkhoff); each brane's motion fixed by its own content; no independent radion | derived |
| $\Omega_\infty^3 = (\epsilon - f)/(1+\epsilon)$, $f$ = $\Sigma_2$/$\Sigma_1$ radiation, $\epsilon$ = dark radiation/$\Sigma_1$ radiation, both at coincidence | derived, checked to 5% (`tests/approach.py`) |
| `r_b` does not exist as a datum: the three of 5b collapse to two | derived |
| $\epsilon \ge f$ or $\Sigma_2$ has no trajectory: dark radiation $\ge$ mirror energy, $N_{\text{eff}}$ budget doubled; $\mathcal C$ re-opened as collision data | derived |
| Cassini: $\epsilon - f \lesssim 3\times10^{-5}$ — the 1.5% coincidence becomes 0.1–0.3% of $f$; generic collision gives no $\Sigma_2$ or $\Omega_0 \sim 0.1$–1 | derived; "no mirror DM" is now the generic family |
| $\rho \gtrsim \sigma_1$ at coincidence: branes cross, Fork 1 lost; scope is $h \lesssim 1$ | numerical |
| **circle radius $\ell_z$ is an unstabilized modulus** coupled to $\alpha$; the fixed circle of `01_action.md` is not a solution; stabilizer fork owed (≥ +1) | gap; kill risk |
| pre-action layer (independent universes, arrows of time, crystallization) recorded in `00_axiom.md` as hypothesis; unified-sector fork pre-registered in `ledger.md` | not derived, not used |

## 5e. The circle (`04d_circle.md`)

| result | status |
|---|---|
| SM Casimir energy on the wrapped brane is repulsive (62 more fermionic than bosonic degrees of freedom); the action's own terms give a minimum at $\ell_z^{-1} \approx 7$ meV that tracks dark energy — dead | derived (O(1) coefficient [verify]) |
| stabilizer taken: Casimir + negative detuning $\delta_1$ of $\sigma_1$ (**parameter #8**); flux and Goldberger–Wise not taken (more content, same physics) | derived |
| $m_\chi = 10^{-2}\,\mathrm{eV}\,(\ell_z^{-1}/10\,\mathrm{TeV})^2$; Eöt-Wash and $\lvert\delta_1\rvert < \sigma_1$ give $5.4 < \ell_z^{-1}/\mathrm{TeV} < 29$ | derived, two-sided |
| **P1, pre-registered**: composition-dependent gravitational-strength Yukawa force with range 2–66 μm | falsifiable; open |
| $\alpha$ does not drift (minimum independent of $\phi$, $\Phi$): clock/quasar bounds passed | derived |
| moduli problem: overclosure unless $T_R < T_o$; the oscillating circle is a fourth DM family, BMI-specific | derived; adopted in milestone 6 |

## 6. The dark sector (`05_dark_sector.md`)

| result | status |
|---|---|
| thermal misalignment gives all or nothing: $T_R > T_o \approx 2.7$ TeV overcloses; $T_R < T_o$ excites nothing (adiabatic). The 5d "$T_R$ tuned to 0.4%" is retracted | derived |
| $T_R < T_o$ ⇔ $h < 0.07$ at the impact; $T_o < T_t$, so the standard FRW background holds from reheating | derived |
| mechanism: the impact leaves the circle offset by $\delta_z$ (**parameter #9**); $\Omega_\chi \propto \delta_z^2 (T_o/T_R)^3$; $\delta_z \approx 3\times10^{-6}(T_R/T_o)^{3/2}$; 10% in $\delta_z$ → 3% in $\Omega_{DM}$ | derived; fitted |
| structure: Jeans length $4\times10^{-6}$ pc — CDM everywhere; Bullet/halos/dwarfs pass trivially | derived |
| isocurvature: $\delta_z$ uniform to $5\times10^{-6}$ (Planck $\beta_{\text{iso}}$); same homogeneity debt as the missing inflation | derived |
| signatures: $\alpha$, $G$ oscillate at 2.5 THz, amplitude $10^{-31}$; no direct/indirect detection; the only handle is P1 | derived |
| K1–K4 pre-registered: P1 emptied; $T_R >$ few TeV; any DM self-interaction/particle detection; $\beta_{\text{iso}}$ detection | — |

## 5b. Field content from geometry (`02b_localization.md`)

Forced by the AdS$_6$ background plus the SM's own consistency: gravity/radion/scalars on
$\Sigma_1$; $z \in S^1/\mathbb Z_2$ (chirality); SM gauge fields and charged fermions on
$\Sigma_1$ (a bulk gauge field would charge the mirror sector); only gauge singlets may be
bulk fields; $z$-excitations are heavy and ours, $y$-excitations are light by $\Omega$ and
theirs. **Not forced:** the bulk mass $c$ of a bulk fermion — one dial per species, not
admitted; the only clean option is a universal $c$ (would be parameter #8).

## 6. Kill criteria (`01_action.md` §5)

| # | criterion | status |
|---|---|---|
| 1 | GR + ΛCDM in frozen limit | **passed** (milestone 3) |
| 2 | $\dot G/G$ vs LLR | **passed** (milestone 4): $\lesssim 3\times10^{-16}\,\mathrm{yr}^{-1}$ |
| 3 | $w(z)$ vs DESI | **open**: thawing curve, $w>-1$; Planck constant-$w$ needs $c\lesssim0.5$; DESI DR2 central value (phantom) unreachable — chain-level test in milestone 7 |
| 4 | $\Delta N_{\text{eff}}$, $T_2/T_1$ vs BBN/Planck | **fired** (milestone 5): not because the impact gives $T_2/T_1 > 0.5$ (it gives no number) but because no $T_2/T_1 < 0.45$ yields $\Omega_{DM}/\Omega_b = 5.3$ with $\eta_2 = \eta_1$; mirror SM as DM dead |
| 5 | $r > 0.01$ kills the collision origin | **re-labelled** (milestone 5): the action produces no primordial spectrum, so it neither predicts nor is killed by $r$ |
| 6 | $\Omega_{DM}/\Omega_b$, $\sigma/m$ | milestone 6 — only if an exit from §5 is chosen |

## 7. Generic vs BMI-specific (honest split)

Everything in §3 is standard two-brane Randall–Sundrum physics in one more dimension plus
standard exponential quintessence; it earns BMI nothing except consistency. BMI-specific
content so far: the slope of dark energy is the bulk-potential parameter $c$ with no geometric
factor; the radion bound comes from *DM mass drift*; the warped mirror thresholds and the
$\Omega_0$ factor that kill mirror DM; the finite radion range and the overshoot/RS2
alternative. Not yet computed: the low-$\ell$ CMB axis; the matching through the collision.

## 8. Repo state

- PR #1 (freeze v1, retractions, ledger CI) → PR #2 (action) → PR #3 (effective theory) → PR #4 (localization) → PR #5 (background, merged) → PR #6 (impact) → PR #7 (scan) → PR #8 (approach) → PR #9 (circle) → PR #10 (dark sector).
- CI: `tests/check_ledger.py` (undeclared symbols fail the build), `tests/check_background.py` (sympy, background identities), `tests/check_zero_modes.py` (zero-mode profiles per spin), `tests/check_radion.py` (moduli action, quintessence slope), `tests/background_frw.py` (FRW numbers), `tests/impact.py` (freeze-out, $N_{\text{eff}}$, $\mathcal C$, turnaround, inflation numbers).
- `tests/scan_initial_conditions.py`: post-impact initial-data scan and viability map.
- `tests/approach.py`: exact two-brane trajectories in Schwarzschild–AdS, closed-form $\Omega_\infty$, Cassini window in $\epsilon$.
- `tests/circle.py`: Casimir sign, option-0 exclusion, option-A window, modulus mass, moduli abundance, P1 range.
- `tests/dark_sector.py`: thermal-shift overclosure, $T_R < T_o$, $\delta_z(T_R)$, $h$ bound, Jeans length, isocurvature, oscillation signatures.
- Next: milestone 7 (predictions) — the balance is −9 and must move.
