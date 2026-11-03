import sys
import cv2
import time
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <string>")
    exit(1)

filename = sys.argv[1]

img = cv2.imread(filename)
if img is None:
    print(f"failed to read {filename}")
    exit(1)

print(f"Image type: {type(img)}, dtype: {img.dtype}, shape: {img.shape}")

weights = np.array([0.114, 0.587, 0.299])          # B, G, R
print(f"weights: {weights}, shape: {weights.shape}, dtype: {weights.dtype}")

img_times_weights = (img * weights)
print(f"img_times_weights: shape: {img_times_weights.shape}, dtype: {img_times_weights.dtype}")

gray = img_times_weights.sum(axis=2)                 # float64, shape (H, W)
print(f"gray: shape: {gray.shape}, dtype: {gray.dtype}")
print(f"gray min: {gray.min()}, max: {gray.max()}")

gray = np.clip(gray, 0, 255).astype(np.uint8)
print(f"gray: shape: {gray.shape}, dtype: {gray.dtype}")

rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


mean = rgb_img.mean()
print(f"Mean value of the image: {mean}")
stretched = (rgb_img - mean) * 1.8 + mean    # stretch around the mean
print(f"stretched: shape: {stretched.shape}, dtype: {stretched.dtype}, "
      f"min: {stretched.min()}, max: {stretched.max()}")
stretched = np.clip(stretched, 0, 255).astype(np.uint8)

mask = gray < 80
print(f"mask: shape: {mask.shape}, dtype: {mask.dtype}, sum: {mask.sum()}")

# display the original, grayscale, stretched and masked images side by side
fig, axes = plt.subplots(1, 4, figsize=(12, 6))
axes[0].imshow(rgb_img)
axes[0].set_title("Original")
axes[0].axis("off")

axes[1].imshow(gray, cmap="gray", vmin=0, vmax=255)
axes[1].set_title("Grayscale")
axes[1].axis("off")

axes[2].imshow(stretched)
axes[2].set_title("Stretched")
axes[2].axis("off")

# set pixels in the original image to black where the
# grayscale value is less than 80

start = time.perf_counter()
rgb_img[mask] = [0, 0, 0]
end = time.perf_counter()
print(start, end)
print(f"Time taken to apply mask: {end - start:.6f} seconds")

axes[3].imshow(rgb_img)
axes[3].set_title("Masked (Grayscale < 80)")
axes[3].axis("off")

plt.show()
