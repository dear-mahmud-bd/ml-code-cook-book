import numpy as np

# Create matrix
matrix = np.array([ [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 8] ])

# Return maximum element
np.max(matrix)
# print(np.max(matrix))

# Return minimum element
np.min(matrix)
# print(np.min(matrix))

# Find maximum element in each column
np.max(matrix, axis=0)
# print(np.max(matrix, axis=0))

# Find maximum element in each row
np.max(matrix, axis=1)
# print(np.max(matrix, axis=1))

# Find the mean value in each column
np.mean(matrix, axis=0)
# print(np.mean(matrix, axis=0))


# Return mean
np.mean(matrix)
# print(np.mean(matrix))

# Return variance
np.var(matrix)
# print(np.var(matrix))

# Return standard deviation
np.std(matrix)
print(np.std(matrix))

