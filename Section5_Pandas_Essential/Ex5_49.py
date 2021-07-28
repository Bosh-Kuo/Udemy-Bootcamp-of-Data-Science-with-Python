import pandas as pd

date = pd.date_range(start = '2021-1-1', end = '2021-12-31', freq = '15D')
df = pd.DataFrame(date, columns = ['Date'])
df['Day of Year'] = date.dayofyear
df['Month of Year'] = date.month
print(df)