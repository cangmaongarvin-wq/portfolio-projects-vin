
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

logo_rgb_array = np.load("mystery_image.npy")
                         
#flipped_logo = np.flip(logo_rgb_array, axis=0) # flips the whole array
#flipped_logo = np.flip(logo_rgb_array, axis=1) # You can axis arguments for specific area manipulation
transposed_logo = np.transpose(logo_rgb_array, axes=(1, 0, 2)) # flips the image 90 degress

fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].imshow(logo_rgb_array)
ax[0].set_title("Original Img")

ax[1].imshow(transposed_logo.astype(np.int64))
ax[1].set_title("Transposed Version")

plt.show(block=True)