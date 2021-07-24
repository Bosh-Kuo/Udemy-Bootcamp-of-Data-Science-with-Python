import pandas as pd

scores = [7, 8 , 4.7, 10, 9.5, 6, 5, 7.7]
data = {
    'Name': ['Carl', 'Margaret', 'Maurice', 'Oscar', 'Peter', 'Oswald', 'Paul', 'Ronald'],
    'Score': scores,
    'Result': ['Yes' if score>=7 else 'No' for score in scores]
}
df = pd.DataFrame(data)
 
names = df.Name  
final_result = df['Result']  
print(df)
print()
print(df[['Name','Result']])  
print()
print(df.iloc[6:7])  
print()
print(df.iloc[3:6])  