import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

n = 100
columns = ['Brand '+str(number) for number in range(1,5)]
date = pd.date_range(start = '2021-1-1', periods = n)
data = np.random.randint(low = 1, high = [100, 330, 45, 77], size = (n, 4))
df = pd.DataFrame(data,columns = columns, index = date)
print(df)
#configurando os dados para o plot
data = df.sum().sort_values(ascending = False)
print(data)
 
#plot
plt.bar(x = data.index, height = data)
plt.xlabel('Brands')
plt.ylabel('Values')
plt.title('Title')
plt.show()