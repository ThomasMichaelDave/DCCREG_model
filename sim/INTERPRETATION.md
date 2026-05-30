# DCCREG Simulator — Interpretation Contract

**Read `../CLAUDE.md` and `README.md` (target spec) first.** This file answers: *what does each output mean, and what would confirm, refine, or falsify which claim?* It is the contract that makes a number meaningful before any code is written.

---

## 0. The one principle

Every simulator output does exactly one of three things to an existing claim: **confirm**, **refine**, or **falsify** it. A number that does none of these (decorative, untraceable to a claim) is not a result. And per CLAUDE.md §1: a result **confirms/refines/falsifies an [IR] identification — it does not prove the framework**.

A number counts only when (a) the validation ladder (`README.md`, items 1–5) passes in the same run, and (b) it has converged (stable as lattice size grows). A new number arriving while regression checks fail is a **bug, not a result**.

---

## 1. The three outputs and what each decides

### Output A — the coefficient `K_A` → `G_eff`
**What it is:** the numeric value of the Frank constant from the lattice Biot–Savart sum, with convergence error bars; hence `G_eff ~ 1/K_A`.

**Reads:**
- **Confirms** the `K_A ~ β ~ ρΓ²ln(d/a)` identification (IV-§3a, V-§2a) if it lands `O(1)·ρΓ²` at `ln(d/a)≈4`.
- **Refines** the gravity strength: turns the parametric "∼" into a number, fixing `G_eff`.
- **Falsifies** the `K_A ~ β` identification [IR] if it is orders-of-magnitude off the line-tension scale — which would mean the disclination stiffness is *not* the light-isotropy stiffness, breaking the "one shared parameter" result.

### Output B — the defect spectrum + ground-state loop  ← **the decisive test**
**What it is:** a dataset (one row per candidate loop: energy, octahedral charge, Lk/Tw/Wr, handedness, stable?), distilled to *the lowest-energy stable loop* and its spin parity (Lk mod 2) and handedness.

**Reads:**
- **Confirms** the matter gate (Block V §3–7) at the strongest available level **if** a *stable* loop exists with **odd Lk = spin-½** and definite handedness (Weyl). This is the result the whole matter block is reaching for: a stable spin-½ Weyl ground state.
- **Refines** "spin-½ is available/Fibonacci-selectable" (V-§6a) into "the ground state *is* (or is not) spin-½."
- **Falsifies** "matter = the defect sector" [IR] **if** no stable localized loop exists, or if the lowest stable loop is even-Lk (a boson) with no spin-½ state nearby. Either would mean the defects cannot be the fermions.

### Output C — the interaction law `E(r)` (consistency)
**What it is:** energy-vs-separation for two defects on the real lattice.

**Reads:**
- **Confirms** the v0.6 closure if it recovers the `ln r` (1/k²) Einstein/Newton form (check_02) *with the real lattice coefficient*.
- **Refines** by showing where finite-size / screening (the "atmosphere", IV-§5.6) bends `E(r)` away from `ln r` — i.e. the screening length `κ`, a bounded prediction.
- **Falsifies** the hexatic-screening picture [IR] if `E(r)` stays `r²ln r` (1/k⁴, confining) at large `r` — meaning the lattice did *not* melt to the hexatic and the Einstein-form closure (IV-§5.5) does not apply.

---

## 2. The decision table (what each result means for the programme)

| Result | Meaning | Block action |
|--------|---------|--------------|
| `K_A` converges, `O(1)·ρΓ²` | gravity strength pinned; shared-parameter confirmed | IV v0.8 "K_A computed" [OC value, IR id] |
| `K_A` far off line-tension scale | `K_A~β` identification wrong | IV: demote the shared-parameter claim to History; flag |
| stable **odd-Lk** ground loop, definite handedness | spin-½ Weyl matter exists — matter gate's strongest result | V v0.3 "matter ground state" [OC+IR] |
| stable **even-Lk** lowest loop | matter is bosonic at ground; spin-½ excited only | V: refine §6a; reassess fermion claim |
| **no stable** localized loop | "matter = defects" fails at this level | V: record falsification; matter gate reopens |
| `E(r) → ln r` with lattice coeff | Einstein-form closure confirmed numerically | IV: upgrade §5.5 from "conditional" toward "computed" |
| `E(r) → r²ln r` at large r | not hexatic; Einstein closure void | IV: reopen Fork-1; hexatic identification falsified |

Note the symmetry: **every row has a falsification branch.** That is the point — the simulation is built to be able to kill claims, not only support them.

---

## 3. From number to Block (the graduation step)

A converged, validated number does **not** edit a Block directly (CLAUDE.md §3.2/§3.5). It graduates:

1. Run passes the validation ladder; result converges; `results/<run>/NOTES.md` tags every claim [OC]/[IR]/[RH] and states what it confirms/refines/falsifies (this doc, §1).
2. A **consolidation session** updates the target Block: bump version, add a revision-history row, move the prior version to `docs/archive/`, update cross-refs (IV-§3a ↔ V-§2a/§9), move the superseded *parametric/conditional* statement to a History note, record the new number **with its tier and its run id**.
3. Suggested graduations: `K_A`→`G_eff` ⇒ **Block IV v0.8**; ground-state loop ⇒ **Block V v0.3**. One run feeds both (the joining).

---

## 4. What a result never does

- It never promotes [RH] to [OC]. A stable spin-½ Weyl loop confirms *fermion-capability*; it does **not** make these the electrons/quarks of nature (that stays [RH], fenced in V-§8).
- It never "proves DCCREG." It confirms/refines/falsifies a specific identification within it.
- It is never reported without its convergence log and validation-ladder status.
