# interpolate.py
# Quan Dou walked me through the implementation of the code
import numpy as np
import matplotlib.pyplot as plt

def interpolateBspline(x,y,xi):
    n = len(x)
    h = x[1] - x[0]
    A = y
    
    m = len(xi)
    yi = np.zeros((m))
    
    
    for i in range(m):
        for j in range(n):
            xnew = xi[i] - x[j]
            yi[i] += A[j] * np.maximum(1-np.abs(xnew) / h, 0)
    return yi, A