import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    m,n = len(a),len(a[0])
    size1 = m*n
    size2 = new_shape[0]*new_shape[1]
    if not a or  size1 != size2:
        return []
    list_1d = [item for row in a for item in row]
    reshape_matrix =[]
    cols = new_shape[1]
    for i in range (0,len(list_1d),cols):
        reshape_matrix.append(list_1d[i:i+cols])
    return reshape_matrix



