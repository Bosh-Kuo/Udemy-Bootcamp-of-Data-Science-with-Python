import numpy as np
Coef = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
Const = np.array([2, 4, -1])
sol = np.linalg.solve(Coef,Const)
print(sol)