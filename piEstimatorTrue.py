# piEstimatorTrue.py
# This code estimates pi using a series equation.

import numpy as np

def piEstimatorTrue(tol):
    realPi = np.pi
    values = []
    for k in range(1, 10000):
        values.append(((-1)**(k + 1)) / (2*k - 1))
        piEst = 4 * (np.sum(values))
        truePctRelError = ((realPi - piEst) / realPi ) * 100
        if abs(truePctRelError) < tol:
            return piEst , truePctRelError
        

print("Estimate of pi:",str(piEstimatorTrue(10)))
print("Estimate of pi:",str(piEstimatorTrue(0.1)))
