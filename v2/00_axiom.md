# BMI v2 — Axiom

Two 4-dimensional branes, $\Sigma_1$ (ours) and $\Sigma_2$, are embedded in a
6-dimensional bulk. They collided at $t = 0$ and are now slowly merging. Matter on
$\Sigma_2$ couples to matter on $\Sigma_1$ only through bulk gravity and at most one bulk
scalar field $\Phi$.

That is the whole axiom. Everything in `v2/` must be derived from it and from the action
in `01_action_skeleton.md`, or it does not belong in `v2/`.

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

## What is not in v2

Harmonic mass formulas, winding-number particle assignments, the strain tensor `\Xi_{\mu\nu}`,
Bridge Stress `\tau(t)`, `V_{gap}(t)`, impedance tensors, seams, `D_H`, the 15 Hz sector,
the screening gate. See
`RETRACTED.md`. Any of these may return only by re-derivation from the action.
