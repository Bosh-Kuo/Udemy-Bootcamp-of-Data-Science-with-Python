import pandas as pd
 
data = ['ITUB4', 'BBDC4', 'BBAS3', 'BPAC11', 'SANB11']
index = [1, 2, 3, 4, 5]
serie = pd.Series(data, index, name = 'Prices')
dic = serie.to_dict()
list_ = serie.to_list()
array = serie.to_numpy()
print(serie)
print(dic)
print(list_)
print(array)