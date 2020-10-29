# gold.py
# implements golden section search
import numpy as np

def gold(myfunc,xL,xU,reltol):
    gr = (np.sqrt(5) - 1) / 2
    error = np.abs(xU-xL) 
    d = gr * (xU - xL)
    x1 = xL + d
    x2 = xU - d
    f1 = myfunc(x1)
    f2 = myfunc(x2)
    if f1 > f2:
        xopt = x1
        fx = f1
    else:
        xopt = x2
        fx = f2
    while error > reltol:
        d = gr * d
        if f1 > f2:
            xL = x2
            x2 = x1
            x1 = xL + d
            f2 = f1
            f1 = myfunc(x1)
        else:
            xU = x1
            x1 = x2
            x2 = xU - d
            f1 = f2
            f2 = myfunc(x2)  
        if f1 > f2:
            xopt = x1
            fx = f1
        else: 
            xopt = x2
            fx = f2
        if xopt != 0:
            error = ((1-gr) * (abs(xU-xL) / xopt) ) * 100 
    xmax = xopt
    return xmax




