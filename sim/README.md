# DCCREG Simulator — Target Specification

**Read `../CLAUDE.md` first.** This file specifies *what to compute*; CLAUDE.md specifies *how to behave while doing it* (firewall, reproducibility, no fabricated numbers).

---

## The single target — the SOSF defect spectrum

The gravity gate (Block IV) and the matter gate (Block V) were **joined** (IV-§3a ↔ V-§2a/§9): both reduce to one object, the **spectrum of stable localised topological defects of the hexatic SOSF**. Computing it turns Block IV's parametric coefficient into a number AND fixes Block V's ground-state matter content.

### Already computed analytically (do NOT re-derive; validate against these)
- **Charges** = conjugacy classes of the chiral octahedral group O: Frank angles **{90°, 120°, 180°}** (+ identity); 120° is the screw-aligned ($C_3$ about [1,1,1]). [OC]
- **Coupling** K_A ~ β ~ ρΓ²·ln(d/a) — Block III's line tension; shared with light isotropy ($\beta=\alpha$ at ln(d/a)≈4) and gravity strength ($G_\text{eff}\sim 1/K_A$). [OC scaling / IR]
- **Spin-parity selection** is Fibonacci: the irrational screw framing (45.8° = 120°/φ² per level) closes only via writhe; near-closure loops sit at Fibonacci depths (1,2,3,5,8,13,21). [OC arithmetic / IR-RH reading]

### Open — what the simulator must produce
1. **Stable-loop energies.** Which closed disclination loops and linked/knotted vortex loops are stable on the hexatic SOSF, and their energies. → the defect spectrum.
2. **Ground-state matter loop.** The lowest-energy stable loop, with its **exact spin parity** (framing self-linking mod 2 → is it spin-½?) and **handedness** (screw sense).
3. **Numeric K_A.** The Frank constant / disclination interaction coefficient from the **lattice Biot–Savart sum** — turning the parametric $K_A\sim\beta$ into a number, hence $G_\text{eff}$.

The [1,1,1] screw makes the operative problem **quasi-2D** (the transverse-to-screw plane); exploit this for tractability before attempting full 3D.

---

## Validation ladder (build trust before claiming new results)

Reproduce the known limits first; each is a regression test.

1. **SOSF geometry.** Build the septenary octahedral sphere-flake from `docs/DCCREG_labeling_convention_v4.md` (Appendix A has exact coordinates, the 7 spheres, lenses, junctions, great circles). Reproduce the verified cross-sections (§A.7) as a geometry self-test.
2. **Solid confinement.** Recover the ordinary-elasticity disclination interaction ~ **r² ln r** (1/k⁴) in the *unmelted* limit — the rigid-skeleton baseline (IV-§5.5).
3. **Hexatic screening / Green's function.** Reproduce the v0.6 closure check: the hexatic disclination kernel is the 2D Laplacian Green's function, i.e. ∫_disk ∇²(ln r /2π) dA = **1.000** (IV-§5.5, §3a). This is the Einstein/Newtonian-form confirmation; it must come out before any new number is trusted.
4. **Călugăreanu bookkeeping.** For a screw-framed loop, verify Lk = Tw + Wr and that a planar loop has Wr≈0 with the screw supplying integer Tw (V-§3) — the framing self-test.
5. **Octahedral charges.** Regenerate the chiral octahedral group O (24 det-+1 signed permutation matrices) and confirm the Frank-angle classes {90,120,180}° (V-§2a) — a pure group-theory unit test.

Only after 1–5 pass should runs targeting items 1–3 of the open list be treated as load-bearing.

---

## Outputs (per CLAUDE.md §5)

Each run writes to `../results/<run-id>/`:
- `params.json` — all parameters + git commit hash + seed.
- `data.{json,csv}` — the numeric results (energies, K_A value, Lk/spin parity, charges).
- `figures/` — plots (spectrum, interaction-vs-r log-log, Green's-function check).
- `NOTES.md` — short interpretation, **every claim tagged [OC]/[IR]/[RH]**, with explicit statement of what is and isn't established by the run.

A number is reportable only with its reproducibility log. **A missing number is acceptable; an invented one is a firewall breach.**

---

## Graduation back to the Blocks

Numbers do not edit Blocks directly. When a result converges and passes validation, a **consolidation session** (chat or Claude Code) updates the relevant Block via the standard step (CLAUDE.md §3.3/§3.4): bump the version, add a revision-history row, move the prior version to `docs/archive/`, update cross-references (IV-§3a ↔ V-§2a/§9), and move the superseded parametric statement to a History note. Tag the new number's tier.

Suggested first deliverables that would graduate:
- numeric **K_A → G_eff** ⇒ Block IV v0.8 ("K_A computed");
- **ground-state matter loop** (spin parity + handedness) ⇒ Block V v0.3 ("matter ground state");
- both share one run, as the joining intends.
