import pandas as pd
from numpy import random
mean = 10
standard_deviation = 3
data = random.normal(loc = mean, 
                     scale = standard_deviation, 
                     size = (20, 5))
df = pd.DataFrame(data, 
                  columns = list('ABCDE'), 
                  index = range(1, data.shape[0]+1))
print(data)
print('\n',df)
