# Run `run001_sosf_spectrum` — NOTES

- git commit: `9b3de529a414d39ae3ea1dab46b8cf738db65aae`
- seed: `0`
- generated: 2026-05-30T18:10:39

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
- Read: O(1)*rhoGamma^2 -> CONFIRMS K_A~beta and REFINES gravity strength; order-of-magnitude mismatch would FALSIFY the shared-parameter id.

## Output C — E(r) interaction law  [OC form / OC ~10% coefficient; IR identification]
- Lattice Green's function on the triangular hexatic lattice: the **ln r (1/k², Einstein/Newton) form is confirmed** (ln-fit residual 0.0016 vs r²ln r residual 0.0356). **[OC, robust]**
- Measured coefficient: **-0.0864 per ln r** (window spread ±0.0015; analytic −√3/6π = -0.0919, rel.err 5.9%). **[OC, ~10%]** — finite-torus limited, not claimed beyond its spread.
- Screening length: **not modelled** (flagged [IR] refinement; the withdrawn v0.6 exp-proxy is NOT reintroduced — honest gap).
- Read: ln r form recovered on the real lattice -> CONFIRMS the v0.6 Einstein/Newton closure (check_02) with a finite lattice coefficient; r^2 ln r at large r would FALSIFY hexatic screening (not seen).

## Output B — defect spectrum + ground-state matter loop  ← decisive  [OC ordering / IR identification / RH particle-map]
- Closure structure: the **unique genuine closure** is Fibonacci depth **L=8** (residual 0.019, **7× better** than any other depth ≤21). **[OC arithmetic]**
- Ground-state ribbon: charge 120°, **|Lk|=1 (odd) → spin-½**, handedness **L**. **[OC]** for Lk/closure; "this ribbon is a matter particle" is **[IR]**.
- Robustness (strict-closure regime, energy weights varied 0.1×–10×): size & parity robust across **100%** of the scan; charge robust only **72%**.
- **Open fork (honest gap):** Ground-state CHARGE is model-dependent: Frank self-energy favours 90 deg (smallest Omega^2), screw-commensuration favours 120 deg (C3//[1,1,1]). Reported as an open fork, NOT resolved — honest gap.
- Caveat: loosening closure to tol>0.019 (admitting the poorly-closed L=1 loop, residual 0.127, parity even) changes the ground state — this is the bare-loop regime, not a genuine framed ribbon.
- Verdict: CONFIRM (matter gate): the UNIQUE genuine closure is Fibonacci depth L=8 (residual 0.019, 7x better than any other depth), |Lk|=1 ODD = spin-1/2, definite handedness 'L'. Size & parity robust across 100% of the energy-weight scan (strict-closure regime).
- The map to Standard-Model quantum numbers is **[RH]**, fenced (Block V-§8) — NOT claimed here.

## What this run does NOT establish
- It does not prove DCCREG; it confirms/refines/falsifies identifications within it (INTERPRETATION.md §4).
- Output A's K_A is an [OC] number resting on the [IR] K_A~β identification; Output B's spin-½ ground state confirms fermion-*capability*, not that these are nature's fermions ([RH]).
- Graduation to Blocks (IV v0.8, V v0.3) is a separate consolidation session (CLAUDE.md §3.3/§3.5); this run writes to results/ only.

