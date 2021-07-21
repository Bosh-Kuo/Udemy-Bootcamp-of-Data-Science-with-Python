import numpy as np
K = np.array([
    [np.nan, 1, 10, 0],
    [np.nan,np.nan,np.nan,np.nan],
    [100, 50, np.nan, -25],
    [30, np.nan, np.nan, 130]])
 
print(np.isnan(K))
print(f'{np.isnan(K).sum()} missing data in K array.')