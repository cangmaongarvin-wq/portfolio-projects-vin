# Recreating the Cliff walk at Pourville

import numpy as np
import matplotlib.pyplot as plt

# This will now work in your VS Code!
with open("mystery_image.npy", "rb") as f:
    rgb_array = np.load(f)

# The darker version of the painting
dark_rgb_array = rgb_array * 0.5

fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].imshow(rgb_array)
ax[0].set_title("Original Img")

ax[1].imshow(dark_rgb_array.astype(np.int64))
ax[1].set_title("Dark Version")

plt.show(block=True)