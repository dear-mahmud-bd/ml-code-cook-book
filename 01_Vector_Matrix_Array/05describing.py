import numpy as np

# Create matrix
matrix = np.array([ [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]
                ])

# View number of rows and columns
shape = matrix.shape # (3, 4)
print(shape)

# View number of elements (rows * columns)
sz = matrix.size # 12
print(sz)

# View number of dimensions
dimension = matrix.ndim #2
print(dimension,'D')
