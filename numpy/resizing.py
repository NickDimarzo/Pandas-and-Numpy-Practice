import numpy as np

# Creating an array to work with
a = np.array([[1, 2, 3], [4, 5, 6]])
print("This is the orginal array")
print(a)
print(f"The shape of this array is {a.shape}")

# resizing the array
b = np.resize(a, [3, 2])
print("")
print("This is the resized array")
print(b)
print(f"The shape of the new array is {b.shape}")

# resizing the array with larger dimensions, notice it uses repeats 1 2 3
c = np.resize(a, [3, 3])
print("")
print("This is the resized array")
print(c)
print(f"The shape of the new array is {c.shape}")