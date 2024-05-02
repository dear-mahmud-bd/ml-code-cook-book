import numpy as np

# Create matrix
matrix = np.array([[2, 4],
                   [2, 5]])

# Calculate inverse of matrix
np.linalg.inv(matrix)
# print(np.linalg.inv(matrix))

# Multiply matrix and its inverse-> ( A.A^-1 = I )
print(matrix @ np.linalg.inv(matrix))
