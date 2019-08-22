#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# Simulando un sistema dinámico
import Graphics
import numpy as np
from sympy import *
import sys

file_flag = False
equation_flag = False
formulae_str = 'x'

#./dynamic -f archivo.txt
#./dynamic -e ecuacion
n = len(sys.argv)
for i in range(n):
		if "-f" in sys.argv[i]:
			file_flag = True
			filename = sys.argv[i+1]
		if '-e' in sys.argv[i]:
			equation_flag = True
			formulae_str = sys.argv[i+1]

if file_flag:
	with open("filename") as f:
		formulae = f.readlines()
		formulae_str = formulae[0]
		print("Using archive mode with" + formulae_str)
if equation_flag:
	print("Using equation mode with" + formulae_str)

x = Symbol('x')
y = sympify(formulae_str) #no evaluable
#yprime = y.diff(x)
f = lambdify(x,y,'numpy') #funcion evaluable

def iterar(its):
    L = []
    for it in its:
        l = []
        l.append(it)
        for _ in range(8):
            l.append( f(l[-1]) )
        L.append( np.array(l).reshape(-1,1) )
    return L

_init = [0.1, 1., 10.]
arrays = iterar(_init)

Graphics.plotting(arrays, _init)
