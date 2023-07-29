import numpy as np

# Exercise 1
# Create a Numpy array of lenth 10, filled with the values 0 - 9.
# Reshape the array into a 2D array of shape (5, 2)
# Compute the sum of all elements in the 2D array
array = np.arange(10)
array = array.reshape(5, 2)
print(array)
# Result
# [[0 1]
#  [2 3]
#  [4 5]
#  [6 7]
#  [8 9]]

array_sum = np.sum(array)
print(array_sum)
# Result
# 45

# Exercise 2
# Create a Numpy array of shape (5, 5) and fill it with random values between 0 and 1.
# Then, replace all elements that are less than 0.5 with 0 and all elements that are > or = to 0.5 with 1.
# Finally, compute the number of 1's in the resulting array.
array2 = np.random.rand(5, 5)
print(array2)
# Result
# [[0.22074957 0.46247678 0.47977942 0.82589636 0.79398312]
#  [0.93293295 0.06807651 0.61260344 0.93340413 0.97641254]
#  [0.15452081 0.60536505 0.8137838  0.6767093  0.98485673]
#  [0.00947887 0.62203719 0.21924228 0.58375372 0.71320699]
#  [0.67892184 0.32256353 0.46353762 0.01610917 0.71933364]]

array_replace = np.where(array2 < 0.5, 0, 1)
print(array_replace)
# Result
# [[0 0 0 1 1]
#  [1 0 1 1 1]
#  [0 1 1 1 1]
#  [0 1 0 1 1]
#  [1 0 0 0 1]]

ones_number = np.sum(array_replace)
print(ones_number)
# Result
# 15

# Exercise 3
# Generate a Numpy array of shape (10, 1) containing random numbers between 0 and 1.
# Then, normalize the values in the array so that they fall between -1 and 1.
# Finally, compute the mean and standard deviation of the normalized values.

array3 = np.random.rand(10, 1) * 2 - 1
array_mean = np.mean(array3)
array_std = np.std(array3)
print(array3)
print(array_mean)
print(array_std)
# Result
# [[-0.24874089]
#  [-0.35816011]
#  [ 0.77965226]
#  [ 0.39256998]
#  [ 0.95174798]
#  [ 0.55402058]
#  [ 0.62112934]
#  [ 0.52078797]
#  [-0.26160511]
#  [ 0.07913611]]
# 0.30305381095533157
# 0.44476824876946713


# Exercise 4
# Create a Numpy array of shape (20, 20) containing random numbers between -5 and 5.
# Then, find the indices of all elements in the array that are greater than 0 and less than 1, set those elements to 0.
# Finally, calculate the sum of all elements in the modified array that are negative.
array4 = np.random.rand(20, 20) * 10 - 5
array4[(array4 > 0) & (array4 < 1)] = 0
print(array4)
negative_sum = np.sum(array4[array4 < 0])
print(negative_sum)
# Result too large to add


# Exercise 5
# Given a Numpy array of shape (100, 100) containing random integers between -10 and 10,
# create a function that calculates the maximum sum of a sub-array of length k in the original array.
# The sub-array should be contiguous
# (i.e., elements should be taken from consecutive rows and columns in the original array).
array5 = np.random.randint(-10, 10, (100, 100))
def maximum_sum(array, k):

    # variable to store the shape of the array
    # Note here that these variable will be filled when the array is passed through the function
    n, m = array.shape

    # very small number, negative infinity
    max_sum = float('-inf')

    # defining the number of rows and columns in the sub array
    # note if only n - k:
    # were used the array would be 1 unit to small because the last number is not included in the range
    # range only runs up to the stop and does not include
    for i in range(n - k + 1):
        for j in range(m - k + 1):

            # The syntax used for indexing the NumPy array is array[start_row:end_row, start_column:end_column]
            # THIS LINE OF CODE IS CHECKING EVERY COMBINATION OF A K SIZED ARRAY IN THE ORIGINAL ARRAY
            # THIS WILL RETURN THE SUB-ARRAY THAT HAD THE HIGHEST VALUE
            sub_array = array[i:i + k, j:j + k]

            # sum of the current sub_array
            curr_sum = np.sum(sub_array)

            # assigns the higher values between max_sum and curr_sum to max_sum
            max_sum = max(max_sum, curr_sum)
    return max_sum


# Exercise 6
# Given a Numpy array of shape (m, n) containing random floating-point numbers,
# create a function that calculates the average of all the elements in each row,
# and returns a new Numpy array of shape (m, 1) containing the averages for each row.
# The function should use broadcasting to perform the calculation.
def row_average(array):

    # axis=1 refers to the rows of the array
    # keepdims=True keeps the shape of the array 2D or (m,1) instead of (m,) which would be just one row
    row_sums = np.sum(array, axis=1, keepdims=True)

    # If the shape is (4, 5)
    # row_counts = array.shape[1] will result in 5 because 5 is the 1 index.
    # row_counts = array.shape[0] will result in 4 because 4 is the 0 index.
    row_counts = array.shape[1]
    return row_sums/row_counts


