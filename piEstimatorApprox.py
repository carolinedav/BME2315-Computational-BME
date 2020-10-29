# piEstimatorApprox.py
# This code estimates pi using a series equation.


import numpy as np

def piEstimatorApprox(tol):
    values = []
    prevApproxList = [0]
    for k in range(1, 10000):
        values.append(((-1)**(k + 1)) / (2*k - 1))
        piEst = 4 * (np.sum(values))
        prevApproxList.append(piEst)
        prevApprox = prevApproxList[k - 1]
        approxPctRelError = ((piEst - abs(prevApprox)) / piEst ) * 100
        if abs(approxPctRelError) < tol:
            return piEst, approxPctRelError

print("Estimate of pi:",str(piEstimatorApprox(10)))
print("Estimate of pi:",str(piEstimatorApprox(0.1)))
