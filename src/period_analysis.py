from src.bmi_engine import BMIEngine

def analyze_periodicity():
    engine = BMIEngine()
    
    # Store history
    data = []
    # High resolution: 5 Gyr steps up to 3000 Gyr
    for t in range(0, 3000, 5):
        result_str = engine.run_simulation_by_time(t)
        # Parse total field
        total_field = float(result_str.split('|')[-1].split(':')[1].strip())
        data.append((t, total_field))
    
    # Find peaks (local maxima)
    peaks = []
    for i in range(1, len(data) - 1):
        prev_v = data[i-1][1]
        curr_v = data[i][1]
        next_v = data[i+1][1]
        
        # Simple peak detection
        if curr_v > prev_v and curr_v > next_v and curr_v > 0.1: # Only track significant peaks
            peaks.append(data[i][0])
    
    print(f"\nDetected Peaks at (Gyr): {peaks}")
    
    # Calculate periods
    if len(peaks) > 1:
        periods = [peaks[i+1] - peaks[i] for i in range(len(peaks)-1)]
        avg_period = sum(periods) / len(periods)
        print(f"Calculated Average Period: {avg_period:.2f} Billion Years")
    else:
        print("Not enough data to calculate period yet.")

if __name__ == "__main__":
    analyze_periodicity()
