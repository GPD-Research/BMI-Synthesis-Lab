# 04 — The impact: what the collision fixes, what it cannot, and what dies

Milestone 5. Inputs: the action of `01_action.md`; the effective 4D theory of
`02_effective_4d.md` and `03_background.md` (radion $\phi$, $\Omega = e^{-\phi/\ell}$, canonical
radion $\chi = -\tfrac{4}{\sqrt3}M_{Pl}\Omega^{3/2}$, $V_{\text{rad}} = \delta\sigma_2\Omega^4$,
bulk-scalar zero mode $\Phi_4$ with $V = V_*e^{-c\Phi_4/M_{Pl}}$, mirror masses $\Omega m$).
Numerical check: `tests/impact.py`. Everything marked **[verify]** is a stated approximation.

The milestone was to derive four numbers from the collision kinematics: $T_2/T_1$, $n_2/n_1$,
$\mathcal C$, and the sign of $\delta\sigma_2$, plus $(n_s, r)$ if the background permits.
Summary of the outcome, detailed below:

| quantity | outcome | status |
|---|---|---|
| $\mathcal C$ (dark radiation) | **computed**, not a parameter: $\rho_E/\rho_{\text{rad}} \le \alpha/4 \approx 5\times10^{-3}$, $\Delta N_{\text{eff}} \lesssim 0.03$ | derived (D=5 coefficients, §4) |
| $\phi_0$ (#3) | traded for the impact kinetic ratio $r_b$: $\Omega_0 = [1 - \sqrt6\,\mathrm{asinh}\sqrt{r_b}/(4/\sqrt3)]^{2/3}$; Cassini needs $r_b$ within $1.5\%$ of the critical $r_c = 1.186$ | derived; coincidence recorded (§1) |
| $T_2/T_1$ (#7) | **not derivable** from the action; bounded $x < 0.45$ (CMB $N_{\text{eff}}$); the symmetric impact $x = 1$ gives $\Delta N_{\text{eff}} \approx 6$ | stays a parameter; §2 |
| $n_2/n_1$ | forced: $\Omega_{DM}/\Omega_b = \Omega_0\,x^3\,\eta_2/\eta_1 \lesssim 3\times10^{-3}\,\eta_2/\eta_1$; needs $\eta_2/\eta_1 \gtrsim 1600$ | **mirror-SM choice for $\Sigma_2$ is dead** (§3) |
| sign of $\delta\sigma_2$ | not fixed by kinematics ($\lvert V_{\text{rad}}\rvert \ll$ impact energy); earliest turnaround for $\delta\sigma_2<0$ at the bound is $\gtrsim 200$ Gyr | open; fate table now has a number (§5) |
| $(n_s, r)$ | not produced: the only bulk scalar gives power-law inflation with $r = 8c^2 \ge 0.28$ at $n_s = 0.965$ | negative result; `A_s`, $n_s$ stay borrowed (§6) |

## 0. What "the impact" is in this action, and where the action stops

The collision is $\phi \to 0$: $\Omega \to 1$, the two branes coincide. Three facts about that
point follow from milestones 3–4 and are not choices:

1. $M_{Pl}^2(\phi) = \tfrac{M_5^3\ell}{3}(1-\Omega^3) \to 0$: 4D gravity on $\Sigma_1$ switches
   off at the collision. The effective 4D description of `03_background.md` §1 is a moduli
   approximation valid for $\Omega \ll 1$ and $\lvert\dot\phi\rvert \ll 1$; it is *not* valid
   at the impact.
2. The canonical radion has finite range: $\lvert\chi\rvert \le \tfrac{4}{\sqrt3}M_{Pl}$, with
   $\chi = -\tfrac{4}{\sqrt3}M_{Pl}$ at $\Omega = 1$ and $\chi \to 0$ at $\Omega \to 0$
   ($\Sigma_2$ at the AdS horizon). The collision is the *edge* of field space, not a point in
   its interior — the same structure as the Hořava–Witten/ekpyrotic radion (Khoury, Ovrut,
   Steinhardt & Turok 2001), where the 5D geometry at the collision is a compactified Milne
   space and the matching across it is *not* determined by the low-energy action.
3. The bulk-scalar potential $V(\Phi) = V_0e^{-c\Phi/M_6^2}$ is positive and monotonic. It
   cannot supply the steep negative potential that drives an ekpyrotic contraction, so the
   pre-impact phase, if any, is not described by this action either.

So the fixed action determines the post-impact evolution once the branes have separated by
$\Omega \lesssim 0.5$ (say), *given* the state at that moment: the radiation on each brane,
the radion velocity, the bulk radiation. What it does **not** determine is the matching through
$\Omega = 1$ — how the collision energy is split between $\Sigma_1$, $\Sigma_2$ and the bulk.
That split is exactly $T_2/T_1$. Everything in this file that is derived is a *map from the
post-impact state to observables*; wherever the observable requires the matching itself, it is
so labelled and no number is invented for it.

## 1. Post-impact radion freeze-out: what fixes $\phi_0$

After the impact the radion is a canonical field with negligible potential
($V_{\text{rad}}/\rho \sim \delta\sigma_2\Omega^4/\rho \ll 1$ throughout radiation domination,
`03_background.md` §3.1) in a radiation-dominated universe. Its kinetic energy dilutes as
$a^{-6}$, radiation as $a^{-4}$, so it freezes. With $\ln a$ as the time variable and the kinetic-to-radiation
ratio $r_b$ at the moment the moduli approximation becomes valid:
$$
\frac{d\chi}{d\ln a} = \sqrt6\,M_{Pl}\left(\frac{\rho_{\chi}}{\rho_{\text{tot}}}\right)^{1/2}
\quad\Rightarrow\quad
\Delta\chi = \sqrt6\,M_{Pl}\,\mathrm{asinh}\sqrt{r_b} ,
$$
(exact for kination + radiation; checked numerically in `tests/impact.py` §1). Starting at the
collision edge $\chi = -\tfrac{4}{\sqrt3}M_{Pl}$ and freezing at $\chi_0 = -\tfrac{4}{\sqrt3}M_{Pl}\Omega_0^{3/2}$:
$$
\Omega_0 = \left[1 - \frac{\sqrt6}{4/\sqrt3}\,\mathrm{asinh}\sqrt{r_b}\right]^{2/3}
= \left[1 - \tfrac{3}{2\sqrt2}\,\mathrm{asinh}\sqrt{r_b}\right]^{2/3}.
$$
Consequences:

- **Critical ratio.** $\Omega_0 \to 0$ at $r_c = \sinh^2(2\sqrt2/3) = 1.186$. For $r_b > r_c$
  the radion overshoots $\chi = 0$: $\Sigma_2$ reaches the AdS horizon, the branes decouple
  forever and the theory becomes single-brane RS2 with no mirror sector. **[verify]** what
  happens at $\chi = 0$ exactly (the canonical map is singular there; the RS2 limit is the
  natural continuation).
- **Parameter #3 is traded, not removed.** $\phi_0$ is now a function of $r_b$; the budget is
  unchanged (one initial condition replaces one parameter). What is new is that $\Omega_0$ is
  *sensitive*: Cassini ($\Omega_0 < 0.032$) needs $1.168 < r_b < 1.186$, a window of $1.5\%$
  just below overshoot. A generic impact gives $r_b \sim 1$ and $\Omega_0 \sim 0.1$–$0.3$,
  which Cassini excludes. This is a **coincidence problem** of the same kind as the
  cosmological-constant one and is recorded as such, not explained. **[verify]** the $r_b$
  entering here is the ratio *after* the moduli approximation becomes valid ($\Omega \sim 0.5$),
  not at the collision itself; the map from the collision to that point is the unknown matching
  of §0.
- $\Omega_0 = 0$ (overshoot) is *also* consistent with all present data: gravity is then RS2 with
  $\ell \lesssim 10\,\mu$m, dark matter is not mirror matter, and the "continuing collision" axiom
  is false. The theory does not prefer its own axiom; the data (a mirror-DM signature) must.

## 2. $T_2/T_1$: not derivable, bounded, and the null hypothesis is excluded

Define $x \equiv T_2/T_1$ at the impact (both sectors relativistic with the full SM content),
temperatures measured in the $\Sigma_1$ frame (a mirror particle whose energy in the $\Sigma_1$ frame is
$\Omega$ times its proper energy on $\Sigma_2$; energy densities on $\Sigma_2$ enter the
Friedmann equation on $\Sigma_1$ as $\Omega^4\rho^{\mathrm{prop}}$, `02_effective_4d.md` §3).

**Why the action cannot fix $x$.** By construction $\mathcal L^{(1)}$ and $\mathcal L^{(2)}$ are
identical Lagrangians on branes whose tensions are tuned to opposite values, and the bulk is
$\mathbb Z_2$-symmetric under $y \to \phi - y$ at $\phi \to 0$: at the collision the two branes
are related by a symmetry of the action. A symmetric collision therefore deposits equal energy
on both: $x = 1$ is the *null hypothesis of the action*. Departures from it require an
asymmetry the action does not contain — different matter content, different pre-impact
temperatures, a $\Phi$-dependent tension, or an asymmetric bulk state. None is present. $T_2/T_1$
therefore **remains parameter #7**; kill criterion 4 as written ("if impact kinematics give
$T_2/T_1 \gtrsim 0.5$") cannot fire because the kinematics give no number. It is re-stated
below as a condition on whatever mechanism is later invoked.

**The null hypothesis is excluded.** With $x = 1$ the mirror sector doubles the radiation
density. Because mirror species are warped down, they annihilate when their *proper*
temperature $T_2/\Omega$ drops below their mass, i.e. at a $\Sigma_1$ temperature lower by
$\Omega$: the mirror $e^\pm$ annihilate at $T_1 \approx 14$ keV ($\Omega_0 = 0.032$), long
after BBN. So at BBN the mirror sector still carries its $e^\pm$, $\gamma$, $\nu$ and — for
$\Omega_0 \lesssim 0.01$ — its pions, muons and even a quark–gluon plasma
(`tests/impact.py` §2):
$$
\Delta N_{\text{eff}}(x{=}1) = 3.4\text{–}6.1\ \ \mathrm{(BBN)},\qquad
\Delta N_{\text{eff}}(x{=}1) \approx 7.5\ \ \mathrm{(CMB)} .
$$
Both are excluded by more than an order of magnitude ($\Delta N_{\text{eff}} < 0.3$). The
bounds on $x$ from $\Delta N_{\text{eff}} < 0.3$:
$$
x < 0.47\text{–}0.49 \;\;\mathrm{(BBN,\ depends\ on\ }\Omega_0\mathrm{)},\qquad
x < 0.45 \;\;\mathrm{(CMB,\ independent\ of\ }\Omega_0\mathrm{)}.
$$
The CMB bound binds. (Entropy is conserved separately in each sector; $g_*(T)$ is a coarse
step table, thresholds at $m/3$; the bounds are insensitive to this at the 10% level.)

**A floor on $x$ from gravity alone [verify].** Bulk gravitons emitted by the hot $\Sigma_1$
(§4) carry $\epsilon_W \lesssim 5\times10^{-3}$ of its energy into the bulk. In a two-brane
geometry they do not escape to a horizon: they fall toward $\Sigma_2$ (KK gravitons are
IR-localized). If absorbed there, this heats $\Sigma_2$ to $x \gtrsim \epsilon_W^{1/4}
\approx 0.26$ ($T_{RH} \gtrsim T_t$) or $0.09$–$0.16$ ($T_{RH} = 0.1$–$0.3\,T_t$) *even if the
impact deposited nothing on $\Sigma_2$*. The absorption efficiency of a brane for bulk
gravitons is not computed here. If this floor holds, the mirror sector is required to have
$0.1 \lesssim x < 0.45$: a mirror sector that is present, cool, and never absent — a
BMI-specific window, but one that no observation currently probes ($\Delta N_{\text{eff}}
\gtrsim 10^{-3}$–$0.03$; CMB-S4 reaches $0.03$).

**Kill criterion 4, restated.** Any mechanism later proposed for the impact asymmetry must
deliver $x < 0.45$ with $\eta_2/\eta_1$ as in §3; it is killed if it cannot. Kill criterion 4 in
`01_action.md` §6 is annotated accordingly.

## 3. $n_2/n_1$ and the death of the minimal mirror sector

Dark matter on $\Sigma_2$ is mirror baryons of mass $\Omega_0 m_p$ (`02_effective_4d.md` §5).
Their number density relative to ours is fixed by the temperature ratio and the baryon
asymmetries $\eta_i$ (baryon-to-photon ratios) of each sector:
$$
\frac{\Omega_{DM}}{\Omega_b} = \Omega_0\,\frac{n_2}{n_1}
= \Omega_0\left(\frac{T_2}{T_1}\right)^3_{\!\mathrm{today}}\frac{\eta_2}{\eta_1}
\approx 0.10\,\Omega_0\,\frac{\eta_2}{\eta_1}\quad(x\ \mathrm{at\ its\ bound}),
$$
where the factor $0.10$ is $x^3$ corrected for the different entropy histories
(`tests/impact.py` §2). The observed $\Omega_{DM}/\Omega_b = 5.3$ then requires
$$
\frac{\eta_2}{\eta_1} \gtrsim 1600\;(\Omega_0 = 0.032),\qquad
4500\;(\Omega_0 = 0.01),\qquad 1.5\times10^4\;(\Omega_0 = 0.003).
$$
With identical Lagrangians and the same CP violation, the natural expectation is
$\eta_2 = \eta_1$, which gives $\Omega_{DM}/\Omega_b \approx 3\times10^{-3}$: the mirror sector
would be $0.06\%$ of the dark matter. Three-plus orders of magnitude are missing, in the
direction that requires the *colder* sector to have generated a *thousandfold larger* baryon
asymmetry. Nothing in the action does this: the Standard Model's own baryogenesis is
insufficient by orders of magnitude (which is why $\eta_B$ is a borrowed constant in the
ledger), so there is not even a mechanism to make asymmetric. The number $n_2/n_1 \gtrsim 165$
of milestone 3 was the requirement *before* $x < 0.45$ and the entropy factor were known;
with them it is $n_2/n_1 \gtrsim 165 / 0.10 \approx 1600$ in units of what a symmetric
impact would give.

**Verdict: the minimal choice "$\Sigma_2$ carries a mirror Standard Model as the dark matter"
(`01_action.md` §2.2) is dead as a stand-alone account of dark matter.** This is kill criterion
4 firing in its restated form — not because $x$ is too large but because no $x$ works: raising
$x$ toward 1 to gain number density is excluded by $N_{\text{eff}}$, and the mass suppression
$\Omega_0 < 0.032$ is forced by Cassini. The failure is BMI-specific: in a generic
(unwarped) mirror model $m^{(2)} = m$ and $\eta_2 = \eta_1$ with $x \approx 0.5$ gives
$\Omega_{DM}/\Omega_b \approx 0.1$, off by a factor 50, and the mirror-matter literature
closes that gap with asymmetric leptogenesis across the sectors (Berezhiani, Comelli &
Villante 2001). Here the gap is $\gtrsim 1600$ and grows as $1/\Omega_0$; the warp factor
makes it hopeless. This is the first v2 negative result that closes a branch
(§7; recorded as N2 in `RETRACTED.md`).

**What is not affected.** The mirror sector still exists in the action ($\mathcal L^{(2)}$ is
the same Lagrangian) and still contributes $\Delta N_{\text{eff}} \sim x^4$ and a light
subdominant component; its existence is not killed, its role as the dark matter is. The
localization results (`02b_localization.md`), the background (`03_background.md`), the
dark-energy identification and the fate table are unchanged.

**Exits, with their prices (none taken here; decision for the author):**

| exit | what it changes | cost | comment |
|---|---|---|---|
| (a) $\Sigma_2$ has more internal dimensions (pre-registered fallback, `01_action.md` §1) | effective sector-2 fluid `w_2` | +1 parameter | does *not* fix the problem: the fluid's energy is still warped by $\Omega^4$ and its number density is still set by $x$; only helps if the extra dimensions carry a heavy stable state |
| (b) a heavy stable mirror state | proper mass $\gtrsim 5.3/(0.10\,\Omega_0)\,m_p^{\mathrm{prop}}$: $\approx 1.6$ TeV proper, $\approx 50$ GeV in our frame at $\Omega_0 = 0.032$ | new field content on $\Sigma_2$, $\ge$+1 | breaks the "same Lagrangian" premise; generic WIMP, no BMI content |
| (c) asymmetric baryogenesis from the collision itself (v1 Ch 4.3 target) | $\eta_2/\eta_1 \gtrsim 10^3$ | a mechanism, not a parameter — none exists in the action | the only exit that keeps BMI content; requires CP-odd, $\mathbb Z_2$-odd dynamics at the impact, which the action lacks |
| (d) $\Sigma_1$ is the IR brane (Fork 2, `02_effective_4d.md`) | $m^{(2)} = m/\Omega$; then $\Omega_{DM}/\Omega_b \approx 3.3\,\eta_2/\eta_1$ — *natural* | Cassini kills Fork 2 unless the radion is stabilised (+4 parameters, and stabilisation stops the merger) | the only exit that gives $5.3$ for free; it costs the axiom |
| (e) dark matter is not on $\Sigma_2$ at all (e.g. the overshoot case $\Omega_0 = 0$ of §1, DM elsewhere) | drops the mirror-DM prediction | 0 here, but DM is then borrowed | the theory says nothing about DM |

The honest reading is (e) or (c): either BMI is a theory of gravity and dark energy that is
silent on dark matter, or the collision must be shown to generate the asymmetry. (c) is a
well-posed, falsifiable task with a target number ($\eta_2/\eta_1 \gtrsim 1600$) and is the
natural content of a milestone 5b; it is *not* attempted here because the action has no
$\mathbb Z_2$-odd operator to drive it.

## 4. Dark radiation: $\mathcal C$ is computed, not a parameter

The projected-Weyl term $\rho_E = \mathcal C/a^4$ was carried as a pending integration constant
(milestones 3–4). It is not free once the brane is allowed to radiate into the bulk. For a hot
brane in an AdS bulk, Langlois, Sorbo & Rodríguez-Martínez (2002, hep-th/0206146) solved the
coupled system (their eqs. 20–25; $D = 5$, RS2, $\mathbb Z_2$-symmetric bulk):
$$
\dot\rho + 4H\rho = -\frac{\alpha}{12}\kappa_5^2\rho^2,\qquad
\alpha = \frac{212625}{64\pi^7}\,\zeta(9/2)\zeta(7/2)\,\frac{\hat g}{g_*^2} \approx 0.019
\;\;(\mathrm{full\ SM:}\ \hat g = 166.21,\ g_* = 106.75),
$$
and found that $\mathcal C$ is *driven to a fixed point* during the high-energy
($\rho \gtrsim \lambda$, $\lambda$ = brane tension) radiation era:
$$
\epsilon_W \equiv \frac{\rho_E}{\rho_{\text{rad}}} \to \frac{\alpha}{4} \approx 4.8\times10^{-3},
$$
independent of $M_5$ and of the initial value of $\mathcal C$. If reheating is *below* the
transition temperature $T_t$ ($\rho_{RH} < \lambda$), integrating their eq. 23 in the
low-energy regime gives (this file)
$$
\epsilon_W = \frac{\alpha}{2\sqrt2}\left(\frac{T_{RH}}{T_t}\right)^2 ,\qquad
T_t = \left(\frac{30\,\lambda}{\pi^2 g_*}\right)^{1/4},\quad
\lambda = \sigma_1^{(5)} = \frac{8M_5^3}{\ell} = \frac{24M_{Pl}^2}{\ell^2} ,
$$
so $T_t \approx 6$ TeV for $\ell = 10\,\mu$m, $20$ TeV for $1\,\mu$m (the "15 TeV" of
`STATUS.md` was $\lambda^{1/4}$ without the $g_*$ factor; corrected there).

**Result.** $\Delta N_{\text{eff}}^{\mathrm{Weyl}} = \epsilon_W\cdot 10.75/1.75 \le 0.03$ at BBN
for *any* reheating temperature, and $\ll 0.03$ for $T_{RH} \ll T_t$; after the $g_*$ dilution
of their eq. 26 it is $\approx 0.01$. The bound $\Delta N_{\text{eff}} \lesssim 0.3$ is
satisfied by a factor $\ge 10$ with nothing tuned. $\mathcal C$ leaves the pending list of the
ledger: it is an output.

**Two [verify] items, both bounded.** (i) The coefficients are $D=5$ with a two-sided
($\mathbb Z_2$) bulk; ours is $D=6$ with a warped circle and a one-sided bulk toward $\Sigma_2$.
For $T \lesssim 1/\ell_z$ the $z$-modes are frozen and the emission is the 5D rate with $M_5$,
halved for one side; for $T \gtrsim 1/\ell_z$ the extra channels raise $\hat g$ by O(1).
Neither changes the order of magnitude. (ii) In a two-brane geometry the emitted gravitons
reach $\Sigma_2$ (§2); to the extent they are absorbed there, $\mathcal C$ is *smaller* than
the fixed point and $x$ has the floor of §2 instead. Either way the leaked energy is
$\le \epsilon_W\rho_1$: the dark-radiation budget is closed regardless of which way it goes.

**Generic vs BMI.** The fixed point $\epsilon_W \to \alpha/4$ is generic braneworld physics
(LSR). BMI-specific is only the two-brane fate of the gravitons, item (ii), which converts
dark radiation into mirror heat — a prediction-in-waiting once the absorption is computed.

## 5. The sign of $\delta\sigma_2$: not fixed by the impact; the fate table gets a number

The impact cannot fix the sign. At the collision $\lvert V_{\text{rad}}\rvert = \lvert\delta\sigma_2\rvert$
(at $\Omega = 1$), and by `03_background.md` §3.1 today $\lvert\delta\sigma_2\rvert\Omega_0^4
< 5\times10^{-6}\rho_0$, i.e. $\lvert\delta\sigma_2\rvert < 0.15\,\rho_0/\Omega_0 \lesssim
(10\,\text{meV})^4$. This is smaller than the post-impact radiation density by $\gtrsim 36$
orders of magnitude at any $T_{RH} \gtrsim$ MeV: both signs let the branes separate on the
kinetic energy alone ($r_b$ of §1 is unaffected at that level). The sign is therefore an initial-condition question for the
pre-impact geometry, which this action does not describe (§0). It **stays open**; parameter
#4 keeps both signs.

What *can* now be computed is the earliest possible turnaround if $\delta\sigma_2 < 0$
saturates its bound. Integrating the radion, quintessence and matter forward from today
(`tests/impact.py` §4; radion in the moduli approximation, stopped at $\Omega = 0.5$ where
it fails):

| $\Omega_0$ | $\lvert\delta\sigma_2\rvert/\rho_0$ at the bound | $H \to 0$ | reaches $\Omega = 0.5$ |
|---|---|---|---|
| 0.032 | 4.7 | not before $\Omega = 0.5$ | 220 Gyr |
| 0.010 | 15 | not before $\Omega = 0.5$ | 240 Gyr |
| 0.003 | 50 | 250 Gyr | — |

So row 3 of the fate table (`03_background.md` §3.4) reads: *if* attractive, the second impact
is not earlier than $\sim 200$ Gyr from now ($\approx 15$ Hubble times), and the moduli
approximation fails before it, so the actual collision requires the full junction problem.
With $\delta\sigma_2 > 0$ of the same magnitude $\Omega$ decreases monotonically (checked).
The number is a lower bound on the time, from an upper bound on $\lvert\delta\sigma_2\rvert$;
a smaller $\lvert\delta\sigma_2\rvert$ pushes it out without limit. Not a prediction — the
statement "acceleration is permanent on any observable timescale" of milestone 4 stands.

## 6. $(n_s, r)$: the action produces no primordial spectrum

Two candidates exist in the action and both fail:

- **The bulk scalar as inflaton.** $V = V_*e^{-c\Phi_4/M_{Pl}}$ gives power-law inflation,
  $a \propto t^{2/c^2}$, with $n_s - 1 = -c^2/(1-c^2/2)$ and $r = 8c^2$. Matching
  $n_s = 0.965$ needs $c = 0.185$ and gives $r = 0.28$, excluded by BICEP/Keck + Planck
  ($r < 0.036$) by a factor 8; and power-law inflation never ends. Moreover $c$ is the *same*
  slope that milestone 4 needs at $c \lesssim 0.5$ for dark energy, so there is no freedom.
  A negative result with no escape inside the budget.
- **The radion as an ekpyrotic field.** $V_{\text{rad}} = \delta\sigma_2\Omega^4 \propto
  \chi^{8/3}$ in the canonical field: a power law, not the steep negative exponential
  ($V \propto -e^{-\lambda\chi/M_{Pl}}$ with $\lambda \gg 1$) that ekpyrosis needs. No scale-invariant
  spectrum is produced.

Therefore `A_s` and $n_s$ remain borrowed ΛCDM inputs (2 of its 6), and kill criterion 5
("$r > 0.01$ kills the collision origin") is **re-labelled**: it is inherited from ekpyrotic
models whose ingredient (a steep negative potential) this action does not have. The honest
statement is weaker in both directions: the action predicts no $r$, so no $r$ kills it, and it
earns no credit if $r$ is small. Annotated in `01_action.md` §6.

## 7. Negative results recorded

| claim tested | result | consequence |
|---|---|---|
| $T_2/T_1$ derivable from the impact | no; the action is $\mathbb Z_2$-symmetric at the collision, $x = 1$ is its null hypothesis | #7 stays a parameter; null excluded ($\Delta N_{\text{eff}} \approx 6$) |
| mirror SM on $\Sigma_2$ is the dark matter | needs $\eta_2/\eta_1 \gtrsim 1600$; action has no mechanism | **branch closed**; exits listed in §3 |
| $\mathcal C$ is a free integration constant | no; fixed point $\epsilon_W \to \alpha/4$ (LSR) | removed from pending; $\Delta N_{\text{eff}} \lesssim 0.03$ |
| impact fixes sign($\delta\sigma_2$) | no; $\lvert V_{\text{rad}}\rvert$ is $\lesssim 10^{-36}$ of the impact energy | open; earliest turnaround $\gtrsim 200$ Gyr |
| action yields $(n_s, r)$ | no; $r = 8c^2 \ge 0.28$ or no spectrum | `A_s`, $n_s$ borrowed; kill criterion 5 re-labelled |
| $\phi_0$ is a free parameter | it is the image of $r_b$; Cassini needs $r_b$ within 1.5% of overshoot | coincidence problem recorded |

## 8. Generic vs BMI-specific

Generic braneworld: radion kination and freeze-out (§1, any two-brane model); the LSR fixed
point (§4); $x < 0.45$ from $N_{\text{eff}}$ (any mirror sector). BMI-specific: the warped
thresholds that keep mirror $e^\pm$ relativistic through BBN (§2); the factor $\Omega_0$ in
$\Omega_{DM}/\Omega_b$ that kills the mirror-DM branch (§3); the finite range of $\chi$ and the
overshoot/RS2 alternative (§1); the two-brane fate of emitted gravitons (§4 ii).

## 9. Open [verify] items carried forward

1. Matching through $\Omega = 1$ (compactified Milne in 6D with a warped circle): not attempted.
2. Continuation at $\chi = 0$ (overshoot → RS2).
3. $D = 6$, one-sided graviton emission coefficients; brane absorption efficiency on $\Sigma_2$.
4. Whether any $\mathbb Z_2$-odd, CP-odd dynamics at the impact can give $\eta_2/\eta_1 \gtrsim 10^3$ (exit (c) of §3) — proposed milestone 5b, or the branch is abandoned.
5. The coarse $g_*(T)$ table (thresholds at $m/3$; QCD transition at 150 MeV as a step).
