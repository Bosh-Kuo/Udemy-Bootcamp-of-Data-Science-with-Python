import pandas as pd

data = {
    'A': ['z', 'k' ,'m'],
    'B': ['j', 'n' , 'o'],
    'C': ['o', 'p', 'k'],
    'Z': ['i', 'j' ,'k'],
    'W': ['p', 'k', 'u']
}
df = pd.DataFrame(data, range(1,4))
print(df)
df.drop(labels = ['B', 'Z', 'W'], axis = 1, inplace = True)
print(df)