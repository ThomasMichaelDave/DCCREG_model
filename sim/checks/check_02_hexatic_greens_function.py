#!/usr/bin/env python3
"""
check_02_hexatic_greens_function.py
DCCREG verification script — Block IV §5.5 / §3a (the Fork-1 closure),
validation-ladder items 2 & 3.

WHAT THIS CHECKS [OC]:
    (1) Solid (rigid) disclination interaction ~ r^2 ln r  -> 1/k^4 (confining).
    (2) Hexatic (melted-position) disclination interaction ~ ln r -> 1/k^2,
        and that ln r IS the 2D Laplacian Green's function:
            integral_disk  nabla^2 ( ln r / 2pi )  ~ 1
        i.e. the hexatic disclination kernel = the 2D Newtonian/Einstein
        gravitational potential. This is the Einstein-FORM confirmation that
        closes the gravity gate qualitatively (conditional on the hexatic
        identification, which is [IR]).

WHAT THIS DOES *NOT* ESTABLISH:
    - It does NOT prove the SOSF is hexatic (that identification is [IR],
      Block IV §5.5, resting on the locked fluid + fixed-orientation features).
    - It does NOT fix the coefficient K_A or the genuine 3D coefficient
      (those need the lattice Biot-Savart sum = the real simulator).
    - A 1/k^2 static potential is necessary, not sufficient, for full nonlinear
      Einstein dynamics.

*** WITHDRAWN BLOCK (audit trail) ***
    The original inline run also printed a "screening crossover" demonstration
    using an exp(-r/xi) proxy sampled at r=3*xi, with a line claiming the ratio
    was ">>1". The printed numbers were actually <<1 -- the proxy was the WRONG
    model (in a true hexatic the confining term is REMOVED beyond the
    correlation length, not exponentially damped). That interpretation was
    WITHDRAWN in Block IV v0.6. It is preserved below, clearly fenced, because
    the audit trail is the point. The power-law / Green's-function result above
    is independent of it and stands.

Tier: [OC] for the math; the hexatic identification it rests on is [IR].
Reconstructed faithfully from the inline run used for the v0.6 closure.
"""
import numpy as np

a, Y, K_A = 1.0, 1.0, 1.0
r = np.logspace(0.1, 3.0, 400)

E_solid = (Y/(8*np.pi)) * r**2 * (np.log(r/a) - 0.5)   # rigid: r^2 ln r (1/k^4)
E_hex   = (K_A/(2*np.pi)) * np.log(r/a)                # hexatic: ln r   (1/k^2)


def loglog_slope(x, y, mask):
    lx, ly = np.log(x[mask]), np.log(np.abs(y[mask]))
    A = np.vstack([lx, np.ones_like(lx)]).T
    return np.linalg.lstsq(A, ly, rcond=None)[0]


if __name__ == "__main__":
    big = r > 100
    s_solid, _ = loglog_slope(r, E_solid, big)
    A = np.vstack([np.log(r[big]/a), np.ones(big.sum())]).T
    coef_hex, icpt_hex = np.linalg.lstsq(A, E_hex[big], rcond=None)[0]

    print("=== Power-law / form extraction (large r) ===")
    print(f"Solid:   log-log slope of E_solid = {s_solid:.3f}  (~2 + log => 1/k^4)")
    print(f"Hexatic: E_hex = ({coef_hex:.4f})*ln(r/a) + ({icpt_hex:.2e})  => 1/k^2")
    print(f"         fitted coeff vs K_A/(2pi)={K_A/(2*np.pi):.4f}")

    # --- decisive test: ln r is the 2D Laplacian Green's function ---
    N, L = 1024, 200.0
    x = np.linspace(-L/2, L/2, N, endpoint=False); dx = x[1]-x[0]
    X, Yg = np.meshgrid(x, x)
    Rg = np.sqrt(X**2 + Yg**2) + 1e-9
    G = np.log(Rg)/(2*np.pi)
    lap = (np.roll(G, 1, 0)+np.roll(G, -1, 0)+np.roll(G, 1, 1)+np.roll(G, -1, 1)-4*G)/dx**2
    disk = lap[Rg < 5*dx].sum()*dx*dx
    print("\n=== Green's-function / Einstein-form check ===")
    print(f"∫_disk ∇²(ln r /2π) dA = {disk:.3f}   (expect ≈ 1)")
    print("=> hexatic disclination kernel = 2D Laplacian Green's fn")
    print("   = 2D Newtonian/Einstein potential. [OC, conditional on hexatic = IR]")

    # ===================================================================
    # WITHDRAWN BLOCK (Block IV v0.6 self-correction) — kept for audit only.
    # The ">>1" claim below is FALSE; the proxy model is wrong. Do not use.
    # ===================================================================
    print("\n=== [WITHDRAWN — DO NOT USE] screening-crossover proxy ===")
    for xi in [10.0, 50.0, 200.0]:
        screened = E_solid*np.exp(-r/xi)
        idx = np.argmin(np.abs(r - 3*xi))
        ratio = E_hex[idx]/(screened[idx] + 1e-30)
        print(f"  xi={xi:6.1f}: E_hex/E_solid(screened) at r=3xi = {ratio:.2e}  "
              f"[original line wrongly claimed >>1]")
    print("  ^ WITHDRAWN: wrong model (hexatic removes the confining term beyond")
    print("    xi_+, it is not exp-damped). Power-law result above is unaffected.")
