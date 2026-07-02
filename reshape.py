import random as rd

import numpy as np

matrix = np.array([i for i in range(1, 10)])
print(matrix)

matrix_reshaped = matrix.reshape((3, 3))
print(matrix_reshaped)
print(matrix_reshaped.reshape((1, 9)))

matrix_zero = np.zeros((5, 4))
print(matrix_zero)

matrix_zero_reshaped = matrix_zero.reshape((2, 10))
print(matrix_zero_reshaped)

matrix_random = np.random.randint(0, 100, size=(10, 10))
print(matrix_random)
matrix_random[matrix_random <= 17] = 0
print(matrix_random)

