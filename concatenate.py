import numpy as np

zeros = np.zeros((2, 3))
ones = np.ones((2, 3))

matrix_concatenated_y = np.concatenate((zeros, ones), axis=0)
print(matrix_concatenated_y)

matrix_concatenated_x = np.concatenate((zeros, ones), axis=1)
print(matrix_concatenated_x)