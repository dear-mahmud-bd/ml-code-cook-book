import numpy as np

# Create row vector
vector = np.array([1, 2, 3, 4, 5, 6])
# Select third element of vector
print(vector[2]) # 3

# Create matrix
matrix = np.array( [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]] )
# Select second row, second column
print(matrix[1,1]) # 5

# Select all elements of a vector
print(vector[:])

# Select everything up to and including the third element
print(vector[:3])

# Select everything after the third element
print(vector[3:])

# Select the last element
print(vector[-1])

# Select the first two rows and all columns of a matrix
print(matrix[:2,:])

# Select all rows and the second column [:,col:2]
print(matrix[:,1:2])

