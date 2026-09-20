# v2 status — after milestone 4

One page. What is fixed, what is derived, what is still open, what could kill it next.
Details and derivations live in the numbered files; this only points.

## 1. The Lagrangian (fixed, `01_action.md` §2)

$$
S = \int d^6X \sqrt{-G}\left[\tfrac{M_6^4}{2} R_6 - \Lambda_6 - \tfrac12 (\partial\Phi)^2 - V(\Phi)\right]
+ \sum_{i=1,2} \int_{\Sigma_i} d^5\xi \sqrt{-\gamma_i}\left[-\sigma_i + \mathcal L_{\text{matter},i}\right]
+ M_6^4 \sum_i \int_{\Sigma_i} [K_i],
\qquad
V(\Phi) = V_0\, e^{-c\,\Phi/M_6^2}.
$$

Matter on $\Sigma_1$ = Standard Model, on $\Sigma_2$ = mirror Standard Model **[choice]**. No free
functions. Nothing in milestone 3 changed this action; milestone 3 changed the *solution* of it
(background metric, §3 below). A "revised Lagrangian" is therefore not needed — what is still
missing is its *effective 4D form* (§4).

## 2. Parameter budget (7, `ledger.md`)

$M_5,\ \ell,\ \phi_0,\ \sigma_2,\ V_0,\ c,\ T_2/T_1$. Balance $0 - 7 = -7$: no un-fitted
number has been predicted yet. One integration constant ($\mathcal C$, dark radiation) is
pending; it becomes #8 if milestone 5 cannot compute it.

## 3. Derived so far (`02_effective_4d.md`)

| item | status |
|---|---|
| background metric $ds^2 = e^{-2y/\ell}(\eta_{\mu\nu}dx^\mu dx^\nu + dz^2) + dy^2$, $\ell^{-2} = -\Lambda_6/10M_6^4$ | verified symbolically (`tests/check_background.py`) |
| brane tensions $\sigma_1 = 8M_6^4/\ell = -\sigma_2$ | verified |
| $M_{Pl}^2(\phi) = \tfrac13 M_5^3 \ell\,(1 - e^{-3\phi/\ell})$ | verified |
| $\dot G/G \approx -(3\dot\phi/\ell)\,e^{-3\phi/\ell}$ | derived; $\lesssim 3\times10^{-16}\,\mathrm{yr}^{-1}$ once the DM-mass drift bound is imposed — **kill criterion 2 passed** |
| brane field equation $G_{\mu\nu} = 8\pi G_N T_{\mu\nu} + (8\pi G_N/\sigma_1)\hat\pi_{\mu\nu} - E_{\mu\nu} + \Theta_{\mu\nu}$ | structure derived; $D=6$ coefficients of $\hat\pi$ **[verify]** |
| GR + ΛCDM recovered for $\dot\phi \to 0$, low energy | yes — **kill criterion 1 passed** |
| Brans–Dicke $\omega = \tfrac43(e^{3\phi/\ell}-1)$; Cassini: $\phi_0/\ell \gtrsim 3.4$, $\Omega_0 \lesssim 0.032$ | derived in 6D (`03_background.md` §1, `tests/check_radion.py`) |
| radion $K(\phi) = 12M_{Pl}^2\Omega^3/\ell^2$, canonical $\chi \propto \Omega^{3/2}$, $\epsilon_\chi = 2/3\Omega^3$ | derived: the radion never slow-rolls |
| bulk scalar: no static profile; rolling zero mode is canonical quintessence $V_* e^{-c\Phi_4/M_{Pl}}$ with slope exactly $c$ | derived (`03_background.md` §2) |
| thawing $w(z)$ family in $c$; $w>-1$, $w_a<0$; $w_a \approx -1.5(1+w_0)$ | computed (`tests/background_frw.py`) |

Two errors in `01_action.md` were found and corrected in place (unwarped circle was not a
vacuum solution; $M_{Pl}$ exponent was the 5D one). Both are recorded in `02_effective_4d.md` §0.

## 4. The effective 4D Lagrangian (now closed, `03_background.md`)

$$
S_{\text{eff}} = \int d^4x\sqrt{-g}\left[\tfrac{M_{Pl}^2(\phi)}{2}R - \tfrac{K(\phi)}{2}(\partial\phi)^2 - \delta\sigma_2^{(5)}\Omega^4
 - \tfrac12(\partial\Phi_4)^2 - V_* e^{-c\Phi_4/M_{Pl}}\right] + S_{SM}[g] + S_{\text{mirror}}[\Omega^2 g]
$$

with $M_{Pl}^2(\phi) = \tfrac13 M_5^3\ell(1-\Omega^3)$, $K = 12M_{Pl}^2\Omega^3/\ell^2$,
$V_* = \pi\ell_z\ell V_0/5$, $\Omega = e^{-\phi/\ell}$. Two scalars, not one: the radion $\phi$
(merger) and the bulk scalar $\Phi_4$ (dark energy). Still outside it: $E_{\mu\nu} = \mathcal C/a^4$
(milestone 5) and the order-$\ell^2 R^2$ corrections.

**Background result.** The CMB bound on mirror-DM mass drift forces the radion's energy
fraction today to $f_{\text{rad}} < 5\times10^{-6}$: the merger is a spectator, dark energy is
the bulk scalar alone, and "dark energy = inter-brane potential" (v1 Ch 7.4) is dead
(`03_background.md` §4).

## 5. Forced consequence found (the first real kill risk)

$\Sigma_2$ sits at the IR end of the warp, so every mirror-sector mass is
$\Omega\, m$ with $\Omega = e^{-\phi/\ell} \lesssim 0.032$:

- mirror proton $\lesssim 30$ MeV, mirror electron $\lesssim 16$ keV;
- $\Omega_{DM}/\Omega_b = 5.3$ then requires $n_2/n_1 \gtrsim 165$ — the impact must
  deposit far more baryon number on $\Sigma_2$ than on $\Sigma_1$;
- DM masses drift with $\phi(t)$; CMB requires $|\Delta\phi| \lesssim 0.03\,\ell$ since
  recombination, i.e. the merger is essentially stalled over the last 13.8 Gyr —
  milestone 4 shows the action *can* satisfy this (radion spectator, §4) but it does not
  *predict* it: $|\delta\sigma_2|$ small enough is a condition on parameter #4.

This is not generic mirror-matter phenomenology; it is what BMI + Fork 1 forces. Milestone 5
must produce $n_2/n_1 \gtrsim 165$ with $T_2/T_1 \lesssim 0.45$ from the impact, or the
mirror-SM choice for $\Sigma_2$ dies and the fallback (higher-dimensional $\Sigma_2$, +1
parameter) is taken.

## 5b. Field content from geometry (`02b_localization.md`)

Forced by the AdS$_6$ background plus the SM's own consistency: gravity/radion/scalars on
$\Sigma_1$; $z \in S^1/\mathbb Z_2$ (chirality); SM gauge fields and charged fermions on
$\Sigma_1$ (a bulk gauge field would charge the mirror sector); only gauge singlets may be
bulk fields; $z$-excitations are heavy and ours, $y$-excitations are light by $\Omega$ and
theirs. **Not forced:** the bulk mass $c$ of a bulk fermion — one dial per species, not
admitted; the only clean option is a universal $c$ (would be parameter #8).

## 6. Kill criteria (`01_action.md` §5)

| # | criterion | status |
|---|---|---|
| 1 | GR + ΛCDM in frozen limit | **passed** (milestone 3) |
| 2 | $\dot G/G$ vs LLR | **passed** (milestone 4): $\lesssim 3\times10^{-16}\,\mathrm{yr}^{-1}$ |
| 3 | $w(z)$ vs DESI | **open**: thawing curve, $w>-1$; Planck constant-$w$ needs $c\lesssim0.5$; DESI DR2 central value (phantom) unreachable — chain-level test in milestone 7 |
| 4 | $\Delta N_{\text{eff}}$, $T_2/T_1$ vs BBN/Planck | milestone 5 |
| 5 | $\Omega_{DM}/\Omega_b$, $\sigma/m$ | milestone 6, now with §5 above as the hard part |

## 7. Generic vs BMI-specific (honest split)

Everything in §3 is standard two-brane Randall–Sundrum physics in one more dimension plus
standard exponential quintessence; it earns BMI nothing except consistency. BMI-specific
content so far: the slope of dark energy is the bulk-potential parameter $c$ with no geometric
factor; the radion bound comes from *DM mass drift*; $n_2/n_1 \gtrsim 165$ inverted density
ratio. Not yet computed: $T_2/T_1$, $n_2/n_1$, $\mathcal C$ from the impact; the low-$\ell$ CMB axis.

## 8. Repo state

- PR #1 (freeze v1, retractions, ledger CI) → PR #2 (action) → PR #3 (effective theory) → PR #4 (localization) → PR #5 (background), stacked.
- CI: `tests/check_ledger.py` (undeclared symbols fail the build), `tests/check_background.py` (sympy, background identities), `tests/check_zero_modes.py` (zero-mode profiles per spin), `tests/check_radion.py` (moduli action, quintessence slope), `tests/background_frw.py` (FRW numbers).
- Next: milestone 5 — the impact: $T_2/T_1$, $n_2/n_1$, $\mathcal C$, $\delta\sigma_2$ sign, $(n_s, r)$.
