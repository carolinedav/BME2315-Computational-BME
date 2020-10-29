# forwardDividedDifference.py

import numpy as np

def forwardDividedDifference(f,h):
    fp = []
    for i in range(len(f) - 1):
        fp.append((f[i + 1]-f[i]) / h)
    fp = np.asarray(fp)
    return fp

