
import numpy as np
import matplotlib.pyplot as plt

all_walks = []


for i in range(500) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        if np.random.rand() <= 0.005:
            step = 0
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

np_aw = np.array(all_walks)
np_aw_t = np.transpose(np_aw)

#fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# 2. Plot the original (np_aw) on the left
#ax[0].plot(np_aw)
#ax[0].set_title("Original")

# 3. Plot the transposed (np_aw_t) on the right
#ax[1].plot(np_aw_t)
#ax[1].set_title("Transposed")

ends = np_aw_t[:, -1]

success = np.sum(ends >= 60)
print(success)