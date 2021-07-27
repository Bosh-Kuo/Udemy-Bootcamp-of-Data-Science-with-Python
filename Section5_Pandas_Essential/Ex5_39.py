import pandas as pd
import numpy as np
 
series = pd.Series(
    np.random.randint(100,150,4), 
    index = ['Year 1', 'Year 2', 'Year 3', 'Year 4'])
 
print(series)
series.drop(index = 'Year 1', inplace = True)
print(series)
series.drop(index = ['Year 2', 'Year 4'], inplace = True)
print(series)