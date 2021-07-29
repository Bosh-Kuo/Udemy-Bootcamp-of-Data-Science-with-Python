import pandas as pd
import numpy as np

n = 10  
data = {
    'W': np.random.randint(1, 10, n),
    'Z': np.random.uniform(0, 10, n),
    'K': np.linspace(1, 50, n),
    'J': np.arange(n),
    'L': np.random.beta(1, 10, n),
    'M': np.random.exponential(1, n),
    'Y': np.random.randint(-50, -1, n)
}
 
df = pd.DataFrame(data, 
                  index = pd.date_range(start = '2020-12-1', periods = 10))
print(df)
for column in df:
    print(column)