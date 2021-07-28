import pandas as pd
import numpy as np

days = pd.date_range(start = '2018-1-1', end = '2020-12-31')
n = days.shape[0]  #total observations
data = {
    'A': np.random.randint(low = 1, high = 1500, size = n),
    'B': np.random.normal(loc = 10, scale = 2, size = n),
    'C': np.random.uniform(low = 0, high = 1, size = n),
    'D': np.random.lognormal(mean = 4, sigma = 5, size = n),
    'E': np.random.standard_normal(size = n)}
df = pd.DataFrame(data, index = days)
print(df)