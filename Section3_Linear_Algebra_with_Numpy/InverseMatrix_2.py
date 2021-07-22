import numpy as np
A = np.array([[4,-1,2,-2],[3,-1,0,0],[2,3,1,0],[0,7,1,1]])
A_inverse = np.linalg.inv(A)

print('inverse A:\n', A_inverse)
