# Appendix B: On the Age and Size of the Cosmos

## B.1 Theoretical Framework
This appendix establishes the mathematical constraints on the temporal age and spatial volume of the dual-manifold system under the topological assumption of a nested three-torus ($T^3$). While the global geometry deviates from infinite flat space, the local presentation of the cosmological background matches observational constraints, ensuring consistency with the standard $\Lambda$CDM model parameters.

## B.2 The Cosmic Age Parameter ($t_0$)
To demonstrate why the local presentation of the cosmos yields a standard age of approximately 13.8 billion years, we evaluate the expansion rate within the standard Friedmann framework. Given that the local screening mechanism drives the effective coupling constant toward its general relativistic limit ($g_{	ext{eff}} 	o 1$) in typical density regimes, the background Hubble parameter $H(a)$ tracks the standard energy density evolution.

The age of the manifold $t_0$ is calculated by integrating the inverse scale factor evolution from the initial singularity ($a = 0$) to the current epoch ($a_0 = 1$):

$$t_0 = \int_0^1 rac{da}{a \cdot H(a)}$$

Expanding $H(a)$ for a flat spatial geometry governed by non-relativistic matter ($\Omega_{m,0}$) and the cosmological constant ($\Omega_{\Lambda,0}$):

$$H(a) = H_0 \sqrt{\Omega_{m,0} a^{-3} + \Omega_{\Lambda,0}}$$

Substituting this into the time integral yields:

$$t_0 = rac{1}{H_0} \int_0^1 rac{da}{\sqrt{\Omega_{m,0} a^{-1} + \Omega_{\Lambda,0} a^2}}$$

Evaluating this analytically using standard concordance values ($H_0 pprox 67.4 	ext{ km/s/Mpc}$, $\Omega_{m,0} pprox 0.315$, and $\Omega_{\Lambda,0} pprox 0.685$):

$$t_0 = rac{2}{3 H_0 \sqrt{\Omega_{\Lambda,0}}} \ln \left( rac{\sqrt{\Omega_{\Lambda,0}} + 1}{\sqrt{\Omega_{m,0}}} ight)$$

$$t_0 pprox 13.787 	imes 10^9 	ext{ years}$$

Because the local modifications to gravity transition smoothly across density variations, the global temporal baseline remains completely sound and aligned with cosmic microwave background data.

## B.3 Spatial Scale and Volume of the Nested Torus ($T^3 	imes T^3$)
The spatial framework is modeled as a nested topological manifold where a large, macroscopic three-torus contains or is influenced by a compactified, secondary shadow manifold. Both are represented as flat Riemannian three-tori formed by identifying the opposite faces of a fundamental cubic domain.

### Manifold A: The Large/Local Manifold ($M_{	ext{local}}$)
The dimensions of our visible manifold are bounded below by the particle horizon ($d_H$), which is the maximum comoving distance light could have traveled since $t=0$:

$$d_H = c \int_0^{t_0} rac{dt}{a(t)} pprox 46.5 	ext{ billion light-years}$$

For a cubic three-torus with fundamental side length $L_{	ext{local}}$, the absence of recurring topological ghost images or matched circles in the cosmic microwave background requires that the fundamental scale exceed the diameter of the observable causal sphere:

$$L_{	ext{local}} > 2 d_H \implies L_{	ext{local}} \gtrsim 93 	imes 10^9 	ext{ light-years}$$

The total spatial volume ($V_{	ext{local}}$) of this fundamental domain is calculated as:

$$V_{	ext{local}} = (L_{	ext{local}})^3$$

Using the strict observational lower bound:

$$V_{	ext{local}} \gtrsim (9.3 	imes 10^{10} 	ext{ ly})^3 pprox 8.04 	imes 10^{32} 	ext{ ly}^3$$

### Manifold B: The Compactified Shadow Manifold ($M_{	ext{shadow}}$)
The nested secondary manifold exists at a compactification scale $L_{	ext{shadow}}$ far below the threshold of standard optical observation. It governs the structural constraints of the auxiliary fields (such as $\Phi_{	ext{shadow}}$ and $ho_{	ext{shadow}}$). Its fundamental linear dimension is defined by an intrinsic safety or screening cutoff scale:

$$L_{	ext{shadow}} \ll d_H$$

The volume ($V_{	ext{shadow}}$) of this nested domain is similarly defined by its periodic boundary periodicities:

$$V_{	ext{shadow}} = (L_{	ext{shadow}})^3$$

### Total Topological Volume Relations
Because the manifolds are nested or product-mapped topologically, the ratio of their spatial extents determines the structural coupling gradient across the cosmic voids:

$$rac{V_{	ext{local}}}{V_{	ext{shadow}}} = \left( rac{L_{	ext{local}}}{L_{	ext{shadow}}} ight)^3$$

While $V_{	ext{shadow}}$ remains confined to a tiny, microscopic or sub-galactic fundamental patch, the macroscopic manifold $V_{	ext{local}}$ expands dynamically, preserving a vast, finite, but un-bordered global volume that is orders of magnitude larger than the patch of space currently accessible to human observation.
