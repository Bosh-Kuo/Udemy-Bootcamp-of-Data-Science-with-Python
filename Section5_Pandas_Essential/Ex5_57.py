import pandas as pd
import numpy as np

days = pd.date_range(start = '2020-1-1', periods = 10).to_numpy()
np.random.shuffle(days)
df = pd.DataFrame(
    data = np.random.normal(10,3.5,(10,3)),
    columns = list('ABC'),
    index = days)
print(df)

df = df.sort_index()  
print(df)