# BMI v2 — Parameter Ledger (live)

Every quantity that v2 needs from outside the action is listed here. `tests/check_ledger.py`
fails CI if a symbol declared as a parameter appears in `v2/*.md` without a row in the table
below, or if the number of rows exceeds the budget.

**Budget: 7 parameters, 0 free functions.** (ΛCDM: 6. SM: 19.)

Discrete choices (not parameters), all recorded with alternatives in `01_action.md`: Fork 1
(we are the UV brane); one compact bulk direction; exponential bulk potential; mirror Standard
Model on $\Sigma_2$; $\Phi$-independent tensions.

Ledger balance = (un-fitted numerical predictions confirmed) − (parameters). Update the
balance line whenever a row or a prediction changes.

## Parameters

Symbol column is the exact LaTeX macro as it appears in the manuscript, without `$`.

| # | symbol | meaning | fixed by | status |
|---|---|---|---|---|
| 1 | `M_5` | effective 5D Planck mass, $M_5^3 = \pi\ell_z M_6^4$ | $G_N$ with #2, #3 | open |
| 2 | `\ell` | bulk warp length; fixes $\Lambda_6$ and the RS-tuned $\sigma_1$ | $G_N$ with #1, #3 (the CC tuning is stated in `01_action.md` §3, not hidden) | open |
| 3 | `\phi_0` | present brane separation | $M_{Pl}^2 = \tfrac13 M_5^3 \ell (1-e^{-3\phi_0/\ell})$: one relation among #1–#3; Cassini requires $\phi_0/\ell \gtrsim 3.4$ (`03_background.md` §1) | bounded |
| 4 | `\sigma_2` | tension of $\Sigma_2$; only the detuning $\delta\sigma_2 = \sigma_2 + \sigma_1$ is physical | candidate for $\Omega_{DM}/\Omega_b$ | open |
| 5 | `V_0` | bulk potential scale | dark-energy density today | open |
| 6 | `c` | bulk potential slope | $w_0, w_a$ **and** $\dot\phi$; one number, two observables | open |
| 7 | `T_2/T_1` | sector temperature ratio at reheating | **target: derived from impact kinematics, not fit** | open |

## Pending integration constants (not parameters yet)

| symbol | meaning | must be computed in | bound now |
|---|---|---|---|
| `\mathcal C` | dark-radiation constant, $\rho_E = \mathcal C/a^4$ from the projected Weyl tensor | milestone 5 (impact) | $\Delta N_{\text{eff}} \lesssim 0.3$ |
| `c_\nu` | universal bulk mass of bulk gauge singlets (`02b_localization.md` §6); only admitted as *one* number for all species | taken only if a neutrino-sector milestone is opened | none yet |

If milestone 5 cannot compute `\mathcal C`, it becomes parameter #8 and the budget line above is
raised, with a note here saying why.

## Borrowed (not counted, not derived)

$G_N$, $\hbar$, $c$, ΛCDM's six parameters, the Standard Model on $\Sigma_1$.

## Symbols exempt from the check

Coordinates, indices, fields and derived quantities are not parameters. The check-script
allowlist lives in `tests/ledger_allowlist.txt`; add to it only for fields and derived
quantities, never for a new constant.

## Predictions (un-fitted, pre-registered)

| # | quantity | predicted value | data | status |
|---|---|---|---|---|
| — | — | — | — | none yet |

Constraints derived so far (not predictions; they use data to bound the ledger):
$\phi_0/\ell \gtrsim 3.4$ (Cassini); $|\dot G/G| \lesssim 3\times10^{-16}\,\mathrm{yr}^{-1}$ forced by the DM-mass drift bound (`03_background.md` §3.1)
(passes LLR); $\rho^2$ Friedmann corrections only above $T \sim 15$ TeV (table-top $\ell$ bound).
Forced consequence awaiting test: mirror-sector masses are $\Omega m$ with $\Omega \lesssim 0.032$,
requiring $n_2/n_1 \gtrsim 165$ for $\Omega_{DM}/\Omega_b = 5.3$ (`02_effective_4d.md` §5).

## Balance

**0 − 7 = −7.** Milestone 3 passed kill criterion 1 (GR + ΛCDM recovered) without changing
the balance; milestones 4–6 must move it to ≥ 0 or the branch is closed.
