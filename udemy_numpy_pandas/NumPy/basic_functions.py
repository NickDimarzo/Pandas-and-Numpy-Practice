import numpy as np

# NumPy Basic Functions
arr = np.array([1, 2, 3, 4])
print(arr)
# Result
# [1 2 3 4]

print(type(arr))
# Result
# <class 'numpy.ndarray'>

zeros = np.zeros(5)
print(zeros)
# Result
# [0. 0. 0. 0. 0.]

ones = np.ones(10)
print(ones)
# Result
# [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

arr1 = np.arange(1, 10, 1)
print(arr1)
# Result
# [1 2 3 4 5 6 7 8 9]

arr2 = np.arange(0, 10, 2.2)
print(arr2)
# Result
# [0.  2.2 4.4 6.6 8.8]

arr3 = np.linspace(0, 10, 5)
print(arr3)
# Result
# [ 0.   2.5  5.   7.5 10. ]
# Divides the array into 5 equal intervals

print(np.shape(zeros))
# Result
# (5,)

arr4 = np.array([[1, 2], [3, 4]])
print(arr4)
# Result
# [[1 2]
#  [3 4]]

print(np.shape(arr4))
# Result
# (2, 2)

arr5 = np.transpose(arr4)
print(arr5)
# Result
# [[1 3]
#  [2 4]]

arr6 = np.reshape(arr4, (4, 1))
print(arr6)
# Result
# [[1]
#  [2]
#  [3]
#  [4]]

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.dot(a, b)
print(c)
# Result
# 32
# dot = the product of the arrays

d = np.sum(a)
print(d)
# Result
# 6

e = np.mean(b)
print(e)
# Result
# 5.0