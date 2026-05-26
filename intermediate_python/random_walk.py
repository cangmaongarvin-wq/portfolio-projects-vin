
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

np.random.seed(123)

#Random Walk
random_walk = [0]
for x in range(100):
    step = random_walk[-1]
    dice = np.random.randint(1, 7)

    if dice <= 2:
        step = max(0, step - 1) # this make sure if argument nevers goes below zero
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)
    random_walk.append(step)


plt.plot(random_walk)
plt.show()