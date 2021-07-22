import numpy as np
A = np.array([[5]])
B = np.array([[1,2],[3,4]])
C = np.array([[-3,-8],[-5,-2]])
D = np.eye(2)
det_A = np.linalg.det(A).round()
det_B = np.linalg.det(B).round()
det_C = np.linalg.det(C).round()
det_D = np.linalg.det(D).round()

print('det(A):',det_A)
print('\ndet(B):', det_B)
print('\ndet(C):', det_C)
print('\ndet(D):', det_D)
