# DCCREG Fluid Substrate — Foundations & First Dynamics

**Version:** 0.4 (Foundations + First Dynamics block)

**Scope of this document:** the static substrate, its field machinery, and the first dynamical law (the inter-level cascade). It stops deliberately *before* specific solutions and before the higher-scale MHD emergence (#5), which open new scope.

---

## Revision history

| Version | Date | Author | Summary of changes |
|:------------|:--------------|:--------------------|:------------------------------------------------|
| 0.1 | 2026-05-29 | DCCREG Modeling Programme | Initial release — Foundations + First Dynamics block (Sections 0–12 and Appendix). Covers the locked working assumptions, the ideal-incompressible-Euler constitutive class, the two electromagnetic mechanisms, primordial chirality, the SOSF scaffold and space-covering matrix, the fixed-skeleton / dynamic-pressure factorization, the one-field / two-projection machinery, and Dynamics I–III culminating in the inter-level transfer (cascade) law. Stops before specific solutions and the higher-scale MHD emergence. |
| 0.2 | 2026-05-29 | DCCREG Modeling Programme | **Screw-angle correction.** The full-circle golden angle $137.5^\circ$ is rejected and replaced by the $C_3$-sector golden angle $120^\circ/\varphi^2 \approx 45.8^\circ$. Reason: the substrate's discrete $C_3$ symmetry ($120^\circ$ about $[1,1,1]$) means only $\theta \bmod 120^\circ$ acts physically, and $137.5^\circ \bmod 120^\circ = 17.5^\circ = \tfrac{7}{48}$ of the period — rational, so the structure *closes* after 48 steps (verified: the $137.5^\circ$ and $17.5^\circ$ sphere-flakes are identical point sets), defeating the never-settles criterion. The sector angle has residue $1/\varphi^2$ (irrational; Fibonacci convergent $21/55$) and never closes. Updated §4 (new folding correction + Fibonacci note), §10 (helicity coupling), §12 item 4 (fork now resolved), and the Appendix symbol table. Discovered via the substrate simulator. |
| 0.3 | 2026-05-29 | DCCREG Modeling Programme | **Pedagogical addition to §4.** Added the explanatory block "Where $45.8^\circ$ comes from — the golden angle and the sector," covering (i) the golden angle as the golden-ratio cut $1/\varphi^2$ of *any* period, (ii) why the relevant period is the $120^\circ$ $C_3$ sector rather than the full $360^\circ$ circle, and (iii) the 3-fold-clock analogy. No change to results; clarifies the philosophy behind the v0.2 correction. |
| 0.4 | 2026-05-29 | DCCREG Modeling Programme | **Node dynamics + dimension correction (major).** Derived the node allocation law, the shared-node combination rule, and the field-interference frame; and corrected the fractal dimension. (1) **Node law** (new §12): from Kirchhoff (C1), energy flux (C2) and the screw (C3), the central child carries the full axial circulation $\Gamma_c=\Gamma_n$ (conserved spine), the six outer children carry $\Gamma_o=\tfrac12\Gamma_n$ (lateral cascade), swirl sense set by the screw. (2) **Shared-node rule + dual necessity** (new §13): co-rotating neighbours cancel at a shared node, counter-rotating reinforce — so the dual counter-rotating structure is *required* for any lateral cascade. (3) **Dimension correction:** accounting for outer-child sharing, the *matrix* has 4 distinct cells per level (not 7), so $D=\log_2 4 = 2.0$ (the $2.807$ was the single-tree limit-set value, which double-counts shared cells). This propagates: $u_n=$const, $\Gamma$ halves, $\omega$ doubles per level; spectrum steepens to $E(k)\propto k^{-2}$ (Burgers/shock-like). (4) **Field frame** (new §14): pressure (handedness-blind) is a smooth all-reinforcing Coulomb landscape; helicity (sign-carrying) forms a standing checkerboard whose 2-D cancellation faces coincide with the $D=2$ active set, the $k^{-2}$ shock fronts, and the local-handedness cell boundaries. Updated §4, §10, §11, §12(→§15 open forks), and the Appendix. Old §12 (open forks) renumbered to §15. Dimension finding discovered via the substrate simulator's shared-node analysis. |

---

## Epistemic tagging legend

Every substantive claim below carries one of three tags:

- **[OC] Operational Core** — standard, derivable physics or mathematics; true independent of the framework.
- **[IR] Interpretive Reading** — a modeling identification made *within* the framework; internally consistent, chosen rather than forced.
- **[RH] Resonance / Heuristic** — analogical or cosmological reading; suggestive, not load-bearing.

---

## 0. Working assumptions (locked)

1. **Sub-Planck substrate.** The discrete constituent scale (mean-free-path floor) is the Planck length, $\ell_P \approx 1.616\times10^{-35}\ \mathrm{m}$. The continuum "fluid" description is valid for length scales $L \gg \ell_P$ (Knudsen number $\mathrm{Kn} = \ell_P/L \to 1$ only as the floor is approached). **[IR]**
2. **Lossless.** No viscosity, no resistivity, no dissipation of any kind (ideal Euler / ideal MHD). **[locked input]**
3. **Incompressible.** $\nabla\cdot\mathbf{u} = 0$; density $\rho = \text{constant}$. **[locked input]**
4. **Infinite sound speed.** Pressure transmission is instantaneous and nonlocal. Human-scale perceptual/cognitive limits are *not* to be imposed as constraints anywhere in the derivation. **[locked input]**
5. **Plasma-like under rotative agitation; magnetohydrodynamic mixture at higher scale.** **[locked input]**

---

## 1. Constitutive class

Assumptions 2 + 3 fix the system to the **ideal incompressible Euler fluid** — the most rigid and most theorem-rich corner of fluid mechanics. **[OC]**

Consequences carried for free:

- Circulation is conserved (Kelvin's theorem). **[OC]**
- Vortex lines are frozen-in (Helmholtz). **[OC]**
- Kinetic **helicity** $H = \int \mathbf{u}\cdot\boldsymbol{\omega}\,dV$ is an *exact* conserved invariant. **[OC]**

> **Key principle (flagged for reuse across MHD phenomena):**
> $H$ is a conserved **pseudoscalar** — it flips sign under mirror reflection. Mirror/dual nature is therefore *inherent* to the conserved chirality, not added on top. At the MHD level this generalizes to magnetic helicity $\int \mathbf{A}\cdot\mathbf{B}$ and cross-helicity $\int \mathbf{u}\cdot\mathbf{B}$, both conserved in ideal MHD. **[OC]**

---

## 2. The two electromagnetic mechanisms

The "seemingly electrostatic nature under rotation" has two rigorous origins, used together. We do **not** invoke literal charge separation. **[IR for the identification; OC for the underlying theorems]**

### Mechanism A — pressure is the electrostatic potential

In incompressible flow, pressure is a Lagrange multiplier enforcing $\nabla\cdot\mathbf{u} = 0$, determined instantaneously by a Poisson equation:

$$\nabla^2 p = \rho\left(\tfrac{1}{2}\lvert\boldsymbol{\omega}\rvert^2 - \lvert S\rvert^2\right)$$

($\boldsymbol{\omega}$ = vorticity, $S$ = strain-rate tensor). This is structurally identical to electrostatics, $\nabla^2\Phi = -\rho_{\text{charge}}/\varepsilon_0$. The source is the **local excess of rotation over strain**. Define the **effective charge density**:

$$\rho_{\text{eff}} \equiv \rho\left(\tfrac{1}{2}\lvert\boldsymbol{\omega}\rvert^2 - \lvert S\rvert^2\right) = 2\rho Q \qquad (Q = \text{the } Q\text{-criterion})$$

Rotation-dominated regions (vortex cores) are the charge concentrations. **[OC]**

### Mechanism B — rotation manufactures effective EM (Larmor's theorem)

In a frame rotating at $\boldsymbol{\Omega}$, the inertial forces split cleanly:

- Coriolis $-2m\,\boldsymbol{\Omega}\times\mathbf{v}$ has the form of the magnetic Lorentz force ($q\mathbf{B} \leftrightarrow -2m\boldsymbol{\Omega}$) → the *magnetic-like* part. **[OC]**
- Centrifugal is the gradient of a scalar potential $-\nabla\!\left(\tfrac{1}{2}m\Omega^2 r^2\right)$: curl-free, radial → the *electrostatic-like* part. **[OC]**

Threshold for "sufficiently agitated": the effective magnetization (Hall-type) parameter built from $\boldsymbol{\Omega}$ exceeds unity. **[OC]**

---

## 3. Chirality is primordial (cannot be dynamically generated)

For ideal incompressible flow with conservative forces, vorticity obeys

$$\frac{D\boldsymbol{\omega}}{Dt} = (\boldsymbol{\omega}\cdot\nabla)\mathbf{u}$$

Every term contains $\boldsymbol{\omega}$: **if $\boldsymbol{\omega} = 0$ it stays $0$.** Rotation cannot bootstrap from an irrotational state. The usual vorticity sources are all closed off by the locked assumptions: baroclinic generation dies (incompressible $\Rightarrow \nabla\rho = 0$); viscous boundary generation dies (lossless). Therefore handedness must be **primordial — built into the substrate (the packing) as initial/structural data.** Losslessness then conserves it exactly via $H$. **[OC]**

---

## 4. The scaffold — Septenary Octahedral Sphere-Flake (SOSF)

**Geometry.** A permanent, immutable fractal hierarchy of nested spheres. Each parent (radius $R$) contains seven children (radius $R/2$): six on the $\pm x, \pm y, \pm z$ axes at distance $R/2$ (each tangent to the parent wall and passing through the parent centre), plus one central child at the parent centre. The six outer centres form a regular octahedron; the central centre is its body-centre. **[IR — the chosen substrate]**

**Classification.** This is *not* classical packing (the children overlap). It is a **self-similar covering generated by an iterated function system** (seven $\tfrac{1}{2}$-contractions). Working name: *septenary octahedral sphere-flake*. **[OC]**

- Similarity dimension of the **single-tree** limit set: $D_{\text{tree}} = \dfrac{\log 7}{\log 2} \approx 2.807$ (upper bound on Hausdorff dimension; overlap lowers it). **[OC]**
- **Matrix dimension (operative — v0.4 correction):** in the space-covering matrix the six outer children are each *shared* by two cells, so the number of *distinct* cells per parent is $1 + 6\times\tfrac12 = 4$, not $7$. The physically relevant fractal dimension of the medium is therefore $D = \log_2 4 = \mathbf{2.0}$ exactly. Geometrically the children occupy the lattice points and edge-midpoints of the refined grid but skip every face- and body-centre — exactly half the fine lattice — so the active set is genuinely porous and sheet-like. $D_{\text{tree}} = 2.807$ double-counts shared spheres; the cascade and spectrum ride on the matrix value $D = 2$. See §13. **[OC for the count; IR for "matrix value governs the cascade"]**
- Nearest named relatives: Apollonian packing (tangent cousin), octahedron flake / Sierpiński octahedron (no central cell). Distinguished here by the body-centred seventh cell. **[OC]**

**Chirality injection — the screw.** The bare octahedral motif has full $O_h$ symmetry (contains mirrors + inversion) → achiral → would force $H = 0$. To break mirror symmetry, the recursion **rotates as it descends**: each generation is placed in a frame rotated by a fixed angle about the $[1,1,1]$ body diagonal before the $\tfrac{1}{2}$ scaling. A screw is the prototypical chiral element; this converts the achiral covering into a chiral one. **[OC for the symmetry argument; IR for the construction]**

Why $[1,1,1]$:

- It is a genuine 3-fold ($C_3$) axis of the octahedron. **[OC]**
- Viewed along it, the six outer centres project to a regular hexagon — the same projection that yields the Star-of-Solomon hexagram. The twist axis and the hexagram axis coincide. **[IR]**
- The two screw senses ($\pm\theta$) are the two signs of the conserved pseudoscalar $H$. The dual counter-rotating pair = the two enantiomorphic screw-fractals; a mirror swaps them and flips $\operatorname{sign}(H)$. **[IR]**

**Screw angle — selected, not chosen.** The correct value is the **$C_3$-sector golden angle**:

$$\theta \;=\; \frac{120^\circ}{\varphi^2} \;\approx\; 45.8^\circ, \qquad \varphi = \tfrac{1+\sqrt{5}}{2}.$$

- *Sign* of the screw ↔ nature's fundamental (parity-violation-type) chirality: a binary, already settled. **[IR/RH]**
- *Magnitude* ↔ nature's morphological chirality. The relevant quantity is the "most irrational" angle, which avoids resonance/closing. This is selected by the locked **never-settles** requirement, and is the same optimality principle phyllotaxis uses. **[OC for the irrationality optimality; IR for the selection]**
- Decision-matrix verdict: a golden-ratio angle wins robustly across criteria; the only criterion favouring $60^\circ$ (hexagram self-consistency) is overridden by the higher-weighted never-settles criterion. **[IR]**

**Correction (v0.2) — the angle must be taken modulo the substrate's symmetry, not over the full circle.** The screw acts on a substrate with discrete $C_3$ symmetry about $[1,1,1]$ (period $120^\circ$), so only the residue $\theta \bmod 120^\circ$ has physical effect. The full-circle golden angle therefore **fails**: **[OC]**

$$137.5^\circ \bmod 120^\circ = 17.5^\circ = \tfrac{7}{48}\times 120^\circ \quad\text{(a rational fraction — closes after 48 steps).}$$

This was verified directly: the sphere-flake built with $137.5^\circ$ and the one built with $17.5^\circ$ are the **identical point set**. The substrate's own symmetry folds the full-circle golden angle into a resonant, *settling* rotation — destroying the one property (never-settling irrationality) for which it was selected. The correct angle is the golden section of the $120^\circ$ period itself, $120^\circ/\varphi^2 \approx 45.8^\circ$, whose residue is $1/\varphi^2 \approx 0.382$ of the period — irrational, so it **never closes**. (The full-circle $137.5^\circ$ is the right answer only for a continuous, symmetry-free substrate.) This **resolves** the former open fork in favour of the sector angle — forced by the discrete symmetry, not chosen. **[OC for the folding; IR for adopting it]**

**Where $45.8^\circ$ comes from — the golden angle and the "sector."** Two ideas combine in this number; separating them makes the choice transparent.

*The golden angle is the golden-ratio cut of a period.* Take any full period, divide it in the golden ratio $\varphi$, and keep the smaller piece — that fraction is $1/\varphi^2 \approx 0.382$. For a full $360^\circ$ turn this gives the familiar golden angle $360^\circ/\varphi^2 \approx 137.5^\circ$. The reason this particular fraction is special is that $\varphi$ is the "most irrational" number: stepped repeatedly, $1/\varphi^2$ of a period takes the longest possible time to return near its starting point — which is exactly the never-settles property. So the golden angle is "the golden fraction of *whatever the period is*."

*The period here is $120^\circ$, not $360^\circ$.* The octahedron carries a 3-fold ($C_3$) symmetry axis along $[1,1,1]$: rotating the whole structure by $120^\circ$ about that axis maps it exactly onto itself (the $x,y,z$ arms cycle into one another and nothing is distinguishable). A $120^\circ$ rotation is therefore physically *nothing happened* — and so is $240^\circ$. The full circle is carved into **three identical $120^\circ$ wedges**, and only one's position *within* a wedge carries information; rotation matters only modulo $120^\circ$. That single wedge is the **"sector."**

Asking for the golden angle on the *real* period (the $120^\circ$ sector) rather than the full circle gives, by the same recipe:

$$120^\circ \times \frac{1}{\varphi^2} \approx 45.8^\circ.$$

*Clock analogy.* A normal clock face spans $360^\circ$ (12 hours). Now imagine a clock whose 12-, 4-, and 8-o'clock positions are physically indistinguishable — a "3-fold clock." Only the first four-hour wedge is real; everything past it is a repeat. The golden angle for that clock is not $360^\circ/\varphi^2$ but (one wedge)$/\varphi^2$. The substrate *is* that 3-fold clock, and its wedge is $120^\circ$ — hence $45.8^\circ$, not $137.5^\circ$. **[OC]**

> **Fibonacci convergence:** the golden structure already encodes all four letters of DCCREG — self-similar ($\varphi = 1 + 1/\varphi$), chiral, and *dual counter-rotating* (two opposite-handed parastichy families whose arm-counts are consecutive Fibonacci numbers). The corrected angle confirms this on the substrate: the best rational approximation of $\theta/120^\circ = 1/\varphi^2$ within small denominators is $\tfrac{21}{55}$ — a ratio of consecutive Fibonacci numbers, the signature of the genuine golden quantity. The angle selected by the dynamics is the same angle that natively generates the framework's defining geometry. **[IR/RH]**

---

## 5. The space-covering matrix

A single SOSF leaves diagonal gaps inside its parent. The **matrix** of SOSF elements closes them as a **covering** (not a packing): with elements on a cubic lattice of **spacing = radius**, axis-children coincide (the "shared spheres"), and the cubic deep-hole distance $\sqrt{3}\,r/2 \approx 0.866\,r < r$ guarantees every point is covered. Overlap is the mechanism, not a defect. **[OC]**

- Reconciliation — three distinct measures, not a contradiction: (i) the *single-tree limit set* (measure-zero dust) has $D_{\text{tree}}=2.807$; (ii) the *union of solid sphere bodies* fills 3-D space (a covering, by volume); (iii) the *network of distinct active cells* — what the cascade rides on — has counting dimension $D=2.0$ (§4, §13). Different objects, different numbers; the cascade and spectrum use (iii). **[OC]**
- **Decision:** all levels present (parents persist), so coverage is rigorous and the vortex skeleton threads every scale. **[IR]**
- The **shared spheres are the junction nodes** where adjacent filaments link → connected network → nonzero mutual linking → helicity has a substrate. Sharing does physics work, not just geometry. **[IR]**

---

## 6. The factorization — fixed chiral skeleton + dynamic pressure

**Agreed reformulation:** the chiral SOSF skeleton is fixed and immutable. What is perceived as motion is the instantaneous reconfiguration of the pressure-gradient pattern over the stationary lattice — **no substrate transport**. Velocity is the *derived signature* of the pattern, not transported matter. **[IR]**

Two refinements that make this rigorous:

1. "Nothing moves" $\neq \mathbf{u} \equiv 0$ (that would give $\nabla p = 0$, no gradients to displace). It means no *substrate/material* transport; the pattern propagates. **[OC]**
2. **Pressure is mirror-blind, so chirality must live in the skeleton.** Pressure is a true scalar built from $\lvert\boldsymbol{\omega}\rvert^2$ (even under $\boldsymbol{\omega} \to$ mirror); it cannot encode the pseudoscalar handedness. Velocity is built linearly from $\boldsymbol{\omega}$ and carries the sign. The factorization is therefore *forced by projection parity*, not merely asserted. **[OC]**

---

## 7. Field machinery — one master field, two projections

The only fundamental field is $\boldsymbol{\omega}$, carried on the fixed skeleton. Everything perceivable is one of two instantaneous readouts, both through the **same $1/r$ (Coulomb / Laplacian) Green's function**:

$$\underbrace{\mathbf{u} = \nabla\times\mathbf{A}, \qquad \mathbf{A} = \frac{1}{4\pi}\int \frac{\boldsymbol{\omega}(\mathbf{x}')}{\lvert\mathbf{x}-\mathbf{x}'\rvert}\,d^3x'}_{\text{Velocity (vector, LINEAR in }\boldsymbol{\omega}\text{) — Biot–Savart}}$$

$$\underbrace{p = -\frac{\rho}{4\pi}\int \frac{\tfrac{1}{2}\lvert\boldsymbol{\omega}\rvert^2 - \lvert S\rvert^2}{\lvert\mathbf{x}-\mathbf{x}'\rvert}(\mathbf{x}')\,d^3x'}_{\text{Pressure (scalar, QUADRATIC in }\boldsymbol{\omega}\text{) — Poisson}}$$

- The *linear* projection carries handedness (sign of $\boldsymbol{\omega}$); the *quadratic* projection is sign-blind. This is the §6 chirality result, derived. **[OC]**
- The instantaneous $1/r$ kernel is simultaneously the spatial Coulomb form (electrostatics) and, with $c_{\text{sound}} = \infty$, the zero-delay temporal response (the "high-voltage-capacitor-over-1 ns" perceived-power spike: finite energy, perceived power set by the observer's time-binning against a zero-delay kernel). **[OC for the kernel; RH for the capacitor reading]**

---

## 8. Dynamics I — sequence of instantaneous equilibria

Because $c_{\text{sound}} = \infty$, pressure never carries its own time derivative; at every instant it is the current Coulomb equilibrium of the current $\boldsymbol{\omega}$. The time-loop:

$$\text{circulation } \Gamma \text{ on skeleton} \to \boldsymbol{\omega} \to (\mathbf{u},\,p) \text{ by the two projections} \to \nabla p \text{ force pattern} \to \text{node redistribution} \to \text{repeat}$$

Time enters **only** through node redistribution; the external driver is the rotative-stress agitation. "Displaced pressure gradients" = redistribute $\Gamma$ at the nodes, and the whole pressure field re-equilibrates everywhere at once. **[IR built on OC]**

---

## 9. Dynamics II — vortex stretching as cross-recursion transfer

**What vortex stretching is:** circulation $\Gamma = \oint \mathbf{u}\cdot d\mathbf{l}$ is conserved (Kelvin); when geometry concentrates it (smaller area), vorticity $\omega \approx \Gamma/A$ intensifies. The figure-skater / tornado effect. **[OC]**

**In the fixed skeleton:** geometric thinning is unavailable (filaments don't move). The only channel for concentration is to **hand circulation down the recursion** to the pre-existing finer child filaments. Concentration-by-thinning → concentration-by-descent. **[IR]**

**Natural grounding:** the turbulent energy cascade (Richardson / Kolmogorov) — vortex stretching cascading energy to ever-smaller, self-similar (fractal) scales — is exactly this. The SOSF recursion supplies the scale ladder the cascade already wants. MHD twin: the stretch-twist-fold solar dynamo. **[OC]**

**"Amplitude" defined, and the area-vs-recursion question:** amplitude = circulation $\Gamma$. The two intuitions are the two directions of the cascade:

- *Across recursions* (to finer children) = forward / down-cascade = concentration = vortex stretching proper. **[OC/IR]**
- *Over a larger area* (to coarser, wider region) = inverse / up-cascade = de-concentration. **[OC/IR]**

In pressure terms: down-cascade sharpens $\rho_{\text{eff}}$ into point-like intense charges at fine recursions; up-cascade smears them over area at lower peak. Same process, two languages. **[OC/IR]**

---

## 10. Dynamics III — the inter-level transfer law (the cascade)

**Two node conservation conditions:**

1. **Circulation Kirchhoff law:** $\nabla\cdot\boldsymbol{\omega} = 0 \Rightarrow$ signed circulation is conserved at each junction. **[OC]**
2. **Constant energy flux (lossless steady cascade):**

$$\varepsilon = \frac{\rho\, u_n^3\, p_n}{\ell_n} = \text{constant} \qquad (\text{independent of level } n)$$

where $u_n,\ \ell_n,\ p_n$ are the velocity scale, length scale, and active space-fraction at level $n$. This *is* the transfer law. **[OC]**

**Fractal ($\beta$-model) correction — the geometry's fingerprint.** Space-filling cascades branch 8-fold per octave; the SOSF *matrix*, after accounting for shared outer children (§13), has **4** distinct cells per level, so the active fraction shrinks by $\beta = 4/8 = 1/2$ per step on a fractal of dimension $D = \log_2 4 = 2.0$ (the turbulence $\beta$-model, with $\beta$ set by the flake). Feeding $p_n = (1/2)^n$ and $\ell_n = \ell_0\cdot 2^{-n}$ into the constant-flux law gives clean factors of two:

$$\frac{u_{n+1}}{u_n} = 1 \qquad (\text{velocity scale-independent})$$

$$\frac{\Gamma_{n+1}}{\Gamma_n} = \frac{1}{2} \qquad (\text{circulation halves per level})$$

$$\frac{\omega_{n+1}}{\omega_n} = 2 \qquad (\text{vorticity doubles — stretching, quantified})$$

> *History (v0.1–0.3):* before the shared-cell correction these read $u$-ratio $(4/7)^{1/3}\approx0.830$, $\Gamma$-ratio $\approx0.415$, $\omega$-ratio $\approx1.661$, from the overcounted $\beta=7/8$, $D=2.807$. The clean halves/doublings above supersede them.

**Distinguishing prediction — energy spectrum:**

$$E(k) \propto k^{-\frac{5}{3} - \frac{3-D}{3}} = k^{-\frac{8-D}{3}} = k^{-2} \qquad (D=2)$$

Markedly steeper than Kolmogorov's $-5/3$ (recovered only in the space-filling limit $D=3$). A $k^{-2}$ spectrum together with scale-independent velocity is the signature of a **shock/front-dominated (Burgers-like)** field — consistent with the sheet-like $D=2$ active set. The geometry is readable off the spectrum. **[OC for the math; IR for $\beta=1/2$; RH for the Burgers reading]**

**Golden-screw helicity coupling.** The cascade above sets magnitudes only. The $C_3$-sector golden-angle screw ($\approx 45.8^\circ$ per level about $[1,1,1]$; see §4 correction) adds an orientation increment per level; via $h = \mathbf{u}\cdot\boldsymbol{\omega} = \lvert\mathbf{u}\rvert\lvert\boldsymbol{\omega}\rvert\cos\theta$ it fixes the *sign* of the helicity contributed at each step. Because its residue mod the substrate's $120^\circ$ symmetry is irrational ($1/\varphi^2$), no two levels ever co-align into a closing resonance → definite conserved net helicity sign + permanent non-settling. **The transfer law sets *how much*; the screw sets *which hand*; the (substrate-relative) golden angle guarantees it *never locks up*.** **[OC + IR]**

---

## 11. Standing balance & regularization (consequences)

- **Never-settles, derived.** A lossless cascade has no dissipative sink and (with the Planck floor) cannot descend below $\ell_P$ → the down-cascade must reflect → down + up coexist as a permanent standing cascade. The dual counter-rotating structure carries the two directions. This *derives* the previously-assumed "infinite superposition of constructive and negative-constructive behaviour." **[OC/IR]**
- **Blow-up regularized.** Classical 3-D Euler can blow up (stretching thins tubes toward zero area, $\omega \to \infty$). Here there is no geometric thinning, and the recursion is finite (bounded number of levels to $\ell_P$), so maximum attainable vorticity is capped. The immutable geometry + Planck floor is what makes the dynamics finite where ordinary Euler is not. Made explicit in §12; rigorous proof still open (§15). **[IR built on OC]**

---

## 12. Dynamics IV — the node allocation law

The cascade law (§10) is *aggregate*: it gives per-level ratios but not how circulation splits among the seven children at one node. Octahedral symmetry reduces the seven unknowns to two — $\Gamma_c$ (central child) and $\Gamma_o$ (each outer child, equal by symmetry). Three constraints fix them:

**C1 — Kirchhoff (axial through-flux).** Project the children's filament tangents onto the cascade axis $\hat{n}=[1,1,1]/\sqrt3$. The $\pm x,\pm y,\pm z$ outer children form opposite pairs whose projections cancel exactly, so the six outer children contribute **zero** net flux along $[1,1,1]$. Since $[1,1,1]$ is the screw's invariant axis, the central child runs straight down it and carries the entire axial flux:

$$\boxed{\;\Gamma_c = \Gamma_n\;}\qquad(\text{conserved axial spine}). \quad\textbf{[OC]}$$

**C2 — energy flux fixes the outer children.** With the spine pinned, the cascade's circulation loss (§10, now $\Gamma_{n+1}/\Gamma_n = \tfrac12$) has nowhere to live but the outer children:

$$\boxed{\;\Gamma_o = \tfrac{1}{2}\,\Gamma_n\;}\qquad(\text{each of six, lateral}). \quad\textbf{[OC]}$$

Consistency: outer-child vorticity scales as $\omega_o \propto \Gamma_o/\ell^2 \to \tfrac12\times 4 = 2$ per level — exactly the §10 vortex-stretching ratio. The law reproduces the aggregate. ✓

**C3 — the screw fixes the sign, not the size.** The $45.8^\circ$ twist sets the *swirl sense* of the six outer children around the spine (a coherent azimuthal circulation of definite handedness), and its irrationality (mod $120^\circ$) keeps that swirl from ever closing. C3 contributes handedness and non-settling, not magnitude. **[OC + IR]**

**Determinacy & well-posedness.** Two constraints (C1, C2) fix two unknowns — no free parameter; the standing-cascade backstop is not needed. The spine circulation is constant ($=\Gamma_0$) and the outer circulations shrink as $2^{-n}$ — both bounded. Spine *vorticity* grows as $4^n$ but the recursion terminates at $\ell_P$ (finite depth), capping it at $\omega_{\max}\sim\Gamma_0/\ell_P^2$. The Planck floor regularizes the blow-up explicitly. **[OC]**

**Global/local mapping.** The *axial* channel conserves circulation and carries handedness — its net across the dual sublattices is the conserved **global** helicity (the "DC"). The *lateral* channel halves and spreads, forming the locally-varying **local** helicity density (the "AC"). This is the global-fixed / local-varying structure, now *derived* from the node law rather than assumed. **[OC/IR]**

---

## 13. Dynamics V — the shared-node combination rule & the necessity of dual counter-rotation

Each outer child is *shared* by two adjacent cells; each sends $\tfrac12\Gamma$ into it. Whether these add or cancel is fixed by the relative handedness of the two parents.

**The swirl geometry.** Both spines run parallel along $[1,1,1]$; the shared child sits to the side of each. The azimuthal swirl each induces at the shared point ($\hat n \times \mathbf{r}_\perp$) points in *opposite* directions for the two parents when they share the same handedness, and the *same* direction when their handedness is opposite. This is the textbook fact on the lattice: **co-rotating neighbours cancel in the gap between them; counter-rotating neighbours reinforce.** **[OC]**

- Same-handedness pair → **destructive** node ($\approx 0$).
- Opposite-handedness pair → **constructive** node ($\approx \Gamma_n$, i.e. $2\times\tfrac12\Gamma_n$).

**Necessity of the dual structure.** If the whole matrix had one handedness, every shared node would be co-rotating → every lateral child would cancel → the matrix would collapse to decoupled axial spines with no lateral cascade. The lateral cascade exists *only* if neighbours have opposite handedness. Therefore the **dual counter-rotating** sublattice structure is a derived necessity, not an aesthetic choice — the "DC" of DCCREG is forced. **[OC for the mechanism; IR for the reading]**

**Arrangement (fork).** Bipartite (alternating handedness on cubic sites): every axis-neighbour is opposite → every shared node constructive → maximal coupling; here the destructive interference lives in the *field* (§14), not at the nodes. A mixed arrangement instead realises per-node constructive/destructive interference directly. Current working choice: bipartite. **[IR]**

**Dimension consequence.** Counting *distinct* cells with sharing gives $1+6\times\tfrac12 = 4$ per level, hence the matrix dimension $D=\log_2 4 = 2.0$ (§4, §10), superseding the single-tree $2.807$. **[OC for the count; IR for operativeness]**

---

## 14. The field-interference frame

With the node and shared-node rules fixed, the two projections (§7) produce two qualitatively different fields.

**Pressure — handedness-blind, all-reinforcing.** $p$ is built from $\lvert\boldsymbol\omega\rvert^2$ (even under mirror), so both sublattices source it identically; there is no handedness cancellation. Pressure is a smooth Coulomb landscape, peaked at the vortex cores, the same for left- and right-handed cells. **[OC]**

**Helicity — sign-carrying, interfering.** $\mathbf u$ is linear in $\boldsymbol\omega$ and carries the sign, so the helicity density $h=\mathbf u\cdot\boldsymbol\omega$ alternates sign cell-to-cell across the dual sublattices. A continuous field changing sign must vanish on the surfaces between cells — the cell faces — which are **2-dimensional**, codimension-1, space-pervading. **[OC]**

**The convergence.** These $h=0$ faces are, simultaneously:
- the $D=2$ active set counted geometrically (§13);
- the $k^{-2}$ shock fronts — same-amplitude velocity jumps living on surfaces (§10);
- the boundaries between local left- and right-handed cells (the cyclone/anticyclone cells of the global/local principle);
- the locus of the "negative-constructive" superposition stipulated at the outset.

Four independently-derived threads name the same 2-D surface network. **[OC for each thread; IR for the identification that they coincide]**

**Standing, never settling.** Losslessness forbids relaxation, so the interference on these faces is a *permanent standing pattern* (in space and in scale, via the two-way cascade of §11). The never-settle condition now has an explicit geometry: a standing wave on the cancellation sheets. **[OC/IR]**

**Summary of the field structure.** Pressure = smooth all-reinforcing landscape (the "electrostatic" potential, peaked at cores); helicity = perpetually-standing checkerboard whose 2-D cancellation faces carry the shock-front cascade; global handedness on the axial channel, local handedness in the cells.

---

## 15. Open forks / to-derive next

1. **Well-posedness proof.** The Planck-floor cap (§12) makes amplitude finite; a fully rigorous bound on $\Gamma$ at a node remains to be written.
2. **Per-child allocation — RESOLVED (v0.4).** The node law (§12): $\Gamma_c=\Gamma_n$, $\Gamma_o=\tfrac12\Gamma_n$. The remaining sub-item is the *shared-node combination* under a mixed (non-bipartite) arrangement.
3. **Helicity flux law.** The co-cascade of helicity (sign fixed by the screw) is sketched, not fully derived alongside the energy flux.
4. **Screw-angle fork — RESOLVED (v0.2).** $C_3$-sector golden angle $120^\circ/\varphi^2 \approx 45.8^\circ$; full-circle $137.5^\circ$ rejected. See §4 correction.
5. **Dimension/arrangement — partially resolved (v0.4).** Matrix $D=2.0$ established (§13); the sublattice *arrangement* (bipartite vs mixed) and the magnitude of the global handedness imbalance remain open.
6. **Quantitative field solution.** The interference pattern (§14) is derived qualitatively; the full Biot–Savart / Coulomb sums over the skeleton are a simulator task.
7. **Next blocks (new scope, deliberately not started here):**
   - (a) Specific solutions / the "electrostatic discharge" events.
   - (b) The higher-scale **MHD-mixture** emergence (item #5): coarse-graining the vorticity-as-$\mathbf{B}$ and pressure-as-$\mathbf{E}$ analogies into magnetohydrodynamics, including the finite emergent wave speeds vs the infinite micro sound speed.

---

## Appendix — symbols & core equations

### Symbols

| Symbol | Meaning |
|:--|:--|
| $\rho$ | (constant) density |
| $\mathbf{u}$ | velocity field (derived, vector projection of $\boldsymbol{\omega}$) |
| $\boldsymbol{\omega} = \nabla\times\mathbf{u}$ | vorticity (master field, on the skeleton) |
| $S$ | strain-rate tensor |
| $p$ | pressure (scalar projection of $\boldsymbol{\omega}$; the electrostatic potential) |
| $H = \int \mathbf{u}\cdot\boldsymbol{\omega}\,dV$ | kinetic helicity (conserved pseudoscalar = chirality) |
| $\Gamma = \oint \mathbf{u}\cdot d\mathbf{l}$ | circulation ("amplitude" of a filament) |
| $Q$ | $Q$-criterion, $\tfrac{1}{2}\!\left(\tfrac{1}{2}\lvert\boldsymbol{\omega}\rvert^2 - \lvert S\rvert^2\right)$ |
| $\rho_{\text{eff}} = 2\rho Q$ | effective charge density (source of $p$) |
| $\ell_P \approx 1.616\times10^{-35}\ \mathrm{m}$ | Planck-scale recursion floor |
| $D = \log_2 4 = 2.0$ | SOSF **matrix** fractal dimension (operative; v0.4). Single-tree limit set is $D_{\text{tree}}=\log_2 7\approx2.807$ |
| $\beta = 1/2$ | active-fraction ratio per recursion ($\beta$-model; v0.4, supersedes $7/8$) |
| $\Gamma_c = \Gamma_n,\ \ \Gamma_o = \tfrac12\Gamma_n$ | node allocation: central spine (conserved) and each outer child (lateral cascade) |
| $\theta = 120^\circ/\varphi^2 \approx 45.8^\circ$ | $C_3$-sector golden-angle screw per recursion about $[1,1,1]$ (v0.2; supersedes $137.5^\circ$) |

### Core equations

$$\nabla\cdot\mathbf{u} = 0 \qquad\text{(incompressibility)}$$

$$\frac{D\boldsymbol{\omega}}{Dt} = (\boldsymbol{\omega}\cdot\nabla)\mathbf{u} \qquad\text{(vorticity transport)}$$

$$\nabla^2 p = \rho\!\left(\tfrac{1}{2}\lvert\boldsymbol{\omega}\rvert^2 - \lvert S\rvert^2\right) = \rho_{\text{eff}} \qquad\text{(pressure–Poisson / electrostatics)}$$

$$\mathbf{u} = \nabla\times\mathbf{A}, \qquad \mathbf{A} = \frac{1}{4\pi}\int \frac{\boldsymbol{\omega}}{\lvert\mathbf{x}-\mathbf{x}'\rvert}\,d^3x' \qquad\text{(Biot–Savart, vector projection)}$$

$$p = -\frac{\rho}{4\pi}\int \frac{\tfrac{1}{2}\lvert\boldsymbol{\omega}\rvert^2 - \lvert S\rvert^2}{\lvert\mathbf{x}-\mathbf{x}'\rvert}\,d^3x' \qquad\text{(scalar projection)}$$

$$\varepsilon = \frac{\rho\, u_n^3\, p_n}{\ell_n} = \text{const} \qquad\text{(cascade transfer law)}$$

$$\Gamma_c = \Gamma_n,\qquad \Gamma_o = \tfrac12\,\Gamma_n \qquad\text{(node allocation: spine / six lateral)}$$

$$E(k) \propto k^{-\frac{8-D}{3}} = k^{-2} \quad (D=2) \qquad\text{(predicted spectrum; Burgers/shock-like)}$$
