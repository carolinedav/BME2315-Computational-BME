# piEstimator.py
# This code estimates pi using a series equation.
# 7/21 code not giving the right answers
# to run: piEstimator(numIter)

import numpy as np

def piEstimator(numIter):
    realPi = np.pi
    n = numIter
    values = []
    for k in range(1, n):
        values.append(((-1)**(k + 1)) / (2*k - 1))
        
    piEst = 4 * (np.sum(values))

    truePctRelError = ((realPi - piEst) / realPi ) * 100
    return piEst, truePctRelError