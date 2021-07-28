import pandas as pd

september2021 = pd.date_range(start = '2021-9-1', periods = 29)
september2021 = pd.Series(september2021)
print(september2021)