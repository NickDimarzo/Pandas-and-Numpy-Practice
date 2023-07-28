import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print(a[0])
# Result
# 1

print(a[1])
# Result
# 2

print(a[1:3])
# Result
# [2 3]

b = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
print(b[1:3])
# Result
# ['b' 'c']

print(b[1:6:2])
# Result
# ['b' 'd' 'f']

print(b[:2])
# Result
# ['a' 'b']

print(b[2:])
# Result
# ['c' 'd' 'e' 'f']

print(b)
# Result
# ['a' 'b' 'c' 'd' 'e' 'f']

c = b[0:3]
print(c)
# Result
# ['a' 'b' 'c']

c[0] = 'y'
print(c)
# Result
# ['y' 'b' 'c']

# Notice the 0 index of b has also changed
# This is because when we slice the array this is still referencing the original array
print(b)
# Result
# ['y' 'b' 'c' 'd' 'e' 'f']

# copy will create a copy of the original array and therefore any changes made to the copy will not affect the original
d = b[0:3].copy()
d[0] = 'a'
print(d)
# Result
# ['a' 'b' 'c']

print(b)
# Result
# ['y' 'b' 'c' 'd' 'e' 'f']

# check if two arrays are sharing the same memory slots
print(np.may_share_memory(b, d))
# Result
# False

print(np.may_share_memory(b, c))
# Result
# True

