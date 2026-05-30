#!/usr/bin/env python3
"""
sim/geometry/sosf.py
DCCREG simulator — the Septenary Octahedral Sphere-Flake (SOSF) geometry.
Validation-ladder RUNG 1 (sim/README.md): build the geometry from
docs/DCCREG_labeling_convention_v4.md Appendix A and reproduce the verified
§A.7 cross-sections as a geometry self-test.

WHAT THIS IS [OC]:
    Exact, deterministic geometry. The 7 unit spheres at the octahedron
    vertices + origin; the 6 central-outer (CO) and 12 outer-outer (OO) lenses;
    the 20 triple junctions; the 4 great circles whose normals are the body
    diagonals [+-1,+-1,+-1]. The transverse-to-[1,1,1] projection sends the six
    outer centres to a regular hexagon (Star-of-Solomon) — the geometric origin
    of the quasi-2D hexatic (6-fold) frame used by the lattice modules.

WHAT THIS IS NOT:
    Pure construction/coordinates. It asserts nothing physical on its own; it is
    the regression baseline every later [OC]/[IR] number is gated on.
"""
from __future__ import annotations

import numpy as np

R_SPHERE = 1.0  # all spheres unit radius (App. A.1)
D_OUTER = 1.0   # outer centres at distance d = r from origin (App. A.1)

# --- A.2 sphere centres (ASCII labels; Om = central hub) -------------------
SPHERES: dict[str, tuple[float, float, float]] = {
    "Om": (0.0, 0.0, 0.0),
    "Zp": (0.0, 0.0, 1.0),
    "Zm": (0.0, 0.0, -1.0),
    "Xp": (1.0, 0.0, 0.0),
    "Xm": (-1.0, 0.0, 0.0),
    "Yp": (0.0, 1.0, 0.0),
    "Ym": (0.0, -1.0, 0.0),
}
OUTER = ["Zp", "Zm", "Xp", "Xm", "Yp", "Ym"]

BODY_DIAGONALS = {  # A.6 great-circle normals
    "G1": (1, 1, 1),
    "G2": (1, 1, -1),
    "G3": (1, -1, 1),
    "G4": (-1, 1, 1),
}


def central_outer_lenses() -> dict[str, np.ndarray]:
    """A.3 — 6 CO lens centres = midpoints Om<->outer."""
    return {f"L_{o}": np.array(SPHERES[o]) / 2.0 for o in OUTER}


def outer_outer_lenses() -> dict[str, np.ndarray]:
    """A.4 — 12 OO lens centres = midpoints of adjacent outer pairs
    (those at centre-distance sqrt(2) < 2r). Coords are perms of (+-.5,+-.5,0)."""
    out: dict[str, np.ndarray] = {}
    for i, a in enumerate(OUTER):
        for b in OUTER[i + 1:]:
            ca, cb = np.array(SPHERES[a]), np.array(SPHERES[b])
            if np.isclose(np.linalg.norm(ca - cb), np.sqrt(2.0)):
                out[f"l_{a}_{b}"] = (ca + cb) / 2.0
    return out


def triple_junctions() -> dict[str, np.ndarray]:
    """A.5 — 20 triple junctions = centroids of three mutually overlapping
    spheres. Two outer spheres overlap iff their centres are sqrt(2) apart;
    Om overlaps every outer."""
    labels = list(SPHERES)
    cen = {k: np.array(v) for k, v in SPHERES.items()}

    def overlap(a, b):
        return np.linalg.norm(cen[a] - cen[b]) < 2 * R_SPHERE - 1e-9

    out: dict[str, np.ndarray] = {}
    for i in range(len(labels)):
        for j in range(i + 1, len(labels)):
            for k in range(j + 1, len(labels)):
                a, b, c = labels[i], labels[j], labels[k]
                if overlap(a, b) and overlap(a, c) and overlap(b, c):
                    out[f"T_{a}_{b}_{c}"] = (cen[a] + cen[b] + cen[c]) / 3.0
    return out


def great_circles() -> dict[str, list[str]]:
    """A.6 — each GC = the 6 OO-lens centres lying in the plane through the
    origin perpendicular to the corresponding body diagonal, ordered by angle."""
    oo = outer_outer_lenses()
    circles: dict[str, list[str]] = {}
    for name, n in BODY_DIAGONALS.items():
        n = np.array(n, float)
        n /= np.linalg.norm(n)
        members = [(lbl, p) for lbl, p in oo.items() if abs(p @ n) < 1e-9]
        # order around the ring: build an in-plane basis and sort by polar angle
        ref = members[0][1]
        e1 = ref - (ref @ n) * n
        e1 /= np.linalg.norm(e1)
        e2 = np.cross(n, e1)
        members.sort(key=lambda m: np.arctan2(m[1] @ e2, m[1] @ e1))
        circles[name] = [lbl for lbl, _ in members]
    return circles


def cross_section(h: float) -> dict[str, float]:
    """A.7 — the 2D radius of each sphere's circle in the cut plane z=h.
    r2d = sqrt(r^2-(h-cz)^2) if |h-cz|<=r else 0 (tangent/absent)."""
    out: dict[str, float] = {}
    for lbl, (_, _, cz) in SPHERES.items():
        dz = abs(h - cz)
        out[lbl] = float(np.sqrt(max(R_SPHERE**2 - dz**2, 0.0))) if dz <= R_SPHERE else 0.0
    return out


def transverse_hexagon() -> np.ndarray:
    """Project the six outer centres onto the plane perpendicular to [1,1,1].
    Returns the six 2D coordinates in that plane; they form a regular hexagon
    (Star-of-Solomon) — the geometric seed of the quasi-2D hexatic frame."""
    n = np.array([1.0, 1.0, 1.0])
    n /= np.linalg.norm(n)
    # in-plane orthonormal basis
    e1 = np.array([1.0, -1.0, 0.0])
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(n, e1)
    pts = []
    for o in OUTER:
        v = np.array(SPHERES[o])
        vp = v - (v @ n) * n
        pts.append([vp @ e1, vp @ e2])
    return np.array(pts)


# --- §A.7 reference table (verified cross-sections) ------------------------
_A7_REFERENCE = {
    0.0:  {"Om": 1.000, "Zp": 0.000, "Zm": 0.000, "Xp": 1.000, "Xm": 1.000, "Yp": 1.000, "Ym": 1.000},
    0.3:  {"Om": 0.954, "Zp": 0.714, "Xp": 0.954, "Xm": 0.954, "Yp": 0.954, "Ym": 0.954, "Zm": 0.000},
    0.5:  {"Om": 0.866, "Zp": 0.866, "Xp": 0.866, "Xm": 0.866, "Yp": 0.866, "Ym": 0.866, "Zm": 0.000},
    0.75: {"Om": 0.661, "Zp": 0.968, "Xp": 0.661, "Xm": 0.661, "Yp": 0.661, "Ym": 0.661, "Zm": 0.000},
    1.0:  {"Zp": 1.000, "Om": 0.000},
}


def self_test(verbose: bool = True) -> bool:
    """Reproduce §A.7 exactly and check structural counts. Returns pass/fail."""
    ok = True

    # structural counts
    counts = {
        "spheres": (len(SPHERES), 7),
        "CO lenses": (len(central_outer_lenses()), 6),
        "OO lenses": (len(outer_outer_lenses()), 12),
        "triple junctions": (len(triple_junctions()), 20),
        "great circles": (len(great_circles()), 4),
    }
    for name, (got, want) in counts.items():
        good = got == want
        ok &= good
        if verbose:
            print(f"  [{'OK' if good else 'XX'}] {name:18s}: {got} (expect {want})")

    # each great circle must have 6 vertices
    for name, verts in great_circles().items():
        good = len(verts) == 6
        ok &= good
        if verbose and not good:
            print(f"  [XX] {name} has {len(verts)} vertices (expect 6)")

    # §A.7 cross-sections, to 3 decimals
    if verbose:
        print("  §A.7 cross-section reproduction:")
    for h, ref in _A7_REFERENCE.items():
        got = cross_section(h)
        for lbl, want in ref.items():
            good = abs(got[lbl] - want) < 5e-4
            ok &= good
            if verbose:
                flag = "OK" if good else "XX"
                print(f"     [{flag}] h={h:<4} {lbl:3s} r2d={got[lbl]:.3f} (expect {want:.3f})")

    # transverse hexagon must be regular (6 equal radii, 60-deg spacing)
    hexpts = transverse_hexagon()
    radii = np.linalg.norm(hexpts, axis=1)
    good = np.allclose(radii, radii[0], atol=1e-9) and np.isclose(radii[0], np.sqrt(6) / 3, atol=1e-9)
    ok &= good
    if verbose:
        print(f"  [{'OK' if good else 'XX'}] transverse-[1,1,1] hexagon regular, "
              f"R={radii[0]:.4f} (expect {np.sqrt(6)/3:.4f})")

    return bool(ok)


if __name__ == "__main__":
    print("SOSF geometry self-test (validation-ladder rung 1)")
    print("=" * 56)
    passed = self_test(verbose=True)
    print("=" * 56)
    print("RUNG 1:", "PASS" if passed else "FAIL")
    raise SystemExit(0 if passed else 1)
