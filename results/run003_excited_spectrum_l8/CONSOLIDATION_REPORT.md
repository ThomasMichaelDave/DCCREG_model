# DCCREG Simulator — Consolidation Report (run003: excited spectrum)

*Self-contained handoff for a consolidation session. Paste this whole file into a
Claude conversation. It records what the simulator computed, each result's tier
([OC] operational core / [IR] interpretive reading / [RH] resonance-heuristic),
and what each confirms / refines / falsifies. Per the firewall (CLAUDE.md §1), a
result confirms/refines/falsifies an identification **within** DCCREG — it does
not prove the framework.*

- **Run:** `run003_excited_spectrum_l8`  ·  **seed:** `0`  ·  **git:** see `params.json`
- **Branch:** `claude/excited-spectrum-l8-uyAlt`
- **Script:** `sim/checks/check_04_excited_spectrum.py`
- **Target:** the **excited / multiplet spectrum above** the closed ground-state
  gate (run002). Ground state = the fundamental screw closure: depth **L=8**,
  charge **120°** (C₃∥[1,1,1]), self-linking **|Lk|=1 (odd → spin-½)**, definite
  handedness.
- **The question:** above L=8, does the energetics produce **(a)** only the single
  state, **(b)** a **doublet** (isospin-like near-degenerate pair), or **(c)** a
  **generation tower** (replicas of the same quantum numbers)?
- **Standing instruction honoured:** do **not** claim a multiplet the energetics do
  not support.

---

## Validation ladder — status this run

A number is load-bearing only if the regression rungs pass in the same session
(INTERPRETATION §0). The three rungs whose code is on this branch were re-run and
**PASS**:

| Rung | Check | Result | Source |
|------|-------|--------|--------|
| 2+3 | hexatic Green's fn ∫∇²(ln r/2π) = **1.000**; solid r²ln r baseline | PASS | `check_02` |
| 4 | Călugăreanu Lk = Tw + Wr (planar Wr≈0, screw → integer Tw) | PASS | `check_01` |
| 5 | chiral octahedral O: \|O\|=24, Frank classes **{90,120,180}°** | PASS | `check_03` |

Rung 1 (SOSF geometry) and the full Output-A/B/C `sim.run` harness were produced
under **run002** on a different branch and are **inherited, not re-executed here**.
This run adds **no** new gravity (A/C) claim; it works entirely inside the closure
arithmetic that rungs 4 & 5 validate, plus an explicit **[IR]** energy model.

---

## What was computed

### [OC] — the closure spectrum (framework-independent arithmetic)
Screw framing twist per ribbon level: **s = (120/φ²)/360 = 1/(3φ²) = 0.127322
turns/level**, so **1/s = 3φ² = 7.854 levels/turn**. A ribbon closed at depth L has
twist Tw = sL, closes with integer self-linking Lk\* = round(sL), residual writhe
**ε(L) = ‖sL‖**, spin parity = Lk\* mod 2.

Scanning **all** depths L = 1…40, the closure minima (the stable, framed ribbons)
fall at the **fundamental L=8 and its winding harmonics L ≈ 8, 16, 24, 31, 39** —
integer multiples of 1/s = 7.854:

| winding n | depth L | ε(L) | Lk\* | parity |
|---|---|---|---|---|
| 1 | 8  | 0.019 | 1 | **½ (fermion)** ← ground |
| 2 | 16 | 0.037 | 2 | int (boson) |
| 3 | 24 | 0.056 | 3 | **½ (fermion)** |
| 4 | 31 | 0.053 | 4 | int (boson) |
| 5 | 39 | 0.034 | 5 | **½ (fermion)** |

### [IR] — the energy model
> **E(L, Ω, Lk) = w_len·L + w_F·(Ω/120)² + w_W·(Lk − sL)²**

line tension ∝ length; Frank energy ∝ charge² (admissible {120°, 180°}; 90° excluded
by run002's hexatic 6-fold rule); writhe/closure energy ∝ (required writhe)². The
*terms* are standard; identifying **this** functional with the defect energy is the
interpretive step. Defaults w_len=1, w_F=4, w_W=300 (closure-dominant, matching
run002's pinning of the ground state).

Artifacts: `data.csv` (full sorted spectrum), `data.json` (distilled),
`figures/closure_spectrum.png`, `figures/energy_levels.png`.

---

## Results — confirm / refine / falsify

**1. Ground state = isolated spin-½ singlet. [OC arithmetic + IR model]**
(L=8, 120°, Lk=1, spin-½) is the global minimum in **100% (125/125)** of a weight
scan over 0.1×–10× on all three weights — it wins on length, charge *and* closure
at once. → **CONFIRMS** and strengthens run002's ground state. **REFINES** "spin-½
is available" → "the ground state *is* a non-degenerate spin-½ singlet."

**2. No doublet. [OC + IR]**
No near-degenerate low pair, for a structural reason tied to a locked assumption
(CLAUDE.md §2 — the global screw sense is fixed, "DC handedness"):
- the **±writhe partner** Lk=−1 at L=8 needs Wr≈−2.02 not −0.02 → costs ~1222 units;
- a **left/right-handed pair** is not both realised — only the screw-aligned one is.
Smallest gap among the six lowest stable ribbons = **3.3 units ≫ 0**. → **Chirality
lifts the degeneracies that would make a doublet.** A genuine [IR] consequence of the
chiral substrate, not a tuning.

**3. No robust generation multiplet. [OC structure; RH for any SM reading — fenced]**
The (spin-½, 120°) quantum numbers **do recur** at odd-winding harmonics n=1,3,5
(L≈8,24,39), interleaved with even-winding **bosons** at n=2,4 (L≈16,31). But this
is an **infinite winding ladder**, not three replicas; it is **boson-interleaved**,
unlike SM generations; and the **first-excited identity is weight-dependent** —
across the scan it is the **180° same-winding partner (62%)** or the **n=2 boson
harmonic (38%)**, with no single robust "second state." → The energetics **do NOT
support** a clean 3-generation multiplet. The "odd-winding fermion tower ≈
generations" reading is **[RH], fenced (V-§8) — not claimed.**

**4. Charge channels / writhe excitations. [OC + IR]**
The 180° sector is a second tower a fixed Frank gap (×2.25 in charge²) above the
120° tower — split, not degenerate. Fixed-depth writhe excitations (Lk=Lk\*±1) lie
~280 units up — strongly suppressed.

---

## Verdict (answering the run's question)

**Only the single state is robust.** Above the L=8 spin-½ ground state there is **no
doublet** (chirality forbids the degeneracy) and **no robust generation multiplet**
(the excited band is a weight-dependent, boson-interleaved infinite winding ladder).
The ground state is confirmed an **isolated spin-½ singlet**. The recurrence of
spin-½ at odd windings is a real [OC] arithmetic fact whose mapping to physical
generations is **[RH], not established**.

---

## [OC] correction to a prior framing (logged, not silently dropped)

check_03 / run002 listed candidate depths as the **Fibonacci** set {1,2,3,5,8,13,21}
and found L=8 uniquely good *within that set*. Correct as stated — but scanning all
integers shows the true **excited** closures are the **winding harmonics** of L=8
(convergent-denominator depths of 1/(3φ²): L≈16,24,31,39), **not** Fibonacci 13,21
(which close poorly, ε≈0.33). **The ground state L=8 is unchanged**; only the
*excited-depth* description is corrected. Per CLAUDE.md §1 rule 3 the superseded
"Fibonacci-tower" reading is recorded here for the audit trail.

---

## Proposed graduation (for the consolidation session)

These numbers do **not** edit Blocks directly (CLAUDE.md §3.3/§3.5). This run
**refines** Block V's open residual ("the full multiplet / excited spectrum …
remain open"). It is a **negative/structural** result resting on an [IR] energy
model, so a full version bump may not be warranted on its own. Suggested Block V
addition (tag [OC] arithmetic / [IR] model):

- *The excited spectrum above the L=8 ground state is an odd/even-winding ladder
  (winding harmonics of the fundamental, L ≈ 8n). The ground state is an isolated
  spin-½ singlet; the global screw chirality forbids a ground-state doublet
  (±writhe and L/R partners are non-degenerate). No 3-generation structure is
  supported — the spin-½ recurrence at odd windings is [RH], fenced (V-§8).*
- Correct check_03's "Fibonacci-depth" **excited-state** language to "winding
  harmonics of the fundamental L=8" (ground state unaffected).

## Honest residuals (not closed)

- **No absolute energies / masses** — the spectrum is in relative model units; the
  physical-unit lattice energetics (the run002 K_A machinery) are not re-run here.
- The energy functional is an **[IR]** modeling choice. The **robust** conclusions
  (singlet ground; no doublet; weight-dependent first-excited) survive the 0.1×–10×
  scan; the *exact* ordering of the excited band does not, and is not claimed.
- The defect-loop **energies in physical units** and the **numeric K_A** remain the
  open simulator target (run002 `sim.run` harness, on its own branch).

## Reproduce

```bash
pip install -r sim/requirements.txt
python3 sim/checks/check_04_excited_spectrum.py results/run003_excited_spectrum_l8
# validation rungs available on this branch:
python3 sim/checks/check_01_calugareanu_framing.py
python3 sim/checks/check_02_hexatic_greens_function.py
python3 sim/checks/check_03_joining_spectrum.py
```
