import pandas as pd

# Create URL
url = r'P:\Cookbook_Code\02_Loading_Data\csv_file.csv'

# Load data
dataframe = pd.read_csv(url)

# Print first two names uppercased
for name in dataframe['First Name'][0:2]:
    print(name.upper())

# Applying a Function Over All Elements in a Column
# Create function
def uppercase(x):
    return x.upper()
# Apply function, show two rows
dataframe['First Name'].apply(uppercase)[0:2]
print(dataframe['First Name'].apply(uppercase)[0:2])

# Group rows, apply function to groups
dataframe.groupby('Gender').apply(lambda x: x.count())
print(dataframe.groupby('Gender').apply(lambda x: x.count()).reset_index(drop=True))


