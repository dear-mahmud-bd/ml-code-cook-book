import pandas as pd

# Create URL
url = r'P:\Cookbook_Code\02_Loading_Data\csv_file.csv'

# Load data
dataframe = pd.read_csv(url)

# Show two rows
dataframe.head(2)
# print(dataframe.head(2))
print(dataframe)

# Show dimensions
print(dataframe.shape)

# Show statistics
dataframe.describe()
print(dataframe.describe())
