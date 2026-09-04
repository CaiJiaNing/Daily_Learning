import numpy as np

# Create a row vector
row_vector = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])

row_vector.ndim
row_vector.shape
row_vector.size

# Transpose the row vector to get a column vector
col_vector = row_vector.T

col_vector.ndim
col_vector.shape
col_vector.size