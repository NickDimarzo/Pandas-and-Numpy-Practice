import numpy as np

# Creating a new array to work with
a = np.arange(20)

# slicing the array shrinks or cuts peices off of the array reducing the size see examples
print("This is the array:")
print(a)
print("")
print("This is the array after it has been sliced from the 4th index and onwwards")
print(a[4:])
print("")
print("This is the array after it has been sliced from the begining until the 4th index")
print(a[:4])
print("")
print("Can return a single index")
print(a[5])

#can also use the splice commaned to specify the start, end, and step
print("")
print("This is a sliced array:")
s1 = slice(2,9,2)
print(a[s1])

print("")
print("This is a sliced array:")
s2 = slice(2,19,3)
print(a[s2])



