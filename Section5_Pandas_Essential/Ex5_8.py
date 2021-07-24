import pandas as pd
import matplotlib.pyplot as plt

years = list(range(1900, 2021, 10))
values = [i**3 for i in range(1, 14)]
series = pd.Series(data = values, index = years, name = 'Growth over time')[::-1]
series.plot(title = 'Growth Rate over Time');
plt.show()
