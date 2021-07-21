import numpy as np
array = np.random.normal(40,0.5,size = (300))

print("Average: ", array.mean())
print("Median: ", np.median(array))
print("Standard deviation: ", array.std())
print("Variance: ", array.var())
