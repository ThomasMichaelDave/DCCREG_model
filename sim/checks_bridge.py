#!/usr/bin/env python3
"""
sim/checks_bridge.py
Load the already-verified [OC] functions from sim/checks/ so the outputs reuse
them instead of re-deriving (CLAUDE.md: reuse the computed pieces). The checks
scripts guard their demos under __main__, so importing them only exposes the
module-level functions.
"""
from __future__ import annotations

import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_CHECKS = os.path.join(_HERE, "checks")


def _load(modname: str, filename: str):
    spec = importlib.util.spec_from_file_location(modname, os.path.join(_CHECKS, filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

_c01 = _load("dccreg_check01", "check_01_calugareanu_framing.py")
_c03 = _load("dccreg_check03", "check_03_joining_spectrum.py")

# re-exported verified pieces
twist = _c01.twist
writhe = _c01.writhe
build_frame = _c01.build_frame          # uses check_01 module globals t, T, N
chiral_octahedral_group = _c03.chiral_octahedral_group
# the planar reference loop check_01 builds (centerline C, tangent T, step dt)
LOOP_C = _c01.C
LOOP_T = _c01.T
LOOP_DT = _c01.dt
