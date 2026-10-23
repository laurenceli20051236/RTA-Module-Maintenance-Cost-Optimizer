# Chapter 7: Amorphous-Si Crystallization by Laser — Wavelength, Pulse and Fluence Windows

*Source: Arduino et al. 2023 §3*

## Core Idea
For a-Si → poly-Si, wavelength is the primary parameter because it sets absorption: UV/visible crystallize thin films efficiently near the surface; IR penetrates deeper (works on thicker films) but needs more power and shorter pulses and risks ejection.

## Frameworks Introduced
- **Two-threshold fluence window F1–F2** (Garcia et al., Nd:YVO4 12–15 ns):
  - F < F1: no melt → no phase change.
  - F1 < F < F2: annealing / crystallization window.
  - F > F2: ablation / damage.
  - 355 nm: F1 = 70, F2 = 374 mJ/cm². 532 nm: F1 = 110, F2 = 304 mJ/cm². 1064 nm failed (longer pulse and higher fluence needed → material ejection).
- **Depth vs crystallinity trade-off** (Pan et al., fs): 400 nm gives a sharper Raman peak (higher crystallinity) but does not fully crystallize 100 nm a-Si; 800 nm crystallizes through the film. Grain size grows with fluence and with beam overlap / shot count.
- **Raman crystallinity metrics**:
  - a-Si: broad TO band ~480 cm⁻¹ (420–530); c-Si: sharp ~520 cm⁻¹.
  - Peak shift toward 520 and narrower FWHM = better crystallinity. A blue/red shift can also reflect nanocrystal phonon confinement and stress.
  - **Crystalline volume fraction fc = Ic / (Ic + Ia)** from Gaussian deconvolution of the integrated intensities.

## Key Concepts
- **Si bandgap 1.1 eV** → absorption edge ~1100 nm.
- **GLA / BLA**: green (532 nm ns) / blue (450 nm CW diode) laser annealing.
- **Beam overlap**: fraction of area re-irradiated in scanning.
- **Microlens-array interference**: splitting the beam and recombining it raises local intensity → larger, more regular grains (Son et al.).

## Mental Models
- Pick λ by **film thickness vs δ**: thin film → UV/visible; thick film → IR (with care).
- Read Raman in three numbers: **position, FWHM, fc**.
- Furnace still gives the best crystallinity; laser wins on **locality** (only the surface is heated).

## Anti-patterns
- **Pushing IR fluence to compensate for weak absorption** → ablation/ejection.
- **Judging crystallization by peak presence only** → ignores residual amorphous fraction (use fc).
- **Using UV on thick a-Si and assuming full-depth conversion** → bottom stays amorphous.

## Reference Tables
**Si laser annealing literature summary (Arduino Table 1)**

| Laser | λ | Pulse | Profile | Env. | ED / power |
|---|---|---|---|---|---|
| Yb fiber | 1064 nm | 200 ns | – | ambient | – (20 W avg, 20 kHz) |
| Ti:Sapphire | 800 nm | 50–125 fs | – | – | 38–63 mJ/cm² |
| Ti:Sapphire | 800 nm | – | – | – | 160–305 mJ/cm² |
| Yb:KGW | 800 nm | 40–200 fs | Gaussian | – | 49–69 mJ/cm² |
| Yb:KGW | 1026 nm | 230 fs | Gaussian | – | 150 mJ/cm² |
| Ti:Sapphire | 400 nm | 50 fs | – | – | 20–30 mJ/cm² |
| Nd:YVO4 | 355 nm | 12–15 ns | Gaussian | – | 240 mJ/cm² |
| Nd:YVO4 | 532 nm | 12–15 ns | Gaussian | – | 478 mJ/cm² |
| Nd:YVO4 | 532 nm | CW | Gauss × top-hat | – | 7.5 W |
| Diode | 440 nm | CW | elliptical | – | 4.61 W |
| GaN diode | 450 nm | CW | Gaussian | RT, N2 | 530 mW |
| Nd:YAG | 532 nm | 30 ns | rect. | RT, N2 | 153 mJ/cm² |

**Raman comparison (Pyo et al.)**: furnace 519.0 cm⁻¹ / FWHM 7.5; BLA 517.5 / 9.0, fc 90.6 %; GLA 516.5 / 9.5, fc 88.2 %.

## Worked Example
**Setting a nanosecond a-Si crystallization recipe**: (1) choose λ from film thickness (355 nm for thin films); (2) find F1 by increasing ED until melt is detected (reflectivity or Raman change), and find F2 at the onset of ablation; (3) operate mid-window (e.g., 240 mJ/cm² at 355 nm, which lies within 70–374); (4) verify by Raman (position, FWHM, fc) and cross-sectional SEM/TEM for depth.

## Key Takeaways
1. Wavelength dominates a-Si crystallization through absorption.
2. Always work inside the F1–F2 window.
3. UV/visible suit thin films; IR suits thick films at higher risk.
4. Quantify with fc, not just with peak presence.

## Connects To
- **Ch 4**: poly-Si LPC in BEOL.
- **Ch 5**: SLG regime for NEMS.
- **Ch 8**: the same analysis applied to SiC.
