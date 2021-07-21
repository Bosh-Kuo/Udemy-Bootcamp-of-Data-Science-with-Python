import numpy as np
array1 = np.arange(1,11)
array2 = np.linspace(1,50,10)
array3 = np.array(range(51))
array4 = np.logspace(1,10,5)
array5 = np.diag(range(5,31,5))
arrayList = [array1, array2, array3, array4, array5]
for i,array in enumerate(arrayList) :
    print(f'Sum of the elements of array {i}: ', array.sum() )