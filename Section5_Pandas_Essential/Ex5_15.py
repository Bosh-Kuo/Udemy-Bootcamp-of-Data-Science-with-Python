import numpy as np
import pandas as pd
from  matplotlib import pyplot as plt

array = np.random.normal(800, 30, size = (10, 4)).round(2)
years = range(2010, 2020)
columns = ['A', 'B', 'C' , 'D']
df = pd.DataFrame(data = array, index = years, columns = columns)
df.columns.name = 'Products'
df.index.name = 'Years'
print(df)

df.plot();
plt.show()