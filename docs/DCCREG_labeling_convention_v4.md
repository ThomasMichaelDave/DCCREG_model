# DCCREG 7-Sphere Cell — Labeling Convention
### Reference document for model annotation, Kells image correspondence work, and 3D simulator highlight specification

**Version:** v4

> **Editorial status of this draft (v4).** Promotes the Tier 9 **gyrator**
> from [CONJECTURAL] to [OPERATIONAL] by deriving it from the model's
> chirality (new §9G), and retires three provisional names by binding them
> to derived quantities: **σ ("dielectric density")** → the pressure field
> P / source ρ_eff; **"son" (F/M coupling channel)** → the gyrational
> coupling (the ω₊·ω₋ cross-term); and de-provisionalises **Φ (flow)** as
> the current analog J ∝ ∇×ω. The four-sphere junctions Θ⁴ remain
> *provisional* (open geometry, untouched here). Cross-references to the
> derivation programme use **I-§** (Block I: Foundations v0.4) and
> **II-§** (Block II: MHD Emergence v0.2).

---

## Revision history

| Version | Date | Summary of changes |
|---------|------|--------------------|
| v2 | — | Base labeling convention: seven spheres, lenses (Λ/λ), junctions (Θ), great circles, sectors, views, vortex states. |
| v3 | — | Added geometric primitive sub-elements (Tier 1B–3D); two new tiers — Tier 8 (wave/field variables) and Tier 9 (network/circuit elements) — for the pressure-impulse / capacitor model; Appendix B (flat master highlight table for simulator import). Several Tier 7–9 items marked *provisional* pending review. |
| v4 | 2026-05-29 | **Gyrator theory + provisional-name retirement.** (a) New **§9G — Gyrator theory from chirality**: the gyrator is derived as the non-reciprocal two-port whose required time-reversal/mirror-symmetry breaking *is* the model's chirality; its coefficient G is a pseudoscalar hosted by the chiral (helicity) traversal, gyration rate ω_c = 2⟨ω⟩, giving L_eff = G²C as the lumped form of the two-projection structure (C = pressure/electric, L = magnetic/vorticity, G = chirality). Tier 9 gyrator promoted [CONJECTURAL] → [OPERATIONAL]; geometric host changed from "lens body / Θ region (TBD)" to "chiral traversal / local helicity." (b) Retired **σ "dielectric density"** (Tier 8): no independent dielectric — the capacitive-storage field is the pressure P, sourced by ρ_eff ∝ \|ω\|². (c) Retired **"son"** (Tier 7): the F/M coupling channel is the gyrational coupling = the ω₊·ω₋ cross-term (→ §9G). (d) De-provisionalised **Φ (flow)** = current analog J ∝ ∇×ω. (e) Updated component-count table, Appendix B checkbox tree, B.2 master table, and B.3 note 5 accordingly. Θ⁴ four-junctions remain provisional. |

---

## TIER 1 — THE SEVEN SPHERES

| Label | Name | Position | Role |
|-------|------|----------|------|
| **Ω** | Central sphere | origin (0,0,0) | Column hub; receives from both poles |
| **Z⁺** | North polar sphere | +Z axis | Upper driver; draw phase |
| **Z⁻** | South polar sphere | −Z axis | Lower driver; expel phase |
| **X⁺** | East equatorial sphere | +X axis | Lateral coupling |
| **X⁻** | West equatorial sphere | −X axis | Lateral coupling |
| **Y⁺** | Front equatorial sphere | +Y axis | Lateral coupling |
| **Y⁻** | Back equatorial sphere | −Y axis | Lateral coupling |

**Groupings for shorthand:**
- **polar pair** = {Z⁺, Z⁻}
- **equatorial quartet** = {X⁺, X⁻, Y⁺, Y⁻}
- **3-sphere driver column** = {Z⁺, Ω, Z⁻}
- **full 7-sphere cell** = all of the above

---

## TIER 1B — SPHERE PRIMITIVE ELEMENTS

For each sphere S ∈ {Ω, X±, Y±, Z±}, the following geometric
primitives are defined for annotation and simulator highlight.

| Label | Symbol | Definition |
|-------|--------|------------|
| **Sphere interior** | int(S) | Open ball of radius R about C_S |
| **Sphere boundary** | ∂S | 2-sphere surface of radius R about C_S |
| **Sphere centre** | C_S | The centre point of S |

Reference syntax for simulator: `S.interior`, `S.boundary`, `S.centre`
(e.g. `Ω.boundary`, `X⁺.centre`).

---

## TIER 1C — SPHERE UNIT COMPOSITE

The seven spheres treated as one composite object at one
recursion level (no parent or child structure invoked here).

| Label | Symbol | Definition |
|-------|--------|------------|
| **Sphere unit** | U | The seven-sphere assembly Ω ∪ X± ∪ Y± ∪ Z± |
| **Unit centre** | O | The centre of Ω; also the centroid of all seven sphere centres; the origin (0,0,0). The dimensionless impulse origin in §8 |
| **Unit boundary** | ∂U | The outer envelope of U. Comprises six spherical caps drawn from the six equatorial sphere boundaries |

---

## TIER 2 — LENS JUNCTIONS

Two geometrically distinct lens types carry different pressure
coupling constants (κ). Label prefix: **Λ** for central-outer,
**λ** for outer-outer.

### 2A — Central-Outer Lenses (6 total) — prefix Λ
κ_central = 3/16. These are the vertical-register coupling lenses.

| Label | Connects | Type | Pressure character |
|-------|----------|------|--------------------|
| **Λz⁺** | Ω ↔ Z⁺ | polar CO | s ≈ 0, low centrifugal bias |
| **Λz⁻** | Ω ↔ Z⁻ | polar CO | s ≈ 0, low centrifugal bias |
| **Λx⁺** | Ω ↔ X⁺ | equatorial CO | s = R, high centrifugal bias |
| **Λx⁻** | Ω ↔ X⁻ | equatorial CO | s = R, high centrifugal bias |
| **Λy⁺** | Ω ↔ Y⁺ | equatorial CO | s = R, high centrifugal bias |
| **Λy⁻** | Ω ↔ Y⁻ | equatorial CO | s = R, high centrifugal bias |

**Groupings:**
- **Λ-polar** = {Λz⁺, Λz⁻} — axial, low-pressure, poloidal throughflow carriers
- **Λ-eq** = {Λx⁺, Λx⁻, Λy⁺, Λy⁻} — equatorial, high-pressure, vortex hosts

### 2B — Outer-Outer Lenses (12 total) — prefix λ
κ_lateral = 1/8. These are the lateral-register coupling lenses
forming the cuboctahedral medial structure.

**Polar-equatorial group (8 lenses):**

| Label | Connects |
|-------|----------|
| **λ(z⁺x⁺)** | Z⁺ ↔ X⁺ |
| **λ(z⁺x⁻)** | Z⁺ ↔ X⁻ |
| **λ(z⁺y⁺)** | Z⁺ ↔ Y⁺ |
| **λ(z⁺y⁻)** | Z⁺ ↔ Y⁻ |
| **λ(z⁻x⁺)** | Z⁻ ↔ X⁺ |
| **λ(z⁻x⁻)** | Z⁻ ↔ X⁻ |
| **λ(z⁻y⁺)** | Z⁻ ↔ Y⁺ |
| **λ(z⁻y⁻)** | Z⁻ ↔ Y⁻ |

**Equatorial-equatorial group (4 lenses) — the equatorial ring:**

| Label | Connects |
|-------|----------|
| **λ(x⁺y⁺)** | X⁺ ↔ Y⁺ |
| **λ(x⁺y⁻)** | X⁺ ↔ Y⁻ |
| **λ(x⁻y⁺)** | X⁻ ↔ Y⁺ |
| **λ(x⁻y⁻)** | X⁻ ↔ Y⁻ |

**Groupings:**
- **λ-pe** = 8 polar-equatorial OO lenses
- **λ-ee** = 4 equatorial-equatorial OO lenses (the equatorial square ring)

---

### 2C — Lens geometric primitives (per lens)

Each lens L = L(S₁, S₂), whether Λ or λ, has the following
geometric primitives. Reference syntax for simulator: `L.<suffix>`.
These geometric-primitive suffixes coexist with the pressure-character
sub-region suffixes `.c / .a / .b / .ab` defined in §3; the two
suffix families do not collide because the geometric ones use
full-word suffixes (`.cap`, `.equator`, `.axis`, `.midpoint`, `.tip`).

| Suffix | Symbol | Name | Definition |
|--------|--------|------|------------|
| **.body** | L | lens body | The 3D overlap int(S₁) ∩ int(S₂). The lens itself |
| **.cap.<S_i>** | K_{S_i}(L) | lens cap | The piece of ∂L lying on ∂S_i. A lens has exactly two caps, one per parent sphere |
| **.equator** | E(L) | lens equator | The planar circle ∂S₁ ∩ ∂S₂. Lies in the perpendicular bisector of the segment C_{S₁}C_{S₂} |
| **.axis** | α(L) | lens axis | The line through C_{S₁} and C_{S₂} |
| **.midpoint** | m(L) | lens midpoint | The point at the centre of α(L); also the centre of E(L). For CO lenses at distance d=1, m(L) is at distance 1/2 from each parent centre. Coordinates already listed in §A.3 / §A.4 (these *are* the m(L) points) |
| **.tip.<S_i>** | T_{S_i}(L) | lens tip | One of the two points where α(L) meets ∂L. The tip on the S_i side is the diametrically opposite end of α(L) inside S_i's cap. For CO lenses, one tip is always the unit centre O |

Notes:
- For Λx⁺ specifically: K_Ω(Λx⁺) is the cap on ∂Ω; K_{X⁺}(Λx⁺) is the cap on ∂X⁺; T_Ω(Λx⁺) = O; T_{X⁺}(Λx⁺) = C_{X⁺}.
- The CO lens tip identity T_Ω(L) = O for every CO lens is the geometric basis for "the impulse origin is the limit-point of all six CO lenses simultaneously" (§8).

---

## TIER 3 — SHARED JUNCTION REGIONS

Where three spheres co-intersect, a shared sub-volume exists.
Label prefix: **Θ** (junction). These are the regions where
three pressure inputs meet and vortex dynamics negotiate.

### Three-sphere shared junctions (20 total)

**Type A — Central + polar + equatorial (8 regions):**
The central sphere participates alongside a polar and an
equatorial sphere. These are the active three-body junctions
where two driven inputs (Ω and Z±) meet one lateral neighbour.

| Label | Members |
|-------|---------|
| **Θ(Ω, Z⁺, X⁺)** | central + north + east |
| **Θ(Ω, Z⁺, X⁻)** | central + north + west |
| **Θ(Ω, Z⁺, Y⁺)** | central + north + front |
| **Θ(Ω, Z⁺, Y⁻)** | central + north + back |
| **Θ(Ω, Z⁻, X⁺)** | central + south + east |
| **Θ(Ω, Z⁻, X⁻)** | central + south + west |
| **Θ(Ω, Z⁻, Y⁺)** | central + south + front |
| **Θ(Ω, Z⁻, Y⁻)** | central + south + back |

**Type B — Central + 2 adjacent equatorials (4 regions):**
Central sphere meets two adjacent equatorial neighbours.
No polar involvement.

| Label | Members |
|-------|---------|
| **Θ(Ω, X⁺, Y⁺)** | central + east + front |
| **Θ(Ω, X⁺, Y⁻)** | central + east + back |
| **Θ(Ω, X⁻, Y⁺)** | central + west + front |
| **Θ(Ω, X⁻, Y⁻)** | central + west + back |

**Type C — Polar + 2 equatorials, no central (8 regions):**
Pure outer-sphere triple junctions. One per triangular face
of the outer octahedron. No central sphere involvement.

| Label | Members |
|-------|---------|
| **Θ(Z⁺, X⁺, Y⁺)** | north + east + front |
| **Θ(Z⁺, X⁺, Y⁻)** | north + east + back |
| **Θ(Z⁺, X⁻, Y⁺)** | north + west + front |
| **Θ(Z⁺, X⁻, Y⁻)** | north + west + back |
| **Θ(Z⁻, X⁺, Y⁺)** | south + east + front |
| **Θ(Z⁻, X⁺, Y⁻)** | south + east + back |
| **Θ(Z⁻, X⁻, Y⁺)** | south + west + front |
| **Θ(Z⁻, X⁻, Y⁻)** | south + west + back |

### Lens sub-regions (within each lens)

Every lens, regardless of type, has three internal sub-regions.
Use the parent lens label + suffix:

| Suffix | Sub-region | Description |
|--------|------------|-------------|
| **.c** | core | Deepest overlap; all parent spheres meet here; pressure integrator |
| **.a** / **.b** | lobes | One per parent sphere; dominated by that parent's pressure field |
| **.ab** | interface | Surface between two lobes; steepest pressure gradient; flow channel |

Example: **Λx⁺.c** = core of the east equatorial central-outer lens;
**Λx⁺.a** = the lobe inside Ω; **Λx⁺.b** = the lobe inside X⁺;
**Λx⁺.ab** = the interface between them (the gradient channel).

For three-body lenses, there are 3 lobes and 3 interfaces.
For two-body lenses, there are 2 lobes and 1 interface.

---

### 3D — Junction geometric primitives

For each junction Θ(S₁, ..., S_n), the following primitives are
defined in addition to the junction region itself. Reference
syntax for simulator: `Θ.<suffix>`.

| Suffix | Symbol | Name | Definition |
|--------|--------|------|------------|
| **.region** | Θ | junction region | The n-fold sphere overlap int(S₁) ∩ ... ∩ int(S_n), n ≥ 3. A 3D body. (This is the existing Tier 3 Θ object) |
| **.centroid** | centroid(Θ) | junction centroid | The centroid of the n sphere centres; a representative interior point of Θ. Coordinates already listed in §A.5 |
| **.node** | N(S₁,...,S_n) | junction node | A 0D point on ∂S₁ ∩ ... ∩ ∂S_n where one exists. Each 3-junction has **two** nodes (symmetric about the plane through the three sphere centres). 4-junctions have **no** all-boundary node in this geometry — the all-4-boundary system is over-determined |
| **.patch.<S_i>** | patch_{S_i}(Θ) | junction patch | The 2D piece of one ∂S_i that lies inside all the other n−1 spheres of the junction. The n patches together form ∂Θ |

### 3E — Lens junction: lens-side reading of Θ

The junction region Θ(S₁, ..., S_n) is equivalently the spatial
overlap of n−1 lenses sharing one common sphere. Use J(...) to
denote the lens-side reading; same body, two reading conventions.

| Sphere-side notation | Lens-side notation J | Common sphere |
|----------------------|----------------------|---------------|
| Θ(Ω, X⁺, Y⁺) | J(Λx⁺, Λy⁺) | Ω |
| Θ(Ω, Z⁺, X⁺) | J(Λz⁺, Λx⁺) | Ω |
| Θ(Z⁺, X⁺, Y⁺) | J(λ(z⁺,x⁺), λ(z⁺,y⁺)) | Z⁺ |

Use whichever reading is more natural in context. "Junction
region" emphasises the sphere-overlap; "lens junction"
emphasises the lens-overlap. They name the same body.

### 3F — Four-sphere junctions (provisional)

In this geometry, four spheres can co-intersect when they
comprise Ω plus one sphere from each axis-pair: Ω, X^a, Y^b, Z^c
for a, b, c ∈ {+, −}. Eight such regions exist (one per octant),
each a 3D body nested inside a Type-C 3-junction.

| Label | Symbol | Definition |
|-------|--------|------------|
| **Θ⁴(Ω, X^a, Y^b, Z^c)** | Θ⁴ | The 4-fold overlap int(Ω) ∩ int(X^a) ∩ int(Y^b) ∩ int(Z^c). Centroid at (a/4, b/4, c/4). No all-boundary node |

The 4-junctions are *provisional* in v3 — the existing convention
treats only 3-junctions as Θ. Promotion to a full tier (Tier 3F)
pending user review. They are included here because they are
genuine geometric primitives of the 7-sphere unit and the
pressure-impulse model's propagation analysis will need to address
them.

---

## TIER 4 — THE GREAT CIRCLES (4 GCs)

The four cuboctahedral hexagonal great circles.
Label prefix: **Γ**, subscript = the body-diagonal direction
each GC is **perpendicular to**.

| Label | Normal direction | Passes through these 6 OO lenses |
|-------|-----------------|----------------------------------|
| **Γ₁** | [+1,+1,+1] | λ(z⁻y⁺), λ(x⁻y⁺), λ(z⁺x⁻), λ(z⁺y⁻), λ(x⁺y⁻), λ(z⁻x⁺) |
| **Γ₂** | [+1,+1,−1] | λ(x⁻y⁺), λ(z⁺y⁺), λ(z⁺x⁺), λ(x⁺y⁻), λ(z⁻y⁻), λ(z⁻x⁻) |
| **Γ₃** | [+1,−1,+1] | λ(x⁺y⁺), λ(z⁺y⁺), λ(z⁺x⁻), λ(x⁻y⁻), λ(z⁻y⁻), λ(z⁻x⁺) |
| **Γ₄** | [−1,+1,+1] | λ(x⁻y⁻), λ(z⁺y⁻), λ(z⁺x⁺), λ(x⁺y⁺), λ(z⁻y⁺), λ(z⁻x⁻) |

*GC vertex order is the verified hexagonal ring sequence from the
geometry script. These labels use the display format (λ with
superscripts); the viewer brief's JavaScript arrays use the
code-safe id format (lzpxp etc.). Both refer to the same 12 lenses.
The brief's JavaScript IDs are authoritative for all code.*

**GC intersection lines:**
Each pair of GCs intersects along a line through 2 shared vertices.
Label: **Γᵢⱼ** for the intersection of GC i and GC j.

| Label | GC pair | Shared vertices |
|-------|---------|-----------------|
| **Γ₁₂** | Γ₁ ∩ Γ₂ | λ(z⁺x⁺) and λ(z⁻x⁻) |
| **Γ₁₃** | Γ₁ ∩ Γ₃ | λ(z⁺y⁻) and λ(z⁻y⁺) |
| **Γ₁₄** | Γ₁ ∩ Γ₄ | λ(z⁺x⁻) and λ(z⁻x⁺)* |
| **Γ₂₃** | Γ₂ ∩ Γ₃ | λ(x⁺y⁻) and λ(x⁻y⁺) |
| **Γ₂₄** | Γ₂ ∩ Γ₄ | λ(z⁺y⁺) and λ(z⁻y⁻) |
| **Γ₃₄** | Γ₃ ∩ Γ₄ | λ(z⁺x⁻) and λ(z⁻x⁺)* |

*GC intersection vertices are verified by the geometry script.
For code, use the GC_PATHS ring arrays in the viewer brief and
find shared IDs between any two rings to determine intersections.*

---

## TIER 5 — CUBOCTAHEDRAL FACES AND INTERNAL SUBSECTIONS

The 4 GC planes divide the interior of the cell into **14 volumetric
regions** corresponding to the 14 faces of the cuboctahedron.

### 5A — 8 Triangular-face regions (body-diagonal sectors)

Label: **R△** + signs of [x,y,z] in that sector.
Each aligns with one Type-C triple junction (Θ, polar + 2 eq).

| Label | Sector direction | Corresponding Θ junction |
|-------|-----------------|--------------------------|
| **R△₊₊₊** | [+x,+y,+z] | Θ(Z⁺, X⁺, Y⁺) |
| **R△₊₊₋** | [+x,+y,−z] | Θ(Z⁻, X⁺, Y⁺) |
| **R△₊₋₊** | [+x,−y,+z] | Θ(Z⁺, X⁺, Y⁻) |
| **R△₋₊₊** | [−x,+y,+z] | Θ(Z⁺, X⁻, Y⁺) |
| **R△₋₋₊** | [−x,−y,+z] | Θ(Z⁺, X⁻, Y⁻) |
| **R△₋₊₋** | [−x,+y,−z] | Θ(Z⁻, X⁻, Y⁺) |
| **R△₊₋₋** | [+x,−y,−z] | Θ(Z⁻, X⁺, Y⁻) |
| **R△₋₋₋** | [−x,−y,−z] | Θ(Z⁻, X⁻, Y⁻) |

### 5B — 6 Square-face regions (axis-aligned sectors)

Label: **R□** + axis. Each aligns with one outer sphere's
"territory" — the region of the cuboctahedron facing that sphere.

| Label | Faces toward | Outer sphere |
|-------|-------------|--------------|
| **R□z⁺** | +Z | Z⁺ |
| **R□z⁻** | −Z | Z⁻ |
| **R□x⁺** | +X | X⁺ |
| **R□x⁻** | −X | X⁻ |
| **R□y⁺** | +Y | Y⁺ |
| **R□y⁻** | −Y | Y⁻ |

---

## TIER 6 — CANONICAL PROJECTION VIEWS

### 6.0 — The cut-height principle

**A cut does not have to be taken at the obvious plane.**
The exact equatorial cut (Z=0) is the most symmetric but
the least dynamically active. An observer who genuinely
perceived the internal fluid dynamics would be drawn to
the zones of highest activity — steepest pressure gradients,
richest vortex structure, most complex triple-junction
negotiation — which are *not* at the planes of maximum
geometric symmetry.

**This means a Kells cut-view image may show a slice
displaced from the canonical plane.** The displacement
must be estimated and recorded during annotation.
Two images that both look like "4-fold" may be cuts at
different heights and reveal different component combinations
— and if the Kells imagery distinguishes them in a way
that corresponds to different cut-heights in the model,
that is a much stronger resonance than two identical cuts.

---

### 6.1 — The cut-height parameter

All planar cut views (Z, I, G) now carry a **cut-height
subscript** expressed as a percentage of cell radius from
the canonical plane. Positive = toward Z⁺, negative = toward Z⁻.

**Format: View Z₍ₕ₎ where h = height percentage**

Examples:
- **View Z₀** — exact equatorial plane. Maximum 4-fold symmetry,
  minimum dynamical activity. Least likely Kells choice.
- **View Z₃₀** — 30% above equator. Enters the Type-A triple
  junction band Θ(Ω, Z⁺, Eᵢ). Two driven inputs meet one
  passive neighbour. First appearance of 3-body pressure dynamics.
- **View Z₅₀** — 50% above equator. The λ-pe OO lens band.
  GC ring activity peaks here. Transition zone between
  equatorial 4-fold and polar 3-fold character.
- **View Z₇₅** — 75% above equator. Approaching Λz⁺ polar
  lens region. Three-fold structure begins to dominate.
  Axial poloidal throughflow mechanism replaces centrifugal.
- **View Z₁₀₀** — exactly through Z⁺ sphere centre. Pure
  polar face-on view. Single ring-vortex mode, not twin-vortex.

The same subscript applies to View I (displaced along the
[1,1,1] diagonal) and View G (displaced along the GC normal).

---

### 6.2 — Zone character by cut height

| Height band | Dominant components visible | Dynamic character | Symmetry |
|-------------|----------------------------|-------------------|----------|
| 0% (equator) | Ω, 4 equatorials, Λ-eq, λ-ee, Θ-B | Centrifugal, balanced twin vortices | 4-fold |
| 10–40% | Θ-A junctions enter, Λ-eq distorted | 3-body pressure negotiation active | 4-fold breaking |
| 40–60% | λ-pe lenses dominant, GC ring visible | GC ring vortex structure, transition | 3+4 mixed |
| 60–80% | λ-pe and Λz⁺ both present | Poloidal throughflow begins | 3-fold emerging |
| 80–100% (polar) | Z⁺, Λz⁺, λ-pe upper ring | Axial poloidal, single ring vortex | 3-fold |

**The most informationally rich zone is 30–50%.**
This is where:
- The Type-A triple junctions first activate (two driven + one passive)
- The concentric symmetry of the exact equatorial cut is broken
- The inner and outer vortex elements become *asymmetric*
- The distinction between the Ω-lobe and the Z⁺-lobe is visible

A Kells 4-fold image with a distinctly different centre and
an asymmetry between inner and outer elements is most
likely a **View Z₃₀ to Z₅₀** — not View Z₀.
This is the fingerprint of the Type-A junction zone and
is the hardest pattern to produce by coincidence.

---

### 6.3 — Non-axis-aligned cuts

A cut does not have to be parallel to any coordinate plane.
An observer perceiving the GC structure may have drawn a
cut *along* a GC plane rather than perpendicular to an axis,
producing a hexagonal cross-section through the lens ring
at an oblique angle to all coordinate axes.

Label oblique cuts as: **View O(Γₙ, h)** where Γₙ is the
GC the cut plane is parallel to and h is the displacement
from the GC plane centre along the GC normal.

---

### 6.4 — The four canonical views (now with height awareness)

#### View Z₍ₕ₎ — Top-down (Z-axis, variable height)

Looking down the Z axis at height h% above equator.

| At Z₀ (equator) | At Z₃₀₋₅₀ (active zone) |
|-----------------|--------------------------|
| Ω centred, symmetric | Ω offset or distorted |
| 4 equatorials equal | Equatorials asymmetric |
| Θ-B junctions | Θ-A junctions enter |
| Clean 4-fold | 4-fold with internal asymmetry |
| Twin vortex pairs equal | Twin vortex pairs unequal |

*Matches Kells 4-fold motifs. Prefer Z₃₀₋₅₀ as primary
candidate unless the image shows perfect concentric symmetry.*

#### View I₍ₕ₎ — Isometric ([1,1,1] body diagonal, 3-fold)

Looking along the Γ₁ normal. Shows 3-fold symmetry.
Displacement along [1,1,1] from centre changes which
triple junctions are prominent.

Visible at centre (h=0):
- One polar sphere face-on, 3 equatorials at 120°
- Three λ-pe lenses as hexagon sides
- Three R△ triangular regions
- Type-C Θ junctions at hexagon vertices
- Γ₁ as a regular hexagon in projection

*Matches Kells 3-fold / triskelion motifs.
Expected vortex signature: 3-fold pinwheel of Γ₁ ring vortices.*

#### View G₍ₕ₎ — Great-circle face-on (perpendicular to one Γ)

Perpendicular to one GC plane. Shows 6-fold symmetry.
Displacement along the GC normal shifts which sphere
interiors are cross-sectioned.

Visible at centre (h=0):
- 6 OO lens junctions as hexagon vertices
- 6 sphere pairs participating in this GC
- Central sphere Ω foreshortened at centre
- GC ring path connecting all 6
- Alternating F/M vortex pairs at each vertex

*Matches Kells 6-fold motifs.
Expected vortex signature: 6-vertex alternating F/M ring.*

#### View E — Edge-on (looking along one equatorial axis)

Looking directly at an equatorial sphere from outside.
Shows the vertical Z-column from the side.
Height parameter less relevant here — the column is visible
at all heights along the equatorial viewing axis.

Visible:
- Z⁺ at top, Ω at middle, Z⁻ at bottom
- The equatorial sphere face-on at front
- Y⁺ and Y⁻ partially visible left and right
- Λz⁺ and Λz⁻ polar lenses on the Z axis
- Λ-eq lens connecting Ω to the front equatorial sphere

*Matches Kells vertical-column / sophianic imagery.
The 3-sphere driver column reads as a vertical stack.*

---

## TIER 7 — FLUID DYNAMIC STATES

Label the dynamic states of the fluid in each region.
Use these as annotation overlays on the vortex structures.

| Label | Meaning |
|-------|---------|
| **F** | Left-handed (counter-clockwise) toroidal circulation |
| **M** | Right-handed (clockwise) toroidal circulation |
| **F+M** | Caduceus pair, both chiralities co-present (balanced) |
| **↑** | Axial upward throughflow (poloidal, polar lens) |
| **↓** | Axial downward throughflow (poloidal, polar lens) |
| **⊕** | High pressure zone (centrifugal, equatorial, s=R) |
| **⊖** | Low/reference pressure zone (axial, s≈0) |
| **∇P** | Pressure gradient (mark on interface sub-regions .ab) |
| **V_F** | Vortex core, F-chirality |
| **V_M** | Vortex core, M-chirality |
| **Δ** | Symmetry-breaking residual (the pump output term) |

### 7B — F/M as eigenmode pair (v3 clarification)

F and M are the two counter-rotating components of any
standing-wave interference pattern in U. They form a
complex-conjugate eigenmode pair, **not two distinct fluid
populations**. Their amplitudes are coupled.

| Label | Meaning |
|-------|---------|
| **gyrational coupling** | The F/M coupling channel: the inter-chirality electrostatic coupling, identified as the **ω₊·ω₋ cross-term** in the pressure source (the term in \|ω₊ + ω₋\|² beyond the two self-terms). This is the field-level form of the Tier 9 gyrator (§9G). Dominantly plasmic / electrostatic in character. *(v4: supersedes the provisional name "son".)* |

---

## TIER 8 — WAVE AND FIELD VARIABLES

Dynamical variables introduced by the pressure-impulse model of
the sphere unit. **Not directly highlightable as static geometric
objects** by the simulator, but used in annotation overlays on the
geometric elements of Tiers 1B–3 and in parametric highlights
(e.g. the wavefront W(t) at a specified time t).

| Label | Symbol | Definition |
|-------|--------|------------|
| **Impulse origin** | — | The dimensionless point of initial pressure delivery. In the canonical setup: the unit centre O |
| **Wavefront** | W(t) | Locus of constant phase of the propagating pressure wave at time t. For a point impulse at O, initially a sphere of radius r(t) about O |
| **Wavefront radius** | r(t) | Radius of W(t). Range: 0 → R inside Ω; transitions to neighbour sphere(s) at r = R |
| **Pressure field** | P(x, t) | Primary scalar dynamical variable |
| **Pressure differential** | ΔP | Pressure difference between two specified locations or ports |
| **Pressure field** | P(x, t) | Primary scalar dynamical variable. **Carries the capacitive storage directly** — there is no separate dielectric medium (v4). P is the electrostatic potential of the unified picture (φ = P; II-§7), and its source is ρ_eff |
| **Charge source** | ρ_eff | Effective charge density sourcing P via ∇²P = −ρ_eff (the pressure–Poisson / Gauss relation). Set by the vorticity, ρ_eff ∝ \|ω\|² (I-§2, II-§2). *(v4: this and P together replace the retired provisional field σ "dielectric density," which named no independent medium — capacitive storage is the pressure field itself.)* |
| **Flow** | Φ | Pressure-flow rate across a port; the **current analog** in the pressure-circuit picture, Φ ∝ J ∝ ∇×ω (II-§2). *(v4: de-provisionalised — confirmed as the current analog.)* |
| **Radial ray** | r̂ | A unit-vector direction from O along which the wavefront propagates |

---

## TIER 9 — NETWORK / CIRCUIT ELEMENTS

The pressure-impulse model is read as a linear network with
elements localised at the geometric primitives of Tiers 1B–3.
This tier names those elements.

| Label | Symbol | Definition | Geometric host |
|-------|--------|------------|----------------|
| **Capacitive gap** | g(r) | Radial separation between W at radius r and ∂Ω, along a specified direction. Radial model: g = R − r | Between W and ∂Ω |
| **Spherical capacitance** | C(r) | Capacitance between W at radius r and ∂Ω at radius R: C(r) = 4πε · r / (R − r). Diverges as r → R | int(Ω) |
| **Capacitive energy** | U_C | Energy stored at C(r), ΔP: U_C = ½ C(r) ΔP² | (scalar) |
| **Port** | — | Defined interface across which ΔP and Φ are measured. A lens has two ports (one per cap K); an n-junction has n ports (one per patch) | Lens caps; junction patches |
| **Two-port** | — | Network element with two ports. Canonical instance: a lens crossing | Per lens |
| **Multi-port** | — | Network element with ≥ 3 ports. Canonical instance: a junction | Per Θ |
| **Gyrator** | — | Linear **non-reciprocal** two-port satisfying Z_in = G² / Z_load. The C-to-L converter (L_eff = G²C). **[OPERATIONAL — v4]** — host is the **chiral traversal / local helicity** through the element, not the lens body or Θ region as such (derived in §9G) | Chiral (helicity-carrying) traversal of a lens/junction |
| **Gyrator coefficient** | G | The parameter of the gyrator; a **pseudoscalar** (flips sign under mirror reflection; opposite for the F and M chiralities). Set by the chiral gyration rate ω_c = 2⟨ω⟩ via G ~ 1/(ω_c C) (§9G) | Per gyrator instance |

---

## §9G — GYRATOR THEORY FROM CHIRALITY

*This section derives the Tier 9 gyrator, resolving its former [CONJECTURAL]
status. It is Layer I (operational dynamics of the model itself; no
Kells-correspondence claim). Cross-references: I-§ = Block I Foundations
v0.4, II-§ = Block II MHD Emergence v0.2.*

**What a gyrator is.** A gyrator is the one fundamental two-port that is
**non-reciprocal**: it satisfies Z_in = G²/Z_load, so a capacitance C on
its load port appears at its input as an **inductance** L_eff = G²C. It is
the canonical "capacitor-modelled inductor." Unlike resistors, capacitors,
and transformers — all reciprocal — a gyrator **requires broken
time-reversal / mirror symmetry** to exist at all. (This is why a physical
gyrator needs a magnetic bias or a rotating medium: something that
distinguishes one sense of circulation from the other.)

**The host is therefore the chirality.** The model already contains exactly
one ingredient that breaks mirror and time-reversal symmetry: the
**chirality** — the screw sense (I-§4, the ~45.8° golden twist) and the
conserved pseudoscalar helicity H = ∫ u·ω (I-§1). Nothing in the *reciprocal*
geometry (a lens body, a junction region) can host a gyrator; the
non-reciprocity must live in the **handedness of the traversal** through
that geometry. So:

> **The gyrator's host is the chiral (helicity-carrying) traversal of a
> lens or junction, and its coefficient G is a pseudoscalar.**

Concretely, G flips sign under mirror reflection and takes opposite sign
for the two counter-rotating chiralities F and M (Tier 7). A reflection
that exchanges F ↔ M sends G → −G — exactly the non-reciprocity a gyrator
demands. A mirror-symmetric (achiral) element has G = 0 and cannot gyrate.

**G is set by the chiral gyration rate.** At MHD scale the two chiralities
counter-gyrate at the cyclotron frequency ω_c = 2⟨ω⟩ (II-§5; equivalently
the Larmor rate ⟨ω⟩ equals the coarse-grained vorticity). Dimensionally the
gyrator coefficient that converts the local capacitance C into the matching
inductance is

$$G \sim \frac{1}{\omega_c\, C}, \qquad L_\text{eff} = G^2 C \sim \frac{1}{\omega_c^2\, C}.$$

So the gyration rate of the lumped network is the chiral counter-gyration
rate of the field — the same ω_c, read in circuit language.

**Why L = G²C is the two-projection structure in lumped form.** The model's
two field projections (I-§7) are: the **scalar/pressure** projection, which
stores energy electrostatically — this is the **capacitor** C (the spherical
capacitance C(r) = 4πε·r/(R−r) of Tier 9); and the **vector/vorticity**
projection, which stores energy magnetically — this is the **inductor** L.
The gyrator is what couples them, and the coupling agent is the chirality.
Thus:

| Lumped element | Field projection | Stores |
|----------------|------------------|--------|
| Capacitor C | scalar / pressure P (φ = P) | electrostatic energy ½C ΔP² |
| Inductor L | vector / vorticity ω (B = (2m/q)⟨ω⟩) | magnetic energy |
| **Gyrator G** | **chirality (helicity)** | converts one into the other (L = G²C) |

The "capacitor-modelled inductor" is then not a heuristic but the literal
statement that the magnetic (inductive) sector *is* the gyrated pressure
(capacitive) sector, with chirality as the gyration. This is the lumped-
network face of the unified Coulomb-gauge electrodynamics derived in II-§7.

**Field-level identification.** The gyrational coupling between the two
chiralities is the **ω₊·ω₋ cross-term** in the pressure source
\|ω₊ + ω₋\|² = \|ω₊\|² + \|ω₋\|² + 2 ω₊·ω₋ (II-§5). The two self-terms are
the individual capacitive stores; the cross-term 2 ω₊·ω₋ is the channel
through which they exchange — i.e. the gyrator, and the field-level name
for the Tier 7 "gyrational coupling" (formerly "son").

**Geometric placement in the cell.** The gyrator badge attaches wherever a
helicity-carrying traversal links a capacitive store to its neighbour: along
the **screw-threaded lens axes α(L)** and through the **junction patches**
where counter-rotating inputs meet (I-§13: constructive shared nodes are the
counter-rotating pairs). The CO-lens tip identity T_Ω(L) = O (Tier 2C) marks
where all six central-outer chiral traversals converge on the unit centre —
the natural common terminal of the cell's gyrator network.

**Status.** [OPERATIONAL]. The former candidates "lens-traversal" and
"junction-localised" are both partially right — the host is the *chiral
traversal* of either — but the load-bearing fact is that the host is the
**handedness**, not the region. G = 0 for any achiral element.

---

| Component type | Count | Label prefix |
|----------------|-------|--------------|
| Spheres | 7 | Ω, Z±, X±, Y± |
| Sphere boundaries ∂S | 7 | ∂Ω, ∂Z±, ∂X±, ∂Y± |
| Sphere centres C_S | 7 | C_Ω = O, C_Z±, C_X±, C_Y± |
| Sphere unit | 1 | U |
| Unit boundary | 1 | ∂U |
| Central-outer lenses | 6 | Λ |
| Outer-outer lenses | 12 | λ |
| Total lenses (bodies) | 18 | |
| Lens caps K | 36 | K_{S}(L), 2 per lens |
| Lens equators E | 18 | E(L), 1 per lens |
| Lens axes α | 18 | α(L), 1 per lens |
| Lens midpoints m | 18 | m(L); these are the points in §A.3/§A.4 |
| Lens tips T | 36 | T_{S}(L), 2 per lens; 12 of these coincide at O |
| Type-A triple junctions | 8 | Θ(Ω,Z,E) |
| Type-B triple junctions | 4 | Θ(Ω,E,E) |
| Type-C triple junctions | 8 | Θ(Z,E,E) |
| Total triple junctions Θ | 20 | Θ |
| Junction centroids | 20 | one per Θ; coordinates in §A.5 |
| Junction nodes N | 40 | 2 per 3-junction |
| Junction patches | 60 | 3 per 3-junction |
| Four-sphere junctions (prov.) | 8 | Θ⁴(Ω,X^a,Y^b,Z^c) |
| Great circles | 4 | Γ₁..₄ |
| GC intersection lines | 6 | Γᵢⱼ |
| Triangular internal sectors | 8 | R△ |
| Square internal sectors | 6 | R□ |
| Total internal sectors | 14 | R |
| Canonical view types | 4 | Z, I, G, E |
| Oblique GC-parallel views | 4 | O(Γₙ,h) |
| Cut-height parameter | continuous | subscript % |
| Most active annotation zone | — | Z₃₀ to Z₅₀ |
| **Wave/field variables (Tier 8)** | — | W, r, P, ρ_eff, ΔP, Φ, r̂ |
| **Network elements (Tier 9)** | — | g, C, U_C, port, gyrator (G), gyrational coupling |

---

## ANNOTATION PROTOCOL FOR KELLS IMAGES

1. Identify the **view type** first (Z / I / G / E / O) — record as **View: X**
2. Estimate the **cut height** — record as subscript percentage.
   Do not default to h=0. Ask: does the image show perfect concentric
   symmetry (→ Z₀) or internal asymmetry between centre and periphery
   (→ Z₃₀₋₅₀, the active zone)?
3. Mark the **central element** with its Tier 1 sphere label
4. Label **surrounding elements** consistently with same convention
5. Mark **lens regions** with Λ or λ + subscript
6. Overlay **vortex chirality** (F/M) where the miniature suggests rotation
7. Note any **Θ triple junctions** visible — Type A/B/C matters
8. Record **one non-matching element** per image to keep the
   falsification handle honest

**Active-zone priority:** images showing 4-fold patterns with
an asymmetric or distinctly different centre are *more likely*
to be View Z₃₀₋₅₀ (Type-A junction zone) than View Z₀ (exact
equator). Assign the more specific height first; only fall back
to Z₀ if the image shows genuinely perfect concentric symmetry.

*One labeling convention, applied consistently to every image.
Do not re-interpret the convention per image to improve local fit.
The awkward non-matching cases are the most diagnostic ones.*

---

*Document status: [OPERATIONAL] — labeling convention only,
no claims about which correspondences hold.
Correspondences are annotated separately and assessed per
the Layer I / Layer III firewall of §III.0.*

---

## APPENDIX A — HTML VIEWER SPECIFICATION

*This appendix contains all geometry data and interaction spec
needed for Claude Code to generate a self-contained HTML viewer.
Full implementation brief: see DCCREG_viewer_brief.md*

---

### A.1 — Coordinate system and geometry

All spheres have radius **r = 1.0**.
Outer sphere centers are at **d = 1.0** from origin (= r).
This gives CO lens half-angle = 60° (confirmed, matches framework).
OO center distance = √2 ≈ 1.414 < 2r → OO lenses exist.

**Axes:** X = east/west, Y = front/back, Z = vertical column axis.
Positive Z is toward Z⁺ (north, upper driver).

---

### A.2 — Sphere positions

```
Label   x      y      z     Role
------  -----  -----  -----  -------------------------
Ω       0.0    0.0    0.0   central (hub)
Z⁺      0.0    0.0    1.0   north polar (upper driver)
Z⁻      0.0    0.0   -1.0   south polar (lower driver)
X⁺      1.0    0.0    0.0   east equatorial
X⁻     -1.0    0.0    0.0   west equatorial
Y⁺      0.0    1.0    0.0   front equatorial
Y⁻      0.0   -1.0    0.0   back equatorial
```

---

### A.3 — Central-outer lens centers (6)

Midpoints between Ω and each outer sphere.

```
Label   x      y      z     Connects
------  -----  -----  -----  ---------
Λz⁺     0.0    0.0    0.5   Ω ↔ Z⁺
Λz⁻     0.0    0.0   -0.5   Ω ↔ Z⁻
Λx⁺     0.5    0.0    0.0   Ω ↔ X⁺
Λx⁻    -0.5    0.0    0.0   Ω ↔ X⁻
Λy⁺     0.0    0.5    0.0   Ω ↔ Y⁺
Λy⁻     0.0   -0.5    0.0   Ω ↔ Y⁻
```

---

### A.4 — Outer-outer lens centers (12)

Midpoints between adjacent outer sphere pairs.
These 12 points form a cuboctahedron. All coordinates
are permutations of (±0.5, ±0.5, 0).

```
Label           x      y      z     Connects
--------------  -----  -----  -----  -----------
λ(z⁺,x⁺)       0.5    0.0    0.5   Z⁺ ↔ X⁺
λ(z⁺,x⁻)      -0.5    0.0    0.5   Z⁺ ↔ X⁻
λ(z⁺,y⁺)       0.0    0.5    0.5   Z⁺ ↔ Y⁺
λ(z⁺,y⁻)       0.0   -0.5    0.5   Z⁺ ↔ Y⁻
λ(z⁻,x⁺)       0.5    0.0   -0.5   Z⁻ ↔ X⁺
λ(z⁻,x⁻)      -0.5    0.0   -0.5   Z⁻ ↔ X⁻
λ(z⁻,y⁺)       0.0    0.5   -0.5   Z⁻ ↔ Y⁺
λ(z⁻,y⁻)       0.0   -0.5   -0.5   Z⁻ ↔ Y⁻
λ(x⁺,y⁺)       0.5    0.5    0.0   X⁺ ↔ Y⁺
λ(x⁺,y⁻)       0.5   -0.5    0.0   X⁺ ↔ Y⁻
λ(x⁻,y⁺)      -0.5    0.5    0.0   X⁻ ↔ Y⁺
λ(x⁻,y⁻)      -0.5   -0.5    0.0   X⁻ ↔ Y⁻
```

---

### A.5 — Triple junction positions (20)

Centroids of three sphere centers.

**Type A — Ω + polar + equatorial (8):**
All have the form (±1/3, 0 or ±1/3, ±1/3).
Example: Θ(Ω,Z⁺,X⁺) = centroid of (0,0,0),(0,0,1),(1,0,0) = (0.333, 0, 0.333)

**Type B — Ω + 2 equatorials (4):**
Example: Θ(Ω,X⁺,Y⁺) = (0.333, 0.333, 0)

**Type C — polar + 2 equatorials (8):**
Example: Θ(Z⁺,X⁺,Y⁺) = (0.333, 0.333, 0.333)

*Full list: for each type, take all valid sign combinations
from the examples above.*

---

### A.6 — Great circle paths (4 GCs, 6 vertices each)

Each GC is the ordered set of OO lens centers lying in a plane
perpendicular to the given body diagonal.

```
GC    Normal      Ordered vertices (hexagonal ring)
----  ----------  -----------------------------------------
Γ₁   [+1,+1,+1]  λ(z⁻,y⁺) → λ(x⁻,y⁺) → λ(z⁺,x⁻) →
                  λ(z⁺,y⁻) → λ(x⁺,y⁻) → λ(z⁻,x⁺) → (repeat)

Γ₂   [+1,+1,−1]  λ(x⁻,y⁺) → λ(z⁺,y⁺) → λ(z⁺,x⁺) →
                  λ(x⁺,y⁻) → λ(z⁻,y⁻) → λ(z⁻,x⁻) → (repeat)

Γ₃   [+1,−1,+1]  λ(x⁺,y⁺) → λ(z⁺,y⁺) → λ(z⁺,x⁻) →
                  λ(x⁻,y⁻) → λ(z⁻,y⁻) → λ(z⁻,x⁺) → (repeat)

Γ₄   [−1,+1,+1]  λ(x⁻,y⁻) → λ(z⁺,y⁻) → λ(z⁺,x⁺) →
                  λ(x⁺,y⁺) → λ(z⁻,y⁺) → λ(z⁻,x⁻) → (repeat)
```

---

### A.7 — Slice cross-section geometry

A cut plane at height z=h intersects each sphere (center cx,cy,cz,
radius r=1.0) as a circle at screen position (cx,cy) with 2D radius:

```
r2d = sqrt(r² - (h - cz)²)   if |h - cz| ≤ r
r2d = 0                        otherwise (not visible)
```

**Verified cross-sections at key preset heights:**

```
h=0.0  (View Z₀, equatorial):
  Ω   at (0,0)  r2d=1.000    Z⁺ tangent point    Z⁻ tangent point
  X⁺  at (1,0)  r2d=1.000    X⁻ at (-1,0) r2d=1.000
  Y⁺  at (0,1)  r2d=1.000    Y⁻ at (0,-1) r2d=1.000

h=0.3  (View Z₃₀, Type-A junction zone):
  Ω   at (0,0)  r2d=0.954    Z⁺ at (0,0)  r2d=0.714
  X⁺  at (1,0)  r2d=0.954    X⁻,Y⁺,Y⁻ all r2d=0.954    Z⁻ not visible

h=0.5  (View Z₅₀, Λz⁺ lens plane, equal Ω/Z⁺ circles):
  Ω   at (0,0)  r2d=0.866    Z⁺ at (0,0)  r2d=0.866
  X⁺  at (1,0)  r2d=0.866    X⁻,Y⁺,Y⁻ all r2d=0.866    Z⁻ not visible

h=0.75 (View Z₇₅, Z⁺ dominates):
  Ω   at (0,0)  r2d=0.661    Z⁺ at (0,0)  r2d=0.968
  X⁺  at (1,0)  r2d=0.661    X⁻,Y⁺,Y⁻ all r2d=0.661    Z⁻ not visible

h=1.0  (View Z₁₀₀, polar face):
  Z⁺  at (0,0)  r2d=1.000    all others tangent or not visible
```

*Key diagnostic: at Z₃₀, Ω (r2d=0.954) and Z⁺ (r2d=0.714) are
DIFFERENT sizes at the SAME screen position (0,0). This asymmetry
is the Type-A junction zone signature: two driven circles of
unequal size nested concentrically at the column axis.*

---

### A.8 — Color encoding

```
Component          Hex color   Role
-----------------  ----------  ----------------------------
Ω central sphere   #9A78C9    purple
Z⁺ Z⁻ polar        #3FA9F5    blue
Equatorials X Y    #C2603A    coral
CO lenses Λ        #1D9E75    teal
OO lenses λ        #C99A3A    amber
Type-A junctions   #E07A4A    orange (high activity)
Type-B junctions   #7fa3a8    muted teal
Type-C junctions   #dfeef0    pale (outer only)
GC ring paths      #FFFFFF    white (at 40% opacity)
Slice plane        #FFFFFF    white (at 10% opacity)
F vortex           #1D9E75    teal (left-hand)
M vortex           #C2603A    coral (right-hand)
Background         #0d1b1e    dark teal-black
```

---

### A.9 — Preset view parameters

```
Preset     Camera position    Look-at   Slice z  Notes
---------  -----------------  --------  -------  ----------------------
View Z₀    (0, 0, 5)          (0,0,0)   z=0.0    exact equatorial
View Z₃₀   (0, 0, 5)          (0,0,0)   z=0.3    Type-A junction zone
View Z₅₀   (0, 0, 5)          (0,0,0)   z=0.5    Λz⁺ lens plane
View Z₇₅   (0, 0, 5)          (0,0,0)   z=0.75   polar approach
View Z₁₀₀  (0, 0, 5)          (0,0,0)   z=1.0    Z⁺ polar face
View I     (2.5, 2.5, 2.5)   (0,0,0)   none     isometric [1,1,1]
View G1    GC1 normal×5      (0,0,0)   none     GC Γ₁ face-on
View E     (5, 0, 0)          (0,0,0)   none     edge-on, Z-column side
```

---

### A.10 — Zone character panel content

At each slice height the viewer should show a text panel:

```
h=0%   "View Z₀ — Exact equatorial. Maximum 4-fold symmetry.
         Minimum dynamic activity. Components: Ω, X±, Y±, Λ-eq, λ-ee, Θ-B"

h=30%  "View Z₃₀ — Type-A junction zone. Two driven inputs (Ω, Z⁺)
         meet passive equatorials. MOST ACTIVE ZONE.
         Key: Ω circle (r=0.954) and Z⁺ circle (r=0.714) nested at origin.
         Components: Θ(Ω,Z⁺,Eᵢ), Λ-eq distorting, λ-pe entering"

h=50%  "View Z₅₀ — Λz⁺ lens plane. Ω and Z⁺ produce equal circles.
         GC ring activity peaks. Transition zone.
         Components: Λz⁺ at centre, λ-pe dominant"

h=75%  "View Z₇₅ — Polar approach. Z⁺ dominates (r=0.968 vs Ω r=0.661).
         Axial poloidal throughflow mechanism active. 3-fold emerging.
         Components: Λz⁺, λ-pe upper ring"

h=100% "View Z₁₀₀ — Z⁺ polar face. Single ring-vortex mode.
         Centrifugal drive absent (s≈0). Axial only.
         Components: Z⁺ full circle, all others tangent or absent"
```

---

## APPENDIX B — SIMULATOR HIGHLIGHT SPECIFICATION

*This appendix is the data source for the 3D simulator highlight
add-on. Each row defines one highlightable geometric object,
its checkbox-tree path, its geometric class, and the geometric
data needed to render the highlight. Rows are grouped by Tier
for the UI checkbox hierarchy.*

---

### B.1 — Checkbox tree (UI hierarchy)

```
[ ] Tier 1 — Spheres
    [ ] Ω         (sphere; centre, radius)
    [ ] X⁺, X⁻, Y⁺, Y⁻, Z⁺, Z⁻
[ ] Tier 1B — Sphere primitive elements
    [ ] S.interior    (filled volume)
    [ ] S.boundary    (∂S, surface)
    [ ] S.centre      (point C_S)
[ ] Tier 1C — Sphere unit composite
    [ ] U             (full 7-sphere assembly)
    [ ] O             (unit centre point)
    [ ] ∂U            (outer envelope)
[ ] Tier 2A — Central-outer lenses Λ
    [ ] Λz⁺, Λz⁻, Λx⁺, Λx⁻, Λy⁺, Λy⁻
[ ] Tier 2B — Outer-outer lenses λ
    [ ] λ-pe (8 lenses)
    [ ] λ-ee (4 lenses)
[ ] Tier 2C — Lens geometric primitives (per lens)
    [ ] L.body        (3D overlap)
    [ ] L.cap.<S>     (spherical caps, 2 per lens)
    [ ] L.equator     (boundary circle E)
    [ ] L.axis        (line α)
    [ ] L.midpoint    (point m)
    [ ] L.tip.<S>     (axis endpoints, 2 per lens)
[ ] Tier 3 — Junction regions Θ
    [ ] Type A (8), Type B (4), Type C (8)
    [ ] Lens sub-regions (.c / .a / .b / .ab — pressure character)
[ ] Tier 3D — Junction geometric primitives (per junction)
    [ ] Θ.region      (3D overlap body)
    [ ] Θ.centroid    (representative point)
    [ ] Θ.node.<idx>  (boundary nodes N, 2 per 3-junction)
    [ ] Θ.patch.<S>   (boundary patches, n per n-junction)
[ ] Tier 3F — Four-sphere junctions (provisional)
    [ ] Θ⁴(Ω,X^a,Y^b,Z^c) × 8
[ ] Tier 4 — Great circles Γ
    [ ] Γ₁, Γ₂, Γ₃, Γ₄
    [ ] Γᵢⱼ intersection lines (6)
[ ] Tier 5 — Internal sectors R
    [ ] R△ (8 triangular)
    [ ] R□ (6 square)
[ ] Tier 6 — View overlays (camera + cut planes)
    [ ] Z₍ₕ₎, I₍ₕ₎, G₍ₕ₎, E, O(Γₙ, h)
[ ] Tier 7 — Vortex / dynamic state overlays
    [ ] F, M, F+M, ↑, ↓, ⊕, ⊖, ∇P, V_F, V_M, Δ
[ ] Tier 8 — Wave field overlays (parametric)
    [ ] W(t)           (sphere at parametric radius)
    [ ] r̂ (radial ray) (chosen direction)
[ ] Tier 9 — Network element badges
    [ ] Port markers at lens caps and junction patches
    [ ] Gyrator markers (on chiral traversals: screw-threaded lens axes α(L), counter-rotating junction patches)
```

---

### B.2 — Master highlight table

*Geometric class column tells the simulator the render type:*
- **point** = render as a sphere marker
- **line** = render as a thin tube along the segment
- **curve** = render as a thin tube along the curve
- **surface** = render as a transparent 2D surface patch
- **volume** = render as a translucent 3D body
- **annotation** = render as a label/icon attached to a host object

| Tier | Object | Symbol | Class | Render hint |
|------|--------|--------|-------|-------------|
| 1 | Sphere | Ω, X±, Y±, Z± | volume | translucent ball, centre + radius |
| 1B | Sphere boundary | ∂S | surface | full 2-sphere shell |
| 1B | Sphere interior | int(S) | volume | filled ball (rarely highlighted alone) |
| 1B | Sphere centre | C_S | point | small sphere marker at C_S |
| 1C | Sphere unit | U | volume | union of all 7 sphere bodies |
| 1C | Unit centre | O | point | distinguished marker at origin |
| 1C | Unit boundary | ∂U | surface | outer envelope (6 spherical caps) |
| 2A/2B | Lens body | L | volume | translucent vesica solid |
| 2C | Lens cap | K_{S}(L) | surface | spherical cap on ∂S inside the other sphere |
| 2C | Lens equator | E(L) | curve | planar circle in perpendicular bisector |
| 2C | Lens axis | α(L) | line | segment between two sphere centres |
| 2C | Lens midpoint | m(L) | point | small marker; same as §A.3/§A.4 coords |
| 2C | Lens tip | T_{S}(L) | point | endpoint of α(L); CO-lens inner tip = O |
| 3 | Junction region | Θ | volume | translucent 3-sphere or 4-sphere overlap |
| 3D | Junction centroid | centroid(Θ) | point | marker at the n-sphere-centre centroid |
| 3D | Junction node | N | point | 0D point on all n boundaries (3-junctions only) |
| 3D | Junction patch | patch_{S}(Θ) | surface | piece of ∂S inside the other n−1 spheres |
| 3F | 4-sphere junction | Θ⁴ | volume | translucent 4-fold overlap (prov.) |
| 4 | Great circle | Γₙ | curve | hexagonal ring through 6 OO lens midpoints |
| 4 | GC intersection line | Γᵢⱼ | line | segment between 2 shared OO midpoints |
| 5 | Internal sector | R△, R□ | volume | translucent cuboctahedral region |
| 6 | View | Z₍ₕ₎ etc. | camera | sets camera + optional cut plane |
| 7 | Vortex state | F, M, etc. | annotation | small chirality icon at host |
| 8 | Wavefront | W(t) | surface | sphere of radius r(t); parametric on t |
| 8 | Radial ray | r̂ | line | ray from O in chosen direction |
| 9 | Port | — | annotation | small port marker at lens cap or Θ patch |
| 9 | Gyrator | G | annotation | gyrator icon on a chiral traversal (lens axis α / junction patch); pseudoscalar sign by F/M |

---

### B.3 — Notes for simulator implementation

1. **Geometric primitives in Tier 1B–3D are fully derived** from the
   sphere positions in §A.2. The simulator does not need any
   additional coordinate data beyond what §A.2 through §A.6 already
   provide — every primitive can be computed from sphere centres
   and radii.

2. **Coordinate aliasing.** The lens midpoint m(L) is the same
   point as the lens centre in §A.3 and §A.4. The junction centroid
   is the same point as the triple-junction centroid in §A.5. The
   v3 nomenclature does not introduce new coordinates; it names
   primitives that were already implicit.

3. **Sub-region coexistence.** A single lens has both a geometric
   primitive set (Tier 2C: .body, .cap, .equator, .axis, .midpoint,
   .tip) and a pressure-character sub-region set (Tier 3 existing:
   .c, .a, .b, .ab). These can be highlighted independently; the
   UI should group them as sibling sub-folders under each lens.

4. **Tier 8 / 9 parametric items.** Wavefront W(t) and the radial ray
   require parameter sliders (t for wavefront, direction for radial ray).
   The gyrator badge attaches to chiral traversals (lens axes α / junction
   patches) with a pseudoscalar sign taken from the host's F/M chirality;
   no host-selection slider is needed (v4). The other items are static
   highlights from sphere geometry alone.

5. **Provisional items (v4 update).** Of the items flagged provisional in
   v3, three are now resolved and should be enabled by default: the gyrator
   (G) and its gyrational coupling (now [OPERATIONAL], §9G), the flow Φ
   (confirmed as the current analog), and the field formerly called σ
   "dielectric density" (retired — capacitive storage is the pressure field
   P, source ρ_eff). **Only the four-sphere junctions Θ⁴ remain
   *provisional*** and should stay behind a feature flag, disabled by
   default, until their geometry is confirmed.

6. **Documentation image generation.** For each view in Tier 6,
   the simulator should support an "export current highlight set
   to SVG" function. The active highlight set defines the
   annotation layer; the camera defines the projection; the
   resulting SVG carries enough information to be re-rendered
   identically by the convention-following labeling.

---

*Document status: [OPERATIONAL — v4]. Labeling convention plus
simulator highlight specification, with the Tier 9 gyrator now derived
from chirality (§9G) and three provisional names retired. No claims about
which Kells correspondences hold. Correspondences remain annotated
separately per the Layer I / Layer III firewall.*
