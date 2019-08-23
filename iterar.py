import numpy as np
from sympy import *
import numpy as np


def iterar(its,f, N):
	l = []
	l.append(its)
	for _ in range( N-1 ):
		l.append( f(l[-1]) )
	
	return l
