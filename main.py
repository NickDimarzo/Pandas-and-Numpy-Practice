import pandas as pd
import numpy as np

# This is a panada call
data = pd.Series([1, 2, 3])
print(f"This a panda table \n{data}")

# this is a numpy array
new_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"This is a new array \n{new_matrix}")
# prints the first index of the array [1, 2, 3]
print(f"This is the first index of the new array \n{new_matrix[0]}")

# this is a numpy range from 0 - 999
new_range = np.arange(1000)

# this array is 3 x 2
a = np.array([[1, 2], [3, 4], [5, 6]])
print(f"This is a new array \n{a}")

# prints the dimmensions for each object in the array
print(f"The dimensions of this arrary are {a.ndim}")

# prints the iitemsize of the array
print(f"The size of each item in this arrary is {a.itemsize}")

# prints the size of the array
print(f"The size of this arrary is {a.size}")

# prints the shape of the array
print(f"The shape of this arrary is {a.shape}")

# converts all the values in the array from int64 to float 64
b = np.array([[1, 2], [3, 4], [5, 6]], dtype = np.float64)
print(f"This is a new array with values that have been converted to float64 \n{b}")

