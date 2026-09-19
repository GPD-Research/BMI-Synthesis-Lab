# BMI v2 — Axiom

Two 4-dimensional branes, $\Sigma_1$ (ours) and $\Sigma_2$, are embedded in a
6-dimensional bulk. They collided at $t = 0$ and are now slowly merging. Matter on
$\Sigma_2$ couples to matter on $\Sigma_1$ only through bulk gravity and at most one bulk
scalar field $\Phi$.

That is the whole axiom. Everything in `v2/` must be derived from it and from the action
in `01_action.md`, or it does not belong in `v2/`.

## What the axiom commits to

- General relativity, quantum field theory and the six-parameter ΛCDM background are the
  limit in which the brane separation $\phi$ is frozen. v2 must reproduce them there
  (`tests/` milestone 3). It does not contradict them; it extends them only where they are
  untested: $w(z)$ at the few-percent level, $N_{\text{eff}}$, $r$, dark-matter microphysics,
  large-angle CMB isotropy.
- Our brane is the UV brane of a warped bulk (Fork 1), so $G_N$ on $\Sigma_1$ does not
  track $\phi(t)$ and lunar-laser-ranging bounds on $\dot G/G$ are satisfied by construction.
  Merger dynamics appear only in the dark sector.
- The Standard Model Lagrangian on $\Sigma_1$ is borrowed, not derived.

## What the axiom must deliver (kill criteria)

| quantity | must match | source of bound |
|---|---|---|
| $w_0, w_a$ | DESI DR2 + CMB + SNe | one parameter $c$ in $V(\Phi)$ |
| $\Delta N_{\text{eff}}$ from $E_{\mu\nu}$ | $\lesssim 0.3$ (Planck), $\pm 0.03$ (CMB-S4) | bulk Weyl projection |
| $T_2/T_1$ | $\lesssim 0.3$–$0.5$ (BBN, $N_{\text{eff}}$) | impact kinematics |
| $\Omega_{DM}/\Omega_b$ | $5.3$ | $\sigma_2/\sigma_1$, $T_2/T_1$ |
| $\sigma/m$ of sector-2 matter | $\lesssim 1\ \mathrm{cm}^2\,\mathrm{g}^{-1}$ (Bullet Cluster) | sector-2 dissipation with $T_2 < T_1$ |
| $n_s$, $r$ | $0.965$, $< 0.03$ | impact (ekpyrotic-type) spectrum |

A single un-fitted hit moves the parameter ledger positive. A single forced miss kills the
branch; record it in `RETRACTED.md` and stop.

## Deferred hypothesis: field content from geometry (not yet in the action)

The genesis idea behind the SM sector — kept here as a hypothesis, not a v2 commitment —
is that particle species differ by *where they live*: some fields are confined to the
3+1 worldvolume of $\Sigma_1$, some extend into the shared $(y,z)$ pair (a KK tower along
$z$, a profile along $y$), and some are sourced on $\Sigma_2$ and reach us only through the
shared pair ("shadowed"). In braneworld language these are brane-localized fields, bulk
fields, and bulk fields with overlap on both branes. The mechanism is standard (bulk
right-handed neutrinos: Arkani-Hamed–Dimopoulos–Dvali–March-Russell 1998, Dienes–Dudas–Gherghetta 1998;
split fermions: Arkani-Hamed–Schmaltz 2000).

**Admission rule.** This enters `01_action.md` only if the assignment of each field to
{brane, bulk, shadowed} is *forced* by the equations — an anomaly-cancellation, stability,
or zero-mode-existence argument on the AdS$_6$ background of `02_effective_4d.md` §1 — and
not chosen species by species to fit the spectrum. A per-field choice is a free function
(one discrete slot per species) and is the retracted R4 in new clothes.

**What is already known to constrain it.**
- Worked out in `02b_localization.md`: SM gauge fields cannot be bulk fields (a bulk gauge
  zero mode couples universally, so mirror matter would be charged), charged SM fermions
  follow them, and 4D chirality forces $z \in S^1/\mathbb Z_2$. The bleed is limited to
  gravity, $\Phi$, the radion, and gauge singlets (right-handed neutrinos).
- A bulk right-handed neutrino on this background gives: Dirac neutrinos (no neutrinoless double-beta decay), a mass
  hierarchy fixed by the $y$-profile overlap with $\Sigma_1$ (a *ratio* prediction, e.g.
  $\Delta m^2_{31}/\Delta m^2_{21}$, with no per-species parameter), and a tower of sterile
  states at $n/\ell_z$. These are the tests; a fitted absolute scale is not.
- The one number the geometry already fixes is the mass scale on $\Sigma_2$,
  $\Omega = e^{-\phi/\ell}$ (`02_effective_4d.md` §5). Any shadowed field inherits it.

Localization equations: milestone 3b, `02b_localization.md`. Verdict there: spin and the
SM's own consistency fix everything except one bulk-mass dial per bulk fermion; the SM on
$\Sigma_1$ stays borrowed.

## What is not in v2

Harmonic mass formulas, winding-number particle assignments, the strain tensor `\Xi_{\mu\nu}`,
Bridge Stress `\tau(t)`, `V_{gap}(t)`, impedance tensors, seams, `D_H`, the 15 Hz sector,
the screening gate. See
`RETRACTED.md`. Any of these may return only by re-derivation from the action.
