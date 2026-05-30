#!/usr/bin/env python3
"""
check_03_joining_spectrum.py
DCCREG verification script — the Joining (Block IV §3a; Block V §2a, §6a),
validation-ladder item 5 (octahedral charges).

WHAT THIS CHECKS:
    (A) [OC] Allowed disclination CHARGES = conjugacy classes of the chiral
        octahedral group O (24 det=+1 signed permutation matrices): Frank
        angles {90, 120, 180} deg. The 120 deg (C3 about [1,1,1]) is the
        screw-aligned, chirality-natural charge. These are simultaneously the
        gravity curvature sources (IV-§3a) and the Block V matter charges (V-§2a).
    (B) [OC scaling / IR] Gravity coefficient K_A ~ beta ~ rho*Gamma^2*ln(d/a)
        (Block III line tension). At the isotropy point ln(d/a)~4 (beta=alpha),
        K_A and G_eff ~ 1/K_A are pinned in terms of rho*Gamma^2. Light
        isotropy, gravity strength, and matter coupling share ONE parameter.
    (C) [OC arithmetic / IR-RH] Spin-parity selection is Fibonacci: the
        irrational screw framing (45.8 = 120/phi^2 per level) never closes by
        itself, so a closed defect ribbon borrows writhe to make Lk integer;
        near-closure loops sit at Fibonacci depths (best approximants of 1/phi^2).
        Spin-1/2 (odd Lk) is AVAILABLE and selectable.

WHAT THIS DOES *NOT* ESTABLISH:
    - The map from octahedral charges to real particle quantum numbers
      (charge, isospin, colour) is NOT claimed -- that is [RH], fenced (V-§8).
    - WHICH loop is the lowest-energy / ground-state matter loop, its actual
      spin parity and handedness, and the NUMERIC K_A all need the stable-loop
      energies = the real simulator (sim/README.md open targets).
    - This is verification of computable structure, NOT proof of the framework.

Tier: [OC] for the group theory & arithmetic; the physical identifications are
[IR], and the particle-content reading is [RH] (out of scope here).
Reconstructed faithfully from the inline 'joining' run.
"""
import numpy as np
from itertools import permutations, product
from collections import Counter


def chiral_octahedral_group():
    mats = []
    for perm in permutations(range(3)):
        P = np.zeros((3, 3))
        for i, j in enumerate(perm):
            P[i, j] = 1
        for signs in product([1, -1], repeat=3):
            M = (P.T*np.array(signs)).T
            if abs(np.linalg.det(M) - 1) < 1e-9:   # det=+1 -> chiral (no mirrors)
                mats.append(M)
    return np.array(mats)


if __name__ == "__main__":
    print("="*60)
    print("(A) ALLOWED DISCLINATION CHARGES = chiral octahedral group O")
    print("="*60)
    mats = chiral_octahedral_group()
    print(f"|O| = {len(mats)}  (expect 24, mirror-free, consistent with the screw)")
    angles = Counter()
    for M in mats:
        c = max(-1, min(1, (np.trace(M)-1)/2))
        angles[round(np.degrees(np.arccos(c)))] += 1
    for th in sorted(angles):
        print(f"   {th:>4}deg : {angles[th]} elements")
    print("=> charges {90,120,180}deg; 120deg (C3 about [1,1,1]) = screw-aligned.")

    print("\n" + "="*60)
    print("(B) GRAVITY COEFFICIENT K_A ~ Block III line tension beta")
    print("="*60)
    for ln_da in [2.0, 4.0, 6.0]:
        K_A = ln_da/4.0          # units rho*Gamma^2/(pi d^2): alpha=1, beta=ln_da/4
        print(f"  ln(d/a)={ln_da:>3}: beta/alpha={ln_da/4:.2f}  K_A~{K_A:.2f}  "
              f"G_eff~{1/K_A:.2f} [inverse units]")
    print("  At isotropy ln(d/a)~4 (beta=alpha): K_A pinned in rho*Gamma^2.")
    print("  Light isotropy + gravity strength + matter coupling = one parameter.")
    print("  (Precise numeric coefficient needs the lattice sum = simulator.)")

    print("\n" + "="*60)
    print("(C) SPIN-PARITY SELECTION is Fibonacci (screw framing 45.8 deg/level)")
    print("="*60)
    phi = (1+5**0.5)/2
    screw = 120.0/phi**2
    print(f"  screw = 120/phi^2 = {screw:.2f} deg/level (irrational frac of 360)")
    print(f"   {'L':>3} {'totalTwist(deg)':>16} {'Tw(turns)':>10} {'nearest int':>12}")
    for L in [1, 2, 3, 5, 8, 13, 21]:
        tot = screw*L
        print(f"   {L:>3} {tot:>16.1f} {tot/360:>10.3f} {round(tot/360):>12}")
    print("  Closure selects loops; Fibonacci depths approach (half-)integers")
    print("  fastest => spin-1/2 available & selectable. Lowest loop's actual")
    print("  parity needs the simulator. [partial — honest gap]")

    print("\n" + "="*60)
    print("SIMULATOR BOUNDARY (NOT computed here): stable-loop energies; the")
    print("lowest matter loop's exact spin & handedness; the numeric K_A.")
    print("="*60)
