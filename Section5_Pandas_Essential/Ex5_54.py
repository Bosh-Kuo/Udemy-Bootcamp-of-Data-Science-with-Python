import pandas as pd
import numpy as np

data = {
    'A': np.arange(3),
    'B': [n**2 for n in range(1,4)],
    'C': [n for n in range(1,7) if n%2==0]}
 
index = pd.date_range(start = '2020-12-1', periods = 3, freq = 'M')
 
df = pd.DataFrame(data, index)
 
 
for column,values in df.iteritems():
    print(column)
    print(f'\tSum of values: {values.sum()}')
    print(f'\tMinimum value: {values.min()}')
    print(f'\tMaximum value: {values.max()}')
    print(f'\tArithmetic mean of values: {values.mean().round(2)}')
    print(f'\tStandard deviation: {values.std().round(2)}')
    print()