import pandas as pd
import  numpy as np

index = pd.date_range(start = '2020-1-1', end = '2020-1-6', freq = 'D')
data = {
    'A':[10, np.nan, 35, 47, 17, 13],
    'B':['A', np.nan, 'B', 'A', 'A', np.nan],
    'C':[139, np.nan, np.nan, 199, 111, 140]}
 
df = pd.DataFrame(data, index = index)
df.fillna(value = 0, inplace = True)
print(df)