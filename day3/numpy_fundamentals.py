"""
Day 3: NumPy Fundamentals - Arrays, Indexing, Mathematical Operations
Internship Practice File
"""

import numpy as np

print("=" * 60)
print("DAY 3: NUMPY FUNDAMENTALS")
print("=" * 60)

# ============================================================
# 1. ARRAY CREATION
# ============================================================
print("\n--- 1. ARRAY CREATION ---")

# 1D array
arr_1d = np.array([1, 2, 3, 4, 5])
print(f"1D array: {arr_1d}")
print(f"Shape: {arr_1d.shape}, Dtype: {arr_1d.dtype}")

# 2D array (matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2D array:\n{arr_2d}")
print(f"Shape: {arr_2d.shape}")

# Special arrays
print(f"\nZeros (3x4):\n{np.zeros((3, 4))}")
print(f"\nOnes (2x3):\n{np.ones((2, 3))}")
print(f"\nIdentity (3x3):\n{np.eye(3)}")
print(f"\nArange (0 to 10, step 2): {np.arange(0, 10, 2)}")
print(f"Linspace (0 to 1, 5 points): {np.linspace(0, 1, 5)}")

# Random arrays
np.random.seed(42)
rand_arr = np.random.randint(1, 100, size=(3, 3))
print(f"\nRandom integers 1-100 (3x3):\n{rand_arr}")

rand_float = np.random.rand(2, 3)
print(f"Random floats [0,1) (2x3):\n{rand_float}")

# ============================================================
# 2. INDEXING & SLICING
# ============================================================
print("\n--- 2. INDEXING & SLICING ---")

arr = np.array([10, 20, 30, 40, 50, 60, 70])
print(f"Array: {arr}")
print(f"arr[0] = {arr[0]}")
print(f"arr[-1] = {arr[-1]}")
print(f"arr[1:5] = {arr[1:5]}")
print(f"arr[::2] = {arr[::2]}")
print(f"arr[::-1] = {arr[::-1]}")  # Reverse

# 2D indexing
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\nMatrix:\n{mat}")
print(f"mat[0, 1] = {mat[0, 1]}")  # Row 0, Col 1
print(f"mat[1, :] = {mat[1, :]}")  # Row 1
print(f"mat[:, 2] = {mat[:, 2]}")  # Col 2
print(f"mat[0:2, 1:3] = \n{mat[0:2, 1:3]}")  # Submatrix

# Boolean indexing
print(f"\nBoolean indexing:")
print(f"mat > 5:\n{mat > 5}")
print(f"mat[mat > 5] = {mat[mat > 5]}")

# Fancy indexing
indices = [0, 2]
print(f"mat[[0, 2], :] = \n{mat[[0, 2], :]}")  # Rows 0 and 2

# ============================================================
# 3. MATHEMATICAL OPERATIONS
# ============================================================
print("\n--- 3. MATHEMATICAL OPERATIONS ---")

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")  # Element-wise
print(f"a / b = {a / b}")
print(f"a ** 2 = {a ** 2}")
print(f"np.sqrt(a) = {np.sqrt(a)}")

# Aggregations
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\nMatrix:\n{data}")
print(f"Sum: {data.sum()}")
print(f"Mean: {data.mean()}")
print(f"Std: {data.std():.2f}")
print(f"Min: {data.min()}, Max: {data.max()}")
print(f"Sum axis=0 (col): {data.sum(axis=0)}")
print(f"Sum axis=1 (row): {data.sum(axis=1)}")

# Linear Algebra
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(f"\nMatrix A:\n{A}")
print(f"Matrix B:\n{B}")
print(f"A @ B (matrix multiply):\n{A @ B}")
print(f"np.dot(A, B):\n{np.dot(A, B)}")
print(f"A.T (transpose):\n{A.T}")

# ============================================================
# 4. BROADCASTING
# ============================================================
print("\n--- 4. BROADCASTING ---")

mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vec = np.array([10, 20, 30])

print(f"Matrix (3x3):\n{mat}")
print(f"Vector (3,): {vec}")
print(f"mat + vec (broadcast row-wise):\n{mat + vec}")

# Column vector broadcasting
col_vec = np.array([[10], [20], [30]])
print(f"\nColumn vector (3x1):\n{col_vec}")
print(f"mat + col_vec (broadcast col-wise):\n{mat + col_vec}")

# ============================================================
# 5. RESHAPING & MANIPULATION
# ============================================================
print("\n--- 5. RESHAPING & MANIPULATION ---")

arr = np.arange(12)
print(f"Original (12,): {arr}")

reshaped = arr.reshape(3, 4)
print(f"Reshaped (3,4):\n{reshaped}")

reshaped_2 = arr.reshape(2, 2, 3)
print(f"Reshaped (2,2,3):\n{reshaped_2}")

print(f"Flattened: {reshaped.flatten()}")
print(f"Transpose:\n{reshaped.T}")

# Stacking
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"\nvstack:\n{np.vstack([a, b])}")
print(f"hstack: {np.hstack([a, b])}")

# ============================================================
# 6. PRACTICE EXERCISES
# ============================================================
print("\n" + "=" * 60)
print("PRACTICE EXERCISES")
print("=" * 60)

# Exercise 1: 5x5 random matrix, row/col means
print("\n--- Exercise 1: 5x5 Random Matrix Stats ---")
np.random.seed(123)
mat5 = np.random.randint(1, 101, size=(5, 5))
print(f"Matrix:\n{mat5}")
print(f"Row means: {mat5.mean(axis=1)}")
print(f"Col means: {mat5.mean(axis=0)}")
print(f"Overall mean: {mat5.mean():.2f}")

# Exercise 2: Element-wise vs Matrix product
print("\n--- Exercise 2: Element-wise vs Matrix Product ---")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(f"A:\n{A}\nB:\n{B}")
print(f"Element-wise (A * B):\n{A * B}")
print(f"Matrix product (A @ B):\n{A @ B}")

# Exercise 3: Indexing - diagonal, upper triangle
print("\n--- Exercise 3: Diagonal & Upper Triangle ---")
M = np.arange(1, 10).reshape(3, 3)
print(f"Matrix:\n{M}")
print(f"Diagonal: {np.diag(M)}")
print(f"Upper triangle:\n{np.triu(M)}")
print(f"Lower triangle:\n{np.tril(M)}")

# Exercise 4: Broadcasting
print("\n--- Exercise 4: Broadcasting ---")
mat4 = np.ones((4, 3))
vec4 = np.array([1, 2, 3])
print(f"Matrix (4x3):\n{mat4}")
print(f"Vector (3,): {vec4}")
print(f"mat4 + vec4 (add to each row):\n{mat4 + vec4}")

# Exercise 5: Random data analysis
print("\n--- Exercise 5: Random Data Analysis ---")
data = np.random.randn(100, 5)  # 100 samples, 5 features
print(f"Shape: {data.shape}")
print(f"Mean per feature: {data.mean(axis=0)}")
print(f"Std per feature: {data.std(axis=0)}")
print(f"Correlation matrix:\n{np.corrcoef(data.T)}")

print("\n" + "=" * 60)
print("DAY 3 NUMPY FUNDAMENTALS - COMPLETE")
print("=" * 60)