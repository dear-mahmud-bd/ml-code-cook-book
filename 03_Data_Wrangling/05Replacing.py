import pandas as pd

# Create URL
url = r'P:\Cookbook_Code\02_Loading_Data\csv_file.csv'

# Load data
dataframe = pd.read_csv(url)

# Replace values, show two rows
dataframe['Gender'].replace("Female", "Woman").head(2)
# print(dataframe['Gender'].replace("Female", "Woman").head(2))

# Replace "female" and "male with "Woman" and "Man"
dataframe['Gender'].replace(["Female", "Male"], ["Woman", "Man"]).head(5)
# print(dataframe['Gender'].replace(["Female", "Male"], ["Woman", "Man"]).head(5))

# Replace values, show two rows
dataframe.replace("Female", "Woman").head(2)
print(dataframe.replace("Female", "Woman").head(5))


# Replace values, show two rows
# dataframe.replace(r"1st", "First", regex=True).head(2)
