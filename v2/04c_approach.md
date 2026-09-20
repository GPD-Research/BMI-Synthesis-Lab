# 04c — The approach to $\Omega = 1$ without the moduli approximation

Milestone 5c. Question asked: does the collision hand the 4D equations *one* number, or the
three (`r_b`, `f_2`, `\mathcal C`) that `04b_initial_conditions.md` scanned as independent?
Method: drop the moduli approximation of `03_background.md` §1 and use the exact two-brane
solution of the bulk equations. Numbers: `tests/approach.py`.

| result | status |
|---|---|
| the exact two-brane bulk is static Schwarzschild–AdS; each brane's motion is fixed by its own content; **there is no independent radion** | derived (Birkhoff, §1) |
| $\Omega_\infty^{\,n-1} = (\epsilon - f)/(1 + \epsilon)$: the frozen separation in closed form from two collision data | derived (§2), checked numerically to 5% |
| the three post-impact data collapse to two: `r_b` is a function of $(f, \epsilon)$ | derived |
| $\epsilon \ge f$: dark radiation on $\Sigma_1$ must be at least the energy on $\Sigma_2$ (as we see it), or $\Sigma_2$ has no real trajectory | derived (§3) |
| Cassini becomes $\epsilon - f < 3.3\times10^{-5}\,(1+\epsilon)$ in 6D: the 1.5% coincidence of `04_impact.md` §1 sharpens to $\sim 0.1$–$0.3\%$ of $f$ | derived (§4) |
| high-energy collisions ($\rho \gtrsim \sigma$) lose the brane ordering: $\Sigma_2$ overtakes $\Sigma_1$; the action does not describe this | numerical (§5) |
| the exact solution requires all four brane spatial directions to expand together; the fixed circle of `01_action.md` is an **unstabilized modulus** | gap found (§6) — new pending item, kill risk |

## 0. What is different from 03/04

The moduli approximation treats the brane separation $\phi$ as a 4D scalar with its own
kinetic energy, so the impact could hand it an independent velocity (`r_b`). Below, the bulk
between the branes is solved exactly instead. For a bulk with plane-symmetric slices and no
bulk matter — $\Phi$ is negligible early (`03_background.md` §3.1) — the generalized Birkhoff
theorem (Bowcock, Charmousis & Gregory 2000, hep-th/0007177) says the bulk is
Schwarzschild–AdS with a single mass parameter, and each brane is a moving hypersurface in it.
The "radion" is then the *difference of two trajectories*, each fixed by its own junction
condition. Nothing else is available to it.

## 1. Setup

Bulk (units $\ell = 1$, $\kappa^2 = 1/M_6^4 = 1$), $n$ isotropic spatial directions on the brane:
$$
ds^2 = -f\,dt^2 + \frac{dr^2}{f} + \frac{r^2}{\ell^2}\,d\vec x^{\,2},
\qquad f(r) = \frac{r^2}{\ell^2} - \frac{\mu}{r^{\,n-1}} .
$$
$\mu$ is the bulk mass; on a brane it appears as $\rho_E = $ `\mathcal C`$/a^{n+1}$ — the same
dark radiation as `02_effective_4d.md` §3, now with a definite bulk meaning. A $\mathbb Z_2$
brane at $r = R(\tau)$ with tension $\pm\sigma_1$ and radiation $\rho = A/R^{n+1}$ obeys
(Kraus 1999; Ida 2000; Binétruy, Deffayet & Langlois 2000; the $n=4$ case is the 6D action
with the circle expanding with the brane, **[verify]** the $n=4$ coefficient against a
direct Israel computation)
$$
\sqrt{\frac{f}{R^2} + H^2} = \frac{\sigma_1 + s\,\rho}{2n},
\qquad s = +1\ (\Sigma_1),\quad s = -1\ (\Sigma_2),
\qquad \sigma_1 = \frac{2n}{\kappa^2\ell} ,
$$
which for $n = 4$ is the tension $8M_6^4/\ell$ of `01_action.md` §3 — the tuning is
recovered, not assumed. Squaring:
$$
H_1^2 = \frac{\rho_1}{n}\Big(1 + \frac{\rho_1}{2\sigma_1}\Big) + \frac{\mu}{R_1^{\,n+1}},
\qquad
H_2^2 = -\frac{\rho_2}{n}\Big(1 - \frac{\rho_2}{2\sigma_1}\Big) + \frac{\mu}{R_2^{\,n+1}} .
$$
The sign flip on $\Sigma_2$ is the known negative-tension-brane result: its own radiation
*decelerates* its expansion in the bulk frame; only the bulk mass can make it expand.

Collision data. At coincidence $R_1 = R_2 = 1$ define
$$
f \equiv \frac{A_2}{A_1} = \frac{\rho_2}{\rho_1}\Big|_{\Omega=1},
\qquad
\epsilon \equiv \frac{n\mu}{A_1} = \frac{\rho_E}{\rho_1}\Big|_{\Omega=1},
\qquad
h \equiv \frac{\rho_1}{\sigma_1}\Big|_{\Omega=1} .
$$
$f$ is `f_2`$/(1-$`f_2`$)$ of `04b_initial_conditions.md`; $\epsilon$ is the dark-radiation
ratio whose late-time value `04_impact.md` §4 estimated from emission; $h$ measures how far
above the tension scale the collision was.

## 2. The frozen separation in closed form

At low energy ($\rho \ll \sigma_1$, $f \approx R^2$) the bulk-time speed of a brane is
$dR/dt = R^2 H$, so with $H_i^2 R_i^{n+1} = A_1(1+\epsilon)/n$ and $A_1(\epsilon - f)/n$
respectively,
$$
R_i^{(n-1)/2} \propto t
\quad\Rightarrow\quad
\boxed{\;\Omega_\infty^{\,n-1} = \lim_{t\to\infty}\Big(\frac{R_2}{R_1}\Big)^{n-1} = \frac{\epsilon - f}{1+\epsilon}\;}
$$
For the 6D action ($n=4$) $\Omega_\infty^3 = (\epsilon-f)/(1+\epsilon)$; for the 5D two-brane
system without a circle ($n=3$), $\Omega_\infty^2$. `tests/approach.py` §1 integrates the
full junction equations from coincidence and reproduces this to better than 5% for
$h = 0.01$ (and still at $h = 1$ when $f, \epsilon \ll 1$).

What this replaces. In `04_impact.md` §1 the same quantity was
$\Omega_0 = [1 - \tfrac{3}{2\sqrt2}\,\mathrm{asinh}\sqrt{r_b}]^{2/3}$ with `r_b` free. Here
`r_b` does not exist as a datum: the relative motion of the branes is whatever
$(f, \epsilon)$ dictate. So the answer to the milestone question is **two, not three** —
and neither of the two is a velocity. The Friedmann-level freeze-out picture survives
(the separation does freeze); its input does not.

## 3. Existence: $\epsilon \ge f$

$H_2^2 \ge 0$ at low energy requires $\mu/R_2^{n+1} \ge \rho_2/n$. Written on $\Sigma_1$,
where $\Sigma_2$'s energy appears warped by $\Omega^{n+1}$, this is
$$
\rho_E \;\ge\; \Omega^{n+1}\rho_2 \quad\Leftrightarrow\quad \epsilon \ge f :
$$
**the dark radiation on our brane is bounded below by the energy on the other brane.**
For $\epsilon < f$ the junction condition has no real solution at coincidence
(`tests/approach.py`: "no real trajectory for $\Sigma_2$"); at high energy ($h \gtrsim 1$,
where the $\rho_2^2$ term flips the sign) $\Sigma_2$ can start expanding, but it stops when
$\rho_2$ has diluted to $2\sigma_1$ and falls to the bulk horizon — the overshoot of
`04_impact.md` §1, now with a cause. Consequences for the scan of `04b_initial_conditions.md`:

- the $N_{\text{eff}}$ budget is at least **twice** the mirror-sector one, because $\rho_E$
  counts as dark radiation too ($\Delta N_{\text{eff}} \ge 2\times$ the value of
  `04_impact.md` §2 at given $x = T_2/T_1$);
- the emission fixed point $\epsilon_W \approx 5\times10^{-3}$ of `04_impact.md` §4 is a
  *floor added later*; the collision itself must already supply $\epsilon \ge f$, i.e.
  $\epsilon \gtrsim x^4$. With $x < 0.45$ this is $\epsilon \gtrsim 0.04$, eight times the
  emission value — `\mathcal C` is therefore *not* small and *not* computed by emission alone;
  its status in `ledger.md` is downgraded from "resolved" to "bounded below by $f$".

## 4. The Cassini window, sharpened

$\Omega_0 < 0.032$ means $\epsilon - f < 0.032^{\,n-1}(1+\epsilon)$:

| $n$ | $f$ | allowed $\epsilon$ | width / $f$ |
|---|---|---|---|
| 4 | 0.04 | $[0.04,\ 0.04003]$ | $8.5\times10^{-4}$ |
| 4 | 0.01 | $[0.01,\ 0.01003]$ | $3.3\times10^{-3}$ |
| 4 | $10^{-3}$ | $[10^{-3},\ 1.03\times10^{-3}]$ | $3.3\times10^{-2}$ |
| 3 | 0.01 | $[0.01,\ 0.011]$ | $0.10$ |

(`tests/approach.py` §2.) The coincidence of `04_impact.md` §1 — `r_b` within 1.5% of
overshoot — was the moduli-approximation shadow of this: in the exact solution the dark
radiation must match the $\Sigma_2$ energy to a part in $10^3$ for a mirror sector hot
enough to matter, and the *natural* outcome of a generic collision ($\epsilon$ and $f$
unrelated) is either no $\Sigma_2$ at all ($\epsilon < f$) or $\Omega_0 \sim 0.1$–$1$
(excluded by Cassini). This is worse for the "continuing collision" axiom than milestone 5
made it look, and it is recorded as such. One way out is physical rather than tuned:
$\epsilon = f$ *exactly* is the statement that the bulk mass is the energy $\Sigma_2$ radiated
into the bulk — a collision in which $\Sigma_2$'s content ends up entirely as bulk radiation
seen from our side would sit at the edge $\Omega_\infty \to 0$ with $\Sigma_2$ empty. That is
the "no mirror dark matter" family of `04b_initial_conditions.md` §4, now the *generic* one.

## 5. High-energy collisions

For $h \gtrsim 1$ (`tests/approach.py` §3) the $\rho^2$ terms dominate and the closed form
fails: at $h = 10$ with $f = 0.5$ the trajectories cross ($\Omega > 1$) — $\Sigma_2$ passes
through $\Sigma_1$ and the UV/IR assignment (Fork 1) is lost. The action has no term for two
branes crossing; the ekpyrotic literature (Khoury, Ovrut, Steinhardt & Turok 2001) treats
this as the regime where matching rules must be supplied by hand. So the honest scope of the
exact solution is $h \lesssim 1$: a collision that reheats to no more than the tension scale,
$T_{\text{RH}}^{\,n+1} \lesssim \sigma_1 \sim M_6^4/\ell$. For $\ell \sim 10\,\mu$m and
$M_6$ fixed by $M_{Pl}$ this is a bound on the reheating temperature to be evaluated in
milestone 6 **[verify]**.

## 6. The gap this exposes: the circle is a modulus

The exact solution exists only because all $n$ brane directions share one scale factor. The
6D action of `01_action.md` instead assumes three expanding directions and a circle of fixed
proper size $\ell_z$. The AdS$_6$ background solves the bulk equations for *any* $\ell_z$
(`tests/check_background.py` never used its value): the circle radius is a flat direction, a
massless 4D scalar. Because the SM lives on a 4-brane wrapping $z$, its 4D gauge couplings
scale as $1/g_4^2 \propto \ell_z$, so this modulus is a dilaton coupled to the SM. Unstabilized
it gives (i) a fifth force at gravitational strength — excluded by Cassini/Eöt-Wash unless its
mass exceeds $\sim 10^{-3}$ eV, and (ii) a drifting fine-structure constant — bounded by atomic
clocks to $|\dot\alpha/\alpha| < 10^{-17}\,\mathrm{yr}^{-1}$ and by quasar spectra to
$|\Delta\alpha/\alpha| \lesssim 10^{-5}$ since $z \sim 3$. In the isotropic solution above the
circle grows with $a$, i.e. $\alpha \propto 1/a$: excluded by many orders of magnitude.

Therefore the fixed-circle assumption of `01_action.md` §1 is not a solution of the action as
written; it needs a stabilization mechanism (a flux through the circle, a Casimir potential, or
a second bulk scalar — each at least +1 parameter, listed as a fork in `ledger.md`). Until one
is chosen and shown to work, every result in `02_effective_4d.md`–`04b_initial_conditions.md`
that used $M_5^3 = \pi\ell_z M_6^4$ with constant $\ell_z$ carries this **[verify]**. This is
the concrete form of "some constants may still be settling": the action contains exactly one
candidate for a settling constant — $\alpha$ via $\ell_z$ — and the data say it settled to
better than $10^{-5}$ before $z \sim 3$ and to $10^{-17}\,\mathrm{yr}^{-1}$ now. Any
"still-settling" claim must be a claim about this modulus, and it must be that small.

## 7. Generic vs BMI-specific

| item | generic braneworld | BMI-specific |
|---|---|---|
| Birkhoff bulk, moving branes, $H^2$ with $\pm\rho$ | yes (Kraus; Ida; BDL; BCG) | — |
| $\Omega_\infty^{n-1} = (\epsilon-f)/(1+\epsilon)$ | follows for any RS1-type pair with radiation | the $n=4$ exponent and the identification with the mirror-sector energy |
| $\epsilon \ge f$ as an $N_{\text{eff}}$ doubling | yes | consequence for the mirror-DM scan |
| circle modulus unstabilized | any 6D warped-circle model | the BMI action has no stabilizer |

## 8. What is derived, what is not

Derived: §1–§4 for $h \lesssim 1$, isotropic branes. Not derived: the matching *through*
$\Omega = 1$ (still not attempted — the solution above starts at coincidence with
$(f, \epsilon, h)$ as data); the anisotropic (3+1, fixed circle) two-brane solution — no exact
bulk is known, and the moduli approximation of `03_background.md` remains the only tool
there; the relation between $(f, \epsilon)$ and any pre-collision state. The pre-collision
layer is stated as a hypothesis in `00_axiom.md` §"Pre-action layer" and is not used here.
