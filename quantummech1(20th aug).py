import matplotlib.pyplot as plt
import numpy as np 

def mat(n):
    matrix = [[0]*n for i in range(n)]
    for i in range(n):
        matrix[i][i] = -2
        if i + 1 < n: 
            matrix[i][i + 1] = 1
        if i - 1 >= 0: 
            matrix[i][i - 1] = 1
    return matrix 

A = mat(10)
eigenvalues, eigenvectors = np.linalg.eigh(A)
print(np.round(eigenvalues, 5))
print(np.round(eigenvectors, 5))

for k in range(5):
    plt.plot(eigenvectors[:, k])
    plt.show()