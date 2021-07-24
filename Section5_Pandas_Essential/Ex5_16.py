import pandas as pd

index = ['Product '+str(i) for i in range(1,9)]
data = {
    'Price': [20.3, 31.2, 44.7, 30.5, 19.8, 11.2, 15.7, 17.3],
    'Unit': [10, 33, 45, 51, 11, 8, 91, 8],
    'Total Cost': [100, 568.7, 205.2, 507.1, 250.12, 55.3, 1579, 130]}
df = pd.DataFrame(data, index)
print(df)