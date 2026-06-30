from src.bmi_engine import BMIEngine

def perform_deep_time_sweep():
    engine = BMIEngine()
    
    print(f"\n{'Epoch (Gyr)':<15} | {'N':<10} | {'Total Field':<15}")
    print("-" * 45)
    
    # We check in 100 Gyr increments up to 1,000 Gyr
    for t in range(100, 1001, 100):
        # We use the existing engine logic
        # Note: We are parsing the return string, but for raw data
        # we could modify the engine, but this works for observation.
        result_str = engine.run_simulation_by_time(t)
        
        # Simple string parsing to extract the data for our table
        # Format: "Time: X | N=Y | Baryonic: A | DE: B | Total: C"
        parts = result_str.split('|')
        n_val = parts[1].split('=')[1].strip()
        total_val = parts[4].split(':')[1].strip()
        
        print(f"{t:<15} | {n_val:<10} | {total_val:<15}")

if __name__ == "__main__":
    perform_deep_time_sweep()
