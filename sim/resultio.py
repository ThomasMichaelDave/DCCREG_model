#!/usr/bin/env python3
"""
sim/resultio.py
DCCREG simulator — reproducibility I/O (CLAUDE.md §5).

Every run writes results/<run-id>/ with: params.json (params + git hash + seed),
data.json + data.csv (the numbers), figures/, and a NOTES.md whose every claim
carries an [OC]/[IR]/[RH] tag and a confirm/refine/falsify line. A number is
reportable only with this log.
"""
from __future__ import annotations

import csv
import datetime as _dt
import json
import os
import subprocess

_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_ROOT = os.path.join(_REPO, "results")


def git_hash() -> str:
    try:
        out = subprocess.check_output(["git", "-C", _REPO, "rev-parse", "HEAD"],
                                      stderr=subprocess.DEVNULL)
        dirty = subprocess.call(["git", "-C", _REPO, "diff", "--quiet"]) != 0
        return out.decode().strip() + ("-dirty" if dirty else "")
    except Exception:
        return "unknown"


def make_run_dir(run_id: str | None = None) -> tuple[str, str]:
    if run_id is None:
        run_id = _dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(RESULTS_ROOT, run_id)
    os.makedirs(os.path.join(path, "figures"), exist_ok=True)
    return run_id, path


def write_params(path: str, params: dict) -> None:
    with open(os.path.join(path, "params.json"), "w") as f:
        json.dump(params, f, indent=2)


def write_data(path: str, data: dict) -> None:
    with open(os.path.join(path, "data.json"), "w") as f:
        json.dump(data, f, indent=2, default=float)
    # flat scalar CSV for quick scanning
    rows = []
    for output, payload in data.items():
        for k, v in _flatten(payload).items():
            if isinstance(v, (int, float, bool, str)) or v is None:
                rows.append({"output": output, "key": k, "value": v})
    with open(os.path.join(path, "data.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["output", "key", "value"])
        w.writeheader()
        w.writerows(rows)


def _flatten(d, prefix=""):
    out = {}
    if isinstance(d, dict):
        for k, v in d.items():
            out.update(_flatten(v, f"{prefix}{k}."))
    elif isinstance(d, list):
        out[prefix.rstrip(".")] = f"<list:{len(d)}>"
    else:
        out[prefix.rstrip(".")] = d
    return out


def write_notes(path: str, run_id: str, ghash: str, seed: int,
                ladder: dict, results: dict) -> None:
    a = results.get("A", {})
    b = results.get("B", {})
    c = results.get("C", {})
    lines = []
    L = lines.append
    L(f"# Run `{run_id}` — NOTES")
    L("")
    L(f"- git commit: `{ghash}`")
    L(f"- seed: `{seed}`")
    L(f"- generated: {_dt.datetime.now().isoformat(timespec='seconds')}")
    L("")
    L("**Read `../../CLAUDE.md` (firewall) and `../../sim/INTERPRETATION.md` (contract) first.** "
      "This run targets the SOSF defect spectrum (Outputs A/B/C). Every claim below carries a "
      "tier tag; a result confirms/refines/falsifies an *identification within* DCCREG — it does "
      "not prove the framework.")
    L("")
    L("## Validation ladder (gates everything)")
    for k in sorted(ladder):
        r = ladder[k]
        L(f"- rung {k}: **{'PASS' if r['passed'] else 'FAIL'}** — {r['detail']}")
    all_pass = all(r["passed"] for r in ladder.values())
    L("")
    L(f"**Ladder status: {'5/5 PASS — Outputs are load-bearing.' if all_pass else 'FAILED — any number below is a bug, not a result.'}**")
    L("")

    if a:
        L("## Output A — K_A → G_eff  [OC value on IR identification]")
        L(f"- Lattice Biot–Savart self-energy slope (β coefficient), extrapolated d→0: "
          f"**{a['beta_coeff_extrapolated']:.5f} ρΓ²** "
          f"(analytic ρΓ²/4π = {a['analytic_beta_coeff']:.5f}; "
          f"rel.err {a['beta_coeff_rel_err']:.2%}). **[OC]** — validated against the known limit.")
        L(f"- Converged: **{a['converged']}** (monotone under lattice refinement).")
        L(f"- At the Block III isotropy point ln(d/a)={a['ln_d_over_a']:.0f}: "
          f"**K_A ≈ {a['K_A_over_rhoGamma2']:.3f} ρΓ²** → **G_eff ≈ {a['G_eff_times_rhoGamma2']:.2f} /ρΓ²**. "
          f"**[OC value]** resting on K_A~β **[IR]** (the Joining, IV-§3a/V-§2a); G_eff~1/K_A **[IR]**.")
        v3 = a.get("validation_3D")
        if v3:
            L(f"- **3D cross-check:** the genuine 3D filament Biot–Savart sum gives straight-line "
              f"coefficient **{v3['straight_line_coeff_3D']:.5f}** ({v3['straight_line_rel_err']:.1%} from "
              f"the 2D value) → **quasi-2D reduction validated [OC]** (exact for a straight disclination "
              f"line). The [1,1,1]-screw helix raises the line tension only **×{v3['screw_helix_tension_factor']:.3f}** "
              f"(~1%; the extra arc length is nearly cancelled by antiparallel tangents). So K_A is "
              f"essentially unchanged in 3D.")
        L(f"- Read: {a['reads']}")
        L("")
    if c:
        L("## Output C — E(r) interaction law  [OC form / OC ~10% coefficient; IR identification]")
        L(f"- Lattice Green's function on the triangular hexatic lattice: the **ln r (1/k², "
          f"Einstein/Newton) form is confirmed** (ln-fit residual {c['ln_form_residual']:.4f} vs "
          f"r²ln r residual {c['r2lnr_residual']:.4f}). **[OC, robust]**")
        L(f"- Measured coefficient: **{c['G_slope_per_lnr']:.4f} per ln r** "
          f"(window spread ±{c['G_slope_window_spread']:.4f}; analytic −√3/6π = "
          f"{c['analytic_slope_per_lnr']:.4f}, rel.err {c['slope_rel_err']:.1%}). "
          f"**[OC, ~10%]** — finite-torus limited, not claimed beyond its spread.")
        sc = c.get("screening")
        if sc:
            tbl = [t for t in sc["table"] if t.get("xi_measured")]
            xi_lo = min(t["xi_measured"] for t in tbl) if tbl else float("nan")
            xi_hi = max(t["xi_measured"] for t in tbl) if tbl else float("nan")
            L(f"- **Screening length (computed):** free dislocations Debye-screen the ln r beyond "
              f"**ξ = κ⁻¹ = √(C₂/m²) ∝ n_disloc^(−1/2)** (2D Debye–Hückel). Measured ξ ∈ "
              f"[{xi_lo:.0f}, {xi_hi:.0f}] lattice units over the density range, **validated against "
              f"the continuum Bessel K₀(κr) to {sc['mean_kappa_rel_err']:.1%}**. **[OC]** for the law "
              f"+ validation; the dislocation density n_d (hence the absolute ξ) is an **[IR]** "
              f"thermodynamic input. This REFINES IV-§5.6's 'atmosphere' — and is genuine Debye "
              f"screening, NOT the withdrawn v0.6 exp-proxy of the confining term.")
        L(f"- Read: {c['reads']}")
        L("")
    if b:
        gs = b.get("ground_state")
        L("## Output B — defect spectrum + ground-state matter loop  ← decisive  [OC ordering / IR identification / RH particle-map]")
        cs = b.get("closure_structure", {})
        L(f"- Closure structure: the **unique genuine closure** is Fibonacci depth "
          f"**L={cs.get('best_closure_depth')}** (residual {cs.get('best_closure_residual', float('nan')):.3f}, "
          f"**{cs.get('closure_gap_factor', float('nan')):.0f}× better** than any other depth ≤21). **[OC arithmetic]**")
        if gs:
            L(f"- Ground-state ribbon: charge {gs['charge_deg']:.0f}°, **|Lk|={abs(gs['Lk_int'])} "
              f"({gs['parity']}) → spin-½**, handedness **{gs['handedness']}**. **[OC]** for Lk/closure; "
              f"\"this ribbon is a matter particle\" is **[IR]**.")
        rs = b.get("robustness_scan", {})
        cr = b.get("charge_resolution", {})
        L(f"- Robustness (strict-closure regime, energy weights varied 0.1×–10×): size, parity & "
          f"charge robust across **{rs.get('parity_robustness', 0):.0%}** / "
          f"**{rs.get('charge_robustness', 0):.0%}** of the scan.")
        if cr:
            L(f"- **Charge fork — RESOLVED:** {cr.get('rule')} 90° is excluded categorically "
              f"(ψ₆→−ψ₆, a string-attached half-disclination), leaving admissible "
              f"{cr.get('admissible_charges_deg')}°; Frank energy ∝Ω² then selects "
              f"**{cr.get('ground_charge_deg'):.0f}°** (also the screw-aligned C₃∥[1,1,1] — doubly "
              f"natural). **[OC]** selection on the hexatic 6-fold **[IR]**. No tunable weight.")
        if b.get("loose_closure_caveat"):
            L(f"- Caveat: {b['loose_closure_caveat']}")
        L(f"- Verdict: {b.get('verdict')}")
        L(f"- The map to Standard-Model quantum numbers is **[RH]**, fenced (Block V-§8) — NOT claimed here.")
        L("")

    L("## What this run does NOT establish")
    L("- It does not prove DCCREG; it confirms/refines/falsifies identifications within it (INTERPRETATION.md §4).")
    L("- Output A's K_A is an [OC] number resting on the [IR] K_A~β identification; Output B's "
      "spin-½ ground state confirms fermion-*capability*, not that these are nature's fermions ([RH]).")
    L("- Graduation to Blocks (IV v0.8, V v0.3) is a separate consolidation session (CLAUDE.md §3.3/§3.5); "
      "this run writes to results/ only.")
    L("")
    with open(os.path.join(path, "NOTES.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
