import numpy as np

# Array Manipulation
# Changing shape

a = np.arange(9)
print("The original array:")
print(a)

# Reshape, change the actual shape of the array *note needs to be combatible with the orginal array*
b = a.reshape(3,3)
print("")
print("The modified array:")
print(b)

# Flatten, converts a multi-dimension array into a flat array
# *Flat array is an array that has only one row*
print("")
print("Flattened array:")
print(b.flatten())

# can use the order command with flatten to change the order of the flattend array
# The F value refers to FORTRAN, which will return the values in order of the coloum, not the rows
# The values can be 'F' 'C' 'A'
# default is the C value
print("")
print("This is a Flattened ordered array:")
print(b.flatten(order="F"))

# creating a new array to test with
# note here can create and reshape in the same line
c = np.arange(12).reshape(4,3)
print("")
print("This is a new array:")
print(c)

# THIS IS IMPORTANT
# transpose will swap or reverse the array columns, rows and values
print("")
print("This is a new array after it has been transposed:")
print(c.transpose())

# creating a new array to test with
d = np.arange(8).reshape(2,4)
print("")
print("This is a new array:")
print(d)

# More examples of reshaping
# reshapes the array into 2 elements, with 2 column and 2 rows each 
f = d.reshape(2,2,2)
print("")
print("The modified array:")
print(f)

# rollaxis, rolls the array in different ways, need to play around with this to learn the touch
print("")
print("The modified rolled array:")
print(np.rollaxis(f,2,1))
print("The modified rolled array:")
print(np.rollaxis(f,2))

#swapaxes, swaps the axis of the array in different ways, need to play around with this to learn the touch
print("")
print("The modified swaped array")
print(np.swapaxes(f,1,2))