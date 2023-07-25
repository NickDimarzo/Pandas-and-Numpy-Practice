import numpy as np

# practice example 1
# create a 6*6 two-dimensional array
# Let 1 and 0 be placed alternatively across the diagonals
z = np.zeros((6, 6), dtype=int)
print(z)

# remember the rows and columns count from 0,1,2,3,4,5 for 6 terms
# 1::2 -> start at row 1, then apply every second row after
# ::2 -> start at zero, then apply every second column after
# = 1 -> make these terms equal 1
# notice the first row or row 0 is not effected
# notice the third row or now 2 is not effected
# notice the fifth row or now 4 is not effected
print("first alter")
z[1::2, ::2] = 1
print(z)

# We will run the opposite to change the un effected rows
print("second alter")
z[::2, 1::2] = 1
print(z)


# practice example 2
# find the total number and locations of missing values in the array
# create a 10 * 10 array
x = np.random.rand(10, 10)

# makes 5 of the terms nan or null
x[np.random.randint(10, size=5), np.random.randint(10, size=5)] = np.nan

# original array
print(x)

# The total number of missing values :
print("")
print("Total number of missing values:", np.isnan(x).sum())

# can also find the index of each missing value
print("")
print("The indexes of the missing values are:")
print(np.argwhere(np.isnan(x)))

# another way to organize the index of the missing values
inds = np.where(np.isnan(x))
print("")
print("The x and y values of the indexes of the nan values in 2 arrays ")
print(inds)

# filling the nan values with 0 to clean the data, could also find the average and use this instead of 0
print("")
print("fill the nan values with 0 to clean the data")
x[inds] = 0  # could use average here instead
print(x)
