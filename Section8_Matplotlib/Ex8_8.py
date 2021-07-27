import matplotlib.pyplot as plt
import numpy as np
 
data = np.random.normal(loc = 100, scale = 0.5, size = 100)

plt.hist(x = data)
plt.title('Histogram')
plt.xlabel('Data')
plt.show()