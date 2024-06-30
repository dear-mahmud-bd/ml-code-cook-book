import pandas as pd

# Create URL
url = r'P:\Cookbook_Code\02_Loading_Data\csv_file.csv'


# Load data
dataframe = pd.read_csv(url)


# Show top two rows where column 'Gender' is 'Female'
dataframe[dataframe['Gender'] == 'Female'].head(2)
# print(dataframe[dataframe['Gender'] == 'Female'].head(2))



# Filter rows
dataframe[(dataframe['Gender'] == 'Female') & (dataframe['Age'] >= 27)]
print(dataframe[(dataframe['Gender'] == 'Female') & (dataframe['Age'] <= 27)])
