import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
np.random.seed(7)
data = np.random.randint(low = 100, high = [250, 300, 500, 1000], size = (12, 4))
index = pd.date_range(start = '2021-1-1', periods = 12, freq = 'M')
df = pd.DataFrame(data, columns = list('ABCD'), index = index.month_name())
print(df)
frequency = df.sum().sort_values()
 
# a
plt.bar(x = frequency.index, height = frequency)
plt.title('Bar plot')
plt.show()
 
# b
plt.barh(y = frequency.index, width = frequency)
plt.title('Horizontal bar plot')
plt.show()
 
# c
explode = (0, 0.1, 0.1, 0.1)
plt.pie(frequency, shadow = True, autopct='%1.2f%%', explode = explode)
plt.legend(df.columns, loc = 'upper left')
plt.show()