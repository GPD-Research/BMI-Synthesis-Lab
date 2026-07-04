import numpy as np
from sunpy.map import Map
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt
import glob
import os

def get_files_by_date(date_string, directory="../../data"):
    # Finds files matching the date string (e.g., '20260103')
    pattern = os.path.join(directory, f"*{date_string}*.fits")
    files = glob.glob(pattern)
    return files

def process_and_compare(peri_date, aph_date):
    # 1. Get files
    peri_files = get_files_by_date(peri_date)
    aph_files = get_files_by_date(aph_date)
    
    if not peri_files or not aph_files:
        print("Error: Could not find files for one or both dates.")
        return

    # 2. Load and stack (Median to remove noise)
    peri_maps = [Map(f).data for f in peri_files]
    aph_maps = [Map(f).data for f in aph_files]
    
    avg_peri = np.median(peri_maps, axis=0)
    avg_aph = np.median(aph_maps, axis=0)
    
    # 3. Calculate initial residual
    residual = avg_peri - avg_aph
    
    # 4. Remove large-scale rotation (Gaussian Blur background)
    rotation_background = gaussian_filter(residual, sigma=50)
    high_freq_residual = residual - rotation_background
    
    # 5. Mask the limb (keep inner 80%)
    h, w = high_freq_residual.shape
    y, x = np.ogrid[:h, :w]
    center = (h / 2, w / 2)
    mask = ((x - center[1])**2 + (y - center[0])**2) < (h * 0.4)**2
    masked_residual = high_freq_residual * mask
    
 # 6. (Your existing) Visualize
    plt.figure(figsize=(8, 8))
    plt.imshow(masked_residual, cmap='RdBu_r', vmin=-15, vmax=15)
    plt.colorbar(label='Velocity Residual (m/s)')
    plt.title(f'Manifold Stress: {peri_date} vs {aph_date}')
    plt.show()
    
    # --- ADD THIS NEW PART AT THE VERY BOTTOM ---
    
    # 7. Perform a 2D Fourier Transform to look for coherent patterns
    # We use the 'masked_residual' we created in step 5
    import scipy.fftpack as fft
    
    f_transform = fft.fft2(masked_residual)
    f_shift = fft.fftshift(f_transform)
    # The +1 is to avoid log(0) errors
    magnitude_spectrum = 20 * np.log(np.abs(f_shift) + 1)
    
    plt.figure(figsize=(8, 8))
    plt.imshow(magnitude_spectrum, cmap='magma')
    plt.title('Fourier Space: Looking for Coherent Manifold Harmonics')
    plt.colorbar(label='Magnitude (Log scale)')
    plt.show()

if __name__ == "__main__":
    # Ensure these dates match your filenames exactly
    process_and_compare("20260103", "20250703")
