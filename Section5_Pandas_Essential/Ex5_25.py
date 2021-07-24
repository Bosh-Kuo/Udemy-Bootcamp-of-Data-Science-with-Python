import numpy as np
import pandas as pd

array = np.random.normal(10, 0.5, (10,10)).round(1)
col = [chr(64+i) for i in range(1, array.shape[1]+1)]  #column
index = [chr(64+i)+str(i) for i in range(1,array.shape[0]+1)]
df = pd.DataFrame(data = array, columns = col, index= index)
print(df)