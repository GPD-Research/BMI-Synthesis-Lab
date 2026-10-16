# Master Axiom

_Compiled mathematical framework of the theory: every governing equation found in the chapter markdown under `/home/gregory-dearth/projects/bmi_project`, kept as LaTeX exactly as written, with the descriptive sentence that introduces it in the source and the definitions of its terms. Narrative exposition lives in the manuscript chapters; this file is the equation-level primer. Regenerate it after editing chapters._

## Governing Equations

### Brane-Manifold Interface (BMI) Theory — Research Repository
_Source: README.md_

- **Two independent heavy-mass binary black hole events — analyzed across different detectors, different observing runs, and separated by four years — both show the BMI-predicted $\Delta f = 15.00\ \text{Hz}$ sub-harmonic frequency split in their post-merger ringdown residuals.**

  $$ S_F = -2[\ln p_1 + \ln p_2] = 42.41 \qquad P_{\text{joint}} = 1.37 \times 10^{-8} \approx \frac{1}{73{,}000{,}000} $$

- **Two independent heavy-mass binary black hole events — analyzed across different detectors, different observing runs, and separated by four years — both show the BMI-predicted $\Delta f = 15.00\ \text{Hz}$ sub-harmonic frequency split in their post-merger ringdown residuals.**

  $$ \boxed{\sigma_{\text{combined}} = 5.557\sigma} $$


### Appendix B: On the Age and Size of the Cosmos
_Source: manuscript/md/Appendix_B_On_the_Age_and_Size_of_the_Cosmos.md_

- **The age of the manifold $t_0$ is calculated by integrating the inverse scale factor evolution from the initial singularity ($a = 0$) to the current epoch ($a_0 = 1$):**

  $$ t_0 = \int_0^1 \frac{da}{a \cdot H(a)} $$

- **Expanding $H(a)$ for a flat spatial geometry governed by non-relativistic matter ($\Omega_{m,0}$) and the cosmological constant ($\Omega_{\Lambda,0}$):**

  $$ H(a) = H_0 \sqrt{\Omega_{m,0} a^{-3} + \Omega_{\Lambda,0}} $$

- **Substituting this into the time integral yields:**

  $$ t_0 = \frac{1}{H_0} \int_0^1 \frac{da}{\sqrt{\Omega_{m,0} a^{-1} + \Omega_{\Lambda,0} a^2}} $$

- **Evaluating this analytically using standard concordance values ($H_0 \approx 67.4 \text{ km/s/Mpc}$, $\Omega_{m,0} \approx 0.315$, and $\Omega_{\Lambda,0} \approx 0.685$):**

  $$ t_0 = \frac{2}{3 H_0 \sqrt{\Omega_{\Lambda,0}}} \ln \left( \frac{\sqrt{\Omega_{\Lambda,0}} + 1}{\sqrt{\Omega_{m,0}}} \right) $$

- **Evaluating this analytically using standard concordance values ($H_0 \approx 67.4 \text{ km/s/Mpc}$, $\Omega_{m,0} \approx 0.315$, and $\Omega_{\Lambda,0} \approx 0.685$):**

  $$ t_0 \approx 13.787 \times 10^9 \text{ years} $$

- **The dimensions of our visible manifold are bounded below by the particle horizon ($d_H$), which is the maximum comoving distance light could have traveled since $t=0$:**

  $$ d_H = c \int_0^{t_0} \frac{dt}{a(t)} \approx 46.5 \text{ billion light-years} $$

- **For a cubic three-torus with fundamental side length $L_{\text{local}}$, the absence of recurring topological ghost images or matched circles in the cosmic microwave background requires that the fundamental scale exceed the diameter of the observable causal sphere:**

  $$ L_{\text{local}} > 2 d_H \implies L_{\text{local}} \gtrsim 93 \times 10^9 \text{ light-years} $$

- **The total spatial volume ($V_{\text{local}}$) of this fundamental domain is calculated as:**

  $$ V_{\text{local}} = (L_{\text{local}})^3 $$

- **Using the strict observational lower bound:**

  $$ V_{\text{local}} \gtrsim (9.3 \times 10^{10} \text{ ly})^3 \approx 8.04 \times 10^{32} \text{ ly}^3 $$

- **The nested secondary manifold exists at a compactification scale $L_{\text{shadow}}$ far below the threshold of standard optical observation. It governs the structural constraints of the auxiliary fields (such as $\Phi_{\text{shadow}}$ and $\rho_{\text{shadow}}$). Its fundamental linear dimension is defined by an intrinsic safety or screening cutoff scale:**

  $$ L_{\text{shadow}} \ll d_H $$

- **The volume ($V_{\text{shadow}}$) of this nested domain is similarly defined by its periodic boundary periodicities:**

  $$ V_{\text{shadow}} = (L_{\text{shadow}})^3 $$

- **Because the manifolds are nested or product-mapped topologically, the ratio of their spatial extents determines the structural coupling gradient across the cosmic voids:**

  $$ \frac{V_{\text{local}}}{V_{\text{shadow}}} = \left( \frac{L_{\text{local}}}{L_{\text{shadow}}} \right)^3 $$


### Appendix E: The Effective Field Theory Limit (QFT Emergence)
_Source: manuscript/md/Appendix_E_Theoretical_Formalization.md_

- **In the BMI framework, the fundamental 6D bulk action for a massless scalar field $\Phi(x^\mu, y, z)$ is defined as:**

  $$ S_{6D} = -\frac{1}{2} \int d^4x \int_0^\delta dy dz \sqrt{-G} G^{AB} \partial_A \Phi \partial_B \Phi $$

- **To recover the 4D physics observable in our interface, we perform a Kaluza-Klein expansion along the compactified dimensions $(y, z)$. We decompose the field $\Phi$ into an infinite tower of modes:**

  $$ \Phi(x^\mu, y, z) = \sum_{n,m} \phi_{nm}(x^\mu) \chi_{nm}(y, z) $$

  - Terms: where $\chi_{nm}(y, z)$ are the normalized eigenfunctions of the Laplace-Beltrami operator $\nabla^2_{y,z}$ on the thick brane domain. These eigenfunctions satisfy the boundary conditions imposed by the bulk-interface tension.

- **Substituting this expansion into the 6D action and integrating over the extra-dimensional coordinates, the action reduces to an effective 4D form:**

  $$ S_{eff} = -\frac{1}{2} \sum_{n,m} \int d^4x [ \partial^\mu \phi_{nm} \partial_\mu \phi_{nm} - M_{nm}^2 \phi_{nm}^2 ] $$

- **The transition amplitude $Z_{6D}$ is defined over the 6D path space. By integrating over the extra-dimensional fluctuations $\chi_{nm}$ as a Gaussian measure, we obtain the reduced propagator:**

  $$ D_F(x - y) = \langle 0 | T\{\phi(x) \phi(y)\} | 0 \rangle = \lim_{\delta \to 0} G_6(x, y; y, z) $$


### Appendix F: Classical Relativity as Macro-Geometry
_Source: manuscript/md/Appendix_F_Classical_Relativity_as_Macro_Geometry.md_

- **We begin with the 6D Einstein-Hilbert action evaluated in the bulk:**

  $$ S_{EH} = \frac{1}{2\kappa_6^2} \int d^6x \sqrt{-G} R_6 $$

- **To project this onto our 4D hypersurface, we use the Gauss-Codazzi relations to express the 6D Ricci scalar $R_6$ in terms of the 4D Ricci scalar $R_4$, the extrinsic curvature tensor $K_{\mu\nu}$, and the acceleration of the normal vectors. Assuming a Gaussian normal coordinate system $G_{AB} = \text{diag}(g_{\mu\nu}, h_{ab})$:**

  $$ R_6 = R_4 + K^2 - K_{\mu\nu}K^{\mu\nu} + \nabla_\mu(a^\mu) $$

  - Terms: where $R_4$ is the intrinsic Ricci scalar of our 4D brane and $K$ is the trace of the extrinsic curvature.

- **Integrating the action over the brane thickness $\delta$ effectively scales the coupling constant $\kappa_6$ to the 4D gravitational constant $G_N$:**

  $$ S_{eff} = \frac{1}{2\kappa_4^2} \int d^4x \sqrt{-g} R_4 + S_{matter} $$

- **Varying this effective action with respect to the induced 4D metric $g^{\mu\nu}$ yields the Einstein Field Equations in 4D:**

  $$ G_{\mu\nu} = 8\pi G_N T_{\mu\nu} $$


### Appendix: Higher-Dimensional Projection Mechanics and the Flatlander’s Lens Theorem
_Source: manuscript/md/Appendix_H_HigherDImensional_Projection_Mechanics.md_

- **Our observable universe is modeled as a 4-dimensional hypersurface (brane) $\Sigma$ embedded in M via the smooth mapping:**

  $$ X^A = X^A(x^\mu) $$

  - Terms: where x^\mu (\mu = 0, 1, 2, 3) denote local spacetime coordinates.

- **The physical metric tensor g_{\mu\nu} measured by 3D observers is the pullback of the bulk metric via the first fundamental form:**

  $$ g_{\mu\nu}(x) = G_AB(X) (\partial X^A / \partial x^\mu) (\partial X^B / \partial x^\nu) $$

- **Let a topological macro-seam (tension fault or string) be represented as a parametric curve $\Gamma$ in the bulk:**

  $$ X^A = \Gamma^A(\lambda) $$

  - Terms: where \lambda is an affine parameter. Because the bulk metric $G_{\text{AB}}$ is non-flat, the true path of the seam is a bulk geodesic satisfying:

- **For any observer restricted to \Sigma_{(d)}, the observed projection \tilde{\Phi} of the bulk feature satisfies the mapping:**

  $$ \tilde{\Phi} = P^* [ \Phi \cdot (g_{(d)}, K_{(d)}) ] $$

  - Terms: where P^* is the dimensional pullback operator, g_{(d)} is the induced metric, and K_{(d)} is the extrinsic curvature tensor field (shear tensor) of the embedding.


### Appendix J: Gravitational Wave Empirical Validation and False-Alarm Rate Analysis
_Source: manuscript/md/Appendix_J_GW_Empirical_Validation_and_FAR_Analysis.md_

- **The coupling between local node tension $\mathcal{T}_{int}$ and the macro-scale strain is defined in Chapter 13 as:**

  $$ \Delta f = \mathcal{K} \cdot \left( \frac{\mathcal{T}_{int}}{\Theta_P} \right) \cdot \Omega_{node} $$

  - Terms: where:
    - $\mathcal{K} = 0.13$ is the non-linear curvature coupling coefficient (BMI baseline)
    - $\mathcal{T}_{int}$ is the local brane interface tension at the merger site
    - $\Theta_P$ is the Planck-scale tension reference
    - $\Omega_{node}$ is the winding-mode oscillation eigenfrequency at the $T^{3}$ node

- **The observed $\Delta f$ and its 40 ms temporal phase-lag between detectors calibrate the compactification radius of the hidden dimension:**

  $$ L_{\text{node}} \approx \frac{\hbar}{\Delta f \cdot M_{\text{Planck}}} \approx 10^{-15}\ \text{m} $$

- **Gaussian significance:**

  $$ \sigma_G = \frac{x_{\text{event}} - \mu_{\text{null}}}{\sigma_{\text{null}}} $$

  - Terms: where $\mu_{\text{null}}$ and $\sigma_{\text{null}}$ are the mean and standard deviation of the $N$-trial null distribution. This assumes Gaussianity of the null distribution tails.

- **Empirical significance:**

  $$ p_{\text{emp}} = \frac{|\{i : x_i \geq x_{\text{event}}\}|}{N}, \quad \text{floored at}\ \frac{0.5}{N} $$

- **Empirical significance:**

  $$ \sigma_{\text{emp}} = \Phi^{-1}(1 - p_{\text{emp}}) $$

  - Terms: where $\Phi^{-1}$ is the inverse normal CDF. The empirical $\sigma$ resolves to at most $\sim \Phi^{-1}(1 - 0.5/N)$, so resolving 3$\sigma$ empirically requires $N \gtrsim 740$ trials.

- **For each independent event $i$, the Gaussian Z-score is derived from the off-source null distribution of the 15 Hz split power metric:**

  $$ Z_i = \frac{S_{15,\,i} - \mu_i}{\sigma_i} $$

- **with one-tailed p-value:**

  $$ p_i = 1 - \Phi(Z_i) = \frac{1}{\sqrt{2\pi}} \int_{Z_i}^{\infty} e^{-t^2/2}\,dt $$

- **Method A — Score stacking (equal weight):**

  $$ Z_{\text{combined}} = \frac{\displaystyle\sum_{i=1}^{N} Z_i}{\sqrt{N}} $$

- **Method B — Fisher's combined probability test. Under the null hypothesis $H_0$, the test statistic follows a chi-squared distribution with $2N$ degrees of freedom:**

  $$ S_F = -2\sum_{i=1}^{N} \ln p_i \;\sim\; \chi^2_{2N} $$

- **Method B — Fisher's combined probability test. Under the null hypothesis $H_0$, the test statistic follows a chi-squared distribution with $2N$ degrees of freedom:**

  $$ P_{\text{joint}} = P\!\left(\chi^2_{2N} \geq S_F\right), \qquad \sigma_{\text{combined}} = \Phi^{-1}\!\left(1 - P_{\text{joint}}\right) $$

- **Using the Gaussian Z-scores from the dominant channel of each event (L1 for GW190521, H1 for GW231028 — independent interferometers, independent observing runs):**

  $$ Z_1 = 4.56,\quad p_1 = 2.558 \times 10^{-6} \qquad \text{(GW190521, L1, O3a, N=100 trials)} $$

- **Using the Gaussian Z-scores from the dominant channel of each event (L1 for GW190521, H1 for GW231028 — independent interferometers, independent observing runs):**

  $$ Z_2 = 3.49,\quad p_2 = 2.415 \times 10^{-4} \qquad \text{(GW231028, H1, O4a, N=50 trials)} $$

- **Using the Gaussian Z-scores from the dominant channel of each event (L1 for GW190521, H1 for GW231028 — independent interferometers, independent observing runs):**

  $$ S_F = -2\left[\ln(2.558 \times 10^{-6}) + \ln(2.415 \times 10^{-4})\right] = 42.41 $$

- **Using the Gaussian Z-scores from the dominant channel of each event (L1 for GW190521, H1 for GW231028 — independent interferometers, independent observing runs):**

  $$ P_{\text{joint}} = P\!\left(\chi^2_4 \geq 42.41\right) = 1.37 \times 10^{-8} $$

- **Using the Gaussian Z-scores from the dominant channel of each event (L1 for GW190521, H1 for GW231028 — independent interferometers, independent observing runs):**

  $$ \boxed{\sigma_{\text{combined}} = \Phi^{-1}(1 - 1.37 \times 10^{-8}) = 5.557\sigma} $$


### Appendix K: Entanglement as Manifold Windings in the BMI Framework
_Source: manuscript/md/Appendix_K_Entanglement_Windings.md_

- **Entanglement corresponds to topological windings in $\psi$ characterized by a winding number $W$, a conserved topological charge:**

  $$ W = \frac{1}{2\pi} \oint_{\gamma} d\theta(x,t) $$

  - Terms: where $\gamma$ is a closed loop in $M$ and $\theta = \arg(\psi)$.

- **From `Chapter_6_Advanced_Forces_v3.md`, the BMI Lagrangian density $\mathcal{L}$ includes terms:**

  $$ \mathcal{L} = \bar{\psi}(i\gamma^\mu \partial_\mu - m)\psi - \frac{1}{2} Z_{\mu\nu}(x,t) F^{\mu\nu} F^{\mu\nu} + \dots $$

  - Terms: where:
    * $Z_{\mu\nu}(x,t)$ is the manifold impedance tensor encoding local geometric variations,
    * $F^{\mu\nu}$ is an effective curvature-like field strength emergent from $\psi$ windings,
    * Coupling between $\psi$ and $Z$ encodes interactions as localized geometric impedance variations.

- **Varying $\psi$ and $Z$ yields coupled Euler–Lagrange equations:**

  $$ (i\gamma^\mu \partial_\mu - m)\psi = G[Z, \psi] $$

- **Varying $\psi$ and $Z$ yields coupled Euler–Lagrange equations:**

  $$ \nabla_\alpha (Z^{\alpha\beta}(x,t) F_{\beta\mu}) = J_\mu[\psi] $$

  - Terms: where:
    * $G$ encapsulates the geometric coupling modifying $\psi$ dynamics via impedance,
    * $J_\mu$ is an effective current sourced by the winding structure of $\psi$.

- **Key BMI insight: entangled pairs correspond to linked winding numbers $W_1$ and $W_2$ on spatially separated loops $\gamma_1$, $\gamma_2$, with a global topological constraint:**

  $$ W_1 + W_2 = \text{constant} $$

- **Thus, the time evolution of the winding at site 1 depends on the global impedance and is constrained by:**

  $$ \frac{dW_1}{dt} = -\frac{dW_2}{dt} $$

- **Expressing the winding number dynamics as a functional of the manifold impedance:**

  $$ \frac{d}{dt} W_i(t) = -\int_M \frac{\delta W_j(t)}{\delta Z(x,t)} \cdot \frac{\partial Z(x,t)}{\partial t} \, d^dx \quad \text{with } i \neq j $$

  - Terms: where:
    * $\frac{\delta W_j}{\delta Z}$ is the functional sensitivity of the winding number at site $j$ to changes in global impedance,
    * $\partial_t Z$ encodes the instantaneous global geometric variation,
    * The integral expresses the nonlocal global action over the manifold,
    * Since $Z(x,t)$ adjusts globally, the changes in $W_1$ and $W_2$ are instantaneously correlated without any local signal, preserving causality in spacetime coordinates.

- **Equation from Appendix K: Entanglement as Manifold Windings in the BMI Framework**

  $$ m_i = \mathcal{F}[Z(x,t) \text{ global variations induced by universal matter-energy}] $$

  - Terms: where $\mathcal{F}$ is a functional mapping global geometric impedance configurations to local inertial parameters.

- **Let the inertial mass $m_i$ of a particle at position $x_i$ and time $t$ be given by a functional $\mathcal{M}$ mapping the global impedance field $Z$ to a scalar:**

  $$ m_i(t) = \mathcal{M}[Z](x_i, t) $$

  - Terms: where

- **Let the inertial mass $m_i$ of a particle at position $x_i$ and time $t$ be given by a functional $\mathcal{M}$ mapping the global impedance field $Z$ to a scalar:**

  $$ \mathcal{M}[Z](x_i, t) = m_0 + \int_M K_m(x_i, y; t) \cdot \Delta Z(y, t) \, d^dy $$

- *** Exponential decay kernel (with scale $\lambda$):**

  $$ K_m(x, y) = \frac{1}{N} e^{-\frac{|x-y|}{\lambda}} \cdot W(x, y) $$

  - Terms: where $W(x, y)$ encodes geometric weighting (e.g., curvature, topology) and $N$ normalizes the integral.
    * **Power-law kernel reflecting long-range influence**:

- *** Exponential decay kernel (with scale $\lambda$):**

  $$ K_m(x, y) = \frac{C}{|x-y|^\alpha} \cdot W(x, y) $$

- **Equation from Appendix K: Entanglement as Manifold Windings in the BMI Framework**

  $$ \frac{dm_i}{dt} = \int_M K_m(x_i, y; t) \cdot \frac{\partial}{\partial t} \Delta Z(y, t) \, d^dy + \int_M \frac{\partial}{\partial t} K_m(x_i, y; t) \cdot \Delta Z(y, t) \, d^dy $$

- **Modify the particle kinetic term by replacing fixed mass $m$ with the functional mass $m_i(t)$:**

  $$ \mathcal{L}_{\text{particle}} = \bar{\psi}(x_i, t)(i\gamma^\mu \partial_\mu - m_i(t))\psi(x_i, t) $$

- **Equation from Appendix K: Entanglement as Manifold Windings in the BMI Framework**

  $$ \begin{aligned} m_i(t) &= m_0 + \int_M K_m(x_i, y; t)(Z(y, t) - Z_{\text{ref}}) \, d^dy \\ \mathcal{L}_{\text{particle}} &= \bar{\psi}(x_i, t)(i\gamma^\mu \partial_\mu - m_i(t))\psi(x_i, t) \\ \frac{dm_i}{dt} &= \int_M \left[ K_m(x_i, y; t)\frac{\partial}{\partial t} \Delta Z(y, t) + \frac{\partial}{\partial t} K_m(x_i, y; t)\Delta Z(y, t) \right] d^dy \end{aligned}$$ $$


### The Bimodal Manifold Interaction (BMI) Framework
_Source: manuscript/md/BMI_Framework_Front_Matter_v3.md_

- **To bridge the gap between deterministic scripts and manuscript compilation across systems, the foundational microscopic resonance governing the spectrum is structured as a parameterized function. The raw mass relation maps to the localized manifold energy according to the following baseline expression:**

  $$ M_n = n \times \omega_0 \cdot (1 + \Delta\psi_{\text{harmonic}}) $$


### Chapter 10: Hyper-Dimensional Gauge Embedding and the Unification of Forces
_Source: manuscript/md/Chapter_10_Gauge_Embedding_v3.md_

- **To maintain invariance under a local shift $\Psi \to e^{i q \theta(x^\mu)} \Psi$, we introduce a metric perturbation vector $A_\mu$. The covariant derivative becomes:**

  $$ D_\mu \Psi = (\partial_\mu + i q A_\mu) \Psi $$

- **Replacing the Higgs: In BMI, the mass of the $W^\pm$ and $Z^0$ bosons is not derived from a scalar field, but from geometric clamping. Because these gauge bosons represent torsional twists *perpendicular* to the interface boundaries, they encounter intense resistance from the vacuum pressure of the 6D bulk. The energy required to sustain this perpendicular torsion manifests macroscopically as rest mass:**

  $$ M_W^2 \propto \int_0^\delta dy \, dz \, \left( \partial_y W \cdot \partial_y W + \partial_z W \cdot \partial_z W \right) $$


### Chapter 12: Empirical Validation of BMI Resonance and the O4b Gravitational Data
_Source: manuscript/md/Chapter_12_Empirical_Validation_of_BMI_Resonance.md_

- **The ratio of the resonant peaks $f_L / f_H \approx 1.13$ combined with this phase-lag implies a non-linear curvature interaction coefficient $K \approx 0.13$. This coefficient allows us to back-calculate the scale of the topological interface nodes:**

  $$ L_{\text{node}} \approx \frac{\hbar}{\Delta f \cdot M_{\text{Planck}}} \approx 10^{-15} \text{ m} $$


### Chapter 13: Topological Derivation of the Standard Model
_Source: manuscript/md/Chapter_13_Topological_Derivation_of_the_Standard_Model.md_

- **The Kaluza-Klein modes must satisfy a tri-cyclic boundary condition governed by the Winding Matrix ($\mathbf{R}_{top}$):**

  $$ M_n^2 = \frac{1}{\delta^2} \sum_{i=1}^{3} w_i^2 Z_{i}^2 $$

  - Terms: Where $w_i$ represents the winding number and $Z_i$ the Manifold Impedance tensor for that geometric axis.

- **The stability of these states is governed by the Inter-brane Potential $V_{gap}$. The effective Lagrangian for the mesonic system is expanded from the base manifold action:**

  $$ \mathcal{L}_{meson} = \sum_{a=1,2} \left( -\frac{1}{4}F_{\mu\nu}^a F^{\mu\nu}_a + \bar{\psi}_a(i\gamma^\mu D_\mu - m_a)\psi_a \right) + \mathcal{T}_{int}(\phi_1, \phi_2) $$

  - Terms: Where $\mathcal{T}_{int}$ is the Interaction Tension term, defined as:

- **The stability of these states is governed by the Inter-brane Potential $V_{gap}$. The effective Lagrangian for the mesonic system is expanded from the base manifold action:**

  $$ \mathcal{T}_{int} = \lambda \int_{\Sigma} \sqrt{-g} \left( \nabla_i \phi_1 \cdot \nabla^i \phi_2 \right) \Phi_{bridge} d^3x $$

- **Generating the full Cartesian product of all possible winding states yields a total theoretical state space of:**

  $$ N_{total} = (2 |w_{max}| + 1)^3 = 7^3 = 343 \text{ combinatorial permutations} $$

- **However, the bulk interface ($\Sigma$) possesses a structural breaking limit, defined by the geometric impedance threshold ($\Omega_{max}$). In the Effective Field Theory limit, the impedance of a specific winding configuration is proportional to its Euclidean norm:**

  $$ \Omega = \sqrt{w_x^2 + w_y^2 + w_z^2} $$

- **To validate the stability threshold $\Omega_{max} = 3.5$, we must move beyond static counting and analyze the dynamic stability of the interface. In the Standard Model, the CKM matrix describes the probability amplitudes of quark flavor transitions (e.g., $b \to u$, $b \to c$). The fundamental requirement of quantum mechanics is Unitarity: the sum of the probabilities of all possible decay outcomes for a state must equal exactly 1 ($100\%$).**

  $$ \sum_{j} |V_{ij}|^2 = 1 $$


### Chapter 14: The Architecture of Expansion: Topologically Directed Evolution of the Cosmic Web
_Source: manuscript/md/Chapter_14_The_Architecture_of_Expansion.md_

- **To calculate the Hausdorff dimension ($D_H$) of these creases, we examine the scaling behavior of the energy density $\rho(L)$ relative to the compactification scale ($\delta \approx 10^{-15} \text{ m}$):**

  $$ D_H = 2 + \frac{\ln(\text{Impedance Coupling})}{\ln(L_{node}/\delta)} $$

- **By applying the boundary conditions of the $T^3$ nested torus nodes to the brane expansion, our Lagrangian yields an emergent attractor value:**

  $$ D_H \approx 1.738 $$


### Chapter 1: Foundations of Bimodal Manifold Resonance
_Source: manuscript/md/Chapter_1_Foundations_v3.md_

- **When energy is introduced into this active medium at the microscopic quantum scale, it undergoes a localized geometric transition once it passes specific *Manifestation Thresholds*. The primary mechanics of this microscopic architecture are governed by the fundamental wave equation of the manifold, where the mass $M$ of any given state is a direct function of its integer harmonic index $n$ and the global base frequency $\omega_0$.**

  $$ M(n) = n \cdot \omega_0 \cdot \Lambda_{\text{geom}} $$

  - Terms: Where:
    * $n \in \mathbb{Z}^+$ represents the principal harmonic mode of the localized manifold oscillation.
    * $\omega_0$ is the fundamental invariant base frequency of the background bimodal field.
    * $\Lambda_{\text{geom}}$ is the topological correction factor dictated by the spatial orientation and boundary constraints of the nested torus system.

- **For the nucleon spectrum, the base topological mode split is determined by the alignment or anti-alignment of this geometric phase shift relative to the primary manifold rotation:**

  $$ M_{\text{nucleon}}(n, \sigma) = n \cdot \omega_0 \cdot \left(1 + \sigma \frac{\gamma}{2\pi}\right) $$

  - Terms: Where:
    * $\sigma \in \{-1, 0, 1\}$ dictates the geometric polarity or topological alignment index of the nested manifolds.
    * $\gamma$ represents the accumulated Berry phase invariant under a $2\pi$ rotation of the internal membrane.


### Chapter 2: The Linear Resonance Spectrum and Harmonic Particle Mapping
_Source: manuscript/md/Chapter_2_Resonance_Spectrum_v3.md_

- **Crucially, the mass of these states is not constant; it is subject to the Thermodynamic Scaling discovered in our macroscopic analysis. The effective rest mass $M_n$ at any cosmological epoch is a function of the harmonic mode, the base frequency, and the local metric equilibrium ($\Xi$):**

  $$ M_n(t) = n \cdot \omega_0 \cdot \left(1 + \Delta\psi(n)\right) \cdot f(\Xi(t)) $$

  - Terms: Where $f(\Xi(t))$ represents the coupling of the particle's localized geometry to the total Metric Equilibrium ($\Xi = \tau + V_{gap}$) of the universe at time $t$. This links the mass of the particle directly to the evolution of the manifold coalescence.


### Chapter 3: The Topological Foundations of Spin and Charge
_Source: manuscript/md/Chapter_3_Topological_Properties_v3.md_

- **Fermionic behavior (half-integer spin, $s = \frac{1}{2}$) emerges naturally when a full spatial rotation ($2\pi$ radians) of the outer manifold shell maps to exactly a half-rotation ($\pi$ radians) of the nested inner core. This creates a topological configuration where the system accumulates a non-integrable Geometric Berry Phase Shift ($\gamma$).**

  $$ \Psi(\theta + 2\pi) = \Psi(\theta) \cdot e^{i \gamma} = -\Psi(\theta) $$

  - Terms: Where:
    * $\theta$ represents the spatial angular coordinate of the outer manifold rotation.
    * $\gamma = \pi$ is the accumulated topological phase shift under a single $2\pi$ outer cycle.

- **When an integer harmonic mode phase-locks, the nested tori exhibit a localized "twist" or chirality. This creates a geometric gradient—a differential tension between the internal core and the external environment. We define the charge $Q$ of a stabilized mode as the closed surface integral of this geometric polarity vector ($\mathbf{P}_{\text{geom}}$):**

  $$ Q = \oint_{T^3} \mathbf{P}_{\text{geom}} \cdot d\mathbf{A} = \pm e $$


### Chapter 4: Vacuum Dynamics, State Transitions, and Matter-Antimatter Asymmetry
_Source: manuscript/md/Chapter_4_Vacuum_Dynamics_v3.md_

- **When no localized topological twists are present, the overlapping branes ($\sigma_A$ and $\sigma_B$) oscillate in a state of global Metric Equilibrium ($\Xi$). Matter is not something placed *into* the vacuum; rather, matter represents high-tension, phase-locked deformations *of* the vacuum itself. Propagation is not a particle traversing a background, but the transmission of localized manifold tension. The photon ($\gamma$) is the transient relaxation of this tension, a kinetic wave packet representing the minimum energy unit of the manifold's elastic transition:**

  $$ \Psi_{\text{photon}}(\mathbf{x}, t) = \mathbf{A}_{\text{vac}} \cdot e^{i(\mathbf{k}\cdot\mathbf{x} - \omega t)} $$

  - Terms: Where $\mathbf{A}_{\text{vac}}$ is constrained by the current global Bridge Stress ($\tau$) of the cosmological epoch. As the universe evolves toward Asymptotic Flatness, the "baseline" energy of the vacuum continuum itself slowly recalibrates as the manifolds finalize their coalescence.

- **When a matter harmonic and an antimatter harmonic intersect, the annihilation event is the structural phase-cancellation of localized manifold tension. The potential energy bound within the geometric twists—essentially "frozen" Bridge Stress—is released as the local manifold region snaps back to the global equilibrium state ($\Xi$). This transition maps the bound-state energy directly into radiative vacuum modes (photons):**

  $$ \psi_+(n, \mathbf{P}_{\text{geom}}) + \psi_-(n, -\mathbf{P}_{\text{geom}}) \longrightarrow \sum \Psi_{\text{photon}} $$

- **During the cosmic initiation (the "Cradle" epoch where Bridge Stress $\tau$ was at its maximum), the background field underwent rapid cooling. Hysteresis dictates that the energy path required to create a positive topological twist is not symmetric to the path required to create an inverse twist. Because of an intrinsic chiral bias—a structural non-zero torsion built into the global manifold metric during the impact—the energy activation threshold to stabilize a matter configuration was subtly lower than that required for antimatter:**

  $$ \Delta E_{\text{matter}} = E_0 \cdot (1 - \tau_{\text{global}}) < \Delta E_{\text{antimatter}} = E_0 \cdot (1 + \tau_{\text{global}}) $$


### Chapter 5: The Human-AI Collaborative Methodology and Validation Pipeline
_Source: manuscript/md/Chapter_5_Methodology_v3.md_

- **Approved equations are immediately translated into deterministic source code (Python). These scripts execute automated lab environments, such as the "Cradle Test" (simulating CMB thermal amplitude scaling). The model is only verified if the code outputs match experimental physical constants within strict error tolerances:**

  $$ \delta = \left| \frac{M_{\text{experimental}} - M_{\text{derived}}}{\text{SD}_{\text{experimental}}} \right| \le \epsilon $$


### Chapter 6: Advanced Topological Interacting Forces and Impedance Matrices
_Source: manuscript/md/Chapter_6_Advanced_Forces_v3.md_

- **When separate nested torus systems occupy adjacent regions of the manifold, their internal phase rotations induce mutual drag. This is quantified as a localized Manifold Impedance Matrix ($\mathbf{Z}_{ij}$). The interaction is governed by the geometric overlap integral ($\mathcal{I}_{\text{overlap}}$) of their wave topologies ($\psi_i$ and $\psi_j$):**

  $$ \mathbf{V}_{ij}(t) = \mathbf{Z}_{ij}(\Xi) \cdot \mathcal{I}_{\text{overlap}} $$

  - Terms: Where:
    * $\mathbf{Z}_{ij}(\Xi)$ is the complex impedance tensor, which scales dynamically with the local Metric Equilibrium ($\Xi$).
    * $\mathcal{I}_{\text{overlap}} = \int_{V} \psi_i \otimes \psi_j \, dV$ represents the structural interaction of the nested tori.


### Chapter 7: Cosmological Implications, Higher-Dimensional Boundaries, and Gravitational Equivalence
_Source: manuscript/md/Chapter_7_Cosmological_Boundaries_v3.md_

- **The local metric tensor $g_{\mu\nu}$ is an emergent statistical average of the combined Bridge Stress and Inter-brane Potential. We derive the local curvature as a function of the global equilibrium state $\Xi(t)$:**

  $$ g_{\mu\nu}(t) = \eta_{\mu\nu} + \mathbf{\Xi}_{\mu\nu}\left(\tau(t) + V_{gap}(t)\right) $$

  - Terms: Where:
    * $\eta_{\mu\nu}$ is the flat Minkowskian baseline metric of the fully relaxed manifold.
    * $\mathbf{\Xi}_{\mu\nu}$ is the global strain tensor representing the elastic deformation induced by the interacting branes.

- **As energy density varies across cosmic limits—such as early inflationary phases—the active medium shifts winding vectors into these higher spatial constraints. The mapping of a wave packet into these higher dimensions is governed by the boundary constraint matrix $\mathbf{B}_{\text{compact}}$:**

  $$ \oint_{T^n} \mathbf{\Xi}_{\mu\nu} \cdot d\mathbf{V}_n \longrightarrow \mathbf{B}_{\text{compact}}(n) $$


### Chapter 8: Experimental Predictions, Spectral Anomaly Cross-Validation, and Predictive Limits
_Source: manuscript/md/Chapter_8_Experimental_Predictions_v3.md_

- **The BMI analysis lab code maps these deviations across high-energy environments, yielding precise, un-renormalized mass variations. The predicted mass shift for a mode $n$ is scaled by the current cosmological epoch:**

  $$ \delta M_n(\mathbf{E}, \mathbf{B}, t) = n \cdot \omega_0 \cdot \left[ \mathbf{\Lambda}_{\text{tensor}} \cdot f(\Xi(t)) \cdot \left(\mathbf{E}^2 + c^2\mathbf{B}^2\right) \right] $$

  - Terms: Where:
    * $\delta M_n$ is the predicted, localized rest-mass shift.
    * $\mathbf{\Lambda}_{\text{tensor}}$ is the structural deformation coefficient matrix.
    * $f(\Xi(t))$ couples the shift to the prevailing **Bridge Stress ($\tau$)** and **Inter-brane Potential ($V_{gap}$)**.


### Chapter 9: The Hyperspatial Resolution of the Mott Problem: Topological Pinning and Trajectory Localization
_Source: manuscript/md/Chapter_9_Mott_Resolution_v3.md_

- **We define the cosmos as a 6D bulk manifold where our 4D spacetime is embedded within a Thick Brane Interface of finite thickness $\delta$. Let the electron field before interaction be modeled as a complex scalar field $\Psi(x^\mu, y, z)$. Upon emission, the field propagates as a spherically symmetric packet:**

  $$ \Psi_{\text{free}}(r, t, y, z) = \frac{\mathcal{A}}{r} e^{i(kr - \omega t)} \chi_0(y, z) $$

- **The interaction between the field and a target atom (e.g., a nucleus in a bubble chamber) is governed by the Screening Gate Function $g_{\text{eff}}(R)$, a dynamic regulator of the interface permeability:**

  $$ g_{\text{eff}}(R) = \frac{1}{1 + e^{-\alpha(R - R_{\text{crit}})}} $$

  - Terms: Where $R$ is the local Ricci scalar induced by the target.
    * **In Vacuo ($R \to 0$):** $g_{\text{eff}} \to 0$, insulating the field from localized decay.
    * **Interaction ($R \gg R_{\text{crit}}$):** $g_{\text{eff}} \to 1$, triggering a sharp phase transition.

- **We define the energy functional of the interface system as:**

  $$ \mathcal{E}[\phi] = \int d^3x \left[ \frac{1}{2} |\nabla \phi|^2 + V_{\text{eff}}(\phi) - \kappa \, \delta^3(\vec{x} - \vec{x}_1) |\phi|^2 \right] $$

- **The introduction of the delta-function potential ($\kappa$) breaks the spatial homogeneity. The uniform spherical solution $\phi(r)$ ceases to be the minimum energy state. The system minimizes energy by collapsing into a localized exponential screening profile:**

  $$ \phi_{\text{bound}}(\vec{x}) = \mathcal{C} \, e^{-\lambda |\vec{x} - \vec{x}_1|} $$


### Session Notes — 2026-10-14
_Source: session_notes_2026-10-14.md_

- **Using the Bimodal Manifold Interaction (BMI) harmonic mass formula ($M_n = n \cdot \omega_0$), where $\omega_0 = 0.51099895000 \text{ MeV/c}^2$ represents the baseline electron leptonic node, the hadron spectrum maps to discrete topological harmonic indices ($n$):**

  $$ \begin{array}{lcccc} \hline \textbf{Hadron} & \textbf{Harmonic Index } (n) & \textbf{BMI Calculated } (\text{MeV}) & \textbf{Experimental } (\text{MeV}) & \textbf{Residual } (\text{MeV}) \\ \hline \text{Pion } (\pi^0) & 264.1425 & 134.97654 & 134.97680 & -2.59850 \times 10^{-4} \\ \text{Pion } (\pi^+) & 273.1332 & 139.57078 & 139.57040 & +3.78410 \times 10^{-4} \\ \text{Proton } (p) & 1836.1527 & 938.27209 & 938.27208 & +6.40970 \times 10^{-6} \\ \text{Neutron } (n) & 1838.6837 & 939.56542 & 939.56542 & -3.57843 \times 10^{-7} \\ \text{Kaon } (K^0) & 973.8820 & 497.65268 & 497.61100 & +4.16794 \times 10^{-2} \\ \text{Eta } (\eta) & 1072.1810 & 547.88337 & 547.86200 & +2.13652 \times 10^{-2} \\ \hline \end{array} $$

- **Using the Bimodal Manifold Interaction (BMI) harmonic mass formula ($M_n = n \cdot \omega_0$), where $\omega_0 = 0.51099895000 \text{ MeV/c}^2$ represents the baseline electron leptonic node, the hadron spectrum maps to discrete topological harmonic indices ($n$):**

  $$ ### Summary The calculations demonstrate that hadron rest masses are represented as topological harmonic multiples of the fundamental vacuum frequency $\omega_0$. Nucleon state indices ($n \approx 1836-1838$) reproduce experimental masses with sub-electronvolt precision. <<<DONE>>> --- ## 16:24 — File System (R1: Speculation & Horizons) File operation results: - RUN `CALC .scratch/calc_1792009372540.py` → exit 0 (0.1s) stdout: ```text Hadron | Index (n) | BMI Mass (MeV) | Exp Mass (MeV) | Diff (MeV) -------------------------------------------------------------------------------- Pion (pi0) | 264.1425 | 134.97654 | 134.97680 | -2.59850e-04 Pion (pi+) | 273.1332 | 139.57078 | 139.57040 | 3.78410e-04 Proton (p) | 1836.1527 | 938.27209 | 938.27208 | 6.40970e-06 Neutron (n) | 1838.6837 | 939.56542 | 939.56542 | -3.57843e-07 Kaon (K0) | 973.8820 | 497.65268 | 497.61100 | 4.16794e-02 Eta (eta) | 1072.1810 | 547.88337 | 547.86200 | 2.13652e-02 ``` --- $$


### 01 — The Action
_Source: v2/01_action.md_

- **an effective 5D space with**

  $$ M_5^3 \equiv \pi \ell_z\, M_6^4 $$

- **Equation from 01 — The Action**

  $$ S = S_{\text{bulk}} + S_{\Sigma_1} + S_{\Sigma_2} + S_{\text{GHY}} $$

- **Equation from 01 — The Action**

  $$ S_{\text{bulk}} = \int_{\mathcal M_6} d^6X \sqrt{-G}\, \left[ \frac{M_6^4}{2}\, R_6 \;-\; \Lambda_6 \;-\; \frac12\, G^{AB}\partial_A\Phi\,\partial_B\Phi \;-\; V(\Phi) \right] $$

- **Equation from 01 — The Action**

  $$ S_{\Sigma_i} = \int_{\Sigma_i} d^5\xi \sqrt{-\gamma_i}\, \left[ -\sigma_i \;+\; \mathcal L^{(i)}_{\text{matter}}(\gamma_i, \psi_i) \right], \qquad i = 1, 2 $$

- **Equation from 01 — The Action**

  $$ S_{\text{GHY}} = M_6^4 \sum_{i} \int_{\Sigma_i} d^5\xi \sqrt{-\gamma_i}\; [K_i] $$

- **Equation from 01 — The Action**

  $$ V(\Phi) = V_0\, \exp\!\left(-\,c\,\frac{\Phi}{M_6^2}\right), \qquad V_0 > 0,\; c > 0 . $$

- **With $\Phi$ constant and no brane matter, the bulk equations admit the RS solution**

  $$ ds^2 = e^{-2y/\ell}\left( \eta_{\mu\nu} dx^\mu dx^\nu + dz^2 \right) + dy^2, \qquad \ell^{-2} = -\frac{\Lambda_6}{10\, M_6^4} $$

- **provided the tensions satisfy the RS tuning**

  $$ \sigma_1 = -\sigma_2 = \frac{8\, M_6^4}{\ell} . $$

- **v2 assumes it exactly for $\sigma_1$ and treats the *detuning* of $\sigma_2$,**

  $$ \delta\sigma_2 \equiv \sigma_2 + \sigma_1 , $$

- **result with the $D=6$ measure):**

  $$ M_{\text{Pl}}^2 = \frac{M_5^3\,\ell}{3}\,\bigl(1 - e^{-3\phi/\ell}\bigr). $$

- **For $\phi \gg \ell$ this is $\phi$-independent up to $e^{-3\phi/\ell}$, so**

  $$ \frac{\dot G}{G} = -\frac{3\,\dot\phi}{\ell}\,\frac{e^{-3\phi/\ell}}{1-e^{-3\phi/\ell}} \;\approx\; -\frac{3\dot\phi}{\ell}\, e^{-3\phi/\ell}. $$

- **in the 4D Jordan frame with $g_{\mu\nu}$ the metric on $\Sigma_1$:**

  $$ S_{\text{eff}} \supset \int d^4x \sqrt{-g}\; \frac{M_5^3\,\ell}{3} \left[ \frac{1-\Omega^3}{2}\,R_4 \;-\; 3\,(\partial\Omega)^2 \right] \;-\; \int d^4x \sqrt{-g}\; V_{\text{eff}}(\phi) \quad \textbf{[verify factor 3]} $$

- **with**

  $$ V_{\text{eff}}(\phi) = \Omega^4\,\delta\sigma_2 \;+\; \int_0^{\phi} dy\; e^{-5y/\ell}\, V(\Phi(y)) \quad \textbf{[verify; requires the } \Phi(y) \textbf{ profile]}. $$


### BMI v2 — Action and Parameter Budget (skeleton)
_Source: v2/01_action_skeleton_superseded.md_

- **Equation from BMI v2 — Action and Parameter Budget (skeleton)**

  $$ S_{\text{bulk}} = \int d^6X \sqrt{-G}\left[\frac{M_6^4}{2}R_6 - \frac12 (\partial\Phi)^2 - V(\Phi)\right] $$

- **Equation from BMI v2 — Action and Parameter Budget (skeleton)**

  $$ S_{\Sigma_i} = \int_{\Sigma_i} d^4x \sqrt{-g_i}\left[-\sigma_i(\Phi) + \mathcal L^{(i)}_{\text{matter}}(g_i, \psi_i)\right] $$

  - Terms: where:

- **Junction conditions (Israel 1966) at each brane fix the extrinsic curvature jump in terms of \(\sigma_i\) and the brane stress-energy. In 6D codimension-1 they read \([K_{\mu\nu}] - g_{\mu\nu}[K] = -M_6^{-4}\,S^{(i)}_{\mu\nu}\). This is what Appendix F should have been: the Einstein equation on \(\Sigma_1\) comes out with the standard correction terms (Shiromizu–Maeda–Sasaki 2000):**

  $$ G_{\mu\nu} = 8\pi G_N T_{\mu\nu} + \frac{1}{M_6^8}\pi_{\mu\nu}(T^2) - E_{\mu\nu} + (\text{radion terms}) $$

- **With two branes, \(G_N\) on \(\Sigma_1\) depends on \(\phi\). In RS-type warped setups \(G_N^{-1} \propto M_6^4 \,\ell\,(1 - e^{-2\phi/\ell})\); in flat bulk \(G_N^{-1} \propto M_6^4\,\phi\). Either way an inspiral means \(\dot\phi \neq 0 \Rightarrow \dot G/G \neq 0\).**

  $$ \frac{\dot G}{G} \approx -\frac{\dot\phi}{\phi} \quad (\text{flat bulk}) $$

- **The radion kinetic + potential energy on \(\Sigma_1\) behaves as quintessence:**

  $$ w_\phi(z) = \frac{\tfrac12\dot\phi^2 - V_{\text{eff}}(\phi)}{\tfrac12\dot\phi^2 + V_{\text{eff}}(\phi)} $$

- **[BMI] — the one place the collision picture is non-generic. After a brane collision, each brane reheats to a temperature set by its own tension and the kinetic energy deposited. For asymmetric tensions or an oblique impact, \(T_2/T_1 \neq 1\).**

  $$ \frac{T_2}{T_1} = \left(\frac{\epsilon_2}{\epsilon_1}\right)^{1/4}\quad\text{where } \epsilon_i = \text{energy deposited per unit 3-volume on } \Sigma_i $$


### 02 — The Effective 4D Theory
_Source: v2/02_effective_4d.md_

- **directions,**

  $$ ds^2 = e^{-2y/\ell}\left(\eta_{\mu\nu}dx^\mu dx^\nu + dz^2\right) + dy^2 , $$

- **Bulk equations $G_{AB} = -\Lambda_6\, G_{AB}/M_6^4$ with constant $\Phi$ and $V_0 \to 0$:**

  $$ ds^2 = e^{-2y/\ell}\left(\eta_{\mu\nu}dx^\mu dx^\nu + dz^2\right) + dy^2 , \qquad \ell^{-2} = -\frac{\Lambda_6}{10\,M_6^4} . $$

- **`01_action.md` §2):**

  $$ 2M_6^4\left(K_{ab} - \gamma_{ab}K\right) = -S_{ab}, \qquad S_{ab} = -\sigma_i\gamma_{ab} + T^{(i)}_{ab}, $$

- **gives**

  $$ \sigma_1 = \frac{8M_6^4}{\ell}, \qquad \sigma_2 = -\sigma_1 . $$

- **and $R_6 \supset e^{2y/\ell}R_4$, so**

  $$ \frac{M_6^4}{2}\int d^6X\sqrt{-G}\,R_6 \;\supset\; \frac{M_6^4}{2}\,(\pi\ell_z)\int_0^{\phi}dy\,e^{-3y/\ell}\int d^4x\sqrt{-g}\,R_4 = \frac{M_{\text{Pl}}^2(\phi)}{2}\int d^4x\sqrt{-g}\,R_4 , $$

- **and $R_6 \supset e^{2y/\ell}R_4$, so**

  $$ \boxed{\;M_{\text{Pl}}^2(\phi) = \frac{M_5^3\,\ell}{3}\left(1 - e^{-3\phi/\ell}\right), \qquad 8\pi G_N = M_{\text{Pl}}^{-2}\;} $$

- **Time variation.**

  $$ \frac{\dot G}{G} = -\frac{3\dot\phi}{\ell}\,\frac{e^{-3\phi/\ell}}{1 - e^{-3\phi/\ell}} . $$

- **of $\Sigma_1$:**

  $$ {}^{(5)}G_{ab} = -\Lambda_{\text{brane}}\,\gamma_{ab} + 8\pi G_5\,T_{ab} + \frac{1}{M_6^8}\,\pi_{ab} - E_{ab}, $$

  - Terms: where
    - $\Lambda_{\text{brane}} = 0$ by §1 (it is the combination of $\Lambda_6$ and $\sigma_1^2$ that

- **Reducing on the circle at energies below $1/\ell_z$ (zero mode only) gives the 4D equation**

  $$ \boxed{\;G_{\mu\nu} = 8\pi G_N(\phi)\,T_{\mu\nu} + \frac{8\pi G_N}{\sigma_1^{(5)}}\,\hat\pi_{\mu\nu} - E_{\mu\nu} + \Theta_{\mu\nu}[\phi]\;} $$

- **Adelberger et al. 2007, treat as approximate). Then**

  $$ \sigma_1^{(5)} \gtrsim 24\,(2.4\times10^{18}\,\mathrm{GeV})^2\,(5\times10^{10}\,\mathrm{GeV}^{-1})^{-2} \approx 5\times10^{16}\,\mathrm{GeV}^4 \approx (1.5\times10^{4}\,\mathrm{GeV})^4 . $$

- **the Jordan-frame effective action is**

  $$ S_{\text{eff}} = \int d^4x\sqrt{-g}\left[\frac{M_5^3\ell}{6}\,\Psi\,R_4 - \frac{M_5^3\ell}{6}\,\frac{\omega(\Psi)}{\Psi}(\partial\Psi)^2 - V_{\text{eff}}(\phi)\right] + S_{\text{SM}}[g,\psi_1] + S_{\text{mirror}}[\Omega^2 g,\psi_2] . $$

- **Tortora 2003). With the 6D formula:**

  $$ \boxed{\;\phi_0/\ell \;\gtrsim\; 3.4,\qquad \Omega_0 \lesssim 0.032\;} $$

- **Effective potential. The two contributions:**

  $$ V_{\text{eff}}(\phi) = \Omega^4\,\delta\sigma_2^{(5)} \;+\; \pi\ell_z\int_0^\phi dy\;e^{-5y/\ell}\,V(\Phi(y)) \quad\textbf{[verify: requires } \Phi(y)\textbf{]} $$

- **means: same dimensionless couplings, all masses multiplied by $\Omega(\phi)$:**

  $$ m_e^{(2)} = \Omega\,m_e,\qquad m_p^{(2)} = \Omega\,m_p,\qquad \Lambda_{\text{QCD}}^{(2)} = \Omega\,\Lambda_{\text{QCD}} . $$


### BMI v2 — 02b. Where fields live: the localization equation
_Source: v2/02b_localization.md_

- **Background, $A = y/\ell$, $d = 5$ warped directions $x^a = (x^\mu, z)$:**

  $$ ds^2 = e^{-2A}\,\eta_{ab}\,dx^a dx^b + dy^2 . $$

- **term and are in the test file)**

  $$ e^{dA}\,\partial_y\!\left(e^{-dA}\,\partial_y f\right) + e^{2A}\!\left(m_4^2 - \frac{n^2}{\ell_z^2}\right) f - M^2 f = 0 . $$


### 03 — Background: the low-energy 4D theory in closed form and its FRW solution
_Source: v2/03_background.md_

- **(`tests/check_radion.py`, which also reproduces the 5D Garriga–Tanaka result as a control):**

  $$ S_{\text{rad}} = \frac{M_5^3\ell}{6}\int d^4x\sqrt{-g}\left[\Psi R_4 - \frac{\omega(\Psi)}{\Psi}(\partial\Psi)^2\right], \qquad \Psi = 1-\Omega^3,\qquad \boxed{\;\omega(\Psi) = \frac{4\Psi}{3(1-\Psi)} = \frac43\left(e^{3\phi/\ell}-1\right)\;} $$

- **Cassini. $\omega > 4\times10^4$ (Bertotti, Iess & Tortora 2003) gives**

  $$ \phi_0/\ell > \tfrac13\ln\!\left(1+\tfrac34\omega_C\right) = 3.44, \qquad \Omega_0 < 0.032 . $$

- **Radion kinetic term and canonical field. Writing $\tfrac12 K(\phi)(\partial\phi)^2$,**

  $$ K(\phi) = \frac{4M_5^3}{\ell}\,e^{-3\phi/\ell} = \frac{12M_{\text{Pl}}^2}{\ell^2}\,\Omega^3, \qquad \chi \equiv -\frac{4}{\sqrt3}\,M_{\text{Pl}}\,\Omega^{3/2} $$

- **Radion potential. From `02_effective_4d.md` §4 with the $\Phi$ term moved to §2 below,**

  $$ V_{\text{rad}}(\phi) = \delta\sigma_2^{(5)}\,\Omega^4 = \delta\sigma_2^{(5)}\left(\frac{\sqrt3\,\chi}{4M_{\text{Pl}}}\right)^{8/3}, \qquad \delta\sigma_2^{(5)} \equiv \pi\ell_z(\sigma_2+\sigma_1). $$

- **Reducing on the slice (`tests/check_radion.py`):**

  $$ S_\Phi = \int d^4x\sqrt{-g}\left[-\frac{M_{\text{Pl}}^2(\phi)}{2M_6^4}(\partial\Phi)^2 - \frac{\pi\ell_z\ell}{5}\left(1-\Omega^5\right)V_0\,e^{-c\Phi/M_6^2}\right]. $$

- **and the canonical field is $\Phi_4 = (M_{\text{Pl}}/M_6^2)\,\Phi$. Then**

  $$ \boxed{\;V(\Phi_4) = V_*\,e^{-c\,\Phi_4/M_{\text{Pl}}},\qquad V_* = \frac{\pi\ell_z\ell}{5}\,V_0\;} $$

- **$\dot\chi \simeq -V'/(3H_0)$ (matter era, $H$ of order $H_0$) in the matter era, `tests/background_frw.py` gives**

  $$ \Delta\ln\Omega = \frac{f_{\text{rad}}}{3\Omega^3}, \qquad f_{\text{rad}} \equiv \frac{V_{\text{rad}}}{3M_{\text{Pl}}^2H^2}, $$

- **(per Hubble time), so the bound is**

  $$ f_{\text{rad}}(t_0) \lesssim 0.15\,\Omega_0^3 < 5\times10^{-6}, \qquad \left|\frac{\dot G}{G}\right| = \frac{3\Omega^3}{1-\Omega^3}\,\left|\frac{\dot\phi}{\ell}\right| \lesssim 3\times10^{-16}\ \mathrm{yr}^{-1}. $$


### 04 — The impact: what the collision fixes, what it cannot, and what dies
_Source: v2/04_impact.md_

- **ratio $r_b$ at the moment the moduli approximation becomes valid:**

  $$ \frac{d\chi}{d\ln a} = \sqrt6\,M_{Pl}\left(\frac{\rho_{\chi}}{\rho_{\text{tot}}}\right)^{1/2} \quad\Rightarrow\quad \Delta\chi = \sqrt6\,M_{Pl}\,\mathrm{asinh}\sqrt{r_b} , $$

- **collision edge $\chi = -\tfrac{4}{\sqrt3}M_{Pl}$ and freezing at $\chi_0 = -\tfrac{4}{\sqrt3}M_{Pl}\Omega_0^{3/2}$:**

  $$ \Omega_0 = \left[1 - \frac{\sqrt6}{4/\sqrt3}\,\mathrm{asinh}\sqrt{r_b}\right]^{2/3} = \left[1 - \tfrac{3}{2\sqrt2}\,\mathrm{asinh}\sqrt{r_b}\right]^{2/3}. $$

- **(`tests/impact.py` §2):**

  $$ \Delta N_{\text{eff}}(x{=}1) = 3.4\text{–}6.1\ \ \mathrm{(BBN)},\qquad \Delta N_{\text{eff}}(x{=}1) \approx 7.5\ \ \mathrm{(CMB)} . $$

- **bounds on $x$ from $\Delta N_{\text{eff}} < 0.3$:**

  $$ x < 0.47\text{–}0.49 \;\;\mathrm{(BBN,\ depends\ on\ }\Omega_0\mathrm{)},\qquad x < 0.45 \;\;\mathrm{(CMB,\ independent\ of\ }\Omega_0\mathrm{)}. $$

- **asymmetries $\eta_i$ (baryon-to-photon ratios) of each sector:**

  $$ \frac{\Omega_{DM}}{\Omega_b} = \Omega_0\,\frac{n_2}{n_1} = \Omega_0\left(\frac{T_2}{T_1}\right)^3_{\!\mathrm{today}}\frac{\eta_2}{\eta_1} \approx 0.10\,\Omega_0\,\frac{\eta_2}{\eta_1}\quad(x\ \mathrm{at\ its\ bound}), $$

  - Terms: where the factor $0.10$ is $x^3$ corrected for the different entropy histories

- **(`tests/impact.py` §2). The observed $\Omega_{DM}/\Omega_b = 5.3$ then requires**

  $$ \frac{\eta_2}{\eta_1} \gtrsim 1600\;(\Omega_0 = 0.032),\qquad 4500\;(\Omega_0 = 0.01),\qquad 1.5\times10^4\;(\Omega_0 = 0.003). $$

- **coupled system (their eqs. 20–25; $D = 5$, RS2, $\mathbb Z_2$-symmetric bulk):**

  $$ \dot\rho + 4H\rho = -\frac{\alpha}{12}\kappa_5^2\rho^2,\qquad \alpha = \frac{212625}{64\pi^7}\,\zeta(9/2)\zeta(7/2)\,\frac{\hat g}{g_*^2} \approx 0.019 \;\;(\mathrm{full\ SM:}\ \hat g = 166.21,\ g_* = 106.75), $$

- **($\rho \gtrsim \lambda$, $\lambda$ = brane tension) radiation era:**

  $$ \epsilon_W \equiv \frac{\rho_E}{\rho_{\text{rad}}} \to \frac{\alpha}{4} \approx 4.8\times10^{-3}, $$

- **low-energy regime gives (this file)**

  $$ \epsilon_W = \frac{\alpha}{2\sqrt2}\left(\frac{T_{RH}}{T_t}\right)^2 ,\qquad T_t = \left(\frac{30\,\lambda}{\pi^2 g_*}\right)^{1/4},\quad \lambda = \sigma_1^{(5)} = \frac{8M_5^3}{\ell} = \frac{24M_{Pl}^2}{\ell^2} , $$


### 04c — The approach to $\Omega = 1$ without the moduli approximation
_Source: v2/04c_approach.md_

- **Bulk (units $\ell = 1$, $\kappa^2 = 1/M_6^4 = 1$), $n$ isotropic spatial directions on the brane:**

  $$ ds^2 = -f\,dt^2 + \frac{dr^2}{f} + \frac{r^2}{\ell^2}\,d\vec x^{\,2}, \qquad f(r) = \frac{r^2}{\ell^2} - \frac{\mu}{r^{\,n-1}} . $$

- **direct Israel computation)**

  $$ \sqrt{\frac{f}{R^2} + H^2} = \frac{\sigma_1 + s\,\rho}{2n}, \qquad s = +1\ (\Sigma_1),\quad s = -1\ (\Sigma_2), \qquad \sigma_1 = \frac{2n}{\kappa^2\ell} , $$

- **recovered, not assumed. Squaring:**

  $$ H_1^2 = \frac{\rho_1}{n}\Big(1 + \frac{\rho_1}{2\sigma_1}\Big) + \frac{\mu}{R_1^{\,n+1}}, \qquad H_2^2 = -\frac{\rho_2}{n}\Big(1 - \frac{\rho_2}{2\sigma_1}\Big) + \frac{\mu}{R_2^{\,n+1}} . $$

- **Collision data. At coincidence $R_1 = R_2 = 1$ define**

  $$ f \equiv \frac{A_2}{A_1} = \frac{\rho_2}{\rho_1}\Big|_{\Omega=1}, \qquad \epsilon \equiv \frac{n\mu}{A_1} = \frac{\rho_E}{\rho_1}\Big|_{\Omega=1}, \qquad h \equiv \frac{\rho_1}{\sigma_1}\Big|_{\Omega=1} . $$

- **respectively,**

  $$ R_i^{(n-1)/2} \propto t \quad\Rightarrow\quad \boxed{\;\Omega_\infty^{\,n-1} = \lim_{t\to\infty}\Big(\frac{R_2}{R_1}\Big)^{n-1} = \frac{\epsilon - f}{1+\epsilon}\;} $$

- **$H_2^2 \ge 0$ at low energy requires $\mu/R_2^{n+1} \ge \rho_2/n$. Written on $\Sigma_1$,**

  $$ \rho_E \;\ge\; \Omega^{n+1}\rho_2 \quad\Leftrightarrow\quad \epsilon \ge f : $$


### 04d — Stabilizing the circle
_Source: v2/04d_circle.md_

- **(Appelquist–Chodos form, orbifold halving the modes; O(1) coefficient [verify])**

  $$ V_z(\ell_z) = +62\,\frac{3\zeta(5)}{64\pi^6}\,\frac{1}{\ell_z^4} \equiv \frac{C_z}{\ell_z^4}, $$

- **linear in $\ell_z$. Together with §1,**

  $$ V(\ell_z) = \frac{C_z}{\ell_z^4} + \frac{\pi\ell V_0}{5}\,e^{-c\Phi_4/M_{Pl}}\,\ell_z $$

- **$\pi\ell_z\delta_1$: linear in $\ell_z$, and negative if $\delta_1 < 0$. Then**

  $$ V(\ell_z) = \frac{C_z}{\ell_z^4} + \pi\delta_1\,\ell_z, \qquad \bar\ell_z^5 = \frac{4C_z}{\pi\lvert\delta_1\rvert}, \qquad V(\bar\ell_z) = -\frac{3C_z}{\bar\ell_z^4} . $$

- **(b) The modulus mass and a two-sided window. With $\chi = M_{Pl}\ln\ell_z$,**

  $$ m_\chi^2 = \frac{\bar\ell_z^2 V''(\bar\ell_z)}{M_{Pl}^2} = \frac{20\,C_z}{\bar\ell_z^4 M_{Pl}^2} \quad\Rightarrow\quad m_\chi = 1.0\times10^{-2}\ \mathrm{eV}\left(\frac{\bar\ell_z^{-1}}{10\ \mathrm{TeV}}\right)^{2} . $$

- **$M_6 \approx 27$ PeV for $\ell = 10\,\mu$m [verify]). So**

  $$ 5.4\ \mathrm{TeV} \;\lesssim\; \ell_z^{-1} \;\lesssim\; 29\ \mathrm{TeV}, \qquad 2\,\mu\mathrm{m} \;\lesssim\; m_\chi^{-1} \;\lesssim\; 66\,\mu\mathrm{m}. $$


### 05 — The dark sector: the oscillating circle
_Source: v2/05_dark_sector.md_

- **level dominates,**

  $$ F_T \simeq -\,118\,T^4\left(\frac{x}{2\pi}\right)^{3/2}e^{-x}, \qquad \Delta\ln\ell_z = \frac{\partial F_T/\partial\ln\ell_z}{\ell_z^2 V''} = \frac{118\,T^4 (x/2\pi)^{3/2}\,x\,e^{-x}}{20\,C_z/\ell_z^4}, $$

- **it is the bound:**

  $$ T_R < T_o = \left(\frac{90}{\pi^2 g_*}\right)^{1/4}\sqrt{m_\chi M_{Pl}} \approx 2.7\ \mathrm{TeV}\left(\frac{\ell_z^{-1}}{10\ \mathrm{TeV}}\right). $$

- **$\bar\ell_z(1+\delta_z)$ for the circle radius at the impact, so $\Delta\chi/M_{Pl} = \delta_z$. Then**

  $$ \frac{\rho_\chi}{\rho_r}\Big|_{T_R} = \frac{\tfrac12 m_\chi^2 \delta_z^2 M_{Pl}^2}{3H^2(T_R) M_{Pl}^2} = \frac{\delta_z^2}{6}\left(\frac{T_o}{T_R}\right)^4, \qquad \frac{\rho_\chi}{\rho_r}\Big|_{T_e} \simeq \frac{\delta_z^2}{6}\,\frac{T_o^4}{T_R^3\,T_e} \quad(T_R \le T_o), $$

- **and $\Omega_\chi = \Omega_{DM}$ requires**

  $$ \delta_z \approx 3.1\times10^{-6}\left(\frac{T_R}{T_o}\right)^{3/2} \qquad(2\times10^{-8}\ \text{at}\ T_R = 100\ \mathrm{GeV}). $$


### 06 — Predictions: what the nine numbers say that they were not fitted to
_Source: v2/06_predictions.md_

- **the brane metric in the frame where the 4D Planck mass is constant:**

  $$ ds^2 = e^{-\sigma}\, g_{\mu\nu}dx^\mu dx^\nu + e^{2\sigma} dz^2 . $$

- **Kaluza–Klein result**

  $$ S \supset \int d^4x\sqrt{-g}\;\frac{M_{Pl}^2}{2}\Big[R - \tfrac32 (\partial\sigma)^2\Big], \qquad \chi \equiv \sqrt{\tfrac32}\,M_{Pl}\,\sigma , $$

- **on $\ell_z$ through the gauge kinetic term, $1/g_4^2 = 2\pi\ell_z/g_5^2$ (`04d` §1):**

  $$ \Lambda_{QCD} = \mu_{KK}\,\exp\!\Big(-\frac{2\pi}{b_0\,\alpha_s(\mu_{KK})}\Big), \qquad \mu_{KK} = \ell_z^{-1},\quad \frac{1}{\alpha_s(\mu_{KK})} \propto \ell_z , $$

- **are dropped at the same level [verify]. Altogether, at $\ell_z^{-1} = 10$ TeV,**

  $$ \frac{d\ln m_N}{d\sigma} = -\tfrac12 - 1 - 12.4 = -13.9, \qquad \beta \equiv M_{Pl}\frac{d\ln m_N}{d\chi} = \frac{-13.9}{\sqrt{3/2}} = -11.3, \qquad \alpha_Y = 2\beta^2 = 2.6\times10^2 . $$

- **read off the figure [verify]) are crossed at**

  $$ \alpha_Y = 2.7\times10^2 \;\;\Rightarrow\;\; \lambda < 11.7\,\mu\mathrm m \;\;\Leftrightarrow\;\; \ell_z^{-1} > 14.2\ \mathrm{TeV}. $$

- **The upper edge $\ell_z^{-1} < 29$ TeV ($|\delta_1| < \sigma_1$) is unchanged, so**

  $$ 14\ \mathrm{TeV} < \ell_z^{-1} < 29\ \mathrm{TeV}, \qquad 2.8\,\mu\mathrm m < \lambda < 12\,\mu\mathrm m, \qquad \alpha_Y = 270\text{–}300 . $$


### v2 status — after milestone 7: budget FROZEN at 9
_Source: v2/STATUS.md_

- **Equation from v2 status — after milestone 7: budget FROZEN at 9**

  $$ S = \int d^6X \sqrt{-G}\left[\tfrac{M_6^4}{2} R_6 - \Lambda_6 - \tfrac12 (\partial\Phi)^2 - V(\Phi)\right] + \sum_{i=1,2} \int_{\Sigma_i} d^5\xi \sqrt{-\gamma_i}\left[-\sigma_i + \mathcal L_{\text{matter},i}\right] + M_6^4 \sum_i \int_{\Sigma_i} [K_i], \qquad V(\Phi) = V_0\, e^{-c\,\Phi/M_6^2}. $$

- **Equation from v2 status — after milestone 7: budget FROZEN at 9**

  $$ S_{\text{eff}} = \int d^4x\sqrt{-g}\left[\tfrac{M_{Pl}^2(\phi)}{2}R - \tfrac{K(\phi)}{2}(\partial\phi)^2 - \delta\sigma_2^{(5)}\Omega^4 - \tfrac12(\partial\Phi_4)^2 - V_* e^{-c\Phi_4/M_{Pl}}\right] + S_{SM}[g] + S_{\text{mirror}}[\Omega^2 g] $$


## Source Context
- Theory directory: /home/gregory-dearth/projects/bmi_project
- Master axiom file: /home/gregory-dearth/projects/bmi_project/master_axiom.md
- Files scanned: 82
- Chapters with equations: 33
- Equations compiled: 162 (29 with term definitions)
