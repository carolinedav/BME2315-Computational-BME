# multiTrapezoidal.py

import numpy as np

def multiTrapezoidal(x,y):
    width = x[-1] - x[0]
    deltaX = width / len(x)
    sumValue = 0
    for i in range(len(x)):
        if i == 0 or i == len(x):
            sumValue += y[i]
        else: 
            sumValue += (2 * y[i])
    I = (deltaX / 2) * sumValue 
    return I

multiTrapezoidal(np.arange(0,np.pi/2+np.pi/8,np.pi/8),8+4*np.cos(np.arange(0,np.pi/2+np.pi/8,np.pi/8)))
