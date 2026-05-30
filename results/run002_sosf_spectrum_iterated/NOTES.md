# Run `run002_sosf_spectrum_iterated` — NOTES

- git commit: `ddd7c802babef88822c0fef81d845fb7cce99f6a`
- seed: `0`
- generated: 2026-05-30T18:36:50

**Read `../../CLAUDE.md` (firewall) and `../../sim/INTERPRETATION.md` (contract) first.** This run targets the SOSF defect spectrum (Outputs A/B/C). Every claim below carries a tier tag; a result confirms/refines/falsifies an *identification within* DCCREG — it does not prove the framework.

## Validation ladder (gates everything)
- rung 1: **PASS** — SOSF geometry reproduces §A.7 and structural counts
- rung 2: **PASS** — solid disclination log-log slope = 2.192 (expect ~2, the 1/k^4 baseline)
- rung 3: **PASS** — ∫_disk ∇²(ln r/2π) dA = 1.000 (expect ≈ 1.000, Einstein/Newton form)
- rung 4: **PASS** — planar Wr=0.0000≈0; screw supplies integer Tw (n=1:Lk=-1.000, n=2:Lk=-2.000, n=3:Lk=-3.000)
- rung 5: **PASS** — |O|=24 (expect 24); Frank classes [90, 120, 180] (expect [90,120,180])

**Ladder status: 5/5 PASS — Outputs are load-bearing.**

## Output A — K_A → G_eff  [OC value on IR identification]
- Lattice Biot–Savart self-energy slope (β coefficient), extrapolated d→0: **0.07905 ρΓ²** (analytic ρΓ²/4π = 0.07958; rel.err 0.66%). **[OC]** — validated against the known limit.
- Converged: **True** (monotone under lattice refinement).
- At the Block III isotropy point ln(d/a)=4: **K_A ≈ 0.316 ρΓ²** → **G_eff ≈ 3.16 /ρΓ²**. **[OC value]** resting on K_A~β **[IR]** (the Joining, IV-§3a/V-§2a); G_eff~1/K_A **[IR]**.
- **3D cross-check:** the genuine 3D filament Biot–Savart sum gives straight-line coefficient **0.07881** (1.0% from the 2D value) → **quasi-2D reduction validated [OC]** (exact for a straight disclination line). The [1,1,1]-screw helix raises the line tension only **×1.014** (~1%; the extra arc length is nearly cancelled by antiparallel tangents). So K_A is essentially unchanged in 3D.
- Read: O(1)*rhoGamma^2 -> CONFIRMS K_A~beta and REFINES gravity strength; order-of-magnitude mismatch would FALSIFY the shared-parameter id. The 3D filament sum confirms the quasi-2D reduction (straight-line coeff = 2D value) and a small (~1%) screw correction.

## Output C — E(r) interaction law  [OC form / OC ~10% coefficient; IR identification]
- Lattice Green's function on the triangular hexatic lattice: the **ln r (1/k², Einstein/Newton) form is confirmed** (ln-fit residual 0.0016 vs r²ln r residual 0.0356). **[OC, robust]**
- Measured coefficient: **-0.0864 per ln r** (window spread ±0.0015; analytic −√3/6π = -0.0919, rel.err 5.9%). **[OC, ~10%]** — finite-torus limited, not claimed beyond its spread.
- **Screening length (computed):** free dislocations Debye-screen the ln r beyond **ξ = κ⁻¹ = √(C₂/m²) ∝ n_disloc^(−1/2)** (2D Debye–Hückel). Measured ξ ∈ [9, 40] lattice units over the density range, **validated against the continuum Bessel K₀(κr) to 1.7%**. **[OC]** for the law + validation; the dislocation density n_d (hence the absolute ξ) is an **[IR]** thermodynamic input. This REFINES IV-§5.6's 'atmosphere' — and is genuine Debye screening, NOT the withdrawn v0.6 exp-proxy of the confining term.
- Read: ln r form recovered on the real lattice -> CONFIRMS the v0.6 Einstein/Newton closure (check_02) with a finite lattice coefficient; r^2 ln r at large r would FALSIFY hexatic screening (not seen). Free dislocations Debye-screen the ln r beyond xi=kappa^-1 ~ n_d^(-1/2) (validated vs K0), REFINING IV-§5.6's 'atmosphere'.

## Output B — defect spectrum + ground-state matter loop  ← decisive  [OC ordering / IR identification / RH particle-map]
- Closure structure: the **unique genuine closure** is Fibonacci depth **L=8** (residual 0.019, **7× better** than any other depth ≤21). **[OC arithmetic]**
- Ground-state ribbon: charge 120°, **|Lk|=1 (odd) → spin-½**, handedness **L**. **[OC]** for Lk/closure; "this ribbon is a matter particle" is **[IR]**.
- Robustness (strict-closure regime, energy weights varied 0.1×–10×): size, parity & charge robust across **100%** / **100%** of the scan.
- **Charge fork — RESOLVED:** Admissible isolated hexatic disclination <=> psi6=exp(6 i theta) single-valued <=> 6*Omega = 0 (mod 360) <=> Omega is a multiple of 60 deg. 90° is excluded categorically (ψ₆→−ψ₆, a string-attached half-disclination), leaving admissible [120.0, 180.0]°; Frank energy ∝Ω² then selects **120°** (also the screw-aligned C₃∥[1,1,1] — doubly natural). **[OC]** selection on the hexatic 6-fold **[IR]**. No tunable weight.
- Caveat: loosening closure to tol>0.019 (admitting the poorly-closed L=1 loop, residual 0.127, parity even) changes the ground state — this is the bare-loop regime, not a genuine framed ribbon.
- Verdict: CONFIRM (matter gate): the UNIQUE genuine closure is Fibonacci depth L=8 (residual 0.019, 7x better than any other depth), |Lk|=1 ODD = spin-1/2, definite handedness 'L'. Size & parity robust across 100% of the energy-weight scan (strict-closure regime).
- The map to Standard-Model quantum numbers is **[RH]**, fenced (Block V-§8) — NOT claimed here.

## What this run does NOT establish
- It does not prove DCCREG; it confirms/refines/falsifies identifications within it (INTERPRETATION.md §4).
- Output A's K_A is an [OC] number resting on the [IR] K_A~β identification; Output B's spin-½ ground state confirms fermion-*capability*, not that these are nature's fermions ([RH]).
- Graduation to Blocks (IV v0.8, V v0.3) is a separate consolidation session (CLAUDE.md §3.3/§3.5); this run writes to results/ only.

