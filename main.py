import flags
import Graphics
from iterar import iterar
import dynamic_system
from sympy import *
import numpy as np
import argparse
import rangos
import matplotlib.pyplot as plt

#  plotear sobre la misma escala (misma figura)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Used for plotting equations')
	parser.add_argument('-f', help='filename', type = str) 
	parser.add_argument('-e', help='equation', type = str)
	parser.add_argument('-a', help='a term of ax^n+b', type = str, default = [1]) #reciba lista de argumentos
	parser.add_argument('-n', help='a term of ax^n+b', type = str, default = [1]) #reciba lista de argumentos
	parser.add_argument('-b', help='a term of ax^n+b', type = str, default = [0]) #reciba lista de argumentos
	parser.add_argument('-x0', help='initial condition', type = str, default = [1]) #reciba lista de argumentos
	parser.add_argument('-N', help='number of iterations', type = int, default = 8) 
	
	args = parser.parse_args()
    
	if args.f:
		with open(args.f) as f:
			formulae = f.readlines()
			formulae_str = formulae[0]
			print("Using archive mode with " + formulae_str)
			eq0 = formulae_str
	if args.e:
		print("Using equation mode with " + args.e)
		eq0 = args.e 
	
	a0, b0, n0, x0, N = rangos.rangos(args.a), rangos.rangos(args.b), rangos.rangos(args.n), rangos.rangos(args.x0), args.N
	print(type(x0))
	#eq0, a0, b0, n0, x0, N = flags.flags() 
	for z in x0:
		for a in a0:
			for b in b0:
				for n in n0:
					f, x0, N = dynamic_system.dynamic_system( eq0, a, b, n, z, N )

					orbita = iterar( x0, f , N)
					
					Graphics.plotting( orbita, N , eq0+'_a'+str(a)+'_b'+str(b)+'_n'+str(n)+'_x0'+str(z)+'_i'+str(N)+".png") 
