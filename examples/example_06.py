import numpy as np
import matplotlib.pyplot as plt

# The letter F as an array of points: one row of x, one row of y
F = np.array([[0, 3, 3, 1, 1, 2.5, 2.5, 1, 1, 0],    # x
              [0, 0, 1, 1, 2, 2, 3, 3, 5, 5]])      # y
print(f"F: shape: {F.shape}, dtype: {F.dtype}")

fig, axes = plt.subplots(1, 2, figsize=(8, 5))

# Left: the letter as a filled shape
ax = axes[0]
ax.fill(F[0], F[1], alpha=0.5)          # pts: an array of points, shape (2, n)
ax.plot(0, 0, "ko")                     # the origin (0, 0)
ax.set_title("ax.fill")

# Right: the outline only, dashed (append the first point to close the shape)
closed = np.hstack([F, F[:, :1]])       # shape (2, n + 1)
ax = axes[1]
ax.plot(closed[0], closed[1], "k--")
for i, (x, y) in enumerate(F.T):        # number the points in order
    ax.annotate(str(i), (x, y), textcoords="offset points", xytext=(5, 5))
ax.plot(0, 0, "ko")
ax.set_title("ax.plot, dashed")

for ax in axes:
    ax.invert_yaxis()                   # y down, as in an image
    ax.set_aspect("equal")              # the same scale on both axes
    ax.grid(True)
    ax.set_xlabel("x")
    ax.set_ylabel("y")

plt.tight_layout()
plt.show()
