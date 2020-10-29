# gauss.py
import numpy as np

def gauss(A,b):
    n = len(A)
    print(np.linalg.solve([[1, 0], [1, 1]], [[0], [0.049787]]))
    print(np.linalg.solve([[1, 0, 0], [1, 0.5, 0.25], [1, 1, 1]], [[0], [0.2231], [0.0498]]))
    # forward elimation
    for k in range(n-1):
        for i in range(k+1, n):
            factor = A[i,k] / A[k,k]
            for j in range(k, n):
                A[i,j] = A[i,j] - (factor * A[k,j])
            b[i] = b[i] - (factor * b[k])

    augMat = np.column_stack((A,b))
    x = np.empty((n,1), dtype=float)
    
    # back substitution
    for i in range(n-1, -1, -1):
        sumB = b[i]
        for j in range(i+1, n):
            sumB = sumB - (A[i,j] * x[j])
        x[i] = (sumB / A[i,i])
        
    return x, augMat
