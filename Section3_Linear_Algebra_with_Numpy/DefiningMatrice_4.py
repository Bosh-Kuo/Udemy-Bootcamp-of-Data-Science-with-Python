import numpy as np
A = np.triu(np.arange(1,10).reshape(3,3),k=0)
B = np.tril(np.arange(1,10).reshape(3,3),k=0)
C = np.triu(np.arange(100,125).reshape(5,5))

print(A)
print("\n",B)
print("\n",C)