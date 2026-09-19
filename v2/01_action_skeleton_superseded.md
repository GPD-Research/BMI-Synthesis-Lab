# BMI v2 — Action and Parameter Budget (skeleton)

Purpose: a minimal, attackable starting point for the rebuild. Everything below is either (a) standard two-brane machinery with references, or (b) marked **[BMI]** where a genuinely new assumption enters. Nothing here is a result; the point is to fix the budget *before* solving anything.

---

## 0. Axiom

> Two 4-dimensional branes, \(\Sigma_1\) (ours) and \(\Sigma_2\), are embedded in a 6-dimensional bulk. They collided at \(t=0\) and are now slowly merging. Matter on \(\Sigma_2\) couples to matter on \(\Sigma_1\) only through bulk gravity and, at most, one bulk scalar field.

Everything must follow from this or be deleted.

---

## 1. Setup and coordinates

- Bulk: \(\mathcal M_6\) with coordinates \(X^A = (x^\mu, y, z)\), metric \(G_{AB}\), signature \((-,+,+,+,+,+)\).
- Branes: \(\Sigma_i\) located at \(y = Y_i(x)\), \(z = Z_i(x)\). In the homogeneous limit \(Y_i = Y_i(t)\), \(Z_i = Z_i(t)\).
- **Separation field** \(\phi \equiv\) proper bulk distance between the branes along a geodesic normal to \(\Sigma_1\). This is the inspiral coordinate. In the two-brane RS literature this is the radion; the cyclic model calls it the same thing (Steinhardt & Turok 2002). We inherit that name and its known dynamics.
- Two compact bulk directions are *not* assumed a priori. Whether \(y,z\) are compact (Appx B's \(T^2\) fibre) is a **decision to make**, not an axiom. Recommendation: start with one non-compact bulk direction \(y\) (codimension-1 pair of branes, as in RS/cyclic) and one compact \(z\) of size \(\ell_z\) only if a KK tower is ever needed. Codimension-2 branes in 6D have conical singularities and a much harder junction problem (see Vinet & Cline 2004); do not start there.

---

## 2. Action

\[
S = S_{\text{bulk}} + S_{\Sigma_1} + S_{\Sigma_2} + S_{\text{GHY}}
\]

\[
S_{\text{bulk}} = \int d^6X \sqrt{-G}\left[\frac{M_6^4}{2}R_6 - \frac12 (\partial\Phi)^2 - V(\Phi)\right]
\]

\[
S_{\Sigma_i} = \int_{\Sigma_i} d^4x \sqrt{-g_i}\left[-\sigma_i(\Phi) + \mathcal L^{(i)}_{\text{matter}}(g_i, \psi_i)\right]
\]

where:

| symbol | role | class |
|---|---|---|
| \(M_6\) | 6D Planck mass | N |
| \(\Phi\) | one bulk scalar; its value at each brane sets the tension and mediates the inter-brane force | field |
| \(V(\Phi)\) | bulk potential; **form must be chosen from a finite menu** (see §3) | F → N |
| \(\sigma_1, \sigma_2\) | brane tensions; may depend on \(\Phi\) at the brane | N, N (+ coupling) |
| \(\mathcal L^{(1)}_{\text{matter}}\) | the Standard Model, borrowed as-is | B |
| \(\mathcal L^{(2)}_{\text{matter}}\) | **[BMI]** matter on the other brane; minimal choice: a copy of the SM (mirror sector) or a single fluid with equation of state \(w_2\) | B or N |
| \(S_{\text{GHY}}\) | Gibbons–Hawking–York boundary terms; needed for Israel junction conditions | — |

**Junction conditions** (Israel 1966) at each brane fix the extrinsic curvature jump in terms of \(\sigma_i\) and the brane stress-energy. In 6D codimension-1 they read \([K_{\mu\nu}] - g_{\mu\nu}[K] = -M_6^{-4}\,S^{(i)}_{\mu\nu}\). This is what Appendix F should have been: the Einstein equation on \(\Sigma_1\) comes out with the standard correction terms (Shiromizu–Maeda–Sasaki 2000):

\[
G_{\mu\nu} = 8\pi G_N T_{\mu\nu} + \frac{1}{M_6^8}\pi_{\mu\nu}(T^2) - E_{\mu\nu} + (\text{radion terms})
\]

- \(\pi_{\mu\nu} \propto T^2\): negligible today, matters at \(\rho \gtrsim M_6^4\) (the impact).
- \(E_{\mu\nu}\): projected bulk Weyl tensor — "dark radiation". Bounded by BBN: \(\rho_E/\rho_\gamma \lesssim 0.1\).
- Radion terms: this is where \(\phi(t)\) enters 4D cosmology. Carries the whole "ongoing merger" hypothesis.

---

## 3. Parameter budget (fix before solving)

| # | parameter | meaning | fixed by |
|---|---|---|---|
| 1 | \(M_6\) | bulk gravity scale | \(G_N\) once \(\phi_0\) is known: \(M_{Pl}^2 \sim M_6^4\, \phi_0\) (one relation, so \(M_6\) and \(\phi_0\) are not independent) |
| 2 | \(\phi_0\) | present brane separation | see #1 |
| 3 | \(\sigma_1\) | our tension | RS-type tuning \(\sigma_1^2 \sim M_6^4\,\Lambda_6\) — **this is the cosmological-constant problem; do not hide it.** State the tuning explicitly. |
| 4 | \(\sigma_2\) | their tension | \(\sigma_2/\sigma_1\) is free → candidate for \(\Omega_{DM}/\Omega_b\) |
| 5–6 | \(V(\Phi)\) shape | inter-brane potential | choose ONE from: exponential \(V_0 e^{-c\Phi/M_6^2}\) (2 params: \(V_0, c\)); or Goldberger–Wise quadratic (2 params). No further freedom. |
| 7 | \(T_2/T_1\) at reheating | temperature asymmetry of the two sectors | **[BMI] target: derive from impact kinematics, not fit** |
| 8 | \(w_2\) or mirror-SM | second-sector matter | 0 or 1 params |

**Budget: 7–8 numbers, 0 free functions.** ΛCDM has 6. If the rebuild needs a 9th, write down why before adding it.

Explicitly banned: any function of \(n\), any tensor whose components are not computed from \(G_{AB}\), any epoch-dependence not carried by \(\phi(t)\).

---

## 4. Forced consequences (must be computed, each can kill the theory)

### 4.1 Effective 4D Newton constant

With two branes, \(G_N\) on \(\Sigma_1\) depends on \(\phi\). In RS-type warped setups \(G_N^{-1} \propto M_6^4 \,\ell\,(1 - e^{-2\phi/\ell})\); in flat bulk \(G_N^{-1} \propto M_6^4\,\phi\). Either way an inspiral means \(\dot\phi \neq 0 \Rightarrow \dot G/G \neq 0\).

\[
\frac{\dot G}{G} \approx -\frac{\dot\phi}{\phi} \quad (\text{flat bulk})
\]

**Test:** lunar laser ranging gives \(|\dot G/G| < 1.5\times10^{-13}\ \text{yr}^{-1}\) (Hofmann & Müller 2018; treat as approximate). Since \(H_0 \approx 7\times10^{-11}\ \text{yr}^{-1}\), the inspiral must satisfy \(\dot\phi/\phi \lesssim 2\times10^{-3}\,H_0\). **First kill criterion:** if the merger timescale implied by \(V(\Phi)\) is \(\lesssim 500\,H_0^{-1}\), the theory is dead, or \(G_N\) must be made \(\phi\)-independent by construction (which is possible in warped geometries where \(\Sigma_1\) is the UV brane — a real modelling choice with consequences for #1).

### 4.2 Dark-energy equation of state

The radion kinetic + potential energy on \(\Sigma_1\) behaves as quintessence:

\[
w_\phi(z) = \frac{\tfrac12\dot\phi^2 - V_{\text{eff}}(\phi)}{\tfrac12\dot\phi^2 + V_{\text{eff}}(\phi)}
\]

For an exponential \(V_{\text{eff}}\) with slope \(c\), the late-time attractor gives \(w_\phi\) and its derivative \(w_a\) as functions of \(c\) alone (Copeland, Liddle & Wands 1998). So **\(w_0, w_a\) are predicted by one number \(c\)**, which is also the number controlling \(\dot G/G\) in 4.1. One parameter, two observables.

**Test:** DESI DR2 + CMB + SNe (2025) report \(w_0 \approx -0.75\), \(w_a \approx -0.9\) at ~3–4σ preference over \(\Lambda\) (treat numbers as approximate; look up the current release). Note the sign: DESI prefers \(w\) *crossing* \(-1\) (phantom in the past). A single canonical scalar rolling down a potential **cannot** cross \(w=-1\). If the DESI trend holds, a minimal radion is excluded and the merger would need the radion to be non-canonical or the \(E_{\mu\nu}\) term to contribute — that's a real fork, decide it early.

### 4.3 Temperature ratio of the two sectors

**[BMI]** — the one place the collision picture is non-generic. After a brane collision, each brane reheats to a temperature set by its own tension and the kinetic energy deposited. For asymmetric tensions or an oblique impact, \(T_2/T_1 \neq 1\).

\[
\frac{T_2}{T_1} = \left(\frac{\epsilon_2}{\epsilon_1}\right)^{1/4}\quad\text{where } \epsilon_i = \text{energy deposited per unit 3-volume on } \Sigma_i
\]

**Test:** BBN + CMB \(N_{\text{eff}}\) require the mirror sector to be cold: \(T_2/T_1 \lesssim 0.3\)–\(0.5\) (Berezhiani, Comelli & Villante 2001). If the impact kinematics give \(T_2/T_1 \sim 1\), dead. If they give \(\lesssim 0.3\) *for a reason* (tension asymmetry), that is the first thing BMI would predict that mirror-matter models merely assume.

### 4.4 Dark-matter fraction

If sector-2 matter is our DM, then \(\Omega_{DM}/\Omega_b \approx 5.3\) must come from \((\sigma_2/\sigma_1, T_2/T_1)\) via sector-2 baryogenesis. In mirror models with \(T_2 < T_1\), the mirror baryon asymmetry is typically *larger* (Berezhiani 2004), giving \(\Omega_2/\Omega_1 > 1\) naturally — a qualitative success available to BMI immediately. Turning it into 5.3 is the target.

**Test 2:** sector-2 matter has its own EM and dissipates → dark disks, compact dark objects. Constraints: Bullet Cluster (\(\sigma/m \lesssim 1\ \text{cm}^2\text{g}^{-1}\)), halo shapes, MACHO microlensing limits. Mirror-matter survives these only with \(T_2/T_1 \lesssim 0.3\), which ties 4.4 back to 4.3.

### 4.5 The impact as the big bang

The cyclic/ekpyrotic literature already worked out what a brane collision predicts:
- \(n_s \approx 0.96\)–\(0.97\) from the ekpyrotic contraction phase ✔ (matches Planck \(0.965\))
- \(r \lesssim 10^{-3}\) — **far below** inflation's typical range; falsifiable by LiteBIRD / CMB-S4 in the 2030s
- Non-Gaussianity \(f_{NL}\) of order 1–10, local shape; Planck gives \(f_{NL}^{\text{local}} = -0.9 \pm 5.1\), so this is already mildly constraining.

BMI need not redo this — cite it and state that a detection of \(r > 0.01\) kills the collision origin. That alone is a genuine, sharp, pre-registered prediction inherited for free.

### 4.6 Baryon asymmetry

\(\eta_B \approx 6\times10^{-10}\). Old BMI: \(\Delta E_{\text{matter}} = E_0(1-\tau_{\text{global}})\) with no value. New requirement: \(\eta_B\) from CP violation in the impact/reheating with the parameters of §3 *only*. If the framework has nothing to say, leave \(\eta_B\) as an SM/leptogenesis input and do not claim it.

---

## 5. Explore only after §4

Things the solved model might say that nobody asked it to (these become predictions only if they emerge from §2–4 without new parameters):

- Isolated dark-matter-free galaxies (sector-2 structure formation is offset from ours if \(T_2 \neq T_1\); does the offset make isolated DM-free dwarfs possible where ΛCDM's tidal-stripping explanation cannot apply?)
- GW propagation: bulk leakage changes the GW luminosity distance vs EM distance, \(d_L^{GW}/d_L^{EM} \neq 1\) (Deffayet & Menou 2007). LIGO standard sirens already bound this at the ~10% level at \(z\sim0.01\); LISA will reach percent level.
- Dark-radiation \(\Delta N_{\text{eff}}\) from \(E_{\mu\nu}\): CMB-S4 will measure \(N_{\text{eff}}\) to \(\pm0.03\).
- Late-time \(\dot G/G\) sign and its correlation with \(w_a\): a joint prediction nothing else makes.

---

## 6. What is NOT in this skeleton (deliberately)

- Harmonic mass formulas, \(\omega_0\), \(\Delta\psi(n)\), \(\Lambda_{\text{geom}}\).
- Winding-number particle assignments, \(\Omega_{max}\), 343.
- \(\Xi_{\mu\nu}\), \(\tau(t)\), \(V_{gap}(t)\), \(Z_{ij}\) — all replaced by \(\phi(t)\), \(V(\Phi)\), and the junction conditions.
- Seams, \(D_H\), the 15 Hz sector, Mott/screening gate.
- Any claim to derive the Standard Model. \(\mathcal L^{(1)}\) is borrowed.

If any of these are wanted back, they must be re-derived from §2 or they stay out.

---

## 7. Order of work

1. Choose codimension (recommend 1) and \(V(\Phi)\) form. Write §2 fully with signs and factors.
2. Derive the 4D effective action on \(\Sigma_1\): \(G_N(\phi)\), \(V_{\text{eff}}(\phi)\), coupling of \(\phi\) to \(T^{(1)}\) and \(T^{(2)}\).
3. Solve the homogeneous background: \(a(t), \phi(t)\). Read off \(w(z)\) and \(\dot G/G\). Compare to §4.1–4.2. **Stop here if dead.**
4. Impact kinematics → \(T_2/T_1\). Compare to §4.3.
5. Sector-2 cosmology → \(\Omega_2/\Omega_1\), self-interaction, structure formation.
6. Only then §5.

Steps 1–3 are a few sessions of algebra, not a research program; they are where the theory either earns a positive ledger entry or is killed cleanly.
