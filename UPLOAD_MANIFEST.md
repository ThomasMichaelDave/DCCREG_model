# DCCREG Repo Bundle — Upload Manifest & Quick-Start

This is your checklist for getting the repo onto GitHub and starting the parallel simulator work. Everything below is in the `dccreg/` folder of the bundle.

> **Historical note (original bundle manifest).** The repo is long since on GitHub and the simulator work has advanced through **run005**; this file is retained as the initial-upload record. For current state see `README.md`, `docs/DCCREG_programme_README.md`, and `results/MASTER_CONSOLIDATION_INDEX.md`. The live-version entries below have been updated to match the repo.

---

## What's in the bundle (upload all of it)

### Root
| File | What it is | Status |
|------|-----------|--------|
| `CLAUDE.md` | **Operating discipline** — firewall + workflow + simulator target. Claude Code reads this automatically. The discipline's permanent home. | NEW |
| `README.md` | Top-level repo orientation and layout. | NEW |
| `.gitignore` | Standard Python/OS ignores. | NEW |

### docs/ — the programme (live current versions)
| File | Block | Version |
|------|-------|---------|
| `docs/DCCREG_programme_README.md` | Master handoff / map | v1.7 |
| `docs/DCCREG_fluid_substrate_foundations_v04.md` | Block I — substrate | v0.4 |
| `docs/DCCREG_MHD_emergence_v02.md` | Block II — MHD/EM | v0.2 |
| `docs/DCCREG_radiative_EM_emergent_LI_v02.md` | Block III — light / Lorentz | v0.2 |
| `docs/DCCREG_emergent_gravity_v09.md` | Block IV — gravity | v0.9 |
| `docs/DCCREG_emergent_matter_v06.md` | Block V — matter / fermions | v0.6 |
| `docs/DCCREG_labeling_convention_v4.md` | 7-sphere labeling + sim geometry spec | v4 |
| `docs/DCCREG_sandbox_v01.md` | Sandbox (RH, parallel track) | v0.1 |

### docs/archive/ — superseded versions (audit trail; keep, don't delete)
- `DCCREG_emergent_gravity_v01.md` … `v08.md` (8 files)
- `DCCREG_emergent_matter_v01.md` … `v05.md` (5 files)

### sim/ — simulator (Claude Code's domain)
| File | What it is |
|------|-----------|
| `sim/README.md` | **Simulator target spec** — the single defect-spectrum computation, validation ladder, output format. | NEW |
| `sim/requirements.txt` | Python deps (numpy/scipy/matplotlib). | NEW |
| `sim/.gitkeep` | Placeholder so the dir exists. | NEW |

### sim/checks/ — verification scripts (the [OC] pieces already computed)
| File | What it checks |
|------|---------------|
| `sim/checks/README.md` | Scope + honesty framing for the scripts. | NEW |
| `sim/checks/check_01_calugareanu_framing.py` (+ `.out.txt`) | Screw framing ⇒ ribbon; Lk=Tw+Wr (V-§3). | NEW |
| `sim/checks/check_02_hexatic_greens_function.py` (+ `.out.txt`) | Hexatic kernel = Laplacian Green's fn (∫∇²(ln r/2π)=1) ⇒ Einstein form (IV-§5.5/§3a). Contains a fenced WITHDRAWN block (audit trail). | NEW |
| `sim/checks/check_03_joining_spectrum.py` (+ `.out.txt`) | Octahedral charges; K_A~β; Fibonacci spin-parity (IV-§3a, V-§2a/§6a). | NEW |

> These three scripts are **verifications of computable pieces, not a proof of the framework** (DCCREG is exploratory). They reproduce standard [OC] math conditional on [IR] identifications; particle-content readings are [RH] and fenced. They pre-fill 3 of the 5 validation-ladder rungs in `sim/README.md`.

### results/ — run outputs (starts empty)
| File | What it is |
|------|-----------|
| `results/.gitkeep` | Placeholder; runs land here one folder each. | NEW |

---

## Where the DCCREG discipline lives (so it always has a place)

Three layers, redundant on purpose:
1. **`CLAUDE.md`** — auto-read by Claude Code at the start of every session; the firewall + workflow are the first thing any coding session sees.
2. **`docs/DCCREG_programme_README.md`** — the physics handoff; §1 (firewall), §2 (locked assumptions), §3/§3.1 (conventions + sandbox protocol) restate the discipline for chat sessions.
3. **`sim/README.md`** — repeats the no-fabricated-numbers rule and the graduation-valve step, so even a code-only session can't lose it.

Any new conversation (chat or Claude Code) that reads its entry file inherits the discipline. That's the design: the firewall is written into every door.

---

## Push to GitHub (your steps)

```bash
# from inside the bundle, where the dccreg/ folder is
cd dccreg
git init
git add .
git commit -m "DCCREG: blocks I–V (gravity v0.7, matter v0.2, joined), discipline, sim spec"
git branch -M main
git remote add origin git@github.com:<you>/<repo>.git   # or https URL
git push -u origin main
```

(If you'd rather, create the empty repo on GitHub first and copy its remote URL into the `git remote add` line.)

---

## Then: start the simulator (Claude Code, new session)

1. Open Claude Code in the repo root.
2. It auto-reads `CLAUDE.md`. Point it at the goal: *"Read CLAUDE.md and sim/README.md. Work the validation ladder (items 1–5) first, then the open targets. Write results to results/ with the required logs."*
3. It builds `sim/` scripts, runs them, writes `results/<run>/`.

## And: consolidation (chat session, when numbers converge)
- Bring a converged result back to a chat (or Claude Code) consolidation step.
- It updates the relevant Block through the firewall: bump version, add a revision row, move the prior version to `docs/archive/`, update cross-refs, move superseded parametric statements to History.
- Target graduations: numeric **K_A → G_eff** ⇒ Block IV v0.8; **ground-state matter loop** ⇒ Block V v0.3 (one run does both).

## Optional: keep the sandbox parallel
- Run the speculative track as its own conversation editing only `docs/DCCREG_sandbox_v01.md`.
- It routes earned [OC]/[IR] items to the sandbox's graduation queue; promotion happens in the main track.

---

## One honest note

I can prepare this bundle but I can't push it or drive Claude Code from here — the push and the session launches are yours. Everything above is staged so those steps are mechanical.
