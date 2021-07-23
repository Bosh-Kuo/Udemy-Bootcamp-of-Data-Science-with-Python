from numpy import random

n = 100  #size
mean = 5
standard_deviation = 0.9
array = random.logistic(loc = mean, scale = standard_deviation , size = n)
print(array)