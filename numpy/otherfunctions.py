import numpy as np

# linspace function
a = np.linspace(1, 3, 10)
print("This displays 10 numbers that are between the 1 and 3 range and are evenly spaced")
print(a.round(1))

# sum and axis
b = np.array([(1, 2, 3), (3, 4, 5)])
print("This is a new array")
print(b)

print(" ")
print("summing the values using the axis 0:")
print(b.sum(axis=0))

print(" ")
print("summing the values using the axis 1:")
print(b.sum(axis=1))

# square root and standard deviation
print("")
print("This is the square root of all the different terms in the array")
print(np.sqrt(b))

print("")
print("This is the standard deviation of the array")
print(np.std(b))

# ravel function / similar to flatten
print("")
print("This is the ravel function")
print(b.ravel())

# log function, finds the log base 10 for each term in the array
print("")
print("This is the log function")
print(np.log10(b))

