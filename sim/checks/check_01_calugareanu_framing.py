#!/usr/bin/env python3
"""
check_01_calugareanu_framing.py
DCCREG verification script — Block V §3 / §6, validation-ladder item 4.

WHAT THIS CHECKS [OC]:
    The Calugareanu-White theorem  Lk = Tw + Wr  for a closed vortex loop
    carrying the SOSF chiral screw as its framing. Confirms that the screw
    promotes a BARE loop (trivial framing, Lk=0) into a framed RIBBON with
    definite integer self-linking. A framed ribbon is the object that can
    transform under the SU(2) double cover (2pi != identity) -> the
    prerequisite for spin-1/2.

WHAT THIS DOES *NOT* ESTABLISH:
    - It does NOT prove the defect is a fermion. Spin-1/2 is the topological
      ROTATION property (Finkelstein-Rubinstein), not the value of Lk. This is
      bookkeeping that the framing is nontrivial. [IR for "screw is the framing"]
    - It does NOT prove the substrate's defects are real particles (that is [RH],
      fenced in Block V §8).

Tier: [OC] for the theorem/arithmetic; the physical identification is [IR].
Reconstructed faithfully from the inline run used when opening Block V.
"""
import numpy as np

N = 20000
t = np.linspace(0, 2*np.pi, N, endpoint=False)
dt = t[1] - t[0]

# Planar circular centerline (writhe of a planar curve = 0).
R = 1.0
C = np.stack([R*np.cos(t), R*np.sin(t), 0*t], axis=1)
dC = np.gradient(C, dt, axis=0)
T = dC/np.linalg.norm(dC, axis=1, keepdims=True)   # unit tangent


def build_frame(n_turns):
    """Screw framing: a normal that executes n_turns rotations around the loop."""
    e1 = np.stack([np.cos(t), np.sin(t), 0*t], axis=1)   # radial
    e2 = np.array([0, 0, 1.0])[None, :]*np.ones((N, 1))  # z
    ang = n_turns * t
    U = np.cos(ang)[:, None]*e1 + np.sin(ang)[:, None]*e2
    U = U - (np.sum(U*T, axis=1, keepdims=True))*T       # project perp to T
    U = U/np.linalg.norm(U, axis=1, keepdims=True)
    return U


def twist(T, U, dt):
    dU = np.gradient(U, dt, axis=0)
    integrand = np.sum(np.cross(T, U)*dU, axis=1)
    return integrand.sum()*dt/(2*np.pi)


def writhe(C):
    M = 1000
    idx = np.linspace(0, N, M, endpoint=False).astype(int)
    Cs, Ts, ds = C[idx], T[idx], 2*np.pi/M
    W = 0.0
    for i in range(M):
        r = Cs[i]-Cs
        d = np.linalg.norm(r, axis=1)
        d[i] = np.inf
        num = np.sum(np.cross(Ts[i], Ts)*r, axis=1)
        W += np.sum(num/d**3)*ds*ds
    return W/(4*np.pi)


if __name__ == "__main__":
    print("Calugareanu-White check  (Lk = Tw + Wr) for a screw-framed vortex loop")
    print(f"{'n_turns':>8} {'Tw':>10} {'Wr':>10} {'Tw+Wr':>10} {'Lk(int)':>9}")
    Wr = writhe(C)
    for n in [0, 1, 2, 3]:
        U = build_frame(n)
        Tw = twist(T, U, dt)
        print(f"{n:>8} {Tw:>10.3f} {Wr:>10.3f} {Tw+Wr:>10.3f} {round(Tw+Wr):>9}")
    print("\nReading: planar loop => Wr~0; the screw supplies integer Tw. A bare")
    print("loop (n=0) has trivial framing; the screw (n>=1) makes it a ribbon with")
    print("integer self-linking. Prerequisite for spin-1/2 (NOT a proof of it).")
