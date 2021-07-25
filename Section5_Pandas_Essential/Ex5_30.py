import pandas as pd
 
dic = {
    'A': ['a', 'b', 'c'],
    'B': ['f', 'g', 'w'],
    'C': ['z', 'k', 'm']}
df = pd.DataFrame(dic)
print(df.isin(['f', 'b', 'z']))