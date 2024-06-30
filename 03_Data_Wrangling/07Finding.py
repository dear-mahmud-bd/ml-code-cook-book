import pandas as pd
import numpy as np

# Create URL
url = r'P:\Cookbook_Code\02_Loading_Data\csv_file.csv'

# Load data
dataframe = pd.read_csv(url)

# Calculate statistics
print('Maximum:', dataframe['Age'].max())
print('Minimum:', dataframe['Age'].min())
print('Mean:', dataframe['Age'].mean())
print('Sum:', dataframe['Age'].sum())
print('Count:', dataframe['Age'].count())

# Show counts
dataframe.count()
print(dataframe.count())

# Select unique values
dataframe['Gender'].unique()
print(dataframe['Gender'].unique())

# Show counts
dataframe['Gender'].value_counts()
print(dataframe['Gender'].value_counts())


# Show number of unique values
dataframe['Age'].nunique()
print(dataframe['Age'].nunique())



# Select missing values, show two rows
dataframe[dataframe['Age'].isnull()].head(2)
print(dataframe['Age'].isnull())
print(dataframe[dataframe['Age'].isnull()].head(2))

# Attempt to replace values with NaN
# dataframe['Gender'] = dataframe['Gender'].replace('Male', NaN)
# Replace values with NaN
dataframe['Gender'] = dataframe['Gender'].replace('Male', np.nan)
print(dataframe['Gender'])

# Load data, set missing values
dataframe = pd.read_csv(url, na_values=[np.nan, 'NONE', -999])
print(dataframe)

# Delete column
dataframe.drop('Age', axis=1).head(2)
print(dataframe.drop('Age', axis=1).head(2))







