import pandas as pd

# Create URL
url = r'P:\Cookbook_Code\02_Loading_Data\csv_file.csv'

# Load data
dataframe = pd.read_csv(url)

# Delete column
dataframe.drop('Age', axis=1).head(2)
print(dataframe.drop('Age', axis=1).head(2))
    
# Drop columns
dataframe.drop(['Age', 'Gender'], axis=1).head(2)
print(dataframe.drop(['Age', 'Gender'], axis=1).head(2))

# Drop column index using dataframe.columns
dataframe.drop(dataframe.columns[1], axis=1).head(2)
print(dataframe.drop(dataframe.columns[2], axis=1).head(2))

# Delete rows, show first two rows of output
dataframe[dataframe['Gender'] != 'Female'].head(2)
print(dataframe[dataframe['Gender'] != 'Female'].head(2))

# Delete row, show first two rows of output
dataframe[dataframe['Last Name'] != 'Hashimoto'].head(2)
print(dataframe[dataframe['Last Name'] != 'Hashimoto'].head(2))
 
# Delete row, show first two rows of output
dataframe[dataframe.index != 0].head(2)
print(dataframe[dataframe.index != 0].head(2))
 
# Drop duplicates, show first two rows of output
dataframe.drop_duplicates().head(2)
print(dataframe.drop_duplicates().head(2))
 
# Show number of rows
print("Number Of Rows In The Original DataFrame:", len(dataframe))
print("Number Of Rows After Deduping:", len(dataframe.drop_duplicates()))
 

# Drop duplicates (first)
dataframe.drop_duplicates(subset=['Gender'])
print(dataframe.drop_duplicates(subset=['Gender']))

# Drop duplicates (last)
dataframe.drop_duplicates(subset=['Gender'], keep='last')
print(dataframe.drop_duplicates(subset=['Gender'], keep='last'))

