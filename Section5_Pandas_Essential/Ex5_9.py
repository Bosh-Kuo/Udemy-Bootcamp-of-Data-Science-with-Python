import pandas as pd

s = pd.Series([1, 2, 3, 4, 5, 6], index = ['a', 'b', 'c', 'd', 'e', 'f'])
print(f'First element: {s[0]}')
print(f'Third element: {s[2]}')
print(f'First three elements: \n{s[:3]}')
print(f'Last three elements: \n{s[-3:]}')
print(f'Last element: {s[-1]}')