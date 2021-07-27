import numpy as np
import matplotlib.pyplot as plt
 
x = np.arange(1,11)
y1 = x**2
y2 = x**3
y3 = x**4

plt.plot(y1, 'o', y2, '^', y3, 'bs')
plt.legend(['y1', 'y2','y3'], loc = 'upper left')
plt.title('Values', fontsize = 20)
plt.xlabel('X', fontsize = 15)
plt.ylabel('Y', fontsize = 15)
plt.grid(linestyle = '--', alpha = 0.8, color = 'red')
plt.show()