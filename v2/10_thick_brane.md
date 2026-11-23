# 10 — Fork: thick branes (saved leap, registered 2026-11-23)

The intuition behind this fork: two universes that collide and merge interact over a finite width,
so the branes should be thick walls, not the sharp boundaries of `01_action.md`. This file records
what thickness forces, what it would have to deliver, what it would cost, and how it dies, all
**before any derivation on it**. It is not part of the fixed action. Numbers: `tests/thick_brane.py`.

| result | status |
|---|---|
| a canonical bulk scalar forces $A'' \le 0$ for the warp $e^{2A(y)}$: walls made of it only have positive tension | derived (`tests/thick_brane.py`) |
| $\Sigma_1$ can be a smooth wall; its tension integrates to the RS value and the RS tuning moves into the shape of the wall potential $U$ | derived (`tests/thick_brane.py`) |
| $\Sigma_2$ has negative tension and **cannot** be a smooth wall of any canonical field; the fork must change the geometry or keep $\Sigma_2$ thin | derived (`tests/thick_brane.py`) |
| thickness does not remove the cosmological-constant tuning (Mounaix & Langlois 2002 keep a generalized RS condition) | literature, checked |
| late-time Friedmann equation: no new test; v2's $\rho^2$ term is already negligible below $T_t \approx 5\ \mathrm{TeV}$ | derived (`02_effective_4d.md` §3) |
| P1 (circle modulus) | unchanged by a width in $y$; the stabilizer must be re-derived |
| resolves the collision, fixes $T_2/T_1$ or $(\epsilon, f)$, gives a spectrum | **open**: the reason for the fork |
| parameters | at least +1 (the wall width) unless it is fixed by $\ell$; not taken |

## 0. Why this fork

The thin-brane action fails exactly where the axiom lives. At the collision, $\Omega \to 1$, 4D
gravity on $\Sigma_1$ switches off and the moduli description is invalid (`04_impact.md` §0). The
matching through the collision is not determined by the action. That is why three things are still
inputs or missing:

- $T_2/T_1$ (ledger #7) is a parameter, not an output (`04_impact.md` §2);
- the collision data $(\epsilon, f)$ that set $\phi_0$ are inputs (`04c_approach.md` §8);
- there is no primordial spectrum (`RETRACTED.md` N3, `04_impact.md` §6).

Walls with a finite width can overlap, pass through each other, bounce or annihilate, and that
evolution can be computed from a field theory. A thin brane cannot. That is the case for thickness.
The Friedmann-equation interpolation is *not* the case for it (§2d).

## 1. Prior work

Checked against the paper (2026-11-23):

- **Mounaix & Langlois**, "Cosmological equations for a thick brane", Phys. Rev. D 65, 103523 (2002),
  arXiv:gr-qc/0202089. (Circulated with an attribution to Maartens, Bass & Papadopoulos in Class.
  Quant. Grav.; the arXiv record and the paper name Mounaix and Langlois.) An averaged Friedmann
  equation for a brane of constant thickness interpolates between the thin-brane $\rho^2$ form and a
  linear, Kaluza–Klein-like form. The low-energy linear regime is derived *after* imposing a
  thickness-dependent generalization of the RS fine-tuning (their Eq. 22), which reduces to the RS
  condition in the thin limit. A thickness that changes in time is left as future work. So: the
  tuning is generalized, not removed, and a collision (time-dependent width) is outside the paper.

From memory, to be checked before use [verify]:

- DeWolfe, Freedman, Gubser & Karch (2000), "Modeling the fifth dimension with scalars and
  gravity": flat walls from a superpotential; a flat ($\Lambda_4 = 0$) wall needs a potential of a
  specific form. This is where the tuning goes.
- Gremm (2000); Csáki, Erlich, Hollowood & Shirman (2000): gravity localization on smooth walls.
- Kehagias & Tamvakis (2001): smooth walls localizing gravity, gauge fields and chiral fermions.
- Takamizu & Maeda (2004); Takamizu, Kudoh & Maeda (2007): collisions of two thick domain walls in
  AdS$_5$, computed numerically from the field equations. The closest precedent to BMI's collision.
- Dzhunushaliev, Folomeev & Minamitsuji (2010): review of thick-brane solutions.
- Self-tuning attempts (Arkani-Hamed, Dimopoulos, Kaloper & Sundrum; Kachru, Schulz & Silverstein,
  2000) and their critiques (Csáki, Erlich, Grojean & Hollowood; Förste, Lalak, Lavignac & Nilles,
  2000): removing the tuning this way leaves a bulk singularity.

## 2. What thickness forces

Replace a thin brane by a wall of a canonical bulk scalar $W$ with potential $U(W)$ (which absorbs
$\Lambda_6$), in the warped metric $e^{2A(y)}(\eta_{\mu\nu}dx^\mu dx^\nu + dz^2) + dy^2$ of
`01_action.md` §3, where the thin case is $A = -y/\ell$.

### 2a. The null energy condition

For the null vector along $t$ and $y$, the Einstein tensor gives $-4A''$ and a canonical scalar gives
$W'^2$ (`tests/thick_brane.py`):
$$
A'' = -\frac{W'^2}{4M_6^4} \le 0 .
$$
$A'$ can only decrease along $y$. A thin brane of tension $\sigma$ is a jump in $A'$ of
$-\sigma/(4M_6^4)$ when the bulk is on both sides, so canonical walls only ever make positive tension.

### 2b. $\Sigma_1$ can be smooth; the tuning moves into $U$

A smooth version of $\Sigma_1$ with the $\mathbb Z_2$ reflection, $A'$ running from $+1/\ell$ to
$-1/\ell$ across a finite width, is allowed: $W'^2 \ge 0$ everywhere, the integrated tension is the
two-sided RS value $8M_6^4/\ell$, and far from the wall $U \to \Lambda_6$. But $U$ is read off from
$A$ ($U = W'^2/2 - 10M_6^4A'^2$): the static flat wall exists only if $U$ has the shape built to
match. A generic $U$ gives a de Sitter or anti-de Sitter wall instead. The RS tuning (ledger #2) is
still there, as a relation inside $U$.

### 2c. $\Sigma_2$ cannot be smooth

$\Sigma_2$ is the negative-tension brane: across its $\mathbb Z_2$ reflection $A'$ runs from $-1/\ell$
to $+1/\ell$, so $\int W'^2\,dy = -8M_6^4/\ell < 0$. No canonical field gives that. The fork must pick
one of:

1. **Thick $\Sigma_1$, thin $\Sigma_2$.** $\Sigma_2$ stays a sharp orbifold boundary. The geometry and
   all v2 results stay; the collision becomes a wall hitting a boundary, which is only half resolved.
2. **Two positive-tension walls.** Drop the reflection at $\Sigma_2$, so the bulk continues beyond it.
   Both walls are smooth, and their collision is the Takamizu–Maeda problem. But this is a different
   geometry: $M_{Pl}^2(\phi)$, the radion, the Cassini bound, $\delta\sigma_2$ (#4) and the warped
   mirror sector all have to be re-derived, and gravity must still be shown to localize.
3. **A non-canonical or ghost field.** Excluded by `01_action.md` criterion 2.

Note that v2's collision is between opposite tensions ($\sigma_1 + \sigma_2 = \delta\sigma_2 \approx 0$),
the opposite of the kink–antikink pair of a field theory. Option 2 is closer to "two universes
collide"; option 1 is closer to v2.

### 2d. The Friedmann equation

Thickness changes the brane Friedmann equation only at energies comparable to the inverse wall
width or to the tension. v2's $\rho^2$ term is already suppressed by $(T/T_t)^4$ with
$T_t \approx 5\ \mathrm{TeV}$ (`02_effective_4d.md` §3), so late-time cosmology gives no test of the
width. The interpolation to $H^2 \propto \rho$ is real, but v2 already has it.

### 2e. P1

The fifth force of P1 comes from the circle modulus $\ell_z$, not from the width in $y$. A thick
wall leaves it. It does change the stabilizer: $\delta_1$ (#8) is the detuning of $\sigma_1$, which
becomes a detuning of $U$, and the Casimir term must be recomputed on a smooth profile
(`04d_circle.md` §3). P1 stays registered until that is done.

## 3. What the fork must deliver

- **D1.** A static flat solution of gravity plus one canonical scalar for the chosen option of §2c, with
  the tuning stated as a relation in $U$, not claimed solved.
- **D2.** Kills 1 and 2 still pass: the GR + ΛCDM limit and LLR/Cassini, in the chosen geometry.
- **D3.** The collision computed from the field equations, from approach to separation. Its outputs
  must include the energy split between the two walls and the bulk, i.e. $T_2/T_1$ and $(\epsilon, f)$.
- **D4.** Whatever the collision produces in fluctuations: a primordial spectrum, or an explicit
  statement that it produces none (N3 stays).
- **D5.** The stabilizer re-derived on the smooth profile, and P1's range recomputed.
- **D6.** A parameter count (§4) under the ledger's rules.

## 4. Price

The thin action spends $\sigma_1$ (tuned to $\ell$), $\delta\sigma_2$ (#4) and $\delta_1$ (#8) on the
branes. A wall model spends a choice of potential shape (a finite menu, e.g. quartic or sine-Gordon)
and its numbers: a height and a width. The height replaces the tension. The width is new unless the
equations fix it in terms of $\ell$. Expected price: **+1** (the width), more under option 2.

The provisional-tenth slot of `ledger.md` was used by the exchange fork, which died, and the freeze
is back at 9. Registering this fork costs nothing. Computing it as a tenth number needs that slot
reopened for it, under the same rules: admitted only if it fixes or predicts one of the nine
(candidates: $T_2/T_1$, $\phi_0$ through $(\epsilon, f)$, $\delta_z$ through the impact), paused if it
fits but connects to none, dead only by data.

## 5. Kill criteria (written 2026-11-23, before any derivation)

- **TK1.** If neither option 1 nor option 2 of §2c gives a static flat solution that passes kills 1
  and 2, the fork is dead.
- **TK2.** If the collision of D3 gives $T_2/T_1$ or a bulk mass that violates the $\Delta N_{\text{eff}}$
  bound for every wall shape on the menu and every width, the fork is dead by data.
- **TK3.** If D3 shows that the walls pass through each other or bounce with an energy split that
  depends on the incoming state and not on the action, the collision is unresolved again and the
  fork fixes none of the nine: paused, not admitted.
- **TK4.** Any spectrum (D4) or gravitational-wave output is written down with a date, from the
  action, before it is compared with data (the R1 guard). A spectrum outside Planck's $n_s$ window kills
  that output.
- **TK5.** If D5 moves P1's range, the new range is registered before any comparison with
  inverse-square-law data, and the old one is not kept as a fallback.
- **TK6.** No claim that the cosmological-constant tuning is solved. If the derivation needs $U$
  tuned, that is recorded as tuning and ledger #2 stays.

## 6. Neutrinos and gravitational waves

- **Neutrinos.** A smooth wall localizes fermions through a Yukawa coupling to $W$ (the Rubakov–
  Shaposhnikov mechanism). That coupling is a new number per species unless it is universal, which
  would collide with the one-number rule for $c_\nu$ (`ledger.md`, pending constants). The bulk
  right-handed neutrino of `00_axiom.md` does not need a thick wall.
- **Gravitational waves.** Colliding walls radiate. A stochastic background with a peak frequency
  set by the collision temperature is a natural output of D3; for TeV-scale reheating it would sit
  near the LISA band [order of magnitude, verify]. It counts only if computed from D3 and registered
  under TK4.

## 7. Order of work, if the slot is reopened

1. Choose option 1 or 2 of §2c (decision, recorded with the alternative).
2. D1 and D2 analytically.
3. D3 numerically: a 1+1 field evolution (time and $y$) with gravity, following Takamizu–Maeda.
4. D4, D5, D6, then the ledger decision.
