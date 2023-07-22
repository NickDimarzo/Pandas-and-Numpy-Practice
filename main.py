import pandas as pd
import numpy as np

# This is a panada call
data = pd.Series([1, 2, 3])
print(f"This a panda table \n{data}")

# this is a numpy matrix
new_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"This is a new matrix \n{new_matrix}")

# prints the first index of the matrix [1, 2, 3]
print(f"This is the first index of the new matrix \n{new_matrix[0]}")

# this is a numpy range from 0 - 999
new_range = np.arange(1000)

# this matrix is 3 x 2
a = np.array([[1, 2], [3, 4], [5, 6]])
print(f"This is a new matrix \n{a}")

# prints the dimmensions for each object in the matrix
print(f"The dimensions of this matrix are {a.ndim}")

# prints the itemsize of the matrix
print(f"The size of each item in this matrix is {a.itemsize}")

# prints the size of the matrix
print(f"The size of this matrix is {a.size}")

# prints the shape of the matrix
print(f"The shape of this matrix is {a.shape}")

# converts all the values in the matrix from int64 to float 64
b = np.array([[1, 2], [3, 4], [5, 6]], dtype = np.float64)
print(f"This is a new matrix with values that have been converted to float64 \n{b}")
print("Notice the decimals that have been added to each value")
print(f"Notice the itemsize has also increased to {b.itemsize}")
print(f"The shape of the matrix remains the same at {b.shape}")

# converts all the values in the matrix to complex numbers
c = np.array([[1, 2], [3, 4], [5, 6]], dtype = np.complex128)
print(f"This version of the matrix has been converted to complex numbers \n{c}")

# create a matrix with all zeros 
d = np.zeros((3, 4))
print(f"This is a matrix with all zeros \n{d}")

# create a matrix with all ones 
e = np.ones((3, 4))
print(f"This is a matrix with all ones \n{e}")

# generate an array
# [0, 1, 2, 3, 4]
f = np.arange(5)
print(f"This generate an array based on the range of 5 starting from 0 \n{f}")



# concatination example
# strings
print("This example shows how the matrix can concatinate strings")
print(np.char.add(['Hello ', 'Hi '],['abc', 'xyz']))

print("This multiplies the string 'Hello' by 3")
print(np.char.multiply('Hello ', 3))

print("This centers the word 'Hello' in a string with 20 characters, and fills the remaing space with '-' on each side of the word")
print(np.char.center('Hello', 20, fillchar='-'))
