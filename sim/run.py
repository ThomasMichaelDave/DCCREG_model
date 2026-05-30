#!/usr/bin/env python3
"""
sim/run.py
DCCREG simulator — orchestrator. Runs the validation ladder (must pass), then the
selected Outputs, and writes the full reproducibility log to results/<run-id>/.

Usage:
    python -m sim.run                       # full run, auto run-id
    python -m sim.run --run-id myrun        # named run
    python -m sim.run --outputs A C         # subset
    python -m sim.run --seed 0 --quick      # faster (smaller lattices)

A number is load-bearing ONLY if the ladder is 5/5 in the same run (CLAUDE.md;
INTERPRETATION.md §0). If the ladder fails, Outputs are still computed but are
clearly flagged in the log as NOT load-bearing.
"""
from __future__ import annotations

import argparse
import json
import os

import numpy as np

from . import resultio, validation
from .outputs import output_a_KA, output_b_spectrum, output_c_Er


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="DCCREG SOSF defect-spectrum simulator")
    p.add_argument("--run-id", default=None)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--outputs", nargs="+", default=["A", "B", "C"], choices=["A", "B", "C"])
    p.add_argument("--quick", action="store_true", help="smaller lattices for a fast pass")
    args = p.parse_args(argv)

    np.random.seed(args.seed)
    run_id, path = resultio.make_run_dir(args.run_id)
    figs = os.path.join(path, "figures")
    ghash = resultio.git_hash()

    print(f"=== DCCREG simulator run '{run_id}'  (git {ghash}, seed {args.seed}) ===\n")

    print("Validation ladder:")
    ladder_ok, ladder = validation.run_ladder(verbose=True)
    print(f"  -> {'5/5 PASS' if ladder_ok else 'LADDER FAILED — outputs NOT load-bearing'}\n")

    results: dict = {}
    if "A" in args.outputs:
        print("Output A (K_A -> G_eff): lattice Biot-Savart sum ...")
        d_vals = (1.0, 0.5, 0.25) if args.quick else (1.0, 0.5, 0.25, 0.125)
        R_vals = (20.0, 40.0, 80.0) if args.quick else (20.0, 40.0, 80.0, 160.0)
        results["A"] = output_a_KA.run(d_values=d_vals, R_values=R_vals, figures_dir=figs)
        print(f"  K_A = {results['A']['K_A_over_rhoGamma2']:.3f} rhoGamma^2, "
              f"G_eff = {results['A']['G_eff_times_rhoGamma2']:.2f}, "
              f"converged={results['A']['converged']}\n")
    if "C" in args.outputs:
        print("Output C (E(r) interaction law): lattice Green's function ...")
        n = 256 if args.quick else 512
        K_A = results.get("A", {}).get("K_A_over_rhoGamma2", 0.3162)
        results["C"] = output_c_Er.run(n=n, K_A=K_A, figures_dir=figs)
        print(f"  ln r form: {results['C']['ln_form_beats_r2lnr']}, "
              f"coeff={results['C']['G_slope_per_lnr']:.4f}\n")
    if "B" in args.outputs:
        print("Output B (defect spectrum + ground state): the decisive test ...")
        beta = results.get("A", {}).get("beta_coeff_extrapolated", 0.0791)
        K_A = results.get("A", {}).get("K_A_over_rhoGamma2", 0.3162)
        results["B"] = output_b_spectrum.run(beta_coeff=beta, K_A=K_A, figures_dir=figs)
        print(f"  {results['B']['verdict']}\n")

    params = {
        "run_id": run_id, "git_commit": ghash, "seed": args.seed,
        "outputs": args.outputs, "quick": args.quick,
        "ladder_passed": ladder_ok,
        "note": "A number is load-bearing only if ladder_passed is true (INTERPRETATION.md §0).",
    }
    resultio.write_params(path, params)
    resultio.write_data(path, results)
    resultio.write_notes(path, run_id, ghash, args.seed, ladder, results)

    rel = os.path.relpath(path, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print(f"=== written to {rel}/ (params.json, data.json, data.csv, figures/, NOTES.md) ===")
    return 0 if ladder_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
