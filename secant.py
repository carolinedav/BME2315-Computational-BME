# secant.py
import numpy as np

def secant(myfunc,xr_old,xr,reltol):
    error = abs(xr - xr_old)
    count = 0;
    while error > reltol:
        nX = myfunc(xr) * (xr - xr_old)
        dX = myfunc(xr) - myfunc(xr_old)
        xm = xr - (nX / dX)
        xr_old = xr
        xr = xm
        error = ( abs(xr - xr_old) / xr ) * 100
    return xr
        
