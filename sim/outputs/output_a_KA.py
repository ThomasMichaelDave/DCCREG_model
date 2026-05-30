#!/usr/bin/env python3
"""
sim/outputs/output_a_KA.py
DCCREG simulator — OUTPUT A: the numeric coupling K_A -> G_eff.

Method (sim/README.md open target 3; INTERPRETATION.md Output A):
  The lattice Biot-Savart self-energy sum (biot_savart.py) gives the vortex
  line-tension coefficient beta_coeff = rho Gamma^2 / (4 pi) as the slope of
  E(R) vs ln(R/a). Lattice refinement (d -> 0) is Richardson-extrapolated to the
  continuum and validated against the analytic slope. The Joining (IV-§3a,
  V-§2a) identifies K_A ~ beta, so at Block III's light-isotropy point
  ln(d/a) ~ 4 (where beta = alpha) we report
        K_A   = beta_coeff * ln(d/a)            [number]
        G_eff ~ 1 / K_A.

Tier:
  - beta_coeff (the lattice-sum slope) and its convergence: [OC].
  - K_A = beta_coeff*ln(d/a) AT the isotropy point: [OC value] resting on the
    K_A ~ beta identification, which is [IR] (the Joining).
  - G_eff ~ 1/K_A: [IR] (the gravity-strength identification, Block IV).

Confirm / refine / falsify (INTERPRETATION.md): a converged beta_coeff that is
O(1)*rho Gamma^2 CONFIRMS K_A ~ beta and REFINES gravity strength into a number;
an order-of-magnitude mismatch with the line-tension scale would FALSIFY the
shared-parameter identification.
"""
from __future__ import annotations

import numpy as np

from ..biot_savart import ANALYTIC_BETA_COEFF, beta_coefficient
from ..lattice import TriangularLattice

LN_D_OVER_A_ISOTROPY = 4.0  # Block III isotropy point (beta = alpha, A = 1)


def richardson_extrapolate(d_values: np.ndarray, slopes: np.ndarray) -> float:
    """Linear extrapolation of slope(d) to d -> 0 (leading lattice error ~ d^2)."""
    A = np.vstack([d_values**2, np.ones_like(d_values)]).T
    coeff = np.linalg.lstsq(A, slopes, rcond=None)[0]
    return float(coeff[1])  # intercept = d->0 limit


def run(rho: float = 1.0, gamma: float = 1.0,
        d_values=(1.0, 0.5, 0.25, 0.125),
        R_values=(20.0, 40.0, 80.0, 160.0),
        figures_dir=None) -> dict:
    d_values = np.array(d_values, float)
    R_values = np.array(R_values, float)

    slopes, conv = [], []
    for d in d_values:
        lat = TriangularLattice(d=d, a=d, seed=0)
        slope, icpt, E = beta_coefficient(lat, R_values, rho, gamma)
        slopes.append(slope)
        conv.append({
            "d": float(d),
            "beta_coeff": float(slope),
            "rel_err_vs_analytic": float(abs(slope - ANALYTIC_BETA_COEFF) / ANALYTIC_BETA_COEFF),
        })
    slopes = np.array(slopes)
    beta_coeff = richardson_extrapolate(d_values, slopes)
    rel_err = abs(beta_coeff - ANALYTIC_BETA_COEFF) / ANALYTIC_BETA_COEFF

    # monotone convergence is the trust criterion
    converged = bool(np.all(np.diff(np.abs(slopes - ANALYTIC_BETA_COEFF)) < 1e-9)
                     and rel_err < 0.05)

    K_A = beta_coeff * LN_D_OVER_A_ISOTROPY        # units rho*Gamma^2
    G_eff = 1.0 / K_A if K_A != 0 else float("inf")

    result = {
        "output": "A: K_A -> G_eff",
        "rho": rho, "gamma": gamma,
        "analytic_beta_coeff": ANALYTIC_BETA_COEFF,
        "beta_coeff_extrapolated": beta_coeff,
        "beta_coeff_rel_err": rel_err,
        "convergence": conv,
        "converged": converged,
        "ln_d_over_a": LN_D_OVER_A_ISOTROPY,
        "K_A_over_rhoGamma2": K_A,
        "G_eff_times_rhoGamma2": G_eff,
        "tier": {"beta_coeff": "OC", "K_A": "OC value on IR identification (K_A~beta)",
                 "G_eff": "IR"},
        "reads": ("O(1)*rhoGamma^2 -> CONFIRMS K_A~beta and REFINES gravity strength; "
                  "order-of-magnitude mismatch would FALSIFY the shared-parameter id."),
    }

    if figures_dir is not None:
        _plot(d_values, slopes, beta_coeff, figures_dir)
    return result


def _plot(d_values, slopes, beta_coeff, figures_dir):
    import os
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    os.makedirs(figures_dir, exist_ok=True)
    fig, ax = plt.subplots(figsize=(5, 4))
    dd = np.linspace(0, d_values.max() ** 2, 50)
    ax.plot(d_values**2, slopes, "o", label="lattice-sum slope")
    A = np.vstack([d_values**2, np.ones_like(d_values)]).T
    m, b = np.linalg.lstsq(A, slopes, rcond=None)[0]
    ax.plot(dd, m * dd + b, "-", label=f"extrap d->0: {beta_coeff:.5f}")
    ax.axhline(ANALYTIC_BETA_COEFF, ls="--", color="k",
               label=f"analytic 1/4pi = {ANALYTIC_BETA_COEFF:.5f}")
    ax.set_xlabel("lattice spacing$^2$  $d^2$")
    ax.set_ylabel(r"$\beta$ coefficient (slope of $E$ vs $\ln R/a$)")
    ax.set_title("Output A: Biot-Savart lattice sum -> $K_A$ convergence")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(figures_dir, "output_a_KA_convergence.png"), dpi=130)
    plt.close(fig)


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
