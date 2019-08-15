#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# Simulando un sistema dinámico

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2 + 1

def iterar(its):
    L = []
    for it in its:
        l = []
        l.append(it)
        for _x in range(6):
            l.append( f(l[-1]) )
        L.append( np.array(l).reshape(-1,1) )
    return L


_init = [0.1, 1., 10.]
arrays = iterar(_init)
# print(len(arrays))

x = np.array(range(7)).reshape(-1,1)
for a, c in zip(arrays,_init):
    plt.plot(x, a, label="x = {}".format(c))
    #i += 1
plt.title("Sistema dinámico: x**2 +1")
plt.yscale('log')
plt.legend()
plt.show()

