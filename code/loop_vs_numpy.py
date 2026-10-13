# How much faster is NumPy than a Python loop? Brighten an image both ways and time it.
# Run: python loop_vs_numpy.py ../images/ocean_300_400.jpg
import sys
import time

import cv2
import numpy as np

filename = sys.argv[1] if len(sys.argv) > 1 else "../images/ocean_300_400.jpg"
img = cv2.imread(filename)
if img is None:
    print(f"failed to read image from {filename}")
    sys.exit(1)
print("shape:", img.shape, "pixels * channels:", img.size)


def brighten_loop(image, b):
    result = image.copy()
    rows, cols, channels = image.shape
    for i in range(rows):
        for j in range(cols):
            for c in range(channels):
                result[i, j, c] = min(int(image[i, j, c]) + b, 255)
    return result


def brighten_numpy(image, b):
    return np.clip(image.astype(np.int16) + b, 0, 255).astype(np.uint8)


start = time.perf_counter()
r1 = brighten_loop(img, 50)
t_loop = time.perf_counter() - start

start = time.perf_counter()
r2 = brighten_numpy(img, 50)
t_numpy = time.perf_counter() - start

start = time.perf_counter()
r3 = cv2.add(img, 50)
t_cv = time.perf_counter() - start

print(f"loop:  {t_loop * 1000:10.2f} ms")
print(f"numpy: {t_numpy * 1000:10.2f} ms")
print(f"cv2:   {t_cv * 1000:10.2f} ms")
print(f"numpy is {t_loop / t_numpy:.0f} times faster than the loop")
print("same result:", np.array_equal(r1, r2) and np.array_equal(r2, r3))
