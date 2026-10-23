# Chapter 3: MOL / S-D Contacts — LPER vs SPER, Segregation, Si:P, Strained Si:B, Ge Doping

*Sources: Tabata et al. 2022 §3; Huet et al. 2016 §3.2–3.3*

## Core Idea
Contact resistivity targets (ρc < 1–2 × 10⁻⁹ Ω·cm²) require active carriers near ~1 × 10²¹ cm⁻³ at the metal/semiconductor interface; UV-LA reaches this beyond solid solubility through metastable activation, via either melt regrowth (LPER) or solid-phase regrowth (SPER).

## Frameworks Introduced
- **Two UV-LA activation routes** (Tabata):

| | LPER (liquid phase epitaxial regrowth) | SPER (solid phase epitaxial regrowth) |
|---|---|---|
| Mechanism | melt doped layer, epitaxial regrowth from seed | amorphized layer recrystallizes without melting |
| Typical tool | single ns pulse | ns: >20 shots; µs pulses reduce shot count |
| Morphology | risk of roughening | flat (RMS ~0.10 nm) |
| Activation | metastable; surface segregation if k < 1 | metastable; possibly higher than LPER |
| Productivity | high | low with ns, better with µs |

- **Melting regimes**: *Secondary Melting (SM)* — liquid forms at the surface and extends downward (the regime wanted for LPER). *Explosive Melting (EM)* — a thin (few–10 nm) liquid layer travels into amorphous material and leaves polycrystal.
- **Segregation coefficient k = CS/CL** at the moving l/s interface:
  - k < 1 → dopant piles up at the surface on solidification → more active carriers at the contact interface.
  - k = f(V): higher solidification velocity V pushes k → 1 (less segregation).
  - Active concentration vs V is **downward-convex**: higher V raises substitutional incorporation, **trade-off** with surface segregation.
  - Not every small-k dopant works: Al in SiGe stays near solubility (self-compensation).
- **Full-melt rule**: melt must reach beyond the implant tail and the a/c interface / EOR defects; otherwise residual point defects precipitate as extended defects at the top of the non-melted region. Stacking faults can still nucleate from a non-uniform a/c or l/s interface.

## Key Concepts
- **ρc (specific contact resistivity)**: target < 1e-9 (Tabata) / < 2e-9 Ω·cm² (Huet).
- **Field-emission transport**: tunnelling-dominated regime enabled by very high surface doping.
- **Solidification (melt-front) velocity V**: m/s scale; ~4 m/s simulated for a 14 nm FinFET S/D fin (small volume → fast heat sinking → higher V).
- **Degree of surpassing solid solubility**: active/solubility ratio; >10× at 4 m/s for Sb in Si.
- **Sb solubility in Si**: ~6.8 × 10¹⁹ cm⁻³.
- **DHEM**: differential Hall effect metrology for active carrier depth profiles.
- **Deactivation anneal**: subsequent thermal steps that de-activate metastable dopants.

## Mental Models
- Think of **V as the master variable** in LPER: it sets both incorporation (good when high) and segregation (good when low).
- Treat **metastable activation as perishable**: every later thermal step must be checked for deactivation (ms anneal + spike already de-activates Si:P).
- In SPER, **rate per shot** is a throughput metric: ~0.8–1.8 nm/shot in ~10 nm a-Si (ns); use µs to cut shots.

## Anti-patterns
- **Partial melt of the implanted layer** → extended defects at the melt bottom.
- **Assuming any k < 1 dopant activates** → self-compensation (Al).
- **Ignoring native oxide before melt anneal of Ge:B** → O contamination; P and As are less sensitive.
- **Adding spike anneal after ms/laser activation** → deactivation and extra diffusion.

## Reference Tables
**Si:P epi activation comparison (Huet §3.2, imec work)**

| Anneal | Result |
|---|---|
| As-epi (4.6 % P) | most P inactive; ρc ~1e-8 Ω·cm² |
| ms laser 1200 °C, 2×0.5 ms | ~1e21 cm⁻³ active, ~5 nm diffusion; ρc ~6e-9; ~2× nMOS ION |
| ms + spike 950/1000 °C 1.5 s | deactivation + extra diffusion |
| UV melt 1.8 J/cm², 160 ns (full melt 40 nm) | ~all P active, ~3 nm diffusion, P segregates to surface |

**Other data points**
| Case | Condition | Result |
|---|---|---|
| Si:B strained layer | B 1 keV 1e16, melt 2 J/cm², 1–5 shots | 4 % strain (vs ~2 % conventional limit), ~40 nm junction, defect-free; <3 nm extra diffusion after 5 shots |
| µs UV-LA SPER As:Si | — | active >1e21 near surface, surface segregation; ≤5 % Rs degradation after BEOL-like ns deactivation anneals up to sub-ms |
| Ge: P 15 keV / As 28 keV 1e15 | 0.55–1.05 J/cm², 160 ns | defect-free only when a/c + EOR fully molten (1.05 J/cm²); diode leakage from trap-assisted tunnelling |
| 14 nm FinFET Sb contact | ns UV-LA, 3D TCAD | Sb segregation at fin top, V ≈ 4 m/s |

## Worked Example
**Choosing V for an Sb n-contact (Tabata Figs 7, 9)**: (1) start from the Sb solubility in Si (~6.8e19); (2) from the "degree of surpassing solubility vs V" curve, ~4 m/s gives >10× gain; (3) 3D TCAD of the real fin shows V ≈ 4 m/s because the small S/D volume sinks heat into the substrate quickly; (4) confirm segregation with TEM/EDX at the epi top surface; (5) still pending: electrical ρc on CTLM structures and a check for stacking faults from the a/c interface.

## Key Takeaways
1. ρc < ~1e-9 Ω·cm² needs ~1e21 cm⁻³ active at the interface.
2. LPER: k < 1 dopants segregate to the surface; V trades incorporation against segregation.
3. Always melt past the implant tail and EOR defects.
4. SPER gives flatter surfaces and possibly higher activation, but needs many ns shots or µs pulses.
5. Check every downstream thermal step for deactivation.

## Connects To
- **Ch 2**: melt-confined diffusion.
- **Ch 4**: BEOL anneals used as deactivation tests.
- **Ch 6**: deep melt activation in power devices.
