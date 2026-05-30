# DCCREG Block IV — Emergent Gravity from Vortex-Lattice Elasticity

**Version:** 0.2 (Gravity-gate block)

**Scope of this document:** whether the spatially varying transverse stiffness $C_{66}$ of the chiral vortex lattice (Block III) gives rise to *gravity* — i.e. whether a strain field in the vortex vacuum acts as an effective curved metric for the emergent light, and **what class of gravitational theory the back-reaction dynamics belongs to.** It establishes the kinematic analog metric, the strain→metric dictionary and the Newtonian/Poisson limit, the light-bending test, the identification of the emergent dynamics as **khronometric gravity** (the hypersurface-orthogonal aether forced by the substrate's infinite sound speed), the confrontation of that theory with the preferred-frame observational bounds, and the stress-energy source via the defect–elasticity dictionary (which locks the gravity gate to the fermion gate). It treats General Relativity not as the target to be reproduced but as one falsifiable hypothesis to be compared against; the framework predicts a *specific, distinct* gravity, and GR is recovered as its $\alpha_1,\alpha_2\to0$ infrared limit.

**Companion documents:** Block I (*Foundations* v0.4), Block II (*MHD Emergence* v0.2), Block III (*Radiative EM & Emergent Lorentz Invariance* v0.2). References prefixed **I-§ / II-§ / III-§** point to those; unprefixed **§** is internal to this block.

> **Status of this block.** Built on Block III's computed transverse modulus $C_{66}$ and its emergent-Lorentz-invariance reading. The *kinematic* analog-gravity mechanism is standard physics **[OC]**; the *Newtonian limit* is a standard elasticity result re-read as gravity **[OC/IR]**; the *identification of the emergent dynamics as khronometric gravity* is an [OC] classification + [IR] identification; the *taming of the khronon by infinite sound speed* and *gravity as the defect-curvature sector* are **[RH]**. **This block does not aim to derive General Relativity, and does not treat failure to reproduce GR as a defect.** GR is a falsifiable theory; so is this one. What the block does is locate the construction precisely within the space of gravitational theories and name the measurements ($\alpha_1,\alpha_2$, cosmological $G$) that would confirm or kill it.

---

## Revision history

| Version | Date | Author | Summary of changes |
|:--|:--|:--|:--|
| 0.1 | 2026-05-29 | DCCREG Modeling Programme | Initial release — Gravity-gate block. Kinematic analog metric from varying $C_{66}$; strain→metric dictionary and Newtonian/Poisson limit; light bending (richer than Nordström) with PPN $\gamma$ as make-or-break; dynamics classified as Lorentz-violating aether/Hořava-type with a Newtonian core, GR as an IR limit; two routes to genuine Einstein flagged [RH] (Sakharov induction, Kleinert world-crystal); stress-energy source via the defect–elasticity dictionary (locking to the fermion gate); isotropy and GW-speed consistency threads. Verdict: analog gravity + Newtonian core + light bending + defect source, but **not** Einstein dynamics without extra structure. |
| 0.2 | 2026-05-29 | DCCREG Modeling Programme | **Gravity class identified + verdict reframed (major).** (1) **Khronometric identification** (new §6): the substrate's infinite sound speed supplies an instantaneous global simultaneity surface = a preferred foliation = the **khronon**, so the emergent theory is specifically **khronometric gravity** (hypersurface-orthogonal Einstein-aether / low-energy Hořava), *not* a generic aether. The I-§7 two projections map onto its two sectors: longitudinal/instantaneous = khronon (non-propagating constraint), transverse/finite-$c$ = spin-2 graviton. (2) **GW170817 structural win**: $c_{\rm GW}=c_\gamma$ automatically (both are the one transverse shear mode), so the framework passes the constraint that eliminated most of its own theory class — a genuine, narrow point in its favour. (3) **New make-or-break**: the preferred-frame PPN parameters $\alpha_1,\alpha_2$ (zero in GR, bounded $\lesssim10^{-4}$, $\lesssim10^{-7}$) are the framework's empirical content; **GR is the $\alpha_1,\alpha_2\to0$ limit.** This supplements the §4 PPN-$\gamma$ test. (4) **Khronon-pathology conjecture** [RH]: because the khronon is the *infinite-speed* longitudinal sector it does not propagate (elliptic constraint, like the Newtonian potential), so it cannot be a ghost or carry a gradient instability — the substrate's non-Lorentzian feature may *cure* the standard Hořava scalar pathology; caveat that low-energy strong coupling is a separate disease, not addressed. (5) **Verdict reframed** (§9): from "falls short of GR" to "predicts a specific falsifiable non-Einsteinian (khronometric) gravity"; the divergences from GR are relocated from a shortfall to the theory's testable signature, with the honest counterweight that those divergences are already tightly bounded. Renumbered: old §6→§7, §7→§8, §8→§9, §9→§10; new §6 inserted. Updated §5.2 cross-ref, open forks, Appendix. |

---

## Epistemic tagging legend

- **[OC] Operational Core** — standard, derivable physics/mathematics; true independent of the framework.
- **[IR] Interpretive Reading** — a modeling identification within the framework; internally consistent, chosen rather than forced.
- **[RH] Resonance / Heuristic** — analogical/cosmological; suggestive, not load-bearing.

Tier discipline runs in both directions here. The block must not let "analog gravity works" drift into "we derived GR" (the v0.1 guard); and, per the v0.2 reframe, it must not treat "this isn't GR" as a synonym for "this is wrong." Divergence from GR is empirical content, to be quantified and tested, not apologised for — *and* not waved through, since those divergences are exactly the tightly-bounded quantities.

---

## 0. Inheritance from Blocks I–III

Used here without re-derivation:

1. The substrate is ideal, incompressible, lossless, infinite sound speed; a preferred frame exists — **the lattice is, technically, an aether; Lorentz invariance is emergent** (I-§0, III-§5). This is *load-bearing* here: it is what fixes the gravity class (§6).
2. **Light = the transverse shear mode of the chiral vortex lattice**, $c=\sqrt{C_{66}/\rho}$ (III-§3). The vortex vacuum is a *solid for transverse perturbations* (light at $c$) and an *incompressible fluid for longitudinal ones* (infinite sound).
3. The transverse elastic tensor was **computed** (III-§6): central forces give Zener ratio $A=2/3$; the **achiral** vortex line tension $\beta$ restores isotropy $A=1$ at the natural ratio $\beta=\alpha$ (both $\propto\rho\Gamma^2$, $\beta/\alpha\sim\ln(d/a)/4\sim O(1)$).
4. Modified dispersion $\omega^2=c^2k^2[1-\alpha(k\ell_P)^2+\cdots]$: Lorentz invariance exact in the IR, Planck-suppressed in the UV (III-§5).
5. The two projections (I-§7): **scalar/pressure** (longitudinal, instantaneous Coulomb; II-§7) and **vector/vorticity** (transverse, finite $c$). This split is reused in §6 as the two sectors of the emergent gravity.
6. Topological-defect potential — disclinations, dislocations, linked/knotted vortices (III-§8, the fermion gate). Held until §7.

---

## 1. The claim to be tested

> **The gravity-gate hypothesis (README §6A).** Where the lattice is strained, $C_{66}$ — hence $c$ — varies; the emergent light-cone tilts and curves; a spatially varying lattice-strain field is therefore an *effective curved metric* for the emergent light. The question is what class of gravitational theory the **back-reaction dynamics** of that strain field belongs to — and what plays the role of the stress-energy source.

Two separable halves, never to be conflated:

- **(K) Kinematics:** *do excitations move as if in a curved spacetime?* — the robust half (§2–4).
- **(D) Dynamics:** *what law does that metric obey?* — the hard half (§5–6).

The v0.2 sharpening of (D): the answer is not "GR or failure" but "a specific identifiable theory in the Lorentz-violating family — khronometric gravity — with GR as a limiting case."

---

## 2. The kinematic metric — analog gravity (the robust half)

A linear wave with position-dependent speed $c(\mathbf{x})$ propagates by a curved-space d'Alembertian. Writing the shear-mode equation as
$$\partial_\mu\!\left(\sqrt{-g}\,g^{\mu\nu}\partial_\nu\phi\right)=0$$
defines an **effective (acoustic/elastic) metric** $g^{\text{eff}}_{\mu\nu}$ whose null cones are $c(\mathbf{x})\,dt=|d\mathbf{x}|$. Weak-field, isotropic:
$$ds^2_{\text{eff}}=-c(\mathbf{x})^2\,dt^2+d\mathbf{x}^2.$$
This is the standard analog-gravity construction (Unruh; Barceló–Liberati–Visser): where $C_{66}$ softens, the cone narrows and tilts, null rays bend toward the soft region, horizons form where $c\to0$ relative to a flow. **Kinematically complete and robust.** What it does *not* fix is the *law* determining $C_{66}(\mathbf{x})$ — that is (D), §5–6. **[OC]**

---

## 3. Strain→metric dictionary and the Newtonian limit

**The dictionary.** With $C_{66}(\mathbf{x})=C_{66}^{0}[1+s(\mathbf{x})]$, $\,c\approx c_0(1+s/2)$, matching $-g_{00}=1+s$ to $-g_{00}=1+2\Phi/c_0^2$:
$$\boxed{\;\Phi(\mathbf{x})=\tfrac12\,c_0^{2}\,\frac{\delta C_{66}(\mathbf{x})}{C_{66}^{0}}\;}\qquad\textbf{[OC matching; IR naming it gravity]}.$$
Attraction needs $s<0$: the lattice must **soften** where energy concentrates (anharmonic softening). The sign of this coupling is uncomputed — that energy attracts is a prediction-to-check, not a result. **[IR]**

**Newtonian gravity is generic in 3-D elasticity.** A centre of dilatation produces $u_i\propto x_i/r^3=\partial_i(-1/r)$ — the gradient of a harmonic $1/r$ potential obeying a **Poisson equation**. Through the dictionary this is $\nabla^2\Phi=4\pi G_{\text{eff}}\rho_{\text{source}}$, with $G_{\text{eff}}$ fixed by the elastic constants and the energy→softening coupling. **The inverse-square law is the 3-D elastic Green's function, not an assumption.** The static weak-field limit is on firm ground. **[OC elasticity; IR identification]**

---

## 4. Light bending and the PPN $\gamma$

The discriminator between scalar and tensor gravity is light bending, parametrised by $\gamma$:
$$ds^2=-\Big(1+\tfrac{2\Phi}{c_0^2}\Big)c_0^2dt^2+\Big(1-\tfrac{2\gamma\Phi}{c_0^2}\Big)d\mathbf{x}^2,\qquad \text{deflection}\propto\tfrac{1+\gamma}{2}.$$

- **Nordström/scalar** ($g\propto\eta$, conformally flat): bends no light ($\gamma=-1$). Dead since 1919.
- **GR**: $\gamma=1$. Cassini: $\gamma-1=(2.1\pm2.3)\times10^{-5}$.

The DCCREG construction **bends light** (because $c(\mathbf{x})$ varies directly) — strictly richer than Nordström. **[OC]** But the *coefficient* $\gamma$ is a not-yet-done elastic computation. Note $\beta=\alpha$ (III-§6, spatial isotropy $A=1$) is **necessary but not sufficient** for $\gamma=1$: $A=1$ removes directional dependence of $c$; $\gamma$ concerns the *partition of strain between $g_{00}$ and $g_{ij}$*, a distinct condition. $\gamma$ is a make-or-break for the solar-system regime, alongside the preferred-frame parameters of §6. **[OC framework; result open]**

---

## 5. The dynamics — linear elasticity is not the Einstein kinetic term

**5.1 — Fierz–Pauli potential, not Einstein–Hilbert kinetic.**
The substrate action is elastic:
$$S\propto\int dt\,d^3x\;\big[\rho(\partial_t u_i)^2-C_{ijkl}\,\partial_i u_j\,\partial_k u_l\big].$$
With $h_{ij}\sim\partial_{(i}u_{j)}$, the gradient energy $C(\partial u)^2\sim Ch^2$ is — in metric language — quadratic in $h$ with no derivatives: a **Fierz–Pauli mass/potential** structure, not the Einstein–Hilbert kinetic term $\sim(\partial h)^2$. The field equation is the elastic wave equation $\rho\ddot u_i=\partial_j(C_{ijkl}\partial_k u_l)$, **not** linearized Einstein $\Box\bar h_{\mu\nu}=-16\pi G\,T_{\mu\nu}$ (which is fully covariant with diffeomorphism gauge symmetry). The transverse mode does carry **two polarizations**, matching the graviton count — the kinematic count is right; the dynamical law differs. **[OC]**

**5.2 — The preferred frame fixes the theory class.**
A diffeomorphism-invariant theory has no preferred frame; the substrate has one (the lattice; infinite sound speed). So the emergent gravity carries the preferred frame as dynamical structure — it lives in the **Lorentz-violating gravity family (Einstein-aether / khronometric / Hořava)**. *Which* member is fixed by the substrate in §6. GR sits at the boundary of this family (preferred-frame couplings → 0). **[OC classification; IR adoption]**

**5.3 — Two routes that could promote it to genuine Einstein, both [RH].**
1. **Sakharov induced gravity** — integrating out substrate fluctuations on $g^{\text{eff}}$ generates an induced $\int\sqrt{-g}\,(\Lambda+\kappa R+\cdots)$ with $G_{\text{ind}}\sim\ell_P^2$; the SOSF $\ell_P$ floor is exactly the cutoff the mechanism needs. Not derived; sign and dominance of $\kappa$ uncomputed. **[RH]**
2. **Kleinert world-crystal** — defect proliferation converts the elastic $1/k^4$ metric propagator into Einstein's $1/k^2$. Whether the SOSF defect sector proliferates so is unknown. **[RH]**

These remain conjectures *about this substrate* until computed. But note: per §6 and the v0.2 reframe, reaching Einstein is **not required** for the theory to be viable — it is one option, not the success criterion.

---

## 6. The gravity class, identified — khronometric gravity from the infinite-sound-speed foliation

§5 placed the dynamics in the Lorentz-violating family. The substrate fixes *which* member, and the answer is sharper than a generic aether.

**6.1 — Infinite sound speed = a global preferred foliation = the khronon.** **[OC classification; IR identification]**
The locked infinite sound speed (I-§0) makes the longitudinal/pressure response *instantaneous and nonlocal* (II-§7): the Coulomb sector re-equilibrates everywhere at once. Instantaneous simultaneity across all space *is* a global time function — a preferred foliation of spacetime into constant-substrate-time slices. A dynamical preferred foliation defined by the gradient of a scalar time field is the **khronon** of khronometric gravity: the hypersurface-orthogonal limit of Einstein-aether theory, equivalently the low-energy limit of Hořava gravity. The substrate therefore gives not a *generic* aether (an arbitrary unit timelike vector) but the *hypersurface-orthogonal* one — **khronometric gravity specifically** — because infinite sound speed supplies a genuine global time.

**6.2 — The two projections are the two sectors.** **[IR]**
This lands the I-§7 two-projection structure directly onto the two sectors of khronometric gravity:

| Substrate projection (I-§7) | Sector | Character |
|:--|:--|:--|
| longitudinal / scalar / pressure $p$ (instantaneous Coulomb; II-§7) | the **khronon** (preferred foliation) | non-propagating, elliptic constraint |
| transverse / vector / vorticity $\boldsymbol\omega$ (finite $c$; III-§3) | the **spin-2 graviton** | propagating shear wave = light's sibling |

The split is not introduced to model gravity; it is the same split that defined the electrodynamics. The gravitational and electromagnetic structures share one architecture.

**6.3 — Structural win: survives GW170817.** **[OC/IR]**
The observation that eliminated most Einstein-aether / Hořava parameter space is GW170817: $|c_{\rm GW}/c_\gamma-1|\lesssim10^{-15}$. Here gravitational waves and light are *the same transverse shear sector* (§8; both ride $C_{66}$), so $c_{\rm GW}=c_\gamma$ is **structural, not tuned**. The framework automatically passes the constraint that is fatal to generic members of its own class. Genuine, if narrow — it does not imply the *other* constraints pass.

**6.4 — The make-or-break: preferred-frame PPN ($\alpha_1,\alpha_2$).** **[OC for the bounds; framework prediction open]**
The empirical content of any preferred-frame gravity lives in the PPN parameters $\alpha_1,\alpha_2$, which vanish identically in GR and are bounded extremely tightly:
$$\alpha_1\lesssim10^{-4}\ \text{(lunar laser ranging, orbital tests)},\qquad \alpha_2\lesssim10^{-7}\ \text{(solar-spin alignment, pulsars)}.$$
In this framework $\alpha_1,\alpha_2$ are set by the khronon–graviton coupling relative to the Einstein-Hilbert term. **GR is exactly the $\alpha_1,\alpha_2\to0$ limit.** So "divergence from Einstein" is not a vague shortfall — it is *two measured numbers* that the framework must predict small (naturally) or accept as tuned. This is the gravity-sector analog of the §4 PPN-$\gamma$ test and the III-§6 isotropy test: a concrete falsifiable handle. Per the v0.2 reframe, this **replaces** the framing in which "not-Einstein" was a ceiling; here it is the theory's testable signature.

**6.5 — The infinite sound speed may *tame* the usual khronon pathology — speculative.** **[RH]**
Khronometric / Hořava gravity's chief illness is the extra scalar (khronon) mode: strongly coupled, ghost-like, or gradient-unstable in much of parameter space. Here the khronon is the *longitudinal* sector, whose speed is *infinite* — it does not propagate as a wave; it is solved instantaneously as an elliptic constraint (the pressure/Coulomb equation), exactly like the Newtonian potential. A non-propagating constraint cannot be a ghost or carry a gradient instability in the usual sense. So the very feature that makes the substrate non-Lorentzian (infinite sound speed) is plausibly the feature that removes the standard scalar-mode pathology of this class. **Load-bearing caveat:** this is an argument, not a computation. Low-energy *strong coupling* (the genuine Hořava worry) is a separate disease from gradient instability and is **not** obviously cured by sending the scalar speed to infinity; only an explicit mode and strong-coupling-scale analysis settles it. Flagged [RH], not claimed.

**6.6 — What the framework now inherits.** **[OC]**
Adopting khronometric gravity means inheriting its open problems honestly: the strong-coupling question above; possible deviation of the cosmological $G_{\rm cosmo}$ from the Newtonian $G_N$ (BBN-bounded to $\sim10\%$); and the general theoretical contestation of Hořava-class theories. The reframe ("we are not aiming at GR") buys descriptive honesty but **not** freedom from constraint; it relocates the empirical risk from "$\gamma\neq1$" to "$\alpha_1,\alpha_2$, and the cosmological-$G$ ratio."

---

## 7. The stress-energy source — defects as curvature (locking the two gates)

The README's sub-question: *what plays the role of the stress-energy source?*

**The defect–elasticity dictionary** (Kleinert; Katanaev–Volovich): in an elastic continuum the geometry induced by the strain has its **curvature sourced by disclinations** and its **torsion sourced by dislocations**:
$$\text{disclination density}\leftrightarrow\text{curvature},\qquad \text{dislocation density}\leftrightarrow\text{torsion}. \quad\textbf{[OC]}$$

The fermion gate (III-§8, README §6B) identifies *matter* with exactly that defect sector. Therefore:

> **Matter curves the emergent space because, in the elastic-geometry dictionary, the defect density that *is* matter is the same object that *is* the curvature source.** The fermion gate supplies the $T_{\mu\nu}$ the gravity gate needs; the two gates are not independent. **[IR identification; RH for "this is GR's stress-energy"]**

The non-defect part of the source is the energy–momentum of the propagating excitations (the phonon/photon sector), feeding in through the anharmonic softening of $C_{66}$ (§3). So $T_{\mu\nu}^{\text{eff}}=T^{\text{excitations}}_{\mu\nu}+T^{\text{defects}}_{\mu\nu}$, the second being matter proper. **[IR]**

Tiering: the dictionary is [OC], the defect↔GR-source identification is [IR], and "the resulting field equation is Einstein's" is [RH] — and in the khronometric reading (§6) the field equation is explicitly *not* Einstein's but its preferred-frame generalisation.

---

## 8. Consistency threads with Blocks I–III

- **Isotropy carries over (necessary condition).** The $\beta=\alpha$ ($A=1$) condition isotropizing light (III-§6) is necessary for the gravitational sector too — but, per §4, not sufficient for $\gamma=1$. **[OC/IR]**
- **Gravitational waves = light's sibling.** Both are excitations of the *same* transverse shear sector, so $c_{\rm GW}=c_\gamma=\sqrt{C_{66}/\rho}$ structurally — the GW170817 win of §6.3. A post-diction, not a fit. **[IR]**
- **Planck-modified gravity in the UV.** The $(k\ell_P)^2$ dispersion (III-§5) applies to gravitational shear excitations: emergent gravity is Lorentz-violating at the Planck scale (high-frequency GW dispersion), consistent with the khronometric classification. **[IR]**
- **Longitudinal sector untouched.** Gravity here is *transverse*; the instantaneous longitudinal/Coulomb sector (II-§7) is the khronon (§6.2). Whether the instantaneous longitudinal response and the finite-$c$ transverse metric stay mutually consistent in strong fields is open (§10). **[OC/IR]**

---

## 9. Verdict (reframed)

GR is a falsifiable theory, not the benchmark the framework must hit. Measured against the actual question — *what gravity does the substrate predict, and where could it be killed?* — the placement is:

| Property | Result | Tier |
|:--|:--|:--|
| Kinematic curved metric for light (analog gravity) | **Yes**, robustly | [OC] |
| Newtonian / Poisson static limit | **Yes**, generic to 3-D elasticity | [OC/IR] |
| Light bending (richer than Nordström) | **Yes** ($c$ varies directly) | [OC] |
| Identified theory class | **Khronometric gravity** (hypersurface-orthogonal aether / low-energy Hořava), forced by infinite-sound-speed foliation | [OC/IR] |
| $c_{\rm GW}=c_\gamma$ (GW170817) | **Passes structurally** — survives the constraint fatal to its class | [OC/IR] |
| Built-in matter→curvature source | **Yes**, via defect–elasticity (ties to fermion gate) | [IR/RH] |
| Empirical content / falsification handles | PPN $\gamma$ (§4); preferred-frame $\alpha_1,\alpha_2$ (§6.4); cosmological $G$ ratio | [OC framework; results open] |
| Relation to GR | GR = the $\alpha_1,\alpha_2\to0$ IR limit; the framework predicts *distinct*, bounded preferred-frame effects | [OC/IR] |
| Full nonlinear diffeomorphism-invariant Einstein dynamics | **Not derived, and not required** — one option (§5.3), not the success criterion | [OC/RH] |
| Khronon scalar-mode health | Plausibly tamed by infinite sound speed (non-propagating constraint); strong coupling **un-analysed** | [RH] |

**Bottom line.** The gravity gate yields a *specific, identifiable, falsifiable gravity*: **khronometric (preferred-frame) gravity with a Newtonian core, genuine light bending, $c_{\rm GW}=c_\gamma$ built in, and a matter source made of the lattice's own defects.** It is neither Nordström (light bends) nor GR (a preferred frame is present and dynamical). GR is recovered as the limit in which the preferred-frame couplings vanish. The framework's *divergence* from Einstein is its *empirical content* — concentrated in $\alpha_1,\alpha_2$ and the cosmological-$G$ ratio, all already tightly bounded, so the next task is to compute those numbers and show they can be small (or pin down where the theory is killed). Honesty cuts both ways: not-GR is not a failure, but the not-GR parameters are exactly where the danger lives.

---

## 10. Open forks / to-derive next

1. **Preferred-frame PPN $\alpha_1,\alpha_2$ — the make-or-break (§6.4).** Write the emergent action in khronometric form, express the couplings in terms of the elastic constants ($\alpha,\beta,C_{66},\rho$), and compute $\alpha_1,\alpha_2$. Do they come out below $10^{-4}$, $10^{-7}$ naturally, or only by tuning? **The decisive next calculation.**
2. **Khronon strong-coupling / mode health (§6.5).** Explicit mode analysis: is the non-propagating (infinite-speed) khronon free of low-energy strong coupling, or does the standard Hořava disease survive? Settles whether §6.5's taming is real.
3. **PPN $\gamma$ (§4).** Compute the spatial-metric response; does $\beta=\alpha$-isotropized elasticity give $\gamma=1$ to the Cassini bound, or a measurable deviation?
4. **Sign of the energy→softening coupling (§3).** Does excitation energy soften or stiffen $C_{66}$? Only softening gives attractive gravity; fixes $G_{\text{eff}}$.
5. **Cosmological $G$ vs Newtonian $G$.** Compute the khronometric $G_{\rm cosmo}/G_N$ and confront BBN.
6. **Sakharov / Kleinert promotion [RH] (§5.3).** Whether an induced Einstein–Hilbert term or defect proliferation pushes the theory toward GR — now an *option to explore*, not a target.
7. **Strong-field consistency (§8).** Instantaneous longitudinal sector vs finite-$c$ transverse metric beyond weak field; horizon formation.
8. **Fermion gate (README §6B).** Strongly motivated by §7: derive the defect spectrum, test spin-½ / spin-statistics, feed back as $T^{\text{defects}}_{\mu\nu}$ for items 1, 5, 6.

---

## Appendix — symbols & core relations

### Symbols

| Symbol | Meaning |
|:--|:--|
| $C_{66}$, $c=\sqrt{C_{66}/\rho}$ | transverse shear modulus / emergent light (and GW) speed (III) |
| $s=\delta C_{66}/C_{66}^{0}$ | dimensionless lattice-softening field |
| $\Phi=\tfrac12 c_0^2 s$ | emergent Newtonian potential |
| $g^{\text{eff}}_{\mu\nu}$ | effective (acoustic/elastic) metric felt by the transverse mode |
| $G_{\text{eff}}$, $G_{\rm cosmo}$ | emergent Newton constant / its cosmological counterpart (need not be equal — §6.6) |
| $\gamma$ | PPN light-bending parameter; $\gamma=1$ ⟺ GR |
| $\alpha_1,\alpha_2$ | PPN **preferred-frame** parameters; $=0$ in GR; the framework's empirical content (§6.4) |
| khronon | scalar defining the preferred foliation = the substrate's instantaneous simultaneity surfaces (= longitudinal/pressure sector) |
| $\alpha,\beta$ | radial / line-tension elastic stiffnesses; isotropy at $\beta=\alpha$ (III-§6) |
| $T^{\text{defects}}_{\mu\nu}$ | stress-energy from defects = fermion-gate matter = curvature source (§7) |
| $\ell_P$ | Planck-scale lattice cutoff; sets Sakharov $G_{\rm ind}$ and UV Lorentz violation |

### Core relations

$$ds^2_{\text{eff}}=-c(\mathbf{x})^2dt^2+d\mathbf{x}^2,\qquad c(\mathbf{x})=\sqrt{C_{66}(\mathbf{x})/\rho}\qquad\text{(kinematic analog metric)}$$

$$\Phi=\tfrac12 c_0^2\,\frac{\delta C_{66}}{C_{66}^0},\qquad \nabla^2\Phi=4\pi G_{\text{eff}}\,\rho_{\text{source}}\qquad\text{(Newtonian/Poisson limit)}$$

$$\text{infinite sound speed}\ \Rightarrow\ \text{global foliation}\ \Rightarrow\ \text{khronon}\ \Rightarrow\ \textbf{khronometric gravity}\quad(\text{not generic aether})$$

$$\{p,\ \text{instantaneous}\}\ \leftrightarrow\ \text{khronon (constraint)};\qquad \{\boldsymbol\omega,\ \text{finite }c\}\ \leftrightarrow\ \text{spin-2 graviton}\quad\text{(two projections = two sectors)}$$

$$c_{\rm GW}=c_\gamma=\sqrt{C_{66}/\rho}\ \Rightarrow\ \text{passes GW170817 structurally}$$

$$\alpha_1,\alpha_2\ \text{(preferred-frame PPN)} \ \xrightarrow{\ \to 0\ }\ \text{GR};\qquad \text{measured: }\alpha_1\lesssim10^{-4},\ \alpha_2\lesssim10^{-7}\quad(\textbf{make-or-break})$$

$$\text{disclination density}\leftrightarrow\text{curvature},\quad \text{dislocation density}\leftrightarrow\text{torsion}\quad\text{(defect source; §7)}$$

---

*Document status: [exploratory; internally consistent; tiers honest]. Block IV v0.2 identifies the emergent gravity as **khronometric (preferred-frame) gravity**, forced by the substrate's infinite-sound-speed foliation; passes GW170817 structurally; GR is its $\alpha_1,\alpha_2\to0$ limit. The empirical content — and the decisive next calculation — is the preferred-frame PPN pair $\alpha_1,\alpha_2$. The fermion gate is the natural partner: its defects are the curvature source.*
