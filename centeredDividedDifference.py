# centeredDividedDifference.py

import numpy as np

def centeredDividedDifference(f,h):
    fp = []
    for i in range(1, len(f) - 1):
        fp.append((f[i + 1]- f[i - 1]) / (2*h))
    fp = np.asarray(fp)
    return fp