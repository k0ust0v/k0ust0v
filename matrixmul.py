import numpy as np
def matrixmul(matrix, matrix2):
    rows = len(matrix)
    cols = len(matrix2[0])
    res = [[0] * cols for _ in range(rows)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(len(matrix[0])):
                res[i][j] += matrix[i][k]*matrix2[k][j]

    return res

a = np.array([[1,2,3],[5,6,7],[7,9,8]])
b = np.array([[1,22,31],[25,46,57],[17,39,58]])
print(matrixmul(a,b))
print(a*b)
print(a.dot(b))