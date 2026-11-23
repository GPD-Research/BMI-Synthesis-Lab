# BMI v0 — the original concept

> **Status: pre-mathematical.** This is the concept BMI started from, recorded 2026-11-23 in the
> author's terms. Nothing here is derived, and nothing here changes `v2/`. It exists so that the
> next action is built from the intended idea, not from whatever a toolset found easiest to keep.

## Why v0 exists

| version | how it was built | what happened to the concept |
|---|---|---|
| **v0** | the author's intuition, plus an earlier collision-geometry model (private manuscript); named *Binary Mass Interaction* | never written down as one document; two infographics survive (`figures/`) |
| **v1** | non-agentic AI tools that condensed prose they judged unnecessary | much of v0 was stripped out; what survived was bent (e.g. the arrows of time merge *at* T=0, `Master_BMI_Manuscript.md` §11.3; brane thickness became an unsupported number, `RETRACTED.md` R2). The drift is already visible in the proto-v1 infographic: per-particle "geometric constants" κ labelled as derived masses (one dial per particle, the start of R4), a claimed "simulations and LHC dataset analysis" with nothing behind it, and an Ω_BMI(z) placeholder with no formula |
| **v2** | action-first, ledger, kill criteria written before derivations | sound method, but rebuilt on v1's stripped premises using standard braneworld machinery: thin branes, a collision *as* the Big Bang, one shared interval |

v2's method is kept. What v0 corrects is the premise.

## The concept (author's voice)

Only the author edits this section, or someone with the author's explicit approval.

- **C1. Two universes, two branes.** Each universe has its own dimensions. They touch and shear
  against each other, with partial overlap of their "outer" dimensions. It is not one shared
  brane.
- **C2. The interaction is thick.** The overlap is a region with finite and changing extent,
  not a sharp surface.
- **C3. The collision is gradual and came after the Big Bang.** It is continuous and messy, as
  nature usually is, not a single instant at an apparent singularity.
- **C4. Energy and radiation bleed both ways** across the overlap.
- **C5. Two arrows combine into one.** There is one time dimension. Our cosmological arrow is the
  old one. Our thermodynamic arrow is new: our old arrow plus the input from the other universe.
  The change cascades through our evolution, and seen from today it looks like two inflations:
  one at the Big Bang and one appearing later as the accelerated expansion.
  *(This replaces an earlier version with two time dimensions.)*
- **C6. Primordial black-hole evaporation is the observable face of the leakage.** In the
  author's view, Hawking radiation is shown only by analogy.
- **C7. Convergence as a zipper.** The earlier model described convergence with a "zipper
  diagram", its own version of a KK tower. It is a lower-dimensional cross-section of the
  convergence dynamics, not a whole cosmology.

- **C8. Universes are normally cyclic; ours is the last cycle.** A universe normally ends in a big
  crunch, and the crunch singularity is innately unstable, so it erupts into a new big bang. The
  continuing collision with the other universe broke that cycle for ours. It is the source of the
  dark-energy expansion, which makes this iteration the final one, ending in heat death.

- **C9. The universes braid together.** From the infographics: two strands start isolated, meet at
  a divergence point, twist around each other and converge into one trunk that grows to a
  "maximum stable diameter", an equilibrium state.
- **C10. Crosstalk across an imperfect barrier is the dark sector.** The bridge is a shared
  interaction zone behind a semi-permeable membrane. Inductive coupling across it shows up as
  dark-energy pressure (an expansion vector) and as dark matter, the gravity of the other
  universe "ghosting" into ours.
- **C11. Mass comes from the bridge.** The two universes' Higgs fields overlap and intertwine in
  the bridge, and that overlap modulates particle masses. The coupling constant was born at the
  first overlap.
- **C12. Short-circuit events near supermassive black holes.** At extreme energy density the
  bridge can locally short-circuit.

**Hoped-for outputs, once the foundations are set:** neutrino masses, gravitational-wave
anomalies, and the early-galaxy maturity seen by JWST.

## Open questions (author's voice)

- **O1. Is the collision the origin, or does it come after the big bang?** The proto-v1
  infographic puts the origin at the first intersection, while C3 and C8 put the collision after
  our big bang. The author doesn't think these are mutually exclusive; it may be a relativistic
  question of perspective. Left undefined for now.

## Constraints (a separate voice)

A constraint can reject a derivation. It cannot rewrite a concept above. Anything marked
[verify] was given from memory and has not yet been checked against a source.

| concept | what it has to get past | data that tests it |
|---|---|---|
| C1, C2 | Static thick walls made from an ordinary scalar must all have positive tension (`v2/10_thick_brane.md`, `tests/thick_brane.py`). Two such walls attract, so the setup is dynamic by construction. | GR and ΛCDM limit; Cassini and LLR |
| C3 | A post-Big-Bang onset must leave early-universe physics untouched, or show exactly where it doesn't | BBN, CMB |
| C4 | Leakage into extra dimensions shows up as dark radiation | ΔN_eff (Planck ≲ 0.3; CMB-S4 ±0.03) |
| C5 | To be a prediction it must give the *timing* of late acceleration (onset near z ≈ 0.6), which is the cosmic-coincidence problem. Entropy injection must stay within the distortion limits for whatever epoch it happens in. | DESI w(z); CMB spectral distortions; ΔN_eff |
| C6 | Hawking evaporation follows from standard QFT on curved spacetime. Holes lighter than ~5×10¹⁴ g have evaporated by now; heavier ones would survive unless the mass spectrum is cut off. Evaporation products are bounded (Carr et al. [verify]). The LHC has seen no micro black holes; those required TeV-scale gravity and are excluded to ~9–10 TeV [verify]. The direction of energy flow must be stated. | BBN, CMB, gamma-ray background |
| C7 | A lower-dimensional picture must be shown to be a consistent slice of the full dynamics | follows from C1–C3 |
| C8 | Cyclic models have to deal with entropy building up from cycle to cycle (Tolman's problem) and with getting through the bounce without a singularity. Steinhardt–Turok cyclic cosmology and Penrose's conformal cyclic cosmology (CCC) are precedents to read first. For "final cycle", the dark energy must not decay back into recollapse, or the cycle would resume. Bounce models usually predict a tiny tensor ratio r [verify]. | DESI w(z) (does dark energy weaken?); CMB-S4 r |
| C9 | A preferred twist would be a handedness in our universe, i.e. parity violation on cosmological scales, bounded by CMB isotropy and polarization; the cosmic-birefringence hint is a possible handle [verify]. An equilibrium "maximum stable diameter" must be reconciled with C8's heat death. | CMB TB/EB polarization; large-angle isotropy |
| C10 | Dark matter must act as pressureless matter by recombination (CMB acoustic peaks), with the right abundance, and separate from gas as in the Bullet Cluster. v2's mirror-matter dark matter died on abundance (`RETRACTED.md` N2), which is the warning. Dark-energy pressure is as for C5. | CMB peaks; Bullet Cluster; rotation curves; DESI w(z) |
| C11 | Measured Higgs couplings agree with the Standard Model to roughly 10% [verify], so a second Higgs mixing in must stay within that. Masses must follow from a few overlap parameters, not one per particle, or this is R4 again. | LHC Higgs couplings; fermion mass ratios |
| C12 | Needs a stated signature (spectrum, energy, rate) registered before any data are looked at, and it must differ from ordinary accretion and jet physics. | EHT; AGN gamma rays and neutrinos; LVK |
| outputs | Each must be registered before the data are looked at; v1's 15 Hz split (R1) is the warning. JWST tension has eased as mass estimates were revised [verify]. | oscillation data; LVK; JWST |

## Figures

![v0 cover: the two strands braid into one universe](figures/v0_cover_braid.jpg)

*v0 cover ("Binary Mass Interaction"): Σ_A and Σ_B braid and converge.*

![proto-v1 topology: two conductors, a bridge, crosstalk as the dark sector](figures/proto_v1_conductor_topology.jpg)

*Proto-v1 topology (Gemini era): concepts C9–C12. Its mass table, provenance claims and equations
are the drift recorded above, not results.*

## What v0 asks of the next version

1. **Pick a framework that fits v0, before writing any equations.** Candidates:
   - two thick positive-tension walls that approach and merge (option 2 of
     `v2/10_thick_brane.md`);
   - overlapping or intersecting branes (C1's shearing picture);
   - colliding vacuum bubbles: no branes at all, and a CMB-imprint test that already has
     constraints [verify].

   For each candidate: what it forces, what it costs in parameters, what data could kill it, and
   which of C1–C12 it can't hold.
2. **Write the action only after that**, keeping v2's rules: the ledger, kill criteria written
   first, and `RETRACTED.md`.
3. **Check the draft action against C1–C12, one by one.** A concept the action drops is recorded
   as dropped, with the reason, never silently.
