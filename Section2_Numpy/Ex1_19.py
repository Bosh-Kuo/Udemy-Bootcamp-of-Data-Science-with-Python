import numpy as np
x = np.random.rand(100)
y = np.random.uniform(size=100)

print('Correlation matrix: ',np.corrcoef(x,y))
print('Covariance matrix: ',np.cov(x,y))