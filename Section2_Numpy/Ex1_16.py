import numpy as np
array1 = np.array([-1, 10, 3, 4, 7, 27])
array2 = np.random.randint(-100,300,30)
array3 = np.random.randn(10)
array4 = np.array(range(50,10,-2))
arrayList = [array1, array2, array3, array4]

for i, array in enumerate(arrayList):
    print(array.max())
    print(array.min())
    print("")