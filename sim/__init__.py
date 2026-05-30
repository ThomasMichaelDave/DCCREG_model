"""DCCREG simulator package.

Computes the open targets of sim/README.md (the SOSF defect spectrum):
  Output A — numeric K_A (lattice Biot-Savart sum) -> G_eff
  Output B — defect spectrum + ground-state matter loop (the decisive test)
  Output C — E(r) interaction law on the lattice

Read ../CLAUDE.md (firewall) and README.md (target spec) before trusting any
number. Every load-bearing result is gated behind the 5-rung validation ladder
(see validation.py) and written with its reproducibility log to results/.
"""
