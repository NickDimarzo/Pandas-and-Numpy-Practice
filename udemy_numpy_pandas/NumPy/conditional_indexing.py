import numpy as np

# Conditional Indexing
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
bool_index = a > 5
print(bool_index)
# Result
# [False False False False False  True  True  True  True  True]

selected_elements = a[bool_index]
print(selected_elements)
# Result
# [ 6  7  8  9 10]

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
bool_index = b > 5
print(bool_index)
# Result
# [[False False False]
#  [False False  True]
#  [ True  True  True]

selected_elements2 = b[bool_index]
print(selected_elements2)
# Result
# [6 7 8 9]

# shortened
print(b[b > 5])
# Result
# [6 7 8 9]

# multiples of 3
print(b[b % 3 == 0])
# Result
# [3 6 9]

print(b[(b % 3 == 0) & (b > 6)])
# Result
# [9]

print(b[(b % 3 == 0) | (b > 6)])
# Result
# [3 6 7 8 9]

# Replace all the values that meet the conditions
b[(b % 3 == 0) | (b > 6)] = 0
print(b)
# Result
# [[1 2 0]
#  [4 5 0]
#  [0 0 0]]
