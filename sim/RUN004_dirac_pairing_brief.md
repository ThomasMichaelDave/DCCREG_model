# DCCREG Simulator — Run Brief: Inter-Sublattice Dirac-Pairing Test

**Target run:** `run004_dirac_pairing`
**Reads first:** `../CLAUDE.md`, `README.md` (targets), `INTERPRETATION.md` (how to read), and the two prior reports in `../results/run002_*/` and `../results/run003_*/`.
**Branch from:** the run003 closure/energy machinery (`check_04_excited_spectrum.py`) — this run extends it to two sublattices.

---

## 0. Why this run exists (the tension it resolves)

run003 found the $L=8$ spin-½ ground state is an **isolated singlet** — **no doublet** — because the *fixed global screw sense* (locked assumption, CLAUDE.md §2 / I-§4) means only the screw-aligned handedness is realised, so the L/R partner is non-degenerate and absent.

This puts a **locked axiom on the table**, because it cuts against physics: real fermions are handed *and* come in partners (a Dirac electron has both chiralities; weak isospin pairs them). So either (a) DCCREG predicts no fundamental doublets [a falsifiable stance], (b) **the second handedness already exists on the *other* sublattice** and the "missing partner" is an inter-sublattice object — the Dirac-mass channel Block V §8 flagged [RH], or (c) the fixed-*global*-chirality axiom is genuinely too strong and needs relaxing to *local* handedness.

run003 almost certainly modelled **one sublattice**. The framework's own structure (I-§13: **dual counter-rotating sublattices of opposite handedness**; I-README §2.3: global screw fixes *global* helicity while local helicity density *varies pointwise*) already contains both handednesses. **This run tests possibility (b) before anyone touches the axiom (c).**

> **Discipline note.** We are NOT relaxing the locked axiom in this run. We are testing whether the second handedness is already present in the dual structure. Only if this run forbids the partner *even with both sublattices* does the axiom itself come into question — and then as an open Block I revision with its upstream cost made explicit, not a quiet patch.

---

## 1. The question (one sentence)

**Does the inter-sublattice (L↔R) coupling bind the $L=8$ screw-aligned spin-½ ribbon on sublattice A to its opposite-handed partner on sublattice B into a near-degenerate Dirac pair — or does the coupling leave them split/unbound?**

---

## 2. What to build (extending run003)

1. **Two sublattices, opposite handedness.** Instantiate the dual structure of I-§13: sublattice A with screw rate $s_+ = +1/(3\varphi^2)$, sublattice B with $s_- = -1/(3\varphi^2)$ (mirror screw). Each independently supports the run003 closure ladder; the $L=8$ ground ribbon exists on **both**, with opposite handedness ($\mathrm{Lk}=+1$ on A, $\mathrm{Lk}=-1$ on B).
2. **The shared-node coupling.** Couple A and B through the shared-node / mutual-helicity channel already in the framework: I-§13 (co-rotating neighbours cancel, counter-rotating reinforce) and V-§6 (mutual helicity $\Gamma_i\Gamma_j\mathrm{Lk}_{ij}$ = the statistics/exchange channel). The A-ribbon and B-ribbon are **counter-rotating** (opposite handedness), so by I-§13 they **reinforce** at a shared node — this is the physical coupling to model. Parameterise its strength as $J$ (the inter-sublattice coupling), and **scan $J$** the way run002/3 scanned weights.
3. **The energy model (extend run003's [IR] functional).** Two-ribbon energy:
   $$E_{AB} = E_A + E_B + J\cdot(\text{coupling term in }\mathrm{Lk}_{AB},\ \text{the mutual linking of A and B}).$$
   Keep run003's single-ribbon $E = w_{\rm len}L + w_F(\Omega/120)^2 + w_W(\mathrm{Lk}-sL)^2$ for $E_A,E_B$. The new term is the **mutual-helicity coupling** between the two sublattice ribbons (Moffatt off-diagonal, V-§6). State the functional explicitly in `NOTES.md`; it is **[IR]**.

---

## 3. What to measure (the outputs)

- **The pair gap $\Delta(J)$**: energy splitting between the symmetric (A+B) and antisymmetric (A−B) combinations of the two opposite-handed $L=8$ ribbons, as a function of coupling $J$.
- **Bound vs split**: does the coupled (A,B) system have a near-degenerate low-lying pair (a Dirac doublet) for natural $J$, or does it stay split by $\gg$ the ground-state scale?
- **The combined object's quantum numbers**: net $\mathrm{Lk}$, net handedness, and whether the bound state is **massive** (the A↔B coupling = a mass term mixing the two chiralities — the Dirac-mass signature).
- **Robustness scan** over $J$ (e.g. $0.1\times$–$10\times$ a natural scale set by the mutual-helicity term), exactly as run003 scanned its weights. Report what survives the scan and what does not.

---

## 4. THE BRANCHES — pre-committed, so the result cannot be wished into being

This is the heart of the brief. **Both outcomes are written down before the run, with their consequences, so a "doublet" cannot be manufactured by tuning.**

### Branch B-YES — partner found (axiom holds, doublet is the mass mechanism)
**Trigger:** for natural $J$ (within the scan, not at an extreme edge), the opposite-handed A and B $L=8$ ribbons bind into a near-degenerate low-lying pair whose A↔B mixing is a **mass term**.
**Meaning:** the "missing partner" was on the other sublattice all along. The fixed-global-chirality axiom **survives intact** — global handedness is still fixed (DC), but the *local* dual structure supplies both chiralities, and their coupling **is** the Dirac mass (Block V §8's flagged [RH] mechanism becomes [IR], computed).
**Graduation:** Block V → v0.5 "Dirac pairing": the doublet/mass mechanism is the inter-sublattice coupling; the axiom is confirmed, not questioned. Possibly closes part of the §8 mass [RH].
**Tier:** [OC] for the binding arithmetic; [IR] for "this is the Dirac mass."

### Branch B-NO — partner forbidden even with both sublattices (axiom genuinely on the table)
**Trigger:** across the whole natural $J$ scan, the pair stays split by $\gg$ ground-state scale, OR the coupling fails to produce any near-degenerate combination — i.e. even *with* both sublattices present, no doublet forms.
**Meaning:** the absence of a partner is **not** an artifact of modelling one sublattice; it is structural. This is the genuine, located reason to **question the fixed-chirality axiom** (CLAUDE.md §2 / I-§4) — the first time the programme has earned that.
**Graduation:** open a **Block I chirality revision** as an explicit fork, NOT a quiet patch:
- state that fixed *global* chirality, as locked, forbids fundamental doublets;
- spell out the **upstream cost** — chirality is primordial (I-§3) and load-bearing for helicity conservation (I-§1), the Weyl handedness (V-§7), the no-monopole/induction structure (II), and the $\alpha_1=0$ result (IV-§6.7); relaxing global→local handedness touches all of these;
- frame candidate relaxations (e.g. global helicity conserved but handedness *locally* unpinned) as [RH] hypotheses to be tested, each with its cost.
**Tier:** [OC] for the negative result; the axiom revision is an open [IR]/[RH] fork, handled openly per CLAUDE.md §1 rule 3.

### Branch B-AMBIGUOUS — weight/coupling-dependent
**Trigger:** binding occurs only at extreme $J$, or the result flips across the scan.
**Meaning:** inconclusive — like run003's weight-dependent first-excited state. Report as inconclusive; do **not** force it into B-YES or B-NO. Note which way it leans and what would disambiguate (e.g. pinning $J$ from the mutual-helicity term in physical units, which needs the run002 $K_A$ machinery).

---

## 5. Validation ladder (per INTERPRETATION §0 — gates everything)

Re-run the rungs whose code is on the branch (2,3,4,5 as in run003) **in this session**. The new two-sublattice machinery must also pass two new self-tests before any $\Delta(J)$ is trusted:
- **Decoupling limit $J\to0$:** the two sublattices reproduce two independent copies of the run003 singlet (no spurious binding at zero coupling).
- **Mirror symmetry:** swapping A↔B (and screw sense) leaves $\Delta(J)$ invariant — the coupling must respect the substrate's mirror-pseudoscalar structure (I-§1).

A $\Delta(J)$ arriving while these fail is a bug, not a result.

---

## 6. Honesty constraints (carry into the run)

- **Do not declare B-YES from an edge-of-scan $J$.** A doublet that exists only at unnatural coupling is B-AMBIGUOUS at best.
- **B-NO is a fully acceptable, valuable result** — it is the one that legitimately reopens a locked axiom, which is a bigger deal than finding a doublet. Do not avoid it.
- The energy functional and the coupling term are **[IR]**; flag them. The closure/Lk/mirror arithmetic is [OC].
- No physical masses yet (relative units) unless coupled to run002's $K_A$ — state this.
- Map to real SM doublets (electroweak isospin) stays **[RH], fenced** (V-§8) regardless of branch.

---

## 7. Reproduce / outputs

```bash
pip install -r ../requirements.txt
python3 check_05_dirac_pairing.py ../../results/run004_dirac_pairing
# re-run validation rungs on this branch:
python3 check_01_calugareanu_framing.py
python3 check_02_hexatic_greens_function.py
python3 check_03_joining_spectrum.py
```

Write to `../../results/run004_dirac_pairing/`: `params.json` (params + git + seed), `data.{json,csv}` (the $\Delta(J)$ scan, pair quantum numbers), `figures/` (gap-vs-$J$, level diagram), and `NOTES.md` tagging every claim [OC]/[IR]/[RH] and **stating which branch (B-YES / B-NO / B-AMBIGUOUS) the run lands in and why**.

Then hand the consolidation report back for graduation (Block V v0.5, or a Block I chirality-revision fork — per the branch).
