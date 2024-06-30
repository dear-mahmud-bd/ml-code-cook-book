import pandas as pd

# Create URL
url = r'P:\Cookbook_Code\02_Loading_Data\csv_file.csv'

# Load data
dataframe = pd.read_csv(url)

# Select first row
dataframe.iloc[0]
# print(dataframe.iloc[0])


# Select three rows
dataframe.iloc[1:4]
# print(dataframe.iloc[1:4])

# Select three rows
dataframe.iloc[:4]
# print(dataframe.iloc[:4])


# Set index
dataframe = dataframe.set_index(dataframe['First Name'])
# Show row
name_to_find = 'Mara'
if name_to_find in dataframe.index:
    print(dataframe.loc[name_to_find])
else:
    print(f"'{name_to_find}' not found in the index.")

