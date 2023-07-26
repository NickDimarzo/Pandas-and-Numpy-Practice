import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Creating a new array to work with
print("new working series from a python array:")
arr = [0, 1, 2, 3, 4]
print(arr)
s1 = pd.Series(arr)
print(s1)

# slicing up to the 3 index
print("")
print("Slicing the array up to the third index:")
a = s1[:3]
print(a)

print("")
print("Slicing the array after the third index:")
b = s1[3:]
print(b)

# concatenating series
print("")
print(" Creating two new series")
c = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
s2 = pd.Series(c)
print(s2)

d = {'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
s3 = pd.Series(d)
print(s3)

print("")
print("Concat both series together:")
s4 = pd.concat([s2, s3])
print(s4)

# using drop to remove rows
print("")
print("Droping the f row:")
print(s4.drop('f'))


