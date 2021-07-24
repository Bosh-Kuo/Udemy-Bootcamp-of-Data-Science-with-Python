import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.random(50).reshape((10,5)),
                index = range(1,11),
                columns = list('ABCDE'))
print(df)