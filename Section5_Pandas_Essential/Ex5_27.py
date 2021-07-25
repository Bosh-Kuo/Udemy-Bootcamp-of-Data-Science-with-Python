import pandas as pd

scores = [7, 8 , 4.7, 10, 9.5, 6, 5, 7.7]
data = {
    'Name': ['Carl', 'Margaret', 'Maurice', 'Oscar', 'Peter', 'Oswald', 'Paul', 'Ronald'],
    'Score': [7, 8 , 4.7, 10, 9.5, 6, 5, 7.7],
    'Result': ['Yes' if score>=7 else 'No' for score in scores]
}
df = pd.DataFrame(data)
print(df.Name[1:4].tolist())  
print(df.Name.loc[[0,2,7]].tolist())  
print(df.Name.iloc[0:1][0])  
print(df.Score.iloc[-1])  