def computeDet(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        det = 0
        
        for j in range(len(matrix[0])):
            det += (-1) * j * matrix[0][j] * computeDet(getMinor(matrix, j))
    print(det) 

def getMinor(matrix, col):
    minor = []

    for row in matrix[1:]:
        m = row[:col] + row[col+1:]
        minor.append(m)
    return minor


m = [[1,2,3],[2,4,6],[4,6,8]]
computeDet(m)
import numpy as np
print(np.linalg.det(m))