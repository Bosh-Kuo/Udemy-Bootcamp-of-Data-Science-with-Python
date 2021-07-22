import numpy as np
A = np.diag([7, 8, 11, 2, 4, 5, 1, 3])
A_inverse = np.linalg.inv(A)

print('inverse A:\n', A_inverse)
