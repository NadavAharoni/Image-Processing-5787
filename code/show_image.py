# Read an image with OpenCV and show it, and its three color channels, with Matplotlib.
# Run: python show_image.py ../images/ocean_300_400.jpg
import sys

import cv2
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <string>")
    exit(1)

filename = sys.argv[1] if len(sys.argv) > 1 else "../images/ocean_300_400.jpg"
img = cv2.imread(filename)      # numpy array, channel order is B, G, R
if img is None:
    print(f"failed to read image from {filename}")
    sys.exit(1)

print("type:", type(img))
print("dtype:", img.dtype, "shape:", img.shape, "ndim:", img.ndim)
print("top-left pixel (B, G, R):", img[0, 0])

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)     # Matplotlib expects R, G, B

fig, axes = plt.subplots(1, 5, figsize=(16, 4))
axes[0].imshow(img)
axes[0].set_title("BGR shown as RGB (wrong)")
axes[1].imshow(rgb)
axes[1].set_title("RGB (correct)")
for i, name in enumerate(["R", "G", "B"]):
    # Each channel is a 2D plane; show it in gray, 0 = black, 255 = white
    axes[i + 2].imshow(rgb[:, :, i], cmap="gray", vmin=0, vmax=255)
    axes[i + 2].set_title(f"{name} channel")
for ax in axes:
    ax.axis("off")
plt.tight_layout()
plt.show()
