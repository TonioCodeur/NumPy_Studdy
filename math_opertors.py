import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

np.random.seed(30)
matrix = np.random.randint(0, 10, size=(3, 3))
matrix2 = np.random.randint(0, 10, size=(3, 3))

print(2 * arr1)
print(arr1 * arr2)
print(arr1 + arr2)
print(arr1 @ arr2)  # This will raise an error because the shapes are not aligned for matrix multiplication
print(matrix @ matrix2)  # This will perform matrix multiplication

fusion_matrix = np.concatenate((matrix, matrix2), axis=1)
print(fusion_matrix)

print(np.sum(fusion_matrix))  # This will compute the sum of all elements in the matrix
print(fusion_matrix.prod())  # This will compute the product of all elements in the matrix