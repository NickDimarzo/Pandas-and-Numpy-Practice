import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Operations for DataFrame missing values
# Creating a DataFrame using a dictionary
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
data_frame_1 = pd.DataFrame(data, index=labels)
print("\nThis is a DataFrame created using a library and a python list for the indexes:")
print(data_frame_1)

# Creating a copy to work with
data_frame_2 = data_frame_1.copy()

# Filling the NaN values with a specified piece of data
print("\nThis is the copied DataFrame with the Nan values with 4: ")
print(data_frame_2.fillna(4))

# Filling the NaN values with a specified piece of data
print("\nThis is the copied DataFrame with the Nan values with the mean of the the 'Age' column: ")
mean_age = data_frame_2['age'].mean()
print(f"The mean age is: {mean_age}")
print(data_frame_2.fillna(mean_age))

data_frame_3 = data_frame_1.copy()

# Dropping the Nan values
print("\nAnother copy of the original table")
print(data_frame_3)
print("\nDropping any rows that contain NaN values:")
print(data_frame_3.dropna(how='any'))

