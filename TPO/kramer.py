import math

import numpy as np

A = np.array([
    [1.,3.,4.],
    [2.,3.,5.],
    [4.,5.,6.]
])

B = np.array([
    4., 3., 2.
])


assert np.linalg.det(A) != 0, 'Matrix method will not work'

def kramer(A, B):
    det_A = np.linalg.det(A)
    for i in range(len(A)):
        c = np.copy(A)
        c[:, i] = B
        yield np.linalg.det(c) / det_A


X = kramer(A, B)

print(X)

print(A.dot(X))


