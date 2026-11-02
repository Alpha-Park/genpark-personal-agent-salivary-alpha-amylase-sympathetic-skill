"""
Example usage for Salivary Alpha-Amylase (sAA) Sympathetic Skill.
Demonstrates analyzing acute adrenergic surge and evaluating stress resilience index.
"""

from client import SalivaryAlphaAmylaseClient


def main():
    client = SalivaryAlphaAmylaseClient()

    print("=== 1. Evaluating Acute Autonomic Stress Reactivity (Public Speaking Challenge) ===")
    res = client.evaluate_acute_sympathetic_reactivity(
        baseline_saa_u_ml=38.5,
        peak_saa_u_ml=112.0,
        post30_saa_u_ml=49.0,
        sampling_times_min=[0.0, 15.0, 30.0, 45.0],
        saa_values_u_ml=[38.5, 112.0, 75.0, 49.0]
    )
    print(f"Baseline sAA: {res['baseline_saa_u_ml']} U/mL | Peak: {res['peak_saa_u_ml']} U/mL | 30m Post: {res['post30_saa_u_ml']} U/mL")
    print(f"Surge Delta: +{res['delta_surge_u_ml']} U/mL | Reactivity Ratio: {res['sympathetic_reactivity_ratio']}x")
    print(f"30m Clearance: {res['post30_clearance_pct']} % (Velocity: {res['clearance_velocity_u_ml_min']} U/mL/min)")
    print(f"AUC Ground: {res['auc_ground']} | AUC Increase: {res['auc_increase']}")
    print(f"Resilience Index (SSRI): {res['sympathetic_stress_resilience_index']} / 100")
    print(f"Status: {res['status']}")
    print(f"Interpretation: {res['interpretation']}")
    print(f"Action Protocol: {res['recommended_protocol']}")


if __name__ == "__main__":
    main()
