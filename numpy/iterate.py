import numpy as np

# Iterating over and array

# creating and array to work with
# note here we are specifying the start, end and step
# this is also a way to slice
a = np.arange(0, 45, 5)
print("This is the array:")
print(a)

a = a.reshape(3,3)
print("")
print("This is the reshaped array:")
print(a)

# using a for loop and nditer to iterate through each value
# notice the order is in standard C order
print("")
print("Iterating through the array using a for loop and nditer")
for x in np.nditer(a):
    print(x)

# Iteration order f-style
# notice it order the object by the columns not the rows
print("")
print("Iterating through the array using a for loop and nditer and specifying the order as F")
for x in np.nditer(a, order='F'):
    print(x)
