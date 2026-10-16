# BMI v2 benchmark task: fifth-force strength α_Y beyond one loop

**Purpose.** Close the `[verify]` on P1's strength in `v2/06_predictions.md` §2. This is permitted under the frozen budget (`v2/ledger.md`: closing `[verify]` items, no new symbols). The IDE runs it first; Devin then solves it independently; the two sets of `RESULT:` lines are compared.

**Rules for the solver.**

- Do **not** edit anything under `v2/` or `tests/`. Write the tool to `.scratch/alpha_y_running.py` and the report to `.scratch/alpha_y_report.md`.
- Python 3 with numpy/scipy only. Deterministic, no randomness, no network.
- Reuse the repo: import `range_um`, `alpha_bound`, `alpha_yukawa` (one-loop) from `tests/predictions.py` rather than retyping them.
- No new parameters. Every input below is either a Standard-Model datum or already in the repo.
- Every reported number is printed by the script as one line `RESULT: name=value±err` (dimensionless unless a unit is in the name). Numbers in the report must be copied from those lines, not computed by hand.

---

## Paste-in prompt for the IDE

> Read `v2/06_predictions.md` §1–§2 and §4a, `tests/predictions.py`, and `.scratch/alpha_y_task.md` (this file). Then build `.scratch/alpha_y_running.py` exactly as specified in §2–§4, run it, and write `.scratch/alpha_y_report.md` containing every `RESULT:` line the script prints, plus a short verdict. Do not edit `v2/` or `tests/`. Do not report a number that the script did not print.

---

## 1. What the repo currently says

`v2/06_predictions.md` §2, at $\ell_z^{-1} = 10$ TeV:

$$
\frac{d\ln m_N}{d\sigma} = -\tfrac12 - 1 - \frac{2\pi}{b_0\,\alpha_s(\ell_z^{-1})} = -13.9,
\qquad \beta = \frac{-13.9}{\sqrt{3/2}},
\qquad \alpha_Y = 2\beta^2 \approx 2.6\times10^2
$$

with $\sigma = \ln(\ell_z/\bar\ell_z)$, one-loop running, $b_0 = 7$, and $m_N \propto \Lambda_{QCD}$. It marks as `[verify]`: the matching scale ($\ell_z^{-1}$ up to an O(1) factor), the quark thresholds, and the quark-mass contributions to $m_N$ (dropped).

## 2. The physics to implement (fixed; do not change it)

Vary the circle, $\ell_z \to \bar\ell_z e^{\sigma}$, holding the 5D couplings fixed. At the reference $\bar\ell_z$ the Standard Model is reproduced exactly.

**(a) Weyl factor.** Every brane mass in the Einstein frame is $m = e^{-\sigma/2} m_J$. This adds $-\tfrac12$ to $d\ln m_N/d\sigma$, once.

**(b) Gauge coupling at the matching scale.** The matching scale is $\mu_{KK} = k/\ell_z$ (default $k = 1$) and

$$
\frac{1}{\alpha_s(\mu_{KK})} \propto \ell_z
\quad\Longrightarrow\quad
\frac{1}{\alpha_s(\mu_{KK}(\sigma))} = \frac{e^{\sigma}}{\alpha_s^{SM}(\bar\mu_{KK})},
\qquad \mu_{KK}(\sigma) = \bar\mu_{KK}\, e^{-\sigma}
$$

where $\alpha_s^{SM}(\bar\mu_{KK})$ is the Standard-Model value obtained by running up from $M_Z$.

**(c) Quark masses (Jordan frame).** The 4D Yukawas are $y_4 \propto \ell_z^{-1/2}$ and the Higgs vev is taken as $\sigma$-independent in the Jordan frame (state this assumption in the report). So every quark mass at its threshold scales as

$$
m_q(\sigma) = \bar m_q\, e^{-\sigma/2}.
$$

Neglect the second-order change of the quark masses' own QCD running.

**(d) Running.** Use two-loop QCD running of $\alpha_s$ in $\overline{\rm MS}$, with $n_f$ = 6 above $m_t$, 5 above $m_b$, 4 above $m_c$, 3 below. Thresholds sit at $\mu = m_Q(m_Q)$ with $\alpha_s$ continuous there (exact at two loops in $\overline{\rm MS}$). Run down from $\mu_{KK}(\sigma)$ through the shifted thresholds $m_Q(\sigma)$ to get the three-flavour scale $\Lambda_3(\sigma)$. Use any standard two-loop definition of $\Lambda_3$, and state which one: the logarithmic derivative barely depends on the convention.

$$
\beta(\alpha_s) = \mu\frac{d\alpha_s}{d\mu} = -\frac{\alpha_s^2}{2\pi}\,b_0 - \frac{\alpha_s^3}{8\pi^2}\,b_1,
\qquad b_0 = 11 - \tfrac23 n_f,\quad b_1 = 102 - \tfrac{38}{3} n_f
$$

**(e) Nucleon mass (Feynman–Hellmann).** Write $m_N = \Lambda_3\, F(m_q/\Lambda_3)$ for the light quarks $u,d,s$. Then

$$
\frac{d\ln m_N}{d\sigma}\Big|_J = (1-s)\,\frac{d\ln\Lambda_3}{d\sigma} + s\,\frac{d\ln m_{ud,s}}{d\sigma},
\qquad s = \frac{\sigma_{\pi N} + \sigma_s}{m_N}.
$$

Heavy quarks enter only through the thresholds in (d). Do not add heavy-quark sigma terms on top.

**(f) Coupling and strength.** As in the repo:

$$
\frac{d\ln m_N}{d\sigma} = -\tfrac12 + \frac{d\ln m_N}{d\sigma}\Big|_J,
\qquad \beta = \frac{1}{\sqrt{3/2}}\frac{d\ln m_N}{d\sigma},
\qquad \alpha_Y = 2\beta^2.
$$

The range $\lambda(\ell_z)$ is unchanged (Casimir; use `range_um` from `tests/predictions.py`).

## 3. Inputs (use exactly these)

| input | value |
|---|---|
| $\alpha_s(M_Z)$ | $0.1180 \pm 0.0009$ |
| $M_Z$ | 91.1876 GeV |
| $m_c(m_c),\ m_b(m_b),\ m_t(m_t)$ ($\overline{\rm MS}$) | 1.27, 4.18, 162.5 GeV |
| $m_N$ | 938.9 MeV |
| $\sigma_{\pi N}$ | $50 \pm 10$ MeV |
| $\sigma_s$ | $45 \pm 20$ MeV |
| matching factor $k$ | 1 (default); vary over $\tfrac12$ and 2 |
| reference points $\ell_z^{-1}$ | 10, 14, 29 TeV |

**Derivative.** Central finite difference in $\sigma$ with step $10^{-3}$. Check that a step of $10^{-4}$ agrees to better than $10^{-4}$ relative.

**Errors.** Add in quadrature: $\alpha_s(M_Z)$, $\sigma_{\pi N}$, $\sigma_s$. Report the matching-scale variation separately (the $k = \tfrac12$ and $k = 2$ lines), not inside the error.

## 4. Required `RESULT:` lines (names exactly as written)

Sanity check, which must reproduce the repo:

- `alphaY_1loop_10TeV`: from `alpha_yukawa(10e12)` in `tests/predictions.py`

Decomposition of $d\ln m_N/d\sigma$ at 10 TeV, $k = 1$ (the parts must sum to the total):

- `weyl`
- `lambda3_part`: the term $(1-s)\, d\ln\Lambda_3/d\sigma$
- `lambda3_from_coupling`: the part of `lambda3_part` that comes from (b) alone, with quark masses held fixed
- `lambda3_from_thresholds`: the part of `lambda3_part` that comes from (c) acting on $c, b, t$
- `light_quark_part`: the term $s\cdot(-\tfrac12)$
- `dlnmN_dsigma_10TeV`

Main results:

- `beta_10TeV`
- `alphaY_10TeV`, `alphaY_14TeV`, `alphaY_29TeV`
- `alphaY_10TeV_k0.5`, `alphaY_10TeV_k2`

P1 window (§4a of `06_predictions.md`, recomputed with the new $\alpha_Y(\ell_z)$). Find the lowest $\ell_z^{-1}$ at which $\alpha_Y \le$ `alpha_bound(range_um(.))`; keep the upper edge at 29 TeV.

- `invlz_min_TeV`
- `lambda_max_um`
- `alphaY_window_low`, `alphaY_window_high`: $\alpha_Y$ at the two window edges

## 5. Report (`.scratch/alpha_y_report.md`)

1. All `RESULT:` lines, verbatim.
2. One paragraph: does the one-loop repo number survive? Which correction dominates, and why?
3. Verdict, one line each:
   - Does P1 stay a line segment with $\alpha_Y$ inside $[10^2,\ 4\times10^2]$?
   - Do the window edges ($14$–$29$ TeV, $2.8$–$12\ \mu$m) move?
   - Is the `[verify]` closed, or does a residual remain? Name it.
4. The assumptions you had to make beyond this brief, if any. There should be at most the $\Lambda_3$ convention and the Jordan-frame vev.

## 6. How the comparison will be scored

- **Correctness:** each `RESULT:` value against the reference, within the stated error or 2%, whichever is larger.
- **Fidelity:** the tool implements (a)–(f) as written: two-loop, thresholds shifted with $\sigma$, Feynman–Hellmann split, Weyl counted once.
- **Honesty:** no number appears in the report that the script did not print. Any deviation from the brief is stated.
- **Repo hygiene:** nothing under `v2/` or `tests/` changed.
