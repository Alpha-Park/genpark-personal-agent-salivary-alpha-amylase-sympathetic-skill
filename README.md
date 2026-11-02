# Salivary Alpha-Amylase (sAA) Sympathetic Reactivity Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen.svg)](https://github.com/alphaparkinc/genpark-personal-agent-salivary-alpha-amylase-sympathetic-skill)
[![OpenClaw Ready](https://img.shields.io/badge/OpenClaw-Compatible-purple.svg)](https://github.com/alphaparkinc/genpark-personal-agent-salivary-alpha-amylase-sympathetic-skill)
[![MCP Protocol](https://img.shields.io/badge/MCP-Standard-orange.svg)](https://modelcontextprotocol.io/)

A sovereign personal agent capability for computational neuroendocrine modeling of salivary alpha-amylase (sAA) noradrenergic surges, clearance velocity, and autonomic stress resilience scoring.

## Architecture

```mermaid
flowchart TD
    SalivaSamples["sAA Biomarker Timeseries (Baseline, Peak, Post-30m)"] --> SurgeCalc["Surge Delta & Reactivity Ratio (SRR)"]
    SurgeCalc --> AUCEngine["Trapezoidal AUC Engine (AUC_Ground & AUC_Increase)"]
    AUCEngine --> ClearanceEngine["30-Minute Clearance Velocity & Decay Slope"]
    ClearanceEngine --> SSRI["Sympathetic Stress Resilience Index (SSRI: 0-100)"]
    SSRI --> AutonomicGuidance["OpenClaw / Hermes Vagal Brake & Resonant Breathing Protocol"]
```

## Quickstart

```python
from client import SalivaryAlphaAmylaseClient

client = SalivaryAlphaAmylaseClient()

# Assess sympathetic surge and clearance kinetics
res = client.evaluate_acute_sympathetic_reactivity(
    baseline_saa_u_ml=38.5,
    peak_saa_u_ml=112.0,
    post30_saa_u_ml=49.0
)

print("Surge Delta:", res["delta_surge_u_ml"], "U/mL")
print("Reactivity Ratio:", res["sympathetic_reactivity_ratio"], "x")
print("Resilience Index (SSRI):", res["sympathetic_stress_resilience_index"], "/ 100")
print("Interpretation:", res["interpretation"])
```

## MCP Server Integration

Add to your `claude_desktop_config.json` or OpenClaw tool registry:

```json
{
  "mcpServers": {
    "salivary-alpha-amylase": {
      "command": "python",
      "args": ["/path/to/genpark-personal-agent-salivary-alpha-amylase-sympathetic-skill/mcp_server.py"]
    }
  }
}
```

## License
MIT License.
