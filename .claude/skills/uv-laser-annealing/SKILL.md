---
name: uv-laser-annealing
description: "Knowledge base from three laser-annealing reviews: Tabata et al. 2022 (UV-LA for advanced CMOS, Electronics), Huet et al. 2016 (Doping by Laser Thermal Annealing, MSSP), Arduino et al. 2023 (Si and SiC recrystallization by laser annealing, Materials). Use when reasoning about UV/excimer laser anneal process windows, melt vs sub-melt regimes, LPER/SPER dopant activation, contact resistivity, 3D sequential thermal budget, BEOL Cu/Ru grain growth, HfO2 ferroelectric phase control, IGBT backside activation, SiC/GaN annealing, or a-Si/a-SiC crystallization."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# UV Laser Annealing — Process Knowledge Base
**Sources**: Tabata, Rozé, Thuries, Halty, Raynal, Karmous, Huet — *Electronics* 2022, 11, 2636 (CC BY) · Huet, Mazzamuto, Tabata, Toqué-Tresonne, Mori — *Mater. Sci. Semicond. Process.* 2016 · Arduino, Stassi, Spano, Scaltrito, Ferrero, Bertana — *Materials* 2023, 16, 7674 (CC BY)
**Pages**: ~58 | **Chapters**: 8 | **Generated**: 2026-10-23

## How to Use This Skill
- **Without arguments**: load the core frameworks below.
- **With a topic** (e.g. `segregation coefficient`, `SOI window`, `SiC graphite`): find the chapter in the Topic Index and read it before answering.
- **With a chapter** (`ch03`): load that file.
- For decisions and numbers, open [cheatsheet.md](cheatsheet.md) first.

When a question goes beyond the Core Frameworks, read the relevant chapter file before answering. All numbers are literature values for the specific stacks cited; treat them as starting points, not recipes.

---

## Core Frameworks & Mental Models

**1. Vertical selectivity, not "cold" processing.** UV absorption depth (δ = 1/α) sets *where* heat is generated; ns–µs pulse length sets *how far* it diffuses. Together they let the surface reach melt while buried layers stay within ~500 °C for a few hours (3D sequential budget). Judge compatibility from the **buried layer's simulated T(t)**, then confirm with short-loop electrical tests (Cu line R/C, bottom-device ION/IOFF). Thicker buried oxide gives better isolation. (Ch 1, 5)

**2. Fluence selects the regime.** Below melt: no measurable diffusion; useful for multi-shot SPER and structural relaxation. Partial melt of an implanted layer: defects. Full melt through the a/c interface + EOR damage: defect-free epitaxial regrowth with a **box-like profile** (melt diffusivity ~1e-4 cm²/s, bounded by melt depth). Melt reaching the BOX/seed: poly. Above ablation: damage. Always define a window **[full damage-melt ED, seed-loss ED]** with ~10 % margin (23 nm SOI with cap: ~0.8–0.85 J/cm²; uncapped ~1.25 J/cm²). (Ch 2, 3, 5, 7)

**3. Implant-sensitized selectivity.** Amorphized/implanted regions have lower melt temperature and lower reflectivity, so they melt at much lower ED (Ge-implanted Si <0.25 vs bulk Si 1.7 J/cm²). Use this for self-aligned local SiGe/GeSn/strained layers. (Ch 2)

**4. LPER vs SPER for metastable activation.** Contacts need ρc < 1–2e-9 Ω·cm² → ~1e21 cm⁻³ active at the interface. *LPER*: high throughput; surface segregation when **k = CS/CL < 1**; the solidification velocity V is the master variable (higher V → more incorporation but k → 1, less segregation); Sb in Si at ~4 m/s gives >10× solubility. *SPER*: flat (RMS ~0.1 nm), possibly higher activation, but ns needs >20 shots (0.8–1.8 nm/shot); µs pulses cut the shot count. Not every k<1 dopant works (Al self-compensates). Metastable activation is perishable: audit later thermal steps for deactivation. (Ch 3)

**5. Shot count and dwell time are mechanism knobs.** Repeated ns shots (up to 1000×) rearrange the SiO2/Si network (Pb traps ↓ but tail states ↑) and accumulate HfO2 nucleation. µs dwell controls phase *transformation* (HfO2 permittivity and ferroelectric o-phase); ns controls *nucleation*. Use absorber + SiO2 confinement stacks. (Ch 2, 4)

**6. BEOL opens up.** UV-LA can briefly exceed furnace limits (<420 °C): Cu grains grow ~4× (submelt) / ~10× (melt) vs 600 °C furnace, limited by barrier interdiffusion; Ru line R −25 % with multi-shot ns; prefer **anneal-before-pattern** (subtractive Ru) to avoid optical interference. a-Si LPC gives poly-Si but hillocks need CMP; capped melts can wrinkle. (Ch 4)

**7. Power & wide bandgap.** Melt LA was the first HVM use (IGBT/diode backside). **Assisted heating** (≤350 °C used; tool ≤450 °C) extends activation to ~4 µm at ~100 % while the front side stays <400 °C. SiC/GaN need UV photons; out-of-equilibrium melt regrowth repairs SiC but segregates Si/C at the surface (graphite/poly-Si/4H); GaN loses N at the surface. LA gives uniform backside Ni-silicide ohmic contacts on SiC. (Ch 6)

**8. Wavelength vs bandgap for crystallization.** a-Si: UV/visible efficient for thin films; IR penetrates thick films but needs more power and risks ejection. Keep within **F1 (melt) – F2 (ablation)** (355 nm: 70–374 mJ/cm²). Quantify with Raman position, FWHM, and **fc = Ic/(Ic+Ia)**. a-SiC: UV (4.9 eV ≫ 2–2.5 eV gap) works; green is marginal; IR is indirect. Threshold ~250 mJ/cm² (KrF); overshoot → Si + graphite. Need x ≈ 0.4–0.5 stoichiometry. (Ch 7, 8)

**9. Tool facts (SCREEN LT-3100)**: 160 ns UV pulse, step-and-repeat full field up to 26×33 mm, <±4 % non-uniformity, assist heating ≤450 °C, <10 ppm O2. (Ch 1)

---

## Chapter Index

| # | Title | Key Frameworks |
|---|---|---|
| [ch01](chapters/ch01-fundamentals-thermal-budget.md) | Fundamentals, thermal budget, LT tool | vertical selectivity, Beer–Lambert, photothermal vs photochemical |
| [ch02](chapters/ch02-feol-gate-channel-active-area.md) | FEOL: gate stack, extensions, active area | BTI sources, melt-confined diffusion, implant-sensitized melt |
| [ch03](chapters/ch03-mol-contacts-lper-sper.md) | MOL contacts: LPER/SPER, Si:P, Si:B, Ge | k = f(V), full-melt rule, deactivation |
| [ch04](chapters/ch04-beol-more-than-moore.md) | BEOL & More-than-Moore | Cu/Ru grain growth, LPC hillocks/wrinkles, HfO2 dwell-time phase control |
| [ch05](chapters/ch05-3d-sequential-nems.md) | 3D sequential & NEMS | SOI melt window, buried Cu qualification, SLG |
| [ch06](chapters/ch06-power-wide-bandgap.md) | Power: IGBT, SiC, GaN, ohmic | assisted heating depth, WBG UV rule, Ni silicide |
| [ch07](chapters/ch07-si-crystallization-by-wavelength.md) | a-Si crystallization vs wavelength | F1–F2 window, Raman fc |
| [ch08](chapters/ch08-sic-crystallization.md) | a-SiC crystallization | photon energy vs gap, fluence threshold, phase segregation |

## Topic Index
- **Ablation / F2** → ch07
- **Assisted heating** → ch01, ch06
- **BOX melt / SOI window** → ch05
- **BTI / SiO2-Si interface** → ch02
- **Contact resistivity ρc** → ch03, ch06
- **Cu / Ru interconnect** → ch04
- **Deactivation** → ch03
- **DIBL / extension doping** → ch02
- **Explosive crystallization / melting** → ch02, ch03, ch05
- **Ferroelectric HfO2** → ch04
- **Ge doping / GeSn** → ch02, ch03
- **GaN** → ch06
- **Hillocks / wrinkles** → ch04
- **IGBT backside** → ch06
- **LPER / SPER** → ch03
- **NEMS** → ch05
- **Phase segregation (Si/C)** → ch06, ch08
- **Raman fc / XRD markers** → ch07, ch08
- **Segregation coefficient k, velocity V** → ch03
- **Thermal budget / 3D** → ch01, ch05
- **Wavelength choice** → ch01, ch07, ch08

## Supporting Files
- [glossary.md](glossary.md) — key terms
- [patterns.md](patterns.md) — techniques with when/how/trade-offs
- [cheatsheet.md](cheatsheet.md) — decision rules, regime table, thresholds, tells

---

## Scope & Limits
Covers only these three reviews (2016–2023); figures were not read (only captions and text), so curve shapes are described from the text. Values are stack-specific literature data, not tool recipes. Two papers are from LASSE/SCREEN authors (vendor perspective). For equipment maintenance cost or PM analytics in this repo, combine with the project's own data and the statistics skills.
