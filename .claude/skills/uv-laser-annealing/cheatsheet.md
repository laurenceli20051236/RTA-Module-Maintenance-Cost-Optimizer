# UV Laser Annealing — Decision Cheatsheet

## Decision rules
- **Buried fragile layer (BEOL / bottom tier)** → use ns–µs UV-LA, not RTP/spike; verify the buried T(t) by simulation, not the surface peak T.
- **Need zero diffusion** → stay sub-melt (ns). **Need >solubility activation** → melt (LPER) or multi-shot/µs SPER.
- **Melting an implanted layer** → melt past the a/c interface, EOR and the implant tail, or extended defects form.
- **Thin SOI** → ED ∈ [a/c+EOR melt, BOX melt]; aim for ~10 % margin.
- **Contact needs surface pile-up** → k<1 dopant; lower V boosts segregation, higher V boosts incorporation → pick a compromise.
- **Flat surface critical** → prefer SPER; if melting, plan CMP/cap and check wrinkles.
- **After metastable activation** → audit every later thermal step for deactivation.
- **Deep (µm) backside activation** → add assisted heating (≤350–450 °C) instead of more ED.
- **Wide bandgap (SiC/GaN)** → UV only; expect surface Si/C (Ga/N) segregation; inert ambient.
- **a-Si thin film** → UV/visible; **thick film** → IR at higher ablation risk.
- **a-SiC** → near-stoichiometric (x ≈ 0.4–0.5) and just above threshold; graphite Raman = overshoot.

## Regime by ED (generic)
| ED region | Si result | Action |
|---|---|---|
| < melt threshold (F1) | solid-phase effects only | multi-shot SPER / relaxation |
| partial melt of amorphous layer | defective / poly | increase ED |
| full a/c + EOR melt | defect-free epi | **target** |
| melt reaches BOX / seed lost | poly-Si | decrease ED |
| > ablation (F2) | damage | decrease ED |

## Thresholds & defaults (from the sources)
| Item | Value |
|---|---|
| 3D sequential budget | ~500 °C, few hours |
| BEOL furnace anneal | <420 °C up to 1 h |
| IGBT front side | <400 °C |
| LT-3100 pulse / field / uniformity | 160 ns / 26×33 mm / <±4 % |
| LT-3100 assist heat / O2 | ≤450 °C / <10 ppm |
| ρc target | <1–2e-9 Ω·cm² → ~1e21 cm⁻³ active |
| Bulk Si melt ED (160 ns) | ~1.7 J/cm²; Ge-implanted <0.25 |
| 23 nm SOI capped window | ~0.8–0.85 J/cm², ±10 %; uncapped ~1.25 |
| Buried Cu damage threshold | ~0.35 J/cm² (top a-Si stack) |
| NEMS poly-Si SLG | ~0.7 J/cm² |
| Melt diffusivity | ~1e-4 cm²/s, bounded by melt depth |
| ns SPER rate | 0.8–1.8 nm/shot; >20 shots |
| a-Si F1/F2 @355 nm | 70 / 374 mJ/cm² |
| a-SiC KrF threshold | ~250 mJ/cm² |

## Tells & smells
- Rs good but TEM shows a defect band at the melt bottom → partial melt of the implant tail.
- Hillocks on poly-Si → LPC grain-boundary collision (plan CMP).
- Periodic surface ripples under a cap → wrinkles; melt depth too large for the stack.
- Graphite bands (1350/1600 cm⁻¹) on SiC → over-fluence or C-poor film.
- Damage only in sparse-metal areas → local heat sinking difference.
- Rs drifts up after BEOL steps → metastable dopant deactivation.
- Cu Rs rises after melt LA → barrier interdiffusion.
