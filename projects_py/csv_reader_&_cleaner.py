import numpy as np

array_2d = np.array([[5, 1, 3, 2, 4, 6],
             [5, 8, 0, 3, 1, 2],
             [3, 10, 6, 21, 15, 1]])

print(array_2d[:, 1][array_2d[:, 3] < 10])
print(array_2d[array_2d > 7])
print(array_2d[0, :][array_2d[2, :] < 10])
print(np.where(array_2d > 7))
print(np.delete(array_2d, 0, axis=1))

array_1 = np.array([1, 4, 8])
array_3 = np.array([[8, 6, 4],
                    [1, 8, 0]])

array_1 = array_1.reshape((1, 3))
print(np.concatenate((array_1, array_3)))