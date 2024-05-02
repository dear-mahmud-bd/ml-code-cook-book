import numpy as np

# Create matrix
matrix = np.array([ [1, 2, 3],
                    [2, 4, 6],
                    [3, 8, 9] ])

# Return diagonal elements
matrix.diagonal()
# print(matrix.diagonal())

# Return diagonal one above the main diagonal
matrix.diagonal(offset=1)
# print(matrix.diagonal(offset=1))

# Return diagonal one below the main diagonal
matrix.diagonal(offset=-1)
# print(matrix.diagonal(offset=-1))

# Return diagonal and sum elements
sum(matrix.diagonal())
print(sum(matrix.diagonal()))
