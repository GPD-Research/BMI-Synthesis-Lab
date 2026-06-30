from src.analysis.bridge_stress import calculate_bridge_stress
from src.analysis.interbrane_potential import calculate_interbrane_potential

def run_early_universe_test():
    # Harmonic depth at 380,000 years (0.00038 Gyr)
    n = 1.40
    
    bridge_stress = calculate_bridge_stress(n)
    gap_tension = calculate_interbrane_potential(n)
    total_equilibrium = bridge_stress + gap_tension
    
    print(f"--- Early Universe Analysis (t=380k years) ---")
    print(f"Harmonic Depth (N): {n}")
    print(f"Bridge Stress (tau): {bridge_stress:.4f}")
    print(f"Gap Tension (V_gap): {gap_tension:.4f}")
    print(f"Total Metric Equilibrium: {total_equilibrium:.4f}")
    print("---------------------------------------------")
    print("Expectation: High amplitude due to dynamic thermal scaling.")

if __name__ == "__main__":
    run_early_universe_test()
    
