# v2 status — after milestone 3

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
| $\dot G/G \approx -(3\dot\phi/\ell)\,e^{-3\phi/\ell}$ | derived; passes LLR by $\sim 10^4$ for $\phi_0/\ell = 5$ |
| brane field equation $G_{\mu\nu} = 8\pi G_N T_{\mu\nu} + (8\pi G_N/\sigma_1)\hat\pi_{\mu\nu} - E_{\mu\nu} + \Theta_{\mu\nu}$ | structure derived; $D=6$ coefficients of $\hat\pi$ **[verify]** |
| GR + ΛCDM recovered for $\dot\phi \to 0$, low energy | yes — **kill criterion 1 passed** |
| Cassini bound: $\phi_0/\ell \gtrsim 5$ | first data-derived constraint (uses 5D Brans–Dicke prefactor, **[verify]** in 6D) |

Two errors in `01_action.md` were found and corrected in place (unwarped circle was not a
vacuum solution; $M_{Pl}$ exponent was the 5D one). Both are recorded in `02_effective_4d.md` §0.

## 4. Not yet derived — what "effective Lagrangian" still needs

$$
S_{\text{eff}} = \int d^4x\sqrt{-g}\left[\tfrac{M_{Pl}^2(\phi)}{2}R - \tfrac{K(\phi)}{2}(\partial\phi)^2 - V_{\text{eff}}(\phi)\right] + S_{SM}[g] + S_{\text{mirror}}[\Omega^2 g]
$$

- $M_{Pl}^2(\phi)$: done.
- $K(\phi)$ (radion kinetic factor): 5D result known, 6D **[verify]**.
- $V_{\text{eff}}(\phi) = \Omega^4\delta\sigma_2 + 2\pi\ell_z\int_0^\phi dy\, e^{-5y/\ell} V(\Phi(y))$: needs the
  bulk profile $\Phi(y)$, which needs the coupled $\Phi$–metric background to be solved
  (the pure-AdS$_6$ background above assumes $V(\Phi)$ is a small perturbation — to be checked).
- $E_{\mu\nu}$: homogeneous part is $\mathcal C/a^4$; $\mathcal C$ needs the impact state.

These are milestone 4.

## 5. Forced consequence found (the first real kill risk)

$\Sigma_2$ sits at the IR end of the warp, so every mirror-sector mass is
$\Omega\, m$ with $\Omega = e^{-\phi/\ell} \lesssim 7\times10^{-3}$:

- mirror proton $\lesssim 6$ MeV, mirror electron $\lesssim 3.5$ keV;
- $\Omega_{DM}/\Omega_b = 5.3$ then requires $n_2/n_1 \gtrsim 750$ — the impact must
  deposit far more baryon number on $\Sigma_2$ than on $\Sigma_1$;
- DM masses drift with $\phi(t)$; CMB requires $|\Delta\phi| \lesssim 0.03\,\ell$ since
  recombination, i.e. the merger is essentially stalled over the last 13.8 Gyr.

This is not generic mirror-matter phenomenology; it is what BMI + Fork 1 forces. Milestone 4
must either produce $n_2/n_1$ and a stalled $\phi(t)$ from the action, or the mirror-SM
choice for $\Sigma_2$ dies and the fallback (higher-dimensional $\Sigma_2$, +1 parameter) is
taken.

## 6. Kill criteria (`01_action.md` §5)

| # | criterion | status |
|---|---|---|
| 1 | GR + ΛCDM in frozen limit | **passed** (milestone 3) |
| 2 | $\dot G/G$ vs LLR | passes for $\phi_0/\ell \gtrsim 5$; $\dot\phi$ not yet derived |
| 3 | $w(z)$ vs DESI | milestone 4 |
| 4 | $\Delta N_{\text{eff}}$, $T_2/T_1$ vs BBN/Planck | milestone 5 |
| 5 | $\Omega_{DM}/\Omega_b$, $\sigma/m$ | milestone 6, now with §5 above as the hard part |

## 7. Generic vs BMI-specific (honest split)

Everything in §3 is standard two-brane Randall–Sundrum physics in one more dimension; it
earns BMI nothing except consistency. BMI-specific content, none of it yet computed:
$T_2/T_1$ and $n_2/n_1$ from the impact, $\mathcal C$ from the impact, $\phi(t)$ and hence
$w(z)$ and the DM mass drift, and any preferred direction in the low-$\ell$ CMB.

## 8. Repo state

- PR #1 (freeze v1, retractions, ledger CI) → PR #2 (action) → PR #3 (effective theory), stacked, all CI green.
- CI: `tests/check_ledger.py` (undeclared symbols fail the build), `tests/check_background.py` (sympy, background identities).
- Next: milestone 4 — solve $\Phi(y)$, $V_{\text{eff}}$, then $a(t), \phi(t)$; compute $w_0, w_a$, $\Delta N_{\text{eff}}$, DM mass drift.
