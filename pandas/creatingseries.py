import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# checks pandas version
print(pd.__version__)

# Series create, manipulate, querry, and delete

# creating a series from a list
arr = [0, 1, 2, 3, 4]
print("This is the list before being converted to a series in pandas:")
print(arr)
print("")
print("This is the list after being converted to a series in pandas:")
s1 = pd.Series(arr)
print(s1)

# notice the left column is the index for each value, we can change the index using the order method
print("")
print("Changing the order of the index:")
order = [1, 2, 3, 4, 5]
s2 = pd.Series(arr, index=order)
print(s2)

# This is another example creating a random numpy array and setting the index to letters
print("")
print("Creating a random array with numpy then converting to a series with pandas")
print("Assigning the index to letters:")
a = np.random.randn(5)
index = ['a', 'b', 'c', 'd', 'e']
s3 = pd.Series(a, index=index)
print(s3)

# creating a series from a dictionary
print("")
print("Creating a series from a dictionary:")
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
s4 = pd.Series(d)
print(s4)

# modifying the index of the series
print("")
print("Modifying the first array indexes:")
print(s1)
print("After being modified:")
s1.index = ['A', 'B', 'C', 'D', 'E']
print(s1)
