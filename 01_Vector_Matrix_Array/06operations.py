import numpy as np

# Create matrix
matrix = np.array([ [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
                  ])

# Create function that adds 100 to something
add_100 = lambda i: i + 100

# Create vectorized function
vectorized_add_100 = np.vectorize(add_100)

# Apply function to all elements in matrix
# vectorized_add_100(matrix)

print(vectorized_add_100(matrix))

# print(matrix+100)
