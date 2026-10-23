# Chapter 6: Power Devices — IGBT Deep Buffer Activation, SiC, GaN, Ohmic Contacts

*Source: Huet et al. 2016 §5*

## Core Idea
UV melt LA was first adopted in HVM for backside anode activation of IGBTs and diodes; with assisted heating it scales to µm-deep buffers in Si, and its out-of-equilibrium heating opens processing routes for SiC and GaN that furnaces cannot reach.

## Frameworks Introduced
- **Thin-wafer IGBT backside rule**: wafer < 100 µm; p-collector (B) + n-buffer (P) activated from the back in one step; **front side must stay < 400 °C**; diffusion must be controlled.
- **Assisted heating extends activation depth**: P implanted at 3 MeV (Rp = 2.38 µm), ED 8.5–10 J/cm², chuck RT→350 °C. At 350 °C, activation extends ~2 µm deeper; near-100 % activation over ~4 µm.
- **Wide-bandgap photon rule**: SiC/GaN need photons above the bandgap → in practice UV. Visible/IR only couple through other layers or defects.
- **SiC melt regrowth out of equilibrium**: equilibrium liquid SiC needs >~3200 °C and ~10⁵ bar (not industrial); UV-LA localizes heat to ~200 nm in sub-µs → melt-like epitaxial 4H regrowth.
  - Side effect: Si/C segregation → graphite / poly-Si / 4H-SiC stack at the surface.
  - Al-implanted 4H-SiC (160 keV 7e14 heaviest step), ED 2.0–4.0 J/cm²: melt depth scales with ED; activation in both liquid and solid phase.
- **GaN**: thermal anneal limited by N evaporation (voids, Ga-rich). Pulsed UV: expect surface N loss / Ga segregation but intact stoichiometry deeper. Mg:GaN with 248 nm KrF (23 ns): best ~0.375 J/cm², ~10 pulses (PL + I-V). LA + RTP can cure RTP-induced roughness (Be:GaN).
- **Ohmic contacts (SiC/GaN)**: need high T for low Rc, but full-wafer high T causes non-uniformity and clustering. LA on backside SiC SBD: thin + controlled roughening → 100 nm Ni sputter → optimized clean → LA 1.5–4 J/cm² → Ni silicide with a uniform C nanocluster layer and repair of thinning damage.

## Key Concepts
- **SRA**: spreading resistance analysis (active profile) vs SIMS (chemical profile).
- **Anode / p-collector**: backside layer activated by LA.
- **n-buffer / field stop**: deeper P layer; thicker = higher breakdown.
- **Polytypes**: 4H-SiC (high mobility), 3C (cubic).
- **Phase segregation**: Si/C separation at the melt surface.

## Mental Models
- **Assist heat = depth knob, ED = melt knob**: raise chuck T to push activation deeper without more surface melt.
- **For SiC/GaN, think "surface sacrifice, bulk repair"**: accept a segregated surface layer, then remove or exploit it (e.g., C nanoclusters at the Ni silicide interface).
- **Single backside step** maximizes yield and productivity for thin wafers.

## Anti-patterns
- **Using visible/IR lasers directly on wide-bandgap material**: poor coupling.
- **Furnace activation of GaN**: N evaporation.
- **Over-reading near-surface P peaks** in R&D setups: may be external contamination, not diffusion.

## Reference Tables
| Application | Condition | Result |
|---|---|---|
| Si IGBT n-buffer | P 3 MeV; 10 J/cm²; assist 350 °C | ~100 % activation over ~4 µm |
| 4H-SiC Al implant | 2.0–4.0 J/cm² | epitaxial-like melt regrowth; graphite/poly-Si/SiC surface |
| Mg:GaN | KrF 248 nm, 23 ns, ~0.375 J/cm², ~10 pulses | PL activation ↑, better PN I-V |
| SiC SBD backside ohmic | 100 nm Ni, 1.5–4 J/cm² | NiSi + uniform C nanocluster layer |

## Worked Example
**Deep n-buffer for thin IGBT (Huet Fig. 16)**: (1) implant P at 3 MeV into p-Si (Rp 2.38 µm); (2) single backside LA shot at 10 J/cm²; (3) compare chuck at RT vs 350 °C; (4) SIMS → profile nearly as-implanted in the deep region (little diffusion); (5) SRA → 350 °C assist adds ~2 µm of active depth, reaching ~100 % activation over ~4 µm; (6) ensure the front-side T stays < 400 °C.

## Key Takeaways
1. Power devices were the first HVM UV melt-LA application.
2. Assisted heating converts surface melt LA into µm-deep activation.
3. Wide-bandgap materials need UV photons.
4. SiC/GaN melt LA trades surface segregation for lattice repair and activation.
5. LA gives uniform backside ohmic contacts without heating the front side.

## Connects To
- **Ch 8**: SiC crystallization literature (wavelength, polytype, stoichiometry).
- **Ch 1**: assisted heating spec on LT-3100.
