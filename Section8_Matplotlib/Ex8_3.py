import matplotlib.pyplot as plt
import numpy as np
 
y = np.random.normal(100, 5, 30)
 
plt.plot(y, color = 'red', ls = '--', marker = 'o')
plt.title('Title')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()