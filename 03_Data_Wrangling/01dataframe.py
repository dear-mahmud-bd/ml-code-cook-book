import pandas as pd

# Create DataFrame
dataframe = pd.DataFrame()

# Add columns
dataframe['Name'] = ['Jacky Jackson', 'Steven Stevenson']
dataframe['Age'] = [38, 25]
dataframe['Driver'] = [True, False]

# Show DataFrame
dataframe
# print(dataframe)



# once we have created a DataFrame object, we can append new rows to the bottom 

# Create row
new_person = pd.DataFrame([['Molly Mooney', 40, True]], columns=['Name', 'Age', 'Driver'])
# Append row
dataframe = pd.concat([dataframe, new_person], ignore_index=True)

print(dataframe)
