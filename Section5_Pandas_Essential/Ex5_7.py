import pandas as pd
import numpy as np
 
series_a = pd.Series(
    data = np.arange(1, 20, 2),
    index = [chr(65+i) for i in range(10)])
 
series_b = pd.Series(
    data = np.arange(5, 50, 5),
    index = [chr(70+i) for i in range(9)])

print(series_a,'\n')
print(series_a)