# Patterns & Techniques — UV Laser Annealing

## Melt-Window Bracketing
**When to use**: any melt-LA on an implanted film over a seed or BOX.
**How**: sweep ED → map Rs plus TEM → lower bound = ED fully melting the a/c interface and EOR; upper bound = ED melting to the BOX / losing the seed (or ablation F2). Run mid-window with ≥10 % margin. Confirm melt with in-situ TRR.
**Trade-offs**: caps, stack and pattern density shift the window; requalify per stack (Ch 5).

## Implant-Sensitized Selective Melt
**When to use**: local SiGe/GeSn/strained layers without selective epitaxy.
**How**: high-dose Ge (Sn) implant amorphizes and lowers melt T and reflectivity → ED between the implanted and bulk thresholds melts only the implant (Ge:Si <0.25 vs Si 1.7 J/cm²).
**Trade-offs**: implant optimization required; strain physics is complex (Ch 2).

## LPER Surface-Segregation Contact
**When to use**: n/p contacts needing >solubility activation at the interface.
**How**: choose a k<1 dopant (Sb in Si; Ga, In in SiGe), melt beyond the implant tail, tune V (~m/s) via ED and geometry.
**Trade-offs**: higher V raises incorporation but reduces segregation; morphology and stacking-fault risk; Al self-compensates (Ch 3).

## Multi-Shot ns SPER / µs SPER
**When to use**: flat, metastable activation without melting.
**How**: repeat sub-melt shots (ns: >20 shots at ~0.8–1.8 nm/shot) or move to µs dwell to cut shot count.
**Trade-offs**: throughput (ns); possible surface segregation (µs) (Ch 3).

## Accumulated-Shot Structural Relaxation
**When to use**: interface/network engineering (SiO2/Si, HfO2 nucleation).
**How**: identical ns shots repeated 10–1000×; track with FTIR/XPS/DLTS or XRD/TEM.
**Trade-offs**: competing defect creation (tail states) (Ch 2, 4).

## Dwell-Time Phase Selection (HfO2)
**When to use**: ferroelectric/high-k phase targeting in BEOL.
**How**: µs dwell sweep for transformation control; ns multi-shot for nucleation; absorber metal or Si plus SiO2 heat-confinement stack.
**Trade-offs**: stack- and dopant-dependent (Ch 4).

## Anneal-Before-Pattern
**When to use**: metals where patterns cause optical interference (subtractive Ru).
**How**: UV-LA the blanket film, then etch.
**Trade-offs**: needs a subtractive-compatible metal (Ch 4).

## Assisted-Heat Deep Activation
**When to use**: µm-deep backside buffers (IGBT) with front side <400 °C.
**How**: high-energy implant + single high-ED shot + chuck 300–350 °C.
**Trade-offs**: more total heat; verify the front side and diffusion (Ch 6).

## Short-Loop Buried-Layer Qualification
**When to use**: proving 3D compatibility.
**How**: emulate the stack (Cu BEOL + oxide + top a-Si), anneal across ED, SEM inspection, then measure line R, C and bottom ION/IOFF; simulate T(t) of buried layers.
**Trade-offs**: low-metal-density regions are worst case (Ch 1, 5).

## Raman/XRD Crystallization Readout
**When to use**: a-Si / a-SiC crystallization.
**How**: Raman position, FWHM and fc; SiC 790 cm⁻¹ vs graphite 1350/1600 cm⁻¹; XRD 3C (111) 35.6° plus Scherrer grain size; TEM for interlayers.
**Trade-offs**: Raman shifts also reflect stress and confinement (Ch 7, 8).
