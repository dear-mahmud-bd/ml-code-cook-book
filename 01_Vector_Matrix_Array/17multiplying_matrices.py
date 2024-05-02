import numpy as np

# Create matrix
matrix_a = np.array([[1, 1],
                     [1, 2]])

# Create matrix
matrix_b = np.array([[1, 3],
                     [1, 2]])

# Multiply two matrices
np.dot(matrix_a, matrix_b)
# print(np.dot(matrix_a, matrix_b))
# print(matrix_a @ matrix_b)

# Multiply two matrices element-wise
print(matrix_a * matrix_b)
