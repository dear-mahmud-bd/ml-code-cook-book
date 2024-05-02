import numpy as np

# Set seed
np.random.seed(1)

# Generate three random floats between 0.0 and 1.0
np.random.random(3)
# print(np.random.random(3))

# Generate three random integers between 1 and 10
np.random.randint(0, 11, 3)
# print(np.random.randint(4, 39, 3))

# Draw three numbers from a normal distribution with mean 0.0 and standard deviation of 1.0
np.random.normal(0.0, 1.0, 3)
# print(np.random.normal(0.0, 6.0, 3))

# Draw three numbers from a logistic distribution with mean 0.0 and scale of 1.0
np.random.logistic(0.0, 1.0, 3)

# Draw three numbers greater than or equal to 1.0 and less than 2.0
np.random.uniform(1.0, 2.0, 3)
