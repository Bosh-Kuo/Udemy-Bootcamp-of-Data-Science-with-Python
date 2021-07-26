import matplotlib.pyplot as plt
import numpy as np
 
x = np.arange(20)
y = np.random.randint(1,100, 20)
 
plt.plot(x,y, marker = 'o', color = 'black')
plt.title('Title')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()