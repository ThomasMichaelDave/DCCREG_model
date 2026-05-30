# DCCREG Simulator — Consolidation Report

*Self-contained handoff for a consolidation session. Paste this whole file into a
Claude conversation. It records what the simulator computed, each result's tier
([OC] operational core / [IR] interpretive reading / [RH] resonance-heuristic),
and what each confirms / refines / falsifies. Per the firewall, a result
confirms/refines/falsifies an identification **within** DCCREG — it does not
prove the framework.*

- **Run:** `run002_sosf_spectrum_iterated`  ·  **git:** `ddd7c80`  ·  **seed:** `0`
- **Branch:** `claude/simulator-implementation-mZyYb`
- **Target:** the joined gravity+matter gate — the stable-defect spectrum of the
  hexatic SOSF (sim/README.md Outputs A/B/C).

---

## Validation ladder — 5/5 PASS (gates everything)

A number is load-bearing only if all five regression rungs pass in the same run.

| Rung | Check | Result |
|------|-------|--------|
| 1 | SOSF geometry reproduces labeling_convention_v4 §A.7 + structural counts | PASS |
| 2 | solid disclination ~ r²ln r (1/k⁴) baseline; log-log slope 2.19 (~2) | PASS |
| 3 | hexatic Green's fn: ∫_disk ∇²(ln r/2π) dA = **1.000** (Einstein form) | PASS |
| 4 | Călugăreanu Lk=Tw+Wr: planar Wr≈0, screw supplies integer Tw | PASS |
| 5 | chiral octahedral O: |O|=24, Frank classes **{90,120,180}°** | PASS |

---

## Output A — K_A → G_eff   *(gravity strength)*

- Lattice Biot–Savart self-energy slope (β coefficient), extrapolated d→0:
  **β = 0.07905 ρΓ²** vs analytic ρΓ²/4π = 0.07958 — **rel.err 0.66%**, monotone
  convergence under lattice refinement. **[OC]**, validated against the known limit.
- At Block III's light-isotropy point ln(d/a)=4 (β=α):
  **K_A ≈ 0.316 ρΓ²  →  G_eff ≈ 3.16 /ρΓ².**
  The K_A value is **[OC]** *resting on* the K_A~β identification **[IR]** (the
  Joining, IV-§3a/V-§2a); G_eff~1/K_A is **[IR]**.
- **3D cross-check:** the full 3D filament Biot–Savart sum gives straight-line
  coefficient **0.07881 (1.0% from the 2D value)** → the **quasi-2D reduction is
  validated** (exact for a straight disclination line). The [1,1,1]-screw helix
  raises the line tension only **×1.014 (~1%)** — extra arc length nearly
  cancelled by antiparallel tangents. **K_A is essentially unchanged in 3D. [OC]**
- **Reads:** lands O(1)·ρΓ² → **CONFIRMS** K_A~β and **REFINES** gravity strength
  into a number; an order-of-magnitude mismatch would have **FALSIFIED** the
  shared-parameter identification.

## Output C — E(r) interaction law   *(consistency)*

- Discrete triangular-lattice Green's function: the **ln r (1/k², Einstein/Newton)
  form is confirmed** — ln-fit residual 0.0016 vs r²ln r residual 0.036. **[OC, robust]**
- Measured coefficient **−0.0864 per ln r** (window spread ±0.0015; analytic
  −√3/6π = −0.0919, rel.err 5.9%). **[OC, ~10%]** — finite-torus limited, not
  claimed beyond its spread.
- **Screening length (computed):** genuine Debye screening by free dislocations,
  (−L+m²)G=δ, gives **ξ = κ⁻¹ = √(C₂/m²) ∝ n_disloc^(−1/2)** (2D Debye–Hückel),
  **validated against the continuum Bessel K₀(κr) to ~1.7%**; measured ξ ∈ [9,40]
  lattice units over the density range. **[OC]** for the law + validation; the
  dislocation density n_d (hence absolute ξ) is an **[IR]** thermodynamic input.
  This is genuine Debye screening — **NOT** the withdrawn v0.6 exp-proxy of the
  confining term.
- **Reads:** **CONFIRMS** the v0.6 Einstein-form closure on the real lattice;
  r²ln r persisting at large r would have **FALSIFIED** hexatic screening (not seen).

## Output B — defect spectrum + ground-state matter loop   *(decisive)*

- **Closure structure:** of the Fibonacci closure depths {1,2,3,5,8,13,21}, the
  **unique genuine closure** is **L=8** (twist residual 0.019 — **~7× better**
  than any other depth ≤21). **[OC arithmetic]**
- **Ground-state ribbon:** charge **120°**, **|Lk| = 1 (odd) → spin-½**,
  definite handedness. **[OC]** for the Lk/closure; "this ribbon is a matter
  particle" is **[IR]**.
- **Robustness:** in the strict-closure regime with energy weights varied
  0.1×–10×, the ground-state size, spin parity **and** charge are robust across
  **100%** of the scan.
- **Charge fork — RESOLVED (was open):** an isolated hexatic disclination needs
  ψ₆=exp(6iθ) single-valued ⟺ 6Ω ≡ 0 (mod 360°) ⟺ Ω a multiple of 60°. So **90°
  is excluded categorically** (ψ₆→−ψ₆, a string-attached half-disclination);
  admissible {120°,180°}; Frank energy ∝Ω² selects **120°**, which is *also* the
  screw-aligned C₃∥[1,1,1] — doubly natural. **No tunable weight.** **[OC]**
  selection resting on the hexatic 6-fold **[IR]**.
- **Caveat:** loosening the closure tolerance past 0.019 admits the poorly-closed
  L=1 bare loop (Lk=0, boson) — that is the unframed regime, not a genuine ribbon.
- **Verdict:** **CONFIRM (matter gate)** — a stable spin-½, definite-handedness
  (Weyl-capable) ground-state defect exists, with fixed charge 120°. The map to
  Standard-Model quantum numbers stays **[RH]**, fenced (V-§8) — not claimed.

---

## Proposed graduation (for the consolidation session)

Per CLAUDE.md §3.3/§3.5 these numbers do not edit Blocks directly; they graduate
via a versioned consolidation (bump version, archive prior, revision-history row,
move the superseded parametric/conditional statement to History, tag the new
number's tier). Suggested:

- **Block IV → v0.8 "K_A computed":** record **K_A ≈ 0.316 ρΓ²**, **G_eff ≈
  3.16/ρΓ²** [OC value on IR id]; 3D cross-check validating the quasi-2D
  reduction (~1% screw correction); and the Debye screening law ξ ∝ n_d^(−1/2)
  [OC] refining the §5.6 "atmosphere". Supersede the parametric K_A~β statement
  (move to History).
- **Block V → v0.3 "matter ground state":** record the ground-state defect —
  **spin-½, charge 120° (C₃∥[1,1,1]), definite handedness, Fibonacci depth L=8**;
  the 6-fold admissibility rule that fixes the charge [OC]; keep the SM-map [RH]
  fenced. Update the V-§2a/§6a cross-refs to IV-§3a.

## Honest residuals (not yet closed)

- Output C's *coefficient* is ~6–10% (finite-torus; would need an open-boundary
  solve, not improvable on a torus). The **form** (ln r) is robust.
- The absolute screening length ξ depends on the [IR] dislocation density n_d
  (the n_d^(−1/2) *law* is [OC]).
- Output B fixes the **ground state**; the full multiplet / excited spectrum and
  the [RH] map to real particle quantum numbers remain open.

## Reproduce

```bash
pip install -r sim/requirements.txt
python -m sim.run --run-id <name> --seed 0     # ladder + Outputs A/B/C -> results/<name>/
python -m sim.validation                       # the 5-rung ladder alone
```
