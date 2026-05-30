#!/usr/bin/env python3
"""
sim/lattice.py
DCCREG simulator — the quasi-2D transverse-to-[1,1,1] hexatic lattice.

The [1,1,1] screw makes the operative defect problem quasi-2D (sim/README.md):
the six outer SOSF centres project onto the plane perpendicular to [1,1,1] as a
regular hexagon (geometry/sosf.transverse_hexagon), so the natural in-plane order
is 6-fold — a TRIANGULAR lattice (the clean KTHNY hexatic case). This module
builds that lattice; biot_savart.py and the outputs ride on it.

[OC] for the lattice construction; the identification "the operative defect
plane is transverse-to-[1,1,1]" is [IR] (Block IV-§5.7, V-§9).
"""
from __future__ import annotations

import numpy as np

# triangular-lattice primitive vectors (spacing d set at build time)
_A1 = np.array([1.0, 0.0])
_A2 = np.array([0.5, np.sqrt(3.0) / 2.0])
# the 6 nearest-neighbour bond vectors (hexatic / 6-fold)
NEIGHBORS = np.array([
    _A1, _A2, _A2 - _A1, -_A1, -_A2, _A1 - _A2,
])


class TriangularLattice:
    """A triangular (hexatic) lattice of spacing d with vortex core a.

    Sites fill a disk of radius `extent`*d (for the Biot-Savart self-energy sum)
    or an n x n parallelogram (for the FFT Green's function). Origin is a site.
    """

    def __init__(self, d: float = 1.0, a: float | None = None, seed: int | None = 0):
        self.d = float(d)
        self.a = float(a) if a is not None else float(d)  # core defaults to one spacing
        self.cell_area = (np.sqrt(3.0) / 2.0) * self.d**2
        self.rng = np.random.default_rng(seed)

    # -- site generators -----------------------------------------------------
    def disk_sites(self, radius: float) -> np.ndarray:
        """All sites with |x| <= radius (radius in physical units)."""
        m = int(np.ceil(radius / self.d)) + 2
        i, j = np.meshgrid(np.arange(-m, m + 1), np.arange(-m, m + 1))
        xy = (i.ravel()[:, None] * _A1 + j.ravel()[:, None] * _A2) * self.d
        return xy[np.linalg.norm(xy, axis=1) <= radius + 1e-12]

    def grid_sites(self, n: int) -> tuple[np.ndarray, tuple[int, int]]:
        """n x n parallelogram of sites (skew coords), returned flat with shape."""
        i, j = np.meshgrid(np.arange(n), np.arange(n), indexing="ij")
        xy = (i.ravel()[:, None] * _A1 + j.ravel()[:, None] * _A2) * self.d
        return xy, (n, n)

    def basis_3d(self) -> np.ndarray:
        """The in-plane 2D basis embedded in 3D, perpendicular to [1,1,1].
        Connects the lattice back to the SOSF transverse hexagon."""
        n = np.array([1.0, 1.0, 1.0]); n /= np.linalg.norm(n)
        e1 = np.array([1.0, -1.0, 0.0]); e1 /= np.linalg.norm(e1)
        e2 = np.cross(n, e1)
        return np.array([e1, e2])


if __name__ == "__main__":
    lat = TriangularLattice(d=1.0)
    sites = lat.disk_sites(5.0)
    print(f"triangular hexatic lattice: d={lat.d}, a={lat.a}, "
          f"cell_area={lat.cell_area:.4f}")
    print(f"sites in disk R=5: {len(sites)}  (expect ~ pi*R^2/cell_area "
          f"= {np.pi*25/lat.cell_area:.0f})")
    # coordination check: 6 nearest neighbours at distance d
    d0 = np.linalg.norm(sites, axis=1)
    origin = sites[np.argmin(d0)]
    dists = np.sort(np.linalg.norm(sites - origin, axis=1))
    nn = dists[(dists > 1e-9) & (dists < 1.5 * lat.d)]
    print(f"nearest-neighbour count within 1.5d of a site: {len(nn)} (expect 6)")
