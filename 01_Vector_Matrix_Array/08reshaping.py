import numpy as np

# Create 4x3 matrix
matrix = np.array([ [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                    [10, 11, 12] ])

# Reshape matrix into 2x6 matrix
matrix.reshape(2, 6)
# print(matrix.reshape(2, 6))

# print(matrix.size)


# One useful argument in reshape is -1, which effectively means “as many as needed,” so reshape(-1, 1) means one row and as many columns as needed
matrix.reshape(1, -1)
# print(matrix.reshape(1, -1))


# if we provide one integer, reshape will return a 1D array of that length
matrix.reshape(12)
print(matrix.reshape(12))
