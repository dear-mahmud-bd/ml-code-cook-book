import pandas as pd

# Create URL
url = r'P:\Cookbook_Code\02_Loading_Data\csv_file.csv'

# Load data
dataframe = pd.read_csv(url)

# Group rows by the values of the column 'Sex', calculate mean of each group
# dataframe.groupby('Gender').mean()
# print(dataframe.groupby('Gender').mean())


############# there are one more data type that why need to seperate nummber type data #############
# Select only numeric columns
numeric_columns = dataframe.select_dtypes(include=['number'])
# Include the 'Gender' column for grouping
numeric_columns = numeric_columns.join(dataframe['Gender'])
# Group by 'Gender' and calculate the mean for numeric columns
result = numeric_columns.groupby('Gender').mean()

# Print the result
print(result)


# Group rows, count rows
dataframe.groupby('Gender')['First Name'].count()
print(dataframe.groupby('Gender')['First Name'].count())

# Group rows, calculate mean
print(dataframe.groupby(['Gender','Country'])['Age'].mean())



############ Grouping Rows by Time ############
import numpy as np

# Create date range
time_index = pd.date_range('01/06/2024', periods=100000, freq='45s')

# Create DataFrame
dataframe = pd.DataFrame(index=time_index)

# Create column of random values
dataframe['Sale_Amount'] = np.random.randint(1, 10, 100000)
# print(dataframe['Sale_Amount'].head(50))

# Group rows by week, calculate sum per week
dataframe.resample('W').sum()
print(dataframe.resample('W').sum())

# Show five rows
dataframe.head(5)
print(dataframe.head(5))

# Group by two weeks, calculate mean
dataframe.resample('2W').mean()
print(dataframe.resample('2W').mean())

# Group by month, count rows
dataframe.resample('ME').count()
print(dataframe.resample('ME').count())

# Group by month, count rows Month=ME 
dataframe.resample('ME', label='left').count()
print(dataframe.resample('ME', label='right').count())
