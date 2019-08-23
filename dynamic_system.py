from sympy import *
import numpy as np

def dynamic_system(eq0, a0, b0, n0, x0, N):
	x, a, b, n = Symbol('x'), Symbol('a'), Symbol('b'), Symbol('n')
	y = sympify(eq0) #no evaluable
	y = y.subs(a, a0)
	y = y.subs(b, b0)
	y = y.subs(n, n0)
	
	f = lambdify(x,y,'numpy') #funcion evaluable
	
	return f, x0, N
