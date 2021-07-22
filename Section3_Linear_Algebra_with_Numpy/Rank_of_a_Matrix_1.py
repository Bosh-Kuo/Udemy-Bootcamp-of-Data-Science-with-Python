import numpy as np
A = np.array([[2,-1,3],[1,4,2],[1,-5,1],[4,16,8]])
A_rank = np.linalg.matrix_rank(A)

print('Rank of A:', A_rank)