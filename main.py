#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# Simulando un sistema dinámico
from Graphics import graphic
import numpy as np

def f(x):
    return x**2 + 1

def iterar(its):
    L = []
    for it in its:
        l = []
        l.append(it)
        for _ in range(6):
            l.append( f(l[-1]) )
        L.append( np.array(l).reshape(-1,1) )
    return L


_init = [0.1, 1., 10.]
arrays = iterar(_init)

graphic(arrays, _init)
