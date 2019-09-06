# import flags
import Graphics
from iterar import iterar
import dynamic_system
import rangos
import function_system

from sympy import *
import numpy as np
import argparse
import matplotlib.pyplot as plt
import random as rd

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Used for plotting equations')
	parser.add_argument('-f', help='filename', type = str) 
	parser.add_argument('-o', help='filename', type = str) 
	parser.add_argument('-e', help='equation', type = str)
	parser.add_argument('-r', help='random noise', type = str, default = 0)
	parser.add_argument('-histo', help='plotting histogram', type = int)
	parser.add_argument('-d', help='Evaluating dynamic system', type = str)
	parser.add_argument('-a', help='a term of ax^n+b', type = str, default = "1 2 1") #reciba lista de argumentos
	parser.add_argument('-n', help='a term of ax^n+b', type = str, default = "1 2 1") #reciba lista de argumentos
	parser.add_argument('-b', help='a term of ax^n+b', type = str, default = "0 .5 1") #reciba lista de argumentos
	parser.add_argument('-x0', help='initial condition', type = str, default = "1 2 1") #reciba lista de argumentos
	parser.add_argument('-N', help='number of iterations', type = int, default = 8) 
	
	args = parser.parse_args()
	dynamic_flag = False
	noise_flag = False
	histo_flag = False
	obs_flag = False
	obs_z = []
	obs_d = []
	obs_derr = []
	
	if args.f:
		with open(args.f) as f:
			formulae = f.readlines()
			formulae_str = formulae[0]
			print("Using archive mode with " + formulae_str)
			eq0 = formulae_str
	if args.o:
		obs_flag = True
		obs_filename = args.o
		with open(obs_filename) as f:
			data = f.readlines()
			for line in data:
				if line[0] != "#":
					z, d, d_err = line.split()
					obs_z.append(float(z))
					obs_d.append(float(d))
					obs_derr.append(float(d_err))
				
			#formulae_str = formulae[0]
			#print("Using archive mode with " + obs_filename)
			#eq0 = formulae_str
	if args.e:
		print("Using equation mode with " + args.e)
		eq0 = args.e 
	if args.d:
		dynamic_flag = True
		print("Evaluating dynamic system")
	if args.r:
		noise_flag = True
		noise = int(args.r)
		print("Inserting noise to functions: "+str(noise))
	if args.histo:
		histo_flag = True
		bind = args.histo
		print("Activated histogram: "+str(bind))
		
	#a*sin\(x\)+b
	a0, b0, n0, x0, N = rangos.rangos(args.a), rangos.rangos(args.b), rangos.rangos(args.n), rangos.rangos(args.x0), args.N
	#eq0, a0, b0, n0, x0, N = flags.flags() 
	
	fig, ax = plt.subplots()
	if histo_flag:
		fig_h, ax_h = plt.subplots(1)
	
	mitosis = 3.0
	time = np.arange(0, N*mitosis, mitosis) 
	
	for a in a0:
		for b in b0:
			for n in n0:
				if dynamic_flag:
					for z in x0:
						f = dynamic_system.dynamic_system( eq0, a, b, n)
						orbita = iterar( z, f , N)
				
						Graphics.plotting( eq0+'_a'+str(a)+'_b'+str(b)+'_n'+str(n)+'_x0'+str(z)+'_i'+str(N), fig, ax , orbita, N, eq0, time) 
				else:
					g = function_system.function_system( eq0, a, b, x0, n, noise_flag, noise)
					f = function_system.function_system( eq0, a, b, x0, n, False, noise)
					
					Graphics.plotting( eq0+'_a'+str(a)+'_b'+str(b)+'_n'+str(n)+'_x0'+str(x0)+'_i', fig, ax , g, N, eq0, x0) 
					Graphics.plotting( eq0+'_a'+str(a)+'_b'+str(b)+'_n'+str(n)+'_x0'+str(x0)+'_i', fig, ax , f, N, eq0, x0) 
					
					if histo_flag:
						Graphics.plot_histogram(fig_h, ax_h,f,g,bind)
					if obs_flag:
						Graphics.plot_observations(fig, ax, obs_z, obs_d, obs_derr)
						
	
	plt.savefig(eq0+'_a'+str(args.a)+'_b'+str(args.b)+'_n'+str(args.n)+'_x0'+str(args.x0)+'_i'+str(args.N)+".png")
	plt.show()
	
