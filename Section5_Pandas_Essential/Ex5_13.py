import pandas as pd

data = {
    'A': [i for i in range(1,21) if i%2==0],
    'B': [i**3 for i in range(1,21) if i%2!=0]
        }
 
df = pd.DataFrame(data, index = range(1, len(data['A'])+1))
print(df)