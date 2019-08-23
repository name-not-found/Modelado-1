import flags
import Graphics
from iterar import iterar
import dynamic_system
from sympy import *
import numpy as np

if __name__ == "__main__":
	eq0, a0, b0, n0, x0, N = flags.flags() 
	f, x0, N = dynamic_system.dynamic_system( eq0, a0, b0, n0, x0, N )

	orbita = iterar( x0, f , N)
	
	print(orbita)
	   
	Graphics.plotting( orbita, N )
