#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# Simulando un sistema dinámico
from Graphics import graphic
import numpy as np
from sympy import *
#from readcol import fgetcols

#def f(x):
#    return x**2 + 1

x = Symbol('x')
#formulae = fgetcols('formulae.dat')
#formulae_str = (formulae[0])[0]

with open("formulae.dat") as f:
	formulae = f.readlines()
formulae_str = formulae[0]

y=sympify(formulae_str)
yprime = y.diff(x)
f = lambdify(x,y,"numpy")



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

graphic(arrays, _init)
