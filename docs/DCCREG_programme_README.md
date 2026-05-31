# DCCREG Programme — README & Handoff

**What this is.** An exploratory, internally-disciplined theoretical-physics construction: deriving electromagnetism, magnetohydrodynamics, and light as *emergent* phenomena of a hypothetical sub-Planck **chiral fluid substrate** (DCCREG). It is a "what-if" model-building programme, **not** established physics. Its integrity comes not from being true but from an explicit epistemic firewall (below) and from honest, versioned consolidation of every step. A fresh assistant instance should read this README, then Blocks I → II → III → IV, and resume at the frontier (§ "Current frontier").

> **Changelog — README v1.7 (2026-05-30).** **Dirac-pairing run graduated; a locked axiom stress-tested and held** (run `run004_dirac_pairing`; validation ladder + two new gating rungs PASS — J→0 decoupling and A↔B mirror invariance). Block V → **v0.5**: the two opposite-handed L=8 Weyl ribbons on the dual sublattices (I-§13) are exactly degenerate and bind via mutual helicity into a **massive Dirac** pair — the run003 "missing partner" is **inter-sublattice**, the coupling **is** the §8 Dirac-mass mechanism (§8 mass [RH]→[IR]; magnitude ∝ J still open), and the **fixed-global-chirality axiom (I-§4) is AFFIRMED** (the pre-committed B-NO branch would have opened a Block I revision — it didn't). New §7a; cross-ref V-§8 ↔ I-§13. SM electroweak-isospin map stays [RH], fenced. A `results/MASTER_CONSOLIDATION_INDEX.md` now indexes runs 001–004. Map → matter v05. *(All four runs' full per-run reports are now under `results/`; `MASTER_CONSOLIDATION_INDEX.md` indexes them.)*
>
> **Changelog — README v1.6 (2026-05-30).** **Excited-spectrum run graduated** (run `run003_excited_spectrum_l8`; rungs 2–5 PASS, rung 1 + gravity A/C inherited from run002). Block V → **v0.4**: the $L=8$ spin-½ ground state is an **isolated non-degenerate singlet**; **no doublet** (the locked global screw chirality forbids the degeneracy) and **no robust generation multiplet** (a weight-dependent, boson-interleaved winding ladder $L\approx8n$) — a disciplined *negative* result on an [IR] energy model. **Correction:** the run002 "Fibonacci excited-depth" language is superseded by "winding harmonics of $L=8$" (ground state unchanged). SM-particle/generation map stays [RH], fenced. Map → matter v04. *(Note: `sim/checks/check_04_excited_spectrum.py` lives on the Claude Code branch `claude/excited-spectrum-l8-uyAlt`; its consolidation report is archived under `results/run003_excited_spectrum_l8/`.)*
>
> **Changelog — README v1.5 (2026-05-30).** **First simulator results graduated** (run `run002_sosf_spectrum_iterated`, validation ladder 5/5 PASS). Block IV → **v0.8**: $K_A$ **computed** ($\approx0.316\,\rho\Gamma^2$, $G_{\rm eff}\approx3.16/\rho\Gamma^2$), quasi-2D reduction validated in 3D (~1% screw correction), Debye screening length $\xi\propto n_d^{-1/2}$, $E(r)$ confirms $\ln r$ Einstein form on the real lattice. Block V → **v0.3**: ground-state matter loop = **spin-½**, charge **120°** ($C_3\parallel[1,1,1]$), definite handedness, unique closure $L=8$; charge fixed **categorically** (90° excluded by $\psi_6$ single-valuedness). Map updated to v08/v03. SM-particle identity stays [RH], fenced.
>
> **Changelog — README v1.4 (2026-05-29).** **The Joining.** Block IV → **v0.7** and Block V → **v0.2**: the SOSF defect spectrum is established as one object across both gates. Computed: matter charges = chiral octahedral group $O$ ({90°,120°,180°}; IV-§3a = V-§2a); gravity coefficient $K_A\sim\beta\sim\rho\Gamma^2\ln(d/a)$ — Block III's line tension, so **light isotropy, gravity strength, and matter coupling share one parameter**; Fibonacci spin-parity selection (V-§6a). Bidirectional cross-refs added (IV-§3a ↔ V-§2a/§9). Remaining = the numeric defect spectrum (simulator). Map updated to v07/v02.
>
> **Changelog — README v1.3 (2026-05-29).** Opened **Block V** (emergent matter / fermion gate): the chiral-screw framing makes vortex loops into ribbons carrying **spin-½** with an **automatic spin-statistics connection**; **spin = self-helicity, statistics = mutual helicity** (so Block I's conserved pseudoscalar is the spin-statistics charge); **handedness = chirality** (Weyl). The defect spectrum is the **same computation as the Block IV gravity coefficient**. The [RH] reach (these as real SM particles, mass, charge, gauge, generations) is fenced. Added Block V to the map (V-§), spine, and frontier; cross-ref scheme extended to V-§.
>
> **Changelog — README v1.2 (2026-05-29).** Block IV advanced v0.3 → **v0.6**: gravity identified as **Coulomb-gauge** (instantaneous strong Newtonian potential + weak finite-c graviton); gravity's weakness derived as the **unscreened Coulomb residual**; the **defect/curvature gate closed on the Einstein side** by computation (hexatic SOSF ⇒ disclination interaction = Laplacian Green's function = $1/k^2$ Newtonian/Einstein form), conditional on the [IR] hexatic identification; **α₁ = 0 forced**; boundary-condition/screening ("atmosphere") section added. README map and §5/§6 spine refreshed accordingly. Added the v0.2→v0.3 Fierz–Pauli correction and v0.6 closure to the audit trail. No change to the locked assumptions or the firewall.

---

## 1. Epistemic discipline — read first, non-negotiable

Every substantive claim carries one of three tags:

- **[OC] Operational Core** — standard, derivable physics/mathematics; true independent of the framework.
- **[IR] Interpretive Reading** — a modeling identification *within* the framework; internally consistent, chosen rather than forced.
- **[RH] Resonance / Heuristic** — analogical or cosmological; suggestive, not load-bearing.

Keep the tiers honest. Do not let [RH] drift into [OC]. The programme's value is the firewall; collapsing it destroys the work. The user prizes honest pushback and self-correction over validation.

---

## 2. Locked assumptions — do **not** "fix" these

The substrate is an **ideal, incompressible, lossless Euler fluid** with **infinite sound speed** (instantaneous pressure transmission), structured down to the **Planck length** ℓ_P, intrinsically **chiral**, plasma-like under rotative agitation, and MHD-like at higher scale. Standing principles (treat as given):

1. **Infinite sound speed is intentional.** Do not impose human-scale perceptual limits or try to make it finite. It is the incompressible limit and does real work (instantaneous Coulomb sector; cures the elastic-aether longitudinal-light flaw; supplies the khronon foliation in IV).
2. **Losslessness ⇒ helicity is the ground philosophy.** H = ∫ u·ω dV is a conserved pseudoscalar that flips sign under mirror reflection. The mirror/dual character is inherent.
3. **Screw sense fixes *global* helicity ("DC handedness"); helicity *density* u·ω varies pointwise**, so locally opposite-handed cells form while the global integral is conserved.

---

## 3. Working conventions

- **Derive a coherent frame, then consolidate** it into a versioned `.md` with a revision-history table. Each handed-back file gets a new version number and a row documenting what changed and why.
- **Correct openly when rigor demands.** Precedents already in the record: screw angle 137.5° → **45.8°**; fractal dimension 2.807 → **2.0**; the chirality-vs-line-tension isotropy mechanism (Block III v0.1 → v0.2); and the graviton mass-term reasoning (Block IV v0.2 → v0.3, Fierz–Pauli "mass" corrected to a massless phonon / compatibility argument). Preserve superseded values in "History" notes — the audit trail is the point.
- Deliverables are **markdown**. Cross-reference scheme: **I-§**, **II-§**, **III-§**, **IV-§**, **V-§** point between blocks.
- One labeling convention applied consistently; the awkward non-matching cases are the diagnostic ones.

### 3.1 — Sandbox & parallel-track protocol (added v1.1)

Speculation that has **not** earned [OC]/[IR] does not go in the Blocks. It goes in the **sandbox** (`DCCREG_sandbox_v01.md`), a sealed [RH]-dominant space, so wild ideas can develop without contaminating the Block audit trail.

- **The one-way graduation valve.** Nothing crosses from the sandbox into a numbered Block until it independently earns [OC] or [IR]. A sandbox idea may *inspire* a Block computation; the Block records only what the computation establishes, never the speculation. **Blocks cite Blocks; the sandbox cites nothing load-bearing, and is never cited by a Block.**
- **Parallel-track use.** The sandbox is designed to be carried into a **separate conversation** run in parallel, so the main conversation keeps closing convergent forks without speculative drift. The parallel track edits **only** the sandbox; the main track owns the Blocks and the forks. The **graduation queue** (in the sandbox) is the sole channel between them, and it flows one way.
- **Guardrail.** A tangent is an asset only while the convergent work proceeds. If the sandbox grows faster than the main-track forks close, the tangent has become an escape hatch — that is the signal to stop branching and return to depth.
- Sandbox-internal references use **S-§**; the sandbox may read Block content via I-§…IV-§.

---

## 4. Document map

| File | Role | Cross-ref prefix |
|------|------|------------------|
| `DCCREG_fluid_substrate_foundations_v04.md` | **Block I** — substrate, two projections, SOSF scaffold, cascade, node law, field frame | I-§ |
| `DCCREG_MHD_emergence_v02.md` | **Block II** — B = coarse-grained vorticity, Maxwell, pair-plasma two-fluid, Coulomb-gauge electrodynamics | II-§ |
| `DCCREG_radiative_EM_emergent_LI_v02.md` | **Block III** — light as transverse vortex-lattice shear mode, emergent Lorentz invariance, isotropy computation | III-§ |
| `DCCREG_emergent_gravity_v08.md` | **Block IV** — gravity gate: analog metric; compatible/incompatible split (light = compatible, gravity+matter = incompatible defect sector); khronometric + Coulomb-gauge identification; α₁ = 0 forced; **defect gate closed on the Einstein side** (hexatic disclination kernel = Laplacian Green's fn), conditional on the hexatic identification | IV-§ |
| `DCCREG_emergent_matter_v05.md` | **Block V** — matter / fermion gate: screw-framing ⇒ ribbons; **spin-½** (belt trick / Finkelstein–Rubinstein); **automatic spin-statistics**; **spin = self-helicity, statistics = mutual helicity**; chirality ⇒ **Weyl**. Defect spectrum = the Block IV gravity coefficient | V-§ |
| `DCCREG_labeling_convention_v4.md` | 7-sphere-cell labeling + simulator spec; gyrator derived from chirality (§9G). Secondary for the next frontier | (standalone) |
| `DCCREG_sandbox_v01.md` | **Sandbox (parallel track)** — sealed [RH]-dominant speculation; one-way graduation valve into Blocks | S-§ (never cited by a Block) |

---

## 5. The spine of results (compressed; tiers in the docs)

- **Substrate (I):** ideal incompressible Euler [locked]. ω is the master field; **u = Biot–Savart(ω)** (vector projection), **p = Coulomb(ρ_eff)** (scalar projection); ρ_eff ∝ ½|ω|² − |S|². Chirality is primordial. Scaffold = **SOSF** with a **45.8°** golden screw about [1,1,1]. Matrix dimension **D = 2.0**; cascade: u const, Γ halves, ω doubles per level; spectrum **k⁻²** (Burgers/shock-like). **Node law:** Γ_c = Γ_n (spine), Γ_o = ½Γ_n (lateral); **dual counter-rotation is forced.** Field frame: pressure = smooth Coulomb landscape; helicity = standing checkerboard on **2-D cancellation sheets**.
- **MHD (II):** **B = (2m/q)⟨ω⟩.** Maxwell falls out — **∇·B = 0 structural**, induction = vorticity transport, ideal Ohm from losslessness, J = ∇×ω, vortex cores = charges. **Pair-plasma** two-fluid (Hall vanishes): bulk Alfvén + chiral counter-gyration at **ω_c = 2⟨ω⟩**; L/R polarisation asymmetry ∝ **net magnetic helicity**. Emergent theory = **incompressible MHD**. Unified electrodynamics = **Coulomb gauge**. **No light at c** (deferred to III).
- **Light (III):** **light = transverse shear mode of the chiral vortex lattice**, c = √(C₆₆/ρ). Sound (longitudinal, infinite) and light (transverse, finite) are orthogonal polarisations. Modified dispersion ω² = c²k²[1 − α(kℓ_P)²]: **emergent Lorentz invariance, IR-exact, Planck-suppressed UV violation.** Isotropy **computed**: central Biot–Savart → A = 2/3; achiral line tension restores **A = 1 at β = α**, natural — **near-isotropic light, no fine-tuning.** Chirality's role is **optical activity**, not isotropy.
- **Gravity (IV, v0.6):** strained lattice → **kinematic analog metric** [OC]; **Newtonian/Poisson limit** generic to 3-D elasticity [OC]. Key structural result: **light = the compatible (defect-free) strain sector; gravity + matter = the incompatible (defect) sector** of one lattice (Kröner: incompatibility = linearized Einstein tensor) — the gravity and fermion gates are **one sector**. Gravity is **Coulomb-gauge** (instantaneous strong longitudinal Newtonian potential + weak finite-c transverse graviton), mirroring II; its **weakness = the unscreened residual** of the quasi-neutral-screened Coulomb sector. Emergent class = **khronometric gravity** (infinite sound speed ⇒ khronon foliation); **c_GW = c_γ passes GW170817 structurally**; **α₁ = 0 forced** (c₁₃=0 graviton-=-light, c₁₄=0 instantaneous-khronon), robust against unknown couplings; α₂ parked at the instantaneous-limit singularity. **Defect gate CLOSED on the Einstein side by computation:** the SOSF is **hexatic** (fixed orientation + fluid position), so the disclination/curvature interaction = the **Laplacian Green's function** = the $1/k^2$ Newtonian/Einstein form (direct test ∫∇²(ln r/2π)=1.000) — conditional on the [IR] hexatic identification; residual is the *coefficient* (Frank constant K_A, 3D). The vacuum is a **medium** with a bounded screening length; GR = the α→0 + featureless-medium limit. **Qualitatively Einstein-form; now numeric (run002): $K_A\approx0.316\rho\Gamma^2$, $G_{\rm eff}\approx3.16/\rho\Gamma^2$, $\ln r$ form confirmed on the lattice, quasi-2D validated in 3D, Debye $\xi\propto n_d^{-1/2}$. α₂ + γ residual.**
- **Matter (V, v0.1):** matter = the **incompatible (defect) sector** (IV). The chiral screw **frames** vortex loops into ribbons; framed loops carry **spin-½** (belt trick / Finkelstein–Rubinstein, $\pi_1(SO(3))=\mathbb{Z}_2$); the **spin-statistics connection is automatic** (exchange $\cong$ $2\pi$ rotation). **spin = self-helicity, statistics = mutual helicity** (Moffatt/Călugăreanu) — Block I's conserved pseudoscalar **is** the spin-statistics charge. Substrate chirality ⇒ native **Weyl** fermions (the two sublattices = the two handednesses). The **defect spectrum = the Block IV gravity coefficient $K_A$** — one computation for both gates. **Ground state computed (run002):** spin-½, charge 120° ($C_3\parallel[1,1,1]$, fixed categorically — 90° excluded), definite handedness, closure $L=8$. **Excited spectrum (run003):** the ground state is an isolated **non-degenerate singlet** — **no doublet** (screw chirality forbids it), **no generation multiplet** (boson-interleaved winding ladder $L\approx8n$). **Dirac pairing (run004):** the missing partner is **inter-sublattice** — the two opposite-handed $L=8$ ribbons bind into a **massive Dirac** pair (mass = inter-sublattice coupling, §7a), **affirming** the fixed-chirality axiom; magnitude $\propto J$ open. **Fenced [RH]:** these as actual SM particles, electroweak isospin, generations — not claimed.

---

## 6. Current frontier

**Gravity gate — defect/curvature dynamics CLOSED qualitatively (Block IV v0.6).** The kinematic metric, Newtonian limit, compatible/incompatible merger, khronometric + Coulomb-gauge identification, α₁ = 0, and the **Einstein-vs-softer power-law (closed at 1/k², the Laplacian/Newtonian-Einstein form)** are established at their stated tiers, the last conditional on the [IR] hexatic identification. The gate is **qualitatively closed on the Einstein side**; what remains is *quantitative*: the disclination coefficient K_A and the 3D coefficient (= the fermion-gate disclination spectrum), α₂ at the instantaneous-khronon limit, the energy→softening sign, PPN γ, and dynamic-vs-static shear for light. *Authoritative list in IV-§10.*

**Fermion gate — OPENED (Block V v0.1).** Matter = the incompatible (defect) sector (IV-§5.2/§7). Block V establishes, at the level of spin and statistics: screw-framing ⇒ ribbons; **spin-½** (belt trick / Finkelstein–Rubinstein); **automatic spin-statistics**; **spin = self-helicity, statistics = mutual helicity** (so Block I helicity is the spin-statistics charge); chirality ⇒ **Weyl**. This is necessary, not sufficient, for "these are nature's fermions" — mass, charge, gauge, generations, and the soliton-quantisation measure are unestablished ([RH], fenced in V-§8). *Concrete next derivation (V-§9/§10):* the **stable-defect spectrum of the hexatic SOSF** — which is simultaneously the Block IV gravity coefficient $K_A$ and the Block V matter content. One quasi-2D simulator computation closes both.

**Update (run002, ladder 5/5):** the defect spectrum's *ground state* is computed — $K_A\approx0.316\rho\Gamma^2$/$G_{\rm eff}$ (IV v0.8) and a spin-½, charge-120°, handed ground-state loop ($L=8$) (V v0.3). Remaining: the **excited/multiplet spectrum** above the ground state, α₂, energy→softening sign, γ, soliton quantisation, and the [RH] SM-particle map. Recommendation (updated, post-run004): the matter gate's structure is now well-characterised — spin-½ 120° ground state (run002), isolated singlet / no generations (run003), and a **Dirac mass from inter-sublattice coupling** with the chirality axiom affirmed (run004). The clearest open quantitative target is **absolute energies/masses in physical units**: couple the run004 Dirac mass ($\propto J$) and the V-§6b spectrum to run002's $K_A$ machinery, fixing $J$ and $K_A$ in physical units. Then the carried analytic forks: **α₂** (IV, instantaneous-khronon limit), the **energy→softening sign** (IV, decides whether gravity attracts), and PPN **γ** (IV). **The next simulator target is staged: `sim/RUN005_physical_scales_brief.md`** — reduce all results to the minimal free-input set and compute the input-independent dimensionless ratios (esp. the $G_{\rm eff}$–$m_D$ cross-gate relation); pre-committed branches B-PINNED / B-REDUCED / B-IRREDUCIBLE.

---

## 7. Residual open forks (carried from the blocks)

- **I:** rigorous well-posedness/blow-up proof; helicity flux law; sublattice arrangement (bipartite vs mixed); global-imbalance magnitude.
- **II:** the 2m/q dictionary constant; ideal-MHD-all-the-way (no reconnection without a loss term); quantitative two-fluid dispersion coefficients; dynamo growth rate; MHD-scale spectrum.
- **III:** exact β/α (i.e. ln(d/a)) and the residual-anisotropy bound as a Lorentz-violation prediction; c-pinning to substrate constants; optical-activity magnitude; the preferred frame (CMB?).
- **IV:** defect-interaction power-law (1/k² vs 1/k⁴) — THE gate; α₂ at the instantaneous limit; khronon strong-coupling/mode health; energy→softening sign; PPN γ; cosmological G vs G_N; boundary-condition/screening-length section.
- **V:** the stable-defect spectrum (= IV's $K_A$); soliton quantisation (classical defects → quantum fermions); mass mechanism [RH]; spin content; charge/gauge/generations [RH→sandbox].
- **Labeling v4:** four-sphere junctions Θ⁴ remain provisional geometry.
- **Sandbox:** [RH]-only; see the sandbox's own graduation queue. Nothing here is a Block fork until promoted.

Each block's own "Open forks" section is authoritative.

---

## 8. Resuming

Read this README + Blocks I–V (+ the sandbox for context if working the parallel track). 

- **Main track:** the gravity-gate qualitative verdict is closed (IV v0.6); the live computation is the **stable-defect spectrum of the hexatic SOSF** (V-§9 = IV-§10.1) — it fixes the gravity coefficient $K_A$ *and* the matter content in one quasi-2D simulator pass. Consolidate each coherent frame into a new Block version with a revision-history row; keep the OC/IR/RH tags honest; correct openly if rigor demands.
- **Parallel track:** work the **sandbox** only, per §3.1. Append to its seed branches; route earned [OC]/[IR] items to the graduation queue with a destination Block. Promotion is executed in the main track.

*Programme status: exploratory, internally consistent, falsifiable at the frontier. Substrate → EM → MHD → light established (at their stated tiers); gravity computes to the Einstein/Newtonian $1/k^2$ form (Block IV v0.6, conditional on the hexatic identification); matter/fermion gate opened (Block V v0.1, spin-½ + automatic spin-statistics + Weyl, conditional/fenced). Both gates share one residual computation: the SOSF defect spectrum. The sandbox holds the speculative reach, sealed behind the one-way graduation valve.*
