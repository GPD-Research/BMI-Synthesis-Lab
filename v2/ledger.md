# BMI v2 — Parameter Ledger (live)

Every quantity that v2 needs from outside the action is listed here. `tests/check_ledger.py`
fails CI if a symbol declared as a parameter appears in `v2/*.md` without a row in the table
below, or if the number of rows exceeds the budget.

**Budget: 8 parameters, 0 free functions.** (ΛCDM: 6. SM: 19.)

Ledger balance = (un-fitted numerical predictions confirmed) − (parameters). Update the
balance line whenever a row or a prediction changes.

## Parameters

Symbol column is the exact LaTeX macro as it appears in the manuscript, without `$`.

| # | symbol | meaning | fixed by | status |
|---|---|---|---|---|
| 1 | `M_6` | 6D Planck mass | $G_N$ and warp factor at $\Sigma_1$ | open |
| 2 | `\phi_0` | present brane separation | tied to #1 via $M_{Pl}^2 \sim M_6^4 \ell (1-e^{-2\phi_0/\ell})$ | open |
| 3 | `\sigma_1` | tension of $\Sigma_1$ | RS-type tuning against $\Lambda_6$ (the CC problem, stated not hidden) | open |
| 4 | `\sigma_2` | tension of $\Sigma_2$ | candidate for $\Omega_{DM}/\Omega_b$ | open |
| 5 | `V_0` | bulk potential scale | dark-energy density today | open |
| 6 | `c` | bulk potential slope | $w_0, w_a$ **and** $\dot\phi$; one number, two observables | open |
| 7 | `T_2/T_1` | sector temperature ratio at reheating | **target: derived from impact kinematics, not fit** | open |
| 8 | `w_2` | equation of state of sector-2 matter (or `0` if mirror SM) | sector-2 content choice | open |

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

**0 − 8 = −8.** Milestones 3–6 must move this to ≥ 0 or the branch is closed.
