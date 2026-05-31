# DCCREG Simulator — Master Consolidation Index

*Index of all simulator runs on branch `claude/simulator-implementation-mZyYb`.
Each run has its own self-contained `CONSOLIDATION_REPORT.md` (paste-ready for a
consolidation session). Per the firewall (CLAUDE.md §1), every result
confirms/refines/falsifies an identification **within** DCCREG — it does not prove
the framework. Tiers: [OC] operational core / [IR] interpretive reading / [RH]
resonance-heuristic.*

The runs target the joined gravity+matter gate — the **stable-defect spectrum of
the hexatic SOSF** (sim/README.md). They build on each other:

> **run002** (gravity K_A + matter ground state) → **run003** (excited spectrum:
> no doublet) → **run004** (Dirac pairing: the missing partner is inter-sublattice)
> → **run005** (physical scales: dimensional reduction, **B-REDUCED**).

---

## The runs

| Run | Question | Verdict | Report |
|-----|----------|---------|--------|
| `run001_sosf_spectrum` | first full A/B/C pass | **superseded by run002** (audit trail) | — |
| `run002_sosf_spectrum_iterated` | K_A→G_eff (A); E(r) (C); ground-state loop (B) | K_A pinned; ln r form; **spin-½ 120° L=8 ground state** | [run002](run002_sosf_spectrum_iterated/CONSOLIDATION_REPORT.md) |
| `run003_excited_spectrum_l8` | doublet / generation tower above L=8? | **isolated singlet — no doublet, no robust multiplet** | [run003](run003_excited_spectrum_l8/CONSOLIDATION_REPORT.md) |
| `run004_dirac_pairing` | does L↔R inter-sublattice coupling bind a Dirac pair? | **B-YES — Dirac mass = dual-sublattice coupling; axiom survives** | [run004](run004_dirac_pairing/CONSOLIDATION_REPORT.md) |
| `run005_physical_scales` | reduce all quantities to free inputs; is there a parameter-free cross-gate G↔m_D ratio? | **B-REDUCED — base scales cancel (dimensionally); residual $J^2\ln(d/a)^{-3/2}$, no pure number** | [run005](run005_physical_scales/CONSOLIDATION_REPORT.md) |

All runs pass their validation ladder in-session (run004 adds J→0 decoupling and
A↔B mirror invariance; run005 adds dimensional closure and known-limit recovery).

---

## Headline results (with tiers)

**Gravity — Output A (run002).** Lattice Biot–Savart self-energy → line-tension
coefficient **β = 0.0791 ρΓ²** (0.66% from analytic ρΓ²/4π, monotone convergence)
**[OC]**. At the Block III isotropy point ln(d/a)=4: **K_A ≈ 0.316 ρΓ² →
G_eff ≈ 3.16/ρΓ²** **[OC value on the [IR] K_A~β identification]**. A full **3D**
filament sum validates the quasi-2D reduction (straight-line coeff = 2D value to
~1%); the [1,1,1]-screw helix shifts the tension only ~1% **[OC]**.

**Interaction law — Output C (run002).** The triangular-lattice Green's function is
**ln r (1/k², Einstein/Newton form)** — decisively beats the confining r²ln r
**[OC, robust]**; coefficient to ~10% (finite-torus limited). **Screening length**
ξ = κ⁻¹ ∝ n_disloc^(−1/2) (Debye), validated vs the Bessel K₀ to ~2% **[OC law;
[IR] density input]**.

**Matter ground state — Output B (run002).** The **unique genuine screw closure** is
Fibonacci depth **L=8** (~7× better than any other depth), giving **|Lk|=1 (odd) →
spin-½**, definite handedness **[OC]**. **Charge fork resolved:** 6-fold hexatic
single-valuedness (ψ₆=exp(6iθ)) excludes 90° categorically and Frank energy ∝Ω²
selects **120°** (C₃∥[1,1,1]) **[OC on the [IR] hexatic 6-fold]**.

**Excited spectrum (run003).** Above L=8: an **isolated spin-½ singlet** — **no
doublet** (global chirality lifts the ±writhe and L/R degeneracies) and **no robust
generation multiplet** (the excited band is a weight-dependent, boson-interleaved
winding ladder L≈8n) **[OC arithmetic; RH for any SM generation reading, fenced]**.
Corrected the prior "Fibonacci-tower" excited-depth language to winding harmonics
(ground state unchanged).

**Dirac pairing (run004).** The two opposite-handed L=8 ribbons on the dual
sublattices (Lk=±1) are **exactly degenerate (E_A=E_B) [OC]**; the mutual-helicity
coupling (|Lk_AB|=1, reinforcing) binds them into a bonding/antibonding pair whose
**net-Lk-0 mixing is a Dirac mass term [OC arithmetic / IR identification]**.
**B-YES:** the "missing partner" from run003 is on the other sublattice — the
**fixed-global-chirality axiom survives**; the inter-sublattice coupling **is** the
Block V-§8 Dirac-mass mechanism. Mass magnitude ∝ J (unfixed without K_A).

**Physical scales — run005 (B-REDUCED).** Every sector quantity reduces to
$\{\rho,\Gamma,\ell_P\}\times g(J,\ln d/a)$ ($+\kappa$ EM, $+n_d$ screening); **dimensional
closure PASS** — no hidden input, confirming the declared free-parameter count **[OC]**.
Two emergent scales identified **[IR]**: $\hbar_{\rm eff}\sim\rho\Gamma\ell_P^3$ and
$c\sim(\Gamma/\ell_P)\sqrt{\ln d/a}$. Cross-gate $(m_D/m_{\rm Planck})^2\to J^2\ln(d/a)^{-3/2}$:
the base scales cancel, **but dimensionally** (the generic property of a dimensionless
ratio on a 3-constant basis — *not* a structural signature of sector-sharing); content
is in the residual exponents, tier **[OC arithmetic on the [IR] reduced forms]**. **No
parameter-free cross-gate number** — held open by the missing external $\hbar$, free $J$,
and inexact $\ln(d/a)\approx4$. Input-independent pure numbers are **intra-sector** only
($3\varphi^2$, charge $2.25$, $L\approx8n$). Located gap: one $O(1)$ prefactor + an exact
$\ln(d/a)$. (No SI absolutes — by design.)

---

## Proposed graduations (for the consolidation session)

Numbers do **not** edit Blocks directly (CLAUDE.md §3.3/§3.5). Suggested, per run:

- **Block IV → v0.8 "K_A computed"** (run002): K_A ≈ 0.316 ρΓ², G_eff ≈ 3.16/ρΓ²
  [OC value, IR id]; 3D quasi-2D-reduction validation; the Debye screening law
  ξ ∝ n_d^(−1/2) refining the §5.6 "atmosphere". Supersede the parametric K_A~β
  statement (→ History).
- **Block V → v0.3 "matter ground state"** (run002): spin-½, 120° (C₃∥[1,1,1]),
  definite handedness, L=8; the 6-fold admissibility rule fixing the charge [OC].
- **Block V → v0.4 / note "excited spectrum"** (run003): isolated spin-½ singlet;
  chirality forbids a ground-state doublet; no 3-generation structure [RH fenced];
  correct check_03's excited-depth language to winding harmonics.
- **Block V → v0.5 "Dirac pairing"** (run004): inter-sublattice coupling = the
  Dirac-mass mechanism; moves the §8 mass [RH] → [IR]; **affirms** the I-§4
  fixed-global-chirality axiom (no Block I revision); add cross-ref V-§8 ↔ I-§13.
- **Block IV → v0.9 / Block V → v0.6 "physical-scale reduction"** (run005): record the
  reduced accounting (every quantity $=\{\rho,\Gamma,\ell_P\}\times g(J,\ln d/a)$, closure
  PASS) [OC]; the cross-gate scaling $(m_D/m_{\rm Planck})^2\to J^2\ln(d/a)^{-3/2}$ with the
  **cancellation tagged dimensional, not structural** [OC-on-IR]; the $\hbar_{\rm eff}\sim
  \rho\Gamma\ell_P^3$ and $c\sim\Gamma/\ell_P$ identifications **[IR]** with the cross-ref
  that $\hbar_{\rm eff}$ presupposes the un-done soliton quantisation (V-§10 fork 2); add
  bidirectional IV-§3a ↔ V-§9. Accounting refinement, **not** a new mechanism — residual/
  fork sections only, no body rewrite. SM map stays [RH], fenced. *(Applied: Block IV
  v0.9, Block V v0.6, README + frontier.)*

---

## Honest residuals carried across the runs

- **No physical masses / absolute energies / no SI numbers.** Output C's coefficient
  is ~10% (finite-torus); run003/run004 spectra are in relative units; run004's Dirac
  mass ∝ J. run005 makes this precise: absolute values would require inventing the
  free inputs — forbidden. The framework's content is the input-independent ratios.
- **The cross-gate base-scale cancellation is dimensional, not structural.** $\{\rho,\Gamma,
  \ell_P\}$ span $\{M,L,T\}$, so *any* dimensionless ratio loses them; the cancellation is a
  corollary of dimensional closure, not independent evidence of the Joining. The sharing
  shows only in the residual exponents.
- **$\hbar_{\rm eff}$ is not a derived $\hbar$.** $\rho\Gamma\ell_P^3$ is a valid action [OC],
  but identifying it with the defect spin $=\hbar/2$ presupposes the soliton quantisation
  (V-§10 fork 2 / §8), which is not done. $m_{\rm Planck}$ is therefore internally defined.
- **The cross-gate ratio is an internal scaling relation, not yet measurable.** Confronting it
  with data needs the external-$\hbar$/SI step the run (correctly) refuses. The currently
  input-independent predictions are the intra-sector pure numbers only.
- **[IR] energy functional.** The ribbon/coupling functionals are interpretive; the
  closure/Lk/linking/degeneracy arithmetic and the validation rungs are [OC].
- **[RH], fenced (V-§8):** the map to real Standard-Model quantum numbers
  (generations, electroweak isospin) — not claimed, in any run.

## Reproduce

```bash
pip install -r sim/requirements.txt
python -m sim.run                                              # run002: ladder + Outputs A/B/C
python3 sim/checks/check_05_dirac_pairing.py results/run004_dirac_pairing    # run004
python3 sim/checks/check_06_physical_scales.py results/run005_physical_scales # run005
# (run003's check_04 was not pushed to this branch; its machinery is reconstructed
#  inside check_05 and fully specified in results/run003_excited_spectrum_l8/NOTES.md)
```
