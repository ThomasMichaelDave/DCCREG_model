# DCCREG Simulator — Consolidation Report (run005: physical scales)

*Self-contained handoff for a consolidation session. Paste this whole file into a
Claude conversation. It records what the simulator computed, each result's tier
([OC] operational core / [IR] interpretive reading / [RH] resonance-heuristic),
and what each confirms / refines / falsifies. Per the firewall (CLAUDE.md §1), a
result confirms/refines/falsifies an identification **within** DCCREG — it does
not prove the framework.*

- **Run:** `run005_physical_scales`  ·  **seed:** `0`  ·  **git:** see `params.json` (`6b6c883`)
- **Branch:** `claude/simulator-implementation-mZyYb`
- **Script:** `sim/checks/check_06_physical_scales.py`
- **Brief:** `sim/RUN005_physical_scales_brief.md` (branches from run002 K_A + run004 check_05)
- **Target:** the **dimensional content** of the programme — reduce every computed
  quantity (G_eff, m_D, ξ, the defect-spectrum energies) to the minimal set of
  free dimensional inputs and extract the **input-independent dimensionless
  ratios**, the framework's actual falsifiable content.
- **The question:** which ratios are pinned (input-independent)? In particular, do
  gravity and the Dirac mass — both descended from the *same* lattice stiffness
  K_A∼β∼ρΓ²ln(d/a) (the Joining) — force a **parameter-free G_eff–m_D relation**?
- **Hard firewall on this run (brief §0/§5):** **no SI absolutes.** The framework
  carries free inputs by design; emitting an "electron mass in kg" would mean
  inventing them. Dimensionless ratios and free-input dependences only.

---

## Validation ladder — status this run

A number is load-bearing only if the rungs pass in the same session (INTERPRETATION
§0). Inherited rungs 1–5 re-run **and** the brief's two **new** self-tests added;
**all pass**:

| Rung | Check | Result | Source |
|------|-------|--------|--------|
| 1 | SOSF geometry reproduces §A.7 + structural counts | PASS | `geometry/sosf` |
| 2 | solid r²ln r (1/k⁴) baseline; slope 2.19 | PASS | `check_02` |
| 3 | hexatic Green's fn ∫∇²(ln r/2π) = **1.000** (Einstein form) | PASS | `check_02` |
| 4 | Călugăreanu Lk = Tw + Wr (planar Wr≈0) | PASS | `check_01` |
| 5 | chiral octahedral O: \|O\|=24, classes **{90,120,180}°** | PASS | `check_03` |
| **NEW** | **dimensional closure** — every quantity's units reconstruct from the free-input set (no hidden input) | **PASS** | this run |
| **NEW** | **known-limit recovery** — reduction layer reproduces run002 K_A = 0.3162 ρΓ² and run004 gap(J=1) = 2.000 | **PASS** | this run |

A ratio arriving while these fail is a bug, not a result (brief §4). They pass.

---

## What was computed

### [OC] — the minimal free-input set + dimensional closure
Every computed quantity reduces to **{ρ, Γ, ℓ_P, κ=2m/q, n_d, J, ln(d/a)}** (n_d, the
free-dislocation density, enters only the screening length ξ). Units reconstruct for
**all six** — no hidden input crept in. Reduced forms (basis M,L,T,Q):

| quantity | reduced form | dim | tier |
|----------|--------------|-----|------|
| K_A (line tension) | (β_coeff)·ρΓ²·ln(d/a) | M L T⁻² | OC |
| c (light speed) | ∼ (Γ/ℓ_P)·√(ln d/a) | L T⁻¹ | IR (III) |
| ℏ_eff (action) | ∼ ρΓℓ_P³ | M L² T⁻¹ | IR |
| m_D (Dirac mass) | ∼ ρℓ_P³·(J/ln d/a) | M | IR |
| G_eff (Newton) | ∼ Γ²/(ρℓ_P⁴)·ln(d/a) | L³ M⁻¹ T⁻² | IR |
| ξ (screening) | ∼ n_d^(−1/2) | L | OC |

Two **emergent** scales (both **[IR]**) make the reduction possible: the **action
ℏ_eff ∼ ρΓℓ_P³** (a spin-½ defect's angular momentum = ℏ/2) and the **light speed
c ∼ (Γ/ℓ_P)√(ln d/a)** (Block III). Their units close **[OC]**.

### [OC] — pinned pure-arithmetic ratios (input-independent)
- golden screw period **1/s = 3φ² = 7.854** levels/turn;
- ground closure depth **L = 8** (residual |8s−1| = 0.0186);
- winding harmonics **L ≈ 8, 16, 24, 31, 39**;
- octahedral charge ratio 180/120 = 1.5 → Frank-energy² = **2.25**.

These are genuine input-independent numbers — but **intra-sector** (defect
combinatorics), not cross-gate.

### [OC structure / IR identification] — the cross-gate gravity↔mass combination
> **(m_D/m_Planck)² ≡ G_eff·m_D² / (ℏ_eff·c)**

Computed exponents over the free inputs: **{J: +2, ln(d/a): −3/2}**, everything else
zero. So it is **dimensionless**, and the **base scales ρ, Γ, ℓ_P all cancel** —
made possible *only* by the emergent ℏ_eff∼ρΓℓ_P³ and c∼Γ/ℓ_P. The residual is
**J²·ln(d/a)^(−3/2)**.

---

## Results — confirm / refine / falsify

**1. The input set is minimal and closes. [OC]**
All sector quantities collapse to {ρ, Γ, ℓ_P} (× κ for the EM dictionary, × n_d for
screening) times dimensionless functions of {J, ln(d/a)}. Dimensional closure passes
→ **CONFIRMS** there is no hidden dimensional input; the free-parameter count is as
the framework declares (II-§8 flag 1, IV, V).

**2. The base scales cancel in the gravity↔mass ratio — a real reduction. [OC structure]**
In (m_D/m_Planck)², ρ, Γ and ℓ_P **all cancel**. This is the strongest structural
statement available: the gravity and mass sectors share enough that the three base
scales drop out of their cross-ratio. → **REFINES** the Joining (IV-§3a: "one shared
parameter") into a sharp dimensional statement.

**3. But it is NOT a parameter-free number. [OC]**
The residual **J²·ln(d/a)^(−3/2)** survives. Two reasons it cannot be pinned as it
stands:
- the framework has **no externally-fixed ℏ** — ℏ_eff∼ρΓℓ_P³ is itself built from
  the base scales, which is *why* they cancel, but the cross-ratio then inherits the
  coupling **J** (the run004 mass scale);
- it depends on **ln(d/a)**, which Block III pinned only **≈4, not exactly** (brief §5).
First-principles **J = 1** (the elementary mutual link \|Lk_AB\|=1 computed in run004)
[IR] fixes one residual — leaving ln(d/a)≈4 and an **uncomputed O(1) geometric
prefactor**. So (m_D/m_Planck)² is **conditionally pinned, not a pure number**. We
**refuse to manufacture B-PINNED** by declaring J and ln(d/a) fixed (brief §5).

**4. Pinned ratios that DO exist are intra-sector. [OC]**
The golden screw period 3φ², the octahedral charge ratio 2.25, and the winding
harmonics L≈8n are genuinely input-independent — but they live inside the defect
combinatorics, not across the gravity↔matter gate.

---

## Verdict — BRANCH **B-REDUCED**

The free-input set **reduces and the structure sharpens** — all sector quantities
collapse to {ρ,Γ,ℓ_P}×g(J,ln d/a); the emergent ℏ_eff∼ρΓℓ_P³ and c∼Γ/ℓ_P are
identified; and the base scales **cancel** in the cross-gate (m_D/m_Planck)². But
**no fully input-independent cross-gate number emerges**: the residual J²·ln(d/a)^(−3/2)
remains, held open by the absence of an external ℏ, the free coupling J, and the
inexact ln(d/a)≈4. DCCREG is **one O(1) geometric prefactor + an exact ln(d/a)
away** from a parameter-free gravity↔mass prediction — a sharply-located open
target, not a claim. (Not B-PINNED: that would require burying J/ln(d/a). Not
B-IRREDUCIBLE: the base scales genuinely cancel.)

---

## Proposed graduation (for the consolidation session)

These numbers do **not** edit Blocks directly (CLAUDE.md §3.3/§3.5). This run is a
**dimensional-accounting refinement**, not a new mechanism. Suggested:

- **README frontier / II-§8 / IV / V residuals:** record the **reduced accounting** —
  every sector quantity = {ρ,Γ,ℓ_P}×dimensionless g(J, ln d/a) (+κ for EM, +n_d for
  screening); the emergent **ℏ_eff∼ρΓℓ_P³** and **c∼Γ/ℓ_P** identifications [IR];
  and the cross-gate result that **(m_D/m_Planck)² has the base scales cancel,
  leaving J²·ln(d/a)^(−3/2)**.
- State plainly (no overclaim): DCCREG currently makes **input-independent
  *intra-sector* arithmetic predictions** (3φ², charge 2.25, winding L≈8n) and is
  **one geometric prefactor + an exact ln(d/a) short** of a parameter-free
  *cross-gate* gravity↔mass number. Tag: **[OC]** dimensional structure; **[IR]**
  the c/ℏ_eff identifications and "this ratio is a prediction".

## Honest residuals (not closed)

- **No SI numbers** — by design (brief §0/§5); absolute values need external input.
- The cross-gate cancellation **rests on the [IR]** emergent ℏ_eff and c; the
  dimensional structure is [OC], but "this ratio is a physical prediction" is [IR].
- The **O(1) geometric prefactors** of c, ℏ_eff, G_eff, m_D are **not computed** —
  the gap between B-REDUCED and B-PINNED.
- **ln(d/a)** is pinned only ≈4 (Block III), so any cross-gate number is only as
  pinned as that.
- The map to a **measured** SM mass/coupling ratio stays **[RH], fenced (V-§8)**.

## Reproduce

```bash
pip install -r sim/requirements.txt
python3 sim/checks/check_06_physical_scales.py results/run005_physical_scales
# validation rungs available on this branch:
python3 sim/checks/check_01_calugareanu_framing.py
python3 sim/checks/check_02_hexatic_greens_function.py
python3 sim/checks/check_03_joining_spectrum.py
```
