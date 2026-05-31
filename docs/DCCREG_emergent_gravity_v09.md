# DCCREG Block IV — Emergent Gravity from Vortex-Lattice Elasticity

**Version:** 0.9 (Gravity-gate block)

**Scope of this document:** what gravitational theory the strained chiral vortex lattice (Block III) produces, and where it can be falsified. It establishes the kinematic analog metric; the strain→metric dictionary and Newtonian limit; the **compatible/incompatible strain split** that unifies the gravity and fermion gates (light = compatible phonon sector; gravity+matter = incompatible defect sector); the **gradient-order make-or-break** that decides whether the dynamics is Einstein (Kleinert $1/k^2$) or a softer higher-derivative gravity ($1/k^4$); the **boundary-condition / screening ("atmosphere")** structure — the DCCREG vacuum is a medium, not empty space, so GR's asymptotic flatness is replaced by a substrate background with a plasma screening length; the identification of the emergent theory (conditional on the gradient test) as **khronometric gravity**; the preferred-frame result — the substrate's two locked features (light-is-the-graviton, infinite sound speed) **force $\alpha_1=0$**, with $\alpha_2$ parked at an instantaneous-limit singularity; and (v0.4) the recognition that gravity is **Coulomb-gauge** like the electrodynamics — an *instantaneous* longitudinal Newtonian potential ($1/k^2$, the strong channel) plus the finite-$c$ transverse graviton — which firms the static sector toward Einstein/Newtonian form and explains gravity's weakness as the **unscreened residual** of the strong-but-screened Coulomb sector. General Relativity is treated as one falsifiable hypothesis among several, recovered as the $\alpha_1,\alpha_2\to0$ infrared limit; it is not the success criterion.

**Companion documents:** Block I (*Foundations* v0.4), Block II (*MHD Emergence* v0.2), Block III (*Radiative EM & Emergent Lorentz Invariance* v0.2), and **Block V (*Emergent Matter* v0.5, the matter/fermion gate)** — the joining of §5.5/§10.1's $K_A$ residual with the defect spectrum is shared with Block V (see **V-§2, V-§9**). References prefixed **I-§ / II-§ / III-§ / V-§** point to those; unprefixed **§** is internal.

> **Status of this block.** The kinematic analog-gravity mechanism and the compatible/incompatible (defect-geometry) results are standard physics **[OC]**; the identification of the compatible sector with light and the incompatible sector with gravity+matter is **[IR]**; the khronometric and Coulomb-gauge identifications are [OC classification + IR adoption]; the $\alpha_1=0$ result is **[OC given the §5.4 premise]**; the boundary-condition/screening structure and the "gravity = unscreened Coulomb residual" reading are **[IR]**; the routes to genuine Einstein *dynamics* and the cosmological reach of screening are **[RH]** (the latter quarantined to the sandbox). **This block does not claim to derive GR, and does not treat non-GR as failure.** It locates the construction precisely and names the computations ($1/k^2$ vs $1/k^4$; $\alpha_2$; $\kappa$; the energy→softening sign) that confirm or kill it.

---

## Revision history

| Version | Date | Author | Summary of changes |
|:--|:--|:--|:--|
| 0.1 | 2026-05-29 | DCCREG Modeling Programme | Initial release. Kinematic analog metric from varying $C_{66}$; strain→metric dictionary and Newtonian/Poisson limit; light bending with PPN $\gamma$ as make-or-break; dynamics classified as Lorentz-violating aether/Hořava-type, GR as IR limit; Sakharov / Kleinert routes flagged [RH]; defect–elasticity stress-energy source; isotropy and GW-speed threads. |
| 0.2 | 2026-05-29 | DCCREG Modeling Programme | **Gravity class identified + verdict reframed.** Infinite sound speed ⇒ global foliation ⇒ khronon ⇒ **khronometric gravity** specifically; two projections = khronon (longitudinal) + graviton (transverse); $c_{\rm GW}=c_\gamma$ passes GW170817 structurally; preferred-frame PPN $\alpha_1,\alpha_2$ named as the empirical content, GR = $\alpha_1,\alpha_2\to0$; khronon-pathology-tamed conjecture [RH]; verdict reframed from "falls short of GR" to "predicts a specific falsifiable non-Einsteinian gravity." |
| 0.3 | 2026-05-29 | DCCREG Modeling Programme | **Correction + compatible/incompatible merger + first preferred-frame computation (major).** (1) **Correction to §5.1**: the Fierz–Pauli *mass* claim was wrong — the shear phonon is **gapless/massless**; the strain is the *field strength* of the displacement. (2) **Compatible/incompatible split** (§5.2): compatible ⇒ flat ⇒ **phonon = light**; incompatible ⇒ defects ⇒ **gravity+matter** (Kröner: incompatibility = linearized Einstein tensor). **The gravity gate and the fermion gate are one sector.** (3) **Gradient-order make-or-break** (§5.4): first-gradient ⇒ $1/k^4$ (not Einstein), second-gradient ⇒ $1/k^2$ (Einstein); §6 conditional on this. (4) **$\alpha_1$ computed** (§6.7): $c_{13}=0$ (graviton=light) + $c_{14}=0$ (instantaneous khronon) ⇒ $\alpha_1=-4c_{14}\to0$, robust against unknown $c_1,c_2$; $\alpha_2$ parked at $0/0$. |
| 0.4 | 2026-05-29 | DCCREG Modeling Programme | **Boundary conditions / screening + Coulomb-gauge gravity (major).** (1) **Fork-1 refinement** (§5.5): the defect power-law depends on rigid-skeleton ($1/k^4$, softer) vs melted-fluid ($1/k^2$, Einstein) reading; the *locked fluid/plasma* assumption + the compatible/incompatible split (rigid for light, melted for gravity) make it **lean Einstein**, conditional on the fluidity operating at the metric scale. (2) **Boundary-condition / "atmosphere" section** (new §5.6): the DCCREG vacuum is the substrate equilibrium, not empty Minkowski — so GR's asymptotic flatness is replaced by a structured background with a **plasma/penetration-depth screening length $\kappa$**; **Einstein is the featureless-medium limit** ($\kappa\to0$, flat background, no frame, no floor) — a doubly-exceptional corner (coupling limit *and* boundary-condition limit). Screening = a bounded prediction; the fringe "electric universe" reach is quarantined to the sandbox. (3) **Coulomb-gauge gravity** (new §6.8): resolving the transverse-vs-instantaneous tension, gravity splits like the II-§7 electrodynamics into an **instantaneous longitudinal Newtonian potential** ($1/k^2$, the *strong* channel — the static attraction, correctly instantaneous for the Newtonian limit) **plus the finite-$c$ transverse graviton** (GW = light's sibling, weak). The dominant defect interaction rides the strong Coulomb ($1/k^2$) channel ⇒ static sector firmed to Einstein/Newtonian form; the $1/k^4$ shear is a subdominant correction. **Gravity's weakness explained:** it is the **unscreened residual** of the strong-but-screened (quasi-neutral, II-§5) Coulomb sector — the standard reason gravity dominates large-scale structure, reproduced. (4) Verdict (§9) bumped from "undecided, leans Einstein via melting" to "**static/Newtonian sector firmed to $1/k^2$ via the dominant Coulomb channel; weakness explained; full Einstein dynamics still pending the explicit defect computation**"; open forks and Appendix updated. Section numbers preserved; §5.5/§5.6/§6.8 added. |
| 0.5 | 2026-05-29 | DCCREG Modeling Programme | **Hexatic resolution of the Fork-1 conditional (major).** The dislocation probe (does the SOSF confine or proliferate dislocations?) resolves the rigid-vs-fluid duality of §5.5. (1) **Dislocations are free, not confined**: the substrate is a fluid maintaining no positional order (I-§6, "no substrate transport; the pattern reconfigures"), so a positional dislocation is not held against its $\sim\mu b^2\ln(L/a)$ confinement energy — dislocations are effectively proliferated. (2) **The fixed immutable skeleton pins orientation, not position** — and orientational order without positional order is the **hexatic phase**. The SOSF's two locked features (fixed orientation + fluid position) *are* the hexatic conditions; the rigid/fluid duality **is** the hexatic's orientational-rigid/positional-fluid structure. (3) **Hexatic ⇒ Einstein form**: free dislocations **screen** the disclination (curvature) interaction from the confining $\sim r^2\ln r$ ($1/k^4$) down to $\sim\ln r$ ($1/k^2$) — KTHNY/Kleinert. The melting conditional is resolved *structurally* (no melting-temperature computation needed). (4) **Two channels converge on $1/k^2$**: the §6.8 strong-Coulomb channel and this hexatic-screening channel give the same power independently — robust. (5) **Gates re-locked via melting**: the surviving bound defects are the **disclinations** = orientational/topological charges = fermion-gate matter; gravity = their screened $1/k^2$ interaction. Caveats: clean physics is 2D-KTHNY (the $[1,1,1]$ screw makes the relevant problem quasi-2D, which helps); the 3D coefficient and exact-linearized-Einstein status need the explicit computation; a hexatic has zero *static* shear so light rides the *dynamic* shear rigidity (refinement owed to Block III). Verdict bumped to "**leans Einstein robustly, conditional resolved structurally; closure needs the quasi-2D disclination coefficient**." §5.5 rewritten; §5.7 added; §9/§10/footer updated. |
| 0.6 | 2026-05-29 | DCCREG Modeling Programme | **Fork-1 closure — disclination interaction computed (major).** The quasi-2D hexatic disclination interaction was computed (not asserted): it fits $E\propto\ln r$ (pure log; $1/k^2$, not the solid's $r^2\ln r$/$1/k^4$), and the direct test $\int_{\rm disk}\nabla^2(\ln r/2\pi)\,dA=1.000$ confirms the kernel **is the 2D Laplacian Green's function** = the Newtonian/Einstein gravitational potential. So the gate that v0.3 opened closes **on the Einstein side**, by computation, *conditional on the SOSF-is-hexatic identification* (§5.5, [IR]); the §6.8 strong-Coulomb channel agrees independently. **Honest self-correction:** the script's screening-crossover demonstration (an $e^{-r/\xi}$ proxy sampled at $r=3\xi$) printed "ratio≫1" while the numbers were ≪1 — the proxy was the wrong model (in a true hexatic the confining term is *removed* beyond $\xi_+$, not exp-damped) and that interpretive line is withdrawn; the power-law/Green's-function result is independent of it and stands. **Residuals (quantitative, not the fork):** the coefficient = Frank constant $K_A$ (finite, positive; an $\ln(d/a)$-type ratio, the analog of III's $\beta/\alpha$) is unpinned; the genuine 3D coefficient (stacking quasi-2D $\ln r$ → 3D $1/r$) and the static-vs-dynamic-shear refinement remain. Verdict bumped from "leans Einstein robustly" to "**computes to the Einstein/Newtonian $1/k^2$ form, conditional on hexatic; coefficient residual**." §5.5 closure note added; §9/§10/footer updated. |
| 0.7 | 2026-05-29 | DCCREG Modeling Programme | **The Joining — $K_A$ closed parametrically; shared with Block V (major).** The disclination spectrum (the $K_A$ residual of v0.6) is the *same object* as the Block V matter content; the joining computation (V-§9) fixes the gravity-side pieces parametrically. (1) **$K_A$ = Block III line tension $\beta$.** The Frank constant (disclination/orientational stiffness setting the $1/k^2$ interaction strength, hence $G_{\rm eff}\sim 1/K_A$) is parametrically the **same bond-bending stiffness $\beta$** that Block III computed for light isotropy — both the orientational-bending stiffness $\propto\rho\Gamma^2\ln(d/a)$. At Block III's isotropy point $\ln(d/a)\approx4$ ($\beta=\alpha$), $K_A$ is pinned in terms of $\rho\Gamma^2$. **Light isotropy and gravity strength share one parameter** — the $K_A$ residual is closed *parametrically* (precise numeric coefficient still needs the lattice Biot–Savart sum = simulator). (2) **Matter charges = chiral octahedral group $O$.** The allowed disclination Frank angles are the conjugacy classes of $O$ (order 24, mirror-free, consistent with the screw): **{90°,120°,180°}**, the 120° ($C_3$ about $[1,1,1]$) being the screw-aligned one (Block I's sector). These are the curvature sources = the Block V matter charges. (3) New **§3a** records the joining; §9/§10/footer updated; Block V cross-references (V-§2, V-§9) added. No change to the v0.6 power-law closure. |
| 0.8 | 2026-05-30 | DCCREG Modeling Programme | **$K_A$ computed — simulator run002 (major).** The lattice Biot–Savart sum (validation ladder 5/5 PASS; run `run002_sosf_spectrum_iterated`, git `ddd7c80`) turns the parametric $K_A\sim\beta$ into a number. (1) **$\beta = 0.07905\,\rho\Gamma^2$** (extrapolated $d\to0$) vs analytic $\rho\Gamma^2/4\pi=0.07958$ — **0.66% error**, monotone convergence. At the isotropy point $\ln(d/a)=4$: **$K_A\approx0.316\,\rho\Gamma^2$, $G_{\rm eff}\approx3.16/\rho\Gamma^2$.** [OC value, on the IR $K_A\sim\beta$ id.] **CONFIRMS** $K_A\sim\beta$ (lands $O(1)\,\rho\Gamma^2$). (2) **3D cross-check validates the quasi-2D reduction** (§5.7 caveat closed): full 3D filament sum coefficient 0.07881 (1.0% from 2D); the $[1,1,1]$-screw helix raises line tension only ×1.014 (~1%) — extra arc length nearly cancelled by antiparallel tangents. $K_A$ essentially unchanged in 3D. [OC] (3) **Screening length computed** (§5.6 "atmosphere" refined): genuine Debye screening by free dislocations, $(-\nabla^2+m^2)G=\delta$, gives $\xi=\kappa^{-1}\propto n_{\rm disloc}^{-1/2}$ (2D Debye–Hückel), validated vs continuum $K_0(\kappa r)$ to ~1.7%; $\xi\in[9,40]$ lattice units over the density range. Law [OC]; absolute $\xi$ rests on the dislocation density $n_d$ [IR]. This is genuine Debye screening — **not** the withdrawn v0.6 exp-proxy. (4) **$E(r)$ on the real lattice CONFIRMS the $\ln r$ (1/k², Einstein/Newton) form** (ln-fit residual 0.0016 vs $r^2\ln r$ residual 0.036); coefficient $-0.0864/\ln r$ vs analytic $-\sqrt3/6\pi=-0.0919$ (~6%, finite-torus-limited — form robust, coefficient ~10%). Parametric $K_A\sim\beta$ statement of §3a moved to History below; §3a updated with the number. Residual: the ~6–10% $E(r)$ coefficient (finite torus, not improvable on a torus). |
| 0.9 | 2026-05-31 | DCCREG Modeling Programme | **Dimensional reduction / physical scales (run005) — accounting refinement, not a new mechanism.** The reduction layer (validation ladder incl. two new rungs — dimensional closure and known-limit recovery of run002 $K_A=0.3162\,\rho\Gamma^2$ / run004 gap$(J{=}1)=2.000$ — all PASS) collapses every gravity-sector quantity to $\{\rho,\Gamma,\ell_P\}\times g(J,\ln(d/a))$ ($+\kappa{=}2m/q$ for the EM dictionary, $+n_d$ for screening), with **no hidden dimensional input** — confirming the declared free-parameter count. Recorded: the reduced form $G_{\rm eff}\sim\Gamma^2/(\rho\ell_P^4)\ln(d/a)$ [OC dims]; the cross-gate combination $(m_D/m_{\rm Planck})^2=G_{\rm eff}m_D^2/(\hbar_{\rm eff}c)$ reducing to $J^2\ln(d/a)^{-3/2}$ — the base scales $\rho,\Gamma,\ell_P$ cancel, **but that cancellation is the generic consequence of forming a dimensionless ratio on a three-constant $\{M,L,T\}$ basis, not a special signature of the gravity↔matter sharing**; the informative content is the residual exponents (the shared $\ln(d/a)$ traces the common stiffness $K_A\sim\beta$), tier **[OC arithmetic on the [IR] reduced forms]**. Two emergent scales identified, **[IR]**: $\hbar_{\rm eff}\sim\rho\Gamma\ell_P^3$ (the angular momentum of a Planck-scale vortex; dimensionally [OC]) and $c\sim(\Gamma/\ell_P)\sqrt{\ln(d/a)}$. **No parameter-free cross-gate number emerges** (held open by the absence of an external $\hbar$, the free $J$, and the inexact $\ln(d/a)\approx4$): the located gap is one uncomputed $O(1)$ geometric prefactor + an exact $\ln(d/a)$. New §10 fork 10; §3a note; bidirectional cross-ref to **V-§9**. **No change** to the v0.8 $K_A\approx0.316\,\rho\Gamma^2$ value or the power-law closure. |

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

## 3a. The Joining — $G_{\text{eff}}$ from the defect spectrum (shared with Block V)

*(v0.7. This section records the gravity-side half of the joining computation. The same defect spectrum is the Block V matter content; the matter-side half is **V-§9**, and the defect-charge inventory is **V-§2**. The two gates are one object: see V-§9's "shared computation" statement.)*

The $K_A$ left as Block IV's quantitative residual (the disclination interaction strength, §5.5/§10.1) is fixed *parametrically* by tying it to quantities already computed.

**$K_A$ is Block III's line tension $\beta$.** The disclination interaction $E\sim(K_A/2\pi)\,\theta^2\ln r$ (the $1/k^2$ kernel of §5.5) has its coefficient $K_A$ equal to the **Frank constant** — the orientational/bending stiffness of the hexatic. That bending stiffness is parametrically the **same $\beta$** Block III computed as the vortex line tension (the achiral bond-bending stiffness that fixed light isotropy, III-§6): both are the resistance to local orientation change, $\propto\rho\Gamma^2\ln(d/a)$. Hence
$$K_A \;\sim\; \beta \;\sim\; \frac{\rho\Gamma^2\,\ln(d/a)}{4\pi d^2},\qquad G_{\text{eff}}\;\sim\;\frac{1}{K_A}\;\sim\;\frac{1}{\rho\Gamma^2\,\ln(d/a)}.$$
At Block III's **isotropy point** $\ln(d/a)\approx4$ (where $\beta=\alpha$, $A=1$), $K_A$ — and therefore $G_{\text{eff}}$ — is pinned in terms of $\rho\Gamma^2$ and the lattice spacing. **[OC for the elastic scaling; IR for $K_A\!\sim\!\beta$]**

> **Light isotropy and gravity strength share one parameter.** The single stiffness $\beta\sim\rho\Gamma^2\ln(d/a)$ fixes *both* the isotropy of light (III-§6, $\beta=\alpha$) and the strength of gravity ($G_{\text{eff}}\sim1/\beta$). The $K_A$ residual is therefore closed **parametrically** — no new free input — with only the precise numeric coefficient (the lattice Biot–Savart sum) left to the simulator. **[IR]**

**Computed (v0.8, run002 — ladder 5/5 PASS).** The lattice Biot–Savart sum closes the numeric coefficient:
$$\beta = 0.07905\,\rho\Gamma^2\ \ (\text{vs analytic }\rho\Gamma^2/4\pi=0.07958,\ 0.66\%);\qquad \boxed{K_A\approx0.316\,\rho\Gamma^2,\quad G_{\rm eff}\approx \frac{3.16}{\rho\Gamma^2}}\ \ \text{at }\ln(d/a)=4.$$
The **quasi-2D reduction is validated in 3D** (full filament sum within 1.0%; the screw helix corrects the line tension by only ~1.4%) — this closes the §5.7 dynamic/dimensional caveat on the *coefficient*. The interaction law $E(r)$ on the real triangular lattice **confirms the $\ln r$ (Einstein/Newton, 1/k²) form** (ln-fit residual 0.0016 vs $r^2\ln r$ 0.036); the *coefficient* is good to ~6–10% (finite-torus). A genuine **Debye screening length** $\xi=\kappa^{-1}\propto n_{\rm disloc}^{-1/2}$ is computed and validated against $K_0(\kappa r)$ to ~1.7% — refining the §5.6 "atmosphere" with a concrete (density-dependent) scale. **[OC for the values, on the IR $K_A\sim\beta$ and IR dislocation-density inputs]**

> **History (superseded by v0.8).** Prior to run002 the coefficient was closed only *parametrically* ("$K_A$ pinned in terms of $\rho\Gamma^2$; precise numeric coefficient left to the simulator"). That parametric statement is now replaced by the computed $K_A\approx0.316\,\rho\Gamma^2$ above; retained here as audit trail.

**The curvature sources are octahedral-group charges.** The disclinations that source the curvature carry Frank angles equal to the conjugacy classes of the chiral octahedral group $O$ (order 24, mirror-free — consistent with the screw): **{90°, 120°, 180°}**, the **120°** ($C_3$ about $[1,1,1]$) being the screw-aligned, chirality-natural charge (Block I's sector). These same charges are the Block V matter quantum numbers (**V-§2**). So the gravity source content and the matter content are one discrete, finite set. **[OC group theory; IR for "these are the matter charges"]**

**What remains (simulator).** Which disclination/vortex loops are *stable* (energies), the lowest-energy curvature source, and the precise numeric $K_A$ (lattice sum) are not fixed here — the same simulator boundary as V-§9. The joining closes the *parametric* coefficient and the *structural* gate-sharing, not the numbers.

> **Dimensional reduction (v0.9, run005 — shared with V-§9).** Reducing the gravity-side quantities to the free-input basis gives $G_{\rm eff}\sim\Gamma^2/(\rho\ell_P^4)\ln(d/a)$, and combining with the Block V Dirac mass forms the cross-gate ratio $(m_D/m_{\rm Planck})^2\to J^2\ln(d/a)^{-3/2}$ — the base scales $\rho,\Gamma,\ell_P$ cancelling. That cancellation is **dimensional** (any dimensionless ratio on the $\{\rho,\Gamma,\ell_P\}$ basis loses them — run005 dimensional-closure rung), not evidence of sector-sharing; the sharing shows only in the residual exponents (the $\ln(d/a)$ inherited from the common $K_A\sim\beta$). The Planck mass here is built from the emergent $\hbar_{\rm eff}\sim\rho\Gamma\ell_P^3$ (**[IR]**, and resting on the un-done soliton quantisation, V-§8 / V-§10 fork 2), so the ratio is an **internal scaling relation, not yet a measurable prediction**. Result tier: **[OC arithmetic on the [IR] reduced forms]**; "this ratio is a physical prediction" is **[IR]**. The framework is one uncomputed $O(1)$ prefactor + an exact $\ln(d/a)$ short of a parameter-free gravity↔mass number — a located target, not a claim. **[OC/IR]**

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

### 5.5 The power-law leans Einstein — the substrate is hexatic (dislocation probe, v0.5)

The §5.4 binary is set by whether the gravity sector is **rigid or melted**. v0.4 left this conditional ("leans Einstein if the fluidity operates at the metric scale"). The dislocation probe resolves it structurally.

**Step 1 — the relevant modulus is local.** The relevant modulus is **shear $C_{66}$**. In a vortex lattice the long-range part of the inter-vortex interaction goes into the *compression* modulus (stiffened, here infinite — the sound sector), while **shear is local and finite** (volume-preserving, screened from the long-range piece; standard Abrikosov-lattice elasticity). A local first-gradient shear modulus gives the biharmonic defect law: disclinations interact via the confining $\sim r^2\ln r$ ($\sim1/k^4$). So **a *rigid* skeleton gives softer-than-Einstein.** **[OC]**

**Step 2 — the dislocation probe: dislocations are free, not confined.** A finite local shear gives $1/k^4$ *only while dislocations are bound*. In a rigid crystal a dislocation costs $\sim\mu b^2\ln(L/a)$ — logarithmically divergent with system size — which is what confines them. But the SOSF substrate maintains **no positional order**: I-§6 is explicit that nothing is positionally transported ("what is perceived as motion is the instantaneous reconfiguration of the pressure-gradient pattern over the stationary lattice"). A positional dislocation is therefore not held against that diverging cost — the fluid accommodates it. **Dislocations in the SOSF are effectively free/proliferated.** **[IR, on the locked fluid assumption + I-§6]**

**Step 3 — the fixed skeleton pins orientation, not position ⇒ hexatic.** What the "fixed immutable skeleton" locks is *orientational/topological* structure (the screw axis, the octahedral frame, the recursion), not a pinned positional lattice. Orientational order **without** positional order *is* the **hexatic phase**. The SOSF's two locked features — fixed orientation + fluid position — are precisely the hexatic conditions. The rigid-vs-fluid duality of v0.4 is not a contradiction; it **is** the hexatic's orientational-rigid / positional-fluid structure, read correctly. **[IR]**

**Step 4 — hexatic ⇒ $1/k^2$ (Einstein form).** Standard KTHNY/Kleinert: in the hexatic, the free (proliferated) dislocations **screen** the disclination strain field, softening the disclination–disclination interaction from the confining $\sim r^2\ln r$ ($1/k^4$) down to $\sim\ln r$ ($1/k^2$) — the Newtonian/Einstein form. Dislocation proliferation *is* the screening that converts $1/k^4\to1/k^2$. The SOSF, hexatic by construction, sits in the phase where this operates. **The melting conditional is resolved structurally** — no melting-temperature computation needed; the locked features place the substrate in the melted-positional/hexatic state. **[OC for the KTHNY screening; IR for the SOSF-is-hexatic identification]**

**Two channels converge on $1/k^2$.** §6.8 obtains $1/k^2$ from the strong instantaneous Coulomb channel (defect cores = $\rho_{\text{eff}}$ charges sourcing the pressure field); this section obtains $1/k^2$ from hexatic dislocation-screening of the elastic disclination interaction. Different mechanisms — longitudinal/Coulomb and transverse/elastic — same power. The convergence makes the result robust. **[IR]**

**Re-locking the gates via melting.** The defects that survive the hexatic as bound topological objects are the **disclinations** — the orientational charges tied to the fixed skeleton — which are the curvature sources and the fermion-gate matter (linked/knotted vortices, the orientational/topological sector). So matter = the disclination sector; gravity = their dislocation-screened $1/k^2$ interaction. The fermion gate and the gravity gate are the same disclination physics, seen through melting. **[IR]**

**Net (v0.5):** the power-law **leans Einstein robustly**, with the conditional resolved structurally by the SOSF-is-hexatic identification and two independent channels converging on $1/k^2$. **Closure** — the precise (quasi-2D) disclination coefficient, and whether it is *exactly* linearized Einstein versus merely Newtonian-form — needs the explicit computation, identical to the fermion-gate disclination spectrum (§5.7, §10.1/§10.8).

**Closure (v0.6) — the disclination interaction computed.** The quasi-2D hexatic disclination interaction was evaluated directly. Two results:

1. **Power law.** The hexatic interaction fits $E\propto\ln r$ — a pure logarithm (slope-zero in log-log), i.e. **$1/k^2$** — versus the rigid solid's confining $r^2\ln r$ ($1/k^4$). The fitted log-coefficient equals $K_A/2\pi$ (the Frank constant), finite and positive.
2. **Form (the decisive test).** $\displaystyle\int_{\rm disk}\nabla^2\!\Big(\frac{\ln r}{2\pi}\Big)\,dA = 1.000$ — so the hexatic disclination kernel **is the 2D Laplacian Green's function**. A disclination (curvature charge) interacting through $\ln r$ is a mass sourcing $\nabla^2\Phi=\text{source}$: the **Newtonian/Einstein gravitational potential**, by computation. **[OC]**

So the gate v0.3 opened closes **on the Einstein side**, *conditional on the §5.5 hexatic identification* ([IR]); the §6.8 strong-Coulomb channel agrees independently.

> **Honest self-correction (v0.6).** The closure script also attempted to demonstrate the screening crossover with an $e^{-r/\xi}$ proxy sampled at $r=3\xi$, and printed "ratio $\gg1$" while the actual ratios were $\ll1$. The proxy was the wrong model — in a true hexatic the confining term is *removed* (translational stiffness renormalizes to zero) beyond $\xi_+$, not exponentially damped — so that interpretive line is **withdrawn**. The power-law / Green's-function result above is independent of the crossover demonstration and is unaffected.

**Residuals (quantitative, not the fork).** The *coefficient* is the Frank constant $K_A$, finite and positive but set by an $\ln(d/a)$-type ratio — the exact analog of Block III's $\beta/\alpha$ — and not yet pinned for the SOSF. The genuine **3D** coefficient (stacking the quasi-2D in-plane $\ln r$ into the 3D Newtonian $1/r$) and the static-vs-dynamic-shear refinement (§5.7) remain. None reopen the power law; all are the same disclination-spectrum object as the fermion gate (§10.8).

**Cautious phrasing.** The SOSF gravity sector **computes to the Einstein/Newtonian $1/k^2$ form, conditional on the substrate being hexatic** — which its own locked structure (fluid position + fixed orientation, §5.5) supplies. The conditional is [IR], strong but a reading; the computed consequence is [OC].

### 5.6 Boundary conditions — the vacuum is a medium ("the atmosphere")

The §5.4/§5.5 analysis (and the standard Kleinert and PPN results) implicitly assume the **textbook boundary condition**: an empty Minkowski vacuum with asymptotic flatness. The DCCREG vacuum is not empty — it is the substrate's equilibrium: a pressurised, chiral, plasma-like fluid with a preferred frame and a Planck floor. This is a materially different boundary condition, differing in three ways (each an "atmosphere"):

1. **A non-vanishing background.** Gravity around a mass is a perturbation matched to the substrate equilibrium, not to flat space — like a pressure disturbance in a stratified atmosphere. The background profile enters the matching. **[IR]**
2. **A screening length $\kappa$.** The substrate is *locked* plasma-like, and plasmas screen (Debye); a vortex lattice has a penetration-depth analog beyond which long-range moduli are screened. A bare $1/k^2$ interaction generically completes to a screened $1/(k^2+\kappa^2)$ (Yukawa, finite range). The "atmosphere" is the screening cloud around each mass. **[OC for plasma/vortex screening; IR for applying it to the emergent gravity]**
3. **A preferred frame + UV floor.** The khronon foliation (§6.1) and the reflecting Planck-floor boundary of the standing cascade (I-§11) are non-standard boundary data GR never sees. **[IR]**

> **Einstein gravity is the featureless-medium limit** — flat background, $\kappa\to0$, no preferred frame, no floor. Combined with §6.7 (the $\alpha_1,\alpha_2\to0$ coupling limit), GR is a **doubly-exceptional corner**: the no-atmosphere boundary-condition limit *and* the zero-preferred-frame coupling limit. The generic prediction is gravity-with-an-atmosphere. **[IR]**

The screening length is a **bounded prediction**, not free room: gravity tracks $1/r$ out to at least cluster scales, so $\kappa$ must be tiny (another tightly-constrained number, like the $\alpha$'s). Whether the *gravity-relevant* defects actually feel $\kappa$ depends on the defect's sector coupling (the §5.5/§6.8 question): the penetration depth screens the compression/tilt sectors, and §6.8 finds the dominant gravitational channel *is* the longitudinal/Coulomb one — so gravity plausibly does feel $\kappa$, with the unscreened residual being the long-range $1/r$ piece (§6.8). The fully speculative cosmological reach of this (screening → dark sector) is **quarantined to the sandbox as [RH]**; only the bounded-screening-length structure is recorded here. **[IR for the bounded prediction; RH and out-of-scope for the cosmological reach]**

### 5.7 Caveats on the hexatic resolution (kept honest)

- **2D vs 3D.** The clean physics (KTHNY hexatic → $\ln r$ disclination screening) is **2D**. The substrate is 3D, where defect-mediated melting is murkier (often first-order). Mitigation: the $[1,1,1]$ screw makes the substrate effectively anisotropic/layered, so the operative problem is plausibly the **in-plane (transverse-to-screw) 2D** one — the clean case. Kleinert's world-crystal does obtain linearized Einstein from a 3D defect sector, giving precedent, but the 3D coefficient is not free. **[OC caveat]**
- **Static vs dynamic shear.** A hexatic has **zero static shear modulus** (it flows). Block III computed $C_{66}$ as a *static* modulus for $c=\sqrt{C_{66}/\rho}$. The consistent picture is that light rides the **dynamic** (finite-frequency) shear rigidity a hexatic retains, not the static one — a refinement owed back to Block III, flagged, not resolved. **[open sub-item]**
- **Static vs full dynamics.** $1/k^2$ for the disclination interaction is the *static/Newtonian* form; full nonlinear Einstein dynamics is one further step (consistent with §6.8's "necessary not sufficient"). **[open]**

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

### 6.8 Coulomb-gauge gravity — the static potential is the strong instantaneous channel

The strength hierarchy in nature — the electromagnetic coupling exceeds gravity by $\sim10^{36}$ at the particle scale — is already encoded structurally: the longitudinal/pressure/Coulomb sector is infinite-speed and strong ($C_{11}\to\infty$), while the transverse shear modulus $C_{66}$ that carries gravity is the *small* one (I-§0, III-§6). This forces a refinement of "gravity = the transverse mode."

**The tension.** Block IV built gravity as the *transverse* shear mode (finite $c$, GW = light's sibling). But the dominant static attraction is electric in nature — *instantaneous, longitudinal*. A purely transverse gravity has no static potential; a purely longitudinal one has no waves at $c$. Both are needed.

**The resolution — gravity is Coulomb-gauge, exactly like the II-§7 electrodynamics.** Split gravity as Block II split the EM field:

| Gravitational sector | Channel | Speed | Strength | Role |
|:--|:--|:--|:--|:--|
| **longitudinal / static** | pressure/Coulomb (khronon) | **instantaneous** | **strong** | Newtonian potential, $1/k^2$ |
| **transverse / radiative** | vortex shear | finite $c$ | weak | gravitational waves (= light's sibling) |

Instantaneity of the static potential is *correct* for the Newtonian limit (Poisson's equation is solved with zero delay; Newtonian gravity is action-at-a-distance), and is consistent with the framework's preferred frame (the longitudinal sector is the non-Lorentz-invariant khronon; the transverse graviton carries the emergent LI). This is the same Coulomb-gauge architecture already vetted for the electrodynamics — a re-use, not a new risk. **[IR — structural parallel to II-§7]**

**Effect on the fork.** The defect cores *are* the $\rho_{\text{eff}}$ charges (I-§2: vortex cores = charge concentrations) and source the instantaneous pressure field. So the **dominant defect–defect interaction rides the strong Coulomb ($1/k^2$) channel**, not the weak transverse shear; the $1/k^4$ shear interaction (§5.5) is the subdominant correction, not the leading term. **The static/Newtonian sector is firmed to $1/k^2$ (Einstein/Newtonian form), with the carrying channel now identified.** **[IR; firms the Newtonian sector]**

**Why gravity is weak yet dominates large scales.** Gravity is the **unscreened residual** of the strong-but-screened Coulomb sector. Instantaneous quasi-neutrality (II-§5) screens charge separation with zero delay, so the strong $1/k^2$ electric interaction *cancels* at large scales (quasi-neutral plasma); what survives is the small, non-cancelling, same-sign piece sourced by $\rho_{\text{eff}}\propto|\omega|^2$ — gravity. It is $1/k^2$ (long-range) because it is the unscreened tail of the Coulomb kernel, and weak because it is only the residual. **This is the standard reason gravity governs large-scale structure** (electric forces strong but cancel under quasi-neutrality; gravity weak but uncancellable) — reproduced by the framework. **[IR]**

> *Scope note.* The careful statement above — electric strong but screened, gravity the weak unscreened residual — is mainstream-compatible (it *is* why quasi-neutrality lets gravity win large scales). The stronger "electric currents organise cosmic structure" (electric-universe) claim is a distinct, non-mainstream assertion and is **quarantined to the sandbox as [RH]**, not load-bearing here.

**What this firms and what it does not.** Firmed: the static/Newtonian sector is $1/k^2$ via the dominant Coulomb channel, and the weakness is explained. *Not* settled: a $1/k^2$ static potential (Newtonian limit) is **necessary but not sufficient** for the full nonlinear *Einstein dynamics* — the complete field equation still needs the explicit defect computation (§5.5, §10.1). What v0.4 establishes is the Newtonian sector and its channel, plus the resolution of the transverse-vs-instantaneous tension. **[IR; full dynamics still open]**

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
| **Is the dynamics Einstein?** | **Computes to the Einstein/Newtonian $1/k^2$ form**, now **numerically** ($E(r)$ ln-fit residual 0.0016; $K_A\approx0.316\,\rho\Gamma^2$, $G_{\rm eff}\approx3.16/\rho\Gamma^2$; quasi-2D validated in 3D to ~1%) (§5.5 closure: hexatic disclination kernel = Laplacian Green's function, $\int\nabla^2(\ln r/2\pi)=1.000$), conditional on the SOSF-is-hexatic identification; §6.8 Coulomb channel agrees. The qualitative gate is **closed on the Einstein side**; the *coefficient* ($K_A$, 3D) is the residual | [OC consequence; IR conditional; coefficient open] |
| Identified class (if Einstein-structured) | **Khronometric gravity**, forced by infinite-sound-speed foliation; **Coulomb-gauge** (instantaneous longitudinal + finite transverse, §6.8) | [OC/IR] |
| $c_{\rm GW}=c_\gamma$ (GW170817) | **Passes structurally** | [OC/IR] |
| **Why gravity is weak yet dominant on large scales** | **Explained** — the unscreened residual of the strong-but-screened (quasi-neutral) Coulomb sector (§6.8) | [IR] |
| Boundary conditions / vacuum | The vacuum is a **medium** ("atmosphere"), not empty space; a bounded screening length $\kappa$; Einstein = the featureless-medium limit (§5.6) | [IR] |
| $\alpha_1$ (preferred-frame, $\lesssim10^{-4}$) | **$=0$, forced** by $c_{13}=c_{14}=0$; robust against unknown $c_1,c_2$ | [OC given §5.4] |
| $\alpha_2$ (preferred-frame, $\lesssim10^{-7}$) | **Open** — $0/0$ at the instantaneous limit; needs redone PPN | [open] |
| PPN $\gamma=1$ | **Attainable** in this class; uncomputed | [OC; open] |
| Relation to GR | GR $=$ the $\alpha_1,\alpha_2\to0$ limit; framework predicts distinct, bounded preferred-frame effects | [OC/IR] |
| §5.1 status | **Corrected** (phonon massless; compatibility, not mass, is the issue) | [OC] |

**Bottom line.** The framework has a single coherent picture: **one chiral vortex lattice whose compatible (defect-free) sector is light and whose incompatible (defect) sector is gravity-and-matter**, with gravity itself **Coulomb-gauge** — an instantaneous strong longitudinal Newtonian potential plus a weak finite-$c$ transverse graviton. As of v0.6 the central gate is **closed on the Einstein side by computation**: the SOSF, being hexatic (fixed orientation + fluid position), has its disclination (curvature) interaction equal to the **Laplacian Green's function** — the Newtonian/Einstein $1/k^2$ form (direct test $\int\nabla^2(\ln r/2\pi)=1.000$) — with the §6.8 strong-Coulomb channel agreeing independently. Gravity's weakness is the unscreened-residual result; the vacuum is a medium with a bounded screening length (Einstein = the featureless-medium limit); $c_{\rm GW}=c_\gamma$ passes GW170817 structurally; $\alpha_1=0$ is forced. The closure is **conditional on the hexatic identification** ([IR], strong but a reading) and leaves a **quantitative residual**: the coefficient $K_A$ (an $\ln(d/a)$-type ratio), the genuine 3D coefficient, the static-vs-dynamic-shear refinement, $\alpha_2$, the energy→softening sign, and PPN $\gamma$. GR is recovered as the $\alpha_1,\alpha_2\to0$ *and* featureless-medium limit. Honest net: the qualitative Einstein-vs-softer question is settled (Einstein form, conditional on hexatic), and what remains is quantitative — coefficients and the preferred-frame parameters — all tightly bounded and all feeding the fermion gate.

---

## 10. Open forks / to-derive next

1. **Disclination coefficient — closed parametrically (§3a, §5.5, §5.7).** The power-law is **closed at $1/k^2$** (Einstein form) and the coefficient $K_A$ is now **closed parametrically** (§3a): $K_A\sim\beta\sim\rho\Gamma^2\ln(d/a)$ — Block III's line tension — so $G_{\text{eff}}\sim1/(\rho\Gamma^2\ln(d/a))$, pinned at the isotropy point $\ln(d/a)\approx4$. Remaining is the **precise numeric coefficient** (lattice Biot–Savart sum) and the static-vs-dynamic-shear refinement (§5.7). Identical to the fermion-gate disclination spectrum (item 8; **V-§9**). Simulator-addressable.
2. **Khronon strong-coupling / mode health (§6.5).** Explicit mode analysis of the instantaneous (non-propagating) khronon: free of low-energy strong coupling, or not?
3. **$\alpha_2$ at the instantaneous limit (§6.7).** Redo the PPN expansion with the khronon as an elliptic constraint; evaluate the $0/0$. Depends on the un-fixed $c_2$.
4. **Sign of the energy→softening coupling (§3).** Soften or stiffen $C_{66}$ under excitation energy? Only softening gives attraction; fixes $G_{\text{eff}}$.
5. **PPN $\gamma$ (§4).** Does $\beta=\alpha$-isotropized elasticity give $\gamma=1$ to the Cassini bound?
6. **Cosmological $G$ vs Newtonian $G$ (§6.6).** Compute $G_{\rm cosmo}/G_N$; confront BBN.
7. **Strong-field consistency (§8).** Instantaneous longitudinal sector vs finite-$c$ transverse metric beyond weak field; horizons.
8. **Fermion gate (README §6B).** Now *identical* to the gravity source (§5.2, §7): derive the SOSF defect spectrum, test spin-½ / spin-statistics, feed back as $T^{\text{defects}}_{\mu\nu}$ for items 1, 3, 6. The defect interaction of item 1 is the same object.
9. **Screening length $\kappa$ (§5.6, §6.8).** Compute $\kappa$ (the penetration-depth analog) from the substrate constants; confirm it is cosmologically large (gravity is $1/r$ to cluster scales). Determine whether the gravity-relevant defects feel it (sector-coupling, tied to item 1). The unscreened residual is the long-range Newtonian $1/k^2$ (§6.8).
10. **Physical-scale reduction — DONE as accounting (run005, §3a).** Every gravity-sector quantity reduces to $\{\rho,\Gamma,\ell_P\}\times g(J,\ln(d/a))$ with no hidden input (dimensional closure PASS). The cross-gate $(m_D/m_{\rm Planck})^2\to J^2\ln(d/a)^{-3/2}$ has the base scales cancel **dimensionally** (not structurally). **Remaining (the gap to a parameter-free number):** the $O(1)$ geometric prefactors of $c,\hbar_{\rm eff},G_{\rm eff},m_D$ (uncomputed), and an exact $\ln(d/a)$ (Block III pins only $\approx4$). The $\hbar_{\rm eff}\sim\rho\Gamma\ell_P^3$ identification presupposes the soliton quantisation of **V-§10 fork 2** — it is not a derived $\hbar$. No SI absolutes are produced or sought (by design). Shared object with **V-§9**.

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

$$\text{gravity} = \underbrace{\text{instantaneous longitudinal Newtonian potential}}_{\text{Coulomb}/\text{khronon},\ 1/k^2,\ \text{strong}} \ +\ \underbrace{\text{finite-}c\ \text{transverse graviton}}_{\text{shear, GW = light, weak}}\quad\textbf{(Coulomb-gauge, §6.8)}$$

$$\text{gravity} = \text{unscreened residual of the quasi-neutral-screened Coulomb sector}\ \Rightarrow\ \text{weak but long-range }1/k^2$$

$$\text{vacuum} = \text{medium ("atmosphere")},\quad 1/k^2 \to 1/(k^2+\kappa^2);\qquad \text{Einstein} = \text{featureless-medium limit }(\kappa\to0)$$

---

*Document status: [exploratory; internally consistent; tiers honest]. Block IV v0.9: **dimensional reduction** (run005) — every gravity-sector quantity $=\{\rho,\Gamma,\ell_P\}\times g(J,\ln(d/a))$ (closure PASS, no hidden input); $G_{\rm eff}$ reduced form recorded; cross-gate $(m_D/m_{\rm Planck})^2\to J^2\ln(d/a)^{-3/2}$ (base-scale cancellation is **dimensional**, not structural); emergent $\hbar_{\rm eff}\sim\rho\Gamma\ell_P^3$ and $c\sim\Gamma/\ell_P$ are **[IR]** ($\hbar_{\rm eff}$ presupposes the un-done soliton quantisation, V-§10 fork 2). No parameter-free cross-gate number — gap = $O(1)$ prefactor + exact $\ln(d/a)$. No change to the v0.8 $K_A$ value or power-law closure. Prior (v0.8): $K_A$ **computed** (run002, ladder 5/5): $K_A\approx0.316\,\rho\Gamma^2$, $G_{\rm eff}\approx3.16/\rho\Gamma^2$; quasi-2D reduction validated in 3D (~1% screw correction); $E(r)$ confirms the $\ln r$ Einstein form on the real lattice; a Debye screening length $\xi\propto n_d^{-1/2}$ refines the atmosphere. Prior (v0.7): **The Joining** (§3a) closes the $K_A$ coefficient *parametrically* — $K_A\sim\beta$ (Block III line tension) $\sim\rho\Gamma^2\ln(d/a)$, so $G_{\text{eff}}\sim1/(\rho\Gamma^2\ln(d/a))$, pinned at the isotropy point; light isotropy and gravity strength share one parameter. The disclination/curvature charges are the chiral octahedral group $O$ = the Block V matter charges (V-§2). The defect spectrum is one object across both gates (V-§9). Prior (v0.6): the central gate is **closed on the Einstein side by computation** — the hexatic SOSF disclination interaction equals the 2D Laplacian Green's function ($\int\nabla^2(\ln r/2\pi)=1.000$), the Newtonian/Einstein $1/k^2$ form, with the §6.8 Coulomb channel agreeing. Closure is conditional on the [IR] hexatic identification; a botched screening-crossover demonstration in the closure script was withdrawn (the power-law result is independent). Gravity is Coulomb-gauge, weak as the unscreened Coulomb residual, with $\alpha_1=0$ forced and $c_{\rm GW}=c_\gamma$ structural. Residuals are quantitative: the coefficient $K_A$, the 3D coefficient, dynamic-vs-static shear, $\alpha_2$, the energy→softening sign, $\gamma$. The fermion gate is the same disclination object (§10.1/§10.8) and is the natural next block.*
