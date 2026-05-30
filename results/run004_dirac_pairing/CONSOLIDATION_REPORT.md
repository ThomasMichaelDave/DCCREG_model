# DCCREG Simulator — Consolidation Report (run004: Dirac pairing)

*Self-contained handoff for a consolidation session. Paste this whole file into a
Claude conversation. It records what the simulator computed, each result's tier
([OC] operational core / [IR] interpretive reading / [RH] resonance-heuristic),
and what each confirms / refines / falsifies. Per the firewall (CLAUDE.md §1), a
result confirms/refines/falsifies an identification **within** DCCREG — it does
not prove the framework.*

- **Run:** `run004_dirac_pairing`  ·  **seed:** `0`  ·  **git:** see `params.json` (`9887fba`)
- **Branch:** `claude/simulator-implementation-mZyYb`
- **Script:** `sim/checks/check_05_dirac_pairing.py`
- **Brief:** `sim/RUN004_dirac_pairing_brief.md` (branches from the run003 closure/energy machinery)
- **Target:** the **inter-sublattice (L↔R) coupling** of the run002/run003 ground
  ribbon — depth **L=8**, charge **120°** (C₃∥[1,1,1]), self-linking **|Lk|=1
  (spin-½)**, definite handedness.
- **The question:** does the L↔R coupling **bind** the L=8 ribbon on sublattice A
  (Lk=+1) to its opposite-handed partner on sublattice B (Lk=−1) into a
  **near-degenerate Dirac pair** (whose A↔B mixing is a mass term), or leave them
  **split/unbound**?
- **Why it exists:** run003 found the ground state is an **isolated singlet — no
  doublet** — because the *fixed global screw sense* (locked axiom, CLAUDE.md §2 /
  I-§4) realises only one handedness. This run tests possibility **(b)** of the
  brief — that the second handedness already lives on the *other* sublattice
  (I-§13's dual counter-rotating structure) — **before** touching the axiom (c).
- **Standing instruction honoured:** the axiom is **not** relaxed here; only a
  B-NO would put it on the table. B-YES / B-NO / B-AMBIGUOUS were **pre-committed
  in the brief** so the result cannot be tuned into being.

---

## Validation ladder — status this run

A number is load-bearing only if the regression rungs pass in the same session
(INTERPRETATION §0). The inherited rungs were re-run **and** the brief's two **new**
two-sublattice self-tests were added; **all pass**:

| Rung | Check | Result | Source |
|------|-------|--------|--------|
| 1 | SOSF geometry reproduces §A.7 + structural counts | PASS | `geometry/sosf` |
| 2 | solid disclination r²ln r (1/k⁴) baseline; slope 2.19 | PASS | `check_02` |
| 3 | hexatic Green's fn ∫∇²(ln r/2π) = **1.000** (Einstein form) | PASS | `check_02` |
| 4 | Călugăreanu Lk = Tw + Wr (planar Wr≈0, screw → integer Tw) | PASS | `check_01` |
| 5 | chiral octahedral O: \|O\|=24, Frank classes **{90,120,180}°** | PASS | `check_03` |
| **NEW** | **J→0 decoupling** — two independent run003 singlets, no spurious binding (gap=0, both levels = 12.1035) | **PASS** | this run |
| **NEW** | **A↔B mirror invariance** — Δ(J) unchanged under A↔B + screw-sense swap (max\|diff\|=0) | **PASS** | this run |

A Δ(J) arriving while these fail is a bug, not a result (brief §5). They pass, so
Δ(J) is load-bearing.

---

## What was computed

### [OC] — the exact A↔B degeneracy (the doublet's necessary condition)
The two sublattices carry opposite screw rates **s₊ = +1/(3φ²)**, **s₋ = −1/(3φ²)**.
Both support the run003 L=8 closure, with opposite self-linking: **Lk_A = +1**,
**Lk_B = −1**, each with closure residual **ε = 0.0186**. The run003 energy depends
on the closure through **(Lk − sL)²**, which is **identical** when *both* s and Lk
flip sign — so

> **E_A = E_B = 12.1035** (relative units, ρΓ²≡1) — **EXACTLY degenerate.**

This mirror degeneracy is a framework-grounded **[OC]** fact, not a tuning; it is
the necessary condition for a Dirac doublet.

### [OC] — the mutual-helicity coupling unit
The inter-sublattice coupling is the mutual helicity Γ_AΓ_B·Lk_AB (Moffatt
off-diagonal, V-§6). The elementary mutual linking is fixed by a **Gauss linking
integral**: **|Lk_AB| = 1** for the elementary linked (Hopf) configuration
(computed −1.000), **0** for the unlinked reference (computed 0.000). Counter-
rotating sublattices give **Γ_AΓ_B = −1** (I-§13: counter-rotating neighbours
reinforce), so the natural **reinforcing coupling unit is M₀ = −1**. The coupling is
`t = J·M₀`, with **J scanned 0.1×–10×** the mutual-helicity unit (brief §3–4).

### [IR] — the energy model and the coupling identification
Single-ribbon energy inherited from run003:
> **E(L, Ω, Lk) = w_len·L + w_F·(Ω/120)² + w_W·(Lk − sL)²**, defaults (1, 4, 300).

Two-ribbon Hamiltonian:
> **H = [[E_A, t], [t, E_B]]**,  t = J·M₀.

The *terms* are standard; identifying **this** functional with the defect energy and
the **mutual-helicity off-diagonal with the inter-sublattice coupling / Dirac mass**
is the interpretive step (**[IR]**).

Artifacts: `data.csv`, `data.json` (the Δ(J) scan + pair quantum numbers),
`figures/gap_vs_J.png`, `figures/level_diagram.png`.

---

## Results — confirm / refine / falsify

**1. The pair binds into a bonding/antibonding doublet. [OC arithmetic + IR coupling]**
Diagonalising H at the **natural scale J = 1**: bonding **11.104**, antibonding
**13.104**, **gap Δ = 2.000**. The bonding state is **bound** (11.104 < E₀ = 12.104),
and the gap is **below the first-excited gap (5.00)** → a **near-degenerate
low-lying pair**, not split. → **CONFIRMS** that the opposite-handed partner binds.

**2. The mixing is a Dirac mass. [OC + IR]**
Both mixed eigenstates carry **net Lk = 0** (the symmetric/antisymmetric combinations
of Lk=±1) — they are **non-chiral**. So the A↔B coupling turns the two chiral **Weyl**
ribbons (Lk = ±1, massless) into **massive Dirac** states: the off-diagonal coupling
**is** a mass term. → **REFINES** Block V-§8's flagged mass **[RH]** mechanism into a
**computed [IR]** one (the doublet/mass = the dual-sublattice coupling).

**3. The "missing partner" was on the other sublattice — the axiom survives. [IR]**
run003's absent doublet was an artefact of modelling **one** sublattice. With the
dual structure (I-§13) present, the partner exists on B and the coupling binds it.
The **fixed-*global*-chirality axiom (CLAUDE.md §2 / I-§4) is NOT falsified** —
global handedness stays DC-fixed; the *local* dual structure supplies both
chiralities, exactly as I-README §2.3 anticipated. → This is the brief's **B-YES**
branch: the axiom holds, and Block I needs **no** chirality revision.

**4. Robustness across the J-scan. [OC]**
The degeneracy (E_A=E_B) and the mass signature (net Lk=0) are **J-independent**;
the bonding state is bound for all J>0 and the verdict does **not flip**. The pair is
near-degenerate through the natural-J window; the antibonding member merges with the
excited band only at **strong coupling J ≳ 2.5** (Δ > 5.00). The **mass magnitude
∝ J** and is **not fixed** without physical units for J (see residuals).

---

## Verdict — BRANCH **B-YES** (partner found; axiom holds; doublet = mass mechanism)

The opposite-handed A and B L=8 ribbons are **exactly degenerate [OC]** and the
nonzero, mirror-symmetric mutual-helicity coupling binds them into a
**bonding/antibonding pair whose net-Lk-0 mixing is a Dirac mass term**. At natural
J the pair is near-degenerate and low-lying; the J→0 limit recovers two independent
run003 singlets and the A↔B mirror swap leaves Δ(J) invariant. The second handedness
was on the other sublattice all along — **the fixed-global-chirality axiom survives
intact**, and the inter-sublattice coupling **is** the Dirac-mass channel Block V-§8
had flagged [RH].

---

## Proposed graduation (for the consolidation session)

These numbers do **not** edit Blocks directly (CLAUDE.md §3.3/§3.5). Suggested:

- **Block V → v0.5 "Dirac pairing":** record that the inter-sublattice (A↔B)
  coupling of the two opposite-handed L=8 ribbons is the **Dirac-mass mechanism** —
  the doublet is the dual counter-rotating sublattice structure (I-§13), and the
  mixing of the Lk=±1 Weyl chiralities into net-Lk-0 states **is** the mass term.
  This **moves the V-§8 mass identification from [RH] toward [IR]** (mechanism
  computed, magnitude pending). Affirm explicitly that the **fixed-global-chirality
  axiom (I-§4) is confirmed, not questioned** — global handedness DC-fixed, local
  dual structure supplies both chiralities. Add cross-ref V-§8 ↔ I-§13.
  Tag: **[OC]** degeneracy + binding arithmetic + linking unit; **[IR]** "this is
  the Dirac mass"; the absolute mass scale awaits the run002 K_A units.
- **No Block I revision** is warranted (that was the B-NO branch's action, not
  triggered).

## Honest residuals (not closed)

- **No physical mass.** Δ is in relative model units and **scales with J**; the
  absolute Dirac mass needs J pinned in physical units from the mutual-helicity
  term — i.e. the **run002 K_A machinery** (brief §6). Until then the *mechanism* is
  established, the *value* is not.
- The energy functional and the **"coupling = mass"** identification are **[IR]**;
  the mutual-linking magnitude (|Lk_AB|=1) and the degeneracy are **[OC]**.
- The map to real **electroweak doublets / isospin** stays **[RH], fenced (V-§8)** —
  not claimed, in any branch.
- The coupling is modelled as the elementary mutual-helicity unit scanned by J; a
  first-principles lattice computation of the A–B mutual linking on the real SOSF
  skeleton remains open.

## Reproduce

```bash
pip install -r sim/requirements.txt
python3 sim/checks/check_05_dirac_pairing.py results/run004_dirac_pairing
# validation rungs available on this branch:
python3 sim/checks/check_01_calugareanu_framing.py
python3 sim/checks/check_02_hexatic_greens_function.py
python3 sim/checks/check_03_joining_spectrum.py
```
