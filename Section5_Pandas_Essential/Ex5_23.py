import pandas as pd
import numpy as np
 
data = np.random.uniform(low = 0, high = 5, size = (100,5))
df = pd.DataFrame(data, 
                  index = range(1,data.shape[0]+1), 
                  columns = list('ABCDE'))

print(df)
print() 
print(f'Number of lines: {df.shape[0]}')
print(f'Number of columns: {df.shape[1]}')
print(f'Shape: {df.shape}')
print(f'The total number of elements: {df.size}')
print(f'Number of dimensions: {df.ndim}')
print('-'*100)
print(f'Dataset information:')
print(df.info())
print('-'*100)
print(f'Dtype of each column: \n{df.dtypes}')
print('-'*100)
print(f'Descriptive statistics: \n{df.describe()}')