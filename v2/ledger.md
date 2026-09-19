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
| 1 | `M_5` | effective 5D Planck mass, $M_5^3 = 2\pi\ell_z M_6^4$ | $G_N$ with #2, #3 | open |
| 2 | `\ell` | bulk warp length; fixes $\Lambda_6$ and the RS-tuned $\sigma_1$ | $G_N$ with #1, #3 (the CC tuning is stated in `01_action.md` §3, not hidden) | open |
| 3 | `\phi_0` | present brane separation | $M_{Pl}^2 = M_5^3 \ell (1-e^{-2\phi_0/\ell})$: one relation among #1–#3 | open |
| 4 | `\sigma_2` | tension of $\Sigma_2$; only the detuning $\delta\sigma_2 = \sigma_2 + \sigma_1$ is physical | candidate for $\Omega_{DM}/\Omega_b$ | open |
| 5 | `V_0` | bulk potential scale | dark-energy density today | open |
| 6 | `c` | bulk potential slope | $w_0, w_a$ **and** $\dot\phi$; one number, two observables | open |
| 7 | `T_2/T_1` | sector temperature ratio at reheating | **target: derived from impact kinematics, not fit** | open |

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

## Balance

**0 − 7 = −7.** Milestones 3–6 must move this to ≥ 0 or the branch is closed.
