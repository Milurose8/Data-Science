#4. Given 3 Matrices A, B and C. Write a program to perform matrix multiplication of the 3 matrices.

import numpy as np

np.random.seed(42)

A = np.random.randint(0, 10, size=(2,2))

B = np.random.randint(0, 10, size=(2,3))

C = np.random.randint(0, 10, size=(3,3))

print("Matrix A:\n{}, shape={}\n".format(A, A.shape))

print("Matrix B:\n{}, shape={}\n".format(B, B.shape))

print("Matrix C:\n{}, shape={}\n".format(C, C.shape))