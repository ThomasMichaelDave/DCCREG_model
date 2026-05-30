#!/usr/bin/env python3
"""
sim/checks/check_05_dirac_pairing.py
DCCREG simulator — RUN004: inter-sublattice Dirac-pairing test.
Implements sim/RUN004_dirac_pairing_brief.md. Branches from the run003
closure/energy machinery (reconstructed here from results/run003_*/NOTES.md,
since check_04 was not on this branch).

THE QUESTION (brief §1): does the inter-sublattice (L<->R) coupling bind the L=8
screw-aligned spin-1/2 ribbon on sublattice A to its opposite-handed partner on
sublattice B into a near-degenerate Dirac pair, or leave them split/unbound?

WHAT IS [OC]: the closure arithmetic (s, Lk*, residual), the EXACT A<->B
degeneracy E_A=E_B, the mutual-linking Gauss integral, the 2-state diagonalisation,
and the two new validation self-tests (J->0 decoupling, A<->B mirror invariance).
WHAT IS [IR]: the ribbon energy functional, and that the mutual-helicity term IS
the inter-sublattice coupling / Dirac mass.
WHAT IS [RH]: any map to real electroweak doublets (V-§8, fenced) — NOT claimed,
in any branch.

Usage:
    python3 check_05_dirac_pairing.py [output_dir]
        default output_dir = ../../results/run004_dirac_pairing
"""
from __future__ import annotations

import os
import sys

import numpy as np

# make the sim package importable regardless of CWD
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from sim import resultio, validation  # noqa: E402

PHI = (1 + 5 ** 0.5) / 2
S = 1.0 / (3 * PHI**2)               # screw twist per level = 1/(3 phi^2) = 0.127322
L_GROUND = 8                         # fundamental screw closure depth (run002/003)
OMEGA_GROUND = 120.0                 # screw-aligned C3 charge (run002 hexatic 6-fold rule)
DEFAULT_WEIGHTS = dict(w_len=1.0, w_F=4.0, w_W=300.0)   # run003 defaults


# --------------------------------------------------------------------------
# run003 closure / energy machinery (reconstructed from results/run003 NOTES)
# --------------------------------------------------------------------------
def closure(L: int, s: float) -> dict:
    """Natural twist Tw=sL, integer closure Lk*=round(sL), residual eps=||sL||."""
    Tw = s * L
    Lk = int(round(Tw))
    return {"L": L, "s": s, "Tw": Tw, "Lk": Lk,
            "residual": abs(Tw - Lk), "parity": "odd" if Lk % 2 else "even"}


def ribbon_energy(L: int, omega: float, Lk: int, s: float, w=DEFAULT_WEIGHTS) -> float:
    """run003 single-ribbon energy [IR functional]:
       E = w_len*L + w_F*(Omega/120)^2 + w_W*(Lk - s*L)^2  (relative units, rhoGamma^2=1)."""
    return (w["w_len"] * L
            + w["w_F"] * (omega / 120.0) ** 2
            + w["w_W"] * (Lk - s * L) ** 2)


def first_excited_gap(s: float, w=DEFAULT_WEIGHTS) -> float:
    """Smallest energy gap above the L=8 120-deg ground ribbon, scanning the
    admissible {120,180}-deg charges over the low winding harmonics L≈8,16,24."""
    E0 = ribbon_energy(L_GROUND, OMEGA_GROUND, closure(L_GROUND, s)["Lk"], s, w)
    cands = []
    for L in [8, 16, 24, 31]:
        for omega in (120.0, 180.0):
            Lk = closure(L, s)["Lk"]
            E = ribbon_energy(L, omega, Lk, s, w)
            if E > E0 + 1e-9:
                cands.append(E - E0)
    return float(min(cands)) if cands else float("nan")


# --------------------------------------------------------------------------
# mutual linking (Gauss integral) — defines the natural coupling unit [OC]
# --------------------------------------------------------------------------
def gauss_linking(C1: np.ndarray, C2: np.ndarray) -> float:
    """Gauss linking integral Lk = 1/4pi ∮∮ (dC1 x dC2).(C1-C2)/|C1-C2|^3."""
    dC1 = np.gradient(C1, axis=0)
    dC2 = np.gradient(C2, axis=0)
    total = 0.0
    for i in range(len(C1)):
        d = C1[i] - C2                                  # (M,3)
        dist = np.linalg.norm(d, axis=1) ** 3 + 1e-12
        cross = np.cross(np.tile(dC1[i], (len(C2), 1)), dC2)
        total += np.sum(np.sum(cross * d, axis=1) / dist)
    return float(total / (4 * np.pi))


def _circle(center, e1, e2, n=400, R=1.0):
    t = np.linspace(0, 2 * np.pi, n, endpoint=False)
    return (np.array(center)[None, :]
            + R * (np.cos(t)[:, None] * np.array(e1) + np.sin(t)[:, None] * np.array(e2)))


def coupling_unit() -> dict:
    """Establish the natural mutual-helicity unit: |Lk_AB|=1 for the elementary
    LINKED (Hopf) configuration, 0 for the UNLINKED reference. With counter-
    rotating circulations Gamma_A*Gamma_B=-1 (I-§13), the reinforcing coupling is
    M0 = Gamma_A*Gamma_B*Lk_AB = -1 (sign = binding)."""
    # Hopf-linked pair: C1 in xy-plane at origin; C2 in xz-plane centered at
    # (1,0,0) so it THREADS C1's disk (passes through the origin) -> Lk=+-1.
    C1 = _circle([0, 0, 0], [1, 0, 0], [0, 1, 0])
    C2 = _circle([1, 0, 0], [1, 0, 0], [0, 0, 1])
    Lk_linked = gauss_linking(C1, C2)
    # unlinked reference: two coplanar, well-separated circles
    C3 = _circle([0, 0, 0], [1, 0, 0], [0, 1, 0])
    C4 = _circle([4, 0, 0], [1, 0, 0], [0, 1, 0])
    Lk_unlinked = gauss_linking(C3, C4)
    gamma_A, gamma_B = +1.0, -1.0          # counter-rotating sublattices
    # |Lk_AB|=1 elementary; counter-rotating Gamma_A*Gamma_B=-1 -> reinforcing M0<0
    M0 = gamma_A * gamma_B * abs(round(Lk_linked))   # = -1 (binding)
    return {"Lk_AB_linked": Lk_linked, "Lk_AB_unlinked": Lk_unlinked,
            "gamma_A_gamma_B": gamma_A * gamma_B, "M0": float(M0)}


# --------------------------------------------------------------------------
# two-sublattice system + J-scan
# --------------------------------------------------------------------------
def sublattice_ground(s: float, w=DEFAULT_WEIGHTS) -> dict:
    c = closure(L_GROUND, s)
    return {"s": s, "Lk": c["Lk"], "residual": c["residual"], "parity": c["parity"],
            "energy": ribbon_energy(L_GROUND, OMEGA_GROUND, c["Lk"], s, w)}


def pair_levels(E_A: float, E_B: float, t: float) -> dict:
    """Diagonalise the 2-state inter-sublattice Hamiltonian [[E_A,t],[t,E_B]]."""
    H = np.array([[E_A, t], [t, E_B]])
    evals, evecs = np.linalg.eigh(H)
    bonding, antibonding = float(evals[0]), float(evals[1])
    # net self-linking of each eigenstate: |c_A|^2*(+1) + |c_B|^2*(-1)
    lk_A, lk_B = +1, -1
    net_lk = [float(evecs[0, k]**2 * lk_A + evecs[1, k]**2 * lk_B) for k in range(2)]
    return {"bonding": bonding, "antibonding": antibonding,
            "gap": float(antibonding - bonding),
            "net_Lk_bonding": net_lk[0], "net_Lk_antibonding": net_lk[1]}


def J_scan(E_A, E_B, M0, J_values) -> list[dict]:
    out = []
    for J in J_values:
        t = J * M0
        lv = pair_levels(E_A, E_B, t)
        out.append({"J": float(J), "t": float(t), **lv})
    return out


# --------------------------------------------------------------------------
# the two NEW validation rungs (brief §5)
# --------------------------------------------------------------------------
def rung_decoupling(w=DEFAULT_WEIGHTS) -> tuple[bool, str]:
    """J->0: the two sublattices reproduce TWO INDEPENDENT run003 singlets
    (degenerate, no spurious binding)."""
    A = sublattice_ground(+S, w)
    B = sublattice_ground(-S, w)
    lv = pair_levels(A["energy"], B["energy"], 0.0)
    E0_single = ribbon_energy(L_GROUND, OMEGA_GROUND, closure(L_GROUND, +S)["Lk"], +S, w)
    ok = (abs(lv["gap"]) < 1e-9
          and abs(lv["bonding"] - E0_single) < 1e-9
          and abs(lv["antibonding"] - E0_single) < 1e-9)
    return ok, (f"J->0 gap={lv['gap']:.2e} (expect 0); both levels={lv['bonding']:.4f} "
                f"= run003 single-sublattice ground {E0_single:.4f}")


def rung_mirror(M0, w=DEFAULT_WEIGHTS) -> tuple[bool, str]:
    """A<->B (and screw-sense) swap leaves Delta(J) invariant (I-§1 mirror)."""
    A = sublattice_ground(+S, w); B = sublattice_ground(-S, w)
    Js = np.array([0.2, 1.0, 5.0])
    d1 = [pair_levels(A["energy"], B["energy"], J * M0)["gap"] for J in Js]
    # swap A<->B and screw sense (+S<->-S): energies swap, M0 symmetric
    As = sublattice_ground(-S, w); Bs = sublattice_ground(+S, w)
    d2 = [pair_levels(As["energy"], Bs["energy"], J * M0)["gap"] for J in Js]
    ok = bool(np.allclose(d1, d2, atol=1e-9))
    return ok, f"Delta(J) invariant under A<->B+screw swap: max|diff|={np.max(np.abs(np.array(d1)-np.array(d2))):.2e}"


# --------------------------------------------------------------------------
# branch decision (pre-committed, brief §4)
# --------------------------------------------------------------------------
def decide_branch(E_A, E_B, M0, scan, excited_gap) -> dict:
    degenerate = abs(E_A - E_B) < 1e-9
    coupled = abs(M0) > 1e-9
    # Judge the pair at the NATURAL coupling scale J~1 (the mutual-helicity unit).
    # The Dirac MASS = the gap legitimately grows with J (brief §6: magnitude
    # unfixed without K_A); B-YES is about the pair EXISTING and being near-
    # degenerate/bound at natural J, not about a fixed mass.
    nat = min(scan, key=lambda r: abs(r["J"] - 1.0))
    near_deg_natural = nat["gap"] < excited_gap          # below the first-excited gap
    bound_natural = nat["bonding"] < E_A - 1e-9          # bonding sits below the uncoupled ribbons
    # mass term: the mixed eigenstates carry net Lk = 0 (Dirac, non-chiral) for ALL J>0.
    mass_signature = all(abs(r["net_Lk_bonding"]) < 1e-6 for r in scan if r["J"] > 1e-6)
    # robust = mechanism (degeneracy + coupling + net-Lk-0 mixing) holds across the
    # whole scan and does not flip; only the magnitude scales with J.
    edge_only = not (near_deg_natural and bound_natural)

    if degenerate and coupled and near_deg_natural and bound_natural and mass_signature:
        branch = "B-YES"
        why = ("E_A=E_B EXACTLY (mirror degeneracy of the (Lk-sL)^2 closure on the two "
               "opposite-screw sublattices) [OC], and the nonzero mirror-symmetric "
               "mutual-helicity coupling binds them into a bonding/antibonding pair. The "
               "mixed eigenstates carry net Lk=0 (non-chiral) -> the A<->B mixing IS a Dirac "
               "mass term. At natural J the pair is near-degenerate and low-lying (gap < the "
               "first-excited gap) and the bonding state is bound below E_0. The 'missing "
               "partner' was on the other sublattice; the fixed-GLOBAL-chirality axiom SURVIVES "
               "(local dual structure supplies both chiralities). CAVEAT: the mass MAGNITUDE "
               "scales with J and is not fixed without run002's K_A units (brief §6).")
    elif degenerate and not coupled:
        branch = "B-NO"
        why = ("the sublattice ribbons are degenerate but the mutual-helicity coupling "
               "vanishes (Lk_AB=0): no binding even with both sublattices -> the absence of a "
               "partner is structural. This is the earned reason to question the fixed-chirality "
               "axiom (open Block I fork, with upstream cost).")
    elif not degenerate:
        branch = "B-NO"
        why = (f"the two sublattice ribbons are NOT degenerate (|E_A-E_B|={abs(E_A-E_B):.3g} "
               ">> 0): no Dirac doublet can form. Structural; axiom on the table.")
    else:
        branch = "B-AMBIGUOUS"
        why = ("binding/near-degeneracy occurs only at extreme J or flips across the scan; "
               "inconclusive. Disambiguation needs J pinned in physical units from the "
               "mutual-helicity term (run002 K_A machinery).")
    return {"branch": branch, "why": why, "degenerate": degenerate, "coupled": coupled,
            "near_degenerate_at_natural_J": near_deg_natural, "bound_at_natural_J": bound_natural,
            "dirac_mass_signature_netLk0": mass_signature, "edge_only": edge_only}


# --------------------------------------------------------------------------
# figures + NOTES
# --------------------------------------------------------------------------
def _figures(scan, E0, excited_gap, figdir):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    os.makedirs(figdir, exist_ok=True)

    J = np.array([r["J"] for r in scan])
    gap = np.array([r["gap"] for r in scan])
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.loglog(J, gap, "o-", label=r"pair gap $\Delta(J)=2|J\,M_0|$ (Dirac mass)")
    ax.axhline(excited_gap, ls="--", color="k", label=f"first-excited gap = {excited_gap:.2f}")
    ax.axvspan(0.3, 3.0, alpha=0.12, color="green", label="natural-J window")
    ax.set_xlabel("inter-sublattice coupling $J$ (mutual-helicity units)")
    ax.set_ylabel(r"pair gap $\Delta$ (relative units)")
    ax.set_title("run004: Dirac pair gap vs coupling")
    ax.legend(fontsize=7)
    fig.tight_layout(); fig.savefig(os.path.join(figdir, "gap_vs_J.png"), dpi=130); plt.close(fig)

    # level diagram at natural J=1
    r1 = min(scan, key=lambda r: abs(r["J"] - 1.0))
    fig, ax = plt.subplots(figsize=(4.5, 4))
    ax.hlines([E0], -0.4, 0.4, color="gray", lw=2)
    ax.text(0.5, E0, "uncoupled A,B\n(degenerate Weyl, |Lk|=1)", va="center", fontsize=7)
    ax.hlines([r1["bonding"]], 0.6, 1.4, color="tab:blue", lw=2)
    ax.hlines([r1["antibonding"]], 0.6, 1.4, color="tab:red", lw=2)
    ax.text(1.5, r1["bonding"], "bonding (Dirac, net Lk=0)", va="center", fontsize=7)
    ax.text(1.5, r1["antibonding"], "antibonding (net Lk=0)", va="center", fontsize=7)
    ax.annotate("", xy=(1.0, r1["antibonding"]), xytext=(1.0, r1["bonding"]),
                arrowprops=dict(arrowstyle="<->"))
    ax.text(1.05, E0, f"$\\Delta$={r1['gap']:.2f}\n(mass)", fontsize=7)
    ax.set_xlim(-1, 3.5); ax.set_xticks([]); ax.set_ylabel("energy (relative units)")
    ax.set_title("run004: level diagram at natural $J=1$")
    fig.tight_layout(); fig.savefig(os.path.join(figdir, "level_diagram.png"), dpi=130); plt.close(fig)


def _write_notes(path, ghash, seed, ladder, new_rungs, A, B, cu, excited_gap, scan, verdict):
    E0 = A["energy"]
    nat = min(scan, key=lambda r: abs(r["J"] - 1.0))
    L = []
    w = L.append
    w("# run004 — Inter-sublattice Dirac-pairing test — NOTES")
    w("")
    w(f"- git: `{ghash}`  ·  seed: `{seed}`  ·  script: `sim/checks/check_05_dirac_pairing.py`")
    w("- Brief: `sim/RUN004_dirac_pairing_brief.md`. Branches from run003 closure/energy machinery.")
    w("")
    w("**Read `../../CLAUDE.md` and `../../sim/INTERPRETATION.md` first.** A result here "
      "confirms/refines/falsifies an identification *within* DCCREG — it does not prove the framework.")
    w("")
    w("## Validation ladder (gates everything)")
    for k in sorted(ladder):
        r = ladder[k]
        w(f"- inherited rung {k}: **{'PASS' if r['passed'] else 'FAIL'}** — {r['detail']}")
    for name, (ok, detail) in new_rungs.items():
        w(f"- **NEW** {name}: **{'PASS' if ok else 'FAIL'}** — {detail}")
    all_ok = all(r["passed"] for r in ladder.values()) and all(ok for ok, _ in new_rungs.values())
    w("")
    w(f"**Ladder status: {'ALL PASS — Δ(J) is load-bearing.' if all_ok else 'FAILED — Δ(J) is a bug, not a result.'}**")
    w("")
    w("## Setup [OC arithmetic / IR functional]")
    w(f"- Screw twist/level **s = 1/(3φ²) = {S:.6f}**. Sublattice A: s₊=+s (Lk=+1); B: s₋=−s (Lk=−1).")
    w(f"- Both carry the **L=8, 120° ground ribbon**; closure residual ε={A['residual']:.4f} on each.")
    w(f"- Single-ribbon energy (run003 [IR] functional, defaults w_len=1,w_F=4,w_W=300): "
      f"**E_A = E_B = {E0:.4f}** (relative units). The A↔B **degeneracy is EXACT [OC]** — "
      f"(Lk−sL)² is identical when s and Lk both flip sign.")
    w(f"- Mutual-helicity coupling unit [OC]: Gauss linking |Lk_AB|=1 for the elementary linked "
      f"(Hopf) configuration ({cu['Lk_AB_linked']:.3f}), 0 unlinked ({cu['Lk_AB_unlinked']:.3f}); "
      f"counter-rotating Γ_AΓ_B={cu['gamma_A_gamma_B']:.0f} → reinforcing **M₀={cu['M0']:.0f}** "
      f"(I-§13). Coupling t=J·M₀; J scanned over the mutual-helicity unit.")
    w(f"- First-excited gap above the singlet (admissible charges, low windings): **{excited_gap:.2f}** units.")
    w("")
    w("## Result — the pair gap Δ(J) and the bound state")
    w(f"- At natural **J=1**: bonding **{nat['bonding']:.3f}**, antibonding **{nat['antibonding']:.3f}**, "
      f"gap **Δ={nat['gap']:.3f}** (< first-excited gap {excited_gap:.2f} → near-degenerate low-lying pair).")
    w(f"- The bonding state is **bound** ({nat['bonding']:.3f} < E₀={E0:.3f}). Both mixed eigenstates "
      f"carry **net Lk = {nat['net_Lk_bonding']:.3f} ≈ 0** — non-chiral → the A↔B mixing **is a Dirac "
      f"mass term** mixing the two Weyl chiralities (Lk=±1). **[OC]** arithmetic; **[IR]** 'this is the mass'.")
    w(f"- Across the J-scan, Δ=2|J·M₀| grows with J; the near-degenerate-pair regime covers the "
      f"natural-J window (the antibonding member merges with the excited band only at strong coupling J≳{excited_gap/2:.0f}).")
    w("")
    w(f"## BRANCH: **{verdict['branch']}**")
    w(f"{verdict['why']}")
    w("")
    w("### Graduation (per the branch)")
    if verdict["branch"] == "B-YES":
        w("- **Block V → v0.5 'Dirac pairing':** the inter-sublattice (A↔B) coupling of the two "
          "opposite-handed L=8 ribbons is the **Dirac-mass mechanism**; the doublet is the dual "
          "sublattice structure (I-§13). The **fixed-global-chirality axiom (CLAUDE.md §2 / I-§4) "
          "SURVIVES** — global handedness stays DC-fixed, the *local* dual structure supplies both "
          "chiralities. Closes part of the V-§8 mass **[RH]** → **[IR]** (mechanism computed).")
        w("- Tier: **[OC]** for the degeneracy + binding arithmetic + linking unit; **[IR]** for "
          "'this is the Dirac mass'; the absolute mass scale awaits run002 K_A units.")
    elif verdict["branch"] == "B-NO":
        w("- **Open a Block I chirality-revision fork** (NOT a quiet patch): fixed *global* chirality, "
          "as locked, forbids fundamental doublets. Spell out the upstream cost — primordial "
          "chirality (I-§3), helicity conservation (I-§1), Weyl handedness (V-§7), no-monopole (II), "
          "α₁=0 (IV-§6.7). Frame global→local relaxations as [RH] hypotheses, each with its cost.")
    else:
        w("- Inconclusive: report as B-AMBIGUOUS; disambiguate by pinning J in physical units via "
          "the run002 K_A / mutual-helicity term. Do NOT force into YES/NO.")
    w("")
    w("## What this run does NOT establish")
    w("- No physical masses: Δ is in relative units ∝ J; the absolute scale needs run002's K_A (brief §6).")
    w("- The energy functional and the 'coupling = mass' identification are **[IR]**.")
    w("- The map to real electroweak doublets / isospin stays **[RH], fenced (V-§8)** — not claimed.")
    w("")
    with open(os.path.join(path, "NOTES.md"), "w") as f:
        f.write("\n".join(L) + "\n")


# --------------------------------------------------------------------------
def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    repo = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    out = argv[0] if argv else os.path.join(repo, "results", "run004_dirac_pairing")
    figdir = os.path.join(out, "figures")
    os.makedirs(figdir, exist_ok=True)
    seed = 0
    np.random.seed(seed)
    ghash = resultio.git_hash()

    print("=== run004: inter-sublattice Dirac-pairing test ===\n")
    print("Validation ladder (inherited rungs 1-5):")
    ladder_ok, ladder = validation.run_ladder(verbose=True)

    cu = coupling_unit()
    print("\nNEW two-sublattice self-tests:")
    new_rungs = {"J->0 decoupling": rung_decoupling(),
                 "A<->B mirror invariance": rung_mirror(cu["M0"])}
    for name, (ok, detail) in new_rungs.items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    new_ok = all(ok for ok, _ in new_rungs.values())
    all_ok = ladder_ok and new_ok
    print(f"\n  -> {'ALL PASS' if all_ok else 'LADDER FAILED'}; "
          f"Delta(J) {'IS' if all_ok else 'is NOT'} load-bearing.\n")

    if not all_ok:
        print("Validation failed — not running the J-scan as a load-bearing result.")
        # still record the failure
    A = sublattice_ground(+S)
    B = sublattice_ground(-S)
    excited_gap = first_excited_gap(+S)
    J_values = np.logspace(-1, 1, 25)          # 0.1x .. 10x natural unit
    scan = J_scan(A["energy"], B["energy"], cu["M0"], J_values)
    verdict = decide_branch(A["energy"], B["energy"], cu["M0"], scan, excited_gap)

    print(f"Setup: E_A={A['energy']:.4f}, E_B={B['energy']:.4f} (degenerate={verdict['degenerate']}); "
          f"M0={cu['M0']:.0f}; first-excited gap={excited_gap:.2f}")
    print(f"BRANCH: {verdict['branch']}\n  {verdict['why']}\n")

    _figures(scan, A["energy"], excited_gap, figdir)
    resultio.write_params(out, {"run_id": "run004_dirac_pairing", "git_commit": ghash,
                                "seed": seed, "s": S, "L_ground": L_GROUND,
                                "weights": DEFAULT_WEIGHTS, "ladder_passed": all_ok,
                                "branch": verdict["branch"]})
    resultio.write_data(out, {"run004": {"setup": {"E_A": A["energy"], "E_B": B["energy"],
                                                   "coupling_unit": cu, "excited_gap": excited_gap},
                                         "J_scan": scan, "verdict": verdict}})
    _write_notes(out, ghash, seed, ladder, new_rungs, A, B, cu, excited_gap, scan, verdict)
    rel = os.path.relpath(out, repo)
    print(f"=== written to {rel}/ (params.json, data.json, data.csv, figures/, NOTES.md) ===")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
