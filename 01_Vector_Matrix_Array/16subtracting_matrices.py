import numpy as np

# Create matrix
matrix_a = np.array([ [1, 1, 1],
                      [1, 1, 1],
                      [1, 1, 2] ])

# Create matrix
matrix_b = np.array([ [1, 3, 1],
                      [1, 3, 1],
                      [1, 3, 5] ])

# Add two matrices
np.add(matrix_a, matrix_b)
# print(np.add(matrix_a, matrix_b))
# print(matrix_a + matrix_b)

# Subtract two matrices
np.subtract(matrix_a, matrix_b)
# print(np.subtract(matrix_a, matrix_b))
print(matrix_a - matrix_b)
