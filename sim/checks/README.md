# sim/checks/ — Verification scripts (the computed [OC] pieces)

These are the Python calculations actually run during the derivation, reconstructed as standalone, reproducible scripts. **Read `../../CLAUDE.md` first.**

## Honest framing — what these are and are not

These scripts **verify specific computable pieces** of the construction. They are **not** a proof of the framework — DCCREG is exploratory and not established physics. Each script checks standard [OC] mathematics; the *physical identifications* those checks rest on are [IR], and anything about real particles is [RH] (fenced in Block V §8). Read each file's header for its exact scope and its "does NOT establish" clause.

## The scripts

| Script | Checks | Block | Validation-ladder item |
|--------|--------|-------|------------------------|
| `check_01_calugareanu_framing.py` | Screw framing ⇒ ribbon; Lk = Tw + Wr (planar loop: Wr≈0, screw supplies integer Tw) | V-§3 | item 4 |
| `check_02_hexatic_greens_function.py` | Hexatic disclination kernel = 2D Laplacian Green's fn (∫∇²(ln r/2π)=1.000) ⇒ Einstein/Newton form; solid r²ln r baseline | IV-§5.5, §3a | items 2 & 3 |
| `check_03_joining_spectrum.py` | Octahedral charges {90,120,180}°; K_A~β scaling; Fibonacci spin-parity selection | IV-§3a, V-§2a, §6a | item 5 |

Together they pre-populate **3 of the 5 rungs** of the validation ladder in `../README.md` (items 2, 3, 4, 5). The remaining real work — stable-loop **energies**, the ground-state matter loop, and the **numeric K_A** — is the open simulator target, not done here.

## Reproduce

```bash
pip install -r ../requirements.txt
python3 check_01_calugareanu_framing.py
python3 check_02_hexatic_greens_function.py
python3 check_03_joining_spectrum.py
```

Reference outputs are saved alongside each script as `*.out.txt`.

## Audit-trail note

`check_02` contains a clearly-fenced **WITHDRAWN** block: the original v0.6 run printed a "screening crossover" line claiming a ratio ≫1 when the numbers were ≪1 (a wrong proxy model). Per the firewall's "correct openly" rule, it is preserved and marked, not deleted — the script now prints its own correction. The load-bearing result (the Green's-function power law) is independent of it.
