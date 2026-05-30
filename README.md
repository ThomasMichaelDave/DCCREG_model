# DCCREG

An exploratory, internally-disciplined theoretical-physics construction: deriving electromagnetism, magnetohydrodynamics, light, gravity, and matter as **emergent** phenomena of a hypothetical sub-Planck **chiral fluid substrate**.

> **This is a "what-if" model-building programme, not established physics.** Its value is its epistemic discipline (the OC/IR/RH firewall) and its honest, versioned audit trail — not a claim to be true. Read `CLAUDE.md` and `docs/DCCREG_programme_README.md` before contributing.

---

## Start here

1. **`CLAUDE.md`** — the operating discipline (firewall, workflow, simulator target). Auto-read by Claude Code. Read it first.
2. **`docs/DCCREG_programme_README.md`** — the physics master handoff and document map.
3. **Blocks I → V** (in `docs/`) — the derivation, in order.

---

## Layout

```
dccreg/
├── CLAUDE.md                ← operating discipline (firewall + workflow); read first
├── README.md                ← this file
├── docs/                    ← the programme (live current versions)
│   ├── DCCREG_programme_README.md            master handoff / map
│   ├── DCCREG_fluid_substrate_foundations_v04.md   Block I  — substrate
│   ├── DCCREG_MHD_emergence_v02.md                 Block II — MHD/EM
│   ├── DCCREG_radiative_EM_emergent_LI_v02.md      Block III— light / Lorentz
│   ├── DCCREG_emergent_gravity_v07.md              Block IV — gravity
│   ├── DCCREG_emergent_matter_v02.md               Block V  — matter / fermions
│   ├── DCCREG_labeling_convention_v4.md            7-sphere labeling + sim spec
│   ├── DCCREG_sandbox_v01.md                        sandbox (RH, parallel track)
│   └── archive/             ← superseded versions (audit trail — do not delete)
├── sim/                     ← simulator code (Claude Code's domain)
│   └── README.md            ← the simulator target spec
└── results/                 ← numeric outputs, figures, run logs (data, not prose)
```

---

## The two tracks (see CLAUDE.md §3)

- **Main track** — Blocks, convergent forks, simulator. Disciplined [OC]/[IR].
- **Sandbox track** — `docs/DCCREG_sandbox_v01.md` only. [RH] speculation, sealed behind a **one-way graduation valve**: nothing enters a Block until it earns [OC]/[IR]. Blocks never cite the sandbox.

Both can run as **separate conversations / sessions** in parallel. The graduation queue (in the sandbox) is the only channel between them, and it flows one way.

---

## Current state

Substrate → EM → MHD → light established at their stated tiers. **Gravity** (Block IV) computes to the Einstein/Newtonian 1/k² form (conditional on the hexatic identification); **matter** (Block V) realises spin-½ + automatic spin-statistics + Weyl handedness (fenced from "these are real particles"). The two gates are **joined**: they share one object — the SOSF defect spectrum — whose analytic pieces are computed (octahedral charges; coupling K_A ~ β; Fibonacci spin-selection) and whose **numeric** pieces are the simulator's job (`sim/README.md`).

## Tooling

- **Claude Code** (terminal agent) owns `sim/` and `results/` — building and running the simulator, committing to git.
- **Chat / consolidation sessions** own block consolidation — turning converged numbers into versioned block updates through the firewall.
- No frontend/IDE required; a terminal + this repo + the GitHub connection is sufficient.

*Programme status: exploratory, internally consistent, falsifiable at the frontier.*
