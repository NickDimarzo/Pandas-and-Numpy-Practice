import numpy as np

# Joing arrays

# creating new arrays to work with
a = np.array([[1,2],[3,4]])
print("First array:")
print(a)

b = np.array([[5,6],[7,8]])
print("Second Array:")
print(b)

# Note that these array are the same shape

# Concatenate, combing the arrays
# using the 0 axis results in a 4x2 array
# using the 1 axis results in a 2x4 array
print("")
print("Joining the two arrays along axis: 0")
c = np.concatenate((a,b))
print(c)
print("")
print("Joining the two arrays along axis: 1")
d = np.concatenate((a,b), axis=1)
print(d)