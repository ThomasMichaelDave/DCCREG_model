# DCCREG Block V — Emergent Matter: Vortex Defects as Fermions

**Version:** 0.4 (Matter / fermion-gate block)

**Scope of this document:** whether the topological-defect sector of the chiral vortex lattice — the *incompatible* (curvature) sector that Block IV showed *is* matter — can realise **spin-½ fermions** with the correct **spin-statistics connection**, and whether the substrate's primordial chirality fixes **handed (Weyl-like)** fermions. It establishes the defect inventory (disclinations, dislocations, linked/knotted vortex loops) and its identity with the gravity-sector residual; the **screw-as-framing** result (the chiral twist promotes a bare vortex loop to a *ribbon*); the **spin-½ from the belt-trick / Finkelstein–Rubinstein** topology; the **automatic (geometric) spin-statistics connection** for such defects; the identification **spin = self-helicity, statistics = mutual helicity** (Moffatt / Călugăreanu), which ties the framework's primordial conserved pseudoscalar (Block I helicity) directly to the spin-statistics structure; and the chirality → Weyl correspondence. It is the most speculative block of the programme: the topological mechanisms are standard [OC], their identification with the substrate's defects is [IR], and the claim that these *are* the fermions of nature (mass, charge, generations) is [RH] and explicitly fenced.

**Companion documents:** Block I (*Foundations* v0.4), Block II (*MHD Emergence* v0.2), Block III (*Radiative EM* v0.2), **Block IV (*Emergent Gravity* v0.8)**. The defect spectrum of §9 is shared with Block IV: it is simultaneously the matter content (here) and the gravity coefficient $K_A$ (**IV-§3a**). References prefixed **I-§ … IV-§** point to those; unprefixed **§** is internal.

> **Status of this block.** The topological results invoked — that a framed loop (ribbon) realises the $SU(2)$ double cover so a $2\pi$ rotation can give $-1$ (belt trick / Finkelstein–Rubinstein), that the spin-statistics *connection* for such solitons is geometric, that helicity of linked vortex tubes equals their total linking number (Moffatt), and that self-linking $=$ twist $+$ writhe (Călugăreanu–White) — are **standard physics [OC]**. The identifications — that the DCCREG screw supplies the framing, that the dual counter-rotating sublattices are the two fermion chiralities, that helicity is the physical spin charge — are **[IR]**. The claim that these defects are the actual fermions of the Standard Model, the mass mechanism, charge, gauge structure, and generations are **[RH]** and quarantined in §8. **This block does not claim to derive the Standard Model.** It asks the single sharp question — *can these defects be fermions at all?* — and answers it at the level of spin and statistics, honestly tiered.

---

## Revision history

| Version | Date | Author | Summary of changes |
|:--|:--|:--|:--|
| 0.1 | 2026-05-29 | DCCREG Modeling Programme | Initial release — Matter/fermion-gate block (Sections 0–10 and Appendix). Establishes: the defect inventory and its identity with the Block IV gravity residual (the disclination spectrum / Frank constant $K_A$ is *both* the gravity coefficient and the matter content); **screw-as-framing** — the chiral $[1,1,1]$ twist promotes a bare vortex loop to a framed ribbon (verified via Călugăreanu bookkeeping: a planar loop has writhe $0$ and the screw supplies integer self-linking $\mathrm{Lk}=\mathrm{Tw}+\mathrm{Wr}$); **spin-½** from the belt-trick / Finkelstein–Rubinstein $SU(2)$ double cover ($2\pi$ rotation $\neq$ identity for a ribbon); the **automatic spin-statistics connection** (exchange $\cong$ $2\pi$ rotation topologically, so half-integer spin $\Leftrightarrow$ fermi statistics, not assumed); **spin = self-helicity, statistics = mutual helicity** (Moffatt/Călugăreanu) — so Block I's conserved pseudoscalar *is* the spin-statistics charge; and **chirality → Weyl** (the two screw senses / dual sublattices = the two handednesses). The [RH] reach (these as real SM particles, Dirac mass from L–R sublattice coupling, charge/gauge/generations) is fenced in §8. Verdict: the defects *can* carry spin-½ with correct statistics and definite handedness — Kelvin's vortex atom realised at the level of spin-statistics — but this is necessary, not sufficient, for "these are fermions of nature." |
| 0.2 | 2026-05-29 | DCCREG Modeling Programme | **The Joining — defect spectrum partially computed; shared with Block IV (major).** The §9 spectrum is the same object as Block IV's gravity coefficient; the joining computation fixes the parts accessible without the simulator. (1) **Matter charges = chiral octahedral group $O$** (new §2a): the allowed disclination Frank angles are the conjugacy classes of $O$ (order 24, mirror-free — consistent with the screw): **{90°, 120°, 180°}**, the 120° ($C_3$ about $[1,1,1]$) being the screw-aligned, chirality-natural charge (Block I's sector). A discrete, finite charge set — the same set that sources curvature in **IV-§3a**. (2) **Coupling strength = Block III line tension** (§2a): the interaction/stiffness scale $K_A\sim\beta\sim\rho\Gamma^2\ln(d/a)$ — so matter coupling, gravity strength ($G_{\rm eff}\sim1/K_A$, IV-§3a) and light isotropy (III-§6) share one parameter. (3) **Spin-parity selection is Fibonacci** (new §6a): the irrational screw framing ($45.8°=120°/\varphi^2$ per level) never closes by itself, so a closed defect ribbon borrows writhe to make $\mathrm{Lk}$ integer — closure *selects* loops, and the near-closure loops sit at **Fibonacci recursion depths** (1,2,3,5,8,13,21 — the best rational approximants of $1/\varphi^2$). Spin-½ (odd $\mathrm{Lk}$) is available and selectable; the lowest loop's actual parity needs the simulator. (4) **Simulator boundary** restated (§9): stable-loop energies, the lowest matter loop's exact spin/handedness, and the numeric $K_A$ remain open. §2a, §6a added; §9/§10/footer updated; Block IV cross-refs (IV-§3a) added. The §3–7 spin/statistics/Weyl core (v0.1) is unchanged. |
| 0.3 | 2026-05-30 | DCCREG Modeling Programme | **Matter ground state computed — simulator run002 (major).** The stable-defect spectrum (validation ladder 5/5 PASS; run `run002_sosf_spectrum_iterated`, git `ddd7c80`) fixes the ground-state matter loop. (1) **Unique closure at $L=8$**: of the Fibonacci depths {1,2,3,5,8,13,21} the only genuine framing closure is $L=8$ (twist residual 0.019, ~7× better than any other depth ≤21) — sharpening §6a from "Fibonacci-selectable" to "uniquely $L=8$". [OC arithmetic] (2) **Ground-state ribbon: charge 120°, $|\mathrm{Lk}|=1$ (odd) → spin-½, definite handedness (Weyl-capable).** Robust across a 0.1×–10× energy-weight scan (100%). [OC for Lk/closure; IR for "this ribbon is a matter particle"] (3) **Charge fork RESOLVED categorically** (new §2b): an isolated hexatic disclination needs $\psi_6=e^{6i\theta}$ single-valued $\Leftrightarrow 6\Omega\equiv0\ (\mathrm{mod}\,360°)\Leftrightarrow\Omega\in\{120°,180°\}$ — **90° is excluded** (it forces $\psi_6\to-\psi_6$, a string-attached half-disclination); Frank energy $\propto\Omega^2$ then selects **120°**, which is also the screw-aligned $C_3\parallel[1,1,1]$ — doubly natural, **no tunable weight**. [OC selection on the IR hexatic 6-fold] (4) **Caveat recorded**: loosening the closure tolerance past 0.019 readmits the poorly-closed $L=1$ bare loop ($\mathrm{Lk}=0$, boson) — the unframed regime, not a genuine ribbon; so the result is "the *strict-closure* ground state is spin-½", not unconditional. **CONFIRMS the matter gate** at the level of spin/statistics/handedness; the SM-quantum-number map stays [RH], fenced (§8). §2b added; §6a sharpened; §9/§10/footer updated; coupling cross-ref to IV-§3a now carries the computed $K_A\approx0.316\rho\Gamma^2$. The v0.1 spin/statistics/Weyl core is unchanged. |
| 0.4 | 2026-05-30 | DCCREG Modeling Programme | **Excited spectrum — run003 (negative/structural result + correction).** Run `run003_excited_spectrum_l8` (rungs 2–5 PASS; rung 1 + gravity A/C inherited from run002, not re-run) probed the spectrum *above* the L=8 ground state, with the standing instruction not to claim a multiplet the energetics do not support. **(1) Ground state = isolated spin-½ singlet** (new §6b): the global minimum in 100% (125/125) of a 0.1×–10× three-weight scan — wins on length, charge *and* closure at once. Sharpens "the ground state is spin-½" → "a **non-degenerate** spin-½ singlet." [OC arithmetic + IR energy model] **(2) No doublet** — a genuine consequence of a *locked* assumption (the global screw sense is fixed, CLAUDE.md §2): the ±writhe partner ($\mathrm{Lk}=-1$ at $L=8$) needs $\mathrm{Wr}\approx-2.02$ (costs ~1222 units), and only the screw-aligned handedness is realised, so L/R are non-degenerate; smallest gap among the six lowest ribbons ≫ 0. **Chirality lifts the degeneracy that would make a doublet.** [OC + IR] **(3) No robust generation multiplet**: (spin-½,120°) *does* recur at odd-winding harmonics $L\approx8,24,39$, interleaved with even-winding *bosons* at $L\approx16,31$ — but this is an **infinite, boson-interleaved winding ladder**, not three replicas, and the first-excited identity is weight-dependent (180° partner 62% / n=2 boson 38%). The energetics **do not support** a 3-generation structure; the "odd-winding tower ≈ generations" reading is **[RH], fenced (§8)**. **(4) [OC] correction**: run002/check_03 framed the closure depths as *Fibonacci* {1,2,3,5,8,13,21}; scanning all integers shows the true **excited** closures are the **winding harmonics of L=8** (multiples of $1/s=3\varphi^2\approx7.854$: $L\approx16,24,31,39$), **not** Fibonacci 13/21 (which close poorly, $\varepsilon\approx0.33$). **The ground state L=8 is unchanged**; only the *excited-depth* language is corrected (§6a note). Measured bump: a negative/structural result on an [IR] energy model — §6b added, §6a corrected, §9/§10/footer updated. The v0.1–v0.3 core (spin-½ ground state, 120° categorical charge, $K_A$) is unchanged. |

---

## Epistemic tagging legend

- **[OC] Operational Core** — standard, derivable physics/mathematics; true independent of the framework.
- **[IR] Interpretive Reading** — a modeling identification within the framework.
- **[RH] Resonance / Heuristic** — analogical/cosmological; suggestive, not load-bearing.

This is the block where the firewall matters most. The temptation — "topological solitons can be fermions, therefore these defects are electrons" — is exactly the [RH]→[OC] drift the programme forbids. The [OC] core here is narrow and real (spin and statistics are topologically available); everything about *which* particles, *what* masses, and *whether nature uses this* is [RH] and stays in §8.

---

## 0. Inheritance from Blocks I–IV

1. **Helicity is primordial and conserved** — $H=\int\mathbf{u}\cdot\boldsymbol\omega\,dV$, a pseudoscalar = chirality (I-§1, I-§3). Load-bearing here: it becomes the spin-statistics charge (§6).
2. **The chiral screw** — the $[1,1,1]$ golden twist ($\approx45.8^\circ$ per recursion), the two senses = the two signs of $H$ = the dual counter-rotating sublattices (I-§4, I-§13). Becomes the framing (§3) and the handedness (§7).
3. **Matter = the incompatible (defect) sector.** Compatible strain = flat = light; incompatible strain (defects) = curvature = gravity+matter (IV-§5.2). Disclination density $\leftrightarrow$ curvature, dislocation density $\leftrightarrow$ torsion.
4. **The hexatic state** (IV-§5.5): dislocations proliferated, **disclinations** the surviving bound topological objects — the curvature sources, hence the matter candidates.
5. **The shared residual.** The gravity coefficient (Frank constant $K_A$, the disclination interaction strength; IV-§5.5/§10.1) is the *same object* as the matter spectrum (§2, §9). One computation serves both gates.
6. Linked/knotted vortices carry quantised helicity (linking number) — flagged in III-§8 / README §6B as the spin-like pseudoscalar; made precise in §6.

---

## 1. The claim to be tested

> **Fermion-gate hypothesis (README §6B).** Matter is the topological-defect sector of the lattice — disclinations, dislocations, and **linked/knotted vortices** whose quantised helicity (linking number) is a natural spin-like pseudoscalar. The question: do these defects realise **spin-½ matter with the correct spin-statistics**, and does the substrate chirality fix **handed (Weyl-like) fermions**? "Kelvin's vortex atom reborn, with the substrate chirality supplying spin."

The block separates this into three sharp, individually-checkable questions:

- **(S) Spin.** Can a defect carry half-integer angular momentum — transform under the $SU(2)$ double cover? (§3–4)
- **(C) Connection.** If it has spin-½, does it *automatically* obey fermi statistics? (§5)
- **(H) Handedness.** Does the substrate chirality fix the defect's handedness (Weyl)? (§7)

(S)+(C)+(H) answered affirmatively would mean the defects are *fermion-capable with the right structure* — necessary, not sufficient, for "these are the fermions of nature" (§8).

---

## 2. The defect inventory — and its identity with the gravity residual

The hexatic chiral lattice (IV-§5.5) supports the standard 3-D defect zoo:

- **Disclinations** — rotational defects; the curvature sources (IV-§7). In 3-D these are *lines*; closed disclination loops are localised objects.
- **Dislocations** — translational defects; proliferated in the hexatic (they are what melts the positional order), carrying torsion.
- **Linked / knotted vortex loops** — closed vortex filaments with non-trivial linking/knotting; carry helicity (§6).

The matter candidates are the *localised* topological objects: closed disclination loops and linked/knotted vortex loops. Their **spectrum** — which loops are stable, their energies, their topological charges — is precisely the object Block IV left as its quantitative residual (the Frank constant $K_A$ and the disclination spectrum, IV-§10.1). **The gravity coefficient and the matter content are one computation** (§9). **[IR for the identification; OC for the defect taxonomy]**

---

## 2a. The Joining — matter charges and coupling (shared with Block IV)

*(v0.2. This is the matter-side half of the joining computation; the gravity-side half — the same defect spectrum read as the coefficient $K_A$ — is **IV-§3a**. The two are one object.)*

**The matter charges are the chiral octahedral group $O$.** A disclination is labelled by the lattice rotation it fails to close around — an element of the lattice point group. With the screw breaking all mirrors, that group is the **chiral octahedral group $O$** (order 24). Its conjugacy classes give the allowed Frank angles:
$$\{\,90^\circ\ (C_4),\ \ 120^\circ\ (C_3),\ \ 180^\circ\ (C_2)\,\}\qquad(\text{plus the identity}).$$
So the matter sector carries a **discrete, finite charge set fixed by the lattice symmetry**. The **120°** charge is the $C_3$ about $[1,1,1]$ — the screw-aligned, chirality-natural defect (Block I's $120°$ sector). These are the same charges that source curvature in **IV-§3a**: the gravity source content and the matter content are one set. **[OC group theory; IR for "these are the matter quantum numbers"]**

> *Fence ([RH], §8).* That these octahedral charges map onto real particle quantum numbers (electric charge, weak isospin, colour) is **not** claimed. The result is that matter charges form a finite group-theoretic set; identifying that set with the Standard Model is sandbox-tier.

**The coupling strength is Block III's line tension.** The defect interaction/stiffness scale — the Frank constant $K_A$ — is parametrically the **same $\beta$** (vortex line tension) that Block III used for light isotropy, $K_A\sim\beta\sim\rho\Gamma^2\ln(d/a)$ (IV-§3a). So **matter coupling, gravity strength ($G_{\rm eff}\sim1/K_A$), and light isotropy ($\beta=\alpha$) all share one parameter.** *(Computed, v0.3 / run002: $K_A\approx0.316\,\rho\Gamma^2$, $G_{\rm eff}\approx3.16/\rho\Gamma^2$ — IV-§3a.)* **[OC scaling; IR identification]**

---

## 2b. The ground-state charge is fixed categorically — 120° (run002, v0.3)

The §2a inventory lists *allowed* charges {90°,120°,180°}. The simulator's defect-spectrum run sharpens this to a *unique* ground-state charge, by a selection that needs **no tunable energy weight**.

**90° is excluded by single-valuedness.** An isolated disclination in a hexatic must leave the bond-orientational order parameter $\psi_6=e^{6i\theta}$ single-valued around the defect: $6\Omega\equiv0\ (\mathrm{mod}\ 360^\circ)$, i.e. $\Omega$ a multiple of $60^\circ$. The $90^\circ$ ($C_4$) charge fails this — it forces $\psi_6\to-\psi_6$, a *string-attached half-disclination*, not an isolated object. So $90^\circ$ is **categorically excluded**; the admissible isolated charges are $\{120^\circ,180^\circ\}$. **[OC, on the hexatic 6-fold order [IR]]**

**120° wins by Frank energy and is the screw axis.** Among the admissible charges the Frank (orientational) energy $\propto\Omega^2$ selects the smaller, $120^\circ$ — which is *also* the screw-aligned $C_3\parallel[1,1,1]$ (Block I's sector). Doubly natural: lowest-energy admissible *and* chirality-aligned. The ground-state defect therefore carries charge $120^\circ$ with no free parameter. **[OC selection; IR for the hexatic premise]**

This **resolves** the charge fork that §2a left open (which of {90,120,180}° is the matter charge): it is $120^\circ$, fixed by single-valuedness + $\Omega^2$, robust across a 0.1×–10× energy-weight scan (run002). **[OC]**

---

## 3. The screw is the framing — a vortex loop becomes a ribbon

A bare closed curve cannot carry spin: spin requires a **framing** (a ribbon structure — a continuous choice of normal around the loop), because spin is about how the object transforms under rotation, and only a framed object "remembers" rotations. The DCCREG substrate supplies the framing for free.

Every vortex line is threaded by the chiral screw (I-§4): the $[1,1,1]$ twist advances a definite angle per recursion, so the local frame rotates as one moves along the filament. A vortex line is therefore **not a bare curve but a ribbon** — the screw is its framing.

*Bookkeeping check (Călugăreanu–White, $\mathrm{Lk}=\mathrm{Tw}+\mathrm{Wr}$).* For a planar circular vortex loop (writhe $\mathrm{Wr}=0$), a bare framing ($n=0$ turns) gives self-linking $\mathrm{Lk}=0$ — no ribbon. The screw framing ($n\geq1$ turns of the frame around the loop) gives $\mathrm{Tw}=-n$, hence integer self-linking $\mathrm{Lk}=\mathrm{Tw}+\mathrm{Wr}=-n$. **The screw promotes the loop to a genuine ribbon with definite self-linking.** (This is the prerequisite for spin; the spin itself is the rotation property of §4, not the value of $\mathrm{Lk}$.) **[OC for the theorem; IR for "the screw is the framing"]**

---

## 4. Spin-½ from the belt trick (Finkelstein–Rubinstein)

A framed loop (ribbon) realises the double cover $SU(2)\to SO(3)$. This is the **belt trick / Dirac string trick**: give a ribbon a $2\pi$ twist and it *cannot* be undone by moving its ends; give it $4\pi$ and it *can*. So for a framed object, a $2\pi$ rotation is **not** homotopic to the identity, while a $4\pi$ rotation is — exactly $\pi_1(SO(3))=\mathbb{Z}_2$.

Finkelstein–Rubinstein (1968): in a field theory with such solitons, the configuration-space loop corresponding to a $2\pi$ rotation of the soliton is non-contractible, so the quantum state can pick up $-1$ under $2\pi$ rotation — the defect is a **spinor**, carrying half-integer angular momentum. A *bare* loop (no framing, §3) cannot do this; the framed loop can. **The screw-framing is exactly what makes spin-½ available.** **[OC for the mechanism; IR for its realisation by the screw]**

This answers (S): the defects *can* carry spin-½. Whether a given defect *does* depends on its framing parity — a model-spectrum question (§9), not an in-principle obstruction.

---

## 5. The spin-statistics connection is automatic (not assumed)

The strongest [OC] result of the block. For topological solitons, the **exchange** of two identical defects is topologically *the same operation* as a $2\pi$ **rotation** of one of them (Finkelstein–Rubinstein; Sorkin's spin-statistics-for-solitons). The single $\mathbb{Z}_2$ — $\pi_1(SO(3))=\mathbb{Z}_2$, realised on the framed configuration space — governs both. Consequently:

$$\text{spin-}\tfrac12\ (2\pi\text{ rotation}=-1)\quad\Longleftrightarrow\quad \text{fermi statistics}\ (\text{exchange}=-1).$$

The connection is **geometric, not postulated**: a defect that is a spinor is necessarily a fermion, for the same topological reason. This is a genuine virtue — the framework does not have to *impose* the spin-statistics theorem; for its framed-loop defects it is automatic. **[OC]**

This answers (C).

---

## 6. Spin = self-helicity, statistics = mutual helicity — and helicity is the framework's own pseudoscalar

The framework's primordial conserved quantity now becomes the spin-statistics charge, by a standard topological identity. **Moffatt's theorem:** for a set of thin vortex tubes of circulations $\Gamma_i$,
$$H=\int\mathbf{u}\cdot\boldsymbol\omega\,dV=\sum_{i,j}\Gamma_i\Gamma_j\,\mathrm{Lk}_{ij},$$
the total linking. Splitting diagonal from off-diagonal, and using Călugăreanu ($\mathrm{Lk}_{ii}=\mathrm{Tw}_i+\mathrm{Wr}_i$, §3):

- **Self-helicity** $\Gamma_i^2(\mathrm{Tw}_i+\mathrm{Wr}_i)$ — the framing self-linking of one loop $=$ its **spin** charge (§4). **[OC topology; IR identification with spin]**
- **Mutual helicity** $\Gamma_i\Gamma_j\mathrm{Lk}_{ij}\,(i\neq j)$ — the linking of two loops, picked up under exchange/braiding $=$ the **statistics** phase (§5). **[OC topology; IR identification with statistics]**

So the conserved pseudoscalar $H$ of Block I — the very quantity the programme is built around, the chirality — decomposes precisely into **spin (self) + statistics (mutual)**. The substrate's ground philosophy (losslessness ⇒ helicity conserved; mirror-flipping pseudoscalar) is, read at the defect level, the conservation of fermionic spin-statistics charge. This is the block's central structural result. **[OC for the decomposition; IR for the physical identification]**

---

## 6a. The spin-parity selection is Fibonacci (the joining, v0.2)

The spin parity of a defect is the framing self-linking mod 2 (odd $\Rightarrow$ spin-½). The screw sets the framing rate at the irrational $45.8^\circ=120^\circ/\varphi^2$ per recursion, which **never closes to an integer by itself** — so a *closed* defect ribbon must borrow writhe to make $\mathrm{Lk}=\mathrm{Tw}+\mathrm{Wr}$ integer. Closure is therefore a **selection condition**: only loops whose geometry brings the framing to integer self-linking are admissible.

The recursion depths that come closest to closing — the natural near-closure candidates — are the **Fibonacci depths $L = 1,2,3,5,8,13,21,\dots$**, because these are the best rational approximants of $1/\varphi^2$ (the same golden quantity Block I used to *select* the screw angle now *selects* the matter loops). At those depths the accumulated framing twist approaches half- and whole-integer turns, so **spin-½ (odd $\mathrm{Lk}$) is available and selectable**. The same never-settling golden structure that guarantees the substrate's permanence (I-§4, I-§10) reappears as the quantiser of the matter spectrum. **[OC for the framing arithmetic; IR/RH for the Fibonacci-selection reading]**

What this does **not** fix: *which* admissible loop is the lowest-energy one, and hence the actual ground-state matter parity and handedness — that needs the stable-loop energies (§9, simulator). The result here is that the screw makes spin-½ *available and golden-selected*, not that the lowest defect *is* spin-½. **[honest gap]**

**Computed (v0.3, run002 — the gap closed).** The stable-defect run finds a **unique genuine closure at $L=8$**: of {1,2,3,5,8,13,21}, $L=8$ has twist residual 0.019, ~7× better than any other depth ≤21. The ground-state ribbon there carries $|\mathrm{Lk}|=1$ (**odd → spin-½**), charge $120^\circ$ (§2b), definite handedness — robust across a 0.1×–10× weight scan (100%). So "spin-½ available" (above) is sharpened to **"the strict-closure ground state *is* spin-½, at $L=8$."** *Caveat:* loosening the closure tolerance past 0.019 readmits the poorly-closed $L=1$ bare loop ($\mathrm{Lk}=0$, boson) — the unframed regime, not a genuine ribbon; the spin-½ result holds in the strict-closure regime, not unconditionally. **[OC for the closure/Lk arithmetic; IR for "this is the matter ground state"]**

> **[OC] correction (v0.4, run003).** The "Fibonacci depths {1,2,3,5,8,13,21}" framing above is correct *as a candidate set within which $L=8$ is uniquely good*, but it is the wrong description of the **excited** closures. Scanning all integers $L=1\dots40$, the genuine closure minima are the **winding harmonics of the fundamental** — integer multiples of $1/s = 3\varphi^2 \approx 7.854$ levels/turn, i.e. $L\approx 8,16,24,31,39$ — **not** Fibonacci 13 and 21 (which close poorly, $\varepsilon\approx0.33$). **The ground state $L=8$ is unchanged**; only the excited-depth language is superseded. The "golden/Fibonacci quantiser of the *spectrum*" reading is retired in favour of "winding harmonics of $L=8$"; retained here for the audit trail (CLAUDE.md §1 rule 3). The screw angle's golden origin (Block I) still *sets* $s=1/(3\varphi^2)$ — the fundamental is golden; the ladder above it is its integer windings.

---

## 6b. The excited spectrum — an isolated singlet, no doublet, no generations (run003, v0.4)

Run003 probed the spectrum *above* $L=8$ with the standing instruction not to manufacture a multiplet. The result is **negative and structural**, and the negativity is the point.

**The closure ladder.** With framing rate $s=(120^\circ/\varphi^2)/360^\circ = 1/(3\varphi^2)=0.12732$ turns/level, ribbons close at the winding harmonics $L\approx 8n$ ($n=1,2,\dots$), alternating parity:

| winding $n$ | depth $L$ | residual $\varepsilon$ | $\mathrm{Lk}^*$ | parity |
|:-:|:-:|:-:|:-:|:--|
| 1 | 8  | 0.019 | 1 | **½ (fermion)** ← ground |
| 2 | 16 | 0.037 | 2 | integer (boson) |
| 3 | 24 | 0.056 | 3 | **½ (fermion)** |
| 4 | 31 | 0.053 | 4 | integer (boson) |
| 5 | 39 | 0.034 | 5 | **½ (fermion)** |

**(1) The ground state is a non-degenerate spin-½ singlet.** $(L{=}8,\,120^\circ,\,\mathrm{Lk}{=}1)$ is the global minimum in **100% (125/125)** of the three-weight $0.1\times$–$10\times$ scan — it wins on length, charge, *and* closure simultaneously. This sharpens v0.3's "the ground state is spin-½" to "**a non-degenerate spin-½ singlet**." **[OC arithmetic + IR energy model]**

**(2) No doublet — chirality forbids it.** A ground-state doublet would need a near-degenerate partner; none exists, for a reason tied to the *locked* fixed global screw sense ("DC handedness", CLAUDE.md §2 / I-§4):
- the **$\pm$writhe partner** ($\mathrm{Lk}=-1$ at $L=8$) requires $\mathrm{Wr}\approx-2.02$, not $-0.02$ — costing ~1222 units;
- the **L/R-handed pair** is not both realised — only the screw-aligned handedness exists.

The smallest gap among the six lowest stable ribbons is ≫ 0. **Chirality lifts the degeneracies that would make a doublet** — a genuine [IR] consequence of the chiral substrate, not a tuning. **[OC + IR]**

**(3) No robust generation multiplet.** The $(\text{spin-}\tfrac12,120^\circ)$ quantum numbers *do* recur at odd windings ($L\approx8,24,39$) — but this is **not** a 3-generation structure: it is an **infinite** ladder, **boson-interleaved** (even windings $L\approx16,31$ are integer-$\mathrm{Lk}$ bosons, unlike SM generations), and the **first-excited identity is weight-dependent** (the $180^\circ$ same-winding partner in 62% of the scan, the $n{=}2$ boson harmonic in 38%) — no single robust "second state." The energetics **do not support** clean generations. The "odd-winding fermion tower ≈ generations" reading is **[RH], fenced (§8) — not claimed.** **[OC structure; RH for any SM reading]**

**(4) Charge channels.** The $180^\circ$ sector is a second tower a fixed Frank gap ($\times2.25$ in charge²) above the $120^\circ$ tower — split, not degenerate. Fixed-depth writhe excitations ($\mathrm{Lk}^*\pm1$) lie ~280 units up — strongly suppressed.

> **Verdict.** Above the $L=8$ ground state: **no doublet** (chirality forbids the degeneracy) and **no robust generation multiplet** (a weight-dependent, boson-interleaved infinite winding ladder). The ground state is an **isolated spin-½ singlet**. The spin-½ recurrence at odd windings is a real [OC] arithmetic fact whose mapping to physical generations is **[RH], not established**.

*Tier note: the closure ladder and parities are [OC] arithmetic; the energy ordering rests on an explicit [IR] energy functional ($E=w_{\rm len}L + w_F(\Omega/120)^2 + w_W(\mathrm{Lk}-sL)^2$). The robust conclusions (singlet ground; no doublet; weight-dependent first-excited) survive the $0.1\times$–$10\times$ scan; the exact excited-band ordering does not, and is not claimed.*

---

## 7. Chirality → Weyl: the two sublattices are the two handednesses

Helicity is a pseudoscalar — it flips under mirror reflection (I-§1). A framed-loop fermion with a *definite* handedness (a fixed sign of self-helicity, set by the screw sense) is **massless and chiral** — a **Weyl fermion**. The two screw senses (the dual counter-rotating sublattices, the two signs of $H$; I-§4, I-§13) are then the **two chiralities** — left- and right-handed Weyl defects. Mirror reflection swaps the sublattices and the handedness, exactly as it swaps left/right Weyl fermions. **[IR — strong, directly inherited from the primordial-chirality core]**

This answers (H): the substrate chirality fixes the defect handedness; the framework's matter is natively chiral (Weyl), with both handednesses available as the dual structure.

---

## 8. What this does NOT establish — the fence ([RH], quarantined)

Everything past spin/statistics/handedness is heuristic and is **not** load-bearing:

- **These are not shown to be the Standard Model fermions.** That electrons, quarks, neutrinos *are* these specific defects is **[RH]** — unestablished. The block shows fermion-capability, not particle identity.
- **Mass is [RH].** Weyl defects are massless; a Dirac mass needs left–right coupling. A natural-sounding candidate — a defect tunnelling/coupling between the two sublattices (the two handednesses) — would generate it, but this is sketched, not derived, and the magnitude is unknown.
- **Charge, gauge structure, generations — out of scope.** No claim is made that the defect zoo reproduces $U(1)\times SU(2)\times SU(3)$, three generations, hypercharge, or mixing. These are not even framed as forks yet; loose speculation belongs in the sandbox, not here.
- **Quantisation gap.** Treating classical vortex defects as quantum fermions requires a path-integral measure / canonical quantisation argument (the soliton-quantisation step). Finkelstein–Rubinstein establishes the *topological availability*; the full quantisation of the SOSF defects is not carried out here. **[OC-adjacent but not done]**
- **Spin-½ specifically (vs other spins).** The framed loop gives the $\mathbb{Z}_2$ spinor structure; that the lowest matter defects sit at spin-½ rather than spin-$\tfrac32$ etc. is a spectrum question (§9), not settled.

The honest content of the block is exactly §3–7; §8 is the boundary it does not cross.

---

## 9. The shared computation — defect spectrum = gravity coefficient = matter content

One object closes Block IV's residual and populates Block V at once: **the spectrum of stable localised defects of the hexatic SOSF** — closed disclination loops and linked/knotted vortex loops, their energies, their framings (spin parity), their linking charges. From it:

- the **Frank constant $K_A$** and the disclination interaction coefficient — Block IV's quantitative residual (IV-§10.1), fixing the strength of the emergent gravity;
- the **matter content** — which spin-½ (and other) defects exist, their handedness, their self/mutual helicity charges.

**Status after run002 (v0.3).** The simulator boundary the joining left open is now substantially crossed (validation ladder 5/5 PASS). **Computed:** the numeric coupling $K_A\approx0.316\,\rho\Gamma^2$ (IV-§3a); the **ground-state matter loop** — charge $120^\circ$ (§2b), $|\mathrm{Lk}|=1$ → **spin-½**, definite handedness, unique Fibonacci closure $L=8$ (§6a); and the categorical charge selection (90° excluded, 120° by $\Omega^2$ + screw alignment, §2b). **Excited spectrum probed (v0.4, run003).** The spectrum above $L=8$ is now characterised (§6b): an isolated spin-½ singlet ground state, **no doublet** (chirality forbids it), **no robust generation multiplet** (a weight-dependent, boson-interleaved infinite winding ladder, $L\approx8n$). **Still open:** absolute energies/masses in physical units (run003 works in relative model units; the run002 $K_A$ machinery was not re-run), and the [RH] map to real particle quantum numbers (§8). So the gate is closed at ground-state level and *structurally* characterised above it; physical masses and particle identity remain. **[OC arithmetic + IR energy model for §6b; masses and SM-map open]**

---

## 10. Verdict & open forks

**Verdict.** The fermion gate is *open and favourable at the level it can be tested*: the chiral screw frames vortex loops into ribbons (§3), framed loops carry **spin-½** via the $SU(2)$ double cover (§4), the **spin-statistics connection is automatic** (§5), spin and statistics are **self- and mutual-helicity** — the framework's own conserved pseudoscalar (§6) — and the substrate chirality makes the matter natively **Weyl** (§7). This is *Kelvin's vortex atom realised at the level of spin-statistics*, with chirality supplying spin, exactly as the README anticipated. It is **necessary, not sufficient**, for these to be the fermions of nature; mass, charge, gauge structure, generations, and the quantisation measure are unestablished (§8).

**Open forks.**
1. **Defect spectrum — ground state CLOSED, excited spectrum CHARACTERISED (run002+run003, §2b/§6a/§6b/§9).** Numeric $K_A\approx0.316\rho\Gamma^2$; ground state = isolated spin-½ singlet, charge 120°, handedness, $L=8$ (categorical charge). Excited band = winding harmonics $L\approx8n$, no doublet, no generation multiplet (§6b). **Remaining:** absolute defect **energies/masses in physical units** (couple §6b to the run002 $K_A$ machinery — not yet done); convergence of the $E(r)$ coefficient beyond ~10% (finite-torus, IV).
2. **Soliton quantisation.** Carry out the canonical/path-integral quantisation that promotes the classical framed defects to quantum fermions (the measure / Wess–Zumino-type term).
3. **Mass mechanism [RH].** Whether inter-sublattice (L–R) coupling generates a Dirac mass, and its scale.
4. **Spin content.** Which defects sit at spin-½ vs higher; is there a lowest-spin matter doublet?
5. **Charge / gauge / generations [RH→sandbox].** Whether any internal structure of the defect zoo maps to gauge charges or generations — currently sandbox-tier, not a Block fork.
6. **Back-reaction to gravity.** Feed the spin-½ defect $T^{\text{defects}}_{\mu\nu}$ into Block IV (IV-§7) and check consistency of the matter source with the computed $1/k^2$ curvature interaction.

---

## Appendix — symbols & core relations

### Symbols

| Symbol | Meaning |
|:--|:--|
| $H=\int\mathbf{u}\cdot\boldsymbol\omega\,dV$ | helicity (Block I pseudoscalar) $=$ total linking (Moffatt) $=$ spin + statistics charge |
| $\mathrm{Lk},\mathrm{Tw},\mathrm{Wr}$ | self-linking, twist, writhe; $\mathrm{Lk}=\mathrm{Tw}+\mathrm{Wr}$ (Călugăreanu–White) |
| framing / ribbon | the screw-induced normal field promoting a vortex loop to a ribbon (§3) |
| $\pi_1(SO(3))=\mathbb{Z}_2$ | the topological source of spin-½ and of the spin-statistics connection |
| $K_A$ | Frank constant / disclination interaction strength = gravity residual (IV) = matter spectrum scale |
| Weyl L/R | the two screw senses / dual counter-rotating sublattices = the two fermion chiralities |

### Core relations

$$\text{vortex loop} + \text{screw framing} \;\Rightarrow\; \text{ribbon},\qquad \mathrm{Lk}=\mathrm{Tw}+\mathrm{Wr}\quad(\text{Călugăreanu})$$

$$\text{framed loop}\ \xrightarrow{\ 2\pi\ \text{rot}\ }\ -1\quad(\text{belt trick},\ \pi_1(SO(3))=\mathbb{Z}_2)\ \Rightarrow\ \textbf{spin-}\tfrac12\ \ (\text{Finkelstein–Rubinstein})$$

$$\text{exchange}\ \cong\ 2\pi\ \text{rotation}\ \Rightarrow\ \text{spin-}\tfrac12\Leftrightarrow\text{fermi statistics}\quad(\textbf{automatic spin-statistics})$$

$$H=\sum_{i,j}\Gamma_i\Gamma_j\mathrm{Lk}_{ij}:\quad \underbrace{i=j}_{\text{self-helicity}=\text{spin}}\ +\ \underbrace{i\neq j}_{\text{mutual helicity}=\text{statistics}}\quad(\text{Moffatt})$$

$$\text{screw sense}\ (\pm H)\ \Rightarrow\ \text{handedness}\ \Rightarrow\ \textbf{Weyl L/R};\qquad \text{dual sublattices}=\text{the two chiralities}$$

---

*Document status: [exploratory; internally consistent; tiers honest]. Block V v0.4 — **excited spectrum characterised** (run003): the $L=8$ spin-½ ground state is an **isolated, non-degenerate singlet**; **no doublet** (the locked screw chirality forbids the degeneracy) and **no robust generation multiplet** (a weight-dependent, boson-interleaved winding ladder $L\approx8n$) — a negative/structural result on an [IR] energy model. The run002 "Fibonacci excited-depth" framing is corrected to **winding harmonics of $L=8$** (ground state unchanged). Prior (v0.3) — **matter ground state computed** (run002, ladder 5/5): a stable **spin-½** ($|\mathrm{Lk}|=1$, $L=8$), charge **120°** ($C_3\parallel[1,1,1]$), definite-handedness (Weyl-capable) ground-state defect exists; the charge is fixed categorically (§2b: 90° excluded by $\psi_6$ single-valuedness, $\Omega^2$ selects 120°, no tunable weight); spin-½ holds in the strict-closure regime. Coupling computed: $K_A\approx0.316\rho\Gamma^2$ (IV-§3a). SM-quantum-number map stays [RH], fenced (§8). Prior (v0.2) — **The Joining**: the defect spectrum (matter content) is one object with Block IV's gravity coefficient (IV-§3a). Computed: matter charges = chiral octahedral group $O$ ({90°,120°,180°}, §2a); coupling $K_A\sim\beta\sim\rho\Gamma^2\ln(d/a)$ shared with light isotropy and gravity strength (§2a); Fibonacci spin-parity selection (§6a). The v0.1 spin/statistics/Weyl core is unchanged. Block V opens the matter/fermion gate. Core result ([OC]+[IR]): the chiral-screw framing turns vortex loops into ribbons that carry **spin-½** with an **automatic spin-statistics connection**, with **spin = self-helicity and statistics = mutual helicity** (so Block I's conserved pseudoscalar is the spin-statistics charge) and **handedness = chirality** (Weyl). The defect spectrum is the **same computation as the Block IV gravity coefficient** (§9). The [RH] reach — that these are the actual fermions of nature, mass, charge, gauge, generations — is fenced (§8) and not claimed.*
