# RTA-Module-Maintenance-Cost-Optimizer

## Overview
This project is a data-driven cost optimization framework for Rapid Thermal Anneal (RTA) toolsets in semiconductor manufacturing.

The goal is to improve preventive maintenance decision-making by combining:
- high-frequency early warning signals
- low-frequency electrical verification
- failure risk estimation
- maintenance cost modeling

This project proposes a two-tier monitoring strategy to reduce dependence on expensive Rs monitor wafers while maintaining process health and early drift detection capability.

---

## Business Problem
Traditional RTA monitoring often relies on high-cost Rs/SheetRho monitor wafers, which:
- require pre-treatment, ion implant, and dose verification
- are expensive to run frequently
- are better suited for final verification than early warning

As a result, the monitoring approach is costly and often reactive instead of proactive.

---

## Proposed Solution
This project redesigns the monitoring strategy into two layers:

### Tier 1: High-Frequency Monitoring
- Implant-based bare wafer
- Haze / cross-section haze measurement
- Every 3 days
- Used for early drift detection, stage alignment, and process trend monitoring

### Tier 2: Low-Frequency Verification
- Rs / SheetRho monitor wafer
- Every 2 weeks to monthly
- Used for long-term uniformity verification and model calibration

---

## Estimated Impact
- Reduce Rs monitor frequency by ~75%
- Save approximately ~$200K annually per RTA toolset
- Improve early drift detection
- Lower risk of late-stage excursions

---

## Project Structure

```text
data/raw/
data/processed/
notebooks/
src/rta_optimizer/
reports/figures/

```text
---
## How to Review This Project

For a quick review:
1. Read `reports/executive_summary.md`
2. Review `src/rta_optimizer/cost_model.py`
3. Open `notebooks/03_cost_optimization.ipynb`
4. Check exported figures in `reports/figures/`

---

## Key Results

### Annual Cost Comparison
![Cost Comparison](reports/figures/cost_comparison.png)

### Annual Cost Breakdown
![Cost Breakdown](reports/figures/cost_breakdown.png)

