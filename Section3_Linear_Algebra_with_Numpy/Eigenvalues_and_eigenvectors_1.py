import numpy as np
A = np.array([[1,3],[-1,5]])
eigenvalues = np.linalg.eigvals(A)

print('Eigen values of A:', eigenvalues)