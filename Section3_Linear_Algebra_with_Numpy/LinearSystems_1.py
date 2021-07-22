import numpy as np
Coef_a = np.array([[2,3],[1,-1]])
Const_a = np.array([[6],[8]])
solution_a = np.linalg.solve(Coef_a,Const_a)
 
Coef_b = np.array([[3,1],[1,2]])
Const_b = np.array([[9],[8]])
solution_b = np.linalg.solve(Coef_b,Const_b)

print(solution_a)
print(solution_b)