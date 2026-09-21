# 06 — Predictions: what the nine numbers say that they were not fitted to

Milestone 7. The ledger's rule is that only an un-fitted number, confirmed, moves the balance.
Nine parameters can still predict if they control more than nine observables. This file lists
every candidate relation found in `02`–`05`, states whether it *closes* (no leftover parameter)
or *leaks*, computes the closed ones to a number, and confronts them with the data that exist
today. Numbers: `tests/predictions.py`. Registered 2026-09-21, before the comparison in §4.

| result | status |
|---|---|
| canonical circle modulus from the 6D Einstein–Hilbert term: $\chi = \sqrt{3/2}\,M_{Pl}\ln(\ell_z/\bar\ell_z)$; `04d`/`05` used the coefficient 1 → $m_\chi$ and $\lambda^{-1}$ shrink by $\sqrt{2/3}$ | derived (§1) |
| coupling to nucleons: $d\ln m_N/d\ln\ell_z = -\tfrac12 - 1 - 2\pi/(b_0\alpha_s(\ell_z^{-1})) \approx -14$; the QCD piece dominates | derived (§2; cutoff identification and thresholds [verify]) |
| **P1 revised**: $\alpha_Y = 2\beta^2 \approx 2.5\times10^2$, not order one; the fifth force is $\sim\!250\times$ gravity, composition-independent to $10^{-3}$ | derived (§2) |
| existing $\alpha$–$\lambda$ limits at $\alpha_Y \approx 250$ cut the range from the long side: $\lambda < 12\,\mu$m, i.e. $\ell_z^{-1} > 14$ TeV | compared (§4a; digitized bounds [verify]) |
| P1 window now $14 < \ell_z^{-1}/\mathrm{TeV} < 29$ ⇔ $2.8 < \lambda/\mu\mathrm m < 12$ at $\alpha_Y = 270$–$300$ | one-parameter *curve* in the $(\alpha,\lambda)$ plane, half a decade long, both ends set by the action |
| **P2**: dark energy is thawing with $w_a/(1+w_0) = -1.5$ ($-1.56$ at small $c$, $-1.15$ at $c=1.8$), $w>-1$ always | derived (`03_background.md`), registered here as a prediction |
| DESI DR2 + CMB + SNe (Gaussian proxy of the $(w_0,w_a)$ posteriors): the curve's nearest point is $\Delta\chi^2 = 6.5$–$12.7$ from the best fit for the three SNe samples — outside $2\sigma$, always closer than ΛCDM by $2$–$10$ | compared (§4b; proxy, not chains [verify]) |
| Cassini ↔ $N_{\text{eff}}$ ($\Omega_\infty^3 = (\epsilon-f)/(1+\epsilon)$): leaks — the CMB sees $\epsilon + f$ only | bound, not prediction (§3) |
| $\dot G/G$ ↔ $w(z)$: different fields (radion vs $\Phi_4$) | no relation (§3) |
| GW vs EM luminosity distance: $M_{Pl}$ constant to $10^{-5}$ since recombination ⇒ ratio $= 1 \pm 10^{-5}$ | trivial null (§3) |
| low-$\ell$ CMB preferred axis (the v1 signature) | **not computed**: the action has no primordial spectrum (`04_impact.md` §6), so there is nothing to be anisotropic |
| **ledger balance**: still $0 - 9$. Two sharp, dated, un-fitted predictions exist; neither is confirmed | §5 |

## 1. The canonical circle modulus

The wrapped brane at $y=0$ is five-dimensional with $z \in S^1$ of circumference $2\pi\ell_z$;
the 4D Planck mass comes from the 5D Einstein–Hilbert term integrated over $z$ (`01_action.md`
§3, $M_5^3 = \pi\ell_z M_6^4$). Let the circle breathe, $\ell_z \to \ell_z e^{\sigma(x)}$, and write
the brane metric in the frame where the 4D Planck mass is constant:

$$
ds^2 = e^{-\sigma}\, g_{\mu\nu}dx^\mu dx^\nu + e^{2\sigma} dz^2 .
$$

Reducing $\tfrac{M_5^3}{2}\int d^5\xi\sqrt{-\gamma}\,R_5$ on this ansatz gives the standard
Kaluza–Klein result

$$
S \supset \int d^4x\sqrt{-g}\;\frac{M_{Pl}^2}{2}\Big[R - \tfrac32 (\partial\sigma)^2\Big],
\qquad
\chi \equiv \sqrt{\tfrac32}\,M_{Pl}\,\sigma ,
$$

so the canonically normalised modulus is $\chi = \sqrt{3/2}\,M_{Pl}\ln(\ell_z/\bar\ell_z)$, not
$M_{Pl}\ln\ell_z$. Consequences for what was already written: with $V(\ell_z)$ of `04d` §3,
$m_\chi^2 = V''(\sigma)/(\tfrac32 M_{Pl}^2) = 20 C_z/(\tfrac32\,\bar\ell_z^4 M_{Pl}^2)$; $m_\chi$ and
$\lambda^{-1}$ are $0.82\times$ the `04d`/`05` values, $T_o \propto \sqrt{m_\chi}$ is $0.90\times$,
and the required $\delta_z$ of `05` §2 shifts by the same order. None of the qualitative
statements of `04d`/`05` change; the numbers there carry an implicit $\sqrt{2/3}$ from here on.
Mixing with the radion is absent at quadratic order (the Casimir term lives at $y=0$ and
$M_{Pl}^2 \propto \ell_z(1-\Omega^3)$ factorises); mixing with $\Phi_4$ enters only through
$V_* \propto \ell_z$ and is suppressed by $\rho_{DE}/V_z \sim 10^{-60}$.

## 2. The coupling to matter

In the frame above, a brane field of Jordan-frame mass $m_J$ has Einstein-frame mass
$m = e^{-\sigma/2} m_J$: the Weyl factor gives $d\ln m/d\sigma = -\tfrac12$ for *every* brane
species. On top of that the nucleon mass is $\approx \Lambda_{QCD}$, and $\Lambda_{QCD}$ depends
on $\ell_z$ through the gauge kinetic term, $1/g_4^2 = 2\pi\ell_z/g_5^2$ (`04d` §1):

$$
\Lambda_{QCD} = \mu_{KK}\,\exp\!\Big(-\frac{2\pi}{b_0\,\alpha_s(\mu_{KK})}\Big),
\qquad \mu_{KK} = \ell_z^{-1},\quad \frac{1}{\alpha_s(\mu_{KK})} \propto \ell_z ,
$$

so $d\ln\Lambda_{QCD}/d\ln\ell_z = -1 - 2\pi/(b_0\alpha_s(\ell_z^{-1}))$ with $b_0 = 7$ above $m_t$
($\alpha_s(10\ \mathrm{TeV}) = 0.073$ at one loop from $\alpha_s(M_Z) = 0.118$). The identification
of the matching scale with $\ell_z^{-1}$ up to an order-one factor, and threshold corrections, are
[verify]; they shift the QCD term by $\lesssim 10\%$. Quark-mass and Higgs-vev contributions to
$m_N$ ($\lesssim 10\%$ of $m_N$, and their own $\ell_z$-dependence through $y_4 \propto \ell_z^{-1/2}$)
are dropped at the same level [verify]. Altogether, at $\ell_z^{-1} = 10$ TeV,

$$
\frac{d\ln m_N}{d\sigma} = -\tfrac12 - 1 - 12.4 = -13.9,
\qquad
\beta \equiv M_{Pl}\frac{d\ln m_N}{d\chi} = \frac{-13.9}{\sqrt{3/2}} = -11.3,
\qquad
\alpha_Y = 2\beta^2 = 2.6\times10^2 .
$$

The Yukawa potential between two bodies is $V = -\alpha_Y G m_1 m_2\,e^{-r/\lambda}/r$ with
$\lambda = m_\chi^{-1}$ (reduced-Planck convention, $\alpha_Y = 2\beta^2$). The `04d` guess
"$\alpha_Y$ of order one" was the Weyl piece alone; the QCD running multiplies it by $\sim 10^2$.
Composition dependence: the electromagnetic binding-energy fraction of $m_N$ carries
$d\ln\alpha/d\ln\ell_z = -1$, contributing $\sim 10^{-3}$ of $\beta$ — so P1 is *composition-
independent* at the $10^{-3}$ level, not the composition-dependent force `04d` advertised (that
statement is corrected here). Equivalence-principle tests at $\lambda \sim 10\,\mu$m do not
reach a differential acceleration of $10^{-3}\alpha_Y\,e^{-r/\lambda}$ for laboratory separations; the handle is the
inverse-square-law test.

## 3. Relations that do not close

- **Cassini ↔ $N_{\text{eff}}$.** `04c` gives $\Omega_\infty^3 = (\epsilon - f)/(1+\epsilon)$, so the
  post-Newtonian $\gamma - 1 \propto \Omega_0^3$ is fixed by two collision data. Dark radiation
  and the mirror sector both enter $N_{\text{eff}}$ as $\epsilon + f$; the difference is
  unobservable. Only "$\Delta N_{\text{eff}}$ at least twice the mirror sector's" survives —
  a bound.
- **$\dot G/G$ ↔ $w(z)$.** $\dot G/G$ is the radion ($\phi$), $w(z)$ is the bulk scalar
  ($\Phi_4$); the effective Lagrangian of `03` §2 has no cross term between them at the level of
  the background. The `README` milestone-7 deliverable "joint $(\dot G/G, w_a)$" is therefore
  empty and is dropped, not filled.
- **GW vs EM luminosity distance.** The GW luminosity distance differs from the EM one by
  the ratio of $M_{Pl}$ at emission to $M_{Pl}$ today; the DM-mass-drift bound already forces this to
  $1 \pm 5\times10^{-6}$ (`03` §3.1). LISA/ET reach $10^{-2}$: a null that cannot be tested.
- **Preferred axis in the low-$\ell$ CMB.** v1's signature. The action produces no primordial
  spectrum (`04_impact.md` §6, $r \ge 0.28$ if it did), so it cannot produce an anisotropic one.
  Not computed, and not computable until the collision matching exists.

## 4. Confrontation with data

### 4a. P1 against the inverse-square-law limits

$\alpha_Y(\ell_z)$ is nearly flat ($230$–$300$ over the window; the log running of $\alpha_s$), and
$\lambda = m_\chi^{-1} = 23.5\,\mu\mathrm m\,(10\ \mathrm{TeV}\,\ell_z)^2$. The published 95% limits
on $|\alpha|$ at fixed $\lambda$ (Lee et al. 2020, Fig. 3, compiling Eöt-Wash 2007/2020, Stanford,
IUPUI 2016; only the point $\alpha = 1$ at $\lambda = 38.6\,\mu$m is quoted numerically, the rest are
read off the figure [verify]) are crossed at

$$
\alpha_Y = 2.7\times10^2 \;\;\Rightarrow\;\; \lambda < 11.7\,\mu\mathrm m \;\;\Leftrightarrow\;\; \ell_z^{-1} > 14.2\ \mathrm{TeV}.
$$

The upper edge $\ell_z^{-1} < 29$ TeV ($|\delta_1| < \sigma_1$) is unchanged, so

$$
14\ \mathrm{TeV} < \ell_z^{-1} < 29\ \mathrm{TeV},
\qquad
2.8\,\mu\mathrm m < \lambda < 12\,\mu\mathrm m,
\qquad
\alpha_Y = 270\text{–}300 .
$$

What changed: `04d` had a 1.5-decade window in $\lambda$ at an unspecified strength. Now the
theory occupies a *line segment* in the $(\alpha,\lambda)$ plane: strength fixed to $\sim\!30\%$
by the action, range within half a decade. The current limits sit a factor $2$ (at $12\,\mu$m)
to $10^3$ (at $3\,\mu$m) above the segment; the Eöt-Wash 2020 result already removed the
lower half of `04d`'s $\ell_z$ range. A detection *on* the segment confirms P1 and moves the
balance to $+1$; a detection *off* it (any $\alpha$ outside $\sim[10^2, 4\times10^2]$ at the
detected range, or a range outside $2.8$–$12\,\mu$m) kills the fixed-circle geometry as surely
as a null result down to $\alpha \sim 10^2$ at $3\,\mu$m does. The lower edge is also where
the LHC KK bound ($\ell_z^{-1} \gtrsim 5$ TeV) is now irrelevant: the fifth-force limit is the
stronger one by a factor of three.

### 4b. P2 against DESI DR2

DESI DR2 BAO + CMB + SNe (arXiv:2503.14738, eqs. 26–28) give, in CPL,
$(w_0, w_a) = (-0.838\pm0.055,\ -0.62^{+0.22}_{-0.19})$ [Pantheon+],
$(-0.667\pm0.088,\ -1.09^{+0.31}_{-0.27})$ [Union3], $(-0.752\pm0.057,\ -0.86^{+0.23}_{-0.20})$ [DESY5].
The thawing curve fitted by CPL over $0<z<1$ has $w_a/(1+w_0) = -1.56$ at small $c$ rising to
$-1.15$ at $c = 1.8$; the data want $w_a/(1+w_0) \approx -3.5 \pm 1$, i.e. $w$ crossing $-1$ near
$z \approx 0.4$, which a canonical scalar cannot do. Approximating each posterior as a
bivariate Gaussian with correlation $\rho \in [-0.95, -0.8]$ [verify: chains], the curve's
nearest point lies at $\Delta\chi^2 = 6.5$–$8.5$ (Pantheon+), $9.0$–$12.1$ (Union3), $10.0$–$12.7$
(DESY5): outside $2\sigma$ (6.18) in every case, beyond $3\sigma$ (11.8) for Union3/DESY5 with
$\rho \le -0.9$; ΛCDM sits at $9$–$20$ in the same proxy. So the minimal canonical scalar is
in the same tension with DESI as ΛCDM is, reduced but not removed by being able to move along
$w_0 > -1$, $w_a < 0$. The nearest $c$ is $0.4$–$1.1$, compatible with the Planck constant-$w$
bound $c \lesssim 0.5$ only at the Pantheon+ end.

This is the pre-registered kill criterion 3 with the proxy in place of the chains. It does not
fire (the proxy is not the test; the CPL posterior is non-Gaussian along the degeneracy
direction), and it does not pass. If the phantom-crossing preference survives the
SNe-sample dependence and the chain-level comparison, the exponential $V(\Phi)$ dies and the
ledger's $V(\Phi)$-feature fork is the only replacement inside the action — at +1 shape choice
+1 scale, which the budget rule then has to weigh against closing the branch.

## 5. The ledger after milestone 7

Balance: **$0 - 9 = -9$**, unchanged. Milestone 7 was to move it or close the branch; it did
neither in the strict sense. What it did:

- P1 is now a *computed* prediction (strength and range from the action, no free number once
  $\ell_z$ is anywhere in its window) instead of a window at an unspecified strength; the
  existing data removed half its range and left the rest two to three orders of magnitude
  below current sensitivity at the short end and a factor $2$ at the long end.
- P2 is registered: $w_a = -1.5(1+w_0)$, $w > -1$. The current data disfavour it at the
  $2$–$3\sigma$ level in the proxy, exactly as they disfavour ΛCDM.
- Three relations that looked like predictions leak or are trivially null; the v1 low-$\ell$
  axis is not computable from this action.

A confirmation of P1 on the segment would make the balance $+1 - 9 = -8$; the honest reading
is that the theory has two dated, falsifiable statements and eight numbers that are read from
data. The rule of `ledger.md` says the branch closes. Proposal, for the decision that this
file cannot make: freeze the budget at 9 (no #10 under any circumstance), keep the two
predictions open, and stop deriving until one of them is tested — a next-generation
inverse-square-law experiment at $3$–$12\,\mu$m or the DESI DR2 chain comparison.

## 6. Generic vs BMI-specific

$\alpha_Y \approx 2\beta^2$ with $\beta$ dominated by QCD running is generic for any radius
modulus that sets $1/g^2$ (Damour–Polyakov dilaton, string moduli). BMI-specific: the range is
tied to the SM Casimir coefficient and $\delta_1$ (not to a string scale), the modulus is the
dark matter, and the same $\ell_z$ is bounded from above by $|\delta_1| < \sigma_1$ — giving
both ends of the segment from the action. The thawing relation $w_a \approx -1.5(1+w_0)$ is
generic exponential quintessence; the BMI-specific content of P2 is only that the slope is the
6D parameter $c$ with no geometric factor and that $\Phi$ cannot be the inter-brane potential.
