import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Series operations

# creating arrays to work with
print("These are 2 new python arrays:")
arr1 = [0, 1, 2, 3, 4, 5, 7]
arr2 = [6, 7, 8, 9, 5]
print(arr1)
print(arr2)

print("\nThis is the second array as a pandas series: ")
s2 = pd.Series(arr2)
print(s2)

print("\nThis is the first array as a pandas series: ")
s1 = pd.Series(arr1)
print(s1)

# Adding one series to another, arithmetically
print("\nThis is the series after being added:")
print(s1.add(s2))
print("Notice the last 2 rows are nan because the first array had only 5 values")

# subtracting is the same process
print("\nThis is the series after being subtracted:")
print(s1.sub(s2))
print("Notice the last 2 rows are nan because the first array had only 5 values")

# multiplying
print("\nThis is the series after being multiplied:")
print(s1.mul(s2))
print("Notice the last 2 rows are nan because the first array had only 5 values")

# Dividing
print("\nThis is the series after being divided:")
print(s1.div(s2))
print("Notice the last 2 rows are nan because the first array had only 5 values")

# Finding the median of each series
print(f"\nThis is the median of the first series: {s1.median()}")
print(f"This is the median of the second series: {s2.median()}")

# Finding the min and max values:
print(f"\nThe max value of the first series is {s1.max()}")
print(f"The max value of the second series is {s2.max()}")
print(f"The min value of the first series is {s1.min()}")
print(f"The min value of the second series is {s1.min()}")

# Note when using these operations Nan or inf values are dropped for the calculations

