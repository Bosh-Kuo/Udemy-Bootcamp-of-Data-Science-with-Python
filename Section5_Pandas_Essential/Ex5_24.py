import pandas as pd
import numpy
 
dic = {
    'A': [11, 3, 7, 99, 100, 130, 150],
    'B': [1.2, 0.5, 1.2, 3.2, 0.9, 1.7, 9.5],
    'C': ['A', 'Z', 'W', 'K', 'A', 'Z', 'Z'],
    'D': [True, False, True, False, True, False, True],    
    'E': ['A', 'A', 'B', 'B', 'A', 'A', 'B'],
    'F': [True, True, False, False, True, False, True],}
 
index = list(range(10, 71, 10))
df = pd.DataFrame(data = dic, index = index)
df[['C','E']] = df[['C', 'E']].astype('category')  #converting the data type of columns 'C' and 'E'
print(df)
print()
print('_'*100)
print(f'Dtype of each column: \n{df.dtypes}')
print('_'*100)
print(f"The columns from the category type: \n{df.select_dtypes('category')}")
print('_'*100)
print(f'The columns from the bool type: \n{df.select_dtypes(bool)}')
print('_'*100)
print(f'Numeric columns: \n{df.select_dtypes(include = [float, int])}')
print('_'*100)
print('Descriptive statistics')
print(df.describe(include = 'all').T)
print('_'*100)