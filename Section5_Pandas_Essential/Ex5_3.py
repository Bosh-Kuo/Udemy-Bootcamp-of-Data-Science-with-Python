import pandas as pd
import numpy as np
 
array = np.arange(1, 50, 2)
serie = pd.Series(array, index = range(25,50), name = 'Serie', dtype = float)
print(serie)