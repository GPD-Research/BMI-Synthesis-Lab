# Appendix E: The Effective Field Theory Limit (QFT Emergence)

### E.1 Kaluza-Klein Expansion and Compactification
In the BMI framework, the fundamental 6D bulk action for a massless scalar field $\Phi(x^\mu, y, z)$ is defined as:

$$S_{6D} = -\frac{1}{2} \int d^4x \int_0^\delta dy dz \sqrt{-G} G^{AB} \partial_A \Phi \partial_B \Phi$$

To recover the 4D physics observable in our interface, we perform a Kaluza-Klein expansion along the compactified dimensions $(y, z)$. We decompose the field $\Phi$ into an infinite tower of modes:

$$\Phi(x^\mu, y, z) = \sum_{n,m} \phi_{nm}(x^\mu) \chi_{nm}(y, z)$$

where $\chi_{nm}(y, z)$ are the normalized eigenfunctions of the Laplace-Beltrami operator $\nabla^2_{y,z}$ on the thick brane domain. These eigenfunctions satisfy the boundary conditions imposed by the bulk-interface tension.

### E.2 Dimensional Reduction and EFT Limit
Substituting this expansion into the 6D action and integrating over the extra-dimensional coordinates, the action reduces to an effective 4D form:

$$S_{eff} = -\frac{1}{2} \sum_{n,m} \int d^4x [ \partial^\mu \phi_{nm} \partial_\mu \phi_{nm} - M_{nm}^2 \phi_{nm}^2 ]$$

The effective masses $M_{nm}$ are proportional to the eigenvalues of the extra-dimensional Laplacian. At energy scales $E \ll 1/\delta$, the massive modes ($n, m > 0$) are frozen out. The dynamics are dominated by the zero-mode $\phi_{00}$, which reproduces the standard 4D QFT Lagrangian for a massless scalar field.

### E.3 Path Integral as a Partition Function
The transition amplitude $Z_{6D}$ is defined over the 6D path space. By integrating over the extra-dimensional fluctuations $\chi_{nm}$ as a Gaussian measure, we obtain the reduced propagator:

$$D_F(x - y) = \langle 0 | T\{\phi(x) \phi(y)\} | 0 \rangle = \lim_{\delta \to 0} G_6(x, y; y, z)$$

This formally proves that "virtual particle" interactions in 4D are, fundamentally, the physical harmonic overtones of the interface fabric vibrating between its boundary walls.
