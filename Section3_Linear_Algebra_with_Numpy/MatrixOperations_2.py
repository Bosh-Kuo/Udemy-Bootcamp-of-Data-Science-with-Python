import numpy as np
A = np.array([[10,11],[5,1],[-2,4]])
B = np.array([[1,25],[3,4],[0,-10]])
C = np.array([[7,3],[6,1],[0,0]])
zero = np.zeros(shape=(3,2))
print((A+B)==(B+A))
print('\n', (A+(B+C))==((A+B)+C))
print('\n',A+zero==A)