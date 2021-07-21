import numpy as np
def info_array(array):
    print('Max: ', array.max())
    print('Min: ', array.min())
    print('Mean: ', array.mean())
    print('Median: ', np.median(array))
    print('Variance: ', array.var())
    print('Standard deviation:: ', array.std())
    
array = np.array([-57, 101, 270, 130, 144])
info_array(array)
