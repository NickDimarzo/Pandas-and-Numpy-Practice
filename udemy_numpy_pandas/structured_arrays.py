import numpy as np

# Structured arrays
# Structured arrays are arrays that have different dtypes for each column

# can create your own datatype
data_type = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])

# creating an array using the defined datatype
students = np.array([('Alice', (90, 95)), ('Bob', (85, 88))], dtype=data_type)

print(students)
# Result
# [('Alice', [90., 95.]) ('Bob', [85., 88.])]

print(students.dtype)
# Result
# [('name', '<U16'), ('grades', '<f8', (2,))]

print(students['name'])
# Result
# ['Alice' 'Bob']

print(students['grades'])
# Result
# [[90. 95.]
#  [85. 88.]]
