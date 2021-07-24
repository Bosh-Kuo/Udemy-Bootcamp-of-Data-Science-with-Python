import pandas as pd

names = ['Oswald', 'Richard', 'Victor', 'Walter', 'Ronald', 'Rebecca', 'Maurice', 'Margaret']
scores = [7, 8 , 4.7, 10, 9.5, 6, 5, 7.7]
results = ['Yes' if score>=7 else 'No' for score in scores]
data = {
    'Name': names,
    'Score': scores,
    'Result': results 
}
df = pd.DataFrame(data)
approved_students = df[df['Result'] == 'Yes']
 
print('Summary:')
print(df.describe())
print(f'Highest score: \n{df.max()}')
print()
print(f'Lowest score:\n{df.min()}')
print()
print(approved_students)