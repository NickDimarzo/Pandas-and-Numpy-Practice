import pandas as pd
import numpy as np

# introduction 

# This is a panda call
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

# prints the dimensions for each object in the matrix
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
print(f"\nThis generate an array based on the range of 5 starting from 0 \n{f}")

# concatenating strings example
# strings
print("\nThis example shows how the matrix can concatinate strings")
print(np.char.add(['Hello ', 'Hi '],['abc', 'xyz']))

print("\nThis multiplies the string 'Hello' by 3")
print(np.char.multiply('Hello ', 3))

print("\nThis centers the word 'Hello' in a string with 20 characters, and fills the remaing space with '-' on each side of the word")
print(np.char.center('Hello', 20, fillchar='-'))

# multiple string examples
#capitilaize
print("")
print(np.char.capitalize('hello world'))

# Title, Capatailize all words in the string
print("")
print(np.char.capitalize('numpy is fun'))

# lower, makes all characters lowercase including strings in an array
print("")
print(np.char.lower(['HELLO', 'WORLD']))
print(np.char.lower('HELLO'))

# upper, opposite of lower
print("")
print(np.char.upper(['hello', 'world']))
print(np.char.upper('hello'))

# split, turns a string of words into an array of each individual word
print("")
print(np.char.split('are you coming to the party this evening?'))

# splitlines, does the same but splits when there is a new line marker 
print("")
print(np.char.splitlines('are you coming to the party this evening? \n because i am going'))

# strip, strips the letter 'a' from each string, only if they are leading or trailing letters
# notice the second a in 'anaita does not get striped
# more common for punctuation, like reading from csv file in c#
print("")
print(np.char.strip(['nina', 'admin', 'anaita'], 'a'))

# join, joins the using the selected characters
print("")
print(np.char.join(['.', '-'],['123', '456']))

# replace, replaces selected string with new string
# replaces the word 'is' with 'was'
print("")
print(np.char.replace('He is a good dancer', 'is', 'was'))