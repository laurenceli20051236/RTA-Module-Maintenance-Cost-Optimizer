# Chapter 2: FEOL — Gate Stack Reliability, Channel/Extension Doping, Active Area Formation

*Sources: Tabata et al. 2022 §2; Huet et al. 2016 §3.1*

## Core Idea
In FEOL, UV-LA replaces long, high-T steps (800–1000 °C reliability anneals, spike anneals) with ns-scale heat that limits dopant diffusion and allows non-equilibrium bond rearrangement and local strain engineering.

## Frameworks Introduced
- **BTI source split in HfO2/SiO2/Si stacks** (Tabata):
  - Source 1: HfO2 bulk traps → mitigated by an HfO2/SiO2 dipole.
  - Source 2: traps in the ~1 nm chemical SiO2 and the SiO2/Si interface → need annealing within budget.
  - Alternatives: low-T (100–450 °C) H-based anneal, plasma treatment, or ns UV-LA.
- **Accumulated-shot SiO2/Si engineering**: ns UV-LA at ~900 °C effective T, ~10⁻⁷ s dwell, repeated up to 1000×.
  - Evidence chain: ATR-FTIR (LO phonon shift of the Si–O–Si AS mode) + XPS Si 2p → network rearrangement; DLTS → Pb-center-type traps annihilated **but** competing "tail states / U-shaped continuum" (Si–O weak bonds) form.
- **Melt-confined diffusion** (Tabata §2.2): below Si melt, ns UV-LA gives negligible B/P/As diffusion; in melt, diffusivity jumps to ~10⁻⁴ cm²/s but is bounded by melt depth → **box-like profile**.
- **Active area formation by melt LA** (Huet §3.1): implant Ge into Si (or Sn into Ge), then melt only the implanted region → local SiGe (GeSn) with strain, without selective epitaxy.
  - Why selective: implanted / amorphized material has a **lower melting point and lower reflectivity** → melts at much lower ED (Ge-implanted Si < 0.25 J/cm² vs bulk Si 1.7 J/cm²).

## Key Concepts
- **EOT**: equivalent oxide thickness; subnanometer target in the 7 nm planar gate stack.
- **BTI**: bias temperature instability, driven by gate stack traps.
- **DLTS**: deep-level transient spectroscopy for trap signatures.
- **DIBL**: drain-induced barrier lowering — the SCE metric used to compare LA vs spike.
- **Box-like profile**: abrupt profile bounded by maximum melt depth.
- **Melting threshold**: ED at which the surface first melts; strongly material/implant dependent.
- **Explosive crystallization**: melt-front propagation through amorphous layers (also seen in Ge, Huet §3.3).

## Mental Models
- Use **number of shots** as a cumulative "dose" knob for non-equilibrium structural relaxation (1 vs 1000 shots act differently).
- Think of **implant-amorphized regions as "pre-sensitized" targets**: they melt first, giving self-aligned selectivity.
- Use melt depth = junction depth design: the melt front is the diffusion wall.

## Anti-patterns
- **Expecting UV-LA alone to perfect the SiO2/Si interface**: it trades Pb centers for tail states; combine with other passivation.
- **Using spike annealing for thin-body extensions**: B and P diffuse more than As; spike degrades DIBL.
- **Partial melt of an amorphized channel**: leaves defects; target full melt of the amorphous layer down to the crystalline seed.

## Reference Tables
| Case (Tabata/Huet) | Condition | Outcome |
|---|---|---|
| Chemical SiO2/Si, ns UV-LA | ~900 °C, ~10⁻⁷ s, ×1–1000 | Si–O–Si rearrangement; Pb traps ↓, tail states ↑ |
| FDSOI 11 nm Si channel, extension | full melt of 5–7 nm amorphized Si | monocrystalline regrowth, raised S/D epi OK, DIBL better than spike |
| Si + GeH4 PLAD (3 kV, 1e17) + B2H6 | melt LA | crystalline SiGe, slight strain, mobility ↑ |
| Ge epi + Sn (10 keV 5e15) + Sb (11 keV 5e15) | non-melt / shallow / deep melt | no diffusion sub-melt; Sn surface segregation above solubility in melt |

## Worked Example
**FDSOI extension flow (Tabata Fig. 4)**: (1) form gate; (2) extension implant amorphizes 5–7 nm of an 11 nm Si channel; (3) ns UV-LA fully melts only the amorphous layer — simulated T(t) confirms melt depth; (4) liquid regrows epitaxially from the underlying crystal seed (TEM confirms single crystal); (5) raised S/D epi grows normally on the regrown surface (no morphology penalty); (6) DIBL vs Lg is better than with spike anneal, most clearly for B and P.

## Key Takeaways
1. ns UV-LA below melt ≈ zero diffusion; in melt, diffusion is bounded by melt depth.
2. Implanted/amorphous regions melt at far lower ED → built-in selectivity.
3. Repeated shots allow non-equilibrium bond engineering, but with competing defect formation.
4. Validate with a structural + electrical chain (FTIR/XPS + DLTS; TEM + DIBL).

## Connects To
- **Ch 3**: LPER/SPER activation physics in contacts.
- **Ch 5**: the same melt-window logic in 3D SOI.
