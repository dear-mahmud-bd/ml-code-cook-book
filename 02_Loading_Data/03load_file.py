import pandas as pd
import os


# Specify the CSV file path
file_path = r'P:\Cookbook_Code\02_Loading_Data\csv_file.csv'
# Check if the file exists
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    try:
        # Load dataset
        dataframe = pd.read_csv(file_path)

        # View first two rows
        print(dataframe.head(3),'\n')
        # View all rows
        print(dataframe,'\n\n')
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        print("No data. The file is empty.")
    except pd.errors.ParserError:
        print("Error parsing the file. Please check the file format.")
    except Exception as e:
        print(f"An error occurred: {e}")
        




# Specify the EXCEL file path
url = r'P:\Cookbook_Code\02_Loading_Data\excel_file.xlsx'
# Load data
try:
    # Load the Excel file with the correct keyword argument
    dataframe1 = pd.read_excel(url, sheet_name=0, header=0)

    # View the last two rows of the dataframe
    print(dataframe1.tail(4), '\n\n')
except FileNotFoundError:
    print("File not found. Please check the file path.")
except pd.errors.EmptyDataError:
    print("No data. The file is empty.")
except pd.errors.ParserError:
    print("Error parsing the file. Please check the file format.")
except Exception as e:
    print(f"An error occurred: {e}")
    
    



# Specify the json file path
file_path1 = r'P:\Cookbook_Code\02_Loading_Data\json_file.json'

# Load data into a DataFrame
try:
    # Load the JSON file
    dataframe = pd.read_json(file_path1,  orient='columns')
    
    # View the first two rows of the dataframe
    print(dataframe.tail(6), '\n\n')
except FileNotFoundError:
    print("File not found. Please check the file path.")
except pd.errors.EmptyDataError:
    print("No data. The file is empty.")
except pd.errors.ParserError:
    print("Error parsing the file. Please check the file format.")
except Exception as e:
    print(f"An error occurred: {e}")




# import sqlite3

# # Define the file path for the SQLite database
# db_path = r'P:\Cookbook_Code\02_Loading_Data\sample.db'

# # Connect to the SQLite database (this will create the file if it doesn't exist)
# conn = sqlite3.connect(db_path)
# cursor = conn.cursor()

# # Create a table named 'data' if it doesn't exist
# cursor.execute('''CREATE TABLE IF NOT EXISTS data (
#                     Id INTEGER PRIMARY KEY,
#                     FirstName TEXT,
#                     LastName TEXT,
#                     Gender TEXT,
#                     Country TEXT,
#                     Age INTEGER,
#                     DateOfBirth DATE
#                 )''')

# # Define the data to be inserted
# data_to_insert = [
#     (1, 'Dulce', 'Abril', 'Female', 'United States', 32, '2017-10-15'),
#     (2, 'Mara', 'Hashimoto', 'Female', 'Great Britain', 25, '2016-08-16'),
#     (3, 'Philip', 'Gent', 'Male', 'France', 36, '2015-05-21'),
#     (4, 'Kathleen', 'Hanner', 'Female', 'United States', 25, '2017-10-15'),
#     (5, 'Nereida', 'Magwood', 'Female', 'United States', 58, '2016-08-16'),
#     (6, 'Gaston', 'Brumm', 'Male', 'United States', 24, '2015-05-21'),
#     (7, 'Etta', 'Hurn', 'Female', 'Great Britain', 56, '2017-10-15'),
#     (8, 'Earlean', 'Melgar', 'Female', 'United States', 27, '2016-08-16'),
#     (9, 'Vincenza', 'Weiland', 'Female', 'United States', 40, '2015-05-21')
# ]

# # Insert the data into the 'data' table
# cursor.executemany('INSERT INTO data VALUES (?, ?, ?, ?, ?, ?, ?)', data_to_insert)

# # Commit the transaction and close the connection
# conn.commit()
# conn.close()

# print(f"Data has been inserted into SQLite database '{db_path}' successfully.")





from sqlalchemy import create_engine

# Define the file path for the SQLite database
db_path = r'P:\Cookbook_Code\02_Loading_Data\sample.db'

# Create a connection to the database
database_connection = create_engine(f'sqlite:///{db_path}')

# Load data from the 'data' table into a DataFrame
dataframe = pd.read_sql_query('SELECT * FROM data', database_connection)

# View the first five rows
print(dataframe.head(5))
