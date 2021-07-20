import numpy as np
from numpy.core.numeric import array_equal

def inspect_array(array):
    if type(array) == type(np.array([])):
        print('Shape: ', array.shape)
        print('Size: ', array.size)
        print('Ndim: ', array.ndim)
        print('Nbytes: ', array.nbytes)
        print('Dtype: ',  array.dtype)
        print('Type: ', type(array))
        print(array)
    
    else:
        print('The inserted object is not a NumPy array.')

inspect_array(np.array([1,2,3])) 
print("")
inspect_array([1,2,3]) 
