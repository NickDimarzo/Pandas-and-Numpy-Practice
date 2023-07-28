import numpy as np

# Logical Operations

a = np.array([True, False, True, False])
b = np.array([False, False, True, True])

print(np.logical_and(a, b))
print(a & b)
# Result
# [False False  True False]

print(np.logical_or(a, b))
print(a | b)
# Result
# [ True False  True True]

# returns true if either condition is true but not both true
print(np.logical_xor(a, b))
print(a ^ b)
# Result
# [ True False False  True]

# returns the logical inverse of the passed array
print(np.logical_not(a))
print(~a)
# Result
# [False  True False  True]

c = np.array([1, 2, 3, 4])
d = np.array([4, 3, 2, 1])
print(c < d)
# Result
# [ True  True False False]

print(c >= d)
# Result
# [False False  True  True]

print(c == d)
# Result
# [False False False False]

print(c != d)
# Result
# [ True  True  True  True]


