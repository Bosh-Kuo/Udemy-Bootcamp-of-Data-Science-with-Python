
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

data = random.normal(size = 3000)
sns.displot(data, kind = 'kde')
sns.displot(data, kind = 'hist')
plt.show()
