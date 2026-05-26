
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# This is the background(white), a canvas
#Shape: (Height, Width, 3 Color Channels)
#np.full argument (how big is the array, what number do you want in every slot that represents the color, the type of data - np.uint8 for image)
logo = np.full((100, 100, 3), 255, dtype=np.uint8)

# This it define the Numpy word inside the logo with blue
dark_blue = [77, 121, 255] # Top/Main blue
light_blue = [0, 188, 212] # The side "cyan" blue

# This is to draw the main cube structure
# For the Dark Blue parts
logo[20:50, 20:50] = dark_blue # Top left block
logo[50:80, 50:80] = dark_blue # Bottom right block

# For the Light Blue parts
logo[20:50, 50:80] = light_blue # Top left block
logo[50:80, 20:50] = light_blue # Bottom right block

#This is how to save your file
np.save("logo.npy", logo)

#This is to call the file. 
with open("logo.npy", "rb") as f:
    logo_rgb_array = np.load(f)
    # A more efficient way is to just put logo_rgb_array = np.load("logo.npy")

# Examining RGB data by slicing
red_array = logo_rgb_array[:, :, 0]
green_array = logo_rgb_array[:, :, 1]
blue_array = logo_rgb_array[:, :, 2]
#print(red_array[1], green_array[1], blue_array[1])

# Updating RGB data using np.where/Changing the background to dark
dark_logo_array = np.where(logo_rgb_array == 255, 50, logo_rgb_array)

# To compare the two logos
# 1. We need a figure with 1 row and 2 columns
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# 2. Plot the original in the first pane
ax[0].imshow(logo_rgb_array)
ax[0].set_title("Original Logo")

# 3. Plot the dark version in the second pane
# .astype(np.uint8) ensures the colors stay correct
ax[1].imshow(dark_logo_array.astype(np.uint8))
ax[1].set_title("Dark Background")

plt.show(block=True)

# To save the edited logo
with open("dark_logo.npy", "wb") as f:
    np.save(f, dark_logo_array)
    # A better way to save is np.save("dark_logo.npy", dark_logo_array.astype(np.uint8))