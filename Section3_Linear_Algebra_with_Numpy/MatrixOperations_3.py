import numpy as np
A = np.array([[1,2,3],[2,1,-1]])
B = np.array([[-2,0,1],[3,0,1]])
C = np.array([[-1],[2],[4]])
D = np.array([[2,-1]])

#1
print('A+B:',A+B)
#2
print('\nA.C:',A.dot(C))
#3
print('\nB.C:',B.dot(C))
#4
print('\nC.D:',C.dot(D))
#5
print('\nD.A:',D.dot(A))
#6
print('\nD.B:',D.dot(B))
#7
print('\n-A:',(-1)*(A))
#8
print('\n-D:',(-1)*D)
#9
print('\n2A+3B:',2*A+3*B)