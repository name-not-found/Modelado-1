import numpy as np

def rangos(entrada):
	entrada=list(map(float,entrada.split(" ")))
	return np.arange(entrada[0], entrada[1], entrada[2]) 
