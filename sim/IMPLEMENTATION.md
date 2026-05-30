# DCCREG Simulator — Implementation Guide

**Read `../CLAUDE.md` (firewall), `README.md` (target spec) and `INTERPRETATION.md`
(contract) first.** This file describes the *code that exists*; the three docs
above describe *what it must compute and how a number becomes meaningful*.

The simulator computes the single joined target — the **stable-defect spectrum of
the hexatic SOSF** — as the three Outputs of `README.md`, each gated behind the
5-rung validation ladder. It writes a full reproducibility log to `../results/`.

## Run it

```bash
pip install -r requirements.txt
python -m sim.run                 # full run -> results/<timestamp>/
python -m sim.run --quick         # smaller lattices, fast
python -m sim.run --outputs A C   # subset
```

Each run writes `results/<run-id>/`: `params.json` (params + git commit + seed),
`data.json`, `data.csv`, `figures/`, and `NOTES.md` (every claim tagged
[OC]/[IR]/[RH] with a confirm/refine/falsify line). **A number is load-bearing
only if the ladder is 5/5 in the same run** (`INTERPRETATION.md` §0).

## Module map (`sim/`)

| Module | Role |
|--------|------|
| `geometry/sosf.py` | SOSF geometry from `docs/DCCREG_labeling_convention_v4.md` App. A; reproduces §A.7 cross-sections (**validation rung 1**); the transverse-[1,1,1] hexagon that seeds the lattice. |
| `lattice.py` | The quasi-2D transverse-to-[1,1,1] **triangular (hexatic) lattice** — the clean KTHNY frame. |
| `biot_savart.py` | Biot–Savart lattice self-energy sum; converges to the line-tension coefficient ρΓ²/4π. |
| `outputs/output_a_KA.py` | **Output A** — numeric `K_A → G_eff` from the lattice Biot–Savart sum, validated against the analytic ln(d/a) limit. |
| `outputs/output_c_Er.py` | **Output C** — `E(r)` via the discrete triangular-lattice Green's function; confirms the ln r (1/k²) Einstein form. |
| `outputs/output_b_spectrum.py` | **Output B** (decisive) — defect spectrum + ground-state framed ribbon; spin parity (Lk mod 2) + handedness, with a robustness scan. |
| `validation.py` | The 5-rung ladder runner (gates all Outputs). |
| `checks_bridge.py` | Reuses the verified `checks/` functions (`twist`, `writhe`, `build_frame`, `chiral_octahedral_group`) — no re-derivation. |
| `resultio.py` | Reproducibility I/O: run dir, git hash, params/data/NOTES writers. |
| `run.py` | Orchestrator. |

## What the current build establishes (and does not)

- **Output A [OC]:** the lattice Biot–Savart slope converges monotonically to
  ρΓ²/4π (≈0.66% at the finest lattice). At the Block III isotropy point
  ln(d/a)=4 this gives **K_A ≈ 0.32 ρΓ²** → **G_eff ≈ 3.16 /ρΓ²**. The
  `K_A ~ β` identification it rests on is **[IR]** (the Joining).
- **Output C [OC]:** the lattice Green's function is **ln r** (decisively beats
  the confining r²ln r); coefficient measured to ~10% (finite-torus limited).
  Screening length is **not modelled** (flagged [IR] gap — the withdrawn v0.6
  exp-proxy is deliberately not reintroduced).
- **Output B:** the **unique genuine closure** is Fibonacci depth **L=8** (≈7×
  better closure than any other depth ≤21), giving **|Lk|=1 (odd) → spin-½**
  with definite handedness — robust across the energy-weight scan. The
  ground-state **charge** (90° vs 120°) is an **open fork**, reported not
  resolved. The map to Standard-Model quantum numbers is **[RH]**, out of scope.

Graduation of any number into a Block (IV v0.8, V v0.3) is a separate
consolidation session (`CLAUDE.md` §3.3/§3.5); this code writes to `results/`
only.

## Open / next

- Output A: reduce the residual with a genuine 3D (not quasi-2D) lattice sum.
- Output C: the screening length κ⁻¹ on a lattice carrying free dislocations.
- Output B: resolve the 90°-vs-120° charge fork (needs the full Frank elastic
  energy on the lattice, not the stated parametric model).
