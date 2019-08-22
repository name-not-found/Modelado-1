import initial_conditions
import Graphics
import numpy as np
from sympy import *
import sys
from iterar import iterar

if __name__ == "__main__":
	x = Symbol('x')
	y = sympify( initial_conditions.flags() ) #no evaluable
	f = lambdify(x,y,'numpy') #funcion evaluable

	_init = [0.1, 1., 10.]
	arrays = iterar(_init,f)

	Graphics.plotting(arrays, _init)
