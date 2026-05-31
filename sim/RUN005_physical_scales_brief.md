# DCCREG Simulator — Run Brief: Physical Scales & Dimensionless Ratios

**Target run:** `run005_physical_scales`
**Reads first:** `../CLAUDE.md`, `README.md`, `INTERPRETATION.md`, and the four prior
reports in `../results/` (run002 K_A; run003 spectrum; run004 Dirac mass; master index).
**Branch from:** the run002 `sim.run` harness (the physical-unit K_A / lattice machinery)
**and** the run004 closure/coupling machinery (`check_05`).

---

## 0. The honest scope (read this before building anything)

The framework carries **free dimensional inputs by design** (locked, not bugs):
- $\rho$ (substrate density), $\Gamma$ (circulation quantum), $\ell_P$ (Planck cutoff) — the base scales;
- $2m/q$ — the Block II dictionary constant (II-§8 flag 1), explicitly "the single free dimensional input the dictionary requires";
- $J$ — the run004 inter-sublattice coupling (sets the Dirac-mass magnitude);
- $\ln(d/a)$ — the lattice-spacing-to-core ratio (Block III; isotropy at ≈4).

**Therefore RUN005 cannot and must not output absolute SI values** (an "electron mass in kg", a "G in m³/kg/s²"). Doing so would mean inventing inputs — a firewall breach. What it **can** do, and what this run is *for*:

> **Reduce every computed quantity to the minimal set of free inputs, and compute the dimensionless RATIOS and exponents that are input-independent.** Those ratios are the framework's actual falsifiable content — they survive any choice of the free scales.

This is the difference between "internally consistent structure" (where we are) and "numbers that constrain anything" (the ratios). The run succeeds by producing ratios, not absolutes.

---

## 1. The questions (in priority order)

1. **What is the minimal free-input set?** Confirm by dimensional analysis that all of {gravity $G_{\rm eff}$, the Dirac mass $m_D$, the screening length $\xi$, the defect-spectrum energies} reduce to combinations of $\{\rho,\Gamma,\ell_P,\,2m/q,\,J,\,\ln(d/a)\}$ — and that no *hidden* extra input has crept in. [OC dimensional analysis]
2. **Which dimensionless ratios are pinned (input-independent)?** Compute the ratios that do **not** depend on the free inputs — e.g. the ratio of the antibonding gap to the first-excited gap (run004 gave 2.000 vs 5.00 → 0.4 at J=1, but how does it move with J?), the ratio of the 180°-tower offset to the 120° ground energy (×2.25 in charge², run003), the ratio of successive winding-harmonic energies ($L\approx8n$). [OC arithmetic]
3. **What is the $G_{\rm eff}$–$m_D$ relation?** Both descend from the *same* lattice stiffness ($K_A\sim\beta\sim\rho\Gamma^2\ln(d/a)$, IV-§3a) and the same defect geometry. Is there a fixed dimensionless relation between the gravitational coupling and the Dirac mass — i.e. does the "one shared parameter" (the Joining) force a $G_{\rm eff}\,m_D^2$-type combination to be a pure number? **This is the highest-value target:** a pinned gravity–mass ratio would be the strongest cross-gate prediction the framework can make. [OC if it falls out; IR for the identification]

---

## 2. What to build

1. **Dimensional reduction layer.** Express $G_{\rm eff}$ (run002), $m_D$ (run004), $\xi$ (run002), and the spectrum energies (run003) symbolically in terms of the free-input set. Tabulate units and the free-input dependence of each. (Symbolic/`sympy` is fine; this is bookkeeping, but it is the load-bearing bookkeeping.)
2. **Ratio extractor.** For every pair of computed quantities, form the dimensionless ratio and determine whether the free inputs cancel. Output the list of **input-independent ratios** (the predictions) separately from the **input-dependent** ones (which need a scale choice).
3. **The $J$ and $\ln(d/a)$ scans.** Re-express run004's $m_D(J)$ and run002's $G_{\rm eff}(\ln d/a)$ on common footing; find any combination in which $J$ or $\ln(d/a)$ cancels between gravity and mass.
4. **(If feasible) first-principles $J$.** run004 modelled $J$ as a scanned multiple of the mutual-helicity unit. A first-principles lattice computation of the A–B mutual linking on the real SOSF skeleton (run004 residual) would *fix* $J$ in terms of $\rho\Gamma^2$ — collapsing one free input. Attempt it; if it doesn't converge, leave $J$ free and say so.

---

## 3. The branches — pre-committed

### B-PINNED — a cross-gate ratio is input-independent
**Trigger:** at least one nontrivial dimensionless ratio (ideally the $G_{\rm eff}$–$m_D$ relation, §1.3) comes out **independent of all free inputs**, robust across the $J$ and $\ln(d/a)$ scans.
**Meaning:** the framework makes a genuine parameter-free prediction — a pure number relating two sectors. This is the strongest possible RUN005 outcome.
**Graduation:** a new short cross-block note (or Block IV/V joint addendum) recording the ratio [OC for the arithmetic; IR for "this is a prediction of DCCREG"]. Still **not** an SI value — a dimensionless prediction.

### B-REDUCED — inputs reduce but no pure ratio
**Trigger:** the free-input set shrinks (e.g. first-principles $J$ succeeds, or several quantities collapse to one combination) but no fully input-independent cross-gate ratio emerges.
**Meaning:** honest progress — fewer free parameters, sharper structure — without a parameter-free prediction. The expected, respectable outcome.
**Graduation:** update II-§8 / IV / V residuals with the reduced input count and the computed dependences.

### B-IRREDUCIBLE — the inputs are genuinely independent
**Trigger:** the free inputs do not cancel in any physically meaningful ratio; the framework's predictions all scale with unfixed inputs.
**Meaning:** also a valid, important result — it says DCCREG, as it stands, is a *structural* theory with no parameter-free numerical predictions until the inputs are fixed externally. Records the honest ceiling of the current construction.
**Graduation:** state plainly in the README frontier and the block residuals that absolute/relative numerical predictions require external input — no overclaim.

---

## 4. Validation ladder (gates everything, per INTERPRETATION §0)

Re-run the rungs on the branch (1–5). Plus two new self-tests specific to this run:
- **Dimensional closure:** every computed quantity's units reconstruct correctly from the free-input set (a quantity whose units don't close signals a missing hidden input — a bug).
- **Known-limit recovery:** the run002 $K_A$ and run004 $m_D(J{=}1)$ values are reproduced exactly by the reduction layer before any ratio is trusted.

A ratio arriving while these fail is a bug, not a result.

---

## 5. Honesty constraints (carry into the run)

- **No SI numbers.** Absolute values require inventing inputs — forbidden. Dimensionless ratios and free-input dependences only.
- **B-IRREDUCIBLE is a fully acceptable result** — possibly the most honest one. Do not manufacture a pinned ratio by burying an input.
- The dimensional analysis is [OC]; the *identification* of any ratio as "a physical prediction" is [IR]; the map to a *measured* SM ratio stays [RH], fenced (V-§8).
- If a "prediction" depends on $\ln(d/a)$, it is only as pinned as that ratio (Block III left it ≈4, not exact) — state the residual dependence.

---

## 6. Outputs

Write to `../../results/run005_physical_scales/`: `params.json` (+ git + seed),
`data.{json,csv}` (the free-input table, the ratio list split into
input-independent vs input-dependent), `figures/` (ratio-vs-$J$, ratio-vs-$\ln(d/a)$),
and `NOTES.md` tagging every claim and **stating the branch (B-PINNED / B-REDUCED /
B-IRREDUCIBLE) and why**. Then a consolidation report for graduation.

---

## 7. Why this is the right next run

Every "computed" result in the programme (run002–004) is currently in relative units.
This run draws the exact line between what the framework *predicts regardless of inputs*
(the real content) and what *needs a scale choice* (the free parameters). Whichever
branch it lands in, it tells us the honest ceiling of the current construction — which
is more valuable than any single new mechanism, because it bounds what all the mechanisms
together can actually claim.
