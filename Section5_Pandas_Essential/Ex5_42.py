import pandas as pd
months = pd.date_range(start = '1-1-2021', periods = 12, freq = 'M')
print(months)