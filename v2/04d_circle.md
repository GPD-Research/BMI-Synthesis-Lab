# 04d — Stabilizing the circle

Milestone 5d. `04c_approach.md` §6 found that the circle radius $\ell_z$ is a flat direction of
the fixed action and sets the SM gauge couplings ($1/g_4^2 \propto \ell_z$). A flat direction
coupled to $\alpha$ is excluded by atomic clocks and Eöt-Wash; the action must stabilize it or
die. This file works through the finite menu declared in `ledger.md`. Numbers: `tests/circle.py`.

| result | status |
|---|---|
| the SM on the brane fixes the sign of the Casimir energy: 62 more fermionic than bosonic degrees of freedom, repulsive, $V_z = C_z/\ell_z^4$, $C_z \approx 3\times10^{-3}$ | derived (O(1) coefficient [verify]) |
| **option 0** (terms already in the action: Casimir + $V_* \propto \ell_z$): a minimum exists at $\ell_z^{-1} \approx 7$ meV and tracks the dark-energy roll — excluded by LHC and by $\Delta\alpha/\alpha$ | dead |
| **option A** (Casimir + negative detuning $\delta_1$ of $\sigma_1$): minimum at $\ell_z^5 = 4C_z/\pi\lvert\delta_1\rvert$, one new number → **parameter #8, taken** | derived |
| modulus mass $m_\chi = 1.0\times10^{-2}\,\mathrm{eV}\,(\ell_z^{-1}/10\,\mathrm{TeV})^2$; Eöt-Wash needs $m_\chi > 3$ meV; $\lvert\delta_1\rvert < \sigma_1$ caps it: $5.4\ \mathrm{TeV} < \ell_z^{-1} < 29\ \mathrm{TeV}$ | derived (window from two conditions) |
| **prediction (pre-registered, dated 2026-09-20)**: a gravitational-strength Yukawa force, range $2$–$66\ \mu$m, composition-dependent (couples to $\alpha$) | falsifiable by next-generation Eöt-Wash / Casimir-force experiments |
| $\alpha$ drift at the minimum: zero (the minimum depends on neither $\phi$ nor $\Phi$) | derived; clock bounds satisfied |
| cosmological moduli problem: an O(1) early displacement overcloses by $10^{12}$; the modulus does not decay ($\tau \sim 10^{38}$ yr) | derived; kill risk unless $T_R \lesssim \ell_z^{-1}/14$ |
| if instead the displacement is $\lvert\Delta\ell_z/\ell_z\rvert \sim 10^{-6}$, the oscillating circle **is** cold dark matter (fourth family, BMI-specific) | conditional; taken in `05_dark_sector.md`, where the "$T_R$ to 0.4%" of §4 is corrected |
| option B (flux, new 1-form) reproduces A with two numbers; option C (Goldberger–Wise) needs new codimension-2 branes | not taken |

## 0. Why this is forced now

`tests/check_background.py` verifies the AdS$_6$ background for every $\ell_z$: the metric
$e^{-2y/\ell}(\eta_{\mu\nu}dx^\mu dx^\nu + dz^2) + dy^2$ is locally AdS$_6$ whatever the
identification $z \sim z + 2\pi\ell_z$. Dimensionally reducing, $\ell_z$ is a 4D scalar
$\chi = M_{Pl}\ln(\ell_z/\ell_z^{(0)})$ (kinetic normalisation O(1) [verify]) with

- $M_{Pl}^2 \propto \ell_z$ (`01_action.md` §1) — a Brans–Dicke coupling to all matter;
- $1/g_4^2 \propto \ell_z$ for the brane gauge fields — a dilaton coupling to $\alpha$.

Massless, it is a gravitational-strength fifth force that violates the equivalence principle
(excluded, Eöt-Wash 2008: gravitational strength needs range $< 56\,\mu$m) and it makes
$\alpha$ track the cosmic expansion (excluded, $\lvert\Delta\alpha/\alpha\rvert < 10^{-5}$ at
$z\sim3$). So: what potential does the action give it?

## 1. The Casimir term and its sign

Every brane-localised field on the 4-brane wrapping $S^1/\mathbb Z_2$ has a KK tower at
$n/\ell_z$ (`02b_localization.md` §4). Its vacuum energy per unit 4-volume is
(Appelquist–Chodos form, orbifold halving the modes; O(1) coefficient [verify])
$$
V_z(\ell_z) = +62\,\frac{3\zeta(5)}{64\pi^6}\,\frac{1}{\ell_z^4}
\equiv \frac{C_z}{\ell_z^4},
$$
with periodic fermions; the 62 is the SM's fermionic minus bosonic on-shell count
(45 Weyl × 2 = 90, minus 12 gauge × 2 + Higgs 4 = 28). So $C_z = 62 \times 5.1\times10^{-5} = 3.1\times10^{-3} > 0$: the
force is **repulsive**, the circle wants to grow. Bulk fields (graviton 9, $\Phi$ 1) add 10
bosonic degrees of freedom and do not flip the sign. This is a fact about *our* field content,
not a choice: a Scherk–Schwarz twist (antiperiodic fermions) would flip it but is an extra
discrete choice, and it would make $V_z$ attractive with no short-distance repulsion —
collapse to $\ell_z \to 0$, worse. Stabilization therefore needs something that grows with
$\ell_z$ and is *negative*.

## 2. Option 0: what the action already contains

The bulk-scalar term is $V_* = \pi\ell_z\ell V_0/5$ (`03_background.md` §2): positive and
linear in $\ell_z$. Together with §1,
$$
V(\ell_z) = \frac{C_z}{\ell_z^4} + \frac{\pi\ell V_0}{5}\,e^{-c\Phi_4/M_{Pl}}\,\ell_z
$$
*does* have a minimum, at $\ell_z^5 = 4C_z/(\pi\ell V_0/5)$. But the second term is the
dark energy, $\approx (2.25\ \mathrm{meV})^4$ today, so the minimum sits at
$\ell_z^{-1} = (\rho_*/4C_z)^{1/4} \approx 7$ meV — SM KK modes at 7 meV, excluded
by $10^{15}$. And since $V_*$ rolls, $d\ln\ell_z/d\ln V_* = -1/5$: a thawing roll of
$\Delta\ln V \sim 0.3$ since $z\sim3$ gives $\lvert\Delta\alpha/\alpha\rvert \sim 0.06$. Dead
twice. Recorded because it is the *only* stabilizer that costs nothing, and it fails.

## 3. Option A: Casimir against a negative tension detuning — taken

The RS tuning $\sigma_1 = 8M_6^4/\ell$ was imposed in `01_action.md` §3 for a flat brane. Let
$\sigma_1 \to \sigma_1 + \delta_1$. The brane wraps the circle, so its 4D vacuum energy is
$\pi\ell_z\delta_1$: linear in $\ell_z$, and negative if $\delta_1 < 0$. Then
$$
V(\ell_z) = \frac{C_z}{\ell_z^4} + \pi\delta_1\,\ell_z,
\qquad
\bar\ell_z^5 = \frac{4C_z}{\pi\lvert\delta_1\rvert},
\qquad
V(\bar\ell_z) = -\frac{3C_z}{\bar\ell_z^4} .
$$
Three consequences.

**(a) One new parameter.** $\delta_1$ is #8 in the ledger. It is *not* the same number as
$\delta\sigma_2$ (#4): that detunes $\Sigma_2$ and drives the radion; this detunes $\Sigma_1$.
The negative vacuum energy at the minimum, $-(3C_z)^{1/4}/\bar\ell_z \approx -(3\ \mathrm{TeV})^4$,
must be cancelled by retuning $\Lambda_6$ — the cosmological-constant problem in its usual
form, not a new one, but stated: the action does not explain why $\rho_\Lambda$ is small, here
or anywhere.

**(b) The modulus mass and a two-sided window.** With $\chi = M_{Pl}\ln\ell_z$,
$$
m_\chi^2 = \frac{\bar\ell_z^2 V''(\bar\ell_z)}{M_{Pl}^2} = \frac{20\,C_z}{\bar\ell_z^4 M_{Pl}^2}
\quad\Rightarrow\quad
m_\chi = 1.0\times10^{-2}\ \mathrm{eV}\left(\frac{\bar\ell_z^{-1}}{10\ \mathrm{TeV}}\right)^{2} .
$$
Eöt-Wash excludes a gravitational-strength Yukawa with range above $\sim 60\,\mu$m, i.e.
$m_\chi \gtrsim 3$ meV: $\ell_z^{-1} \gtrsim 5.4$ TeV (the LHC bound on SM KK modes,
$\gtrsim 5$ TeV, lands in the same place independently). From above, the detuning must be a
detuning: $\lvert\delta_1\rvert < \sigma_1$ gives $\ell_z^{-1} \lesssim 29$ TeV (using
$M_6 \approx 27$ PeV for $\ell = 10\,\mu$m [verify]). So
$$
5.4\ \mathrm{TeV} \;\lesssim\; \ell_z^{-1} \;\lesssim\; 29\ \mathrm{TeV},
\qquad
2\,\mu\mathrm{m} \;\lesssim\; m_\chi^{-1} \;\lesssim\; 66\,\mu\mathrm{m}.
$$

**(c) The prediction.** *Superseded in milestone 7 (`06_predictions.md` §1–2, §4a): the canonical
normalisation is $\chi = \sqrt{3/2}M_{Pl}\ln\ell_z$, the strength is $\alpha_Y \approx 270$ (QCD
running of $1/g_s^2 \propto \ell_z$), composition-independent to $10^{-3}$, and Eöt-Wash 2020 at
that strength moves the lower edge to $\ell_z^{-1} > 14$ TeV, $\lambda < 12\,\mu$m. The text below
is kept as registered.* The modulus mediates a Yukawa force of gravitational strength
($\alpha_Y$ of order one, exact coefficient from the $\chi$ normalisation [verify]) with range
in the window above, and it is composition-dependent because $\chi$ couples to $\alpha$ (a
$\Delta\alpha$-type charge $\propto$ electromagnetic binding energy fraction). This is the
first statement in v2 that is (i) forced once the stabilizer is chosen, (ii) not yet excluded,
and (iii) within reach of running experiments (Eöt-Wash, Casimir-force and levitated-sensor
searches at 1–50 $\mu$m). Pre-registered here, 2026-09-20. If the range window is emptied, the
Casimir+detuning stabilizer is dead and, with options B/C, the fixed-circle geometry with it.

**(d) $\alpha$ today.** The minimum depends on $C_z$ and $\delta_1$ only — not on the
radion $\phi$ (the Casimir term lives on $\Sigma_1$ at $y=0$) nor on $\Phi$. So $\alpha$ does not
drift with the merger or the dark-energy roll: the clock and quasar bounds are satisfied
identically. The "still-settling constant" of `00_axiom.md` is, in this action, settled.

## 4. The circle in the early universe: moduli problem, or dark matter

$\chi$ is light and gravitationally coupled: the classic moduli problem. It starts oscillating
when $H = m_\chi$, at $T_o \approx 2.7$ TeV $(\ell_z^{-1}/10\,\mathrm{TeV})$ — the
same epoch as the KK scale, not a coincidence ($T_o^2 \sim m_\chi M_{Pl} \sim
\sqrt{C_z}\,\ell_z^{-2}$). Its energy then redshifts as matter while radiation wins
until $T_e$, and it never decays (rate $m_\chi^3/M_{Pl}^2$, lifetime $10^{38}$ yr).

- If the KK modes were ever thermal ($T_R \gtrsim \ell_z^{-1}$), the thermal free energy
  $\propto T^5\ell_z$ shifts the minimum by O(1), and $\rho_\chi/\rho_r$ at $T_e$
  is $\sim 6\times10^{11}$. **Overclosure.** So the action requires
  $T_R < \ell_z^{-1}$: a *reheating bound* of a few TeV, below the KK scale, stronger
  than the $h\lesssim1$ bound of `04c_approach.md` §5.
- With $T_R < \ell_z^{-1}$ the shift is Boltzmann-suppressed. **Corrected in `05_dark_sector.md` §1:**
  the shift is a *moving minimum*, and once $H < m_\chi$ (i.e. $T < T_o \approx 0.27\,\ell_z^{-1}$)
  the field follows it adiabatically and nothing is excited; if instead $T_R > T_o$ the shift
  at $T_o$ is O(0.4) and overcloses. The bound is therefore $T_R < T_o$, and the thermal shift
  cannot be tuned to give $\Omega_{DM}$. The earlier text here ("$T_R \approx 730$ GeV tuned to
  0.4%") was wrong and is retracted; the working mechanism is the collision's own offset
  $\delta_z$ of the circle (`05_dark_sector.md` §2).

So there is a **fourth dark-matter family**, and it is the first one that is BMI-specific in
mechanism: the dark matter is the still-oscillating width of the shared circle — a coherent
scalar of mass $10^{-2}$ eV, cold from $T\sim$ TeV, collisionless, with no particle-physics
content. Its price is one number, the offset $\delta_z \sim 10^{-6}$ left by the impact. Its
signatures: none in direct detection ($\alpha$ oscillates at 2.5 THz with amplitude
$10^{-31}$); a Jeans scale far below galactic; structure formation identical to CDM. It is
falsified with option A itself if the fifth-force window is emptied, and independently if a
primordial gravitational-wave or reheating signal shows $T_R \gtrsim$ few TeV.

This is the honest form of the founding intuition "dark matter is an inherited, still-settling
quantity": it can be, in this action, if and only if the circle is stabilized as in §3, the
collision reheated below $T_o$, and the collision left the circle offset by a part in $10^6$.
Taken as milestone 6.

## 5. Options B and C

**B, flux.** A new bulk 1-form with $n$ units through $z$ contributes a term $\propto +1/\ell_z$ (flux quantum and coupling: two numbers)
(repulsive, softer than Casimir). Against $\pi\delta_1\ell_z$ it stabilizes with
$\bar\ell_z^2 \propto 1/\lvert\delta_1\rvert$ and $m_\chi^2 \propto 1/(\bar\ell_z^4 M_{Pl}^2)$ as in A:
same Eöt-Wash window, same moduli problem, two new numbers and a new field, and
`02b_localization.md` forbids bulk gauge fields with charged matter, so the form must be
inert. Dominated by A; not taken.

**C, Goldberger–Wise.** A second bulk scalar with potentials at the ends of the *circle* needs
codimension-2 branes at the orbifold fixed points $z = 0, \pi\ell_z$ — objects the action does
not contain. New content, not a stabilizer of the existing one; not taken. Recorded so the
menu is closed.

## 6. Generic vs BMI-specific

| item | generic | BMI-specific |
|---|---|---|
| Casimir sign from the SM count | any circle with SM towers | — |
| Casimir + negative tension minimum, meV-scale modulus | any 5D-brane-on-circle model | the tension is the RS-tuned $\sigma_1$ of `01_action.md`; the window ties $\ell_z$ to Eöt-Wash |
| moduli problem, $T_R < \ell_z^{-1}$ | generic | the reheating is the impact of `04_impact.md` |
| oscillating circle as DM | "moduli dark matter" is known | the modulus is the shared dimension between the two universes; abundance ↔ $T_R$ of the collision |

## 7. [verify] carried forward

O(1) Casimir coefficient and orbifold factor; canonical normalisation of $\chi$ (Brans–Dicke
mixing with $M_{Pl}^2 \propto \ell_z$ may shift $m_\chi$ by O(1) and sets $\alpha_Y$
exactly); $M_6$ for the upper edge of the window; whether $\delta_1 \ne 0$ back-reacts on the
AdS$_6$ slice beyond a constant shift (it should appear as a de Sitter/anti-de Sitter brane
curvature absorbed in the $\Lambda_6$ retuning of §3a).
