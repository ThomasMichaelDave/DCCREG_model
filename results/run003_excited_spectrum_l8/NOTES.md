# run003 — Excited / multiplet defect spectrum above the L=8 spin-½ ground state

- **Run:** `run003_excited_spectrum_l8` · **seed:** `0` · **git:** see `params.json`
- **Script:** `sim/checks/check_04_excited_spectrum.py`
- **Target:** the spectrum *above* the closed ground-state gate (run002). The
  ground state is the fundamental screw closure: depth **L=8**, charge **120°**
  (C₃∥[1,1,1]), self-linking **|Lk|=1 (odd → spin-½)**, definite handedness
  (`results/run002_sosf_spectrum_iterated/CONSOLIDATION_REPORT.md`). This run asks
  the open question carried in that report's residuals: **does a doublet or a
  generation-like multiplet sit above L=8, or only the single state?**

Per the firewall (CLAUDE.md §1) and the interpretation contract (`sim/INTERPRETATION.md`
§0): a result here confirms/refines/falsifies an identification **within** DCCREG —
it does not prove the framework. The explicit instruction for this run was *not to
claim a multiplet the energetics do not support*; the verdict below honours that.

---

## Validation ladder — status

Load-bearing only if the regression rungs pass in the same session (INTERPRETATION §0).
The three rungs whose code lives on this branch were re-run and **PASS**:

| Rung | Check | Result | Source |
|------|-------|--------|--------|
| 2+3 | hexatic Green's fn ∫∇²(ln r/2π)=**1.000**; solid r²ln r baseline | PASS | `check_02` |
| 4 | Călugăreanu Lk=Tw+Wr (planar Wr≈0, screw → integer Tw) | PASS | `check_01` |
| 5 | chiral octahedral O: |O|=24, Frank classes **{90,120,180}°** | PASS | `check_03` |

Rungs 1 (SOSF geometry) and the full A/B/C `sim.run` harness were produced under
run002 on branch `claude/simulator-implementation-mZyYb` and are **not present on
this branch** — they are inherited, not re-executed here. This run adds no new
load-bearing claim to gravity (Output A/C); it works entirely inside the closure
arithmetic that rungs 4 & 5 already validate, plus an explicit [IR] energy model.

---

## What was computed

### [OC] — the closure spectrum (framework-independent arithmetic)
The screw framing twist per ribbon level is **s = (120/φ²)/360 = 1/(3φ²) =
0.127322 turns/level**, so **1/s = 3φ² = 7.854 levels/turn**. A ribbon closed at
depth L has natural twist Tw = sL and closes with integer self-linking
Lk\*(L)=round(sL), residual writhe **ε(L)=‖sL‖**, spin parity = Lk\* mod 2.

Scanning all depths L=1…40, the **closure minima** (the genuinely stable, framed
ribbons) fall at the **fundamental L=8 and its winding harmonics L ≈ 8, 16, 24,
31, 39** — i.e. integer multiples of 1/s=7.854, *not* the higher Fibonacci numbers:

| winding n | depth L | ε(L) | Lk\* | spin parity |
|---|---|---|---|---|
| 1 | 8  | 0.019 | 1 | **½** (fermion) ← ground |
| 2 | 16 | 0.037 | 2 | int (boson) |
| 3 | 24 | 0.056 | 3 | **½** (fermion) |
| 4 | 31 | 0.053 | 4 | int (boson) |
| 5 | 39 | 0.034 | 5 | **½** (fermion) |

**Correction to a prior framing [OC].** check_03/run002 listed candidate depths as
the *Fibonacci* set {1,2,3,5,8,13,21} and found L=8 uniquely good *within that set*
(≈7× better than the next). That is correct as stated, but scanning **all** integers
shows the true second-best closures are the **winding harmonics** L=16,24,31,39
(convergent-denominator depths of 1/(3φ²)), **not** the higher Fibonacci numbers
13,21 (which close poorly, ε≈0.33). The **ground state L=8 is unchanged either
way**; only the description of the *excited* depths is corrected. (Per CLAUDE.md §1
rule 3, the superseded "Fibonacci-tower" reading is recorded here, not silently
dropped.) Figure: `figures/closure_spectrum.png`.

### [IR] — the energy model
The ribbon energy (relative units, ρΓ²≡1):
> **E(L, Ω, Lk) = w_len·L + w_F·(Ω/120)² + w_W·(Lk − sL)²**

— line tension ∝ length, Frank energy ∝ charge² (admissible charges {120°,180°};
90° excluded by run002's hexatic 6-fold rule), writhe/closure energy ∝ (required
writhe)². The *terms* are standard physics; identifying **this** functional with
the defect energy is the interpretive step. Defaults w_len=1, w_F=4, w_W=300 put
the closure energy dominant, consistent with run002's finding that closure pins the
ground state. Figure: `figures/energy_levels.png`; full sorted spectrum: `data.csv`.

---

## Results — and what each confirms / refines / falsifies

**1. Ground state is an isolated singlet. [OC arithmetic + IR model]**
(L=8, 120°, Lk=1, spin-½) is the global minimum in **100% (125/125)** of a weight
scan spanning 0.1×–10× on all three weights. It wins on **all three** terms
simultaneously (shortest stable length, lowest admissible charge, best closure), so
no weight choice unseats it. → **CONFIRMS** and *strengthens* run002's ground-state
result (run002 reported 100% over its weight scan; this reproduces it from an
independent enumeration). **REFINES** "spin-½ is available" → "the ground state *is*
a non-degenerate spin-½ singlet."

**2. No doublet. [OC + IR]**
The decisive question was whether a near-degenerate low pair (isospin-like) exists.
It does **not**, for a *structural* reason tied to a locked assumption (CLAUDE.md §2):
the **global screw sense is fixed** ("DC handedness"). Therefore
- the **±writhe partner** Lk=−1 at L=8 is not degenerate with Lk=+1 — it would need
  Wr≈−2.02 instead of −0.02, costing ~1222 units (split, not a doublet);
- a **left/right-handed** pair is not both realised — only the screw-aligned
  handedness exists.
The smallest gap among the six lowest stable ribbons is **3.3 units ≫ 0**: no
accidental near-degeneracy. → **Chirality lifts the degeneracies that would make a
doublet.** This is a genuine [IR] consequence of the chiral substrate, not a tuning.

**3. No robust generation multiplet. [OC for the structure; RH for any SM reading — fenced]**
The same (spin-½, 120°) quantum numbers **do recur** at the odd-winding harmonics
n=1,3,5 (L≈8,24,39), interleaved with even-winding **bosons** at n=2,4 (L≈16,31).
But:
- this is an **infinite winding ladder**, not three replicas;
- it is **interleaved with bosonic states**, unlike SM generations;
- the **first-excited identity is weight-dependent** — across the scan it is the
  **180° same-winding partner** (62%) or the **n=2 boson harmonic** (38%); there is
  no single robust "second state."
→ The energetics **do NOT support** a clean 3-generation multiplet or a fixed
low-lying excited state. The "odd-winding fermion tower ≈ generations" reading is
**[RH]**, fenced (V-§8) — **explicitly not claimed.** This is the honest negative
answer to the run's question.

**4. Charge channels and writhe excitations. [OC + IR]**
The 180° sector is a second tower sitting a fixed Frank gap (×2.25 in charge²) above
the 120° tower — split, not degenerate. Fixed-depth writhe excitations (Lk=Lk\*±1)
lie ~280 units up (closure-energy dominated) — strongly suppressed.

---

## Verdict (answering the run's question)

**Only the single state is robust.** Above the L=8 spin-½ ground state there is **no
doublet** (chirality forbids the degeneracy) and **no robust generation multiplet**
(the excited band is a weight-dependent, boson-interleaved infinite winding ladder).
The ground state is confirmed as an **isolated spin-½ singlet**. The recurrence of
spin-½ quantum numbers at odd windings is a real [OC] arithmetic fact but its
mapping to physical generations is **[RH], not established**.

## What this run does NOT establish
- No absolute energies / masses (no physical-unit lattice energetics; that is the
  run002 K_A machinery, not re-run here). The spectrum is in **relative model units**.
- It does not prove ribbons are particles ([IR]) or that windings are generations ([RH]).
- The energy functional is an [IR] modeling choice; the **robust** conclusions
  (singlet ground, no doublet, weight-dependent first-excited) survive the 0.1×–10×
  scan, but the *exact* level ordering of the excited band does not and is not claimed.

## Graduation note (for a later consolidation session)
This **refines** Block V's open residual ("the full multiplet / excited spectrum …
remain open", run002 report). It does not yet warrant a new Block version on its own
— it is a negative/structural result resting on an [IR] energy model. A consolidation
session could record in **Block V**: *the excited spectrum is an odd/even-winding
ladder with the ground state an isolated spin-½ singlet; chirality forbids a
ground-state doublet; no 3-generation structure is supported [RH fenced]* — and
correct check_03's "Fibonacci-depth" excited-state language to "winding harmonics of
the fundamental L=8" (the ground state is unaffected). Tag: [OC] arithmetic / [IR] model.

## Reproduce
```bash
pip install -r sim/requirements.txt
python3 sim/checks/check_04_excited_spectrum.py results/run003_excited_spectrum_l8
```
