import pandas as pd
import numpy as np

days = pd.date_range(start = '2021-1-1', periods = 10)
df = pd.DataFrame(np.arange(1, 31).reshape(10, 3), 
                  columns = list('ABC'),
                  index = days
                 )
 
for row_index, row in df.iterrows():
    print(row_index.strftime('%d/%m/%Y'))
    print('Sum: '+str(row.sum()))
    print()