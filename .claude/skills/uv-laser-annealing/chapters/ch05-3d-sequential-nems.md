# Chapter 5: 3D Sequential Integration (CoolCube™) & NEMS Above IC

*Sources: Huet et al. 2016 §4; Tabata et al. 2022 §1*

## Core Idea
Sub-µm heat confinement lets top-tier junctions reach RTP-equivalent Rs while buried transistors and Cu interconnects see no change — **provided the fluence sits inside a window bounded below by full a/c + EOR melt and above by melting the buried-oxide interface.**

## Frameworks Introduced
- **Melt-LA process window on thin SOI** (Huet Fig. 13):
  - Lower bound: ED that melts the a/c interface and EOR defects → defect-free crystal.
  - Upper bound: ED that melts down to the BOX interface → seed lost → poly-Si.
  - Result (23 nm Si / 25 nm BOX, 7 nm SiN cap, BF2/As/P): optimum ~0.8–0.85 J/cm² with ~10 % margin; Rs ≈ or better than 1050 °C spike RTP. Uncapped: window shifts to ~1.25 J/cm².
- **Top-tier activation options** under the 500 °C budget: SPER-based low-T activation, or surface-confined heating (UV-LA).
- **Buried-interconnect robustness check** (short-loop, 28 nm FDSOI Cu M1 + SiCN + 50/120 nm PECVD oxide + 20 nm a-Si):
  - Confirm melt of the top a-Si with in-situ TRR.
  - Damage threshold ~0.35 J/cm², independent of oxide thickness; damage more likely in **low metal density** regions.
  - Cu line R and lateral C unchanged even at 0.4 J/cm² (voids in a-Si notwithstanding).
- **Poly-Si NEMS by room-T deposition + UV-LA**: 100 nm sputtered a-Si; resistance drops with ED (explosive crystallization) until the **Super Lateral Growth (SLG)** threshold (~0.7 J/cm²).

## Key Concepts
- **CoolCube™ / sequential 3D**: transistor tiers stacked with lithographic alignment (vs TSV bonding).
- **TRR (time-resolved reflectivity)**: in-situ melt detection; also validated phase-field models.
- **SLG**: near-complete-melt regime giving large lateral grains.
- **Allan deviation**: NEMS frequency-stability metric.
- **Mass resolution (zg)**: NEMS sensing figure of merit.

## Mental Models
- Define every melt-LA window as **[full-damage-melt ED, seed-loss ED]**; margin ≈ 10 % is "comfortable".
- **Metal density modulates local heat sinking** → check sparse-pattern areas first for damage.
- Use **in-situ TRR as a regime sensor** before trusting ED setpoints.

## Anti-patterns
- **Running at ED above the BOX-melt bound** → polycrystalline channel.
- **Qualifying only at dense metal patterns** → misses damage at low density.
- **Assuming capping doesn't move the window** → caps shift the optimal ED (~0.8 vs ~1.25 J/cm²).

## Reference Tables
**Poly-Si vs c-Si NEMS (Huet Table 1, 3e20 cm⁻³)**

| NEMS | Q air/vac | Allan dev. (×10⁻⁷) @100 ms | Mass res. (zg) | Yield | DR (dB) |
|---|---|---|---|---|---|
| c-Si | 113 / 6040 | 3.8 | 0.18 | 100 % | 106 |
| polyA (0.7 J/cm²) | 96 / 4700 | 8.0 | 0.38 | 94 % | 95 |

## Worked Example
**3D SOI window qualification (Huet §4.1)**: (1) implant BF2/As/P into 23 nm SOI and cap with 7 nm low-T SiN; (2) sweep ED 0.4–1.0 J/cm² at 160 ns; (3) strip the cap, map Rs vs ED against a 1050 °C spike reference; (4) TEM each ED to locate regimes (partial melt → full a/c melt → BOX melt); (5) pick ~0.8–0.85 J/cm² (defect-free, ~10 % margin); (6) separately, run a short-loop Cu BEOL wafer under the same top stack, inspect by SEM, and measure line R and C.

## Key Takeaways
1. The SOI melt window is bounded by EOR-melt (low) and BOX-melt (high).
2. ~10 % ED margin is acceptable for integration.
3. Buried Cu is unaffected when the top-tier anneal stays in the window.
4. Low-metal-density zones are the damage-sensitive spots.
5. UV-LA enables poly-Si NEMS above IC with ~94 % yield.

## Connects To
- **Ch 1**: thermal budget lens.
- **Ch 3**: full-melt rule.
- **Ch 4**: poly-Si in BEOL.
