# DCCREG Block IV — Emergent Gravity from Vortex-Lattice Elasticity

**Version:** 0.1 (Gravity-gate block)

**Scope of this document:** whether the spatially varying transverse stiffness $C_{66}$ of the chiral vortex lattice (Block III) gives rise to *gravity* — i.e. whether a strain field in the vortex vacuum acts as an effective curved metric for the emergent light, and whether the back-reaction dynamics of that strain field is **Einstein-like** ($G_{\mu\nu}=8\pi T_{\mu\nu}$), **Nordström/scalar-like**, or something between. It establishes the kinematic analog metric, the strain→metric dictionary and the Newtonian/Poisson limit, the light-bending sub-test (PPN $\gamma$), the honest classification of the dynamics as preferred-frame "aether" gravity with a Newtonian core, the two candidate routes to genuine Einstein dynamics (Sakharov induction, Kleinert world-crystal), and the stress-energy source via the defect–elasticity dictionary (which locks the gravity gate to the fermion gate). It opens, but does not close, the question of whether GR is recovered.

**Companion documents:** Block I (*Foundations* v0.4), Block II (*MHD Emergence* v0.2), Block III (*Radiative EM & Emergent Lorentz Invariance* v0.2). References prefixed **I-§ / II-§ / III-§** point to those; unprefixed **§** is internal to this block.

> **Status of this block.** Built directly on Block III's now-computed transverse modulus $C_{66}$ and its emergent-Lorentz-invariance reading. The *kinematic* analog-gravity mechanism is standard physics **[OC]**; the *Newtonian limit* is a standard elasticity result re-read as gravity **[OC/IR]**; the *classification of the dynamics* (aether-gravity, not Einstein) is an honest [OC] structural argument; the *routes to genuine Einstein dynamics* and *gravity as the defect-curvature sector* are **[RH]**. This block does **not** claim to derive General Relativity. It claims to locate, precisely and honestly, where the construction sits relative to GR, and to name the one decisive calculation that would falsify or promote it.

---

## Revision history

| Version | Date | Author | Summary of changes |
|:--|:--|:--|:--|
| 0.1 | 2026-05-29 | DCCREG Modeling Programme | Initial release — Gravity-gate block (Sections 0–9 and Appendix). (1) **Kinematic metric** (§2): varying $C_{66}(x)$ ⇒ position-dependent $c$ ⇒ effective acoustic/elastic metric for the emergent light; light-cones tilt and curve (textbook analog gravity). (2) **Strain→metric dictionary + Newtonian limit** (§3): $\Phi = \tfrac12 c_0^2\,\delta C_{66}/C_{66}$; a localized dilatation source in 3-D elasticity yields a $1/r$ potential obeying $\nabla^2\Phi=$ source — Newtonian gravity is generic, with $G$ set by the elastic constants and the energy→softening coupling. (3) **Light bending / PPN $\gamma$** (§4): the model bends light (so it is **not** Nordström), but the coefficient $\gamma$ is a separate, not-yet-done elastic computation — declared the **make-or-break sub-test** of this block, parallel to III-§6's isotropy test. (4) **Dynamics classification** (§5): linear elasticity's $(\text{strain})^2$ energy is a Fierz–Pauli *potential*, not the Einstein–Hilbert *kinetic* term; combined with the substrate's preferred frame (III aether), the natural class is **Lorentz-violating (Einstein-aether / Hořava-type) gravity with a Newtonian core**, GR recoverable only in an IR limit. Two routes to genuine Einstein flagged **[RH]**: Sakharov induced gravity, Kleinert world-crystal. (5) **Stress-energy source** (§6): defect–elasticity dictionary — disclination density = curvature, dislocation density = torsion — so the fermion-gate defects source the curvature; the two gates lock together. (6) **Consistency** (§7): the $\beta=\alpha$ isotropy condition (III-§6) is necessary for the gravity sector too; light and gravitational waves share the transverse shear sector ⇒ equal speeds, consistent with GW170817. **Verdict** (§8): analog gravity + Newtonian core + genuine light bending + built-in matter→curvature source, but **not** Einstein dynamics without extra structure. |

---

## Epistemic tagging legend

- **[OC] Operational Core** — standard, derivable physics/mathematics; true independent of the framework.
- **[IR] Interpretive Reading** — a modeling identification within the framework; internally consistent, chosen rather than forced.
- **[RH] Resonance / Heuristic** — analogical/cosmological; suggestive, not load-bearing.

Tier discipline is the point of the programme (README §1). This block in particular resists the temptation to let "analog gravity works" (true, [OC]) drift into "we derived GR" (false). Where the construction stops short of Einstein, it says so.

---

## 0. Inheritance from Blocks I–III

Used here without re-derivation:

1. The substrate is ideal, incompressible, lossless, infinite sound speed; a preferred frame exists — **the lattice is, technically, an aether; Lorentz invariance is emergent** (I-§0, III-§5). This is *load-bearing* here, not incidental.
2. **Light = the transverse shear mode of the chiral vortex lattice**, $c=\sqrt{C_{66}/\rho}$ (III-§3). The vortex vacuum is a *solid for transverse perturbations* (finite shear rigidity → light at $c$) and an *incompressible fluid for longitudinal ones* (infinite bulk modulus → infinite sound).
3. The transverse elastic tensor was **computed** (III-§6): central Biot–Savart forces give Zener ratio $A=2/3$ (anisotropic); the **achiral** vortex line tension $\beta$ restores isotropy $A=1$ at the natural ratio $\beta=\alpha$ (both $\propto\rho\Gamma^2$, so $\beta/\alpha\sim\ln(d/a)/4\sim O(1)$). Chirality's separate role is optical activity, not isotropy.
4. Modified dispersion $\omega^2=c^2k^2[1-\alpha(k\ell_P)^2+\cdots]$: Lorentz invariance exact in the IR, Planck-suppressed violation in the UV (III-§5).
5. The substrate carries **topological-defect potential** — disclinations, dislocations, linked/knotted vortices (III-§8, the fermion gate). Held in reserve until §6.

---

## 1. The claim to be tested

> **The gravity-gate hypothesis (README §6A).** Where the lattice is strained, $C_{66}$ — hence $c$ — varies; the emergent light-cone tilts and curves; a spatially varying lattice-strain field is therefore an *effective curved metric* for the emergent light. The question is whether the **back-reaction dynamics** of that strain field resembles $G_{\mu\nu}=8\pi T_{\mu\nu}$, or only a weaker (Nordström/scalar) gravity — and what plays the role of the stress-energy source.

The hypothesis has two clearly separable halves, and the honesty of the block depends on never conflating them:

- **(K) Kinematics:** *do excitations move as if in a curved spacetime?* — the metric that light/matter feels.
- **(D) Dynamics:** *does that metric obey Einstein's field equations?* — the law that says how matter curves the metric.

(K) is the easy, robust half (it is what every analog-gravity system delivers). (D) is the hard half, and is where essentially every emergent-gravity programme either stalls or invokes extra structure. We treat them in order.

---

## 2. The kinematic metric — analog gravity (the robust half)

A linear wave with a position-dependent speed $c(\mathbf{x})$ propagates according to a curved-space d'Alembertian. For the transverse shear mode, writing the equation of motion as
$$\partial_\mu\!\left(\sqrt{-g}\,g^{\mu\nu}\partial_\nu\phi\right)=0,$$
defines an **effective (acoustic/elastic) metric** $g_{\mu\nu}^{\text{eff}}$ whose null cones are exactly the surfaces $c(\mathbf{x})\,dt = |d\mathbf{x}|$. In the simplest isotropic, weak-field case,
$$ds^2_{\text{eff}} = -c(\mathbf{x})^2\,dt^2 + d\mathbf{x}^2. $$

This is the standard analog-gravity construction (Unruh's sonic metric; Barceló–Liberati–Visser). It is **kinematically complete**: where $C_{66}$ softens, $c$ drops, the cone narrows and tilts, and null rays bend toward the soft region. Horizons form where $c\to 0$ relative to a flow; Hawking-like analog radiation is available in principle. **[OC]**

What the construction does *not* yet say is how $C_{66}(\mathbf{x})$ — equivalently $g_{\mu\nu}^{\text{eff}}$ — is *determined*. That is (D), deferred to §5. The metric is real and curved; its **law of motion** is the open question.

---

## 3. Strain→metric dictionary and the Newtonian limit

**The dictionary.** Let the shear modulus carry a small dimensionless softening field $s(\mathbf{x})$:
$$C_{66}(\mathbf{x}) = C_{66}^{0}\,[1+s(\mathbf{x})], \qquad c(\mathbf{x}) = c_0\sqrt{1+s}\approx c_0\!\left(1+\tfrac{s}{2}\right).$$
Matching $-g_{00}=c^2/c_0^2 = 1+s$ to the weak-field form $-g_{00}=1+2\Phi/c_0^2$ identifies the **Newtonian potential**
$$\boxed{\;\Phi(\mathbf{x}) = \tfrac12\,c_0^{2}\,\frac{\delta C_{66}(\mathbf{x})}{C_{66}^{0}}\;}\qquad\textbf{[OC for the matching; IR for naming it gravity]}.$$
Attraction (a potential well, $\Phi<0$) requires $s<0$ — the lattice must **soften** where energy/matter concentrates. The natural mechanism is **anharmonic softening**: excitation energy density lowers the effective shear modulus. The *sign* of this coupling is an anharmonic property of the SOSF lattice not yet computed; that energy attracts (rather than repels) is therefore a prediction-to-check, not a result. **[IR]**

**Newtonian gravity is generic in 3-D elasticity.** A localized source of volumetric strain (a *centre of dilatation*) in a 3-D elastic continuum produces the displacement field
$$u_i(\mathbf{x}) \propto \frac{x_i}{r^3} = \partial_i\!\left(-\frac{1}{r}\right),$$
i.e. the gradient of a harmonic $1/r$ potential. The associated scalar field obeys a **Poisson equation** with the source at the origin. Re-read through the dictionary, this is precisely
$$\nabla^2\Phi = 4\pi G_{\text{eff}}\,\rho_{\text{source}},$$
with $G_{\text{eff}}$ fixed by the elastic constants and the energy→softening coupling. **The inverse-square law is not an assumption here — it is the 3-D elastic Green's function.** Static Newtonian gravity therefore emerges cleanly. **[OC for the elasticity; IR for the gravitational identification]**

This is the single strongest positive result of the block: the *static, weak-field* limit is on firm ground.

---

## 4. Light bending and the PPN $\gamma$ — the make-or-break sub-test

The Newtonian limit alone does not decide between scalar and tensor gravity. The discriminator is **light bending** and, quantitatively, the post-Newtonian parameter $\gamma$:
$$ds^2 = -\left(1+\frac{2\Phi}{c_0^2}\right)c_0^2\,dt^2 + \left(1-\frac{2\gamma\Phi}{c_0^2}\right)d\mathbf{x}^2,\qquad \text{light deflection}\propto \frac{1+\gamma}{2}.$$

- **Nordström / pure scalar gravity** has $g_{\mu\nu}\propto\eta_{\mu\nu}$ (conformally flat); null geodesics are conformally invariant, so **scalar gravity bends no light** ($\gamma=-1$, deflection zero). This is why it was abandoned after 1919.
- **General Relativity** has $\gamma=1$: the spatial metric curves, *doubling* the naïve Newtonian deflection. Measured by Cassini to $\gamma-1=(2.1\pm2.3)\times10^{-5}$.

**Where the DCCREG construction sits.** Because $c(\mathbf{x})$ varies *directly* (not merely as a conformal factor), the model **does** bend light — it is strictly richer than Nordström. **[OC]** But whether the strain also induces the *spatial-metric* variation with the GR coefficient ($\gamma=1$) is a **separate computation on the elastic tensor that has not been done.** A generic anisotropic-then-isotropized elastic medium will produce *some* $\gamma$, and there is no a priori reason it equals 1.

> **Make-or-break sub-test (parallel to III-§6).** The gravity gate lives or dies on $\gamma$. If the elastic computation yields $\gamma=1$ (to the Cassini bound), the construction reproduces solar-system GR; if not, it is falsified there. **Crucially, the Block III isotropy condition $\beta=\alpha$ ($A=1$) is *necessary but not sufficient*:** $A=1$ guarantees the *spatial* propagation is direction-independent (no gross rotational Lorentz violation), but $\gamma$ concerns the *partition of strain between $g_{00}$ and $g_{ij}$*, a logically distinct condition. So even with $A=1$ secured, $\gamma$ remains open. This is the decisive calculation of the next iteration. **[OC for the framework; result genuinely open]**

---

## 5. The dynamics question — is the back-reaction Einstein? (the honest core)

Here is where the block must not flinch.

**5.1 — Linear elasticity is a Fierz–Pauli *potential*, not the Einstein *kinetic* term.**
The substrate action is the elastic one,
$$S \;\propto\; \int dt\,d^3x\;\Big[\,\rho\,(\partial_t u_i)^2 \;-\; C_{ijkl}\,\partial_i u_j\,\partial_k u_l\,\Big].$$
Identifying the metric perturbation with the strain, $h_{ij}\sim \partial_{(i}u_{j)}$, the gradient energy $C(\partial u)^2 \sim C\,h^2$ is — in metric language — a term **quadratic in $h$ with no derivatives**: the structure of a **Fierz–Pauli mass / potential** term, not the Einstein–Hilbert kinetic term $\sim(\partial h)^2$. The only derivative structure on $h$ comes from the $\rho(\partial_t u)^2$ kinetic term, i.e. **time derivatives only**. So the field equation for $u$ is the elastic wave equation $\rho\,\ddot u_i = \partial_j(C_{ijkl}\partial_k u_l)$ — *not* the linearized Einstein equation $\Box \bar h_{\mu\nu}=-16\pi G\,T_{\mu\nu}$, which is fully covariant (space and time derivatives on equal footing, with diffeomorphism gauge symmetry). **[OC]**

A consolation worth recording: the transverse shear mode has **exactly two polarizations** (III-§3), matching the two graviton polarizations. The *kinematic* count is right; it is the *dynamical law* that differs.

**5.2 — The preferred frame forces a Lorentz-violating gravity class.**
The substrate has a preferred rest frame (the lattice; infinite sound speed; III-§5). A diffeomorphism-invariant theory has *no* preferred frame. Therefore the emergent gravitational dynamics **cannot be fundamentally GR**; it must carry the preferred frame as a dynamical structure. The natural home for "gravity with a dynamical preferred foliation" is the family of **Lorentz-violating gravities — Einstein-aether / khronometric / Hořava-type.** In these theories GR is recovered only in a limit where the preferred-frame couplings vanish (an IR limit), exactly mirroring Block III's "Lorentz invariance is emergent and IR-exact, Planck-violated in the UV." The gravity sector inherits the same trans-Planckian aether remnant as the light sector. **[OC for the classification; IR for adopting it as the framework's gravity]**

This is the honest answer to the README's binary: **neither pure Nordström (light *does* bend) nor full Einstein (no covariant dynamics, preferred frame present).** The construction's natural gravity is an **aether/Hořava-class theory with a Newtonian core and genuine light bending**, with GR as a special IR limit.

**5.3 — Two routes that *could* promote it to genuine Einstein (both [RH]).**

1. **Sakharov induced gravity.** Even if the bare elastic action contains no Einstein–Hilbert term, integrating out the substrate's quantum fluctuations propagating on $g^{\text{eff}}_{\mu\nu}$ generates, at one loop, an effective action containing $\int\sqrt{-g}\,(\Lambda + \kappa R + \cdots)$, with an *induced* Newton constant $G_{\text{ind}}\sim 1/(\kappa)\sim \ell_P^{2}$ set by the cutoff. The DCCREG substrate has a natural cutoff ($\ell_P$, the SOSF floor), which is precisely the ingredient Sakharov's mechanism needs. So Einstein dynamics might be **induced** rather than built in. This is plausible and attractive but **not derived here** — the sign and magnitude of $\kappa$, and whether the induced term dominates the bare elastic potential, are uncomputed. **[RH]**
2. **Kleinert world-crystal.** Ordinary elasticity gives a metric propagator $\sim 1/k^4$ (a static/Newtonian-type response), whereas Einstein gravity needs $\sim 1/k^2$. Kleinert showed that a *fluctuating crystal with proliferating defects* ("floppy world crystal") converts the former into the latter, reproducing linearized Einstein gravity from defect elasticity. Whether the SOSF vortex lattice is of this type — in particular whether its defect sector (§6) proliferates in the required way — is unknown. **[RH]**

Both routes are real, named mechanisms in the literature, not hand-waving; but both are *conjectures about this substrate* until computed.

---

## 6. The stress-energy source — defects as curvature (locking the two gates)

The README's key sub-question: *what plays the role of the stress-energy source?* The construction answers this cleanly, and the answer ties the gravity gate to the fermion gate.

**The defect–elasticity dictionary.** In an elastic continuum, the geometry induced by the strain field has its **curvature sourced by disclinations** and its **torsion sourced by dislocations** (the standard differential geometry of crystal defects; Kleinert, Katanaev–Volovich). The defect density *is* the curvature two-form of the strain geometry:
$$\text{disclination density}\;\longleftrightarrow\;\text{curvature }(R_{\mu\nu}\text{-like}),\qquad \text{dislocation density}\;\longleftrightarrow\;\text{torsion}.$$
**[OC for the defect geometry]**

So the source of emergent curvature is the **defect density** — and the fermion-gate programme (III-§8, README §6B) identifies *matter* with exactly that defect sector (linked/knotted vortices, disclinations, dislocations). Therefore:

> **Matter curves the emergent space because, in the elastic-geometry dictionary, the defect density that *is* matter is the same object that *is* the curvature source.** The gravity gate and the fermion gate are not independent: the fermion gate supplies the $T_{\mu\nu}$ that the gravity gate needs. **[IR for the identification; RH for "this is the stress-energy of GR"]**

The **non-defect** part of the source is the energy–momentum of the propagating excitations (the phonon/photon sector), which feeds in through the anharmonic softening of $C_{66}$ (§3). Together: $T_{\mu\nu}^{\text{eff}} = T^{\text{excitations}}_{\mu\nu} + T^{\text{defects}}_{\mu\nu}$, the second being the matter sector proper. **[IR]**

This is the most satisfying structural result of the block — but note its tier: the *dictionary* is [OC], the *identification of defects with the GR source* is [IR], and *the resulting field equation being Einstein's* remains [RH] (it inherits the §5 limitation: a source for *what dynamics?*).

---

## 7. Consistency threads with Blocks I–III

- **Isotropy carries over (necessary condition).** A cubic/octahedral lattice gives anisotropic elasticity; the same $\beta=\alpha$ ($A=1$) condition that isotropizes light (III-§6) is **necessary** for the gravitational sector to be isotropic. The "passes in the favourable sense" result of Block III therefore extends to gravity *as a necessary condition* — but, per §4, **not a sufficient** one for $\gamma=1$. **[OC/IR]**
- **Gravitational waves = light's sibling.** Both light and the fluctuations of $g^{\text{eff}}$ are excitations of the *same* transverse shear sector. Hence gravitational waves and light propagate at the **same speed**, $c=\sqrt{C_{66}/\rho}$, at leading order. This is a genuine post-diction: GW170817 constrains $|c_{\text{GW}}-c_\gamma|/c<10^{-15}$, and a construction in which both ride the one shear modulus delivers $c_{\text{GW}}=c_\gamma$ structurally. **[IR — a virtue, not a fit]**
- **Planck-modified gravity in the UV.** The $(k\ell_P)^2$ dispersion (III-§5) applies to the gravitational shear excitations too: emergent gravity is Lorentz-violating at the Planck scale, consistent with the §5.2 aether classification. **[IR]**
- **No light at $c$ from the longitudinal sector, still.** Gravity here is a *transverse* (shear) phenomenon; the instantaneous longitudinal/Coulomb sector (II-§7) is untouched and remains the Newtonian *instantaneous* limit's natural partner — worth checking whether the instantaneous longitudinal response and the finite-speed transverse metric are mutually consistent in a strong field (open, §9). **[OC/IR]**

---

## 8. Verdict

Re-reading the README's binary — *Einstein-like $G_{\mu\nu}=8\pi T_{\mu\nu}$, or only weaker Nordström/scalar gravity?* — the honest placement is **between the two and short of Einstein**:

| Property | Delivered? | Tier |
|:--|:--|:--|
| Kinematic curved metric for light (analog gravity) | **Yes**, robustly | [OC] |
| Newtonian / Poisson static limit ($\nabla^2\Phi=$ source) | **Yes**, generic to 3-D elasticity | [OC/IR] |
| Light bending (richer than Nordström) | **Yes** ($c$ varies directly) | [OC] |
| Correct light-bending coefficient ($\gamma=1$) | **Open** — the make-or-break sub-test | [OC framework; result open] |
| Built-in matter→curvature source | **Yes**, via defect–elasticity (ties to fermion gate) | [IR/RH] |
| Full nonlinear, diffeomorphism-invariant Einstein dynamics | **No**, not without extra structure | [OC limitation] |
| Natural classification of the dynamics | **Lorentz-violating aether/Hořava-type with a Newtonian core**; GR as IR limit | [OC/IR] |
| Routes to genuine Einstein | Sakharov induction; Kleinert world-crystal | [RH] |

**Bottom line.** The gravity gate yields *analog gravity with a Newtonian core, genuine light bending, and a matter source built from the lattice's own defects* — a real, structured, falsifiable emergent gravity. It does **not** yield General Relativity. The construction's preferred frame (the locked aether) makes the *natural* emergent gravity a Lorentz-violating one, with GR recoverable only in an IR limit or via an induced-gravity / world-crystal promotion that is conjectured, not derived. This is exactly the honest position the firewall demands: a substantial positive result (Newton + analog metric + defect source) sitting beneath a clearly marked ceiling (no Einstein dynamics yet), with one decisive calculation ($\gamma$) named as the next gate.

---

## 9. Open forks / to-derive next

1. **PPN $\gamma$ — the make-or-break (§4).** Compute the spatial-metric response of the strained vortex lattice and extract $\gamma$. Does the $\beta=\alpha$-isotropized elastic tensor give $\gamma=1$ to the Cassini bound, or a measurable deviation (a Lorentz/GR-violation prediction)? This is the decisive next step.
2. **Sign and magnitude of the energy→softening coupling (§3).** Does excitation energy density soften or stiffen $C_{66}$? Only softening gives attractive gravity. Compute the relevant anharmonic coefficient of the SOSF lattice; this also fixes $G_{\text{eff}}$.
3. **Sakharov induced-gravity term [RH] (§5.3).** Compute (or bound) the one-loop induced Einstein–Hilbert coefficient $\kappa$ against the $\ell_P$ cutoff; determine whether it dominates the bare elastic potential and so promotes the dynamics toward Einstein.
4. **World-crystal test [RH] (§5.3).** Determine whether the SOSF defect sector proliferates in the Kleinert sense (does the metric propagator go $1/k^4\to1/k^2$?). Requires the fermion-gate defect spectrum.
5. **Strong-field / consistency of the two sectors (§7).** Check that the instantaneous longitudinal (Coulomb) sector and the finite-speed transverse (gravitational) metric remain mutually consistent beyond weak field; identify whether horizons form consistently.
6. **The aether-gravity action explicitly (§5.2).** Write the emergent gravitational action in Einstein-aether / khronometric form and identify the preferred-frame coupling constants in terms of the elastic constants; confront them with existing Lorentz-violation-in-gravity bounds.
7. **Fermion gate (README §6B).** Now strongly motivated by §6: if defects are the curvature source, derive the defect spectrum, test spin-½ / spin-statistics, and feed the result back as $T^{\text{defects}}_{\mu\nu}$ for items 3–4.

---

## Appendix — symbols & core relations

### Symbols

| Symbol | Meaning |
|:--|:--|
| $C_{66}$, $c=\sqrt{C_{66}/\rho}$ | transverse shear modulus / emergent light (and GW) speed (III) |
| $s(\mathbf{x})=\delta C_{66}/C_{66}^{0}$ | dimensionless lattice-softening field |
| $\Phi=\tfrac12 c_0^2\,s$ | emergent Newtonian potential |
| $g^{\text{eff}}_{\mu\nu}$ | effective (acoustic/elastic) metric felt by the transverse mode |
| $G_{\text{eff}}$ | emergent Newton constant (set by elastic constants + softening coupling) |
| $\gamma$ | PPN light-bending parameter; $\gamma=1$ ⟺ GR; **the make-or-break sub-test** |
| $\alpha,\beta$ | radial / bond-bending (line-tension) elastic stiffnesses; isotropy at $\beta=\alpha$ (III-§6) |
| $T^{\text{defects}}_{\mu\nu}$ | stress-energy from topological defects = the fermion-gate matter (source of curvature) |
| $\ell_P$ | Planck-scale lattice cutoff; sets the Sakharov-induced $G_{\text{ind}}$ and the UV Lorentz violation |

### Core relations

$$ds^2_{\text{eff}} = -c(\mathbf{x})^2\,dt^2 + d\mathbf{x}^2,\qquad c(\mathbf{x})=\sqrt{C_{66}(\mathbf{x})/\rho}\qquad\text{(kinematic analog metric)}$$

$$\Phi = \tfrac12\,c_0^{2}\,\frac{\delta C_{66}}{C_{66}^{0}},\qquad \nabla^2\Phi = 4\pi G_{\text{eff}}\,\rho_{\text{source}}\qquad\text{(strain→potential; Newtonian/Poisson limit)}$$

$$\text{deflection}\propto\frac{1+\gamma}{2};\quad \gamma=1\ (\text{GR}),\ \ \gamma=-1\ (\text{Nordström});\quad \gamma_{\text{DCCREG}}=\ ?\ \text{(open — §4)}$$

$$\text{elastic EOM: }\ \rho\,\ddot u_i=\partial_j(C_{ijkl}\partial_k u_l)\ \neq\ \Box\bar h_{\mu\nu}=-16\pi G\,T_{\mu\nu}\quad\text{(not Einstein; §5.1)}$$

$$\text{disclination density}\leftrightarrow\text{curvature},\quad \text{dislocation density}\leftrightarrow\text{torsion}\quad\text{(defect source; §6)}$$

$$c_{\text{GW}}=c_\gamma=\sqrt{C_{66}/\rho}\quad\text{(shared transverse sector; consistent with GW170817)}$$

---

*Document status: [exploratory; internally consistent; tiers honest]. Block IV opens the gravity gate: analog metric + Newtonian core + defect source established at their stated tiers; full Einstein dynamics **not** derived. Decisive next calculation: the PPN $\gamma$. The fermion gate (README §6B) is now the natural partner, since defects are the curvature source.*
