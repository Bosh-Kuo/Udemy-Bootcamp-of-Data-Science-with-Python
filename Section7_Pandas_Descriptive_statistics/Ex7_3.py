import pandas as pd

sales = [10, 38, 47, 9, 11, 9, 21, 49, 17, 29]
index = pd.date_range(start = '12/1/2020', periods = 10)
df = pd.DataFrame(sales, index , columns = ['Daily Sales'])
print(df)

day_max_value = df.idxmax()[0]  #day with the biggest sale
day_min_value = df.idxmin()[0]  #day with the lowest sale
 
print('Descriptive statistics'.center(100, ' '))
print(f'\tMean daily sales: {df.mean()[0]}')
print(f'\tStandard deviation: {df.std()[0].round(2)}')
print(f'\tVariance: {df.var()[0].round(2)}')
print(f'\tMode: {df.mode().iloc[0][0]}')
print(f'\tTotal quantity sold in the period: {df.sum()[0]}')
print(f'\tMaximum sales value: {df.max()[0]}')
print(f"\t\tDay: {day_max_value.strftime('%d/%m/%Y')}")
print(f'\tMinimum sales value: {df.min()[0]}')
print(f"\t\tDay: {day_min_value.strftime('%d/%m/%Y')}")