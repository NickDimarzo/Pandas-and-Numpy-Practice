import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# DataFrame File Operations
# Creating a DataFrame to work with
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
data_frame_1 = pd.DataFrame(data, index=labels)
print("\nThis is a DataFrame created using a library and a python list for the indexes:")
print(data_frame_1)

# Write the DataFrame to a CSV file with pandas
print("Writing the DataFrame to a CSV fie")
data_frame_1.to_csv('animal.csv')

# Read the CSV file to a DataFrame from a CSV file
print("Reading the CSV file to a DataFrame")
data_frame_2 = pd.read_csv('animal.csv')
print(data_frame_2)

# Write the DataFrame to an Excel sheet
# print("Writing the DataFrame to an Excel sheet")
# data_frame_1.to_excel('animal.xlsx', sheet_name='Sheet1')

# Read the DataFrame from an Excel sheet
# data_frame_3 = pd.read_excel('animal.xlsx', 'Sheet1', index_col=None, na_values=['NA'])

# MISSING MODULE 'openpyxl'







