---
name: genpark-personal-agent-salivary-alpha-amylase-sympathetic-skill
description: Deterministic evaluation of salivary alpha-amylase (sAA) noradrenergic surges, clearance velocity, and autonomic stress resilience scoring.
version: 1.0.0
author: GenPark Autonomous Agents Ecosystem
license: MIT
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
---

# Salivary Alpha-Amylase (sAA) Sympathetic Reactivity Skill

## Overview
The `genpark-personal-agent-salivary-alpha-amylase-sympathetic-skill` delivers mathematical modeling of salivary alpha-amylase (sAA) dynamics to personal sovereign agents. Salivary alpha-amylase is secreted by parotid acinar cells under direct $\beta$-adrenergic sympathetic innervation, functioning as an instantaneous surrogate biomarker of sympathetic adrenomedullary system activation (distinct from the delayed hypothalamic-pituitary-adrenal cortisol axis). This skill computes acute surge magnitude, post-stress clearance velocity, area under the curve ($AUC_G$, $AUC_I$), and the Sympathetic Stress Resilience Index ($SSRI$).

## Physiological Model & Mathematics
1. **Acute Surge Delta & Reactivity Ratio**:
   $$\Delta sAA = sAA_{\text{peak}} - sAA_{\text{baseline}}$$
   $$SRR = \frac{sAA_{\text{peak}}}{sAA_{\text{baseline}}}$$
2. **Clearance Velocity ($k_{\text{rec}}$)**:
   $$k_{\text{rec}} = \frac{sAA_{\text{peak}} - sAA_{\text{post30}}}{\Delta t_{\text{post}}}$$
3. **Trapezoidal Area Under the Curve**:
   $$AUC_G = \sum_{i=1}^{n-1} \left(\frac{y_i + y_{i+1}}{2}\right) \cdot (t_{i+1} - t_i)$$
   $$AUC_I = AUC_G - \left(y_1 \cdot (t_n - t_1)\right)$$
4. **Sympathetic Stress Resilience Index ($SSRI$)**:
   Quantifies whether an autonomic stress response is adaptive (robust immediate surge followed by rapid parasympathetic reinstatement clearing $> 70\%$ of excess amylase by 30 minutes) versus maladaptive (chronic sympathetic hyperarousal or allostatic exhaustion).

## Tools & Endpoints
- `evaluate_acute_sympathetic_reactivity`: Computes sAA surge, clearance percentage, $AUC_G$, $AUC_I$, and $SSRI$ resilience score.
