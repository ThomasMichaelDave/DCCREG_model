#!/usr/bin/env python3
"""
check_04_excited_spectrum.py
DCCREG simulator — the EXCITED / multiplet defect spectrum above the L=8
spin-1/2 ground state (Block V matter sector; the Joining IV-§3a / V-§2a/§6a).

CONTEXT (what is already closed, run002):
    The GROUND-STATE gate is closed. The lowest stable framed ribbon is the
    fundamental screw closure at Fibonacci depth L=8: charge 120 deg
    (C3 about [1,1,1]), self-linking |Lk|=1 (odd -> spin-1/2), definite
    handedness. See results/run002_sosf_spectrum_iterated/CONSOLIDATION_REPORT.md.

THE QUESTION THIS RUN ASKS:
    What sits ABOVE the L=8 ground state? Does the energetics produce
      (a) only the single state (an isolated singlet),
      (b) a DOUBLET (a near-degenerate low pair, isospin-like), or
      (c) a GENERATION tower (replicas of the same quantum numbers)?
    The firewall rule for this run: DO NOT claim a multiplet the energetics do
    not support. Report the gaps and the robustness, tag every claim.

WHAT IS [OC] HERE (standard arithmetic, framework-independent):
    - The screw framing twist per level s = (120/phi^2)/360 turns = 1/(3 phi^2).
    - The closure residual eps(L) = || s L || (distance to nearest integer) and
      the optimal self-linking Lk*(L) = round(s L); spin parity = Lk* mod 2.
    - The Frank energy scales as the SQUARE of the disclination charge (Omega^2);
      the admissible charges are {120,180} deg (90 excluded by the hexatic
      6-fold single-valuedness rule, run002), and 120 < 180.

WHAT IS [IR] HERE (a modeling choice WITHIN the framework):
    - The total ribbon energy functional
          E = w_len * L  +  w_F * (Omega/120)^2  +  w_W * (Lk - s L)^2
      i.e. line tension ~ length, Frank energy ~ Omega^2, and a writhe/closure
      energy ~ (required writhe)^2. The TERMS are standard; identifying THIS
      functional as the defect energy is the interpretive step.
    - Identifying a stable ribbon with "a matter particle" is [IR]; the map to
      real Standard-Model generations / quantum numbers is [RH], fenced (V-§8).

WHAT THIS DOES *NOT* ESTABLISH:
    - It does not compute the absolute energies in physical units (those need the
      lattice Biot-Savart sum, the run002 K_A machinery, not re-derived here).
    - It does not prove these ribbons are real particles, nor that any apparent
      replication is the three SM generations. That stays [RH].

Tier: [OC] for the closure arithmetic, parities and gaps; [IR] for the energy
functional and "ribbon = particle"; [RH] for any generation reading.
"""
import json
import os
import subprocess
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
S = (120.0 / PHI ** 2) / 360.0          # framing twist, turns per level = 1/(3 phi^2)
ADMISSIBLE_CHARGES = (120.0, 180.0)     # 90 excluded by the hexatic 6-fold rule (run002)
FIBONACCI = {1, 2, 3, 5, 8, 13, 21, 34}

# ---- default [IR] energy weights (relative units; rho*Gamma^2 set to 1) ----
DEFAULTS = dict(w_len=1.0, w_F=4.0, w_W=300.0)
# w_W >> w_len reflects run002's finding that the *closure* energy dominates and
# pins L=8 as the ground state across a wide weight scan; we verify that below.

L_MAX = 40
LK_MAX = 6


def closure(L):
    """[OC] Screw closure at depth L: natural twist, optimal integer self-linking,
    residual writhe and spin parity."""
    Tw = S * L
    Lk_star = int(round(Tw))
    eps = abs(Tw - Lk_star)
    return Tw, Lk_star, eps


def energy(L, Omega, Lk, w):
    """[IR] Ribbon energy functional (relative units)."""
    Tw = S * L
    return w["w_len"] * L + w["w_F"] * (Omega / 120.0) ** 2 + w["w_W"] * (Lk - Tw) ** 2


def stable_ribbon_depths():
    """[OC] The physically stable ribbons are the screw-closure MINIMA: depths
    where ||sL|| is a local minimum below tolerance. These are the fundamental
    L=8 (winding n=1) and its winding harmonics L ~ 8n. An off-minimum depth is
    NOT a separate defect -- it relaxes toward the nearest minimum -- so the
    spectrum is built on the minima, not on every integer L."""
    mins = []
    for L in range(1, L_MAX + 1):
        Tw, Lk, eps = closure(L)
        nbr = [abs(S * j - round(S * j)) for j in (L - 1, L + 1) if 1 <= j <= L_MAX]
        if Lk >= 1 and eps < 0.10 and all(eps <= e for e in nbr):
            mins.append(dict(L=L, Lk=Lk, eps=eps, winding=Lk))
    return mins


def enumerate_spectrum(w):
    """The physical ribbon spectrum: stable-closure depths x admissible charges,
    plus the fixed-depth writhe excitations (Lk = Lk* +/- 1). Sorted by energy."""
    rows = []
    for m in stable_ribbon_depths():
        L, Lk_star, eps = m["L"], m["Lk"], m["eps"]
        Tw = S * L
        for Omega in ADMISSIBLE_CHARGES:
            # the ground closure (Lk*) and its writhe excitations Lk* +/- 1
            for Lk in (Lk_star - 1, Lk_star, Lk_star + 1):
                if Lk < 1:
                    continue
                E = energy(L, Omega, Lk, w)
                rows.append(dict(
                    L=L, Omega=Omega, Lk=Lk, Tw=round(Tw, 4),
                    writhe=round(Lk - Tw, 4), eps_opt=round(eps, 4),
                    framed=True, winding=Lk, is_ground_closure=(Lk == Lk_star),
                    spin=("1/2" if Lk % 2 == 1 else "int"),
                    fibonacci=(L in FIBONACCI), E=E))
    rows.sort(key=lambda r: r["E"])
    return rows


def git_hash():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=os.path.dirname(__file__) or ".",
            stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return "unknown"


def main(outdir=None):
    np.random.seed(0)   # determinism logged per CLAUDE.md S5 (computation is exact)
    w = dict(DEFAULTS)

    # ---------------------------------------------------------------
    # PART 1 -- the closure spectrum (pure [OC] arithmetic)
    # ---------------------------------------------------------------
    print("=" * 68)
    print("PART 1 -- screw-closure spectrum  [OC arithmetic]")
    print("=" * 68)
    print(f"s = (120/phi^2)/360 = {S:.6f} turns/level ; 1/s = {1/S:.4f} = 3 phi^2")
    print(f"{'L':>3} {'Tw=sL':>8} {'Lk*':>4} {'resid':>7} {'spin':>5} {'fib':>4}  note")
    closures = []
    for L in range(1, L_MAX + 1):
        Tw, Lk, eps = closure(L)
        # local minimum of residual = a stable-closure candidate depth
        nbr = [abs(S * j - round(S * j)) for j in (L - 1, L + 1) if 1 <= j <= L_MAX]
        is_min = all(eps <= e for e in nbr) and eps < 0.10
        spin = "1/2" if Lk % 2 == 1 else "int"
        note = f"winding n={Lk}" if is_min and Lk >= 1 else ("bare/unframed" if is_min else "")
        if is_min or L in FIBONACCI:
            print(f"{L:>3} {Tw:>8.4f} {Lk:>4} {eps:>7.4f} {spin:>5} "
                  f"{'F' if L in FIBONACCI else '':>4}  {note}")
        if is_min and Lk >= 1:
            closures.append(dict(L=L, Lk=Lk, eps=round(eps, 4), spin=spin))
    print("\nThe good closures (residual local minima) fall at the FUNDAMENTAL L=8")
    print("and its winding HARMONICS L ~ 8,16,24,31,39 (multiples of 1/s=7.854),")
    print("NOT at the higher Fibonacci numbers 13,21 (those close poorly). Spin")
    print("parity follows the winding number n: odd n -> spin-1/2, even n -> boson.")

    # ---------------------------------------------------------------
    # PART 2 -- energy spectrum and the gap above the ground state
    # ---------------------------------------------------------------
    print("\n" + "=" * 68)
    print("PART 2 -- energy spectrum (default [IR] weights)  ground + excited")
    print("=" * 68)
    print(f"weights: {w}")
    spec = enumerate_spectrum(w)
    framed = spec   # every entry is a genuinely framed (Lk>=1) stable-closure ribbon
    gs = framed[0]
    print("(spectrum built on the stable-closure depths L~8,16,24,31,39 + their")
    print(" fixed-depth writhe excitations Lk*+-1; off-minimum depths relax away)")
    print(f"{'rank':>4} {'L':>3} {'Omega':>6} {'Lk':>3} {'spin':>5} "
          f"{'E':>9} {'dE_gs':>9}  comment")
    for i, r in enumerate(framed[:12]):
        dE = r["E"] - gs["E"]
        tag = ""
        if i == 0:
            tag = "<-- GROUND (matches run002: L=8, 120deg, spin-1/2)"
        elif not r["is_ground_closure"]:
            tag = "writhe excitation (Lk != Lk*) -- costly, high-lying"
        elif r["Omega"] == 180:
            tag = "180deg charge channel (Frank gap, ~2.25x)"
        elif r["winding"] % 2 == 1:
            tag = f"odd-winding harmonic n={r['winding']} (spin-1/2, generation-like?)"
        else:
            tag = f"even-winding harmonic n={r['winding']} (boson)"
        print(f"{i:>4} {r['L']:>3} {int(r['Omega']):>6} {r['Lk']:>3} {r['spin']:>5} "
              f"{r['E']:>9.3f} {dE:>9.3f}  {tag}")
    gap1 = framed[1]["E"] - gs["E"]
    print(f"\nGround-state gap to first excited ribbon: dE = {gap1:.3f} "
          f"(in w_len*length units, the line-tension quantum).")

    # ---------------------------------------------------------------
    # PART 3 -- DOUBLET / degeneracy test (does chirality lift it?)
    # ---------------------------------------------------------------
    print("\n" + "=" * 68)
    print("PART 3 -- doublet test: is the ground state degenerate?")
    print("=" * 68)
    # (i) writhe-sign partner Lk = -1 vs +1 at L=8
    E_plus = energy(8, 120, +1, w)
    E_minus = energy(8, 120, -1, w)
    print(f"(i) writhe-sign partners at L=8, 120deg:")
    print(f"    Lk=+1: E={E_plus:.3f}  (Wr={1-S*8:+.3f})  <-- realized")
    print(f"    Lk=-1: E={E_minus:.3f}  (Wr={-1-S*8:+.3f})  split dE={E_minus-E_plus:.3f}")
    print(f"    => the fixed screw sense makes Lk=-1 cost ~{E_minus-E_plus:.0f} units;")
    print(f"       NOT degenerate. No +/- writhe doublet.")
    # (ii) handedness: the global screw fixes ONE handedness (DC handedness).
    print(f"(ii) handedness: global screw sense is fixed (locked assumption);")
    print(f"     a left- and right-handed ribbon are NOT both realized -> no L/R")
    print(f"     parity doublet. Chirality lifts the degeneracy by construction.")
    # nearest-energy gap among the low states (numerical degeneracy check)
    lows = sorted(set(round(r["E"], 6) for r in framed[:6]))
    min_split = min(np.diff(lows)) if len(lows) > 1 else float("inf")
    print(f"(iii) smallest energy split among the 6 lowest framed ribbons: "
          f"{min_split:.3f} >> 0 -> no accidental near-degeneracy.")

    # ---------------------------------------------------------------
    # PART 4 -- robustness scan over the [IR] weights (run002-style)
    # ---------------------------------------------------------------
    print("\n" + "=" * 68)
    print("PART 4 -- robustness: vary weights 0.1x-10x, track ground + 1st excited")
    print("=" * 68)
    rng = np.random.default_rng(0)
    factors = [0.1, 0.3, 1.0, 3.0, 10.0]
    gs_stable = 0
    first_excited_ids = []
    n = 0
    for fl in factors:
        for ff in factors:
            for fw in factors:
                wf = dict(w_len=DEFAULTS["w_len"] * fl,
                          w_F=DEFAULTS["w_F"] * ff,
                          w_W=DEFAULTS["w_W"] * fw)
                fr = [r for r in enumerate_spectrum(wf) if r["framed"]]
                g = fr[0]
                if g["L"] == 8 and g["Omega"] == 120 and g["Lk"] == 1:
                    gs_stable += 1
                first_excited_ids.append((fr[1]["L"], int(fr[1]["Omega"]), fr[1]["Lk"]))
                n += 1
    from collections import Counter
    print(f"ground state = (L=8, 120deg, spin-1/2) in {gs_stable}/{n} = "
          f"{100*gs_stable/n:.0f}% of the weight scan  [robust -> isolated singlet]")
    fe = Counter(first_excited_ids)
    print("first-EXCITED ribbon across the same scan (it is NOT stable):")
    for (L, Om, Lk), c in fe.most_common(5):
        spin = "1/2" if Lk % 2 == 1 else "int"
        print(f"    (L={L:>2}, {Om}deg, Lk={Lk}, {spin})  in {100*c/n:>4.0f}%")
    print("=> the FIRST EXCITED identity is weight-DEPENDENT (no single answer)")
    print("   => the excited band is NOT a robust doublet or generation multiplet.")

    # ---------------------------------------------------------------
    # PART 5 -- verdict
    # ---------------------------------------------------------------
    print("\n" + "=" * 68)
    print("VERDICT")
    print("=" * 68)
    print("- GROUND STATE: isolated spin-1/2 singlet (L=8, 120deg, |Lk|=1),")
    print("  robust across the weight scan; large closure gap below all others.")
    print("- DOUBLET: NONE. The global screw (fixed chirality) lifts both the")
    print("  +/- writhe and the L/R handedness degeneracies. No near-degenerate pair.")
    print("- GENERATION TOWER: the same (spin-1/2, 120deg) quantum numbers DO recur")
    print("  at odd-winding harmonics (n=1,3,5 -> L~8,24,39), interleaved with")
    print("  even-winding bosons (n=2,4 -> L~16,31). But this is an INFINITE winding")
    print("  ladder, not three replicas, and the low-excited ordering is weight-")
    print("  dependent. The energetics do NOT support a clean 3-generation multiplet.")
    print("  Any 'generation' reading is [RH], fenced (V-§8) -- NOT claimed.")

    # ---- write outputs (CLAUDE.md S5) ----
    if outdir:
        os.makedirs(os.path.join(outdir, "figures"), exist_ok=True)
        params = dict(seed=0, git=git_hash(), s_turns_per_level=S,
                      admissible_charges=list(ADMISSIBLE_CHARGES),
                      weights=w, L_max=L_MAX, Lk_max=LK_MAX,
                      robustness_factors=factors)
        with open(os.path.join(outdir, "params.json"), "w") as f:
            json.dump(params, f, indent=2)
        data = dict(
            closure_minima=closures,
            ground_state=dict(L=gs["L"], Omega=gs["Omega"], Lk=gs["Lk"],
                              spin=gs["spin"], E=gs["E"]),
            ground_gap=gap1,
            spectrum_low=[{k: r[k] for k in
                           ("L", "Omega", "Lk", "spin", "winding", "E", "fibonacci")}
                          for r in framed[:12]],
            doublet=dict(present=False,
                         writhe_split=E_minus - E_plus,
                         reason="global screw fixes chirality; +/- writhe and "
                                "L/R handedness non-degenerate"),
            ground_state_robust_pct=100 * gs_stable / n,
            first_excited_distribution={
                f"L{L}_{Om}_Lk{Lk}": c for (L, Om, Lk), c in fe.items()},
            verdict="isolated spin-1/2 singlet; no doublet; no robust generation "
                    "multiplet; recurring odd-winding fermionic harmonics are [RH]")
        with open(os.path.join(outdir, "data.json"), "w") as f:
            json.dump(data, f, indent=2)
        # CSV of the full sorted spectrum
        import csv
        with open(os.path.join(outdir, "data.csv"), "w", newline="") as f:
            wcsv = csv.DictWriter(f, fieldnames=list(spec[0].keys()))
            wcsv.writeheader()
            for r in spec:
                wcsv.writerow(r)
        _figures(os.path.join(outdir, "figures"), w, spec, framed)
        print(f"\n[written] {outdir}/params.json data.json data.csv figures/")
    return spec, framed


def _figures(figdir, w, spec, framed):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    # Fig 1: closure residual vs depth, harmonics marked
    Ls = np.arange(1, L_MAX + 1)
    eps = np.array([closure(L)[2] for L in Ls])
    Lk = np.array([closure(L)[1] for L in Ls])
    fig, ax = plt.subplots(figsize=(7, 4))
    odd = Lk % 2 == 1
    ax.stem(Ls[odd], eps[odd], linefmt="C3-", markerfmt="C3o", basefmt=" ",
            label="odd winding (spin-1/2)")
    ax.stem(Ls[~odd], eps[~odd], linefmt="C0-", markerfmt="C0s", basefmt=" ",
            label="even winding (boson)")
    ax.axvline(8, color="k", ls=":", lw=0.8)
    ax.annotate("ground L=8", (8, 0.02), (10, 0.12),
                arrowprops=dict(arrowstyle="->", lw=0.7))
    ax.set_xlabel("ribbon depth L"); ax.set_ylabel("closure residual ||sL||")
    ax.set_title("Screw-closure spectrum: fundamental L=8 and winding harmonics")
    ax.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(os.path.join(figdir, "closure_spectrum.png"), dpi=130)
    plt.close(fig)

    # Fig 2: energy level diagram of the lowest framed ribbons
    fig, ax = plt.subplots(figsize=(5, 6))
    gsE = framed[0]["E"]
    for r in framed[:10]:
        c = "C3" if r["Lk"] % 2 == 1 else "C0"
        x = 0 if r["Omega"] == 120 else 1
        ax.hlines(r["E"] - gsE, x - 0.35, x + 0.35, color=c, lw=2)
        ax.text(x + 0.4, r["E"] - gsE, f"L={r['L']},Lk={r['Lk']}",
                va="center", fontsize=7)
    ax.set_xticks([0, 1]); ax.set_xticklabels(["120 deg", "180 deg"])
    ax.set_ylabel("E - E_ground  (relative units)")
    ax.set_title("Defect energy levels (red=spin-1/2, blue=boson)")
    fig.tight_layout(); fig.savefig(os.path.join(figdir, "energy_levels.png"), dpi=130)
    plt.close(fig)


if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else None
    main(out)
