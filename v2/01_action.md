# 01 — The Action

Milestone 2. This file replaces `01_action_skeleton.md` as the definition of the theory.
Everything in later files must be derived from the action written here. Where a formula is
standard, the source is cited; where a choice is made, it is marked **[choice]** and its
alternatives are listed so the choice can be revisited without touching anything else.
Statements marked **[verify]** are standard results quoted from memory whose numerical factors
must be re-derived in milestone 3 before they are used.

## 1. Geometry

**Bulk.** $\mathcal M_6$ with coordinates $X^A = (x^\mu, y, z)$, $\mu = 0..3$, metric $G_{AB}$,
signature $(-,+,+,+,+,+)$. Bulk Planck mass $M_6$.

**Extra dimensions [choice].** $z$ is compact, $z \sim z + 2\pi \ell_z$, with a
$\mathbb Z_2$ identification $z \sim -z$ (orbifold $S^1/\mathbb Z_2$): the orbifold is not a
choice but forced by the existence of chiral 4D fermions on a brane whose worldvolume
includes the circle (`02b_localization.md` §4.1). $y$ is an interval
$0 \le y \le \phi$ bounded by the two branes. Alternatives rejected: (a) both $y, z$
non-compact with codimension-2 branes — conical deficit angles make the junction problem
ill-posed for brane matter (Cline, Descheneau, Giovannini & Vinet 2003); (b) both compact —
then there is no interval to merge across.

**Branes.** $\Sigma_1$ (ours) at $y = 0$, $\Sigma_2$ at $y = \phi(x)$. Each brane is a
4-brane (five-dimensional worldvolume) wrapping the $z$ circle. At energies below
$1/\ell_z$ the $z$ dependence is frozen and each brane is an effective 3-brane; the bulk is
an effective 5D space with
$$
M_5^3 \equiv \pi \ell_z\, M_6^4
$$
(the orbifold halves the circle volume). Only $M_5$ is observable until $z$-KK modes are probed. $M_6$ and $\ell_z$ therefore enter
the ledger as the single number $M_5$. $\ell_z$ is the circle radius *at $\Sigma_1$*; in the
warped background of §3 the proper radius at $y$ is $\ell_z e^{-y/\ell}$.

**Correspondence with the original picture.** The v1 genesis was two manifolds sharing two
compactified spatial dimensions: ours is 3 space + 2 shared + time (6D), the other has at least
3 space + the same 2 shared + time, possibly more. In the language above the shared pair is
the bulk $(y, z)$, and each manifold is a brane extended in its own three space dimensions.
Two things follow. (i) If both manifolds filled the shared pair completely they would already
coincide and there would be nothing to merge; so one shared direction ($z$) is wrapped by both
and the other ($y$) is the one along which they are displaced. This is not an extra
assumption, it is what "separated and merging" means in a 2D shared space, and it is the only
arrangement whose junction problem is well-posed (see the codimension-2 remark above; a 3+3+1
split would make the shared space 3D and the problem worse). (ii) Any additional internal
dimensions of $\Sigma_2$ are invisible from $\Sigma_1$ except through how sector-2 matter
dilutes and gravitates. v2 takes the minimal 3+1 worldvolume for $\Sigma_2$ **[choice]**; a
higher-dimensional $\Sigma_2$ is the fallback and costs one parameter (an effective equation of
state for its matter as seen from 4D).

**Fork 1 [choice].** The bulk is warped with $\Sigma_1$ at the ultraviolet (large-warp-factor)
end. Reason: in this configuration $G_N$ on $\Sigma_1$ depends on the brane separation only
through $e^{-3\phi/\ell}$ (§4), so an ongoing merger does not violate lunar-laser-ranging bounds
on $\dot G/G$ without tuning. Alternative rejected: flat bulk, where $G_N^{-1} \propto \phi$
and the merger timescale must exceed $\sim 500\,H_0^{-1}$ (`01_action_skeleton_superseded.md` §4.1).

**Separation field.** $\phi(x)$ is the proper distance between the branes along $\partial_y$.
It is the radion of two-brane Randall–Sundrum models (Randall & Sundrum 1999a;
Goldberger & Wise 1999) and the inspiral coordinate of the cyclic model
(Steinhardt & Turok 2002). Its dynamics are *not* postulated; they follow from §2.

## 2. Action

$$
S = S_{\text{bulk}} + S_{\Sigma_1} + S_{\Sigma_2} + S_{\text{GHY}}
$$

$$
S_{\text{bulk}} = \int_{\mathcal M_6} d^6X \sqrt{-G}\,
\left[ \frac{M_6^4}{2}\, R_6 \;-\; \Lambda_6 \;-\; \frac12\, G^{AB}\partial_A\Phi\,\partial_B\Phi \;-\; V(\Phi) \right]
$$

$$
S_{\Sigma_i} = \int_{\Sigma_i} d^5\xi \sqrt{-\gamma_i}\,
\left[ -\sigma_i \;+\; \mathcal L^{(i)}_{\text{matter}}(\gamma_i, \psi_i) \right],
\qquad i = 1, 2
$$

$$
S_{\text{GHY}} = M_6^4 \sum_{i} \int_{\Sigma_i} d^5\xi \sqrt{-\gamma_i}\; [K_i]
$$

with $\gamma_i$ the induced metric on $\Sigma_i$, $K_i$ the trace of its extrinsic curvature,
and $[K_i]$ the jump across the brane. The GHY terms are required for the variational
problem to yield the Israel junction conditions (Israel 1966; Chamblin & Reall 1999).

**Field content.**

| symbol | what it is | class |
|---|---|---|
| $G_{AB}$ | bulk metric | field |
| $\Phi$ | one real bulk scalar | field |
| $\Lambda_6$ | bulk cosmological constant; sets the warp length $\ell$ (§3) | parameter, via $\ell$ |
| $V(\Phi)$ | bulk scalar potential, form fixed in §2.1 | 2 parameters |
| $\sigma_1, \sigma_2$ | brane tensions, constants | §3 |
| $\mathcal L^{(1)}_{\text{matter}}$ | the Standard Model, borrowed | borrowed |
| $\mathcal L^{(2)}_{\text{matter}}$ | a copy of the Standard Model on $\Sigma_2$ (mirror sector) **[choice]** | borrowed |

The tensions do **not** depend on $\Phi$ **[choice]**. Alternative: Goldberger–Wise brane
potentials `\lambda_i (\Phi^2 - v_i^2)^2`, which stabilise $\phi$ at a fixed value. That is the
opposite of a merger and would add four parameters; rejected for v2.0 and recorded here so
that if the merger is killed (milestone 4), the stabilised alternative is the fallback.

### 2.1 The bulk potential [choice]

$$
V(\Phi) = V_0\, \exp\!\left(-\,c\,\frac{\Phi}{M_6^2}\right),
\qquad V_0 > 0,\; c > 0 .
$$

Two parameters, $V_0$ and $c$. This is the potential of the ekpyrotic/cyclic literature and
of dilatonic domain walls; it is the unique one-scale, one-slope choice with no minimum, which
is what a monotone approach to merger requires. Menu of alternatives, each also two
parameters, fixed here so that later milestones cannot silently switch:
(a) $V_0 \cosh(c\Phi/M_6^2)$; (b) $\tfrac12 m^2 \Phi^2$ with $m$ and a boundary value.
Any other form is a new free function and is banned.

### 2.2 Matter on $\Sigma_2$ [choice]

Mirror Standard Model: same Lagrangian, same couplings, its own gauge fields and fermions,
coupled to $\Sigma_1$ only via $G_{AB}$ and $\Phi$. Consequences that are forced, not chosen:
sector-2 has its own electromagnetism, hence its dark matter is *dissipative*; its equation of
state is fixed by its thermal history once $T_2/T_1$ is known. Alternatives: a single fluid
with fixed equation of state `w_2` (one parameter, less predictive), or nothing on $\Sigma_2$ (then there is no
second matter sector and the axiom is empty). Mirror-sector phenomenology is reviewed in
Berezhiani (2004) and Foot (2014).

## 3. Warped background and the tension tuning

With $\Phi$ constant and no brane matter, the bulk equations admit the RS solution
$$
ds^2 = e^{-2y/\ell}\left( \eta_{\mu\nu} dx^\mu dx^\nu + dz^2 \right) + dy^2,
\qquad
\ell^{-2} = -\frac{\Lambda_6}{10\, M_6^4}
$$
provided the tensions satisfy the RS tuning
$$
\sigma_1 = -\sigma_2 = \frac{8\, M_6^4}{\ell} .
$$
These are the $D=6$ cases of the general codimension-1 RS relations
$\Lambda_D = -\tfrac12 (D-1)(D-2)\,M_D^{D-2}/\ell^2$ and $\sigma = 2(D-2)\,M_D^{D-2}/\ell$, which
reduce to the familiar $\Lambda_5 = -6M_5^3/\ell^2$, $\sigma = 6M_5^3/\ell$ at $D=5$.
All five brane directions, including the circle, are warped: the metric with $dz^2$ unwarped
that an earlier draft of this file wrote is *not* a vacuum solution (`02_effective_4d.md` §0;
`tests/check_background.py`). Both branes wrap the circle, whose proper radius shrinks toward
$\Sigma_2$.

This tuning is the cosmological-constant problem in braneworld form. It is stated, not solved:
v2 assumes it exactly for $\sigma_1$ and treats the *detuning* of $\sigma_2$,
$$
\delta\sigma_2 \equiv \sigma_2 + \sigma_1 ,
$$
as the physical parameter. $\delta\sigma_2 = 0$ is the static RS vacuum; $\delta\sigma_2 \ne 0$
sources an effective potential for $\phi$ (milestone 3) and is the first candidate for
$\Omega_{DM}/\Omega_b$ (`01_action_skeleton_superseded.md` §4.4). Recovering a static, flat $\Sigma_1$ with $\Lambda_4 = 0$
in the $\delta\sigma_2 \to 0,\; V_0 \to 0$ limit is the milestone-3 consistency test.

Once $\ell$ is fixed, $\Lambda_6$ and $\sigma_1$ are not independent numbers; they are
functions of $(M_6, \ell)$.

## 4. What the action already fixes (to be derived in milestone 3)

These are standard two-brane results, quoted so the ledger can be closed now. Milestone 3
re-derives each with the factors of §3.

**Newton's constant on $\Sigma_1$** (derived in `02_effective_4d.md` §2; the two-brane RS
result with the $D=6$ measure):
$$
M_{\text{Pl}}^2 = \frac{M_5^3\,\ell}{3}\,\bigl(1 - e^{-3\phi/\ell}\bigr).
$$
For $\phi \gg \ell$ this is $\phi$-independent up to $e^{-3\phi/\ell}$, so
$$
\frac{\dot G}{G} = -\frac{3\,\dot\phi}{\ell}\,\frac{e^{-3\phi/\ell}}{1-e^{-3\phi/\ell}}
\;\approx\; -\frac{3\dot\phi}{\ell}\, e^{-3\phi/\ell}.
$$
Lunar laser ranging, $|\dot G/G| \lesssim 1.5\times10^{-13}\,\mathrm{yr}^{-1}$
(Hofmann & Müller 2018; treat as approximate), is satisfied for any $\dot\phi \lesssim H_0\,\ell$
once $\phi/\ell \gtrsim 3$. Fork 1 makes the LLR test easy to pass; the price is that the
observable merger dynamics live entirely in the dark sector.

**Warp factor of $\Sigma_2$ as seen from $\Sigma_1$:** $\Omega \equiv e^{-\phi/\ell}$.
Energy densities on $\Sigma_2$ appear in the 4D Einstein equation on $\Sigma_1$ suppressed by
$\Omega^4$ **[verify]**, and mass scales on $\Sigma_2$ are redshifted by $\Omega$. The merger
$\phi \to 0$ therefore *un-suppresses* sector-2 gravity over cosmic time. This is the
mechanism by which "the collision continues" becomes an observable: the effective
gravitating mass of the mirror sector grows as $\Omega(t)^4$.

**Radion effective action** (Goldberger & Wise 1999; Charmousis, Gregory & Rubakov 2000),
in the 4D Jordan frame with $g_{\mu\nu}$ the metric on $\Sigma_1$:
$$
S_{\text{eff}} \supset \int d^4x \sqrt{-g}\;
\frac{M_5^3\,\ell}{3} \left[ \frac{1-\Omega^3}{2}\,R_4 \;-\; 3\,(\partial\Omega)^2 \right]
\;-\; \int d^4x \sqrt{-g}\; V_{\text{eff}}(\phi)
\quad \textbf{[verify factor 3]}
$$
with
$$
V_{\text{eff}}(\phi) = \Omega^4\,\delta\sigma_2 \;+\; \int_0^{\phi} dy\; e^{-5y/\ell}\, V(\Phi(y))
\quad \textbf{[verify; requires the } \Phi(y) \textbf{ profile]}.
$$
$V_{\text{eff}}$ is not a free function: it is fixed by $(\delta\sigma_2, V_0, c, \ell)$ once the
bulk scalar profile is solved. This is the object that replaces v1's `\tau(t) + V_{gap}(t)`.

## 5. Parameter budget (closes the ledger)

| # | parameter | replaces in skeleton | fixed by |
|---|---|---|---|
| 1 | $M_5$ | $M_6$ (absorbs $\ell_z$) | $G_N$ together with #2, #3 |
| 2 | $\ell$ | $\sigma_1$ (RS-tuned, so not independent) | $G_N$; sets $\Lambda_6, \sigma_1$ |
| 3 | $\phi_0$ | — | present separation; $G_N$ fixes one combination of #1–#3 |
| 4 | $\sigma_2$ (via $\delta\sigma_2$) | — | $\Omega_{DM}/\Omega_b$ target |
| 5 | $V_0$ | — | dark-energy density today |
| 6 | $c$ | — | $w_0, w_a$ and $\dot\phi$ |
| 7 | $T_2/T_1$ | — | target: derived from impact kinematics (milestone 5) |

**7 numbers, 0 free functions.** One relation ($M_{\text{Pl}}$) among #1–#3 leaves 6 free.
Discrete choices, not counted: Fork 1; compact $z$; exponential $V$; mirror SM on $\Sigma_2$;
$\Phi$-independent tensions.

## 6. Kill criteria that this action alone commits to

1. If milestone 3 cannot recover $G_{\mu\nu} = 8\pi G_N T_{\mu\nu}$ with $\Lambda_4 = 0$ in the
   limit $\delta\sigma_2 \to 0$, $V_0 \to 0$, $\dot\phi \to 0$, the action is wrong.
   *Status: passed* (`02_effective_4d.md` §6), with the metric correction of its §0.
2. If the late-time attractor of $V_{\text{eff}}$ gives $w_0, w_a$ outside the DESI + Planck
   allowed region for every $c$ (milestone 4), the exponential potential is dead; move to
   menu item (a) or (b) of §2.1 **once**, and record the failure in `RETRACTED.md`.
3. A single canonical radion cannot cross $w = -1$. If phantom crossing is confirmed at
   $>5\sigma$, the minimal radion is out and only $E_{\mu\nu}$ (milestone 3) can save the
   branch.
4. If impact kinematics give $T_2/T_1 \gtrsim 0.5$ (milestone 5), the mirror sector violates
   BBN/$N_{\text{eff}}$ and §2.2 is dead.
   *Status: fired, in a stronger form* (`04_impact.md` §2–3). The kinematics give no number
   (the action is $\mathbb Z_2$-symmetric at the collision; its null value $T_2/T_1 = 1$ gives
   $\Delta N_{\text{eff}} \approx 6$), and for every $T_2/T_1 < 0.45$ the warped mirror
   baryons fall short of $\Omega_{DM}/\Omega_b = 5.3$ by a factor $\gtrsim 1600$ in baryon
   asymmetry. §2.2 as the dark matter is dead; exits are tabulated there.
5. Detection of primordial tensor modes with $r > 0.01$ kills the collision origin
   (inherited from ekpyrotic models; Khoury, Ovrut, Steinhardt & Turok 2001).
   *Status: re-labelled* (`04_impact.md` §6). This action has no ekpyrotic potential and
   produces no primordial spectrum; it neither predicts $r$ nor is killed by it. `A_s`, $n_s$
   are borrowed.

## 7. What this action does not contain

No `\omega_0`, no harmonic index, no `\Xi_{\mu\nu}`, no epoch dependence except through
$\phi(t)$, no derivation of $\mathcal L^{(1)}$. The electron and the neutrino — the original
inspirations for v1 — are Standard-Model inputs here. If the geometry has anything to say about
them it will appear as a $z$-KK spectrum at scale $1/\ell_z$, and it will be found, not assumed.
