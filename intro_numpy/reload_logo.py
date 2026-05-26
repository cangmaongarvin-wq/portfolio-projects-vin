import numpy as np
import matplotlib.pyplot as plt

# 1. Load the array from your workspace
# No need for 'rb' or with open, np.load is smart enough!
reloaded_logo = np.load("dark_logo.npy")

# 2. Check that the data survived
print(f"Reloaded Shape: {reloaded_logo.shape}")
print(f"Data Type: {reloaded_logo.dtype}")

# 3. View the recreated logo
plt.imshow(reloaded_logo)
plt.title("Logo Loaded from .npy")
plt.show()