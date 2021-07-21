import numpy as np
A = np.array([[1,-3,2],[2,1,-3],[4,-3,-1]])
B = np.array([[1,4,1,0],[2,1,1,1],[1,-2,1,2]])
C = np.array([[2,1,-1,-2],[3,-2,-1,-1],[2,-5,-1,0]])
print(A.dot(B)==A.dot(C))