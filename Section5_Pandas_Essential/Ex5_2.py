import pandas as pd
 
data = ['k','w','z','y']
serie1 = pd.Series(data = data)
 
dic = {'a':10,'b':30,'c':15,'d':12}
serie2 = pd.Series(data = dic)
 
list1 = serie1.to_list()
list2 = serie2.to_list()
 
df1 = pd.DataFrame(serie1, columns = ['Letters'])
df2 = pd.DataFrame(serie2, columns = ['Values'])

print(serie1)
print(serie2)
print(df1)
print(df2)