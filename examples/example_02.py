import sys
import cv2
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

rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_img)
plt.show()
