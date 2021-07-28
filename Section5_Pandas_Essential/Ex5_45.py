import pandas as pd

quarters2021 = pd.date_range(start = '1-1-2021',periods = 4, freq = '3M' )
quarters2021 = pd.Series(quarters2021)
print(quarters2021)