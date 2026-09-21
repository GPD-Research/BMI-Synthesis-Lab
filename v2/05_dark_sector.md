# 05 — The dark sector: the oscillating circle

Milestone 6. Family chosen (of the four listed in `04d_circle.md` §4 and `04b_initial_conditions.md`):
the dark matter is the coherent oscillation of the shared-circle modulus $\chi$ about the
minimum found in `04d_circle.md` §3. No mirror-sector matter is needed; $\Sigma_2$ may be empty,
distant, or subdominant. Numbers: `tests/dark_sector.py`.

| result | status |
|---|---|
| **thermal misalignment fails**: the KK free energy shifts the minimum by $\Delta\ln\ell_z \approx 0.4$ at $T_o$ ($H = m_\chi$); if $T_R > T_o$ this is frozen in and $\Omega_\chi \approx 0.3$ of critical from the thermal shift alone — overclosure; if $T_R < T_o$ the field tracks the shifting minimum adiabatically and the shift excites nothing | derived; **retracts** the "$T_R$ tuned to 0.4%" of `04d_circle.md` §4 |
| hard bound **$T_R < T_o \approx 2.7\ \mathrm{TeV}\,(\ell_z^{-1}/10\,\mathrm{TeV})$**; in impact language $h = \rho_1/\sigma_1 < 0.07$ (inside the $h \lesssim 1$ scope of `04c_approach.md` §5) | derived |
| the mechanism is **collision misalignment**: the impact leaves the circle at $\ell_z(1+\delta_z)$; $\Omega_\chi \propto \delta_z^2\,(T_o/T_R)^3$; $\Omega_\chi = \Omega_{DM}$ needs $\delta_z \approx 3\times10^{-6}\,(T_R/T_o)^{3/2}$ | derived; **parameter #9 = $\delta_z$** |
| tuning: 10% in $\delta_z$ moves $\Omega_{DM}$ by 3%, 10% in $T_R$ by 5% — mild, not a coincidence | derived |
| $T_o < T_t$: reheating is below the $\rho^2$ transition, so the standard FRW background of `03_background.md` holds from reheating on | derived |
| structure: Jeans length $4\times10^{-6}$ pc; identical to collisionless CDM on all observed scales; Bullet Cluster, halo shapes, DM-free dwarfs are CDM's | derived |
| isocurvature: spatial variation of $\delta_z$ across the collision surface must be $< 5\times10^{-6}$ (Planck $\beta_{\text{iso}} < 0.038$) | derived; a homogeneity requirement on the collision, which the action already owes (no inflation) |
| signatures: $\alpha$ and $G$ oscillate at $2.5$ THz with amplitude $10^{-31}$ (unobservable); no self-interaction; no direct detection; the *only* handle is the fifth force P1 | derived |
| kill criteria K1–K4 pre-registered (§5) | — |

## 0. What was chosen and what it means

The four families on the table after milestone 5d were: pre-loaded asymmetric mirror SM
(thin band, dissipative), cold relic on $\Sigma_2$ (generic, no BMI content), no dark matter
from the two-brane structure at all, and the oscillating circle. The fourth is taken because
it is the only one whose *mechanism* exists because two universes share a dimension: the
common wall of the catamaran is still ringing from the impact, and the ringing is the dark
matter. It also matches the founding intuition that dark matter is inherited from the
collision rather than manufactured afterwards — with one correction, §2, to what "inherited"
means quantitatively.

"No mirror DM" is thereby *also* adopted for $\Sigma_2$: whatever it carries must be
subdominant, which `04c_approach.md` says is the generic outcome anyway. The mirror sector
still exists (Fork 1) and still owes $N_{\text{eff}}$ via $f$ and $\epsilon$.

## 1. The thermal route, and why it is closed

The brane's KK tower has free energy $F_T(\ell_z)$; for $x = 1/(\ell_z T) \gg 1$ the first
level dominates,
$$
F_T \simeq -\,118\,T^4\left(\frac{x}{2\pi}\right)^{3/2}e^{-x},
\qquad
\Delta\ln\ell_z = \frac{\partial F_T/\partial\ln\ell_z}{\ell_z^2 V''}
= \frac{118\,T^4 (x/2\pi)^{3/2}\,x\,e^{-x}}{20\,C_z/\ell_z^4},
$$
with 118 the SM's on-shell degrees of freedom. At $T_o$ ($H = m_\chi$; $x = 3.7$
for $\ell_z^{-1} = 10$ TeV) this gives $\Delta\ln\ell_z \approx 0.4$. Two regimes:

- $T_R > T_o$. While $H > m_\chi$ the field cannot follow; when $H$ drops to $m_\chi$ it finds
  itself displaced by the thermal shift, $\approx 0.4$, and oscillates with that amplitude:
  $\rho_\chi/\rho_r = \Delta^2/6$ at $T_o$, growing as $a$ until equality — $\Omega_\chi \approx 0.3$
  of critical, i.e. all of the matter budget and more once $\Sigma_1$ baryons are added.
  **Overclosure.**
- $T_R < T_o$. From reheating on $H < m_\chi$: the minimum moves slowly compared with the
  oscillation period, the field follows it adiabatically, and the amplitude excited is
  suppressed by $(H/m_\chi)^2$. The thermal shift produces nothing.

So the thermal shift cannot be tuned to give $\Omega_{DM}$ — it gives either everything or
nothing. `04d_circle.md` §4 claimed a $T_R$ tuned to $0.4\%$ through $e^{-1/(\ell_zT_R)}$;
that neglected the adiabaticity and is **retracted** (corrected in place). What survives of
it is the bound:
$$
T_R < T_o = \left(\frac{90}{\pi^2 g_*}\right)^{1/4}\sqrt{m_\chi M_{Pl}}
\approx 2.7\ \mathrm{TeV}\left(\frac{\ell_z^{-1}}{10\ \mathrm{TeV}}\right).
$$
In the impact variables of `04c_approach.md`, $\rho_1 = (\pi^2/30)g_*T_R^4$ and the 4D
tension is $\pi\ell_z\sigma_1 \approx (13\ \mathrm{TeV})^4$ (for $\ell = 10\,\mu$m, $M_6$ [verify]):
$h < 0.07$. The exact two-brane solution of 5c was valid for $h \lesssim 1$; the dark matter
now demands the low-energy end of that range. And $T_o/T_t \approx 0.45$: reheating sits
below the $\rho^2$-correction scale, so the FRW background of `03_background.md` is standard
from reheating on — a consistency the earlier milestones assumed and can now claim.

## 2. Collision misalignment: the mechanism and parameter #9

With $T_R < T_o$, whatever displacement the circle has at reheating is *frozen*: $H < m_\chi$
means it oscillates immediately, and the amplitude is whatever the collision left. Write
$\bar\ell_z(1+\delta_z)$ for the circle radius at the impact, so $\Delta\chi/M_{Pl} = \delta_z$. Then
$$
\frac{\rho_\chi}{\rho_r}\Big|_{T_R} = \frac{\tfrac12 m_\chi^2 \delta_z^2 M_{Pl}^2}{3H^2(T_R) M_{Pl}^2}
= \frac{\delta_z^2}{6}\left(\frac{T_o}{T_R}\right)^4,
\qquad
\frac{\rho_\chi}{\rho_r}\Big|_{T_e} \simeq \frac{\delta_z^2}{6}\,\frac{T_o^4}{T_R^3\,T_e}
\quad(T_R \le T_o),
$$
and $\Omega_\chi = \Omega_{DM}$ requires
$$
\delta_z \approx 3.1\times10^{-6}\left(\frac{T_R}{T_o}\right)^{3/2}
\qquad(2\times10^{-8}\ \text{at}\ T_R = 100\ \mathrm{GeV}).
$$
A cooler collision leaves less radiation to dilute the same oscillation energy, so it needs a
*smaller* offset.
This is **parameter #9**: the fractional amount by which the collision left the shared
dimension away from its resting width. It is the quantitative content of "inertia preserved
after contact" (`00_axiom.md`, pre-action layer): not the radion's velocity (5c: not a datum),
not the circle's velocity (Hubble-damped), but the circle's *offset*. Its price is mild —
$\Omega_\chi \propto \delta_z^2 (T_o/T_R)^3$ before it saturates the matter budget, so 10% in
$\delta_z$ moves $\Omega_{DM}$ by 3% and 10% in $T_R$ by 5% — unlike the Cassini coincidence in $\epsilon - f$ (5c), which is $10^{-3}$. The
smallness $\delta_z \sim 10^{-6}$ is not explained; it is the analogue of the axion
misalignment angle, and like it, it is an initial condition of a phase the action does not
describe (the crystallization). Recorded as such.

Whether $\delta_z$ and $T_R$ are independent is the question `04c_approach.md` asked of
$r_b$ and $f$: a collision computed through $\Omega = 1$ would give both from the incoming
state. Until then $\delta_z$ is a datum, the ninth.

## 3. Structure formation

$m_\chi \approx 10^{-2}$ eV is 20 orders of magnitude above the fuzzy-DM regime: the comoving
Jeans length is $(16\pi G\rho_m m_\chi^2)^{-1/4} \approx 4\times10^{-6}$ pc. On every scale
probed — CMB, BAO, Lyman-$\alpha$, halos, the Bullet Cluster, DM-free dwarfs — the oscillating
circle is collisionless CDM: no self-interaction ($\sigma/m$ from the quartic of $V(\ell_z)$ is
Planck-suppressed), no dissipation, no offset between DM and baryons beyond CDM's. The
"structure formation offset" the roadmap listed for milestone 6 is therefore zero; that is a
pass, not a prediction.

Cold from the start: at $T_R$ the field is a zero-momentum condensate. There is no thermal
$\chi$ population because $\chi$ couples with gravitational strength.

**Isocurvature.** $\delta_z$ set at the collision can vary across the collision surface. A
fractional variation $\delta(\delta_z)/\delta_z$ is a CDM isocurvature mode $\mathcal S = 2\,\delta(\delta_z)/\delta_z$;
Planck's $\beta_{\text{iso}} < 0.038$ (uncorrelated, at 0.05 Mpc$^{-1}$) gives
$\delta(\delta_z)/\delta_z < 4.6\times10^{-6}$ on CMB scales. The action has no inflation
(`04_impact.md` §6, $r \ge 0.28$), so it already owes an explanation of homogeneity at
$10^{-5}$; this adds a second field that must be homogeneous at the same level. Same debt,
not a new one — but now with a second observable attached.

## 4. Signatures — or their absence

- $\alpha$ and $G$ oscillate at $f = m_\chi/2\pi = 2.5$ THz (corrects the "16 THz" of
  `04d_circle.md` §4, which omitted $2\pi$) with amplitude $\delta\alpha/\alpha = \sqrt{2\rho_m}/(m_\chi M_{Pl}) \approx 2\times10^{-31}$
  ($6\times10^{-29}$ in a $10^5$ overdensity). Unobservable by any proposed clock.
- Direct detection: nothing — no particle, gravitational-strength coupling.
- Indirect: nothing — it does not decay ($\tau \sim 10^{38}$ yr) or annihilate.
- Astrophysics: CDM.

The only laboratory handle on this dark matter is the *stabilizer* that makes it possible:
P1, the composition-dependent fifth force at $2$–$66\,\mu$m. That is the honest shape of the
family: it is invisible as dark matter and visible as a fifth force, and the two stand or fall
together.

## 5. Kill criteria (pre-registered, 2026-09-20)

- **K1.** No gravitational-strength, composition-dependent Yukawa force with range in
  $2$–$66\,\mu$m (P1 emptied). Kills the stabilizer, hence $\chi$, hence this family.
- **K2.** Evidence that $T_R > T_o \sim$ few TeV — e.g. a primordial gravitational-wave
  background or a relic requiring reheating above the TeV scale. Kills by overclosure.
- **K3.** Any detection of dark-matter self-interaction ($\sigma/m > 0$), decay, annihilation,
  or a direct-detection particle signal.
- **K4.** CDM isocurvature above the level set by whatever homogeneity mechanism the collision is
  eventually given (currently: any detection of $\beta_{\text{iso}}$ at the $10^{-2}$ level is a
  tension; a detection at $\beta_{\text{iso}} \gtrsim 0.1$ kills).

## 6. Generic vs BMI-specific

| item | generic | BMI-specific |
|---|---|---|
| misalignment production of a light scalar | axion / moduli DM | the scalar is the width of the dimension shared by the two universes |
| $T_R < T_o$ from thermal-shift overclosure | generic moduli problem | $T_R$ is the impact temperature; the bound becomes $h < 0.07$ on the collision |
| CDM phenomenology | generic | — |
| fifth-force ↔ dark-matter link | dilaton DM models | the link runs through the Casimir + $\delta_1$ stabilizer with a two-sided window |

## 7. [verify] carried forward

$g_*$ dilution between $T_R$ and $T_e$ (factor $\sim 0.3$ in $\Omega_\chi$, i.e. $\sim 0.5$ in
$\delta_z$); leading-Boltzmann form of the KK free energy near $x \sim 3$ (higher levels
contribute at the 10% level); $M_6$ and hence the $h$ bound; whether $\delta_z$ carries
back-reaction on the radion at the impact (the two moduli mix at $\Omega \to 1$).
