import matplotlib.pyplot as plt
import numpy as np
 
 
x = np.arange(-5.0, 5.0, 0.01)
y = np.sin(np.pi*x)
 
#plot
plt.plot(x,y)
plt.title('Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()