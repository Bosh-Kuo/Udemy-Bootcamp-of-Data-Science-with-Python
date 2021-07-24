import pandas as pd
 
data = {
    'Customers': ['Adrian', 'Carl', 'Eliza', 'Albert', 'Fred', 'Oswald', 'Grace', 'John'],
    'Age': [36, 39, 33, 32, 27, 35, 28, 18],
    'Rating': [6.2, 2.17, 6.56, 8.32, 9.15, 1.34, 0.57, 1.66] 
}
 
df = pd.DataFrame(data, index = range(1,9))

print(df.head())
print(df.head(n = 3))
print(df.tail())
print(df.tail(n = 2))