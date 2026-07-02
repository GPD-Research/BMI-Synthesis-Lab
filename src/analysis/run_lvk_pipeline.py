import sys
import numpy as np
from fetch_gw250114 import fetch_validated_data

def run():
    for det in ['H1', 'L1']:
        data = fetch_validated_data(det)
        fft = data.fft()
        power = np.abs(fft.value)**2
        mask = (fft.frequencies.value >= 50) & (fft.frequencies.value <= 250)
        peak = fft.frequencies.value[mask][np.argmax(power[mask])]
        print(f'{det} Anomaly: {peak:.2f} Hz')

if __name__ == '__main__':
    run()