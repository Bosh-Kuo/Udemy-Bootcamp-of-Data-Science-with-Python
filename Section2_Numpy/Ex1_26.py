import numpy as np
ar = np.array([
    [[1, 1, 5, 1],
    [1, 1, 1, 9]],
    [[1, 3, 1, 1],
    [1, 1, 21, 1]]
                ])
print(ar[0][0][2])
print(ar[0][1][-1])
print(ar[1][0][1])
print(ar[1][1][-2])