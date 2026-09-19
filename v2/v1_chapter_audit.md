# Where v1 went off the rails — chapter-by-chapter audit

Method: read `manuscript/md/` in order and stop at the first statement that does not
follow from what precedes it *and* on which later chapters depend. Then trace every
"validated" claim in Chapters 1–4 to the code under `src/` that is supposed to validate it.

## Verdict

**The hard stop is Chapter 1, §1.2, the first equation of the manuscript:**

    M(n) = n · ω₀ · Λ_geom

Nothing before it is wrong (it is the two-brane premise, stated in words). Nothing after it
in Chapters 1–4 is derived from anything but it. And it contains no content:

- `ω₀` is never assigned a value anywhere in the repository (manuscript or `src/`).
- `n` is never assigned to any particle. Chapter 2 §2.3 writes `n = n_base, n_μ, n_π, n_p, n_n`
  and stops. There is no table of integers, so the "linear resonance spectrum" was never
  actually fitted, let alone predicted.
- `Λ_geom` is an undefined multiplicative function. With `ω₀` free, `n` free per particle and
  `Λ_geom` free, the equation is `M = M`.

Everything downstream of §1.2 in Chapters 1–4 (nucleon splitting, thermodynamic mass scaling,
the harmonic catalog, mass gaps, vacuum recalibration) inherits this: each adds a new named
quantity (`γ`, `Δψ(n)`, `f(Ξ)`, `Ξ`, `P_geom`, `τ_global`) without a definition that could be
evaluated. There is no point in Chapters 1–4 at which a number could have come out wrong.

## What the "Cradle Test" actually is

Chapter 1 §1.5 and Chapter 5 §5.2 cite the Cradle Test as *validation* of thermodynamic
scaling "at the CMB recombination epoch". The code is `src/test_early_universe.py` →
`src/analysis/bridge_stress.py`, `interbrane_potential.py`:

    τ(n)     = 2.72548 · (41.4 / (1+n)) · exp(−0.05 n) · sin(n)
    V_gap(n) = 1 / sqrt(1+n)
    n        = 1.40   # "harmonic depth at 380,000 years"
    n_today  = 41.4

- `n` here is a time coordinate, not the harmonic index of §1.2, though it uses the same
  letter; the mapping 380 kyr → 1.40 and today → 41.4 is not stated anywhere.
- The prefactor is the CMB temperature in kelvin; `V_gap` is dimensionless; they are then
  added (`total_equilibrium = τ + V_gap`).
- `sin(n)`, `exp(−0.05 n)` and `41.4` are unexplained. Nothing is compared with data; the
  script prints four numbers and the line `Expectation: High amplitude`.

So the single empirical anchor claimed for Chapters 1–4 is a plot of an arbitrary damped
sine. This is the point at which the manuscript started to *describe itself* as validated.
Chapter 5 §5.2 further claims a "symbolic audit tier" checked dimensional consistency; the
kelvin-plus-dimensionless sum above, and `L_node = ħ/(Δf·M_Pl)` (an area, see
`RETRACTED.md` R2), show that tier did not run.

## Chapter-by-chapter

| Ch. | Status | Reason |
|---|---|---|
| 1.1–1.2 prose | **keep as premise** | Two overlapping branes; `τ`, `V_gap` as names for tension and gap potential. This is the v2 axiom, minus the tori. |
| 1.2 eq. | **hard stop** | `M = n ω₀ Λ_geom`, see above. |
| 1.3 | drop | `γ` is a free number here; Ch 3 fixes `γ = π`, which gives a 50 % n–p split. Same symbol, incompatible values. |
| 1.4 | fold into Ch 3 | Restated there. |
| 1.5 | drop | Rests on the Cradle Test. |
| 2 (all) | drop | Adds `Δψ(n)`, `f(Ξ(t))`, `Ξ = τ + V_gap`. No `n` assignments exist anywhere. "Geometric impedance" and "mass gaps" are prose. `M_n(t) ∝ f(Ξ(t))` also implies drifting `m_p/m_e`, bounded by quasar spectroscopy at ~10⁻⁷; never confronted. |
| 3.2 | keep as definition, not result | `Ψ(θ+2π) = −Ψ` is the SU(2)→SO(3) double cover. Correct, generic to every theory with fermions; earns nothing. |
| 3.3 | drop | `Q = ∮ P_geom · dA = ±e`: `P_geom` undefined, so the equation defines `P_geom`, not `Q`. Charge quantisation is asserted. |
| 3.4 | drop | Coulomb-as-impedance prose; no potential, no 1/r². |
| 4.1–4.2 | drop | Photon plane wave with amplitude "constrained by τ" (how is not said); annihilation restated in words. |
| 4.3 | **keep as hypothesis** | Collision-induced chiral bias → baryon asymmetry is a real, computable target (v2 milestone 5: `η_B` from impact kinematics). The equation `ΔE = E₀(1 ∓ τ_global)` is a placeholder — `τ_global` has no value, and no `η_B ≈ 6×10⁻¹⁰` is produced. |
| 5 | drop from theory | Methodology chapter. Its claims about audit tiers are contradicted by the record above. |
| 7.2 | drop | `g_μν = η_μν + Ξ_μν(τ + V_gap)` is a *different* gravity theory from Appendix F, which derives exact GR from the same action. Both cannot hold; F is the one that follows from the action. |
| 7.4 | **keep as hypothesis** | "Dark energy = residual inter-brane potential" is exactly `V(Φ)` in the v2 action. Testable via `w(z)`. |
| App. E | keep, generic | Standard KK reduction of a bulk scalar. Correct, not BMI-specific. |
| App. F | keep, generic | Standard Gauss–Codazzi projection. Correct at the level written (junction conditions and `E_μν` omitted — v2 skeleton §2 restores them). Not BMI-specific. |
| 8–14, App. G–J | not needed | Everything from Ch 8 onward builds on `Ξ`, `τ(t)`, `K`, `L_node`, 15 Hz; see `RETRACTED.md`. Ch 13 (SM from `343` winding states) is the harmonic trap in a different costume and is not audited further here. |

## What survives into v2

1. Two branes, one bulk, ongoing merger (Ch 1 prose) → `v2/00_axiom.md`.
2. Dark energy as inter-brane potential (Ch 7.4) → `V(Φ)` in `v2/01_action_skeleton.md`.
3. Baryon asymmetry from impact chirality (Ch 4.3) → milestone 5 target, must output `η_B`.
4. KK reduction and Gauss–Codazzi (App. E, F) → milestone 3 boilerplate, credited as generic.
5. Spinor double cover (Ch 3.2) → a definition; not listed as a prediction.

Everything else in Chapters 1–4 is retired. It is not that the deeper math was wrong; there
was no math to be wrong. The first equation had no evaluable content, and every later chapter
added names rather than constraints.
