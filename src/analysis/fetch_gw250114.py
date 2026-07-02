import os
import numpy as np
from gwpy.timeseries import TimeSeries

def fetch_validated_data(detector='H1'):
    GPS_MERGER = 1420878141.2
    file_map = {'H1': 'data/H-H1_GWOSC_O4b_4KHZ_R1-1420877824-4096.hdf5', 'L1': 'data/L-L1_GWOSC_O4b_4KHZ_R1-1420877824-4096.hdf5'}
    fpath = file_map[detector]
    strain = TimeSeries.read(fpath, format='hdf5.gwosc')
    wide = strain.crop(GPS_MERGER - 2.0, GPS_MERGER + 2.0)
    conditioned = wide.whiten().bandpass(30, 500)
    shift = 0.25 if detector == 'H1' else 0.26
    return conditioned.crop(GPS_MERGER + shift, GPS_MERGER + shift + 0.20)
