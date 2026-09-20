# BMI Parameter Ledger

Compiled from `master_axiom.md` (73 equations, 19 chapters). Every symbol that must be supplied from outside the theory is listed once, with where it appears, what kind of freedom it represents, and whether anything currently pins it down.

Freedom classes (in increasing order of how much they let the theory "answer anything"):

| class | meaning |
|---|---|
| **N** | a number (one real constant) |
| **T** | a tensor / matrix of numbers (several constants at once) |
| **F** | a free *function* — infinite freedom unless its form is derived |
| **I** | an integer label assigned per particle/state (free per datum) |
| **B** | borrowed — a standard-physics input taken as given (not BMI's, but not derived either) |

Status codes: `derived` (follows from the action), `fitted` (set to match data), `asserted` (stated, no derivation), `undefined` (name only, never given a form), `killed` (retracted by the authors).

---

## A. Fundamental / structural constants

| # | symbol | class | where | status | notes |
|---|---|---|---|---|---|
| 1 | \(\kappa_6\) (6D gravitational coupling) | N | Appx F | asserted | not related numerically to \(G_N\); the integral over \(\delta\) that would fix it is stated in words only |
| 2 | \(\delta\) (brane thickness) | N | Appx E, F, Ch 9, 13, 14 | asserted, \(\approx 10^{-15}\) m | value inherited from the killed 15 Hz result (Ch 12 / Appx J); now unsupported. Sets KK scale \(\hbar c/\delta \approx 200\) MeV |
| 3 | \(L_{\text{local}}\) | N | Appx B | bounded only (\(>93\) Gly) | lower bound copied from CMB topology limits; no upper bound, no prediction |
| 4 | \(L_{\text{shadow}}\) | N | Appx B | undefined (\(\ll d_H\)) | no numerical value anywhere; the ratio \(V_{local}/V_{shadow}\) is therefore also undefined |
| 5 | \(L_{\text{node}}\) | N | Ch 12, Appx J, Ch 14 | killed | derived from \(\Delta f = 15\) Hz; \(L_{node} = \hbar/(\Delta f\, M_{Pl})\) is also dimensionally wrong (gives seconds·kg\(^{-1}\)... needs \(c\)); with the 15 Hz claim retracted this has no basis |
| 6 | \(\omega_0\) (base frequency) | N | Front matter, Ch 1, 2, 8 | fitted | the single scale of the harmonic mass formula; value not stated in the compiled equations |
| 7 | \(\gamma\) (Berry phase) | N | Ch 1, 3 | asserted \(=\pi\) in Ch 3, free in Ch 1 | Ch 3 fixes \(\gamma=\pi\) (spinor double cover, generic); Ch 1 uses \(\gamma/2\pi\) as a nucleon splitting factor — if \(\gamma=\pi\) that predicts a 50% n/p mass split, which is wrong by 3 orders of magnitude, so \(\gamma\) must be a *different* fitted number in Ch 1. **Internal inconsistency.** |
| 8 | \(\mathcal K\) (curvature coupling) | N | Ch 12, Appx J | killed | 0.13, inferred from the 15 Hz data; circular with Appx J's "fixed prior" claim |
| 9 | \(\Theta_P\) (Planck tension) | N | Appx J | B / undefined | never defined numerically |
| 10 | \(\Omega_{node}\) (node eigenfrequency) | N | Appx J | undefined | never given a value |
| 11 | \(w_{max}\) | I (global) | Ch 13 | asserted \(=3\) | gives \(7^3=343\); no reason given for 3 |
| 12 | \(\Omega_{max}\) (impedance cutoff) | N | Ch 13 | fitted, 3.5 | chosen so the surviving winding states match the count of SM states; "validated" by CKM unitarity, which every unitary matrix satisfies |
| 13 | \(\lambda\) (tension coupling in \(\mathcal T_{int}\)) | N | Ch 13 | undefined | |
| 14 | \(\tau_{global}\) (chiral torsion) | N | Ch 4 | undefined | should produce \(\eta_B \approx 6\times10^{-10}\); never computed |
| 15 | \(E_0\) (activation energy) | N | Ch 4 | undefined | |
| 16 | \(\alpha\), \(R_{crit}\) (screening gate) | N, N | Ch 9 | undefined | note \(R=0\) in vacuum outside any source, so the gate is 0 everywhere a bubble-chamber electron actually travels — the mechanism cannot work as written with the Ricci scalar; would need Weyl/Kretschmann curvature |
| 17 | \(\kappa\), \(\lambda\), \(\mathcal C\), \(\mathcal A\) (Mott functional) | N ×4 | Ch 9 | undefined | standard delta-potential bound state; not BMI-specific |
| 18 | \(q\) (charge) | N | Ch 10 | B | taken from U(1) gauge theory; Ch 3's \(Q=\pm e\) is asserted, not computed from \(\mathbf P_{geom}\) |

**Subtotal: 18 named constants (21 counting the ×4 in row 17), of which 0 are derived, 3 are fitted, 3 are killed, and ~12 have no value at all.**

---

## B. Free functions, tensors and matrices

These are the critical entries. Each one is an unbounded reservoir of fitting freedom.

| # | symbol | class | where | status | what it can absorb |
|---|---|---|---|---|---|
| 19 | \(f(\Xi(t))\) | F | Ch 2, Ch 8 | undefined | any cosmological time-dependence of *every* mass; also must be tuned to \(\lvert\Delta\mu/\mu\rvert<10^{-7}\) at \(z\sim3\) and to BBN constraints — currently unconstrained |
| 20 | \(\Delta\psi(n)\) / \(\Delta\psi_{\text{harmonic}}\) | F of I | Front matter, Ch 2 | undefined | a free correction *per harmonic index* — with this, \(M=n\omega_0(1+\Delta\psi(n))\) fits **any** spectrum exactly (set \(\Delta\psi(n) = M_n/(n\omega_0)-1\)). Zero predictive content until its functional form is fixed. |
| 21 | \(\Lambda_{\text{geom}}\) | F (of orientation, boundary conditions) | Ch 1 | undefined | same role as \(\Delta\psi\) under a different name |
| 22 | \(\mathbf\Lambda_{\text{tensor}}\) | T | Ch 8 | undefined | any field-dependent mass shift |
| 23 | \(\mathbf\Xi_{\mu\nu}(\tau+V_{gap})\) | T-valued F | Ch 7 | undefined | any metric deviation from Minkowski, i.e. all of cosmology and gravity phenomenology; not connected to Appx F's \(G_{\mu\nu}=8\pi G T_{\mu\nu}\) |
| 24 | \(\tau(t)\) (Bridge Stress) | F | Ch 4, 7 | undefined | any time evolution of the vacuum; candidate dark energy, but no functional form |
| 25 | \(V_{gap}(t)\) (inter-brane potential) | F | Ch 7, 13 | undefined | same |
| 26 | \(\mathbf Z_{ij}(\Xi)\) (impedance tensor) | T-valued F | Ch 6, Ch 13 | undefined | any interaction strength between any pair of states; in Ch 13 it multiplies winding numbers inside \(M_n^2\), so the KK mass spectrum itself is free |
| 27 | \(\mathbf B_{\text{compact}}(n)\) | F of I | Ch 7 | undefined | never used downstream |
| 28 | \(\mathbf P_{\text{geom}}\) | vector field | Ch 3 | undefined | charge integral asserted to give \(\pm e\); the field is never specified so quantization is not shown |
| 29 | \(\Phi_{bridge}\), \(\Phi_{\text{shadow}}\), \(\rho_{\text{shadow}}\) | fields | Ch 13, Appx B | undefined | named, never given equations of motion |
| 30 | \(\mathcal T_{int}\) | F | Ch 13, Appx J | partly defined (Ch 13) | in Appx J it is a per-event local value; not computable from the Ch 13 definition without \(\lambda\), \(\Phi_{bridge}\) |
| 31 | \(\chi_{nm}(y,z)\) boundary conditions | F | Appx E | asserted | "imposed by the bulk-interface tension" — not written down, so the KK spectrum \(M_{nm}\) is not actually computed |
| 32 | "Impedance Coupling" in \(D_H\) | N (undefined) | Ch 14 | undefined | the only ingredient of \(D_H = 2 + \ln(\text{IC})/\ln(L_{node}/\delta)\) that isn't already dead: \(L_{node}\) is killed and equals \(\delta\) by assertion, so \(\ln(L_{node}/\delta) = \ln 1 = 0\) and the formula **diverges**. \(D_H\approx1.738\) cannot come from this expression. |

**Subtotal: 14 free functions/tensors, 0 derived.** Any one of rows 19, 20, 23, or 26 alone is sufficient to fit arbitrary data in its domain.

---

## C. Per-state integer assignments

| # | symbol | class | where | status |
|---|---|---|---|---|
| 33 | \(n\) (harmonic index) per particle | I | Ch 1, 2, 8 | fitted per particle — one integer per mass; with \(\Delta\psi(n)\) also free this is doubly redundant |
| 34 | \(\sigma\in\{-1,0,1\}\) per nucleon | I | Ch 1 | fitted |
| 35 | \((w_x,w_y,w_z)\) per state | I ×3 | Ch 13 | fitted; the map from winding triple to SM particle is not given in the compiled equations |

---

## D. Borrowed standard-physics inputs (not BMI's, not derived)

\(H_0, \Omega_{m,0}, \Omega_{\Lambda,0}\) (Appx B — the "age of the cosmos" chapter is ΛCDM verbatim), \(G_N\), \(\hbar\), \(c\), \(M_{Pl}\), \(e\), the SM gauge structure (Ch 10 introduces U(1) only), the CKM matrix, the Dirac Lagrangian (Ch 13). ΛCDM's six parameters are all used and none is replaced.

---

## E. Ledger totals

| category | count | derived from the action |
|---|---|---|
| named constants (A) | 21 | 0 |
| free functions / tensors (B) | 14 | 0 |
| per-state integer labels (C) | 3 families | — |
| borrowed inputs (D) | ≥ 6 ΛCDM + SM content | — |
| **quantitative outputs claimed** | 3: \(D_H=1.738\), \(\Delta f=15\) Hz, \(N=343\to\) SM state count | 15 Hz killed; \(D_H\) formula degenerate; 343 depends on fitted \(w_{max}\), \(\Omega_{max}\) |
| **surviving un-fitted numerical predictions** | **0** | |

Ledger balance: **(0 predictions) − (21 constants + 14 free functions) → strongly negative.** SM + ΛCDM: ~25 parameters against \(\gg 10^3\) independent measurements.

---

## F. What actually survives (the honest core)

Derivable and correct, but generic to any 6D thick-brane model:

1. Appx F: Gauss–Codazzi reduction \(\to G_{\mu\nu} = 8\pi G_N T_{\mu\nu}\) (needs the \(\kappa_6\to G_N\) integral written out, and the \(K^2 - K_{\mu\nu}K^{\mu\nu}\) terms kept — they are the only place new physics can enter).
2. Appx E: KK tower from a compact 2D fibre (needs the boundary conditions written down to become a prediction).
3. Ch 3: spinor double cover (correct, textbook).
4. Ch 10: U(1) covariant derivative (correct, textbook; SU(2)×SU(3) absent).

Nothing else in the file is currently a derivation.

---

## G. Gutting list, in priority order

1. **Delete or derive \(\Delta\psi(n)\), \(\Lambda_{\text{geom}}\), \(f(\Xi)\).** As long as any of these is free, the mass sector cannot be wrong and therefore cannot be right.
2. **Give \(\Xi_{\mu\nu}\), \(\tau(t)\), \(V_{gap}(t)\) equations of motion** from the 6D action, or remove Ch 7 and let Appx F be the gravity sector.
3. **Decide \(\delta\).** It currently rests on the killed 15 Hz result. Either commit to \(\delta\sim10^{-15}\) m and identify the KK tower with hadrons (then run the PDG null test), or push \(\delta\) below \(10^{-19}\) m.
4. **Remove \(L_{node}\), \(\mathcal K\), Ch 12, Appx J** to a "retracted results" appendix. Fix the dimensional error in \(L_{node}\) if the concept is kept.
5. **Recompute or drop \(D_H = 1.738\)**; the stated formula is \(2 + \ln(\text{IC})/\ln 1\).
6. **Resolve \(\gamma\)**: \(\pi\) (Ch 3) vs. the small value Ch 1 needs.
7. **Replace the Ricci-scalar gate** in Ch 9 with an acceleration- or Weyl-curvature trigger, or drop the Mott chapter.
8. **Compute one number**: \(\eta_B\) from \(\tau_{global}\), or \(\Omega_{DM}/\Omega_b\) from the bridge friction, or \(a_0\) from \(\dot\tau/\tau\). One un-fitted hit moves the ledger to positive.
