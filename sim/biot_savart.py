#!/usr/bin/env python3
"""
sim/biot_savart.py
DCCREG simulator — Biot-Savart machinery on the hexatic lattice.

The only fundamental field is the vorticity omega; the velocity is its
Biot-Savart readout u = curl A, A = (1/4pi) int omega/|x-x'| (Block I-§7). In the
quasi-2D transverse-to-[1,1,1] plane a vortex line pierces the plane as a 2D
point vortex with azimuthal velocity |u| = Gamma/(2 pi r).

This module computes, by direct LATTICE summation of the kinetic energy
density E = (rho/2) int |u|^2 dA, the self-energy of a vortex out to radius R.
The known continuum limit is

        E(R) = (rho Gamma^2 / 4 pi) ln(R/a),                       [OC]

so the slope of E vs ln(R/a) converges to the line-tension coefficient
beta_coeff = rho Gamma^2 / (4 pi). This is the lattice Biot-Savart sum that
turns the parametric K_A ~ beta (the Joining, IV-§3a/V-§2a) into a number.
Validating the lattice sum against this analytic slope is the convergence test
output_a_KA.py gates on.
"""
from __future__ import annotations

import numpy as np

from .lattice import TriangularLattice


def velocity_magnitude(r: np.ndarray, gamma: float, a: float) -> np.ndarray:
    """2D point-vortex azimuthal speed Gamma/(2 pi r), regularised inside the
    core (rigid rotation |u| = Gamma r / (2 pi a^2) for r < a)."""
    r = np.asarray(r, float)
    out = np.empty_like(r)
    outside = r >= a
    out[outside] = gamma / (2 * np.pi * r[outside])
    out[~outside] = gamma * r[~outside] / (2 * np.pi * a**2)
    return out


def self_energy_lattice(lat: TriangularLattice, R: float,
                        rho: float = 1.0, gamma: float = 1.0) -> float:
    """Lattice Biot-Savart self-energy: sum (rho/2)|u|^2 * cell_area over sites
    in a disk of radius R (core site at origin excluded; its core energy is a
    finite constant absorbed into the offset of the ln fit)."""
    sites = lat.disk_sites(R)
    r = np.linalg.norm(sites, axis=1)
    keep = r >= lat.a  # exclude the core plaquette (constant offset)
    u = velocity_magnitude(r[keep], gamma, lat.a)
    return float(0.5 * rho * np.sum(u**2) * lat.cell_area)


def beta_coefficient(lat: TriangularLattice, R_values: np.ndarray,
                     rho: float = 1.0, gamma: float = 1.0) -> tuple[float, float, np.ndarray]:
    """Fit E(R) = beta_coeff * ln(R/a) + const over a range of system radii R.
    Returns (beta_coeff, intercept, energies)."""
    E = np.array([self_energy_lattice(lat, R, rho, gamma) for R in R_values])
    x = np.log(R_values / lat.a)
    A = np.vstack([x, np.ones_like(x)]).T
    slope, intercept = np.linalg.lstsq(A, E, rcond=None)[0]
    return float(slope), float(intercept), E


ANALYTIC_BETA_COEFF = 1.0 / (4 * np.pi)  # rho=Gamma=1: continuum slope


if __name__ == "__main__":
    print("Biot-Savart lattice self-energy convergence (rho=Gamma=1)")
    print(f"analytic slope rho*Gamma^2/(4pi) = {ANALYTIC_BETA_COEFF:.6f}")
    R_values = np.array([20.0, 40.0, 80.0, 160.0])
    for refine in [1.0, 0.5, 0.25, 0.125]:
        lat = TriangularLattice(d=refine, a=refine)
        slope, icpt, _ = beta_coefficient(lat, R_values)
        err = abs(slope - ANALYTIC_BETA_COEFF) / ANALYTIC_BETA_COEFF
        print(f"  d={refine:<6} slope={slope:.6f}  rel.err={err:6.2%}")
