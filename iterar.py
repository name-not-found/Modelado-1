import numpy as np


def iterar(its,f):
    L = []
    for it in its:
        l = []
        l.append(it)
        for _ in range(8):
            l.append( f(l[-1]) )
        L.append( np.array(l).reshape(-1,1) )
    return L
