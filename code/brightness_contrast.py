# Brightness (add) and contrast (multiply): NumPy vs OpenCV vs float + clip.
# Run: python brightness_contrast.py ../images/ocean_300_400.jpg
import sys

import cv2
import matplotlib.pyplot as plt
import numpy as np

filename = sys.argv[1] if len(sys.argv) > 1 else "../images/ocean_300_400.jpg"
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)   # 2D array, uint8
if img is None:
    print(f"failed to read image from {filename}")
    sys.exit(1)

b = 100      # brightness offset
k = 1.8      # contrast factor

bright_np = img + b                       # uint8 + int: wraps around modulo 256
bright_cv = cv2.add(img, b)               # OpenCV saturates: values above 255 become 255
bright_clip = np.clip(img.astype(np.int16) + b, 0, 255).astype(np.uint8)

contrast_wrap = img * 2                   # uint8 * int: wraps around modulo 256
contrast_float = img * k                  # float64, values may be above 255
contrast_clip = np.clip(contrast_float, 0, 255).astype(np.uint8)

images = [
    (img, "original"),
    (bright_np, f"img + {b} (NumPy)"),
    (bright_cv, f"cv2.add(img, {b})"),
    (bright_clip, f"clip(int16 + {b})"),
    (contrast_wrap, "img * 2 (NumPy)"),
    (contrast_clip, f"clip(img * {k})"),
]

fig, axes = plt.subplots(2, 3, figsize=(12, 9))
for ax, (image, title) in zip(axes.ravel(), images):
    # vmin/vmax: without them Matplotlib stretches each image to its own min..max
    ax.imshow(image, cmap="gray", vmin=0, vmax=255)
    ax.set_title(f"{title}\nmin={image.min()} max={image.max()}")
    ax.axis("off")
plt.tight_layout()
plt.show()
