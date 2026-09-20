# BMI v2 — Rebuild

v1 (everything under `manuscript/`, `src/`, the root `README.md` results) is frozen. Its
audit is in `ledger_v1_audit.md`, the chapter-by-chapter hard-stop audit in `v1_chapter_audit.md`; the negative-results record is `../RETRACTED.md`.

v2 is rebuilt from a single axiom (`00_axiom.md`) and a single action
(`01_action.md`; the milestone-1 skeleton is kept as `01_action_skeleton_superseded.md`), with a fixed parameter budget (`ledger.md`) enforced by CI.

## Milestones

Each milestone is one PR. A milestone merges only when its tests pass and the ledger balance
has not decreased.

| # | milestone | deliverable | test / kill criterion | status |
|---|---|---|---|---|
| 1 | Freeze v1, open v2 | `RETRACTED.md`, `v2/`, `ledger.md`, `tests/check_ledger.py`, CI | ledger check passes on `v2/` | done |
| 2 | Action | `01_action.md`: signs, factors, Fork 1 warped geometry, one $V(\Phi)$ form, GHY terms | ledger ≤ 7 rows, 0 free functions | done |
| 3 | 4D effective theory | `02_effective_4d.md`: Israel junction → $G_{\mu\nu}$ with $\pi_{\mu\nu}$, $E_{\mu\nu}$, radion terms; $G_N(\phi)$, $V_{\text{eff}}(\phi)$ | GR + ΛCDM recovered for frozen $\phi$; $\dot G/G$ within LLR bound | done (background factors checked by `tests/check_background.py`; metric of `01_action.md` §3 corrected; forced consequence: warped mirror sector, §5) |
| 3b | Localization | `02b_localization.md`: zero-mode equation per spin on the AdS$_6$ background; what field content the geometry forces | no per-species choice admitted; SM chirality and darkness of $\Sigma_2$ respected | done (`tests/check_zero_modes.py`; forced: $z \in S^1/\mathbb Z_2$, gauge fields on $\Sigma_1$, only singlets in the bulk, $z$-tower heavy/ours vs $y$-tower light/theirs; not forced: bulk-fermion mass $c$) |
| 4 | Background | `03_background.md`: 6D Brans–Dicke $\omega$, $K(\phi)$, bulk-scalar zero mode, closed effective 4D Lagrangian; FRW $w(z)$; DM-mass drift vs CMB | vs DESI $w_0, w_a$; Planck $N_{\text{eff}}$; $|\Delta\Omega/\Omega| \lesssim$ few % since recombination | done (`tests/check_radion.py`, `tests/background_frw.py`); kill 2 passed, kill 3 open (thawing $w>-1$ vs DESI phantom hint); DE = inter-brane potential dead |
| 5 | Impact | `04_impact.md`: $T_2/T_1$, $n_2/n_1$, $\mathcal C$, sign of $\delta\sigma_2$, $(n_s, r)$ | BBN/CMB $N_{\text{eff}}$; $\Omega_{DM}/\Omega_b$; $r<0.036$ | done (`tests/impact.py`); $\mathcal C$ computed ($\Delta N_{\text{eff}} \lesssim 0.03$), $\phi_0 \leftrightarrow r_b$ with a 1.5% coincidence; $T_2/T_1$ not derivable, $<0.45$; **mirror SM as dark matter dead** (needs $\eta_2/\eta_1 \gtrsim 1600$) — exit decision pending; no primordial spectrum, kill 5 re-labelled |
| 5b | Initial conditions | `04b_initial_conditions.md`: scan of post-impact initial data (`r_b`, `f_2`, `\eta_1`, `\eta_2`/`P_relic`, $\Sigma_2$ content) | Cassini; BBN/CMB $N_{\text{eff}}$; $\Omega_{DM}/\Omega_b$ | done (`tests/scan_initial_conditions.py`); null configuration dead; viable: pre-loaded asymmetric mirror SM (thin band, dissipative DM), cold relic on $\Sigma_2$, or no mirror DM — each mirror-DM survivor costs +1 datum; none adopted |
| 5c | Approach to $\Omega=1$ | `04c_approach.md`: exact two-brane solution in Schwarzschild–AdS (no moduli approximation); $\Omega_\infty$ from collision data | Cassini; $N_{\text{eff}}$; existence of $\Sigma_2$ | done (`tests/approach.py`); $\Omega_\infty^3 = (\epsilon-f)/(1+\epsilon)$, `r_b` not a datum; $\epsilon \ge f$ ($N_{\text{eff}}$ doubled, $\mathcal C$ re-opened); Cassini coincidence sharpened to $10^{-3}$; **circle modulus $\ell_z$ unstabilized** — stabilizer fork owed; pre-action layer + unified-sector fork recorded |
| 6 | Dark sector | `05_dark_sector.md`: $\Omega_{DM}/\Omega_b$, $\sigma/m$, structure formation offset | Bullet Cluster; halo shapes; isolated DM-free dwarfs | blocked on the exit chosen in `04_impact.md` §3 |
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
pip install "sympy>=1.12,<2"
python3 tests/check_background.py
python3 tests/check_zero_modes.py
python3 tests/check_radion.py
pip install numpy scipy
python3 tests/background_frw.py
python3 tests/impact.py
python3 tests/scan_initial_conditions.py
python3 tests/approach.py
```
