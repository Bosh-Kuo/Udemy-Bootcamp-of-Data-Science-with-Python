import pandas as pd
s = pd.Series([15, 31, 41, 47, 39, 10, 33, 13, 31, 33],
              index = pd.date_range(start = '2016', periods = 10, freq = 'Y'))
print('Year with highest revenue'.center(50, ' '))
print(s.idxmax().strftime('%Y'))
print('Year with lower revenue'.center(50, ' '))
print(s.idxmin().strftime('%Y'))