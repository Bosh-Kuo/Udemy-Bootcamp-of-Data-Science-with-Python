import numpy as np
Coef = np.array([[1, 1, 1, 1], [1, 1, 1,-1], [1, 1, -1, 1], [1, -1, 1, 1]])
Const = np.array([[0],[4],[-4],[2]])
sol = np.linalg.solve(Coef,Const)
print(sol)