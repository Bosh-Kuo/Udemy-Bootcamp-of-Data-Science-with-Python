from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

n, p = 6, 0.5
data = random.binomial(n, p, size = 3000)


sns.displot(data, kind = 'hist')
plt.show()
