# bisection.py

import numpy as np

def bisection(myfunc, xl, xu, reltol):
     error = abs(xu-xl) 
     count = 0
     while error > reltol:
         xr = (xl + xu) / 2
         if myfunc(xr) == 0:
             return xr
         else: 
             if myfunc(xr) * myfunc(xl) > 0:
                 xl = xr
             else:
                xu = xr
             error = ( abs(xu-xl) / xr ) * 100
     return xr