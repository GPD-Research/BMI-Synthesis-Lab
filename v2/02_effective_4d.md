# 02 — The Effective 4D Theory

Milestone 3. Input: the action of `01_action.md`, nothing else. Output: the gravitational
field equation on $\Sigma_1$, Newton's constant as a function of the separation, the
corrections to General Relativity that the action forces, and the limit in which GR and ΛCDM
are recovered. Kill criterion 1 of `01_action.md` §6 is tested here.

Every numerical factor in §1 is checked by `tests/check_background.py` (sympy). Results still
quoted from the literature are marked **[verify]** with the reference and the reason they are
not yet re-derived.

## 0. Corrections to `01_action.md` found during this milestone

1. **The metric in §3 was wrong.** `01_action.md` wrote the background as
   $e^{-2y/\ell}\eta_{\mu\nu}dx^\mu dx^\nu + dy^2 + dz^2$ with the circle unwarped. That metric
   is *not* a solution of the 6D vacuum equations: the $(x,x)$ components require
   $\Lambda_6 = -6M_6^4/\ell^2$ and the $(z,z)$ component requires $-10M_6^4/\ell^2$
   (`check_background.py`, last block). The consistent background warps all five brane
   directions,
   $$
   ds^2 = e^{-2y/\ell}\left(\eta_{\mu\nu}dx^\mu dx^\nu + dz^2\right) + dy^2 ,
   $$
   i.e. a slice of $\mathrm{AdS}_6$ with the circle shrinking toward $\Sigma_2$. The factors
   $\Lambda_6 = -10M_6^4/\ell^2$ and $\sigma_1 = 8M_6^4/\ell$ quoted in §3 were already those
   of this metric and are confirmed. `01_action.md` §3 has been corrected.
2. **The Planck-mass formula in §4 had the 5D exponent.** With all five directions warped the
   integrand of the 4D curvature term is $e^{-3y/\ell}$, not $e^{-2y/\ell}$ (§2 below). The
   corrected relation changes the $\dot G/G$ estimate by a factor $\tfrac32$ and the exponent
   $2\to3$; the conclusion (LLR easily satisfied) is unchanged. §4 has been corrected.
3. **$\ell_z$ is the circle radius at $\Sigma_1$.** The proper radius at $y$ is
   $\ell_z e^{-y/\ell}$, so $M_5^3 \equiv \pi\ell_z M_6^4$ (orbifold volume, `02b_localization.md` §4.1) is the UV-brane value. This matters
   for the mirror sector (§5).

None of these changes the parameter count. They are recorded here rather than silently
edited because the point of the ledger is that mistakes are visible.

## 1. Background (verified)

Bulk equations $G_{AB} = -\Lambda_6\, G_{AB}/M_6^4$ with constant $\Phi$ and $V_0 \to 0$:

$$
ds^2 = e^{-2y/\ell}\left(\eta_{\mu\nu}dx^\mu dx^\nu + dz^2\right) + dy^2 ,
\qquad
\ell^{-2} = -\frac{\Lambda_6}{10\,M_6^4} .
$$

Boundary condition at a brane (one-sided, interval geometry, GHY normalisation of
`01_action.md` §2):
$$
2M_6^4\left(K_{ab} - \gamma_{ab}K\right) = -S_{ab},
\qquad S_{ab} = -\sigma_i\gamma_{ab} + T^{(i)}_{ab},
$$
with $K_{ab}$ the extrinsic curvature of the brane with outward normal, $a,b$ running over the
five brane directions. For the vacuum background $K_{ab} = -\gamma_{ab}/\ell$ at $y=0$, which
gives
$$
\sigma_1 = \frac{8M_6^4}{\ell}, \qquad \sigma_2 = -\sigma_1 .
$$
Both checked for $D=5$ (recovering $-6M^3/\ell^2$, $6M^3/\ell$) and $D=6$ by
`check_background.py`.

**Consequence for kill criterion 1.** With these tensions and no brane matter the induced
metric on $\Sigma_1$ is exactly $\eta_{\mu\nu}$, i.e. the effective 4D cosmological constant
vanishes identically, $\Lambda_4 = 0$. The braneworld cosmological-constant problem is the
statement that this needs the tuning of §1; the tuning is assumed (`01_action.md` §3), and the
result is that the assumption does what it must.

## 2. Newton's constant on $\Sigma_1$

Insert $g_{\mu\nu}(x)$ for $\eta_{\mu\nu}$ in the background and integrate the bulk
Einstein–Hilbert term over $0 \le y \le \phi$ and the circle. $\sqrt{-G} = e^{-5y/\ell}\sqrt{-g}$
and $R_6 \supset e^{2y/\ell}R_4$, so
$$
\frac{M_6^4}{2}\int d^6X\sqrt{-G}\,R_6 \;\supset\;
\frac{M_6^4}{2}\,(\pi\ell_z)\int_0^{\phi}dy\,e^{-3y/\ell}\int d^4x\sqrt{-g}\,R_4
= \frac{M_{\text{Pl}}^2(\phi)}{2}\int d^4x\sqrt{-g}\,R_4 ,
$$
$$
\boxed{\;M_{\text{Pl}}^2(\phi) = \frac{M_5^3\,\ell}{3}\left(1 - e^{-3\phi/\ell}\right),
\qquad 8\pi G_N = M_{\text{Pl}}^{-2}\;}
$$
(`check_background.py`, "Planck integral"). For $\phi \gg \ell$: $M_{\text{Pl}}^2 \to M_5^3\ell/3$,
independent of where $\Sigma_2$ is. This is the content of Fork 1.

**Time variation.**
$$
\frac{\dot G}{G} = -\frac{3\dot\phi}{\ell}\,\frac{e^{-3\phi/\ell}}{1 - e^{-3\phi/\ell}} .
$$
With $\dot\phi \sim H_0\ell$ (separation changing by one warp length per Hubble time — the
fastest "slow merger" worth the name) and $\phi_0/\ell = 5$: $|\dot G/G| \approx 3\times
3\times10^{-7}\,H_0 \approx 7\times10^{-17}\,\mathrm{yr}^{-1}$, four orders of magnitude inside
the lunar-laser-ranging bound $1.5\times10^{-13}\,\mathrm{yr}^{-1}$ (Hofmann & Müller 2018).
$\phi_0/\ell \gtrsim 3$ suffices for the bound alone; §4 imposes the stronger condition.

## 3. The field equation on $\Sigma_1$

Gauss–Codazzi projection of the bulk equations onto a codimension-one brane with the junction
condition of §1 (Shiromizu, Maeda & Sasaki 2000, generalised to $D=6$; the structure is
dimension-independent and only the coefficients change). On the five-dimensional worldvolume
of $\Sigma_1$:
$$
{}^{(5)}G_{ab} = -\Lambda_{\text{brane}}\,\gamma_{ab} + 8\pi G_5\,T_{ab} + \frac{1}{M_6^8}\,\pi_{ab} - E_{ab},
$$
where

- $\Lambda_{\text{brane}} = 0$ by §1 (it is the combination of $\Lambda_6$ and $\sigma_1^2$ that
  the RS tuning kills);
- $8\pi G_5 \propto \sigma_1/M_6^8$ is the brane Newton constant, which after reduction on the
  circle becomes $G_N$ of §2 **[verify: coefficient]**;
- $\pi_{ab}$ is quadratic in $T_{ab}$: $\pi_{ab} = -\tfrac14 T_{ac}T^c{}_b + \tfrac{1}{12}TT_{ab}
  + \tfrac18\gamma_{ab}(T_{cd}T^{cd} - \tfrac13 T^2)$ in $D=5$ **[verify: $D=6$ coefficients]**;
- $E_{ab} = C_{AaBb}\,n^A n^B$ is the projection of the bulk Weyl tensor: the influence of the
  bulk and of $\Sigma_2$ on our gravity, not determined by brane data alone.

Reducing on the circle at energies below $1/\ell_z$ (zero mode only) gives the 4D equation
$$
\boxed{\;G_{\mu\nu} = 8\pi G_N(\phi)\,T_{\mu\nu} + \frac{8\pi G_N}{\sigma_1^{(5)}}\,\hat\pi_{\mu\nu} - E_{\mu\nu} + \Theta_{\mu\nu}[\phi]\;}
$$
with $\sigma_1^{(5)} = \pi\ell_z\sigma_1 = 8M_5^3/\ell$ the tension per unit 4-volume,
$\hat\pi_{\mu\nu}$ the 4D quadratic tensor, and $\Theta_{\mu\nu}[\phi]$ the radion stress
(derivative terms in $\phi$ plus $V_{\text{eff}}(\phi)\,g_{\mu\nu}$, §4). This is the equation
v1's Chapter 7 was reaching for: $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ is its weak-field
expansion, and v1's undefined `\Xi_{\mu\nu}` is the sum of the three correction terms, now
each with a definition and a size.

**Size of each correction.**

*Quadratic term.* Relative to the GR term it is $\rho/\sigma_1^{(5)}$. Using §2,
$\sigma_1^{(5)} = 24M_{\text{Pl}}^2/\ell^2$ up to the $e^{-3\phi/\ell}$ correction. Table-top
tests of the inverse-square law bound the warp length $\ell \lesssim 10\,\mu\mathrm m$ (Eöt-Wash;
Adelberger et al. 2007, treat as approximate). Then
$$
\sigma_1^{(5)} \gtrsim 24\,(2.4\times10^{18}\,\mathrm{GeV})^2\,(5\times10^{10}\,\mathrm{GeV}^{-1})^{-2}
\approx 5\times10^{16}\,\mathrm{GeV}^4 \approx (1.5\times10^{4}\,\mathrm{GeV})^4 .
$$
The quadratic correction is $(T/15\,\mathrm{TeV})^4$ during radiation domination: below
$10^{-16}$ at BBN and irrelevant for the CMB. It is a genuine prediction of the action (a
$\rho^2$ term in the Friedmann equation at $T \gtrsim 10\,\mathrm{TeV}$), and it is
generic to every codimension-one braneworld — **not** BMI-specific.

*Weyl term.* In a homogeneous background $E_{\mu\nu}$ is a radiation-like fluid,
$\rho_E = \mathcal C/a^4$ ("dark radiation"), with $\mathcal C$ an integration constant of the
bulk solution. It is not a parameter of the action; it is fixed by the bulk initial state at
the impact, i.e. it must be *computed* in milestone 5, and it is bounded now:
$\Delta N_{\text{eff}} = 4.4\,\rho_E/\rho_\gamma$ (evaluated today) $\lesssim 0.3$ (Planck 2018).
If milestone 5 cannot compute $\mathcal C$, it becomes an 8th ledger entry and the balance
worsens by one. Recorded in `ledger.md` as a pending integration constant.

*Radion term.* §4.

## 4. The radion: scalar–tensor structure and the GR limit

Let $\phi$ vary. The 4D theory is a scalar–tensor theory in which the coefficient of $R_4$ is
$M_{\text{Pl}}^2(\phi)$ of §2. Writing $\Omega \equiv e^{-\phi/\ell}$, $\Psi \equiv 1 - \Omega^3$,
the Jordan-frame effective action is
$$
S_{\text{eff}} = \int d^4x\sqrt{-g}\left[\frac{M_5^3\ell}{6}\,\Psi\,R_4
 - \frac{M_5^3\ell}{6}\,\frac{\omega(\Psi)}{\Psi}(\partial\Psi)^2 - V_{\text{eff}}(\phi)\right]
 + S_{\text{SM}}[g,\psi_1] + S_{\text{mirror}}[\Omega^2 g,\psi_2] .
$$
The mirror sector couples to the *induced metric on $\Sigma_2$*, which is $\Omega^2 g_{\mu\nu}$ —
this is not a choice, it is where $\Sigma_2$ sits in the warped bulk.

**Brans–Dicke parameter.** For the 5D two-brane system observers on the positive-tension brane
see $\omega = \tfrac32\,(e^{2\phi/\ell} - 1)$ (Garriga & Tanaka 2000; Charmousis, Gregory &
Rubakov 2000). The $D=6$ value is derived in `03_background.md` §1 (moduli approximation,
`tests/check_radion.py`): $\omega = \tfrac43(e^{3\phi/\ell}-1)$ — the guess $\tfrac32$
originally written here was wrong. Either way $\omega \to \infty$ as $\phi/\ell \to \infty$,
which is GR.

**GR test in the solar system.** Cassini requires $\omega > 4\times10^4$ (Bertotti, Iess &
Tortora 2003). With the 6D formula:
$$
\boxed{\;\phi_0/\ell \;\gtrsim\; 3.4,\qquad \Omega_0 \lesssim 0.032\;}
$$
(the earlier working value $5$ used the 5D prefactor and exponent). This is the first *number*
v2 produces from data: the present brane separation is at least about three and a half warp
lengths. It is a constraint, not a prediction — it uses Cassini — but it is un-fitted in the
sense that no ledger entry was adjusted to reach it.

If $V_{\text{eff}}$ gives the radion a mass $m_\phi \gg 1/\mathrm{AU}$, the Cassini bound is
evaded regardless of $\omega$ (Yukawa-suppressed). The exponential potential has no minimum, so
this cannot be assumed; milestone 4 must check whether $m_{\text{eff}}^2 = \partial_\phi^2 V_{\text{eff}}$ on
the cosmological solution is large or small compared to $H_0^2$. If small, §4 applies and
$\phi_0/\ell \gtrsim 3.4$ is mandatory. (`03_background.md` §1: the exponential potential
gives the radion no mass; the bound applies.)

**Effective potential.** The two contributions:
$$
V_{\text{eff}}(\phi) = \Omega^4\,\delta\sigma_2^{(5)} \;+\; \pi\ell_z\int_0^\phi dy\;e^{-5y/\ell}\,V(\Phi(y))
\quad\textbf{[verify: requires } \Phi(y)\textbf{]}
$$
with $\delta\sigma_2^{(5)} = \pi\ell_z\,\delta\sigma_2$. The $\Omega^4$ scaling of the detuning
term is the standard warped-down IR-brane tension (the same redshift that makes
the RS hierarchy). The measure of the bulk-potential term is $e^{-5y/\ell}$ (six-dimensional
$\sqrt{-G}$), correcting the $e^{-4y/\ell}$ written in `01_action.md` §4, which was the 5D value.
The profile $\Phi(y)$ is not solved here; with $V_0 \ll |\Lambda_6|$ the scalar is a probe on
the AdS background and $\Phi(y)$ follows from $\Phi'' - (5/\ell)\Phi' = V'(\Phi)$ with Neumann
conditions at the branes (tensions are $\Phi$-independent). Solving this is milestone 4's
first task. Until then $V_{\text{eff}}$ is a functional of the ledger, not a free function.

## 5. Forced consequence: the mirror sector is a *warped* copy

This was not in the skeleton and follows directly from §4. Because $\Sigma_2$ sits at
$y = \phi$, every dimensionful quantity in $\mathcal L^{(2)}$ is redshifted by
$\Omega = e^{-\phi/\ell}$ relative to $\Sigma_1$ (Randall & Sundrum 1999a — the mechanism they
used for the weak/Planck hierarchy). "Mirror Standard Model with the same couplings" therefore
means: same dimensionless couplings, all masses multiplied by $\Omega(\phi)$:
$$
m_e^{(2)} = \Omega\,m_e,\qquad m_p^{(2)} = \Omega\,m_p,\qquad \Lambda_{\text{QCD}}^{(2)} = \Omega\,\Lambda_{\text{QCD}} .
$$
With $\phi_0/\ell \gtrsim 3.4$ (§4), $\Omega \lesssim 0.032$: mirror protons lighter than
about $30\,\mathrm{MeV}$, mirror electrons below $16\,\mathrm{keV}$, mirror atoms with
Bohr radii $\gtrsim 30\times$ ours. Three things follow, none of them chosen:

1. **Dark matter is light and dissipative.** $\Omega_{DM}/\Omega_b = (n_2/n_1)(\Omega\,m_p/m_p)$
   requires $n_2/n_1 \approx 5.3/\Omega \gtrsim 165$ — the mirror sector needs far *more*
   baryons than ours, not a colder copy. This inverts the standard mirror-matter picture and
   is either a striking prediction for milestone 5 (impact asymmetry must produce it) or the
   death of §2.2. It is the first place where BMI differs from generic mirror-matter models.
2. **DM particle masses change with cosmic time.** As the merger proceeds ($\dot\phi < 0$)
   $\Omega$ grows and every mirror mass grows. The CMB acoustic peaks constrain the DM
   mass–energy between $z \sim 1100$ and today to be that of a pressureless fluid diluting as
   $a^{-3}$; a mass growing as $\Omega(t)$ violates this unless
   $|\Delta\Omega/\Omega| \lesssim$ a few percent since recombination, i.e.
   $|\Delta\phi| \lesssim 0.03\,\ell$ over the last Hubble time. Combined with §2 this
   strongly limits how fast the merger can be *now* — a forced, quantitative statement that
   milestone 4 confronts: `03_background.md` §3.1 — the bound forces the radion to be a
   spectator. (Variable-mass DM has a literature: Anderson & Carroll 1997;
   this is that mechanism with $\Omega(\phi)$ as the coupling.)
3. **Mirror KK scale.** The circle radius at $\Sigma_2$ is $\Omega\ell_z$, so mirror-sector
   $z$-modes sit at $1/(\Omega\ell_z) \gg 1/\ell_z$; no light mirror KK states.

Point 2 is dangerous for the "collision continues" axiom and is flagged as a **kill risk**: if
milestone 4 finds that the exponential potential drives $\dot\phi$ fast enough to matter for
$w(z)$, it is likely already excluded by the DM-mass constraint. That tension — merger fast
enough to see, slow enough for CDM — is the theory's first real test.

## 6. Recovery of GR and ΛCDM

Take $\dot\phi \to 0$ at $\phi = \phi_0$ with $\phi_0/\ell \gtrsim 3.4$, $V_0 \to 0$,
$\delta\sigma_2 \to 0$, and $\mathcal C \to 0$. Then:

- $\Theta_{\mu\nu} \to 0$, $E_{\mu\nu} \to 0$, $\hat\pi_{\mu\nu}/\sigma_1^{(5)} \to 0$ at
  $T \ll 10\,\mathrm{TeV}$;
- $G_N(\phi_0) = 3/(8\pi M_5^3\ell)$ up to $e^{-15}$;
- the field equation is $G_{\mu\nu} = 8\pi G_N T_{\mu\nu}$ with $\Lambda_4 = 0$ (§1).

**Kill criterion 1 is passed.** GR is recovered with the corrections as listed, and the
Newtonian limit is then the usual weak-field limit of GR, one level further down. The
hierarchy the user asked for — bulk action → brane equation with corrections → GR → Newton —
is realised, with each arrow a controlled limit.

ΛCDM is recovered by *not* taking $V_0, \delta\sigma_2 \to 0$ but freezing $\phi$: then
$V_{\text{eff}}(\phi_0)$ is a constant, $\Lambda_4 = 8\pi G_N V_{\text{eff}}(\phi_0)$, and with
mirror matter on $\Sigma_2$ as the pressureless component (subject to §5) the background is
exactly ΛCDM. The value $\Lambda_4 = (2.3\,\mathrm{meV})^4$ is *fitted* through $V_0$ — that is
ledger entry 5 doing its declared job, and it is the standard cosmological-constant tuning,
not solved here.

Where v2 can differ from ΛCDM, and only there: $w(z) \ne -1$ from $\dot\phi \ne 0$;
$\Delta N_{\text{eff}}$ from $\mathcal C$; dissipative, light, time-varying-mass dark matter
from §5; the $\rho^2$ term above 10 TeV; $\dot G/G$ at the $10^{-16}\,\mathrm{yr}^{-1}$
level. Each is computable from the seven ledger entries. Milestone 4 computes the first two.

## 7. What is generic and what is BMI

| result | generic braneworld | BMI-specific |
|---|---|---|
| RS tuning, $\Lambda_4 = 0$ | yes | — |
| $M_{\text{Pl}}^2(\phi)$, Fork-1 $G$-stability | yes (RS-I) | — |
| $\rho^2$ Friedmann term at $T \gtrsim 10$ TeV | yes | — |
| dark radiation $\mathcal C/a^4$ | yes | value of $\mathcal C$ from impact (m5) |
| scalar–tensor radion, $\phi_0/\ell \gtrsim 3.4$ | yes (GT 2000) | 6D prefactor $\tfrac43$ |
| warped mirror sector: $m^{(2)} = \Omega\, m$ | RS mechanism | applied to a *full* mirror SM as DM: $n_2/n_1 \gtrsim 165$ and time-varying DM mass are BMI's |
| $w(z)$ from exponential $V$ | ekpyrotic/quintessence | with $V_{\text{eff}}$ fixed by the ledger, not fitted |

Nothing in the first five rows is evidence for BMI. The sixth row is the first place the axiom
says something a generic model does not, and it is falsifiable.

## 8. Open items carried to milestone 4

1. ~~Derive the 6D Brans–Dicke $\omega(\phi)$~~ done, `03_background.md` §1.
2. Solve $\Phi(y)$ on the AdS background for the exponential $V$; obtain $V_{\text{eff}}(\phi)$.
3. Cosmological solution: $w(z)$, $\dot\phi(t)$, $m_{\text{eff}}$ of the radion.
4. Confront §5.2: DM-mass variation since recombination vs $\dot\phi$ needed for observable $w(z)$.
5. $D=6$ coefficients of $\pi_{ab}$ and $G_5$ (cosmetic; the sizes above do not depend on them).
