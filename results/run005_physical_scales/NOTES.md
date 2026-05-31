# run005 — Physical scales & dimensionless ratios — NOTES

- git: `6b6c88362c1d427f56c966472cf2f9ee6aa11413`  ·  seed: `0`  ·  script: `sim/checks/check_06_physical_scales.py`
- Brief: `sim/RUN005_physical_scales_brief.md`. Branches from run002 (K_A) + run004 (check_05).

**Read `../../CLAUDE.md` and `../../sim/INTERPRETATION.md` first.** Per brief §0 this run emits **no SI absolutes** (that would invent inputs); it reports dimensionless ratios and free-input dependences only. A result confirms/refines/falsifies an identification *within* DCCREG.

## Validation ladder (gates everything)
- inherited rung 1: **PASS** — SOSF geometry reproduces §A.7 and structural counts
- inherited rung 2: **PASS** — solid disclination log-log slope = 2.192 (expect ~2, the 1/k^4 baseline)
- inherited rung 3: **PASS** — ∫_disk ∇²(ln r/2π) dA = 1.000 (expect ≈ 1.000, Einstein/Newton form)
- inherited rung 4: **PASS** — planar Wr=0.0000≈0; screw supplies integer Tw (n=1:Lk=-1.000, n=2:Lk=-2.000, n=3:Lk=-3.000)
- inherited rung 5: **PASS** — |O|=24 (expect 24); Frank classes [90, 120, 180] (expect [90,120,180])
- **NEW** dimensional closure: **PASS** — all 6 quantities' units reconstruct from the free-input set
- **NEW** known-limit recovery: **PASS** — K_A(lnda=4)=0.3162 rhoGamma^2 (run002 0.3162); gap(J=1)=2.000 (run004 2.000)

**Ladder status: ALL PASS — ratios are load-bearing.**

## 1. Minimal free-input set [OC dimensional analysis]
Every computed quantity reduces to **{ρ, Γ, ℓ_P, κ=2m/q, n_d, J, ln(d/a)}** (n_d enters only the screening length ξ). Dimensional closure (units reconstruct) **passes for all** — no hidden input. Reduced forms:
- **K_A** = (prefactor) · rho^1 Gamma^2 lnda^1   [OC] — line tension (run002); K_A=(beta_coeff)*lnda*rhoGamma^2
- **c** = (prefactor) · Gamma^1 ellP^-1 lnda^0.5   [IR] — emergent light speed c=sqrt(C66/rho)~ (Gamma/ellP) sqrt(lnda) (Block III)
- **hbar_eff** = (prefactor) · rho^1 Gamma^1 ellP^3   [IR] — emergent action: defect ang. momentum rho*Gamma*ellP^3 = spin hbar/2
- **m_D** = (prefactor) · rho^1 ellP^3 J^1 lnda^-1   [IR] — Dirac mass m_D = (gap energy)/c^2 ~ rho ellP^3 * J/lnda (run004)
- **G_eff** = (prefactor) · rho^-1 Gamma^2 ellP^-4 lnda^1   [IR] — emergent Newton coupling G_eff ~ c^4/K_A ~ Gamma^2/(rho ellP^4)*lnda
- **xi** = (prefactor) · n_d^-0.5   [OC] — Debye screening length xi=1/kappa_D ~ n_d^-1/2 (run002, validated vs K0)

Two emergent scales make the reduction possible (both **[IR]**): the action **ℏ_eff ~ ρΓℓ_P³** (a spin-½ defect's angular momentum = ℏ/2) and the light speed **c ~ (Γ/ℓ_P)√(ln d/a)** (Block III). Their units close [OC].

## 2. Pinned pure-arithmetic ratios (input-independent) [OC]
- golden screw period **1/s = 3φ² = 7.8541** levels/turn
- ground closure depth **L = 8** (residual |8s−1| = 0.0186)
- winding harmonics **L ≈ [8, 16, 24, 31, 39]** (ratios [1.0, 2.0, 3.0, 3.88, 4.88])
- octahedral charge ratio 180/120 = 1.5, Frank-energy² = **2.25**
These are genuine input-independent numbers — but **intra-sector** (defect combinatorics), not cross-gate.

## 3. The cross-gate gravity↔mass relation (the high-value target, brief §1.3)
**G_eff * m_D^2 / (hbar_eff * c)  ==  (m_D/m_Planck)^2**
- exponents over the free inputs: `{'lnda': -1.5, 'J': 2.0}`
- dimensionless: **True**; base scales (ρ,Γ,ℓ_P) cancel: **True**; surviving inputs: **['J', 'lnda']**.
- base scales rho,Gamma,ellP CANCEL (real reduction, enabled by the emergent hbar~rho*Gamma*ellP^3 and c~Gamma/ellP); residual J^2 * lnda^(-3/2) remains -> NOT a fully input-independent pure number.
- First-principles **J = 1** (elementary mutual link |Lk_AB|=1, run004 Gauss integral) [IR] fixes one residual; the rest is ln(d/a)≈4 (not exact) × an uncomputed O(1) geometric prefactor. So the cross-gate (m_D/m_Planck)² is **conditionally pinned, not a pure number**.

## BRANCH: **B-REDUCED**
REAL REDUCTION: in the cross-gate combination (m_D/m_Planck)^2 = G_eff m_D^2/(hbar_eff c) the base scales rho,Gamma,ellP ALL CANCEL — made possible by identifying the emergent hbar~rho*Gamma*ellP^3 [IR] and c~Gamma/ellP [IR]. The residual is J^2 * lnda^(-3/2): surviving dimensionless inputs ['J', 'lnda']. First-principles J=1 (elementary mutual link, run004) fixes one of these [IR], leaving only lnda(~4, not exact) and an uncomputed O(1) geometric prefactor — so the ratio is CONDITIONALLY pinned, NOT a fully input-independent pure number. Pinned PURE-arithmetic ratios DO exist (golden screw period 3*phi^2, octahedral charge ratio, winding harmonics) but they are intra-sector, not cross-gate. Per brief §3 this is B-REDUCED: inputs reduce and structure sharpens, without a parameter-free cross-gate number. We refuse to manufacture B-PINNED by declaring J,lnda fixed (brief §5).

## Graduation (per the branch)
- **B-REDUCED:** update the II-§8 / IV / V residuals with the reduced accounting: all sector quantities collapse to {ρ,Γ,ℓ_P} × dimensionless g(J, ln d/a); the emergent ℏ~ρΓℓ_P³ and c~Γ/ℓ_P are identified; the cross-gate (m_D/m_Planck)² has the base scales cancel, leaving J²·ln(d/a)^(−3/2). Record that DCCREG is **one O(1) geometric prefactor + an exact ln(d/a) away** from a parameter-free gravity↔mass number — a sharply-located open target, not a claim.

## What this run does NOT establish
- **No SI numbers** — by design (brief §0/§5); absolute values need external input.
- The cross-gate cancellation rests on the **[IR]** emergent ℏ and c identifications; the **dimensional structure** is [OC] but 'this ratio is a physical prediction' is [IR].
- The map to a **measured** SM mass/coupling ratio stays **[RH], fenced (V-§8)**.
- The O(1) geometric prefactors of c, ℏ_eff, G_eff, m_D are **not computed** (honest gap).

