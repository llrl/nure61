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


inv_A = np.linalg.inv(A)

X = inv_A.dot(B)

print(X)

print(A.dot(X))