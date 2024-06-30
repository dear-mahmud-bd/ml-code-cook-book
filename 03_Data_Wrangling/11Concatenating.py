import pandas as pd

# Create DataFrame
data_a = {'id'   : ['1', '2', '3'],
          'first': ['Alex', 'Amy', 'Allen'],
          'last' : ['Anderson', 'Ackerman', 'Ali']}
dataframe_a = pd.DataFrame(data_a, columns = ['id', 'first', 'last'])

# Create DataFrame
data_b = {'id'   : ['4', '5', '6'],
          'first': ['Billy', 'Brian', 'Bran'],
          'last' : ['Bonder', 'Black', 'Balwner']}
dataframe_b = pd.DataFrame(data_b, columns = ['id', 'first', 'last'])

# Concatenate DataFrames by rows
pd.concat([dataframe_a, dataframe_b], axis=0)
print(pd.concat([dataframe_a, dataframe_b], axis=0))

# Concatenate DataFrames by columns
pd.concat([dataframe_a, dataframe_b], axis=1)
print(pd.concat([dataframe_a, dataframe_b], axis=1))


########### Merging DataFrames ###########
# Create DataFrame
employee_data = {'employee_id': ['1', '2', '3', '4'],
                 'name'       : ['Amy Jones', 'Allen Keys', 'Alice Bees', 'Tim Horton']}
dataframe_employees = pd.DataFrame(employee_data, columns = ['employee_id', 'name'])

# Create DataFrame
sales_data = {'employee_id': ['3', '4', '5', '6'], 
              'total_sales': [23456, 2512, 2345, 1455]}
dataframe_sales = pd.DataFrame(sales_data, columns = ['employee_id', 'total_sales'])

# Merge DataFrames
pd.merge(dataframe_employees, dataframe_sales, on='employee_id')
print(pd.merge(dataframe_employees, dataframe_sales, on='employee_id'))

# Merge DataFrames
pd.merge(dataframe_employees, dataframe_sales, on='employee_id', how='outer')
print(pd.merge(dataframe_employees, dataframe_sales, on='employee_id', how='outer'))

# Merge DataFrames => left and right joins
pd.merge(dataframe_employees, dataframe_sales, on='employee_id', how='left')
print(pd.merge(dataframe_employees, dataframe_sales, on='employee_id', how='right'))

# Merge DataFrames => can also specify the column name
pd.merge(dataframe_employees, dataframe_sales, left_on='employee_id', right_on='employee_id')
print(pd.merge(dataframe_employees, dataframe_sales, left_on='employee_id', right_on='employee_id'))
