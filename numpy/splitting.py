import numpy as np

# creating an array to work with
a = np.arange(9)
print("This is the original array:")
print(a)

# splits the array into 3 equal parts
print("")
print("This is the array after is has been split 3 by 3")
print(np.split(a, 3))

# splits the array into 3 parts at markers 4 and 5
print("")
print("This the array split by [4,5]")
print(np.split(a, [4, 5]))

# splits the array into 3 parts at markers 4 and 7
print("")
print("This is the array split by [4,7]")
print(np.split(a, [4, 7]))

# split the array into 4 parts at markers 4,5, and 7
print("")
print("This is the array split by [4,5,7]")
print(np.split(a, [4, 5, 7]))





