import numpy as np

# Create a row vector
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Convert the list to a NumPy array
a_ = np.array(a_list)

b_ = np.arange(1, 11)

dim = a_.ndim       # ndim() returns the number of dimensions of the array
shape = a_.shape    # shape() returns the dimensions of the array
size = a_.size      # size() returns the total number of elements in the array

print("a_:", a_)
print("Dimension of a_:", dim)
print("Shape of a_:", shape)
print("Size of a_:", size)