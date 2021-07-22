import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[-1,3],[5,4]])
A_inverse = np.linalg.inv(A)
B_inverse = np.linalg.inv(B)

print('inverse A:\n', A_inverse)
print('inverse B:\n', B_inverse)