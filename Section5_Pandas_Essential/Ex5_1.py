import numpy as np
import pandas as pd
 

data = ['a', 'b', 'c', 'd']
array = np.arange(10,20,2)
serie1 = pd.Series(data)
serie2 = pd.Series(data,index=[10, 11, 12, 13])
serie3 = pd.Series(10,index=[0,1,2,3])
serie4 = pd.Series(array, index=range(1,6), dtype=float)

print(serie1)
print(serie2)
print(serie3)
print(serie4)