# DCCREG Block II — MHD Emergence

**Version:** 0.2 (MHD Emergence block)

**Scope of this document:** the coarse-graining of the sub-Planck fluid substrate (Block I) into magnetohydrodynamics at observable scales. It establishes the substrate→MHD dictionary, the emergence of the Maxwell–MHD equation set, the wave-speed reconciliation, the equal-mass (pair-plasma) two-fluid treatment, the chirality→magnetic-helicity correspondence, and the unified Coulomb-gauge electrodynamics (coupling the scalar/electric and vector/magnetic projections). It stops at the boundary of radiative electromagnetism: because the electric sector is instantaneous, there is no light at $c$, and recovering true radiative EM is deferred to Block III.

**Companion document:** *DCCREG Fluid Substrate — Foundations & First Dynamics* (Block I, v0.4), which this builds directly upon. Section references prefixed **I-§** point to that document; unprefixed **§** references are internal to this one.

---

## Revision history

| Version | Date | Author | Summary of changes |
|:--|:--|:--|:--|
| 0.1 | 2026-05-29 | DCCREG Modeling Programme | Initial release — MHD Emergence block (Sections 0–6 and Appendix). Establishes the master identification $\mathbf{B} = (2m/q)\langle\boldsymbol{\omega}\rangle$; the emergence of the Maxwell–MHD set (structural $\nabla\cdot\mathbf{B}=0$, induction = vorticity transport, ideal Ohm from losslessness, current as curl of vorticity, vortex cores as charges); the dual-sublattice origin of the multi-fluid "mixture"; the wave-speed reconciliation (infinite sound speed = incompressible fast mode, finite Alfvén = Kelvin waves on vortex lines → emergent theory is specifically *incompressible* MHD); and the chirality→magnetic-helicity correspondence with dynamo amplification. Stops before quantitative multi-fluid coupling and dynamo growth rate. |
| 0.2 | 2026-05-29 | DCCREG Modeling Programme | **Equal-mass two-fluid treatment + unified electrodynamics (major).** (1) **Pair-plasma treatment** (new §5): the two species are equal mass, opposite Larmor coupling (handedness), same-sign electrostatic charge ($\rho_{\text{eff}}\propto\lvert\omega\rvert^2$) — i.e. a *pair plasma*. The Hall effect therefore vanishes (no whistler/ion-cyclotron splitting; an earlier ion–electron sketch is superseded). Bulk = undispersed Alfvén; the antisymmetric mode is the two chiralities **counter-gyrating at $\omega_c = 2\langle\omega\rangle$** (infinite sound speed enforces instantaneous quasi-neutrality); L/R degeneracy is broken only by the handedness imbalance, so the polarization asymmetry is **proportional to the net magnetic helicity** — a direct readout of the conserved chirality. (2) **Unified electrodynamics** (new §7): coupling the two projections yields **Coulomb-gauge electrodynamics** — $\mathbf{A}=$ Biot–Savart of $\boldsymbol\omega$ (transverse, $\nabla\cdot\mathbf{A}=0$ automatic from solenoidal $\boldsymbol\omega$); scalar potential $\varphi = p$ (instantaneous Coulomb, $\nabla^2\varphi=-\rho_{\text{eff}}$ = Gauss); $\mathbf{E}=-\nabla\varphi-\partial_t\mathbf{A}$ with Faraday $\nabla\times\mathbf{E}=-\partial_t\mathbf{B}$ automatic; electrostatic dynamics is **instantaneous Coulomb** (the capacitor-discharge phenomenology, formalized). Consequence: theory is Galilean / Coulomb-gauge, **no radiative EM (no light at $c$)** — carried to Block III. Renumbered: old §5→§6, §6→§8; new §5, §7 inserted. Updated §1/§3 cross-refs, open forks, Appendix. |

---

## Epistemic tagging legend

Every substantive claim carries one of three tags (consistent with Block I):

- **[OC] Operational Core** — standard, derivable physics or mathematics; true independent of the framework.
- **[IR] Interpretive Reading** — a modeling identification made *within* the framework; internally consistent, chosen rather than forced.
- **[RH] Resonance / Heuristic** — analogical or cosmological reading; suggestive, not load-bearing.

---

## 0. Inheritance from Block I

The substrate established in Block I and used here without re-derivation:

1. Ideal incompressible Euler, lossless, infinite sound speed (I-§0, I-§1).
2. $\boldsymbol{\omega}$ is the master field; velocity $\mathbf{u}$ (vector / Biot–Savart projection) and pressure $p$ (scalar / Coulomb projection) follow instantaneously (I-§7).
3. The exact equivalence of vorticity transport and ideal-MHD induction:
   $$\frac{D\boldsymbol{\omega}}{Dt} = (\boldsymbol{\omega}\cdot\nabla)\mathbf{u} \quad\Longleftrightarrow\quad \frac{D\mathbf{B}}{Dt} = (\mathbf{B}\cdot\nabla)\mathbf{u}.$$
   Vortex lines frozen-in (Kelvin) ↔ flux lines frozen-in (Alfvén) (I-§1, I-§10).
4. Mechanism B (Larmor): in a rotating frame, Coriolis ↔ magnetic Lorentz with $q\mathbf{B} \leftrightarrow 2m\boldsymbol{\Omega}$; centrifugal ↔ electrostatic (I-§2).
5. Effective charge density $\rho_{\text{eff}} = \rho(\tfrac12\lvert\boldsymbol{\omega}\rvert^2 - \lvert S\rvert^2) = 2\rho Q$; vortex cores are the charges (I-§2, I-§7).
6. Dual counter-rotating sublattices of opposite handedness (necessity derived in I-§13); conserved helicity, global handedness on the axial channel, local checkerboard on 2-D sheets (I-§12, I-§14).

---

## 1. The master identification (the dictionary)

Two Block-I results combine into a single bridge. The induction equivalence (item 3) fixes the *dynamics*; the Larmor relation (item 4) fixes the *dimensional conversion*. Together:

$$\boxed{\;\mathbf{B} = \frac{2m}{q}\,\langle\boldsymbol{\omega}\rangle\;}$$

where $\langle\cdot\rangle$ denotes coarse-graining over a scale $L \gg \ell_P$, and $m/q$ is the mass-to-charge ratio of the substrate constituent. **The coarse-grained vorticity is the magnetic field.** Everything in §2 is a consequence of this one identification. **[OC for the induction equivalence and the Larmor conversion; IR for adopting this as the definition of the emergent $\mathbf{B}$]**

The conversion constant $2m/q$ is the single free dimensional input the dictionary requires (see §8, flag 1).

---

## 2. The Maxwell–MHD set emerges

- **No magnetic monopoles — structurally.** $\mathbf{B} \propto \langle\nabla\times\mathbf{u}\rangle$ is a curl, and $\nabla\cdot(\nabla\times\mathbf{u}) \equiv 0$. So $\nabla\cdot\mathbf{B}=0$ is not a dynamical constraint to be enforced but an algebraic identity. The substrate cannot produce a monopole. **[OC]**
- **Faraday / induction.** $\partial_t\mathbf{B} = \nabla\times(\mathbf{u}\times\mathbf{B})$ is the coarse-grained vorticity transport equation, already identical (item 3). **[OC]**
- **Ideal Ohm's law.** Losslessness = zero resistivity = infinite conductivity, i.e. $\mathbf{E} = -\mathbf{u}\times\mathbf{B}$. "Lossless" *is* "perfect conductor." **[OC]**
- **Ampère / current.** $\mathbf{J} = \nabla\times\mathbf{B}/\mu_0 \propto \nabla\times\boldsymbol{\omega}$ — the macroscopic current is the curl of the vorticity (the second curl of $\mathbf{u}$). **[OC]**
- **Gauss / charge.** $\rho_{\text{charge}} = \rho_{\text{eff}}$ (item 5): the vortex cores are the charge concentrations; the electrostatic pressure landscape (I-§14) is the electric sector. **[OC for the identification]**

The substrate, coarse-grained, *satisfies Maxwell's equations* — with the no-monopole law a free consequence of $\mathbf{B}$ being a curl, and ideal Ohm a free consequence of losslessness.

---

## 3. The "mixture" — multi-fluid origin

The dual counter-rotating sublattices (item 6) coarse-grain into **two interpenetrating conducting fluids of opposite handedness** — a two-component (multi-fluid) MHD. The "magnetohydrodynamic mixture" of the original specification is the dual structure viewed at large scale: two species, opposite chirality, sharing one frozen-in field. **[IR]**

(Quantitative inter-species coupling is derived in §5.)

---

## 4. Wave-speed reconciliation — the infinite-sound-speed tension resolved

**The apparent problem.** The substrate has infinite sound speed (incompressible, instantaneous pressure; I-§0), yet MHD carries finite wave speeds.

**The resolution — incompressible MHD has both.** The fast magnetosonic speed is $\sqrt{c_s^2 + v_A^2}$, which $\to\infty$ as $c_s\to\infty$: in the incompressible limit the fast mode *decouples to infinite speed and becomes the incompressibility constraint itself*. The **Alfvén mode remains finite**,

$$v_A = \frac{B}{\sqrt{\mu_0\rho}},$$

because it is transverse — it rides the *tension* of the field lines. In the substrate those field lines are vortex lines, so the emergent Alfvén waves are precisely **Kelvin waves on the vortex filaments** (transverse waves on tension-bearing lines — the same object).

**Consequence.** The emergent theory is not generic MHD but specifically **incompressible MHD**: an instantaneous (infinite-speed) pressure/fast channel plus finite transverse Alfvén/Kelvin waves whose speed is set by the coarse-grained $\langle\boldsymbol{\omega}\rangle$ and $\rho$. The infinite sound speed is therefore not a defect to reconcile but the correct signature of the incompressible limit. **[OC — standard incompressible-MHD mode structure]**

---

## 5. The equal-mass (pair-plasma) two-fluid treatment

The two species share one $\mathbf{B}$ and couple to it by handedness. Opposite handedness flips the Larmor coupling ($q\mathbf{B}=2m\boldsymbol\Omega$ with $\boldsymbol\Omega\to-\boldsymbol\Omega$), so the two have **opposite magnetic-coupling charge**, but **equal mass** (same constituent) and **equal-sign electrostatic charge** ($\rho_{\text{eff}}\propto\lvert\boldsymbol\omega\rvert^2$ is mirror-blind). Equal mass + opposite magnetic coupling $=$ a **pair plasma** (not an ion–electron plasma).

**Hall effect vanishes.** The Hall term's coefficient scales with the species mass *asymmetry*, which is exactly zero here. Hence there is **no** generic dispersive splitting of the Alfvén wave into a $k^2$ whistler branch and a saturating ion-cyclotron branch — that ion–electron form does not apply. **[OC]**

**Symmetric (bulk) mode — undispersed Alfvén.** $\mathbf{U}=(\mathbf{u}_++\mathbf{u}_-)/2$ obeys single-fluid incompressible MHD: the transverse Alfvén wave at $v_A$ (Kelvin waves on the vortex lines; §4), with no Hall dispersion. **[OC]**

**Antisymmetric (chiral) mode — the signature.** $\mathbf{w}=\mathbf{u}_+-\mathbf{u}_-$ is the two chiralities moving oppositely. The infinite sound speed enforces **instantaneous quasi-neutrality** (any charge separation is screened with zero delay — the electric analog of incompressibility), freezing out charge separation; the residual relative dynamics is pure magnetic gyration. The two opposite-handed populations therefore **counter-gyrate at the cyclotron frequency**

$$\omega_c = \frac{qB}{m} = 2\langle\omega\rangle$$

(equivalently the Larmor frequency $\omega_L = \omega_c/2 = \langle\omega\rangle$ equals the coarse-grained vorticity — Mechanism B at macro scale). This chiral counter-gyration carries the helicity dynamics. The result survives the equal-mass correction untouched, since $\omega_c$ has no mass-asymmetry in it. **[OC given the dictionary]**

**Polarization asymmetry $=$ a readout of the chirality.** A *balanced* pair plasma has the L and R polarizations exactly degenerate (pair-plasma symmetry; no Faraday rotation). The degeneracy is broken only by the **imbalance** between the two sublattices — which is precisely the conserved global handedness $=$ magnetic helicity (§6). So the R/L wave-speed asymmetry is **proportional to the net magnetic helicity**: the polarization splitting *is* a direct, in-principle-measurable readout of the substrate's conserved chirality, not a generic Hall effect. **[OC for pair-plasma symmetry; IR for tying the splitting to the helicity imbalance]**

---

## 6. Chirality becomes magnetic helicity

With $\mathbf{B} = (2m/q)\langle\boldsymbol{\omega}\rangle$, the substrate's conserved **global handedness** (the axial-channel imbalance between the two sublattices; I-§12, I-§14) coarse-grains into the **magnetic helicity**

$$H_M = \int \mathbf{A}\cdot\mathbf{B}\,dV,$$

a conserved, *measurable* quantity central to solar physics, dynamos, and fusion confinement. The framework's chirality core thus lands on a real observable rather than remaining abstract. In ideal MHD $H_M$, cross-helicity $\int\mathbf{u}\cdot\mathbf{B}$, and kinetic helicity $\int\mathbf{u}\cdot\boldsymbol{\omega}$ are all conserved (I-§1). **[OC for the helicity correspondence; IR for equating the substrate global handedness with $H_M$]**

**Dynamo.** The substrate vortex-stretching cascade ($\omega$ doubles per level; I-§10) is, at macro scale, **dynamo action** — amplification of $\mathbf{B} = (2m/q)\langle\boldsymbol{\omega}\rangle$. The framework predicts dynamo behaviour as the large-scale face of its substrate cascade. **[OC for stretching↔dynamo; RH for "this is the origin of astrophysical magnetism"]**

---

## 7. The unified electrodynamics — Coulomb-gauge coupling of the two projections

The scalar (pressure/electric) and vector (vorticity/magnetic) projections, separate since I-§7, couple into a single electrodynamics — and the result is exactly **electrodynamics in the Coulomb gauge**.

**The vector potential is automatically transverse.** $\mathbf{A} = \frac{1}{4\pi}\int \boldsymbol\omega/\lvert\mathbf{x}-\mathbf{x}'\rvert\,d^3x'$ (the Biot–Savart potential, I-§7). Because $\nabla\cdot\boldsymbol\omega = 0$, integration by parts gives $\nabla\cdot\mathbf{A}=0$ — the **Coulomb-gauge condition for free** — and $\mathbf{B}=\nabla\times\mathbf{A}=(2m/q)\langle\boldsymbol\omega\rangle$. **[OC]**

**The scalar potential is the pressure, and it is instantaneous.** Identify $\varphi = p$ (up to a constant). It obeys $\nabla^2\varphi = -\rho_{\text{eff}}$ — the pressure–Poisson equation *is* Gauss's law — and, the sound speed being infinite, $\varphi$ is solved instantaneously at every instant: longitudinal, curl-free, instantaneous Coulomb. **[OC/IR]**

**Faraday's law falls out.** With $\mathbf{E} = -\nabla\varphi - \partial_t\mathbf{A}$:

$$\nabla\times\mathbf{E} = \nabla\times(-\nabla\varphi) - \partial_t(\nabla\times\mathbf{A}) = -\partial_t\mathbf{B}.$$

Faraday holds with the **full** $\mathbf{E}$; the electrostatic part $-\nabla\varphi$ is curl-free and drops out automatically (as it must), and the $-\partial_t\mathbf{A}$ part reduces in the ideal limit to the motional $-\mathbf{u}\times\mathbf{B}$ of §2. The magnetic Faraday of §2 is thus the transverse piece of a complete $\mathbf{E}$. **[OC]**

**Electrostatic dynamics — instantaneous Coulomb (the capacitor-discharge sector).** The longitudinal field $\mathbf{E}_\parallel = -\nabla\varphi = -\nabla p$ is sourced by the vortex-core charges $\rho_{\text{eff}}$ and re-equilibrates *instantaneously* whenever charges redistribute (the cascade / node dynamics, I-§12). This is genuine, energy-carrying electric dynamics, but **instantaneous Coulomb**, not retarded: the displacement current $\partial_t\mathbf{E}_\parallel$ is the instantaneous term enforcing charge conservation as a *constraint*, not a wave source. This is the capacitor-discharge picture (finite energy through the $1/r$ kernel with zero delay; the apparent-power spike), now a derived sector. **[OC for instantaneity; IR for the capacitor reading]**

**What the coupled theory is — and isn't.** The complete electrodynamics is **Coulomb-gauge / Galilean**: an instantaneous longitudinal electrostatic sector ($\varphi=p$, infinite speed) plus a transverse magnetic sector propagating at the finite Alfvén speed. Gauss, Faraday, and ideal Ohm all hold. But because the longitudinal sector is instantaneous, there is **no displacement-current-driven radiation — no light at $c$**, and the theory is not Lorentz-invariant Maxwell. Recovering true radiative EM is a separate, deeper question (Block III; §8 flag). **[OC for the consequence]**

---

## 8. Open forks / to-derive next

1. **The conversion constant $2m/q$.** Assigns a mass-to-charge to the substrate constituent — a free dimensional input; its value (and whether it is fixed by the Planck-scale constituent) is undetermined.
2. **Ideal-MHD-all-the-way.** No resistivity (lossless) ⇒ no reconnection ⇒ frozen field topology and exactly-conserved $H_M$. Internally consistent, but precludes macro reconnection unless a localized loss term is introduced (the tension flagged in Block I). Decide whether macro reconnection is wanted.
3. **Multi-fluid coupling — RESOLVED for equal mass (v0.2, §5).** Pair-plasma treatment: Hall vanishes, undispersed bulk Alfvén, chiral counter-gyration at $\omega_c=2\langle\omega\rangle$, L/R splitting $\propto$ net helicity. Remaining: a fully quantitative equal-mass two-fluid dispersion relation including the antisymmetric-mode coupling coefficients.
4. **Dynamo growth rate.** Stretching↔dynamo is identified (§6) qualitatively; a quantitative growth rate from the cascade ratios (I-§10) is not yet derived.
5. **Spectrum at MHD scale.** The substrate $k^{-2}$ spectrum (I-§10) coarse-grained — how the emergent MHD turbulence spectrum relates to the substrate one — is not addressed here.
6. **Radiative electromagnetism / light (→ Block III).** The unified electrodynamics (§7) is Coulomb-gauge / Galilean with an instantaneous electric sector, hence **no light at $c$**. Whether (and how) true radiative EM emerges — by reinstating a displacement-current analog or as an emergent transverse mode — is the central open question of the next block.
7. **Observable predictions.** Concrete, in-principle-testable signatures: chiefly the **L/R polarization asymmetry $\propto$ net magnetic helicity** (§5), the chiral-gyration frequency $\omega_c=2\langle\omega\rangle$, and the dynamo signature.

---

## Appendix — symbols & core relations

### Symbols

| Symbol | Meaning |
|:--|:--|
| $\langle\cdot\rangle$ | coarse-graining over scale $L \gg \ell_P$ |
| $\mathbf{B} = (2m/q)\langle\boldsymbol{\omega}\rangle$ | emergent magnetic field = coarse-grained vorticity |
| $m/q$ | mass-to-charge ratio of the substrate constituent (dictionary constant) |
| $\mathbf{E} = -\mathbf{u}\times\mathbf{B}$ | electric field (ideal Ohm, from losslessness) |
| $\mathbf{J} = \nabla\times\mathbf{B}/\mu_0 \propto \nabla\times\boldsymbol{\omega}$ | current density (curl of vorticity) |
| $\rho_{\text{charge}} = \rho_{\text{eff}} = 2\rho Q$ | charge density = vortex-core source |
| $v_A = B/\sqrt{\mu_0\rho}$ | Alfvén speed (finite; = Kelvin-wave speed on vortex lines) |
| $\omega_c = qB/m = 2\langle\omega\rangle$ | cyclotron frequency = twice coarse-grained vorticity; chiral counter-gyration rate (§5) |
| $\mathbf{w}=\mathbf{u}_+-\mathbf{u}_-$ | chiral (antisymmetric) mode — the two handednesses counter-gyrating |
| $\varphi = p$ | scalar potential = pressure (instantaneous Coulomb; $\nabla^2\varphi=-\rho_{\text{eff}}$) |
| $\mathbf{A} = \frac{1}{4\pi}\int\boldsymbol\omega/\lvert\mathbf{x}-\mathbf{x}'\rvert\,d^3x'$ | vector potential (transverse, $\nabla\cdot\mathbf{A}=0$ automatic) |
| $H_M = \int\mathbf{A}\cdot\mathbf{B}\,dV$ | magnetic helicity (= coarse-grained global handedness; conserved) |

### Core relations

$$\mathbf{B} = \frac{2m}{q}\langle\boldsymbol{\omega}\rangle \qquad\text{(master identification)}$$

$$\nabla\cdot\mathbf{B} = 0 \qquad\text{(structural — } \mathbf{B}\text{ is a curl; no monopoles)}$$

$$\partial_t\mathbf{B} = \nabla\times(\mathbf{u}\times\mathbf{B}) \qquad\text{(induction = vorticity transport)}$$

$$\mathbf{E} = -\mathbf{u}\times\mathbf{B}, \qquad \mathbf{J} = \frac{1}{\mu_0}\nabla\times\mathbf{B} \qquad\text{(ideal Ohm; Ampère)}$$

$$\text{fast mode} \to \infty \ (c_s\to\infty), \qquad v_A = \frac{B}{\sqrt{\mu_0\rho}} \ \text{finite} \qquad\text{(incompressible MHD)}$$

$$\omega_c = \frac{qB}{m} = 2\langle\omega\rangle \qquad\text{(chiral counter-gyration; pair-plasma, Hall-free)}$$

$$\varphi = p,\quad \nabla\cdot\mathbf{A}=0,\quad \mathbf{E} = -\nabla\varphi - \partial_t\mathbf{A},\quad \nabla\times\mathbf{E} = -\partial_t\mathbf{B} \qquad\text{(Coulomb-gauge electrodynamics)}$$

$$H_M = \int\mathbf{A}\cdot\mathbf{B}\,dV = \text{const} \qquad\text{(chirality} \to \text{magnetic helicity; L/R splitting} \propto H_M)$$
