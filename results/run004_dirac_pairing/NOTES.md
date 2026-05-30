# run004 — Inter-sublattice Dirac-pairing test — NOTES

- git: `9887fba6f155944c6ed26bedd35796f1dcac32d5`  ·  seed: `0`  ·  script: `sim/checks/check_05_dirac_pairing.py`
- Brief: `sim/RUN004_dirac_pairing_brief.md`. Branches from run003 closure/energy machinery.

**Read `../../CLAUDE.md` and `../../sim/INTERPRETATION.md` first.** A result here confirms/refines/falsifies an identification *within* DCCREG — it does not prove the framework.

## Validation ladder (gates everything)
- inherited rung 1: **PASS** — SOSF geometry reproduces §A.7 and structural counts
- inherited rung 2: **PASS** — solid disclination log-log slope = 2.192 (expect ~2, the 1/k^4 baseline)
- inherited rung 3: **PASS** — ∫_disk ∇²(ln r/2π) dA = 1.000 (expect ≈ 1.000, Einstein/Newton form)
- inherited rung 4: **PASS** — planar Wr=0.0000≈0; screw supplies integer Tw (n=1:Lk=-1.000, n=2:Lk=-2.000, n=3:Lk=-3.000)
- inherited rung 5: **PASS** — |O|=24 (expect 24); Frank classes [90, 120, 180] (expect [90,120,180])
- **NEW** J->0 decoupling: **PASS** — J->0 gap=0.00e+00 (expect 0); both levels=12.1035 = run003 single-sublattice ground 12.1035
- **NEW** A<->B mirror invariance: **PASS** — Delta(J) invariant under A<->B+screw swap: max|diff|=0.00e+00

**Ladder status: ALL PASS — Δ(J) is load-bearing.**

## Setup [OC arithmetic / IR functional]
- Screw twist/level **s = 1/(3φ²) = 0.127322**. Sublattice A: s₊=+s (Lk=+1); B: s₋=−s (Lk=−1).
- Both carry the **L=8, 120° ground ribbon**; closure residual ε=0.0186 on each.
- Single-ribbon energy (run003 [IR] functional, defaults w_len=1,w_F=4,w_W=300): **E_A = E_B = 12.1035** (relative units). The A↔B **degeneracy is EXACT [OC]** — (Lk−sL)² is identical when s and Lk both flip sign.
- Mutual-helicity coupling unit [OC]: Gauss linking |Lk_AB|=1 for the elementary linked (Hopf) configuration (-1.000), 0 unlinked (0.000); counter-rotating Γ_AΓ_B=-1 → reinforcing **M₀=-1** (I-§13). Coupling t=J·M₀; J scanned over the mutual-helicity unit.
- First-excited gap above the singlet (admissible charges, low windings): **5.00** units.

## Result — the pair gap Δ(J) and the bound state
- At natural **J=1**: bonding **11.104**, antibonding **13.104**, gap **Δ=2.000** (< first-excited gap 5.00 → near-degenerate low-lying pair).
- The bonding state is **bound** (11.104 < E₀=12.104). Both mixed eigenstates carry **net Lk = 0.000 ≈ 0** — non-chiral → the A↔B mixing **is a Dirac mass term** mixing the two Weyl chiralities (Lk=±1). **[OC]** arithmetic; **[IR]** 'this is the mass'.
- Across the J-scan, Δ=2|J·M₀| grows with J; the near-degenerate-pair regime covers the natural-J window (the antibonding member merges with the excited band only at strong coupling J≳2).

## BRANCH: **B-YES**
E_A=E_B EXACTLY (mirror degeneracy of the (Lk-sL)^2 closure on the two opposite-screw sublattices) [OC], and the nonzero mirror-symmetric mutual-helicity coupling binds them into a bonding/antibonding pair. The mixed eigenstates carry net Lk=0 (non-chiral) -> the A<->B mixing IS a Dirac mass term. At natural J the pair is near-degenerate and low-lying (gap < the first-excited gap) and the bonding state is bound below E_0. The 'missing partner' was on the other sublattice; the fixed-GLOBAL-chirality axiom SURVIVES (local dual structure supplies both chiralities). CAVEAT: the mass MAGNITUDE scales with J and is not fixed without run002's K_A units (brief §6).

### Graduation (per the branch)
- **Block V → v0.5 'Dirac pairing':** the inter-sublattice (A↔B) coupling of the two opposite-handed L=8 ribbons is the **Dirac-mass mechanism**; the doublet is the dual sublattice structure (I-§13). The **fixed-global-chirality axiom (CLAUDE.md §2 / I-§4) SURVIVES** — global handedness stays DC-fixed, the *local* dual structure supplies both chiralities. Closes part of the V-§8 mass **[RH]** → **[IR]** (mechanism computed).
- Tier: **[OC]** for the degeneracy + binding arithmetic + linking unit; **[IR]** for 'this is the Dirac mass'; the absolute mass scale awaits run002 K_A units.

## What this run does NOT establish
- No physical masses: Δ is in relative units ∝ J; the absolute scale needs run002's K_A (brief §6).
- The energy functional and the 'coupling = mass' identification are **[IR]**.
- The map to real electroweak doublets / isospin stays **[RH], fenced (V-§8)** — not claimed.

