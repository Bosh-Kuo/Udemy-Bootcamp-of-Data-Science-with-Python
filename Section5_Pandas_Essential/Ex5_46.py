import pandas as pd

hours = pd.date_range(start = '2030-12-31', periods = 24, freq ='H')
print(hours)