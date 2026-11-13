# 07 — The provisional tenth: dark-sector energy exchange

Taken under the 2026-11-11 rule of `ledger.md` (admit / pause / dead) after P2 was killed
(`06_predictions.md` §4c–4d). The question: can energy flow between the dark matter and the dark
energy (or across the branes) fast enough to give the DESI pattern, $w_0 > -1$ with $w < -1$ in the
past, which no canonical scalar can give alone? Numbers: `tests/exchange.py`.

| result | status |
|---|---|
| the action already couples DM to DE: $V_* \propto \ell_z$ (`03` §2), i.e. $e^{-\sigma}e^{-c\Phi_4/M_{Pl}}$ in the Einstein frame; its effect on the $\chi$ condensate is $\delta m_\chi^2/m_\chi^2 \approx 4\times10^{-62}$, order $(H_0/m_\chi)^2$ | derived, zero parameters, negligible |
| a tenth coupling that makes $m_{DM}$ depend on $\Phi$ must act through the stabilizer, so it moves the circle: $d\ln m_\chi = -3\,d\bar\sigma$ | derived (the lock) |
| the circle sets $\mu = m_p/m_e$ ($d\ln\mu/d\sigma \approx -8.8$) and $\alpha$ ($-1$); quasar bounds give $\lvert\Delta\bar\sigma\rvert < 10^{-8}$ since $z \approx 0.9$ | data [verify: bounds] |
| hence $\lvert\Delta\ln m_{DM}\rvert < 3\times10^{-8}$ and an exchange-induced $\lvert\Delta w\rvert < 10^{-8}$; DESI needs $\sim 0.3$ | **dead as a P2 fallback**, by data |
| other channels: baryons (Cassini), radiation ($10^{-4}$ of $\rho$), the radion ($1/\omega < 3\times10^{-5}$), bulk emission ($\rho/\sigma_1^{(5)}$) | derived, all negligible |
| fixes or predicts one of the nine? | no |

## 1. The coupling the action already has

In the Einstein frame of `06_predictions.md` §1, $ds^2 = e^{-\sigma}g_4 + e^{2\sigma}dz^2$ (5D) with
$\sigma = \ln(\ell_z/\bar\ell_z)$, $\chi = \sqrt{3/2}\,M_{Pl}\sigma$, a brane-frame term $\propto \ell_z^n$ becomes
$\propto e^{(n-2)\sigma}$. The bulk-potential term of `03_background.md` §2 is linear in $\ell_z$, so
$$
U \supset \rho_\Phi\,e^{-\sqrt{2/3}\,\chi/M_{Pl}},\qquad \rho_\Phi = V_*e^{-c\Phi_4/M_{Pl}} .
$$
This is a DM–DE coupling with no free number. Because $m_\chi \approx 8$ meV $\gg H_0$, the
condensate sees it only as a mass shift $\delta m_\chi^2/m_\chi^2 = \tfrac23\rho_\Phi/(M_{Pl}^2m_\chi^2)
\approx 4\times10^{-62}$ and a tadpole of the same order: heavy-field decoupling. It is the
Einstein-frame version of `04d_circle.md` §2's option 0, there seen as the meV minimum.

## 2. A tenth coupling, and the lock

For the dark matter to exchange energy with $\Phi$ coherently its mass must depend on $\Phi$
(the number channel, $\chi \to \Phi\Phi$, is gravitational, $\tau \sim 10^{38}$ yr; a faster one needs a
cubic coupling that no part of the geometry supplies). The DM mass is fixed by the stabilizer,
$U = C_z e^{-6\sigma} - \pi\lvert\delta_1\rvert e^{-\sigma}$ (`04d` §3, brane-frame $C_z/\ell_z^4 + \pi\delta_1\ell_z$):
$$
e^{5\bar\sigma} = \frac{6C_z}{\lvert\delta_1\rvert},\qquad
\tfrac32 M_{Pl}^2 m_\chi^2 = U''(\bar\sigma) = 5\lvert\delta_1\rvert e^{-\bar\sigma},\qquad
\boxed{\;d\ln m_\chi = -3\,d\bar\sigma\;}
$$
($C_z$ is a count, not a function of $\Phi$; in the brane frame the factor is $-\tfrac52$). Any
$\Phi$-dependence of $\delta_1$ — the only place a new coupling can enter — therefore changes the
width of the circle, and with it every brane coupling: $d\ln\alpha/d\sigma = -1$ and
$d\ln\mu/d\sigma = (1-s)\,d\ln\Lambda_3/d\sigma \approx -8.8$ (`06` §2; $m_e$ and the Weyl factor cancel in $\mu$).

**Data.** $\lvert\Delta\mu/\mu\rvert \lesssim 10^{-7}$ at $z \approx 0.9$ (molecular absorption toward
PKS 1830−211) and $\lvert\Delta\alpha/\alpha\rvert \lesssim 10^{-5}$ at $z \sim 1$–$3$ [verify: both from memory]
give $\lvert\Delta\bar\sigma\rvert < 1.1\times10^{-8}$, so $\lvert\Delta\ln m_{DM}\rvert < 3.4\times10^{-8}$ since
$z \approx 0.9$. A mass drift of that size shifts the inferred $w$ by
$\sim(\Omega_{DM}/\Omega_{DE})\,\lvert d\ln m/d\ln a\rvert/3 < 10^{-8}$. DESI's CPL fits need
$\lvert\Delta w\rvert \sim 0.3$ near $z \approx 1$: short by $4\times10^7$.

**Verdict under the rule.** Dead by data (rule 4): the registered kill "dark-matter dilution must
stay $a^{-3}$" is not just satisfied, it is forced to hold to $10^{-8}$ by the circle, so the
exchange cannot do the one thing it was proposed for. It fixes none of the nine. Not paused,
because pausing is for a number that fits but does not connect; this one cannot fit.

## 3. The other channels

- **Baryons** couple to $\Phi$ only through gravity (tensions $\Phi$-independent, `01` §2); a new
  coupling is a long-range fifth force, $\beta_b^2 \lesssim 10^{-5}$ (Cassini), on 5% of the energy.
- **Radiation**: $10^{-4}$ of $\rho$ today.
- **The radion** (inter-brane proper): its coupling to $\Sigma_1$ matter is $1/(2\omega+3) < 1.2\times10^{-5}$
  and its potential carries $\Omega^4$; a sum of canonical fields has $\rho + p \ge 0$.
- **Bulk emission** into $\mathcal C$: $\rho/\sigma_1^{(5)} \sim (T/15\,\mathrm{TeV})^4$, nothing at late times.

## 4. What this leaves

1. The lock is a result in its own right: in v2 **any dark-matter mass drift is a drift of $\mu$
   and $\alpha$**, $\Delta\ln m_{DM} \approx 0.34\,\Delta\ln\mu \approx 3\,\Delta\ln\alpha$. Interacting-dark-energy
   fits with $\beta_{DM} \gtrsim 10^{-6}$ would contradict v2's dark matter, not just its dark energy.
   Shared with ΛCDM as a null, so it does not move the balance.
2. The DESI pattern stays unexplained in v2; the remaining registered step is menu (a)/(b) of
   `01_action.md` §2.1, or closing the dark-energy branch.
3. **Inconsistency found** (not fixed here): ledger #4's bound $\lvert\delta\sigma_2\rvert < 0.15\,\rho_0/\Omega_0$
   and the $\dot G/G \lesssim 3\times10^{-16}$ constraint come from the *mirror*-DM mass drift
   (`03` §3.1). Since milestone 6 the dark matter is $\chi$, whose minimum does not depend on $\phi$
   (`04d` §3d), so that bound needs re-deriving from LLR and the residual $\Sigma_2$ content.
