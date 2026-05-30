# DCCREG Block III — Radiative EM & Emergent Lorentz Invariance

**Version:** 0.2 (Radiative-EM block)

**Scope of this document:** whether and how true radiative electromagnetism (light propagating at finite c) emerges from the substrate, given that Block II left the electric sector instantaneous. It establishes light as the transverse shear mode of the chiral vortex lattice, the resolution of the historical elastic-aether problem, the modified dispersion relation and emergent Lorentz invariance, and — now computed — the elastic-isotropy result: central Biot–Savart forces give an anisotropic A = 2/3, restored to isotropy by the (achiral) vortex line tension at the natural ratio β = α, with chirality supplying the separate optical-activity (L/R) effect. It opens the gravity and fermion gates without entering them.

**Companion documents:** Block I (*Foundations* v0.4) and Block II (*MHD Emergence* v0.2). References prefixed **I-§** and **II-§** point to those; unprefixed **§** is internal.

> **Status of this block.** The most speculative block of the programme. The mechanism (transverse shear waves of a vortex lattice) and the elastic computation are standard physics [OC]; the identification of that mode with light and the emergent-Lorentz-invariance reading are interpretive [IR]; the gravity and fermion gates are heuristic [RH]. As of v0.2 the elastic-isotropy make-or-break **passes in the favourable sense** (isotropy at the natural stiffness ratio β = α, no fine-tuning) — see §6.

---

## Revision history

| Version | Date | Author | Summary of changes |
|:--|:--|:--|:--|
| 0.2 | 2026-05-29 | DCCREG Modeling Programme | **Transverse shear-modulus computation + correction to the isotropy mechanism (major).** Computed the elastic tensor from the actual inter-vortex Biot–Savart interaction (the transverse stiffness that sets light), not the longitudinal pressure couplings used in v0.1. Results: (a) **central forces alone give A = 2/3** (equal circulation; ≤ that, down to ~0.06, as circulation concentrates on the spine) — Cauchy C₁₂ = C₄₄ holds, light anisotropic; the v0.1 longitudinal A = 0.80 was the wrong stiffness family. (b) **Isotropy (A = 1) is restored by the transverse bond-bending stiffness β — the vortex line tension — at β/α = 1**, which breaks Cauchy; and β ≈ α is *natural*, since both ∝ ρΓ² (β/α ~ ln(d/a)/4 ~ O(1)), so near-isotropic light needs no fine-tuning and exact isotropy is the mild condition ln(d/a) ≈ 4. (c) **Correction to v0.1:** the isotropy agent is the **achiral line tension**, not chirality; for a cubic lattice the chiral and achiral point groups share the same three bulk elastic constants, so chirality cannot move the bulk Zener ratio. Chirality's role is the separate k-linear **optical-activity / L/R splitting** (§4, II-§5), not isotropy. Rewrote §6, corrected §4 and §7 (chirality does helicity + gyrator + optical activity — three roles, not the four claimed in v0.1), updated open forks and Appendix. |

---

## Epistemic tagging legend

- **[OC] Operational Core** — standard, derivable physics/mathematics.
- **[IR] Interpretive Reading** — a modeling identification within the framework.
- **[RH] Resonance / Heuristic** — analogical / cosmological; suggestive, not load-bearing.

---

## 0. Inheritance

1. The substrate is ideal, incompressible, lossless, infinite sound speed (I-§0).
2. Coulomb-gauge electrodynamics (II-§7): scalar potential φ = p instantaneous; vector potential A = Biot–Savart(ω), ∇·A = 0; E = −∇φ − ∂_tA; B = (2m/q)⟨ω⟩. Faraday, Gauss, ideal Ohm hold. **No displacement-current radiation — no light at c.**
3. The chiral vortex skeleton: SOSF lattice, [1,1,1] screw, conserved helicity (I-§4, I-§12–14).
4. The two chiralities counter-gyrate at ω_c = 2⟨ω⟩; L/R polarisation asymmetry ∝ net magnetic helicity (II-§5).
5. The gyrator is hosted on the chiral [1,1,1] traversal (labeling convention v4 §9G).

---

## 1. The problem

Block II's electrodynamics is Galilean: an instantaneous longitudinal electric sector and a finite transverse magnetic (Alfvén) sector, with the displacement current absent. Light — a transverse wave at finite c sustained by a displacement current — is not present. The locked infinite sound speed appears to forbid radiation. **[OC]**

---

## 2. The dissolution — light and sound are orthogonal polarisations

Incompressibility constrains only the **longitudinal** (compressional) response, sending the longitudinal sound speed to infinity. It says nothing about **transverse** waves. A plain fluid has none, but a fluid threaded with a vortex lattice has shear rigidity and therefore carries transverse waves at finite speed.

- **Longitudinal** (compressional / pressure / electric): speed → ∞ — the instantaneous Coulomb sector.
- **Transverse** (vortex-shear / magnetic): finite speed — where radiation lives.

Infinite sound and finite light are different polarisations of one medium; incompressibility touches only the former. Block II's "no light" analysed the longitudinal and mean-field sectors, not the bare transverse sector. **[OC]**

---

## 3. Light = the transverse shear mode of the chiral vortex lattice

Two transverse modes are *not* light: the **inertial wave** of uniform rotation (ω = 2Ω₀cosθ, wavelength-independent) and the **Kelvin wave** of a single filament (ω ∝ k²). Neither is linear. Light requires the feature both lack — a **lattice** with **shear rigidity**, which carries a transverse shear sound with linear dispersion:

$$\text{light} = \text{transverse shear mode of the chiral vortex lattice}, \qquad c = \sqrt{C_{66}/\rho},$$

C₆₆ the transverse (shear) modulus of the vortex vacuum. The SOSF skeleton does double duty: chirality carrier *and* source of the vacuum's transverse stiffness. No lattice → no shear modulus → no light. **[OC for the mechanism; IR for the identification with light]**

**Characterisation:** the chiral vortex vacuum is a **solid for transverse perturbations** (finite shear rigidity → light at c) and an **incompressible fluid for longitudinal ones** (infinite bulk modulus → infinite sound). One medium, two faces.

**Cures the historical elastic aether.** The 19th-century elastic-solid aether failed because an elastic solid also carries *longitudinal* waves → predicted longitudinal light, never observed. Here incompressibility pushes the longitudinal speed to infinity, converting that mode into the instantaneous Coulomb constraint (II-§7) — so there is no longitudinal light, structurally rather than by fiat. The Block II instantaneous electric sector and the Block III transverse light are the two halves of the cure. **[IR/RH for the historical reading; OC for the mechanism]**

---

## 4. The transverse mode is gyroscopic — chirality enters as optical activity

A transversely displaced vortex feels a **Magnus force** f = ρΓ(ẑ × u̇): perpendicular to its velocity, ∝ circulation Γ, with **sign set by the handedness**. This is a *gyroscopic* (velocity-dependent) force, so it does not contribute to the static elastic constants; its effect is **k-linear** and acts on the propagating wave:

- The displacement separates into two **circular polarisations**; the Magnus term splits their speeds — the **optical activity** of a chiral medium, identical to the L/R circular birefringence ∝ net helicity of II-§5. The photon's two polarisations and their speed difference are the gyroscopic signature of the chiral vacuum.
- This is chirality's role in the radiative sector: **a polarisation effect (optical activity), not the source of isotropy.** Isotropy is a property of the static bulk elastic tensor and is fixed separately (§6).

**Stiffness-family note.** The labeling-convention couplings κ (κ_central = 3/16, κ_lateral = 1/8) are **longitudinal** (pressure/capacitive) stiffnesses. Light rides the **transverse** vortex elasticity (radial Biot–Savart interaction α + bond-bending line tension β), computed in §6. **[OC for the gyroscopic structure; IR for the optical-activity reading; ties to II-§5]**

---

## 5. Modified dispersion and emergent Lorentz invariance

The lattice shear mode is linear only at long wavelength; the discrete structure (scale a ~ ℓ_P) bends it:

$$\omega^2 = c^2 k^2\left[\,1 - \alpha\,(k\ell_P)^2 + \cdots\right].$$

- **Infrared** (kℓ_P → 0): ω = ck exact. Lorentz invariance is **emergent and exact** at low energy; the preferred frame (the lattice) is invisible. **[OC/IR]**
- **Ultraviolet** (kℓ_P ~ 1): Lorentz violation enters at order **(kℓ_P)²** — Planck-suppressed. The framework survives the experimental bounds precisely because the leading deviation is (E/E_Planck)², and it predicts a concrete quadratic high-energy dispersion correction. **[OC for the form; IR for ℓ_P]**

**Conceptual commitment.** A theory with two speeds (∞ sound, finite c) cannot be *fundamentally* Lorentz invariant — it has a preferred frame; the substrate is, technically, an aether. Lorentz invariance is therefore **emergent**: an approximate low-energy symmetry of the transverse sector, as relativistic excitations emerge in condensed-matter / analog-gravity systems over a preferred-frame lattice. The infinite sound speed and preferred frame are the trans-Planckian remnant. Whether the emergence is exact enough to meet the Lorentz-violation bounds is the central open question, shared with every emergent-spacetime programme. **[RH — most speculative claim of the programme]**

---

## 6. The make-or-break — elastic isotropy (computed)

Cubic/octahedral elasticity is generically **anisotropic**; unless the elastic tensor meets the isotropy condition, light's speed depends on direction → leading-order rotational Lorentz violation (tightly bounded, would falsify). The decisive quantity is the **transverse** vortex elasticity (the modulus light rides), computed here from the inter-vortex Biot–Savart interaction — not the longitudinal pressure couplings.

**Radial (central) part.** Two vortex lines at separation d interact via the 2-D-Coulomb (logarithmic) Biot–Savart potential φ(d) = −(ρΓ²/2π)ln d. The effective central bond stiffness is k_eff = φ″ − φ′/d = ρΓ²/(πd²), so **k_eff·d² is length-independent** — each bond contributes with weight ∝ Γ² only. Central forces satisfy the **Cauchy relation C₁₂ = C₄₄**, and over the ⟨100⟩ (CO) + ⟨110⟩ (OO) bond network this gives

$$\boxed{A_{\text{central}} = 2/3}\quad(\text{equal circulations}),$$

falling further (to ~0.06) as Block I's circulation allocation concentrates Γ on the spine. **Light from the central forces alone is anisotropic.** (The v0.1 figure A = 0.80 used the *longitudinal* pressure couplings — the wrong stiffness family — and is superseded.) **[OC]**

**Bond-bending (line tension) restores isotropy — at the natural value.** A vortex line resists bending; this gives each bond a **transverse stiffness β** (the line tension) in addition to the radial α. Non-central forces **break the Cauchy relation** (C₁₂ ≠ C₄₄) and shift the Zener ratio. Computed:

| β/α | C₁₂ vs C₄₄ | A |
|:--|:--|:--|
| 0 | equal (Cauchy) | 0.667 |
| 0.5 | split | 0.889 |
| **1.0** | split (C₁₂ → 0) | **1.000** |
| 2.0 | split | 1.111 |

**Isotropy is reached at β = α**, and **β ≈ α is natural**: the radial interaction stiffness and the line-tension bending stiffness are *both* ∝ ρΓ² (α ~ ρΓ²/πd², β ~ ρΓ²·ln(d/a)/4πd²), so β/α ~ ln(d/a)/4 — an O(1) number with no hierarchy. Exact isotropy is the mild condition **ln(d/a) ≈ 4** (a natural lattice-spacing-to-core ratio). So the framework produces **near-isotropic light generically, with no fine-tuning**, and any residual β/α ≠ 1 appears as a small, in-principle-measurable rotational anisotropy — a prediction, not an embarrassment. **[OC for the computation; IR for the naturalness reading]**

**Chirality is *not* the isotropy agent (correction to v0.1).** For a cubic lattice the chiral (O) and achiral (O_h) point groups have the **same three bulk elastic constants**, so chirality cannot move the bulk Zener ratio; the static Magnus force is gyroscopic and contributes no static modulus. The isotropy fix is the **achiral line tension**. Chirality's role is the separate k-linear **optical activity** (§4). The v0.1 claim that a chiral [1,1,1] term tunes isotropy conflated the achiral bond-bending stiffness with a chiral term and is withdrawn. **[OC]**

**Status.** The make-or-break **passes in the favourable sense**: achiral vortex elasticity gives isotropic light at the natural stiffness ratio β = α, no tuning; emergent isotropic Lorentz invariance is generic, with a small residual anisotropy (∝ |β/α − 1|) as a testable signature. **[OC/IR]**

---

## 7. The [1,1,1] convergence (corrected)

The body-diagonal screw axis carries three roles: (a) global helicity / chirality (I-§12–14); (b) the gyrator host (v4 §9G); (c) the optical activity of light (§4, II-§5 L/R splitting). One axis, three roles — all *chiral* effects.

**Not** elastic isotropy. The v0.1 draft listed isotropy as a fourth [1,1,1] role; the §6 computation corrects this — isotropy is set by the **achiral** vortex line tension (β ≈ α), independent of handedness. So the clean division is: **chirality governs the polarisation sector (helicity, gyrator, optical activity); achiral line tension governs the isotropy of the bulk.** The two are decoupled, which is the honest and the more robust picture. **[OC for the decoupling; IR for the reading]**

---

## 8. Gates opened (not entered)

- **Gravity.** C₆₆, hence c, varies where the lattice is strained → the light-cone tilts and curves → an effective curved metric for the emergent light. Gravity = the elasticity field of the vortex vacuum (analog-gravity mechanism). **[RH]**
- **Fermions / matter.** An elastic lattice has topological defects — disclinations, dislocations, linked/knotted vortices whose quantised helicity (linking number) is a natural spin-like pseudoscalar. Matter would be the defect sector of the same lattice whose phonon is light: Kelvin's vortex atom with chirality supplying spin. **[RH — deepest, most speculative gem]**

---

## 9. Open forks / to-derive next

1. **Isotropy computation — RESOLVED (v0.2, §6).** Central Biot–Savart gives A = 2/3; the vortex line tension (transverse stiffness β) restores A = 1 at β = α, a natural ratio (both ∝ ρΓ²). Residual: the precise β/α (i.e. ln(d/a)) from the SOSF core-to-spacing ratio, which fixes the magnitude of any leftover anisotropy.
2. **Dispersion regime / c-pinning.** Determine the Magnus-to-inertia ratio and the long-wavelength dispersion; tie c = √(C₆₆/ρ) to the substrate constants and the II 2m/q dictionary.
3. **Emergent-LI exactness.** Quantify α in the (kℓ_P)² correction and confront the Lorentz-violation bounds; quantify the optical-activity (L/R) magnitude vs the helicity; identify the preferred frame (CMB frame?).
4. **Residual anisotropy as a prediction.** Turn |β/α − 1| into a concrete bound/signature for rotational Lorentz violation.
5. **Gravity gate (§8).** Whether the strained-lattice effective metric has Einstein-like dynamics.
6. **Fermion gate (§8).** Whether linked/knotted vortex defects realise spin-½ matter.

---

## Appendix — symbols & core relations

### Symbols

| Symbol | Meaning |
|:--|:--|
| C₆₆ / c = √(C₆₆/ρ) | transverse shear modulus of the vortex vacuum / speed of light |
| C₁₁, C₁₂, C₄₄ | cubic elastic constants; A = 2C₄₄/(C₁₁−C₁₂), A = 1 ⟺ isotropy |
| α | radial (central) Biot–Savart bond stiffness, k_eff = ρΓ²/(πd²) |
| β | transverse (bond-bending) stiffness = vortex line tension; isotropy at β = α |
| f_M = ρΓ(ẑ × u̇) | Magnus force (gyroscopic, k-linear): optical activity / L/R splitting, **not** isotropy |
| ℓ_P | Planck-scale lattice cutoff |

### Core relations

$$\text{light} = \text{transverse mode of the chiral vortex lattice}, \qquad c = \sqrt{C_{66}/\rho}$$

$$\text{longitudinal} \to \infty \ (\text{incompressible}) \quad\text{vs}\quad \text{transverse} \to c \ \text{finite (vortex shear)}$$

$$\omega^2 = c^2 k^2\left[1 - \alpha(k\ell_P)^2 + \cdots\right] \qquad (\text{IR-exact, UV Planck-suppressed Lorentz violation})$$

$$\text{central forces (Cauchy } C_{12}=C_{44})\Rightarrow A = 2/3;\qquad \text{line tension } \beta \Rightarrow A=1 \text{ at } \beta=\alpha$$

$$\beta/\alpha \sim \ln(d/a)/4 \sim O(1) \ \Rightarrow\ \text{near-isotropic light without tuning;}\ \ \text{exact at } \ln(d/a)\approx 4$$
