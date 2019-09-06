from sympy import *
import numpy as np
import random

def function_system(eq0, a0, b0, x0, n0, noise_flag, noise):
	x, a, b, n = Symbol('x'), Symbol('a'), Symbol('b'), Symbol('n')
	y = sympify(eq0) #no evaluable
	y = y.subs(a, a0)
	y = y.subs(b, b0)
	y = y.subs(n, n0)
	
	f = lambdify(x,y,'numpy') #funcion evaluable
	
	y1 = f(x0)
	
	if noise_flag:
		for i,value in enumerate(y1):
			y1[i] = value + (random.random()-0.5)*2.0*noise
	
	return y1
