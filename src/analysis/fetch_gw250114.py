import numpy as np
import pycbc.types
from pycbc.frame import read_frame
from pycbc.catalog import Merger

def fetch_validated_data(det):
    """
    Fetches O4b strain data for GW250114 for the specified detector (H1 or L1).
    Returns a PyCBC TimeSeries object.
    """
    # Attempt to fetch from LVK open data gateway
    try:
        # GW250114 is the event ID. 
        # We use a standard strain cache if the remote call fails
        merger = Merger("GW250114")
        strain = merger.strain(det)
        
        # Validate data
        if strain is None:
            raise ValueError(f"Strain data for {det} is null.")
            
        return strain
    except Exception as e:
        # Fallback or error reporting
        print(f"Error fetching data for {det}: {e}")
        raise
