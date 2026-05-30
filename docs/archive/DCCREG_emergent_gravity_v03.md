# DCCREG Block IV — Emergent Gravity from Vortex-Lattice Elasticity

**Version:** 0.3 (Gravity-gate block)

**Scope of this document:** what gravitational theory the strained chiral vortex lattice (Block III) produces, and where it can be falsified. It establishes the kinematic analog metric; the strain→metric dictionary and Newtonian limit; the **compatible/incompatible strain split** that unifies the gravity and fermion gates (light = compatible phonon sector; gravity+matter = incompatible defect sector); the **gradient-order make-or-break** that decides whether the dynamics is Einstein (Kleinert $1/k^2$) or a softer higher-derivative gravity ($1/k^4$); the identification of the emergent theory (conditional on that test) as **khronometric gravity**; and the first computed preferred-frame result — the substrate's two locked features (light-is-the-graviton, infinite sound speed) **force $\alpha_1=0$**, with $\alpha_2$ parked at an instantaneous-limit singularity. General Relativity is treated as one falsifiable hypothesis among several, recovered as the $\alpha_1,\alpha_2\to0$ infrared limit; it is not the success criterion.

**Companion documents:** Block I (*Foundations* v0.4), Block II (*MHD Emergence* v0.2), Block III (*Radiative EM & Emergent Lorentz Invariance* v0.2). References prefixed **I-§ / II-§ / III-§** point to those; unprefixed **§** is internal.

> **Status of this block.** The kinematic analog-gravity mechanism and the compatible/incompatible (defect-geometry) results are standard physics **[OC]**; the identification of the compatible sector with light and the incompatible sector with gravity+matter is **[IR]**; the khronometric identification is [OC classification + IR adoption]; the $\alpha_1=0$ result is **[OC given the §5.4 premise]**; the routes to genuine Einstein dynamics and the gravity-as-defect-sector dynamics are **[RH]** pending the §5.4 gradient-order computation. **This block does not claim to derive GR, and does not treat non-GR as failure.** It locates the construction precisely and names the computations ($1/k^2$ vs $1/k^4$; $\alpha_2$; the energy→softening sign) that confirm or kill it.

---

## Revision history

| Version | Date | Author | Summary of changes |
|:--|:--|:--|:--|
| 0.1 | 2026-05-29 | DCCREG Modeling Programme | Initial release. Kinematic analog metric from varying $C_{66}$; strain→metric dictionary and Newtonian/Poisson limit; light bending with PPN $\gamma$ as make-or-break; dynamics classified as Lorentz-violating aether/Hořava-type, GR as IR limit; Sakharov / Kleinert routes flagged [RH]; defect–elasticity stress-energy source; isotropy and GW-speed threads. |
| 0.2 | 2026-05-29 | DCCREG Modeling Programme | **Gravity class identified + verdict reframed.** Infinite sound speed ⇒ global foliation ⇒ khronon ⇒ **khronometric gravity** specifically; two projections = khronon (longitudinal) + graviton (transverse); $c_{\rm GW}=c_\gamma$ passes GW170817 structurally; preferred-frame PPN $\alpha_1,\alpha_2$ named as the empirical content, GR = $\alpha_1,\alpha_2\to0$; khronon-pathology-tamed conjecture [RH]; verdict reframed from "falls short of GR" to "predicts a specific falsifiable non-Einsteinian gravity." |
| 0.3 | 2026-05-29 | DCCREG Modeling Programme | **Correction + compatible/incompatible merger + first preferred-frame computation (major).** (1) **Correction to §5.1** (openly flagged): the v0.1/0.2 claim that elastic $C(\partial u)^2$ is a Fierz–Pauli *mass* term for the graviton was wrong — the transverse shear phonon is **gapless/massless** ($\omega=ck$); the strain is the *field strength* of the displacement, so $\varepsilon^2$ is a kinetic, not mass, term. The conclusion (elasticity ≠ Einstein dynamics) stands; the reason is corrected. (2) **Compatible/incompatible split** (rewritten §5.2): compatible strain ($\eta=0$, no defects) ⇒ flat geometry ⇒ **the phonon = light**; incompatible strain ($\eta\neq0$, defects) ⇒ curvature/torsion ⇒ **gravity+matter**. Kröner's theorem: incompatibility $=$ linearized Einstein tensor. **The gravity gate and the fermion gate are one sector**: light is compatible, gravity+matter is incompatible, of the same lattice. (3) **Gradient-order make-or-break** (new §5.4): Kleinert — first-gradient elasticity gives a $1/k^4$ defect interaction (**not** Einstein); second-gradient gives $1/k^2$ (**linearized Einstein**). The whole Einstein-aether/§6 analysis is **conditional** on the SOSF effective elasticity (or its fluctuation-induced form) being second-gradient. Sharp, simulator-addressable. (4) **$\alpha_1$ computed** (new §6.7): with $c_{13}=0$ (graviton=light) and $c_{14}=0$ (instantaneous khronon), $\alpha_1=-4c_{14}\to0$ — **forced, robust against the unknown $c_1,c_2$**; $\alpha_2$ is $0/0$ at $c_{14}=0$ and parked pending the instantaneous-limit PPN. (5) Verdict and open forks updated; the $1/k^2$-vs-$1/k^4$ test promoted to the #1 fork (it gates everything downstream). Section numbers preserved from v0.2; §5 rewritten, §6.7 added, §7/§9/§10/Appendix updated. |

---

## Epistemic tagging legend

- **[OC] Operational Core** — standard, derivable physics/mathematics.
- **[IR] Interpretive Reading** — a modeling identification within the framework.
- **[RH] Resonance / Heuristic** — analogical/cosmological; suggestive, not load-bearing.

Tier discipline runs both ways: don't let "analog gravity works" drift to "we derived GR," and don't let "this isn't GR" mean "this is wrong." Divergences from GR are empirical content — to be computed and tested (they are tightly bounded), not apologised for and not waved through. v0.3 also demonstrates the third rule: **correct openly when rigor demands** (the §5.1 fix).

---

## 0. Inheritance from Blocks I–III

1. Ideal, incompressible, lossless, infinite sound speed; a preferred frame exists — **the lattice is an aether; Lorentz invariance is emergent** (I-§0, III-§5). Load-bearing: it fixes the gravity class (§6).
2. **Light = transverse shear mode of the chiral vortex lattice**, $c=\sqrt{C_{66}/\rho}$ (III-§3). Solid for transverse perturbations (light at $c$), incompressible fluid for longitudinal (infinite sound).
3. Transverse elastic tensor computed (III-§6): central forces $A=2/3$; achiral line tension $\beta$ restores $A=1$ at $\beta=\alpha$ (both $\propto\rho\Gamma^2$).
4. Modified dispersion $\omega^2=c^2k^2[1-\alpha(k\ell_P)^2+\cdots]$ (III-§5).
5. Two projections (I-§7): scalar/pressure (longitudinal, instantaneous Coulomb; II-§7) and vector/vorticity (transverse, finite $c$).
6. Topological-defect potential — disclinations, dislocations, linked/knotted vortices (III-§8, the fermion gate). Now central (§5.2, §7).

---

## 1. The claim to be tested

> **Gravity-gate hypothesis (README §6A).** Where the lattice is strained, $C_{66}$ — hence $c$ — varies; the light-cone tilts and curves; the strain field is an effective curved metric. The questions: what *class* of gravitational theory is the back-reaction, and what is the stress-energy source.

Two halves, never conflated: **(K) kinematics** — do excitations move as in curved spacetime? (robust, §2–4); **(D) dynamics** — what law does the metric obey? (§5–6). The v0.3 spine: (D) is decided by one computable quantity (the gradient-order, §5.4); *if* it is Einstein-class, the substrate's mode speeds then force $\alpha_1=0$ (§6.7).

---

## 2. The kinematic metric — analog gravity (the robust half)

A linear wave with position-dependent speed $c(\mathbf{x})$ propagates by a curved-space d'Alembertian $\partial_\mu(\sqrt{-g}\,g^{\mu\nu}\partial_\nu\phi)=0$, defining an effective metric whose null cones are $c(\mathbf{x})\,dt=|d\mathbf{x}|$. Weak-field isotropic: $ds^2_{\text{eff}}=-c(\mathbf{x})^2dt^2+d\mathbf{x}^2$. Cones tilt toward soft ($C_{66}\downarrow$) regions; horizons where $c\to0$ relative to a flow. Kinematically complete; the *law* for $C_{66}(\mathbf{x})$ is (D). **[OC]**

---

## 3. Strain→metric dictionary and the Newtonian limit

With $C_{66}=C_{66}^0[1+s]$, $c\approx c_0(1+s/2)$, matching $-g_{00}=1+2\Phi/c_0^2$:
$$\boxed{\;\Phi=\tfrac12 c_0^2\,\frac{\delta C_{66}}{C_{66}^0}\;}\qquad\textbf{[OC matching; IR naming]}.$$
Attraction needs softening ($s<0$) where energy concentrates (anharmonic; sign uncomputed — §10.4). A 3-D centre of dilatation gives $u_i\propto\partial_i(-1/r)$, a harmonic $1/r$ potential obeying $\nabla^2\Phi=4\pi G_{\text{eff}}\rho_{\text{source}}$ — **the inverse-square law is the elastic Green's function**, with $G_{\text{eff}}$ set by the elastic constants and the energy→softening coupling. The static weak-field limit is firm. **[OC elasticity; IR identification]**

---

## 4. Light bending and PPN $\gamma$

$$\text{deflection}\propto\tfrac{1+\gamma}{2}:\quad \gamma=-1\ (\text{Nordström, no bending}),\ \ \gamma=1\ (\text{GR}),\ \ \text{Cassini: }\gamma-1=(2.1\pm2.3)\times10^{-5}.$$
DCCREG **bends light** ($c$ varies directly) — richer than Nordström. **[OC]** The coefficient $\gamma$ is an uncomputed elastic quantity; $\beta=\alpha$ (III-§6, $A=1$) is **necessary but not sufficient** for $\gamma=1$ ($A=1$ removes directional dependence of $c$; $\gamma$ concerns the $g_{00}$/$g_{ij}$ strain partition). In the Einstein-aether reading (§6) $\gamma=1$ is *attainable*, so this regime has room to pass. **[OC framework; result open]**

---

## 5. The dynamics — compatible vs incompatible strain (corrected)

### 5.1 Correction (openly flagged): the phonon is massless

v0.1/v0.2 claimed the elastic energy $C(\partial u)^2$ is a Fierz–Pauli **mass** term for the metric perturbation. **This was wrong.** The propagating degree of freedom is the displacement $u_i$, and the transverse shear phonon is **gapless** ($\omega=ck$, linear) — massless, not a massive graviton. The strain $\varepsilon_{ij}=\partial_{(i}u_{j)}$ is the *field strength* of $u$ (analogous to $\partial A$ in electromagnetism), so $\varepsilon^2$ is a **kinetic** term written in field-strength variables, not a mass term. The earlier *conclusion* — bare elasticity is not Einstein dynamics — stands; the stated *reason* is corrected here. The correct reason is §5.2. **[OC]**

### 5.2 Compatible strain = flat = light; incompatible strain = defects = curvature

Strain built from a single-valued displacement, $\varepsilon_{ij}=\partial_{(i}u_{j)}$, automatically satisfies the **Saint-Venant compatibility** condition: its incompatibility tensor
$$\eta_{ij}=\epsilon_{ikl}\,\epsilon_{jmn}\,\partial_k\partial_m\varepsilon_{ln}$$
vanishes. By **Kröner's theorem**, $\eta_{ij}$ *is* the linearized Einstein tensor of the geometry $g=\delta+2\varepsilon$. Hence two sectors of one lattice:

| Strain sector | Geometry | Physical content |
|:--|:--|:--|
| **Compatible** ($\eta=0$, defect-free) | **flat** | the propagating phonon $=$ **light** |
| **Incompatible** ($\eta\neq0$, defects) | **curved/torsioned** | **gravity + matter** |

Disclination density $\leftrightarrow$ curvature; dislocation density $\leftrightarrow$ torsion (standard defect geometry; Kröner, Kleinert, Katanaev–Volovich). A disclination produces a conical-deficit geometry — a genuine curvature concentration — and the compatible phonon's path bends around it: **that bending is the analog metric's gravitational lensing, now derived from the defect rather than posited.**

> **The gravity gate and the fermion gate are one sector.** Light is the *compatible* (defect-free) phonon; gravity-and-matter is the *incompatible* (defect) sector of the same lattice. The fermion gate does not merely *source* gravity (§7) — it *is* the curved sector. **[OC for the defect geometry; IR for the light/gravity identification]**

### 5.3 The preferred frame fixes the theory class

A diffeomorphism-invariant theory has no preferred frame; the substrate has one. So the emergent gravity carries the preferred frame dynamically — it lives in the **Lorentz-violating family (Einstein-aether / khronometric / Hořava)**, with GR at the boundary (preferred-frame couplings → 0). Which member is fixed in §6. **[OC classification; IR adoption]**

### 5.4 Does the dynamics come out Einstein? The gradient-order make-or-break

Whether the incompatible (defect) sector's dynamics is **Einstein** or a softer gravity is decided by the gradient-order of the effective elastic energy (Kleinert's world-crystal result):

| Effective elasticity | Defect–defect interaction | Emergent gravity |
|:--|:--|:--|
| first-gradient (ordinary, $\sim(\partial u)^2$) | $\sim 1/k^4$ | **not** Einstein — soft/higher-derivative |
| second-gradient ($\sim(\partial^2 u)^2$) | $\sim 1/k^2$ | **linearized Einstein** |

So "does an Einstein $R$-term exist?" sharpens to **one computable question:** *is the SOSF substrate's effective elasticity (or its fluctuation-induced form) first- or second-gradient — equivalently, is the defect interaction $1/k^2$ or $1/k^4$?* This is simulator-addressable: compute the defect–defect interaction on the SOSF skeleton and read off the power. **It gates everything downstream** — if $1/k^4$, the Einstein-aether PPN framework (and the §6.7 $\alpha_1=0$ result) does not strictly apply and the theory is a higher-derivative gravity instead. **[OC for the Kleinert criterion; the SOSF result is open]**

*Complementary loop route [RH].* Sakharov induction (integrating out substrate fluctuations against the $\ell_P$ cutoff) generates $\int\sqrt{-g}\,(\Lambda+\kappa R+\cdots)$, $G_{\rm ind}\sim\ell_P^2$. This can contribute the $R$-term even if the bare elasticity is first-gradient, but brings the usual induced cosmological-constant problem and an uncomputed sign/dominance. Secondary to the structural Kleinert route, which is tied to the actual lattice. **[RH]**

*Flag, not a claim [RH].* Block I derived a $k^{-2}$ *energy spectrum* (I-§10). A $k^{-2}$ energy spectrum and a $1/k^2$ *Green's function* are a priori different objects; whether the substrate's native $k^{-2}$ structure relates to the desired $1/k^2$ Einstein-defect propagator is worth checking when §5.4 is computed — flagged, not load-bearing.

---

## 6. The gravity class, identified — khronometric gravity

*All of §6 is **conditional on §5.4 yielding the Einstein ($1/k^2$) structure.** If §5.4 gives $1/k^4$, replace "Einstein-aether" below with the appropriate higher-derivative-gravity analysis.*

### 6.1 Infinite sound speed = global foliation = the khronon

The instantaneous longitudinal/pressure response (II-§7) means instantaneous simultaneity across all space — a global time function — a preferred foliation. A dynamical preferred foliation defined by the gradient of a scalar time field is the **khronon** of khronometric gravity (hypersurface-orthogonal Einstein-aether / low-energy Hořava). The substrate gives the *hypersurface-orthogonal* aether specifically, because infinite sound speed supplies a genuine global time. **[OC classification; IR identification]**

### 6.2 The two projections are the two sectors

| Substrate projection (I-§7) | Sector | Character |
|:--|:--|:--|
| longitudinal / pressure $p$ (instantaneous Coulomb) | **khronon** (preferred foliation) | non-propagating, elliptic constraint |
| transverse / vorticity $\boldsymbol\omega$ (finite $c$) | **spin-2 graviton** | propagating shear wave = light's sibling |

The split that defined the electrodynamics is the split of the gravity. **[IR]**

### 6.3 Structural win — survives GW170817

GW and light are the *same transverse shear sector*, so $c_{\rm GW}=c_\gamma=\sqrt{C_{66}/\rho}$ **structurally**. The framework automatically passes $|c_{\rm GW}/c_\gamma-1|\lesssim10^{-15}$ — the constraint fatal to generic members of its own class. Genuine but narrow; says nothing about $\alpha_1,\alpha_2$. **[OC/IR]**

### 6.4 The make-or-break — preferred-frame PPN ($\alpha_1,\alpha_2$)

$\alpha_1,\alpha_2$ vanish in GR and are bounded $\alpha_1\lesssim10^{-4}$, $\alpha_2\lesssim10^{-7}$. **GR is the $\alpha_1,\alpha_2\to0$ limit.** The framework's divergence from Einstein is exactly these two numbers — its empirical content. Computed in §6.7. **[OC bounds; framework result in §6.7]**

### 6.5 Khronon pathology possibly tamed by infinite sound speed [RH]

The khronon is the *infinite-speed* longitudinal sector, so it does not propagate — it is an elliptic constraint (like the Newtonian potential), which cannot be a ghost or carry a gradient instability. The substrate's non-Lorentzian feature may thus remove the standard Hořava scalar-mode pathology. **Caveat:** low-energy *strong coupling* is a separate disease, not addressed by an infinite speed; only an explicit mode/strong-coupling analysis settles it (§10.2). **[RH]**

### 6.6 What the framework inherits

Khronometric gravity's open problems come with it: the strong-coupling question; possible $G_{\rm cosmo}\neq G_N$ (BBN-bounded $\sim10\%$); general contestation of Hořava-class theories. The reframe buys honesty, not freedom from constraint; the risk relocates to $\alpha_1,\alpha_2$ and the cosmological-$G$ ratio. **[OC]**

### 6.7 Preferred-frame parameters computed — $\alpha_1=0$ forced; $\alpha_2$ at a singularity

*Conditional on §5.4 (Einstein structure) and on the induced action having Einstein-aether form.* Write the aether couplings $c_1,c_2,c_3,c_4$; $c_{13}\equiv c_1+c_3$, $c_{14}\equiv c_1+c_4$. The mode speeds are physical and matched directly to the substrate:

- **Graviton speed $=$ light speed.** Spin-2: $s_2^2=1/(1-c_{13})$; the graviton *is* light, so $s_2=c_\gamma\Rightarrow \boxed{c_{13}=0}$ (also the GW170817 condition — here structural).
- **Khronon speed $=\infty$.** The spin-0 speed carries $c_{14}$ in its denominator, $s_0^2\propto1/c_{14}$; the locked infinite sound speed $\Rightarrow \boxed{c_{14}=0}$.

**Evaluate $\alpha_1$.** With the standard form $\alpha_1=-8(c_3^2+c_1c_4)/(2c_1-c_1^2+c_3^2)$ and $c_{13}=0$ (so $c_3=-c_1$):
$$c_3^2+c_1c_4=c_1^2+c_1c_4=c_1(c_1+c_4)=c_1\,c_{14},\qquad 2c_1-c_1^2+c_3^2=2c_1,$$
$$\boxed{\;\alpha_1=-4\,c_{14}\;}\ \xrightarrow{\;c_{14}=0\;}\ \alpha_1=0.$$
The exact numerical coefficient is convention-dependent; the robust content is **$\alpha_1\propto c_{14}$, vanishing in the instantaneous limit.** Both defining features of the framework — light-is-the-graviton *and* infinite sound speed — drive the tightly-bounded $\alpha_1$ to zero **by structure, not tuning**, and the result depends only on $c_{13},c_{14}$, **not** on the un-fixed $c_1,c_2$. **[OC given the premises]**

**$\alpha_2$ is parked at a singularity.** $\alpha_2$ carries $c_{14}$ in its denominator (scalar sector), so $c_{14}=0$ is singular for the standard finite-speed formula; and the relevant numerator factor $(c_1+2c_3-c_4)=c_1-2c_1+c_1=0$ also vanishes under the substrate conditions — a $0/0$. The hint (numerator vanishing too) suggests a removable singularity but **is not a result.** $\alpha_2$ requires the post-Newtonian expansion **redone with the khronon as an instantaneous elliptic constraint** rather than a propagating mode, and it also depends on the un-fixed $c_2$. This is the residual preferred-frame make-or-break (§10.3). **[honest open]**

---

## 7. The stress-energy source — the incompatible sector (locking the gates)

The §5.2 split already answers the README's sub-question: the curvature source is the **incompatible strain $=$ the defect density**, and defects are the fermion-gate matter. Disclination density $\leftrightarrow$ curvature, dislocation density $\leftrightarrow$ torsion. **[OC dictionary]**

> Matter curves the emergent space because, in the defect-geometry dictionary, the defect density that *is* matter is the same object that *is* the curvature source. The fermion gate supplies $T_{\mu\nu}$; the gates are one sector. **[IR identification; RH for "this is GR's stress-energy" — and in the khronometric reading the field equation is the preferred-frame generalisation, not Einstein's]**

The non-defect source is the energy–momentum of the compatible-sector excitations (phonon/photon), entering via anharmonic softening of $C_{66}$ (§3). So $T^{\text{eff}}_{\mu\nu}=T^{\text{excitations}}_{\mu\nu}+T^{\text{defects}}_{\mu\nu}$. **[IR]**

---

## 8. Consistency threads with Blocks I–III

- **Isotropy carries over (necessary).** $\beta=\alpha$ ($A=1$, III-§6) is necessary for the gravity sector too; not sufficient for $\gamma=1$ (§4). **[OC/IR]**
- **GW = light's sibling.** Same transverse shear sector ⇒ $c_{\rm GW}=c_\gamma$ structurally (§6.3) — post-diction, not fit. **[IR]**
- **Planck-modified gravity in the UV.** The $(k\ell_P)^2$ dispersion (III-§5) applies to gravitational shear excitations (high-frequency GW dispersion), consistent with the khronometric/aether classification. **[IR]**
- **Longitudinal sector = khronon.** Gravity is transverse; the instantaneous longitudinal sector (II-§7) is the khronon (§6.1). Strong-field mutual consistency open (§10.7). **[OC/IR]**

---

## 9. Verdict

Measured against the real question — *what gravity does the substrate predict, and where could it die?*:

| Property | Result | Tier |
|:--|:--|:--|
| Kinematic curved metric for light | **Yes**, robustly | [OC] |
| Newtonian / Poisson static limit | **Yes**, generic to 3-D elasticity | [OC/IR] |
| Light bending (richer than Nordström) | **Yes** | [OC] |
| **Gravity & matter = one (incompatible) sector**; light = compatible sector | **Yes** (Kröner/defect geometry) | [OC/IR] |
| **Is the dynamics Einstein?** | **Undecided — hinges on §5.4**: $1/k^2$ (Einstein) vs $1/k^4$ (softer). The gating computation. | [OC criterion; open] |
| Identified class (if Einstein-structured) | **Khronometric gravity**, forced by infinite-sound-speed foliation | [OC/IR] |
| $c_{\rm GW}=c_\gamma$ (GW170817) | **Passes structurally** | [OC/IR] |
| $\alpha_1$ (preferred-frame, $\lesssim10^{-4}$) | **$=0$, forced** by $c_{13}=c_{14}=0$; robust against unknown $c_1,c_2$ | [OC given §5.4] |
| $\alpha_2$ (preferred-frame, $\lesssim10^{-7}$) | **Open** — $0/0$ at the instantaneous limit; needs redone PPN | [open] |
| PPN $\gamma=1$ | **Attainable** in this class; uncomputed | [OC; open] |
| Relation to GR | GR $=$ the $\alpha_1,\alpha_2\to0$ limit; framework predicts distinct, bounded preferred-frame effects | [OC/IR] |
| §5.1 status | **Corrected** (phonon massless; compatibility, not mass, is the issue) | [OC] |

**Bottom line.** The framework now has a single coherent picture: **one chiral vortex lattice whose compatible (defect-free) sector is light and whose incompatible (defect) sector is gravity-and-matter.** Whether that gravity is *Einstein* or a *softer higher-derivative* gravity is decided by one computable power-law (§5.4, $1/k^2$ vs $1/k^4$) — the gate on everything else. *If* it is Einstein-structured, the theory is **khronometric gravity** that passes GW170817 structurally and has its hardest-but-one preferred-frame parameter **forced to zero ($\alpha_1=0$)** by the same two features that define the substrate — a real, non-tuned win — with $\alpha_2$ the remaining live risk at a singular limit. GR is recovered as the $\alpha_1,\alpha_2\to0$ limit; the framework's divergences are its falsifiable content, and they are tightly bounded, so the danger is real and located. Honest net: the construction is more unified and one error lighter than at v0.2, the deepest gate is now a specific calculation rather than a mystery, but the dynamics is **not yet shown to be Einstein**.

---

## 10. Open forks / to-derive next

1. **Gradient-order / defect-interaction power-law — THE gate (§5.4).** Compute the SOSF defect–defect interaction: $1/k^2$ (Einstein, Kleinert) or $1/k^4$ (softer)? Decides whether all of §6 applies. Simulator-addressable. Also check the I-§10 $k^{-2}$ flag.
2. **Khronon strong-coupling / mode health (§6.5).** Explicit mode analysis of the instantaneous (non-propagating) khronon: free of low-energy strong coupling, or not?
3. **$\alpha_2$ at the instantaneous limit (§6.7).** Redo the PPN expansion with the khronon as an elliptic constraint; evaluate the $0/0$. Depends on the un-fixed $c_2$.
4. **Sign of the energy→softening coupling (§3).** Soften or stiffen $C_{66}$ under excitation energy? Only softening gives attraction; fixes $G_{\text{eff}}$.
5. **PPN $\gamma$ (§4).** Does $\beta=\alpha$-isotropized elasticity give $\gamma=1$ to the Cassini bound?
6. **Cosmological $G$ vs Newtonian $G$ (§6.6).** Compute $G_{\rm cosmo}/G_N$; confront BBN.
7. **Strong-field consistency (§8).** Instantaneous longitudinal sector vs finite-$c$ transverse metric beyond weak field; horizons.
8. **Fermion gate (README §6B).** Now *identical* to the gravity source (§5.2, §7): derive the SOSF defect spectrum, test spin-½ / spin-statistics, feed back as $T^{\text{defects}}_{\mu\nu}$ for items 1, 3, 6. The defect interaction of item 1 is the same object.

---

## Appendix — symbols & core relations

### Symbols

| Symbol | Meaning |
|:--|:--|
| $C_{66}$, $c=\sqrt{C_{66}/\rho}$ | transverse shear modulus / emergent light (and GW) speed |
| $s=\delta C_{66}/C_{66}^0$, $\Phi=\tfrac12 c_0^2 s$ | softening field / emergent Newtonian potential |
| $\varepsilon_{ij}=\partial_{(i}u_{j)}$ | strain (field strength of the displacement $u$); the metric perturbation |
| $\eta_{ij}$ | incompatibility tensor $=$ linearized Einstein tensor (Kröner); $=0$ ⟺ compatible/flat |
| $\gamma$ | PPN light-bending parameter; $\gamma=1$ ⟺ GR |
| $\alpha_1,\alpha_2$ | PPN **preferred-frame** parameters; $=0$ in GR; the framework's empirical content |
| $c_1,c_2,c_3,c_4$; $c_{13},c_{14}$ | Einstein-aether couplings; $c_{13}=0$ (graviton=light), $c_{14}=0$ (instantaneous khronon) |
| khronon | scalar of the preferred foliation = substrate's instantaneous simultaneity surfaces (= longitudinal sector) |
| $\alpha,\beta$ | radial / line-tension elastic stiffnesses; isotropy at $\beta=\alpha$ (III-§6) |
| $T^{\text{defects}}_{\mu\nu}$ | stress-energy from defects = fermion-gate matter = incompatible-sector curvature source |
| $\ell_P$ | Planck-scale cutoff; sets Sakharov $G_{\rm ind}$ and UV Lorentz violation |

### Core relations

$$ds^2_{\text{eff}}=-c(\mathbf{x})^2dt^2+d\mathbf{x}^2,\qquad \Phi=\tfrac12 c_0^2\,\delta C_{66}/C_{66}^0,\qquad \nabla^2\Phi=4\pi G_{\text{eff}}\rho_{\text{source}}$$

$$\eta_{ij}=\epsilon_{ikl}\epsilon_{jmn}\partial_k\partial_m\varepsilon_{ln}:\quad \eta=0\ \Rightarrow\ \text{flat}\ \Rightarrow\ \text{phonon}=\textbf{light};\qquad \eta\neq0\ \Rightarrow\ \text{defects}\ \Rightarrow\ \textbf{gravity+matter}$$

$$\text{defect interaction}\ \sim 1/k^2\ (\text{2nd-gradient}\Rightarrow\textbf{Einstein})\quad\text{vs}\quad 1/k^4\ (\text{1st-gradient}\Rightarrow\text{softer})\qquad\textbf{(§5.4 gate)}$$

$$\text{infinite sound speed}\Rightarrow\text{global foliation}\Rightarrow\text{khronon}\Rightarrow\textbf{khronometric gravity}$$

$$c_{13}=0\ (\text{graviton=light}),\quad c_{14}=0\ (\text{instantaneous khronon})\ \Rightarrow\ \alpha_1=-4c_{14}=\mathbf{0};\qquad \alpha_2:\ 0/0\ \text{(open)}$$

$$c_{\rm GW}=c_\gamma=\sqrt{C_{66}/\rho}\ \Rightarrow\ \text{passes GW170817 structurally};\qquad \alpha_1,\alpha_2\to0\ \Rightarrow\ \text{GR}$$

---

*Document status: [exploratory; internally consistent; tiers honest]. Block IV v0.3 unifies the gravity and fermion gates into the compatible/incompatible split of one lattice (light = compatible, gravity+matter = incompatible), corrects the §5.1 mass-term error, and reports the first preferred-frame computation: $\alpha_1=0$ forced by the substrate's two locked features. The gating open question is the defect-interaction power-law ($1/k^2$ vs $1/k^4$, §5.4/§10.1) — it decides whether the dynamics is Einstein. The fermion gate is now the same object.*
