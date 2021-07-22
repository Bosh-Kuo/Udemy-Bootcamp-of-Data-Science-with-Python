import numpy as np
Coef = np.array([[1,0,3],[2,-4,0],[3,-2,-5]])
Const = np.array([[-8],[-4],[26]])
sol = np.linalg.solve(Coef,Const)
print (sol)