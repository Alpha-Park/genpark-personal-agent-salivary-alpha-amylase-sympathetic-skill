"""
Salivary Alpha-Amylase (sAA) & Autonomic Sympathetic Reactivity Engine.
Provides deterministic, zero-dependency computation of sAA surge kinetics,
Area Under the Curve (AUC_G / AUC_I), and sympathetic stress resilience index.
"""

from typing import Dict, Any, List, Optional


class SalivaryAlphaAmylaseClient:
    """
    Deterministic client for analyzing salivary alpha-amylase (sAA) kinetics and autonomic stress recovery.
    Pure Python standard library implementation based on neuroendocrine stress literature.
    """

    def __init__(self):
        pass

    def evaluate_acute_sympathetic_reactivity(
        self,
        baseline_saa_u_ml: float,
        peak_saa_u_ml: float,
        post30_saa_u_ml: float,
        sampling_times_min: Optional[List[float]] = None,
        saa_values_u_ml: Optional[List[float]] = None
    ) -> Dict[str, Any]:
        """
        Evaluates sAA surge, recovery slope, and Sympathetic Stress Resilience Index (SSRI).
        sAA is directly stimulated by sympathetic noradrenergic innervation of parotid glands.
        """
        if baseline_saa_u_ml <= 0:
            return {"error": "Baseline sAA must be a positive value"}

        delta_saa = max(0.0, peak_saa_u_ml - baseline_saa_u_ml)
        srr = round(peak_saa_u_ml / max(0.1, baseline_saa_u_ml), 2)

        # Recovery fraction at 30 min post-peak
        recovered_amount = max(0.0, peak_saa_u_ml - post30_saa_u_ml)
        clearance_pct = round((recovered_amount / max(0.1, delta_saa)) * 100.0, 1) if delta_saa > 0 else 100.0
        recovery_velocity = round(recovered_amount / 30.0, 3)

        # Compute AUC using trapezoidal rule if timeseries provided, or standard 3-point approximation
        if sampling_times_min and saa_values_u_ml and len(sampling_times_min) == len(saa_values_u_ml) and len(sampling_times_min) >= 2:
            times = sampling_times_min
            vals = saa_values_u_ml
        else:
            times = [0.0, 15.0, 45.0]  # Baseline (0), Peak (15), Post-stress recovery (45)
            vals = [baseline_saa_u_ml, peak_saa_u_ml, post30_saa_u_ml]

        auc_g = 0.0
        for i in range(len(times) - 1):
            dt = times[i + 1] - times[i]
            trap_area = ((vals[i] + vals[i + 1]) / 2.0) * dt
            auc_g += trap_area

        total_dt = times[-1] - times[0]
        auc_i = max(0.0, auc_g - (vals[0] * total_dt))

        # Sympathetic Stress Resilience Index (SSRI, 0 - 100):
        # Adaptive: Reactivity ratio between 1.5 and 3.5 + clearance >= 70% at 30 min
        reactivity_score = 50.0
        if srr < 1.15:
            reactivity_score = 25.0  # Hypo-reactive / blunted autonomic responsiveness
        elif srr > 4.5:
            reactivity_score = 30.0  # Hyper-reactive adrenergic storm
        else:
            reactivity_score = 50.0  # Healthy adaptive surge

        clearance_score = min(50.0, (clearance_pct / 100.0) * 50.0)
        ssri = round(min(100.0, max(5.0, reactivity_score + clearance_score)), 1)

        is_prolonged_elevation = clearance_pct < 50.0 and delta_saa > 25.0
        is_blunted_reactivity = srr < 1.15 and baseline_saa_u_ml < 30.0

        if ssri >= 80.0:
            status = "OPTIMAL_AUTONOMIC_RESILIENCE"
            interpretation = "Healthy, adaptive sympathetic surge followed by prompt vagal brake reinstatement."
            action = "Autonomic tone is flexible and resilient. Continue routine physiological balance."
        elif is_blunted_reactivity:
            status = "BLUNTED_ADRENERGIC_RESPONSIVENESS"
            interpretation = "Minimal sAA elevation during stress challenge; indicates potential autonomic exhaustion or severe fatigue."
            action = "Prioritize mitochondrial recovery, restorative sleep, and eliminate stimulant reliance."
        elif is_prolonged_elevation:
            status = "CHRONIC_SYMPATHETIC_HYPERAROUSAL"
            interpretation = "Elevated sAA fails to clear after 30 minutes; deficient parasympathetic vagal brake."
            action = "Engage vagal reactivation immediately: 5 minutes of resonant coherent breathing (5.5s inhale, 5.5s exhale)."
        else:
            status = "MODERATE_STRESS_ACCUMULATION"
            interpretation = "Partial clearance of adrenergic surge with mild sympathetic residual."
            action = "Implement somatic unwinding pause and monitor evening recovery trajectory."

        return {
            "baseline_saa_u_ml": baseline_saa_u_ml,
            "peak_saa_u_ml": peak_saa_u_ml,
            "post30_saa_u_ml": post30_saa_u_ml,
            "delta_surge_u_ml": round(delta_saa, 2),
            "sympathetic_reactivity_ratio": srr,
            "post30_clearance_pct": clearance_pct,
            "clearance_velocity_u_ml_min": recovery_velocity,
            "auc_ground": round(auc_g, 1),
            "auc_increase": round(auc_i, 1),
            "sympathetic_stress_resilience_index": ssri,
            "is_prolonged_elevation": is_prolonged_elevation,
            "status": status,
            "interpretation": interpretation,
            "recommended_protocol": action
        }
