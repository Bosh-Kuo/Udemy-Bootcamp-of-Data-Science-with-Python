import numpy as np
import pandas as pd

np.random.seed(77)
data = np.random.randint(1,50,16).reshape((4,4))
df = pd.DataFrame(data, 
                columns = ['A', 'B', 'C', 'D'],
                index = ['i', 'j', 'k', 'w'])
print(df)                
df.drop(['k', 'j'], inplace = True)
print(df)
df.drop(['A', 'D'], axis = 1, inplace = True)
print(df)