# NumPy basics: dtype, shape, overflow.
# Run: python numpy_basics.py
import numpy as np

# A small "image": 2 rows, 3 columns, one byte per pixel
a = np.array([[10, 100, 200],
              [50, 150, 250]], dtype=np.uint8)

print("a =")
print(a)
print("dtype:", a.dtype)        # uint8 = unsigned 8-bit integer, 0..255
print("shape:", a.shape)        # (rows, columns)
print("ndim:", a.ndim)          # number of dimensions
print("size:", a.size)          # number of elements
print("itemsize:", a.itemsize)  # bytes per element
print("nbytes:", a.nbytes)      # total bytes = size * itemsize
print()

# Element access: [row, column]
print("a[1, 2] =", a[1, 2])
print()

# Arithmetic on uint8 wraps around (modulo 256)
print("a + 10 =")
print(a + 10)                   # 250 + 10 -> 4
print("a - 20 =")
print(a - 20)                   # 10 - 20 -> 246
print()

# A Python int that does not fit in uint8 is an error (NumPy 2)
try:
    print(a + 300)
except OverflowError as e:
    print("a + 300 -> OverflowError:", e)
print()

# Multiplying by a float gives a float array (float64)
b = a * 1.5
print("a * 1.5 =")
print(b)
print("dtype:", b.dtype)
print()

# Back to uint8: first clip to 0..255, then convert
c = np.clip(b, 0, 255).astype(np.uint8)
print("np.clip(a * 1.5, 0, 255).astype(np.uint8) =")
print(c)
print()

# Never convert floats outside 0..255 to uint8 without clip: the result is not defined
# (it may differ between computers)

# Reductions
print("min:", a.min(), "max:", a.max(), "mean:", a.mean())
print("sum:", a.sum(), "dtype of sum:", a.sum().dtype)  # NumPy uses a bigger type for sum
print("max of each column (axis=0):", a.max(axis=0))
print("max of each row (axis=1):", a.max(axis=1))
print()

# A color image has 3 dimensions: rows, columns, channels
img = np.zeros((4, 6, 3), dtype=np.uint8)
img[:, :, 0] = 255              # first channel of every pixel
print("color image shape:", img.shape, "ndim:", img.ndim, "nbytes:", img.nbytes)
print("pixel [0, 0]:", img[0, 0])
