# interpolatePoly.py
import numpy as np
import matplotlib.pyplot as plt

def interpolatePoly(x,y,xi):
    n = len(x)
    Z = np.zeros((n,n))

    Z[:,0] = 1
    for value in range(1,len(Z)):
        Z[:,value] = x**value

    
    A = np.linalg.solve(Z, y)
    yi = np.zeros(len(xi))
                  
    for i in range(len(xi)):
        for j in range(0,n):  # adding the next part of eq. to a function
            yi[i] = yi[i] + A[j]*(xi[i]**j)
    print(yi)
    yi = np.squeeze(yi)
    
    return yi, A
