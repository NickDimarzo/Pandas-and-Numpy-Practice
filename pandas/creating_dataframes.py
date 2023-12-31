import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Creating Dataframes
# Create multiple series to build a dataframe

# creating dates:
# Define time sequence as the index
print("Generating an array of 6 days starting from 'today':")
dates = pd.date_range('today', periods=6)
print(dates)

# creating a random numpy array with 6 rows and 4 columns
print("\nGenerating a numpy multi-dimensional array with 6 rows and 4 columns:")
num_arry = np.random.randn(6, 4)
print(num_arry)

# Note: the number of rows matches the number of indexes defined above

# Creating column names for the table:
columns = ['A', 'B', 'C', 'D']
print("\nThese are the names for the columns:")
print(columns)

# Creating a dataframe using the information we have created
print("\nThis is the pandas DataFrame created using the arrays above:")
data_frame_1 = pd.DataFrame(num_arry, index=dates, columns=columns)
print(data_frame_1)

# Creating a DataFrame using a dictionary
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
data_frame_2 = pd.DataFrame(data, index=labels)
print("\nThis is a DataFrame created using a library and a python list for the indexes:")
print(data_frame_2)

# See the datatypes of the DataFrame:
print(data_frame_2.dtypes)

# Using head to target the first entries of the DataFrame, can specify how many. default is the first 5
print(f"\nThis is the default head of the DataFrame: \n{data_frame_2.head()}")
print(f"This is the head of the DataFrame reduced to 3: \n{data_frame_2.head(3)}")
print(f"This is the head of the DataFrame increased to 7: \n{data_frame_2.head(7)}")

# you can also use head to create a new DataFrame by making a variable = the head of the original table:
data_frame_3 = data_frame_2.head(4)
print(f"\nThis is a new DataFrame created from the head of the first DataFrame:\n{data_frame_3}")

# This can also be repeated using the tail:
print(f"\nThis is the default tail of the DataFrame: \n{data_frame_2.tail()}")
print(f"This is the tail of the DataFrame reduced to 2: \n{data_frame_2.tail(2)}")
print(f"This is the tail of the DataFrame increased to 6: \n{data_frame_2.tail(6)}")

# you can also use tail to create a new DataFrame by making a variable = the tail of the original table:
data_frame_4 = data_frame_2.tail(3)
print(f"\nThis is a new DataFrame created from the tail of the first DataFrame:\n{data_frame_4}")

# Display the indexes
print("\nDisplaying the Indexs:")
print(data_frame_2.index)

# Display the Columns
print("\nDisplaying the Columns:")
print(data_frame_2.columns)

# Display the values
# Easy way to convert back to a numpy array
print("\nDisplaying the values:")
print(data_frame_2.values)

# See statistical data of a DataFrame
print("\nThis is the information produced with the describe command:")
print(data_frame_2.describe())

# Using Transpose to flip the DataFrame, switch the columns and rows
print(data_frame_2.T)

# Can sort the data
print("\nSorting the data within the DataFrame by the animal age:")
print(data_frame_2.sort_values(by='age'))

# Slicing the DataFrame:
print("\nSlicing the DataFrame between the 1 and 3 index: returns 2 rows")
print(data_frame_2[1:3])

# iloc is the same as slice
print("\nSlicing the DataFrame between the 1 and 3 index: returns 2 rows")
print(data_frame_2.iloc[1:3])

# Combining the sort and slice to return a different table
print("\nSorting and slicing will return new DataFrames:")
data_frame_5 = data_frame_2.sort_values(by='age')[1:3]
print(data_frame_5)

# Query the DataFrame by tag
print("\nQuery the DataFrame into 2 columns")
print(data_frame_2[['age', 'visits']])

# Can create a copy of the DataFrame
data_frame_6 = data_frame_2.copy()
print("\nCreating a copy of the DataFrame:")
print(data_frame_6)

# check if any values in the DataFrame are null:
print("\nChecking for NaN values:")
print(data_frame_6.isnull())

# Changing the actual data in the DataFrame:
# Note: This does not create a new DataFrame like the previous methods, This will change the selected DataFrame
print("\nChanging the 'age' value at index 'f' to '1.5'")
data_frame_6.loc['f', 'age'] = 1.5
print(data_frame_6)

# Finding the mean for values in the DataFrame in a selected column
print("\nThe mean value for the age column is:")
print(data_frame_6[['age']].mean())

# Can use all the series operations to calculate values for specified columns:
print(f"\nThe Sum of all values in the 'visits' column is: {data_frame_2['visits'].sum()}")
print(f"The min of all values in the 'visits' column is: {data_frame_2['visits'].min()}")
print(f"The max of all values in the 'visits' column is: {data_frame_2['visits'].max()}")
