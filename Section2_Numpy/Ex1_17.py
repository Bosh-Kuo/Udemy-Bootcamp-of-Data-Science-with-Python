import  numpy as np
def info_array(array):
    print('Maximum value of the matrix: ', array.max())
    print('Maximum value per column: ', array.max(axis=0))
    print('Maximum value per line: ', array.max(axis=1))
    print('Maximum value of the matrix: ', array.min())
    print('Maximum value per column: ', array.min(axis=0))
    print('Maximum value per line: ', array.min(axis=1)) 
matrix = np.random.randint(-1000,1000,50).reshape(10,5)
info_array(matrix)