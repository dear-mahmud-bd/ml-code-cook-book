import pandas as pd
import collections

# Create URL
url = r'P:\Cookbook_Code\02_Loading_Data\csv_file.csv'

# Load data
dataframe = pd.read_csv(url)

# Rename column, show two rows
dataframe.rename(columns={'Date': 'Date of Birth'}).head(2)
# print(dataframe.rename(columns={'Date': 'DOB'}).head(2))


# Rename columns, show two rows
print(dataframe.rename(columns={'Date':'DOB', 'Gender':'Sex'}).head(2))


# Create dictionary
column_names = collections.defaultdict(str)

# Create keys
for name in dataframe.columns:
   column_names[name]

# Show dictionary
column_names
print(column_names)
 
 