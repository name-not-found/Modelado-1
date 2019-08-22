import initial_conditions
import Graphics
import numpy as np
from sympy import *
import sys

def iterar(its):
    L = []
    for it in its:
        l = []
        l.append(it)
        for _ in range(8):
            l.append( f(l[-1]) )
        L.append( np.array(l).reshape(-1,1) )
    return L

if __name__ == "__main__":
	x = Symbol('x')
	y = sympify( initial_conditions.flags() ) #no evaluable
	f = lambdify(x,y,'numpy') #funcion evaluable

	_init = [0.1, 1., 10.]
	arrays = iterar(_init)

	Graphics.plotting(arrays, _init)
