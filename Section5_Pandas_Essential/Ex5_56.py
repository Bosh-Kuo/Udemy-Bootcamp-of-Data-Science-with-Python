import pandas as pd
import numpy as np

days = pd.date_range(start = '2021-1-1', periods = 10)
df = pd.DataFrame(np.arange(1, 31).reshape(10, 3), 
                  columns = list('ABC'),
                  index = days
                 )
print(df)
for row in df.itertuples():
    print(row)