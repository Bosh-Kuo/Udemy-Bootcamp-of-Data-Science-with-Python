import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
 
X, y = make_regression(n_samples = 100, n_features = 1, noise = 20)
 
#plot
plt.scatter(X, y, color = 'k', marker = '^', alpha = 0.3)
plt.title('Relationship between X and Y')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.grid(True, linestyle = '--', alpha = 0.5)
plt.savefig('fig7.jpeg')
plt.show()