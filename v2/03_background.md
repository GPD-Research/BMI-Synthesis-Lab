# 03 — Background: the low-energy 4D theory in closed form and its FRW solution

Milestone 4. Inputs: the action of `01_action.md`, the AdS$_6$ slice and Planck relation of
`02_effective_4d.md` §1–2, the localization results of `02b_localization.md` (only gravity,
the radion and the bulk scalar $\Phi$ are bulk fields at this milestone). Checks:
`tests/check_radion.py` (symbolic), `tests/background_frw.py` (numerical). Everything marked
**[verify]** is a stated approximation, not an omitted derivation.

## 0. Corrections to earlier files made here

- `02_effective_4d.md` §4 guessed the 6D Brans–Dicke prefactor as $\tfrac32$. Derived value:
  $\tfrac43$ (§1). Cassini then gives $\phi_0/\ell \gtrsim 3.4$, not $5$; $\Omega \lesssim 0.032$.
  §5 numbers there (mirror proton $\lesssim 6$ MeV, $n_2/n_1 \gtrsim 750$) become
  $\lesssim 30$ MeV and $\gtrsim 165$. Corrected in place with a pointer here.
- `01_action.md` §2.1 assumed $\Phi$ has a static profile $\Phi(y)$. It has none (§2): with
  $\Phi$-independent tensions the exponential potential admits no static solution, so $\Phi$
  is a *rolling* zero mode. Nothing in the action changes; the interpretation does.

## 1. The radion sector (moduli approximation)

At energies below $1/\ell$ the gravitational sector has two light fields: the 4D metric
$g_{\mu\nu}$ and the separation $\phi(x)$. In this regime the effective action is the
difference of the induced Einstein–Hilbert terms on the two branes (Kanno & Soda 2002;
Brax, van de Bruck, Davis & Rhodes 2002), each 5-dimensional and reduced on the circle it
wraps. Since the induced metric on $\Sigma_2$ is $\Omega^2$ times that on $\Sigma_1$ with
$\Omega = e^{-\phi/\ell}$, and the circle radius there is $\Omega\ell_z$, the $\Sigma_2$ term
carries $\Omega^3$ (not $\Omega^2$ as in 5D). The conformal identity gives, exactly
(`tests/check_radion.py`, which also reproduces the 5D Garriga–Tanaka result as a control):
$$
S_{\text{rad}} = \frac{M_5^3\ell}{6}\int d^4x\sqrt{-g}\left[\Psi R_4
 - \frac{\omega(\Psi)}{\Psi}(\partial\Psi)^2\right],
\qquad \Psi = 1-\Omega^3,\qquad
\boxed{\;\omega(\Psi) = \frac{4\Psi}{3(1-\Psi)} = \frac43\left(e^{3\phi/\ell}-1\right)\;}
$$
This replaces the **[verify]** in `02_effective_4d.md` §4. The approximation is the standard
low-energy (gradient) expansion; its validity in $D=6$ with a warped circle is **[verify]**
only in the sense that the next order ($\ell^2 R_4$ terms) has not been computed — it is the
same order at which `02_effective_4d.md` §3 already truncates.

**Cassini.** $\omega > 4\times10^4$ (Bertotti, Iess & Tortora 2003) gives
$$
\phi_0/\ell > \tfrac13\ln\!\left(1+\tfrac34\omega_C\right) = 3.44,
\qquad \Omega_0 < 0.032 .
$$

**Radion kinetic term and canonical field.** Writing $\tfrac12 K(\phi)(\partial\phi)^2$,
$$
K(\phi) = \frac{4M_5^3}{\ell}\,e^{-3\phi/\ell} = \frac{12M_{\text{Pl}}^2}{\ell^2}\,\Omega^3,
\qquad
\chi \equiv -\frac{4}{\sqrt3}\,M_{\text{Pl}}\,\Omega^{3/2}
$$
is canonical. This is the $K(\phi)$ listed as missing in `STATUS.md`. The radion's full field
range for $\Omega < 0.032$ is $|\chi| < 0.013\,M_{\text{Pl}}$.

**Radion potential.** From `02_effective_4d.md` §4 with the $\Phi$ term moved to §2 below,
$$
V_{\text{rad}}(\phi) = \delta\sigma_2^{(5)}\,\Omega^4
 = \delta\sigma_2^{(5)}\left(\frac{\sqrt3\,\chi}{4M_{\text{Pl}}}\right)^{8/3},
\qquad \delta\sigma_2^{(5)} \equiv \pi\ell_z(\sigma_2+\sigma_1).
$$
The slow-roll parameter is $\epsilon_\chi = \tfrac{M_{\text{Pl}}^2}{2}(V'/V)^2 = \tfrac{2}{3\Omega^3} > 2\times10^4$:
**the radion can never drive acceleration.** Its sign fixes the direction of motion:
$\delta\sigma_2 < 0$ pulls the branes together (merger), $\delta\sigma_2 > 0$ pushes them apart.
"The collision continues" is therefore the statement $\sigma_2 < -\sigma_1$, a sign of ledger
parameter #4, and nothing else.

## 2. The bulk scalar sector: no static profile, a rolling zero mode

The static probe equation on the slice, $\Phi'' - \tfrac5\ell\Phi' = V'(\Phi)$, integrates to
$\int_0^\phi dy\,e^{-5y/\ell}\,V'(\Phi) = e^{-5y/\ell}\Phi'\big|_0^\phi$, which vanishes for
Neumann conditions (tensions independent of $\Phi$, `01_action.md` §2). Since
$V' = -(c/M_6^2)V < 0$ everywhere, there is **no static solution**. The alternatives were
already rejected in `01_action.md` §2 (Goldberger–Wise brane potentials add parameters). So
$\Phi$ rolls, and at lowest order in $\ell\partial_x$ it is $y$-independent: $\Phi = \Phi(x)$,
which satisfies both Neumann conditions exactly and the bulk equation up to the $V'$ source,
which is of order $V_0/|\Lambda_6|$ and is the same small quantity that lets the AdS slice be the
background at all.

Reducing on the slice (`tests/check_radion.py`):
$$
S_\Phi = \int d^4x\sqrt{-g}\left[-\frac{M_{\text{Pl}}^2(\phi)}{2M_6^4}(\partial\Phi)^2
 - \frac{\pi\ell_z\ell}{5}\left(1-\Omega^5\right)V_0\,e^{-c\Phi/M_6^2}\right].
$$
With $\Omega^3 \lesssim 3\times10^{-5}$ the $\phi$-dependence of both prefactors is negligible
and the canonical field is $\Phi_4 = (M_{\text{Pl}}/M_6^2)\,\Phi$. Then
$$
\boxed{\;V(\Phi_4) = V_*\,e^{-c\,\Phi_4/M_{\text{Pl}}},\qquad V_* = \frac{\pi\ell_z\ell}{5}\,V_0\;}
$$
— the 4D slope in reduced-Planck units is **exactly the ledger parameter $c$**, with no
leftover geometric factor (the same $\pi\ell_z\ell/3$ that makes $M_{\text{Pl}}^2$ cancels in
the canonical normalisation). $\Phi$ couples to brane matter only through gravity
(tensions are $\Phi$-independent), so it is a pure quintessence field: no fifth force, no
Cassini constraint, no varying constants on $\Sigma_1$.

Bookkeeping: the observable combination is $V_*e^{-c\Phi_{4,i}/M_{\text{Pl}}}$; the initial value
$\Phi_{4,i}$ is an integration constant degenerate with $V_0$ and is absorbed into ledger #5.
No new parameter.

## 3. The FRW background

Flat FRW on $\Sigma_1$ with baryons, mirror matter (pressureless: `02_effective_4d.md` §5, and
the mirror sector must be cold enough — milestone 5), radiation, $\Phi_4$ and $\chi$. The
$E_{\mu\nu}$ dark radiation is carried along as $\mathcal C/a^4$ and set to zero here (its
value is milestone 5's).

### 3.1 The radion is a spectator, forced by the CMB

Because $m^{(2)} \propto \Omega$, the mirror-DM mass drift since recombination is
$\Delta\ln m_{\text{DM}} = -\Delta\phi/\ell$, and the acoustic peaks require
$|\Delta\ln m_{\text{DM}}| \lesssim 0.05$ (order of magnitude; variable-mass-DM CMB limits
**[verify: quote a specific analysis]**). With the terminal-velocity estimate
$\dot\chi \simeq -V'/(3H_0)$ (matter era, $H$ of order $H_0$) in the matter era, `tests/background_frw.py` gives
$$
\Delta\ln\Omega = \frac{f_{\text{rad}}}{3\Omega^3},
\qquad f_{\text{rad}} \equiv \frac{V_{\text{rad}}}{3M_{\text{Pl}}^2H^2},
$$
(per Hubble time), so the bound is
$$
f_{\text{rad}}(t_0) \lesssim 0.15\,\Omega_0^3 < 5\times10^{-6},
\qquad
\left|\frac{\dot G}{G}\right| = \frac{3\Omega^3}{1-\Omega^3}\,\left|\frac{\dot\phi}{\ell}\right|
 \lesssim 3\times10^{-16}\ \mathrm{yr}^{-1}.
$$
Three consequences, none chosen:

1. **Kill criterion 2 (LLR, $|\dot G/G| < 10^{-13}\,\mathrm{yr}^{-1}$) passes** by three orders
   of magnitude, and does so *because of* the CMB bound, not independently of it.
2. **The merger is invisible in the expansion history.** $f_{\text{rad}} < 10^{-5}$ means the
   inter-brane potential contributes nothing measurable to $w(z)$. `01_action.md` §4's hope
   that dark energy is the inter-brane potential is dead; recorded as a negative result below.
3. **The kill risk of `02_effective_4d.md` §5.2 is resolved in the safe direction**: the merger
   is slow enough for CDM. The price is that "ongoing collision" has exactly two observable
   handles left: a percent-level drift of the DM mass and $\dot G/G \sim 10^{-16}\,\mathrm{yr}^{-1}$.

### 3.2 Dark energy is the bulk scalar: thawing quintessence with slope $c$

With the radion frozen, the only dynamical dark energy is $\Phi_4$. Hubble friction freezes it
in the radiation era (for $c < \sqrt3$ there is no early scaling attractor with
$\Omega_\Phi > 0$), so the solution is the *thawing* branch. `tests/background_frw.py`
integrates it with Planck-2018 $\Omega_m, \Omega_r$ and $V_*$ fixed by $\Omega_{DE}(t_0) = 0.685$:

| $c$ | $w(z{=}0)$ | $w_0$ (CPL) | $w_a$ (CPL) | $w(z{=}1)$ | $w_\infty = -1 + c^2/3$ |
|---|---|---|---|---|---|
| 0.1 | $-0.999$ | $-0.999$ | $-0.002$ | $-1.000$ | $-0.997$ |
| 0.3 | $-0.987$ | $-0.987$ | $-0.018$ | $-0.997$ | $-0.970$ |
| 0.5 | $-0.963$ | $-0.964$ | $-0.052$ | $-0.991$ | $-0.917$ |
| 0.7 | $-0.927$ | $-0.929$ | $-0.102$ | $-0.982$ | $-0.837$ |
| 1.0 | $-0.849$ | $-0.850$ | $-0.211$ | $-0.959$ | $-0.667$ |
| 1.3 | $-0.739$ | $-0.735$ | $-0.364$ | $-0.921$ | $-0.437$ |
| 1.6 | $-0.591$ | $-0.571$ | $-0.563$ | $-0.854$ | $-0.147$ |

Forced structure of the prediction:

- **$w(z)$ is a one-parameter family** in $c$; $V_0$ only sets $\Omega_{DE}$ today. The
  $(w_0, w_a)$ pairs lie on a curve, $w_a \approx -1.5\,(1+w_0)$ for small $c$ — this is the
  test, not the individual numbers.
- **$w > -1$ always, $w_a < 0$ always.** A canonical scalar cannot be phantom.
- $\Lambda$CDM is the $c \to 0$ limit; the theory contains it and differs from it only for
  $c \gtrsim 0.3$ (where $|1+w_0| > 0.01$).

**Against data (numbers approximate; the pre-registered comparison is milestone 7):**

- Planck 2018 + Pantheon, constant $w$: $w_0 = -1.03 \pm 0.03$. On the thawing branch this
  is $c \lesssim 0.5$.
- DESI DR2 + CMB + SNe (2025) prefer $w_0 \approx -0.75$, $w_a \approx -0.9$, i.e. $w < -1$
  for $z \gtrsim 0.4$. The thawing curve at $w_0 = -0.75$ has $w_a \approx -0.35$, not $-0.9$;
  the DESI *central value* is unreachable. Whether the thawing curve lies inside the DESI
  $2\sigma$ contour is a chain-level question deferred to milestone 7. **Kill criterion 3 is
  therefore open, not passed**: if the phantom preference sharpens, the minimal action is out
  and the only remaining lever is $E_{\mu\nu}$ (dark radiation cannot mimic $w<-1$ either), so
  it would be a genuine death, not a patch.

### 3.3 $\Delta N_{\text{eff}}$

Two contributions: $E_{\mu\nu}$ ($\mathcal C$) and mirror radiation
($\Delta N_{\text{eff}} = 3.044\,(T_2/T_1)^4$ times the mirror-to-visible ratio of relativistic degrees of freedom, for a full mirror sector at
BBN, about $7.4\,(T_2/T_1)^4$). Neither is computable before milestone 5; the Planck bound
$\Delta N_{\text{eff}} \lesssim 0.3$ then requires $T_2/T_1 \lesssim 0.45$ — a *ceiling* the impact
must respect. Note the mirror sector needs $n_2/n_1 \gtrsim 165$ with $T_2 < 0.45\,T_1$: many
more baryons, fewer photons. That is the number milestone 5 must produce or the mirror-SM
choice is dead.

### 3.4 Fate of the cosmos: what the action allows, pre-registered

The founding picture had acceleration as a passing phase — dissipation of the collision
energy eventually forcing a maximum size or a turnaround. Write down what the fixed action
can and cannot do about that, before any data enters.

**The constraint.** On a flat brane $3M_{Pl}^2H^2 = \rho_{\text{tot}}$. Every component with
non-negative energy — matter, radiation, the bulk scalar with $V_0>0$, $\mathcal C>0$ dark
radiation, energy flowing in from $\Sigma_2$ or the bulk — keeps $H^2>0$: expansion can slow
but cannot stop or reverse. "Dissipation" (energy leaving $\Sigma_1$; $\nabla^\mu T_{\mu\nu}
\ne 0$ is allowed on a brane) lowers $\rho$ and makes the universe coast, not turn around.
Extra energy injected by the impact raises $H$; $\Omega_{\text{tot}}=1$ is an identity, not a
ceiling. A static maximum-size state is unstable (Einstein static) in any scalar–tensor
theory. Reversal therefore needs a component with *negative* energy, or positive spatial
curvature (Planck: $\Omega_k = 0.001\pm0.002$; with any residual $V>0$ it does not recollapse).

**Where negative energy can come from inside the budget.** Exactly one place: the radion
potential $V_{\text{rad}} = \delta\sigma_2\,\Omega^4$, whose sign is parameter #4. This *is* the
"resistance to merging" of the founding picture, now with a definite form: for
$\delta\sigma_2<0$ it is negative and grows in magnitude as the branes approach ($\Omega\to1$),
i.e. the branes attract — the ekpyrotic/cyclic mechanism (Steinhardt & Turok 2002). Nothing
else in the action can go negative: $V(\Phi)$ has $V_0>0$ fixed, and $\mathcal C<0$ dilutes as
$a^{-4}$ (an early-universe effect, bounded by BBN, irrelevant to the fate).

| $\delta\sigma_2$ | radion force | late-time behaviour | fate |
|---|---|---|---|
| $>0$ | repulsive, $\phi\to\infty$ | quintessence dominates; $w\to -1+c^2/3$ | eternal expansion, accelerating iff $c<\sqrt2$ (data: $c\lesssim0.5$, so accelerating) |
| $=0$ | none ($\phi$ frozen) | as above | eternal accelerating expansion |
| $<0$ | attractive, $\phi\to0$ | $\lvert\delta\sigma_2\rvert\Omega^4$ eventually overtakes $V_*e^{-c\Phi_4/M_{Pl}}$; $\rho_{\text{tot}}\to0$ then $<0$ | turnaround, then brane collision (a second impact) |

What is fixed by §3.1 either way: today $f_{\text{rad}} < 5\times10^{-6}$, so the third row is a
far-future statement — the merger is presently negligible, and the acceleration is
permanent *on any observable timescale*. The turnaround time in row 3 is computable once
$\lvert\delta\sigma_2\rvert$ has a lower bound; with the *upper* bound of §3.1 the earliest
possible turnaround is $\gtrsim 200$ Gyr (`04_impact.md` §5), and near
$\Omega\to1$ the moduli approximation of §1 fails and the full junction problem must be
solved (also $M_{Pl}^2\propto 1-\Omega^3\to0$ there). The sign of $\delta\sigma_2$ is a
kinematic question for the impact (milestone 5): branes that separated against an attraction
vs. branes pushed apart. Not adopted: any feature in $V(\Phi)$ (bump, negative minimum) that
would end acceleration through the dark-energy scalar — that is a new shape choice and +1
parameter, logged as a fork in `ledger.md`, to be taken only if milestone 7 kills the pure
exponential.

**Retracted-lineage note.** v1's "bridge impedance" was one scalar resistance. Here the
merger involves two mechanisms of different sign and scaling — the attractive/repulsive
tension detuning $\delta\sigma_2\Omega^4$ and the warp-induced radion stiffness
$K(\phi)\propto\Omega^3$ — neither of which is an impedance; R6 stays retracted.

## 4. Negative results recorded

| claim | status | reason |
|---|---|---|
| dark energy = inter-brane potential (`01_action.md` §4, v1 Ch 7.4) | **dead** | $f_{\text{rad}} < 5\times10^{-6}$ forced by CMB DM-mass bound (§3.1) |
| merger dynamics visible in $w(z)$ | dead | same |
| static bulk-scalar profile $\Phi(y)$ | dead | Neumann + fixed-sign $V'$ (§2) |
| radion as slow-roll field | dead | $\epsilon_\chi = 2/3\Omega^3$ (§1) |

Surviving: dark energy as the bulk scalar with slope $c$; merger as a percent-level DM-mass
drift; $\dot G/G \sim 10^{-16}\,\mathrm{yr}^{-1}$.

## 5. Generic vs BMI-specific

| result | generic | BMI-specific |
|---|---|---|
| $\omega = \tfrac43(e^{3\phi/\ell}-1)$ | moduli approximation | 6D warped-circle exponent and prefactor |
| exponential quintessence, thawing | standard (Ratra–Peebles, Scherrer–Sen) | slope $= c$ exactly, tied to the bulk potential; $\Lambda$ as $c\to0$ |
| radion spectator | RS without stabilisation | bound comes from *mirror DM mass drift*, a BMI structure |
| $T_2/T_1 < 0.45$ with $n_2/n_1 > 165$ | mirror-matter $N_{\text{eff}}$ bound | inverted density ratio is BMI's |

## 6. Open [verify] items carried forward

1. Next order in the gradient expansion ($\ell^2 R_4^2$-type terms) for the 6D moduli action.
2. A specific CMB limit on $\Delta\ln m_{\text{DM}}$ since recombination (replace $0.05$).
3. Milestone 5: $\mathcal C$, $T_2/T_1$, $n_2/n_1$, and whether the impact can deliver
   $\delta\sigma_2<0$ with $f_{\text{rad}} < 5\times10^{-6}$ today.
4. Milestone 7: thawing curve vs DESI chains; pre-register $(w_0, w_a)(c)$ before looking.
