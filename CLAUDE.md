# CLAUDE.md — Standing instructions for the DCCREG repository

**Read this file fully before doing anything in this repo.** It is the contract. It applies to every assistant instance (Claude Code or chat) working here.

---

## 0. What this repo is

An exploratory, internally-disciplined theoretical-physics construction: deriving EM, MHD, light, gravity, and matter as *emergent* phenomena of a hypothetical sub-Planck **chiral fluid substrate** (DCCREG). It is a "what-if" model-building programme, **not** established physics. Its integrity comes from an explicit epistemic firewall and honest, versioned consolidation — not from being true.

Start by reading `docs/DCCREG_programme_README.md`, then Blocks I → V. That README is the master handoff; this file is the *operating discipline* layered on top of it.

---

## 1. THE FIREWALL — non-negotiable, applies to every output

Every substantive claim carries exactly one tag:

- **[OC] Operational Core** — standard, derivable physics/mathematics; true independent of the framework.
- **[IR] Interpretive Reading** — a modeling identification *within* the framework; internally consistent, chosen not forced.
- **[RH] Resonance / Heuristic** — analogical/cosmological; suggestive, not load-bearing.

Rules:
1. **Never let [RH] drift into [OC].** This is the single most important rule. The programme's entire value is the firewall; collapsing it destroys the work.
2. **Non-GR / non-standard results are not failures.** Divergence from established physics is *empirical content* to be quantified, not apologised for and not waved through. But quantify it — the divergences are tightly bounded by experiment.
3. **Correct openly when rigor demands.** Superseded values stay in "History" notes; the audit trail is the point. (Precedents: screw angle 137.5°→45.8°; fractal dim 2.807→2.0; the Block IV Fierz–Pauli mass-term correction in v0.2→v0.3.)
4. **The user prizes honest pushback and self-correction over validation.** Say what is weak. Flag what is unestablished. Do not inflate a result to please.
5. **If a computation's interpretation turns out wrong, withdraw it explicitly** (precedent: the v0.6 screening-crossover line was withdrawn while the power-law result stood).

---

## 2. LOCKED ASSUMPTIONS — do **not** "fix" these

The substrate is an **ideal, incompressible, lossless Euler fluid** with **infinite sound speed** (instantaneous pressure), structured to the **Planck length** ℓ_P, intrinsically **chiral**, plasma-like under rotative agitation, MHD-like at higher scale.

1. **Infinite sound speed is intentional** — the incompressible limit; do real work with it (instantaneous Coulomb sector; khronon foliation). Do not try to make it finite.
2. **Losslessness ⇒ helicity is the ground philosophy.** H = ∫u·ω dV is a conserved pseudoscalar; mirror/dual character is inherent.
3. **Screw sense fixes global helicity ("DC handedness"); helicity density u·ω varies pointwise.**

---

## 3. WORKFLOW — how work moves through this repo

### 3.1 The two tracks
- **Main track** — owns the numbered Blocks (`docs/DCCREG_*Block*`), the convergent forks, and the simulator (`sim/`, `results/`). Disciplined, [OC]/[IR] load-bearing.
- **Parallel/sandbox track** — owns `docs/DCCREG_sandbox_v01.md` only. [RH]-dominant speculation. **The sandbox is never cited by a Block.**

### 3.2 The one-way graduation valve
Nothing crosses from the sandbox (or from speculation generally) into a numbered Block until it independently earns [OC] or [IR]. A speculation may *inspire* a computation; the Block records only what the computation establishes. **Blocks cite Blocks; the sandbox cites nothing load-bearing.**

### 3.3 Derive → consolidate
Derive/compute a coherent frame first; **then** consolidate into a versioned `.md` with a revision-history table row documenting what changed and why. Each handed-back block gets a new version number. Never silently overwrite — bump the version and log the change.

### 3.4 Doc edit discipline
- `docs/` holds the **live** current versions; `docs/archive/` holds **superseded** versions (audit trail — do not delete).
- When consolidating a new block version: write the new file in `docs/`, move the prior version to `docs/archive/`, update the cross-references and the README map.
- **Cross-reference scheme:** `I-§ II-§ III-§ IV-§ V-§` between blocks; `S-§` inside the sandbox. Keep cross-refs bidirectional when two blocks share an object (e.g. IV-§3a ↔ V-§2a/§9, the joining).

### 3.5 Simulator → Blocks
`sim/` results are **numbers**, not claims. A numeric result graduates into a Block only via the consolidation step (3.3), through the firewall (3.2): the Block records the computed value with its tier, and the prior parametric/conditional statement is updated, not erased (it moves to History).

---

## 4. THE CURRENT FRONTIER — what to compute

The two open gates (gravity, matter) have been **joined into one object**: the **stable-defect spectrum of the hexatic SOSF**. See `sim/README.md` for the full target spec. In short:

- **Computed already (analytic, no simulator):** matter charges = chiral octahedral group O ({90°,120°,180°}); coupling K_A ~ β ~ ρΓ²ln(d/a) (= Block III line tension, shared with light isotropy and gravity strength); Fibonacci spin-parity selection. (IV-§3a, V-§2a, V-§6a.)
- **Open (this is the simulator's job):** which disclination / linked-vortex loops are **stable** (energies); the **lowest-energy** matter loop's exact **spin parity & handedness**; the **precise numeric K_A** (lattice Biot–Savart sum). The [1,1,1] screw makes the relevant problem **quasi-2D** (transverse-to-screw).

Closing this single computation turns the parametric gravity coefficient into a number AND fixes the ground-state matter content — both gates at once.

Other carried forks (authoritative lists in each block's own "Open forks"): α₂ at the instantaneous-khronon limit (IV); energy→softening sign (IV); PPN γ (IV); dynamic-vs-static shear for light (IV/III); soliton quantisation and mass mechanism (V).

---

## 5. CODING CONVENTIONS (for `sim/`)

- Python; `numpy`/`scipy` baseline. Keep dependencies minimal and declared in `sim/requirements.txt`.
- **Every run is reproducible:** fixed random seeds; log parameters + git commit hash with each result into `results/`.
- **Results are data, not prose.** Write numeric outputs (JSON/CSV) + figures to `results/`; keep interpretation in a short `results/<run>/NOTES.md` that tags every claim [OC]/[IR]/[RH].
- **Do not fabricate numbers.** If a quantity needs a run that hasn't converged or isn't implemented, say so and leave it unfilled. A missing number is fine; an invented one is a firewall breach.
- Validate against known limits where possible (e.g. recover the solid r²ln r confinement before claiming the hexatic ln r screening; reproduce the v0.6 Green's-function check ∫∇²(ln r/2π)=1).
- Small, composable scripts over monoliths. One script per computable target.

---

## 6. WHAT NOT TO DO

- Do not edit `docs/` blocks except via the consolidation step (3.3/3.4).
- Do not import sandbox speculation into a Block (3.2).
- Do not present a simulator number as established without its tier and its reproducibility log.
- Do not soften or drop a known weakness to make the programme look more finished than it is.
- Do not treat "this isn't standard physics" as either an error to hide or a license to overclaim.

---

*This file is the operating discipline. The physics handoff is `docs/DCCREG_programme_README.md`. If the two ever conflict, the README's block-level "Open forks" sections are authoritative for physics scope; this file is authoritative for process and the firewall.*
