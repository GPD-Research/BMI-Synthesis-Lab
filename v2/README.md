# BMI v2 — Rebuild

v1 (everything under `manuscript/`, `src/`, the root `README.md` results) is frozen. Its
audit is in `ledger_v1_audit.md`, the chapter-by-chapter hard-stop audit in `v1_chapter_audit.md`; the negative-results record is `../RETRACTED.md`.

v2 is rebuilt from a single axiom (`00_axiom.md`) and a single action
(`01_action_skeleton.md`), with a fixed parameter budget (`ledger.md`) enforced by CI.

## Milestones

Each milestone is one PR. A milestone merges only when its tests pass and the ledger balance
has not decreased.

| # | milestone | deliverable | test / kill criterion | status |
|---|---|---|---|---|
| 1 | Freeze v1, open v2 | `RETRACTED.md`, `v2/`, `ledger.md`, `tests/check_ledger.py`, CI | ledger check passes on `v2/` | this PR |
| 2 | Action | `01_action.md`: signs, factors, Fork 1 warped geometry, one $V(\Phi)$ form, GHY terms | ledger ≤ 7 rows, 0 free functions | |
| 3 | 4D effective theory | `02_effective_4d.md`: Israel junction → $G_{\mu\nu}$ with $\pi_{\mu\nu}$, $E_{\mu\nu}$, radion terms; $G_N(\phi)$, $V_{\text{eff}}(\phi)$ | GR + ΛCDM recovered for frozen $\phi$; $\dot G/G$ within LLR bound | |
| 4 | Background | `03_background.md`: $a(t), \phi(t)$; $w(z)$; $\Delta N_{\text{eff}}$ | vs DESI $w_0, w_a$; Planck $N_{\text{eff}}$ | |
| 5 | Impact | `04_impact.md`: $T_2/T_1$, $n_s$, $r$, $f_{NL}$ | BBN $T_2/T_1$; Planck $n_s$; $r<0.03$ | |
| 6 | Dark sector | `05_dark_sector.md`: $\Omega_{DM}/\Omega_b$, $\sigma/m$, structure formation offset | Bullet Cluster; halo shapes; isolated DM-free dwarfs | |
| 7 | Predictions | `06_predictions.md`: preferred-axis low-$\ell$ CMB covariance; $d_L^{GW}/d_L^{EM}$; joint $(\dot G/G, w_a)$ | pre-registered, dated, before comparison | |
| 8 | Unlike | `07_unlike.md`: reciprocal comparison with SM, GR, ΛCDM, MOND, string theory | every cell cites a v2 equation or says "not derived" | |

## Rules

1. No free functions. A function is allowed only if its form is derived in `v2/` or chosen
   from a finite menu declared in `ledger.md`.
2. No symbol enters `v2/*.md` without a ledger row or an allowlist entry.
3. Predictions are written down with a date before the data comparison is run.
4. A forced miss is recorded in `RETRACTED.md`, not patched with a new parameter.
5. `master_axiom.md` is regenerated from `v2/` only, once milestone 3 lands.

## Regenerating checks locally

```bash
python3 tests/check_ledger.py
```
