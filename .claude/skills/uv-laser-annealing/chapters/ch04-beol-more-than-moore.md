# Chapter 4: BEOL & "More Than Moore" — Cu/Ru Grain Growth, Poly-Si LPC, Hf-Based Ferroelectrics

*Source: Tabata et al. 2022 §4–5*

## Core Idea
BEOL is limited to ~400 °C-class furnace anneals; UV-LA lets the top metal or film briefly reach far higher temperatures (even Cu melt), enabling grain growth, crystallization of a-Si, and HfO2 phase control inside the interconnect stack.

## Frameworks Introduced
- **Line resistivity scaling problem**: as trench CD shrinks, grain boundaries and surface scattering grow and line resistance rises steeply. Remedy: larger grains / bamboo structure.
- **Metal figure of merit**: λ (electron mean free path) × ρ0 (bulk resistivity) vs melting point (EM reliability). Ru: higher ρ0 but smaller λ and >2× Cu melting point.
- **Cu submelt vs melt UV-LA** (50 nm blanket Cu): mean grain ~100 nm after 600 °C furnace; ~4× with µs submelt UV-LA; ~10× with melt UV-LA. Limit: interlayer diffusion in dielectric/Cu/Ta/SiO2 stacks → need better barriers/liners (TaN/Co, TaN/Ru, TaMnxOy).
- **Ru lines**: 21 nm half-pitch dual damascene, no melt, multiple ns UV-LA → up to 25 % lower line R. **Semi-damascene (subtractive) Ru** fits UV-LA better: anneal blanket metal *before* patterning → avoids optical interference effects from patterns.
- **LPC vs SPC for a-Si in BEOL**: SPC on SiO2 needs ~600 °C for hours (out of budget); UV-LA enables LPC (and SPC).
  - LPC side effects: **hillocks** at final grain boundaries (solidification fronts collide) → CMP needed. Dielectric caps help LPER flatness but can trigger **wrinkles** (elastic layer on liquid); wavelength/height grow with melt depth → co-design the stack.
- **HfO2 phase control by dwell time**: ferroelectric o-phase (Pca21) appears in the t→m transition.
  - µs dwell → phase *transformation* control (permittivity evolves with dwell; ferroelectricity shown by PUND P-V).
  - ns dwell → *nucleation*-controlled; repeated ns shots accumulate the same phase; selectivity depends on peak T, doping, stack.
  - Need absorber + heat-confinement layers, e.g. metal/HfO2/metal/SiO2/Si (metal absorbs UV, SiO2 confines heat).

## Key Concepts
- **Bamboo structure**: grains span the whole line width → few scattering boundaries.
- **Sheet resistance drop**: proxy for grain growth in blanket films (Cu process A submelt: −15 %).
- **Hillocks**: surface bumps at LPC grain boundaries.
- **Wrinkles**: periodic surface undulation of a capped liquid layer.
- **PUND**: Positive-Up-Negative-Down correction for ferroelectric P-V.
- **Phases of HfO2**: c, t, o (ferroelectric), m (stable).

## Mental Models
- **Dwell time is a phase selector**: µs = transformation kinetics, ns = nucleation statistics.
- **Anneal before patterning** whenever optical interference from patterned features would make heating non-uniform.
- **Melt buys grain size but costs morphology**: plan CMP or capping and check wrinkles.

## Anti-patterns
- **Melting Cu on a standard Ta barrier stack without checking diffusion** → Rs degrades (processes B/C).
- **Capping a melted layer without mechanical design** → wrinkles.
- **Expecting grain growth from a single ns shot in HfO2** → negligible growth; ns acts on nucleation.

## Reference Tables
| Application | UV-LA mode | Key result |
|---|---|---|
| Cu blanket 50 nm | µs submelt / melt | grain ~4× / ~10× vs 600 °C furnace; diffusion limits window |
| Ru dual damascene 21 nm HP | ns multi-shot, no melt | line R −25 % |
| Ru blanket | ns multi-shot | grain growth, Rs drop |
| a-Si in BEOL | ns melt (LPC) | poly-Si; hillocks need CMP |
| HfO2 10 nm | µs dwell sweep | k evolves; ferroelectricity |
| HfO2 50 nm / TiN / Si | ns single vs multi | cumulative crystallization of same phase |

## Worked Example
**HfO2 ferroelectric in BEOL (Tabata Figs 19–20)**: (1) build an absorber/confinement stack (metal or Si / HfO2 / metal / SiO2 / Si); (2) for transformation control, sweep µs dwell and track relative permittivity against the predicted k for each phase; (3) confirm ferroelectricity with PUND-corrected P-V; (4) for nucleation control, use ns shots near/above Si melt and add shots to accumulate the phase (verify with XRD and dark-field TEM); (5) tune dopant (stabilizer) and stack to bias phase selection.

## Key Takeaways
1. UV-LA brings above-furnace temperatures into BEOL without breaking the budget.
2. Cu benefits are real, but barrier/liner thermal stability sets the window.
3. Subtractive Ru suits UV-LA (anneal before patterning).
4. LPC poly-Si needs a morphology plan (CMP, caps, wrinkle check).
5. Dwell time selects the HfO2 phase-control mechanism.

## Connects To
- **Ch 3**: BEOL anneal conditions reused as dopant deactivation tests.
- **Ch 5**: NEMS and poly-Si above IC.
- **Ch 7**: a-Si crystallization physics vs wavelength.
