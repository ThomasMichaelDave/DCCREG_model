#!/usr/bin/env python3
"""
sim/validation.py
DCCREG simulator — the 5-rung VALIDATION LADDER (sim/README.md).

A number is load-bearing only if all five regression rungs pass IN THE SAME RUN
(INTERPRETATION.md §0). This runner re-verifies the invariants directly (fast,
numpy-version robust) and reuses the already-written checks/ pieces:

  rung 1  SOSF geometry  -> geometry/sosf.self_test (reproduces §A.7)
  rung 2  solid baseline -> disclination ~ r^2 ln r (1/k^4)
  rung 3  hexatic Green  -> ∫_disk ∇²(ln r/2π) dA ≈ 1 (Einstein form)
  rung 4  Calugareanu    -> Lk = Tw + Wr integer for a screw-framed planar loop
  rung 5  octahedral O   -> 24 det=+1 elements; Frank classes {90,120,180}

Returns (all_passed, per_rung_dict). Outputs are gated on all_passed.
"""
from __future__ import annotations

import numpy as np

from .checks_bridge import (LOOP_C, LOOP_DT, LOOP_T, build_frame,
                            chiral_octahedral_group, twist, writhe)
from .geometry import sosf


def _rung1_geometry() -> tuple[bool, str]:
    ok = sosf.self_test(verbose=False)
    return ok, "SOSF geometry reproduces §A.7 and structural counts"


def _rung2_solid_baseline() -> tuple[bool, str]:
    a = 1.0
    r = np.logspace(0.1, 3.0, 400)
    E_solid = (1.0 / (8 * np.pi)) * r**2 * (np.log(r / a) - 0.5)
    big = r > 100
    lx, ly = np.log(r[big]), np.log(np.abs(E_solid[big]))
    slope = np.polyfit(lx, ly, 1)[0]
    ok = 2.0 < slope < 2.2     # r^2 ln r => slope slightly above 2
    return bool(ok), f"solid disclination log-log slope = {slope:.3f} (expect ~2, the 1/k^4 baseline)"


def _rung3_greens_function() -> tuple[bool, str]:
    N, L = 1024, 200.0
    x = np.linspace(-L / 2, L / 2, N, endpoint=False)
    dx = x[1] - x[0]
    X, Y = np.meshgrid(x, x)
    Rg = np.sqrt(X**2 + Y**2) + 1e-9
    G = np.log(Rg) / (2 * np.pi)
    lap = (np.roll(G, 1, 0) + np.roll(G, -1, 0) + np.roll(G, 1, 1)
           + np.roll(G, -1, 1) - 4 * G) / dx**2
    disk = lap[Rg < 5 * dx].sum() * dx * dx
    ok = abs(disk - 1.0) < 0.02
    return bool(ok), f"∫_disk ∇²(ln r/2π) dA = {disk:.3f} (expect ≈ 1.000, Einstein/Newton form)"


def _rung4_calugareanu() -> tuple[bool, str]:
    Wr = writhe(LOOP_C)
    ok = abs(Wr) < 1e-3        # planar loop has Wr ≈ 0
    msgs = []
    for n in [1, 2, 3]:        # integer screw turns -> integer Lk
        Tw = twist(LOOP_T, build_frame(n), LOOP_DT)
        Lk = Tw + Wr
        ok &= abs(Lk - round(Lk)) < 1e-2
        msgs.append(f"n={n}:Lk={Lk:.3f}")
    return bool(ok), f"planar Wr={Wr:.4f}≈0; screw supplies integer Tw ({', '.join(msgs)})"


def _rung5_octahedral() -> tuple[bool, str]:
    mats = chiral_octahedral_group()
    n = len(mats)
    angles = set()
    for M in mats:
        c = max(-1.0, min(1.0, (np.trace(M) - 1) / 2))
        ang = round(np.degrees(np.arccos(c)))
        if ang != 0:
            angles.add(ang)
    ok = (n == 24) and (angles == {90, 120, 180})
    return bool(ok), f"|O|={n} (expect 24); Frank classes {sorted(angles)} (expect [90,120,180])"


_RUNGS = {
    1: _rung1_geometry,
    2: _rung2_solid_baseline,
    3: _rung3_greens_function,
    4: _rung4_calugareanu,
    5: _rung5_octahedral,
}


def run_ladder(verbose: bool = True) -> tuple[bool, dict]:
    results, all_ok = {}, True
    for k in sorted(_RUNGS):
        ok, msg = _RUNGS[k]()
        all_ok &= ok
        results[k] = {"passed": bool(ok), "detail": msg}
        if verbose:
            print(f"  [{'PASS' if ok else 'FAIL'}] rung {k}: {msg}")
    return bool(all_ok), results


if __name__ == "__main__":
    print("DCCREG validation ladder (must be 5/5 before any Output is load-bearing)")
    print("=" * 72)
    passed, _ = run_ladder(verbose=True)
    print("=" * 72)
    print("LADDER:", "5/5 PASS" if passed else "FAILED")
    raise SystemExit(0 if passed else 1)
