# FRESH START — clean repo reset

Use this if the previous local clone got corrupted / crashed Claude Code.
This bundle is **verified clean** (text/markdown/Python only — no `.git`, no caches,
no junk, no zero-byte files; all 3 verification scripts re-run and PASS).
The corruption was in the old *local clone*, not in this content.

---

## Step 1 — get rid of the broken copy

On your machine, delete the old local folder entirely (don't try to repair it):

```bash
rm -rf /path/to/old/dccreg        # the broken local clone
```

If the broken state was also pushed to GitHub and the remote is messed up, either:
- **(a)** delete the GitHub repo and make a fresh empty one, OR
- **(b)** keep the repo but force a clean history in Step 3 (noted there).

A fresh empty GitHub repo (option a) is the cleanest if you're unsure.

---

## Step 2 — unzip this clean bundle

```bash
unzip dccreg_repo_bundle.zip        # creates a clean ./dccreg/
cd dccreg
```

Sanity-check it looks right (optional):
```bash
ls                                   # CLAUDE.md README.md docs/ sim/ results/ ...
python3 sim/checks/check_02_hexatic_greens_function.py | grep "∫_disk"
#   -> ∫_disk ∇²(ln r /2π) dA = 1.000
```

---

## Step 3 — make it a fresh git repo and push

**Fresh history (recommended after corruption):**
```bash
cd dccreg
rm -rf .git                          # ensure no inherited git state (there is none in the bundle, but be safe)
git init
git add .
git commit -m "DCCREG: clean restart — blocks I–V (gravity v0.8, matter v0.4), discipline, sim specs, run002/003 reports, run004 brief"
git branch -M main
git remote add origin <YOUR_REPO_URL>     # ssh or https
git push -u origin main
```

If you kept the old GitHub repo (option b in Step 1) and it has a broken history,
force the clean state over it:
```bash
git push -u origin main --force
```

---

## Step 4 — start Claude Code on the clean repo

Open Claude Code in the `dccreg/` folder. First message:

> Read `CLAUDE.md`, then `sim/README.md`, `sim/INTERPRETATION.md`, and
> `sim/RUN004_dirac_pairing_brief.md`. Also read the two prior reports in
> `results/run002_sosf_spectrum_iterated/` and `results/run003_excited_spectrum_l8/`.
> Do NOT write code yet — confirm back what run004 tests, the three pre-committed
> branches (B-YES / B-NO / B-AMBIGUOUS), and the two new validation rungs.

When its summary looks right, second message:

> Implement run004 per the brief as `sim/checks/check_05_dirac_pairing.py`,
> branching from the run003 closure/energy machinery. Run the validation rungs
> first (they gate everything); only if they pass, run the J-scan and write
> outputs to `results/run004_dirac_pairing/` with a NOTES.md that tags every
> claim [OC]/[IR]/[RH] and states which branch the run lands in and why.

Then:

> Write a consolidation report like `results/run003_excited_spectrum_l8/CONSOLIDATION_REPORT.md`,
> then commit and push.

---

## What "current" means (so you know nothing was lost)

- **Blocks:** I (substrate v0.4), II (MHD v0.2), III (radiative EM v0.2),
  **IV (gravity v0.8 — K_A computed)**, **V (matter v0.4 — excited spectrum)**.
- **Reports preserved:** run002 (ground state) and run003 (excited spectrum) under `results/`.
- **Next target staged:** `sim/RUN004_dirac_pairing_brief.md` (the chirality-axiom test).
- **Verification scripts:** `sim/checks/check_01..03` (+ outputs) — the regression suite,
  all passing.

> **Note on run003's script.** `check_04_excited_spectrum.py` was written on the
> Claude Code branch, not in this bundle (only its report is here). When you redo
> run004, Claude Code can regenerate check_04 from the run003 report if it needs
> the machinery, or build run004's check_05 fresh per the brief — either is fine.

---

## To avoid re-corrupting it

- Let **Claude Code** own all git operations in `sim/` and `results/`; don't hand-edit
  inside a running session and also commit from another terminal at the same time.
- Don't edit `docs/` from the Claude Code session except via the consolidation step
  (CLAUDE.md §3.3/§3.4) — keep doc edits to the chat-consolidation flow.
- Commit after each run; if a run wedges, `git status` / `git stash` before retrying,
  rather than forcing files around a half-written state.
