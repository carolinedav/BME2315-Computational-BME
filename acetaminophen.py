# acetaminophen.py
import numpy as np
import matplotlib.pyplot as plt
from gold import gold

ED50 = 1
TD50 = 10
conc = np.logspace(-2,2,20)

def effect(conc): return conc/(ED50+conc)
def toxic(conc): return conc/(TD50+conc)
def net_effect(conc): return effect(conc)-2*toxic(conc)

xmaxE = gold(effect, -2, 20, 0.5)
print(xmaxE)
xmaxT = gold(toxic, -2, 20, 0.5)
print(xmaxT)
final = gold(net_effect, -2, 20, 0.5)
print(final)
f, axes = plt.subplots(3,1)
axes[0].semilogx(conc,effect(conc))
axes[0].set_ylabel('Pain relief')

axes[1].semilogx(conc,toxic(conc))
axes[1].set_ylabel('Liver damage')

axes[2].semilogx(conc,net_effect(conc))
axes[2].plot(final,net_effect(final),'o')
axes[2].set_ylabel('Net effect')
axes[2].set_xlabel('Acetaminophen dose (g)')

