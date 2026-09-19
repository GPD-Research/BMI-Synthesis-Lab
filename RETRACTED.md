# Retracted and Suspended Results

This file is the negative-results record for BMI v1. Nothing here is deleted from the
manuscript; the v1 chapters under `manuscript/md/` are frozen as written so the history is
auditable. Each entry states what was claimed, where, why it no longer carries weight, and
what (if anything) would be needed to revive it.

Status codes:

- **RETRACTED** — shown to be wrong, circular, or an analysis artifact.
- **SUSPENDED** — not shown wrong, but currently has no derivation or no free-parameter-free
  content; excluded from v2 until re-derived from the v2 action.

---

## R1. The 15 Hz gravitational-wave ringdown split (RETRACTED)

**Claimed in:** README.md, Chapter 12, Appendix J (5.557σ Fisher-combined significance,
GW190521 L1 + GW231028 H1).

**Why retracted:** Follow-up testing determined that the split was an artifact of the
analysed spectrum's limits and the template-subtraction step, not a feature of the strain.
Evidence already recorded in Appendix J.9 points the same way:

- the split is not detected in the un-modelled excess-power search on raw whitened strain
  (split ratio 1–4 %, below the 10 % threshold; J.9.3);
- an alternative whitening/alignment (PyCBC) reduces the split power from 39–81 % to 8–13 %,
  i.e. the result is pipeline-dependent (J.9.3);
- the null distributions (N = 100 and N = 50 off-source trials) cannot empirically resolve
  p ~ 10⁻⁶; the 5.557σ rests on Gaussian tails of a 50–100-sample null (J.3–J.4);
- the coupling constant K = 0.13 is described in Appendix J as fixed *before* data ingestion
  and in Chapter 12 as *inferred from* f_L/f_H ≈ 1.13 in the same data — the prediction is
  circular as written.

**Consequences:** everything downstream of Δf = 15 Hz is unsupported: K = 0.13, L_node,
δ ≈ 10⁻¹⁵ m (see R2), and the "mass-regime specificity" argument from GW250114.

**To revive:** a pre-registered, template-independent, multi-detector coherence analysis
(cWB or BayesWave) on the full O3/O4 BBH catalog with Δf and K fixed in advance and a null
of ≥ 10⁴ off-source trials.

---

## R2. Node scale L_node ≈ 10⁻¹⁵ m and brane thickness δ (RETRACTED value; SUSPENDED concept)

**Claimed in:** Chapter 12, Chapter 14, Appendix J; used throughout Chapters 9, 13.

**Why:** L_node = ħ/(Δf · M_Pl) is derived from the retracted Δf, and is also not a length
dimensionally (ħ/(Hz·kg) = J·s²/kg = m², an area; Appendix J.9 itself evaluates it to
3.23 × 10⁻²⁸ "m" while the manuscript body uses 10⁻¹⁵ m). δ ≈ 10⁻¹⁵ m therefore has no
current basis. Note that δ = 10⁻¹⁵ m would place the Kaluza–Klein scale at ħc/δ ≈ 200 MeV,
which v1 never confronted with the hadron spectrum or with collider limits.

**To revive:** δ becomes a parameter of the v2 action (see `v2/01_action_skeleton.md` §3)
and must be fixed by G_N and the warped geometry, not by GW data.

---

## R3. Cosmic-web Hausdorff dimension D_H ≈ 1.738 (RETRACTED)

**Claimed in:** Chapter 14.

**Why:** the stated formula is D_H = 2 + ln(Impedance Coupling) / ln(L_node/δ). With
L_node = δ (both asserted to be 10⁻¹⁵ m) the denominator is ln 1 = 0 and the expression is
undefined. "Impedance Coupling" is never given a value. The number 1.738 cannot come from
this expression; it has no derivation.

**To revive:** a computed filament dimension from an actual T³ (or preferred-axis) structure
formation calculation, with the prediction made before comparison to DESI/Euclid.

---

## R4. Integer-harmonic mass formula M = n·ω₀·(1 + Δψ(n)) (SUSPENDED)

**Claimed in:** Front matter, Chapter 1, Chapter 2, Chapter 8 (also Λ_geom, the nucleon
split with σγ/2π, and the epoch factor f(Ξ(t))).

**Why:** Δψ(n) is a free function of the per-particle integer n. Setting
Δψ(n) = M_n/(nω₀) − 1 reproduces any spectrum exactly, so the formula has zero predictive
content until Δψ is derived. Integer-harmonic mass formulas (Nambu 1952; MacGregor; Palazzi)
have fitted hadron spectra for seventy years for exactly this reason. Additionally, Chapter 3
fixes the Berry phase γ = π while Chapter 1's nucleon split (1 ± γ/2π) would then give a 50 %
n–p mass difference; the two chapters cannot be using the same γ.

**To revive:** a KK spectrum computed from the v2 action with boundary conditions written
down, compared to PDG masses against a random-spectrum null of equal density.

---

## R5. Macro-seams as explanations of large-scale structure (SUSPENDED)

**Claimed in:** Appendix H, Appendix I (preferred axes, "Flatlander's Lens", GRB ring).

**Why:** a projected bulk seam can be placed to explain any closed or linear sky feature,
and predicts no forbidden configuration. Tested directly on the Giant GRB Ring (`tests/grb_ring/`, rerun with `python3 fit.py 1000`)
(Balázs et al. 2015): ring and spiral shape fits do not beat a Monte Carlo null of nine
random points in the same footprint (golden spiral p ≈ 0.55, free log spiral p ≈ 0.07,
circle p ≈ 0.11). The ring's published 2 × 10⁻⁶ significance concerns the redshift-shell
overdensity, not shape.

**To revive:** a seam model with a computed density-contrast profile that predicts the same
feature in all tracers (LRG/quasar/cluster) at a fixed Δz.

---

## R6. Metric-equilibrium / impedance sector (SUSPENDED)

**Claimed in:** Chapters 4, 6, 7, 8, 13 — Ξ_μν(τ + V_gap), τ(t), V_gap(t), Z_ij(Ξ),
Λ_tensor, B_compact(n), Φ_bridge, Φ_shadow, ρ_shadow, T_int, τ_global.

**Why:** none of these objects has an equation of motion or a numerical value in the
manuscript. They are free functions and tensors; see `v2/ledger_v1_audit.md` §B. In v2
their roles are taken by the brane-separation field φ(t), the bulk potential V(Φ), and the
Israel junction conditions.

---

## R7. Ricci-scalar screening gate g_eff(R) (SUSPENDED)

**Claimed in:** Chapter 9 (Mott problem).

**Why:** R = 0 in vacuum outside any source, so the gate is identically zero along the entire
path of a bubble-chamber electron; the mechanism cannot operate as written. A curvature
trigger would need the Weyl or Kretschmann scalar, or an acceleration threshold. α and
R_crit have no values.

---

## R8. "Universe is a black hole of its own size" (RETRACTED as evidence)

**Claimed in:** informal motivation for the collision picture.

**Why:** for a flat FRW universe ρ_c = 3H²/8πG implies R_s = 2GM/c² = c/H identically.
The coincidence is flatness (Ω = 1), already measured. It is not evidence for a brane
collision or for black-hole cosmology.

---

## Kept from v1 (generic, correct, re-derived in v2)

- Appendix F: Gauss–Codazzi reduction to G_μν = 8πG_N T_μν (standard braneworld result;
  v2 replaces it with the Israel junction conditions and keeps the correction terms).
- Appendix E: Kaluza–Klein tower from a compact fibre (boundary conditions to be written).
- Chapter 3: spinor double cover under 2π rotation (textbook; not a prediction).
- Chapter 10: U(1) covariant derivative (textbook; SU(2)×SU(3) not derived).
- Appendix B: age and horizon (ΛCDM verbatim; kept as the background v2 must reproduce).

---

## Kept as the v2 axiom

The single hypothesis that survives the audit and is not generic to braneworlds:

> Two 4-branes collided at t = 0 and are slowly merging. Matter on the second brane couples
> to ours only through bulk gravity (and at most one bulk scalar). The temperature
> asymmetry of the two sectors, the dark-energy equation of state, and the dark-matter
> fraction are consequences of the impact kinematics and the merger dynamics.

See `v2/00_axiom.md`.
