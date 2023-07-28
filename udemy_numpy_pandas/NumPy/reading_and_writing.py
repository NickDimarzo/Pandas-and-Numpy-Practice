import numpy
import numpy as np

# Reading and writing data files

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Writes the array to a .csv file named array.csv and seperates the data using a "," and fmt specifies 2 decimal places
np.savetxt("array.csv", arr, delimiter=",", fmt="%.2f")

# np.loadtxt
# np.genfromtxt
# both have different functions available

data = np.genfromtxt('array.csv', delimiter=",")
print(data)
# result
# [[1. 2. 3.]
#  [4. 5. 6.]]


