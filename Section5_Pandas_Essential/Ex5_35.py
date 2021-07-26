import pandas as pd

data = {
    'Company A': {2018:90, 2019:76, 2020: 109},
    'Company B': {2018: 33, 2020: 13},
    'Company C': {2018:273, 2019: 33}}
 
df = pd.DataFrame(data)
df.columns.name = 'Revenues'
df.index.name = 'Year'

print(df)