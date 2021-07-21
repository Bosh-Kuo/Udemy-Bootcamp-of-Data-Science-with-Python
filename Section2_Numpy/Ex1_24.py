import numpy as np
array1 = np.array([10, 20, 30, 40])
array2 = np.array([100, 30, 5, 1, 40, 100, 20, 130, 155,170])

print('a. array1: ',array1[[0,2,-1]])
print('a. array2: ',array2[[0,2,-1]])
print('b. array1: ',array1[::-1])
print('b. array2: ',array2[::-1])
