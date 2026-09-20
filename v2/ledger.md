# BMI v2 — Parameter Ledger (live)

Every quantity that v2 needs from outside the action is listed here. `tests/check_ledger.py`
fails CI if a symbol declared as a parameter appears in `v2/*.md` without a row in the table
below, or if the number of rows exceeds the budget.

**Budget: 7 parameters, 0 free functions.** (ΛCDM: 6. SM: 19.)

Discrete choices (not parameters), all recorded with alternatives in `01_action.md`: Fork 1
(we are the UV brane); one compact bulk direction; exponential bulk potential; mirror Standard
Model on $\Sigma_2$ (**as the dark matter: dead**, `04_impact.md` §3 — it still exists as a
subdominant sector); $\Phi$-independent tensions.

Ledger balance = (un-fitted numerical predictions confirmed) − (parameters). Update the
balance line whenever a row or a prediction changes.

## Parameters

Symbol column is the exact LaTeX macro as it appears in the manuscript, without `$`.

| # | symbol | meaning | fixed by | status |
|---|---|---|---|---|
| 1 | `M_5` | effective 5D Planck mass, $M_5^3 = \pi\ell_z M_6^4$ | $G_N$ with #2, #3 | open |
| 2 | `\ell` | bulk warp length; fixes $\Lambda_6$ and the RS-tuned $\sigma_1$ | $G_N$ with #1, #3 (the CC tuning is stated in `01_action.md` §3, not hidden) | open |
| 3 | `\phi_0` | present brane separation | $M_{Pl}^2 = \tfrac13 M_5^3 \ell (1-e^{-3\phi_0/\ell})$: one relation among #1–#3; Cassini requires $\phi_0/\ell \gtrsim 3.4$ (`03_background.md` §1); equals the image of the post-impact kinetic ratio $r_b$, which must lie within 1.5% of the overshoot value (`04_impact.md` §1, coincidence recorded) | bounded |
| 4 | `\sigma_2` | tension of $\Sigma_2$; only the detuning $\delta\sigma_2 = \sigma_2 + \sigma_1$ is physical | $\lvert\delta\sigma_2\rvert < 0.15\,\rho_0/\Omega_0$ (DM-mass drift); sign not fixed by the impact (`04_impact.md` §5) | bounded, sign open |
| 5 | `V_0` | bulk potential scale | dark-energy density today | open |
| 6 | `c` | bulk potential slope | $w_0, w_a$ **and** $\dot\phi$; one number, two observables | open |
| 7 | `T_2/T_1` | sector temperature ratio at reheating | **not derivable**: the action is $\mathbb Z_2$-symmetric at the collision, so its null value is 1, which gives $\Delta N_{\text{eff}} \approx 6$ (excluded); bounded $< 0.45$ by the CMB (`04_impact.md` §2) | bounded, null excluded |

## Pending integration constants (not parameters yet)

| symbol | meaning | must be computed in | bound now |
|---|---|---|---|
| `\mathcal C` | dark-radiation constant, $\rho_E = \mathcal C/a^4$ | **resolved, milestone 5**: driven to the fixed point $\rho_E/\rho_{\text{rad}} \to \alpha/4 \approx 5\times10^{-3}$ by bulk-graviton emission (`04_impact.md` §4); $\Delta N_{\text{eff}} \lesssim 0.03$. Not a parameter. | satisfied ×10 |
| `c_\nu` | universal bulk mass of bulk gauge singlets (`02b_localization.md` §6); only admitted as *one* number for all species | taken only if a neutrino-sector milestone is opened | none yet |
| (fork, not a symbol) | a feature in $V(\Phi)$ — bump or negative minimum — that would end acceleration via the dark-energy scalar (`03_background.md` §3.4); one shape choice + 1 scale | taken only if milestone 7 kills the pure exponential against DESI chains | — |

Milestone 5 computed `\mathcal C`; the budget stays at 7.

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
(passes LLR); $\rho^2$ Friedmann corrections only above $T_t \approx 6$ TeV for $\ell = 10\,\mu$m
(table-top $\ell$ bound); $T_2/T_1 < 0.45$ (CMB $N_{\text{eff}}$).
Forced consequence, tested and failed (`04_impact.md` §3): mirror-sector masses are $\Omega m$
with $\Omega \lesssim 0.032$, so $\Omega_{DM}/\Omega_b = 5.3$ needs $\eta_2/\eta_1 \gtrsim 1600$;
the action has no mechanism — mirror SM is not the dark matter.

## Balance

**0 − 7 = −7.** Milestone 3 passed kill criterion 1 (GR + ΛCDM recovered) without changing
the balance. Milestone 5 kept $\mathcal C$ out of the budget (computed, $\Delta N_{\text{eff}}
\lesssim 0.03$ — a confirmed un-fitted *bound*, not a confirmed prediction, so it does not
count) and closed the mirror-DM branch. Milestones 6–7 must move the balance to ≥ 0 or the
branch is closed.
