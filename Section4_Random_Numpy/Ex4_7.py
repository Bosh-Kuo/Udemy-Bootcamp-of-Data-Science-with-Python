import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

data = random.uniform(size = 1000)
sns.displot(data, kind = 'kde')
sns.displot(data, kind = 'hist')
plt.show()
