import pandas as pd

date = pd.date_range(start = '2021-1-1', end = '2021-6-30', freq = '15D')
print(date)