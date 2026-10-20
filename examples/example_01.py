import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as plt_patches

if len(sys.argv) != 2:
    print("Usage: python ex04.py <string>")
    exit(1)

print(f"Image file: {sys.argv[1]}")

img = cv2.imread(sys.argv[1])
if img is None:
    print("failed to read the image")
    exit(1)

rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
print(f"Image type: {type(img)}")
print(f"Image dtype: {img.dtype}")
print(f"Image shape: {img.shape}")

print(f"Top-left pixel (R, G, B): {rgb_img[0, 0]}")
green_channel = img[:, :, 1]

index = green_channel.argmin()  # Find the index of the darkest pixel in the green channel
index_2D = np.unravel_index(index, green_channel.shape)  # Convert the flat index to 2D coordinates
print(f"Index of the darkest pixel in the green channel: {index}")
print(f"Darkest pixel location (row, column): {index_2D}")



# added after class:
sum_channels = np.sum(img, axis=2)  # Sum the color channels to find the darkest pixel overall
print(f"Sum of color channels shape: {sum_channels.shape}, dtype: {sum_channels.dtype}")
darkest_index = sum_channels.argmin()  # Find the index of the darkest pixel overall
print(f"Index of the darkest pixel overall: {darkest_index}")
darkest_location = np.unravel_index(darkest_index, sum_channels.shape)
print(f"Darkest pixel location (row, column): {darkest_location}")

print(f"Darkest pixel value (R, G, B): {rgb_img[darkest_location]}")

# show the image, draw a rectangle around the darkest pixel
# and show the location of the darkest pixel
plt.imshow(rgb_img)

# Draw a rectangle around the darkest pixel
rect = plt_patches.Rectangle((darkest_location[1]-10, darkest_location[0]-10), 20, 20,
                             fill=False, color='white', linewidth=1)
plt.gca().add_patch(rect)

plt.title("Image with Darkest Pixel Highlighted")
# plt.legend()
plt.axis('off')
plt.show()

