import matplotlib.pyplot as plt
import numpy as np

dx, dy = 0.015, 0.05
x = np.arange(-4.0, 4.0, dx)
y = np.arange(-4.0, 4.0, dy)
X, Y = np.meshgrid(x, y)
extent = np.min(x), np.max(x), np.min(y), np.max(y)
z1 = (np.floor(X) + np.floor(Y)) % 2
plt.imshow(z1, cmap="binary_r", interpolation="nearest", extent=extent, alpha=1)

def chess(x, y):
    return (1 - x / 2 + x ** 5 + y ** 6) * np.exp(-(x ** 2 + y ** 2))

z2 = chess(X, Y)
plt.imshow(z2, alpha=0.7, interpolation="bilinear", extent=extent, cmap="viridis")

plt.title("Chess Board with Python")
plt.show()
