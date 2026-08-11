# src/analysis/fetch_gw190521.py

import os
import numpy as np
import pycbc.types
from pycbc.catalog import Merger

import h5py  # Import h5py at the top

def fetch_validated_data(det):
    """
    Fetches strain data for GW190521 for the specified detector (H1 or L1).
    Returns a PyCBC TimeSeries object.
    """
    try:
        merger = Merger("GW190521")
        strain = merger.strain(det)
        if strain is None:
            raise ValueError(f"Strain data for {det} is null.")
        return strain
    except Exception as e:
        print(f"Error fetching data for {det}: {e}")
        raise

if __name__ == "__main__":
    print("Fetching and validating GW190521 data...")
    os.makedirs("data", exist_ok=True)  # Ensure the data directory exists

    for det in ["H1", "L1"]:
        strain = fetch_validated_data(det)
        print(f"-> {det} successfully pulled. Length: {len(strain)} samples at {strain.sample_rate} Hz")

        # Save as HDF5
        with h5py.File(f"data/GW190521_{det}_strain.h5", "w") as f:
            f.create_dataset("strain", data=strain.numpy())
            f.create_dataset("time", data=strain.sample_times)
            f.attrs["sample_rate"] = strain.sample_rate
            f.attrs["epoch"] = strain.start_time

        # Optional: Save as numpy array too
        # np.save(f"data/GW190521_{det}_strain.npy", strain.numpy())
