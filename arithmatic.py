import numpy as np

# Numpy Arithmatic operations

# Creating new arrays to work with
a = np.arange(9).reshape(3,3)
b = np.array([10,10,10])

print("First array:")
print(a)
print("")
print("Second array:")
print(b)

# Add the arrays
print("")
print("Added array:")
print(np.add(a,b))

# Subtract the arrays
print("")
print("Subtracted array:")
print(np.subtract(a,b))

# multiply the arrays
print("")
print("Multiplied array:")
print(np.multiply(a,b))

# Divide the arrays
print("")
print("Divided array:")
print(np.divide(a,b))