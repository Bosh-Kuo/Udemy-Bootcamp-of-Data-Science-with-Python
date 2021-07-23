from numpy import random
import numpy as np

array = random.rand(10,5)
mean = array.mean().round(2)
standard_deviation = array.std().round(2)
median = np.median(array).round(2)
print(f'Mean: {mean}')
print(f'Standard deviation: {standard_deviation}')
print(f'Median: {median}')