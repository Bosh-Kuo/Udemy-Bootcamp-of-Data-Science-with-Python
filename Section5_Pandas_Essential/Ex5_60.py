import pandas as pd

index = [1, 2, 3]
df1 = pd.DataFrame({
    'A': ['A0','A1','A2',],
    'B': ['B0', 'B1', 'B2'],
    'C': ['C0', 'C1', 'C2'],
    }, index = index)
 
df2 = pd.DataFrame({
    'A':['A3', 'A4', 'A5'],
    'B':['B3', 'B4', 'B5'],
    'C':['C3', 'C4', 'C5'],
    }, index = index)
 
df3 = pd.DataFrame({
    'A': ['A6', 'A7', 'A8'],
    'B': ['B6', 'B7', 'B8'],
    'C': ['C6', 'C7', 'C8']
    }, index = index)
 
data1 = df1.append(df2, ignore_index = True) 
print(data1)

data2 = df1.append([df2, df3])  
print(data2)