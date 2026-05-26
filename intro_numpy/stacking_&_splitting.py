
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from summarizing_data_numpy import monthly_sales
q1_sales, q2_sales, q3_sales, q4_sales = np.split(monthly_sales, 4)
quarterly_sales = np.stack([q1_sales, q2_sales, q3_sales, q4_sales])

rgb_array = np.load("mystery_image.npy")
red_array, green_array, blue_array = np.split(rgb_array, 3, axis=2)

emphasized_blue_array = np.where(blue_array > blue_array.mean(), 255, blue_array)

emphasized_blue_array_2D = emphasized_blue_array.reshape((401, 500))
red_array_2D = red_array.reshape((401, 500))
green_array_2D = green_array.reshape((401, 500))

emphasized_blue_monet = np.stack([red_array_2D, green_array_2D, emphasized_blue_array_2D], axis=2)
plt.imshow(emphasized_blue_monet)
plt.show(block=True)