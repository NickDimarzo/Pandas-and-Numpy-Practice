import numpy as np

#Arithmatic operations

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a)
# Result
# [1 2 3]

print(b)
# Result
# [4 5 6]

c = a + b
print(c)
# Result
# [5 7 9]

d = a * b
print(d)
# Result
# [ 4 10 18]

d = a * b
print(d)
# Result
# [ 4 10 18]

e = a - b
print(e)
# Result
# [-3 -3 -3]

f = a / b
print(f)
# Result
# [0.25 0.4  0.5 ]

a1 = np.array([[1, 2], [3, 4]])
b1 = np.array([[5, 6], [7, 8]])

print(a1)
# Result
# [[1 2]
#  [3 4]]

print(b1)
# Result
# [[5 6]
#  [7 8]]

e1 = np.dot(a1, b1)
print(e1)
# Result
# [[19 22]
#  [43 50]]

# Converting the arrays into Matrix
c1 = np.mat(a1)
d1 = np.mat(b1)

# the product of 2 arrays
e2 = a1 * b1
print(e2)
# Result
# [[ 5 12]
#  [21 32]]

# the product of 2 matirx notice is the same result as the np.dot() function for arrays
e3 = c1 * d1
print(e3)
# Result
# [[19 22]
#  [43 50]]

