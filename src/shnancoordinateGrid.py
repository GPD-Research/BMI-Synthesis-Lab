$$python import numpy as np import matplotlib.pyplot as plt from mpl_toolkits.mplot3d import Axes3D
R = 100e9  # Major radius in light years r = 10e9   # Minor radius in light years
theta = np.linspace(0, 2  np.pi, 100) phi = np.linspace(0, 2  np.pi, 100) theta, phi = np.meshgrid(theta, phi)
x = (R + r  np.cos(phi))  np.cos(theta) y = (R + r  np.cos(phi))  np.sin(theta) z = r * np.sin(phi)
print("Sample Coordinates:") print(f"x: {x[0, 0]}, y: {y[0, 0]}, z: {z[0, 0]}")
def distance_to_angle(distance, R): return distance / R
distances = np.array([9e9, 10e9, 11e9, 12e9, 13e9, 14e9]) angles = distance_to_angle(distances, R) print("Angles (radians):", angles)
fig = plt.figure() ax = fig.add_subplot(111, projection='3d') ax.plot_surface(x, y, z, color='b', alpha=0.6)
plt.show()$$
