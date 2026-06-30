# Appendix F: Classical Relativity as Macro-Geometry

### F.1 Gauss-Codazzi Projection of the 6D Einstein-Hilbert Action
We begin with the 6D Einstein-Hilbert action evaluated in the bulk:

$$S_{EH} = \frac{1}{2\kappa_6^2} \int d^6x \sqrt{-G} R_6$$

To project this onto our 4D hypersurface, we use the Gauss-Codazzi relations to express the 6D Ricci scalar $R_6$ in terms of the 4D Ricci scalar $R_4$, the extrinsic curvature tensor $K_{\mu\nu}$, and the acceleration of the normal vectors. Assuming a Gaussian normal coordinate system $G_{AB} = \text{diag}(g_{\mu\nu}, h_{ab})$:

$$R_6 = R_4 + K^2 - K_{\mu\nu}K^{\mu\nu} + \nabla_\mu(a^\mu)$$

where $R_4$ is the intrinsic Ricci scalar of our 4D brane and $K$ is the trace of the extrinsic curvature.

### F.2 Derivation of 4D Einstein Field Equations
Integrating the action over the brane thickness $\delta$ effectively scales the coupling constant $\kappa_6$ to the 4D gravitational constant $G_N$:

$$S_{eff} = \frac{1}{2\kappa_4^2} \int d^4x \sqrt{-g} R_4 + S_{matter}$$

Varying this effective action with respect to the induced 4D metric $g^{\mu\nu}$ yields the Einstein Field Equations in 4D:

$$G_{\mu\nu} = 8\pi G_N T_{\mu\nu}$$

This proves that gravity is not a "force" derived from quantum fields, but the intrinsic geometric curvature of our 4D brane moving within the higher-dimensional bulk geometry.

### F.3 Special Relativity and Local Lorentz Invariance
In the limit where the induced metric $g_{\mu\nu}$ is flat ($\eta_{\mu\nu}$), the 4D hypersurface preserves global $SO(3,1)$ symmetry. The Lorentz group $SO(3,1)$ arises as the stabilizer subgroup of the brane's embedding in the 6D bulk, formally recovering Special Relativity as the local geometric baseline for all field dynamics.
