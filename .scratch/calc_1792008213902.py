import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y_sin = np.sin(x)

# Avoid division by zero at x = 0 for sin(x)/x
y_sinc = np.where(x == 0, 1.0, np.sin(x) / x)

plt.figure(figsize=(8, 5))
plt.plot(x, y_sin, label=r'$\sin(x)$', color='blue', linewidth=1.5)
plt.plot(x, y_sinc, label=r'$\frac{\sin(x)}{x}$', color='red', linestyle='--', linewidth=1.5)

plt.title(r'Comparison of $\sin(x)$ and $\frac{\sin(x)}{x}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
plt.axvline(0, color='black', linewidth=0.8, linestyle=':')
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.savefig('compare.png', dpi=300)
print("Plot generated and saved as compare.png")
