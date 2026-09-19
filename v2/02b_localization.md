# BMI v2 — 02b. Where fields live: the localization equation

**Question.** Does the geometry of `02_effective_4d.md` §1 *force* which fields are confined
to $\Sigma_1$, which spread into the shared $(y,z)$ pair, and which reach us from $\Sigma_2$
— or is that a choice? Rule from `00_axiom.md`: a per-species choice is a slot and is not
admitted.

**Answer in one line.** Spin decides most of it, and the two extra dimensions are forced to
play different roles; but for fermions the geometry leaves one dial per species (the bulk
mass), and 6D anomaly cancellation only pairs chiralities, it does not fix the dial. What is
forced is listed in §5; what remains a choice is listed in §6, with the only non-just-so way
to close it.

Checked symbolically in `tests/check_zero_modes.py`.

---

## 1. The equation

Background, $A = y/\ell$, $d = 5$ warped directions $x^a = (x^\mu, z)$:
$$
ds^2 = e^{-2A}\,\eta_{ab}\,dx^a dx^b + dy^2 .
$$

A bulk field of any spin, expanded in 4D modes of mass $m_4$ and circle momentum $n$,
has a $y$-profile $f(y)$ obeying (spin-0 form; the others differ by the spin-connection
term and are in the test file)
$$
e^{dA}\,\partial_y\!\left(e^{-dA}\,\partial_y f\right) + e^{2A}\!\left(m_4^2 - \frac{n^2}{\ell_z^2}\right) f - M^2 f = 0 .
$$
Its normalization density $\rho(y)$ — the kinetic measure times $|f|^2$ — decides where the mode
lives: $\rho$ falling in $y$ = on $\Sigma_1$; rising = on $\Sigma_2$; flat = shared.

## 2. Result by spin (massless 4D modes, $n = 0$)

| spin | profile $f$ | $\rho(y) \propto$ | lives on | in 5D RS for comparison |
|---|---|---|---|---|
| 2 (graviton) | $1$ | $e^{-3A}$ | $\Sigma_1$ | $e^{-2A}$, $\Sigma_1$ |
| 0 (massless) | $1$ | $e^{-3A}$ | $\Sigma_1$ | $e^{-2A}$, $\Sigma_1$ |
| 1 (gauge) | $1$ | $e^{-A}$ | $\Sigma_1$, weakly | flat (shared) |
| ½, chirality $+$, bulk mass $c/\ell$ | $e^{(5/2 - c)A}$ | $e^{(1-2c)A}$ | $\Sigma_1$ iff $c > \tfrac12$ | same condition |
| ½, chirality $-$ | $e^{(5/2 + c)A}$ | $e^{(1+2c)A}$ | $\Sigma_1$ iff $c < -\tfrac12$ | same condition |

Observations that are *not* choices:

- **Gravity and the radion are on $\Sigma_1$**, with the $e^{-3A}$ that gave
  $M_{Pl}^2 \propto (1-e^{-3\phi/\ell})$. Fork 1 is self-consistent.
- **A bulk gauge field in 6D is not flat** — unlike 5D Randall–Sundrum, the warped circle
  tilts its norm toward $\Sigma_1$ by $e^{-y/\ell}$. Its *coupling* is nevertheless universal
  (constant profile, gauge invariance): a bulk gauge field charges $\Sigma_2$ matter exactly
  as it charges ours. (Consequence for §4.)
- **Fermion localization depends on $c$ and only on $c$**, and the threshold $|c| = \tfrac12$
  is the same in $D = 5$ and $D = 6$. The geometry does not prefer a value of $c$.

## 3. The two extra dimensions are not interchangeable

This is the one result here that is specific to the 6D setup and was not assumed.

- **Excitations along $z$** ("winding into the shared circle"): the mode with circle
  momentum $n$ has 4D mass exactly $m_4 = n/\ell_z$ and the *same* $y$-profile as the zero
  mode. Because the circle is warped together with the 4D directions, the warp cancels out
  of its mass. The $z$-tower is heavy (set by $\ell_z$, the UV-brane radius) and sits where its
  zero mode sits — for gravity, gauge and light scalars, on $\Sigma_1$.
- **Excitations along $y$** ("reaching toward the other manifold"): standard RS behaviour,
  masses $m_k \simeq x_k\, e^{-\phi/\ell}/\ell$ with $x_k$ Bessel zeros, profiles peaked at
  $\Sigma_2$ **[verify: Bessel order for $d=5$]**.

So, in the language of the genesis idea: "winds in the extra circle" $\Rightarrow$ heavy,
ours; "extends toward the other brane" $\Rightarrow$ light by $\Omega$, theirs. That is a
qualitative prediction about *towers*, forced by the metric. It is not yet a statement about
which Standard-Model species does which.

## 4. What the Standard Model's own properties force

Three constraints follow without any per-species input.

1. **Chirality forces an orbifold.** $\Sigma_1$ is five-dimensional ($x^\mu$ plus the
   circle). A fermion confined to it is a 5D fermion and is vector-like; there are no chiral
   4D fermions on $S^1$. The observed chiral SM therefore forces $z \in S^1/\mathbb Z_2$
   (or a further defect inside $\Sigma_1$; the orbifold is the minimal option). The SM zero
   modes then sit at the orbifold fixed points and are 4D-chiral. **This changes
   `01_action.md` §1: $z \sim z + 2\pi\ell_z$ becomes $S^1/\mathbb Z_2$.** No parameter is
   added; the Planck relation $M_5^3 = 2\pi\ell_z M_6^4$ becomes $\pi\ell_z M_6^4$, absorbed in
   $M_5$.
2. **Collider bounds put the gauge bosons on the brane.** If any SM gauge field were a bulk
   field, its $y$-tower would start at $m_1 \simeq 2.5\, e^{-\phi/\ell}/\ell$
   **[verify: $x_1$ for $d=5$]**; LHC dilepton/dijet searches need $m_1 \gtrsim 5$–$10$ TeV.
   With the Cassini floor $\phi/\ell \gtrsim 5$ that is $\ell \lesssim 7\times10^{-22}$ m, i.e.
   a bulk curvature radius of order $10^{13}$ Planck lengths or less. Allowed but not forced. The
   decisive argument is the second: a bulk gauge field couples universally (§2), so mirror
   matter would carry ordinary electric and colour charge and would not be dark. So **SM
   gauge fields are on $\Sigma_1$**, independent of $\ell$.
3. **Bulk fermions come in 6D-chirality pairs.** A single 6D Weyl fermion has an
   irreducible gravitational anomaly ($\mathrm{tr}\,R^4$) that nothing on a codimension-one
   brane can cancel by inflow **[verify: 6D anomaly polynomial, Alvarez-Gaumé–Witten 1984]**.
   Any bulk fermion must therefore come with an opposite-chirality partner (or a self-dual
   tensor, which we do not have). The orbifold then selects which 4D chirality keeps a zero
   mode. This is exactly the structure of a bulk right-handed neutrino in ADD/RS models.

## 5. Forced (no choice made)

- Gravity, radion, any massless bulk scalar: on $\Sigma_1$.
- SM gauge fields, and hence the charged SM fermions: on $\Sigma_1$, 4D-chiral via the
  $\mathbb Z_2$ orbifold of the circle.
- The only species that *can* be bulk fields are gauge singlets: right-handed neutrinos
  (and $\Phi$).
- $z$-excitations are heavy and ours; $y$-excitations are light by $\Omega$ and theirs.
- Anything reaching us from $\Sigma_2$ does so at mass scale $\Omega\,m$.

## 6. Not forced (still a choice) and the only clean way to close it

The bulk mass $c$ of a bulk fermion. Per species it is a slot: with three generations of
bulk $\nu_R$ that is three numbers fitted to three masses — the harmonic trap. The single
non-just-so option is **one universal $c$ for all bulk singlets**, which can be motivated
by a flavour symmetry in the bulk but is, honestly, one added parameter (#8 in the ledger if
taken). It buys: one common suppression $\epsilon = e^{(1/2 - c)\phi/\ell}$ for all neutrino
Yukawas, so the neutrino *mass ratios* are fixed by the brane Yukawa matrix alone and the
absolute scale by $\epsilon$; Dirac neutrinos (no neutrinoless double-beta decay); a sterile
$z$-tower at $n/\ell_z$ (unobservable) and a sterile $y$-tower at $\sim \Omega/\ell$
(possibly observable — if $\ell$ is large this is the "cosmic flow of barely interacting
matter" of the genesis picture, and it is constrained by $N_{\text{eff}}$).

Not admitted: per-species $c$; brane-localized mass terms tuned to make massive bulk fields
have zero modes; any assignment of SM charged species to the bulk.

## 7. Ledger

No parameter added by this file. If §6's universal-$c$ option is taken in a later milestone,
$c_\nu$ becomes #8 and must pay for itself with at least two of: absolute neutrino mass
scale, Dirac nature, a $\Delta N_{\text{eff}}$ contribution from the sterile tower.

## 8. Corrections to earlier files

- `01_action.md` §1: circle $\to$ $S^1/\mathbb Z_2$ (forced by §4.1). Volume factor
  absorbed in $M_5$.
- `00_axiom.md` deferred hypothesis: constraints of §4 supersede the "LHC bounds" bullet
  (gauge fields are now excluded from the bulk by two independent arguments).
