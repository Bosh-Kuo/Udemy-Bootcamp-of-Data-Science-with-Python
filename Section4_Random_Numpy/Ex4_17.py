import pandas as pd
from numpy import random

n = 100  #number of observations
data = {
    'A': random.normal(size = n),
    'B': random.uniform(size = n),
    'C': random.binomial(n = 6, p = 0.6, size = n),
    'D': random.standard_exponential(size = n),
    'E': random.poisson(lam = 10, size = n),
    'F': random.normal(loc = 100, scale = 15, size = n),
    'G': random.randint(low = 50, high = 3000, size = n)}
df = pd.DataFrame(data)

print(df)