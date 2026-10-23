# Chapter 1: Laser Annealing Fundamentals, Thermal Budget & the LT Tool

*Sources: Tabata et al. 2022 §1; Arduino et al. 2023 §2; Huet et al. 2016 §2*

## Core Idea
UV laser annealing (UV-LA) decouples "process temperature" from "thermal budget": shallow UV absorption plus ns–µs dwell confines heat to the top ~100 nm–1 µm, so the surface can reach (or exceed) melt while buried layers stay within a 500 °C-class budget.

## Frameworks Introduced
- **Thermal budget = temperature (activation energy) × time (kinetics)**: the empirical lens for deciding whether a step is 3D-compatible.
  - When to use: any time a high-T step must run above fragile underlayers (BEOL, bottom-tier devices).
  - How: compare the local T(t) profile of the *buried* layer (from simulation) against the accepted limit — ~500 °C for a few hours for 3D sequential integration (Batude/Fenouillet, cited in both Tabata and Huet).
- **Two levers of vertical heat confinement** (Tabata):
  1. *UV wavelength* → strongly limited absorption depth → surface-localized heat source.
  2. *ns–µs timescale* → thermal diffusion length too short to reach the bottom tier.
  - Extra knobs: buried-oxide (SiO2) thickness (thicker = better thermal isolation) and laser fluence.
- **Beer–Lambert absorption** (Arduino): I(z) = I0·e^(−αz); optical penetration depth δ = 1/α (depth where intensity falls to 1/e ≈ 37%). Also written as δ ∝ λ/(4πk), with k the extinction coefficient. α and δ depend on material, λ, and temperature.
- **Photothermal vs photochemical processing** (Arduino):
  - *Photothermal (pyrolytic)*: excitation rate < thermalization rate → absorbed energy becomes heat; typical for ns-and-longer pulses on semiconductors; analyze purely thermally.
  - *Photochemical (photolytic)*: excitation rate > thermalization rate → excited states accumulate, direct bond breaking without temperature rise; fs pulses with photon energy ≈ bond energy.
  - Thermalization time: non-metals ~10⁻⁸–10⁻⁶ s; metals ~10⁻¹²–10⁻¹⁰ s. Electron→phonon transfer < 1 ps.

## Key Concepts
- **Fluence / energy density (ED)**: energy per unit area per pulse (J/cm²); the primary process knob on LT tools.
- **Power density**: used instead of ED for CW lasers.
- **Pulse duration (FWHM)**: LT tool = 160 ns; excimer literature 20–30 ns; solid-state 10–200 ns.
- **Dwell time**: effective time at high T; ns UV-LA ~10⁻⁷ s.
- **Step-and-repeat anneal**: LT-series exposes a full stepper field per shot, unlike scanning lasers.
- **Assisted heating**: chuck pre-heat (LT-3100 up to 450 °C) to extend activation depth.
- **Beam profile**: Gaussian (center-hot, edge-cool) vs rectangular/top-hat (uniform).
- **Scanning tools**: plotter head (fixed mirrors + stage) vs galvo head (rotating mirrors; stage only for large moves).

## Mental Models
- Think of UV-LA as a **"vertical selectivity" tool**, not just a fast RTP: the point is that the bottom tier never sees the peak.
- Use **wavelength to set depth** and **pulse length to set diffusion distance**; use **fluence to set the regime** (sub-melt / melt / over-melt).
- Treat the ns–µs regime as **thermally equilibrated but chemically/mechanically non-equilibrium** (Tabata conclusion) — that is where metastable activation, unusual segregation and phase selection come from.
- **Environment matters at high T**: air oxidizes; vacuum / Ar / N2 / low-O2 (<10 ppm on LT-3100) avoids reactions.

## Anti-patterns
- **Judging 3D compatibility by peak surface temperature**: the relevant metric is the buried layer's T(t), which requires thermal simulation.
- **Assuming fs and ns lasers act the same**: fs pulses can ablate or act photochemically; absorption depth shrinks through multiphoton effects.
- **Ignoring λ-dependent absorption**: photons below the bandgap pass through (unless defects or multiphoton absorption help).

## Reference Tables
**SCREEN LT-3100 key specs (Huet 2016)**

| Parameter | Value |
|---|---|
| Wavelength | UV excimer (Huet states only "UV"; 308 nm per LASSE works cited in Arduino Table 2 / Kerdilès) |
| Pulse duration | 160 ns |
| Anneal scheme | step-and-repeat, full field |
| Field size | up to 26 mm × 33 mm |
| Beam non-uniformity | < ±4 % over field |
| Assisted heating | up to 450 °C |
| Ambient | < 10 ppm O2 |
| Max surface T | up to melting point |

**Laser system parameters to control (Arduino §2)**

| Parameter | Effect |
|---|---|
| Laser technology (gas/excimer/solid-state) | sets available λ, pulse width, power |
| Wavelength | absorption efficiency and depth |
| Power + spot size | power density; ED per pulse |
| Pulse duration | heat confinement; fs risks ablation |
| Scan speed | slower = longer local dwell = stronger anneal |
| Beam profile | spatial uniformity |
| Environment | oxidation / contamination |

## Worked Example
**3D sequential compatibility check (Tabata Fig. 2, 28 nm FDSOI)**: a top-tier layer was UV-LA processed above bottom FDSOI MOSFETs and Cu BEOL. Procedure: (1) simulate T(t) at the bottom device and Cu levels; (2) measure Cu line resistivity before/after; (3) compare ION–IOFF distributions of bottom n/pMOS before/after. Result: no significant degradation → UV-LA is 3D-thermal-budget compatible. Use the same three-step check (simulate → interconnect R → device ION/IOFF) when qualifying any new top-tier anneal.

## Key Takeaways
1. 3D sequential budget ≈ 500 °C for a few hours; UV-LA meets it by confinement, not by being "cold".
2. Absorption depth (λ) and diffusion length (pulse) are independent knobs; fluence picks the regime.
3. Thicker buried oxide isolates heat better.
4. ns-µs UV-LA is photothermal; fs can be photochemical/ablative.
5. Tool uniformity (<±4 %) and ambient O2 (<10 ppm) are production-relevant specs, not footnotes.

## Connects To
- **Ch 5**: 3D sequential integration process windows.
- **Ch 7/8**: wavelength vs bandgap for Si and SiC.
- **RTA / spike / ms flash anneal**: the conventional baselines UV-LA is compared against.
