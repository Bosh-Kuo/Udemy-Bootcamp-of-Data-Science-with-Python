from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

n1, p1 = 6, 0.5
data1 = random.binomial(n1, p1, size = 100)
n2, p2 = 1, 0.8
data2 = random.binomial(n2, p2, size = 1000)

sns.displot(data1, kind = 'kde')
sns.displot(data2, kind = 'kde')
plt.show()
