# Section2 Numpy

## Ex1:
```
Inspection:
Shape: A tuple containing a number of elements (size) in each dimension of the array;  
Size: Total number of elements in the array;  
ndim: Number of dimensions (axes);
nbytes: Number of bytes used to store the data;
dtype: The data type of the elements in the array;
```

 ---
## Ex2:
```
Expected return:

inspect_array(np.array([1,2,3])) 
---
Shape : (3,)
Size:  3
Ndim:  1
Nbytes:  24
Dtype:  int64
Type:  <class 'numpy.ndarray'>
array([1, 2, 3])


inspect_array([1,2,3]) 
---
'The inserted object is not a NumPy array.'
```

---
## Ex3:
```
a. Use a list as an argument and obtain:
array([-1,  4,  7,  9])
b. Use the range() function and obtain:
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
c. Use a tuple as an argument and obtain:
array([10, 11, 12, 13, 14])
d. Use the range() function and obtain:
array([1990, 1995, 2000, 2005, 2010, 2015, 2020])
e. Use the range() function and obtain:
array([2020, 2010, 2000, 1990, 1980, 1970, 1960, 1950, 1940, 1930, 1920, 1910, 1900])
```


---
## Ex4:
```
Use np.one() function to create:  
a. array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])  
b. array([[1., 1., 1., 1.],  
       [1., 1., 1., 1.],  
       [1., 1., 1., 1.],  
       [1., 1., 1., 1.]])  
c. array([[1., 1.],  
       [1., 1.],  
       [1., 1.]])  
```

---
## Ex5:
```
Use np.one() function to create: 
a. array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])  
b. array([[0., 0.],  
      [0., 0.]])  
c. array([[0., 0., 0., 0., 0., 0.],  
       [0., 0., 0., 0., 0., 0.],  
       [0., 0., 0., 0., 0., 0.],  
       [0., 0., 0., 0., 0., 0.]])
```

---
## Ex6:
```
 Use np.arange() or np.array(range()) to create:
a.
array([[10],
       [15],
       [20],
       [25],
       [30],
       [35],
       [40],
       [45]])
b.
array([-50, -45, -40, -35, -30, -25, -20, -15, -10,  -5])
c.
array([[ 50,  52,  54,  56,  58,  60,  62,  64,  66,  68],
       [ 70,  72,  74,  76,  78,  80,  82,  84,  86,  88],
       [ 90,  92,  94,  96,  98, 100, 102, 104, 106, 108],
       [110, 112, 114, 116, 118, 120, 122, 124, 126, 128],
       [130, 132, 134, 136, 138, 140, 142, 144, 146, 148]])
```

---
## Ex7. 
```
Use the np.full(shape, fill_value, dtype) function to create the following arrays.
a. array([5., 5., 5., 5., 5., 5., 5., 5., 5., 5.])
b. array([[-5., -5., -5., -5.],
       [-5., -5., -5., -5.],
       [-5., -5., -5., -5.],
       [-5., -5., -5., -5.]])
c. array([[3, 3, 3],
       [3, 3, 3],
       [3, 3, 3]])
d. array([[50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
       [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
       [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
       [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
       [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
       [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
       [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
       [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
       [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
       [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]])
```

---
## Ex8:
```
Define the K array and check for missing data. Use the np.isnan() function.

array([[ nan,   1.,  10.,   0.],
       [ nan,  nan,  nan,  nan],
       [100.,  50.,  nan, -25.],
       [ 30.,  nan,  nan, 130.]])
```

---
## Ex9:
```
Use np.linspace() function to create:
array([ 1.,  6., 11., 16., 21.])
```

---
## Ex10:
```
Use np.logspace() function to create:
array([[1.00000000e+01],
       [3.59381366e+06],
       [1.29154967e+12],
       [4.64158883e+17],
       [1.66810054e+23],
       [5.99484250e+28],
       [2.15443469e+34],
       [7.74263683e+39],
       [2.78255940e+45],
       [1.00000000e+51]])
```

---
## Ex11:
```
Use np.diag() function to create:
array([[ 5,  0,  0,  0,  0,  0],
       [ 0, 10,  0,  0,  0,  0],
       [ 0,  0, 15,  0,  0,  0],
       [ 0,  0,  0, 20,  0,  0],
       [ 0,  0,  0,  0, 25,  0],
       [ 0,  0,  0,  0,  0, 30]])
```

---
## Ex12:
```
Use the np.eye() function to create:
array([[1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.]])
```

---
## Ex14:
```
Obtain the sum of each array with loop:

import numpy as np
array1 = np.arange(1,11)
array2 = np.linspace(1,50,10)
array3 = np.array(range(51))
array4 = np.logspace(1,10,5)
array5 = np.diag(range(5,31,5))

Sum of the elements of array 1:  55
Sum of the elements of array 2:  255.0
Sum of the elements of array 3:  1275
Sum of the elements of array 4:  10056552148.564463
Sum of the elements of array 5:  105
```

## Ex15:
```
From the matrix defined below, obtain:
a. total sum of the elements;
b. sum of the lines;
c. sum of columns;

import numpy as np
matrix = np.array(np.random.randint(1,100,15)).reshape(5,3)
```

---
## Ex16:
```
Obtain the maximum and minimum value of each array:

import numpy as np
array1 = np.array([-1, 10, 3, 4, 7, 27])
array2 = np.random.randint(-100,300,30)
array3 = np.random.randn(10)
array4 = np.array(range(50,10,-2))
```

---
## Ex17:
```
Create a function that receives a matrix as input and calculate:

a. Maximum value of the matrix;
b. Maximum value per column;
c. Maximum value per line;
d. Minimum value of the matrix;
e. Minimum value per column;
f. Minimum value per line.

Input:
matrix = np.random.randint(-1000,1000,50).reshape(10,5)
info_array(array)

Output:
Maximum value of the matrix:  987
Maximum value per column:  [959 987 597 748 719]
Maximum value per line:  [ 987  312  982  204  719  689  101  793 -460  959]
Minimum value of the matrix:  -969
Minimum value per column:  [-878 -966 -969 -884 -881]
Minimum value per line:  [  30 -878 -335 -863  -40 -289 -660
```

---
## Ex18:
```
Based on the array defined below, obtain your average, median, variance, and standard deviation.

import numpy as np
arr = np.random.normal(40,0.5,size = (300))
```

---
## Ex19:
```
Based on the arrays defined below, obtain the covariance matrix and the correlation matrix.

import numpy as np
x = np.random.rand(100)
y = np.random.uniform(size=100)
```

---
## Ex20:
```
Get the index of the maximum value of array A.
A = np.array([[11, 15, 33, 105],
              [1, 140, 45, 90],
              [67, 230, 78, 99]])
```

---
## Ex21:
```
Get the index of the minimum value of array B.
B = np.array([
    [73, 22, 20, 62,  3],
    [68, 84, 27, 59, 93],
    [48, 52,  4, 55, 50],
    [42, 23, 63, 67,  4],
    [44, 30, 41, 31, 29]])

```

---
## Ex22:
```
Write a function that receives a NumPy array and shows a set of descriptive statistics for this object on the screen.

Input:
array = np.array([-57, 101, 270, 130, 144])
info_array(array)

Output:
Max: 270
Min: -57
Mean: 117.6
Median: 130.0
Variance: 10967.439999999999
Standard deviation: 104.72554607162475
```

---
## Ex23:
```
Use the np.unique() function to obtain an array with the unique elements of the array below

A = np.array([
    [1, 3, 3, 4, 5],
    [4, 7, 11, 3, 5],
    [1, 11, 4, 4, 11]])
```

---
## Ex24:
```
Considering the arrays below:

import numpy as np
array1 = np.array([10, 20, 30, 40])
array2 = np.array([100, 30, 5, 1, 40, 100, 20, 130, 155,170])

Obtain:

a. The first, the third, and the last element of each array;
b. invert the array;
```

---
## Ex25:
```
Access the numbers 9 and 90 of the array below.

import numpy as np
ar = np.array([[-1, 33, 44, 9, 1],[11, 1, 0, 90, 44]])
```

---
## Ex26:
```
Access the number 5, 9, 3 and 21 from the array below
import numpy as np

ar = np.array([
    [[1, 1, 5, 1],
    [1, 1, 1, 9]],
    [[1, 3, 1, 1],
    [1, 1, 21, 1]]
                ])
```

---
## Ex27:
```
Based on the array below, obtain the slice from index 2 to index 6

import numpy as np
ar = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
```