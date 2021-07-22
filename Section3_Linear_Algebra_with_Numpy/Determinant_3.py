import numpy as np
A = np.array([[1, 2],[1, 0]])
B = np.array([[3, -1],[0, 1]])
 
det_A = np.linalg.det(A).round()
det_B = np.linalg.det(B).round()
print('det(A) + det(B): ', det_A+det_B)
 
det_sum = np.linalg.det(A+B).round()
print('det(A+B): ', det_sum)