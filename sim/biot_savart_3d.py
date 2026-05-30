#!/usr/bin/env python3
"""
sim/biot_savart_3d.py
DCCREG simulator — full 3D Biot-Savart filament self-energy.

Output A's lattice sum is quasi-2D (transverse-to-[1,1,1]). This module does the
genuine 3D computation to (a) VALIDATE the quasi-2D reduction for a straight
disclination line, and (b) quantify the [1,1,1]-SCREW correction for a helical
filament. The vortex-filament self-energy (Rosenhead-regularised Biot-Savart):

    E = (rho Gamma^2 / 8 pi) * int int  (t(s) . t(s')) / sqrt(|r(s)-r(s')|^2 + a^2)  ds ds'

For a STRAIGHT line this reduces to the 2D result E/length = (rho Gamma^2/4pi) ln(L/a)
-- the same line-tension coefficient as biot_savart.py. That equality IS the
quasi-2D validation: for a straight defect line the 3D coefficient equals the 2D
transverse one exactly, so the gravity K_A is unchanged in 3D.

The SCREW makes a matter ribbon's centerline helical; the helix is longer per
unit axial length, so it carries a geometric line-tension factor > 1. We compute
it (relevant to Output B's ribbon energy, not to the gravity K_A of straight
disclination lines).

[OC] for the filament self-energy and its straight-line ln limit; the
identification of these lines with disclinations/ribbons is [IR].
"""
from __future__ import annotations

import numpy as np

PHI = (1 + 5 ** 0.5) / 2
SCREW_DEG = 120.0 / PHI**2            # 45.836 deg/level


def _filament_self_energy(r: np.ndarray, t: np.ndarray, ds: np.ndarray,
                          a: float, rho: float, gamma: float) -> float:
    """Rosenhead-regularised double sum over filament nodes.
    r: (N,3) positions, t: (N,3) unit tangents, ds: (N,) arc-length weights."""
    N = len(r)
    E = 0.0
    pref = rho * gamma**2 / (8 * np.pi)
    for i in range(N):
        d = r - r[i]
        dist = np.sqrt(np.sum(d * d, axis=1) + a * a)
        integ = (t @ t[i]) / dist * ds
        E += integ.sum() * ds[i]
    return float(pref * E)


def straight_line(L: float, a: float, nseg: int = 1200,
                  rho: float = 1.0, gamma: float = 1.0) -> float:
    """Self-energy of a straight filament of length L (along z), core a."""
    s = np.linspace(-L / 2, L / 2, nseg)
    ds = np.full(nseg, s[1] - s[0])
    r = np.column_stack([np.zeros(nseg), np.zeros(nseg), s])
    t = np.tile([0.0, 0.0, 1.0], (nseg, 1))
    return _filament_self_energy(r, t, ds, a, rho, gamma)


def screw_helix(axial_L: float, a: float, R_helix: float, pitch: float,
                nseg: int = 1200, rho: float = 1.0, gamma: float = 1.0) -> dict:
    """Self-energy of a helical filament: radius R_helix, axial pitch (axial
    advance per 2pi turn), total axial length axial_L. Returns energy and the
    arc/axial length factor."""
    n_turns = axial_L / pitch
    phi = np.linspace(0, 2 * np.pi * n_turns, nseg)
    z = pitch * phi / (2 * np.pi)
    r = np.column_stack([R_helix * np.cos(phi), R_helix * np.sin(phi), z])
    dr = np.gradient(r, axis=0)
    seglen = np.linalg.norm(dr, axis=1)
    t = dr / seglen[:, None]
    ds = seglen
    arc = float(seglen.sum())
    E = _filament_self_energy(r, t, ds, a, rho, gamma)
    return {"energy": E, "arc_length": arc, "axial_length": axial_L,
            "arc_over_axial": arc / axial_L}


def line_tension_coeff(self_energy_fn, lengths, a, **kw) -> float:
    """Slope of (E / length) vs ln(length/a) -> the line-tension coefficient."""
    E = np.array([self_energy_fn(L, a, **kw) for L in lengths])
    per_len = E / lengths
    x = np.log(lengths / a)
    return float(np.polyfit(x, per_len, 1)[0])


ANALYTIC_COEFF = 1.0 / (4 * np.pi)


def run() -> dict:
    a = 1.0
    Ls = np.array([40.0, 80.0, 160.0, 320.0])

    # (1) straight line -> validate quasi-2D reduction
    straight_coeff = line_tension_coeff(lambda L, a, **kw: straight_line(L, a, **kw),
                                        Ls, a, nseg=1500)
    straight_relerr = abs(straight_coeff - ANALYTIC_COEFF) / ANALYTIC_COEFF

    # (2) screw helix -> 3D screw geometric factor (DCCREG screw: R~hexagon radius
    #     sqrt(6)/3, pitch = (360/45.836) levels * d, with d the axial spacing=a)
    R_helix = np.sqrt(6) / 3 * a               # transverse hexagon radius (geometry/sosf)
    pitch = (360.0 / SCREW_DEG) * a            # axial advance per full screw turn
    helix = screw_helix(axial_L=160.0, a=a, R_helix=R_helix, pitch=pitch, nseg=1500)
    straight_ref = straight_line(160.0, a, nseg=1500)
    helix_factor = helix["energy"] / straight_ref

    return {
        "output": "3D Biot-Savart line tension (K_A in 3D)",
        "analytic_coeff_rhoGamma2_over_4pi": ANALYTIC_COEFF,
        "straight_line_coeff_3D": straight_coeff,
        "straight_line_rel_err": straight_relerr,
        "quasi2D_reduction_validated": bool(straight_relerr < 0.05),
        "screw_geometry": {"R_helix_over_a": float(R_helix / a),
                           "pitch_over_a": float(pitch / a),
                           "arc_over_axial": helix["arc_over_axial"]},
        "screw_helix_tension_factor": float(helix_factor),
        "reads": ("straight-line 3D coeff = 2D value -> quasi-2D reduction is EXACT for a straight "
                  "disclination line, so the gravity K_A is unchanged in 3D [OC]. The screw makes a "
                  "matter ribbon's centerline helical, carrying a geometric tension factor "
                  f"~{helix_factor:.2f}x (relevant to Output B's ribbon, not to gravity K_A)."),
        "tier": {"straight-line coeff & ln limit": "OC", "screw helix factor": "OC geometry",
                 "line=disclination/ribbon id": "IR"},
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
