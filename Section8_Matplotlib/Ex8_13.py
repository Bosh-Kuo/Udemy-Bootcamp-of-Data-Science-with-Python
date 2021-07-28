import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
np.random.seed(7)
data = np.random.randint(low = 100, high = [250, 300, 500, 1000], size = (12, 4))
index = pd.date_range(start = '2021-1-1', periods = 12, freq = 'M')
df = pd.DataFrame(data, columns = list('ABCD'), index = index.month_name())
print(df)

plt.figure(figsize = (15, 5))
plt.plot(df)
plt.title('Values over time')
plt.legend(df.columns, loc = 'best')
plt.grid(linestyle = '--', alpha = 0.5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.ylim(80, 1000)
plt.show()
