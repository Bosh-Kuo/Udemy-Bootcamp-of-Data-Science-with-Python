import numpy as np
matrix = np.array(np.random.randint(1,100,15)).reshape(5,3)
print(matrix)
print('a. ', matrix.sum())
print('b. ', matrix.sum(axis=1))
print('c. ', matrix.sum(axis=0))