import numpy as np

# Create matrix
matrix = np.array([ [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9] ])
# Transpose matrix
matrix.T
# print(matrix.T)


# Flattening a Matrix...
matrix.reshape(1, -1)
print(matrix.reshape(1, -1))
