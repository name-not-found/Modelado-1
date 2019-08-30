import numpy as np
import matplotlib.pyplot as plt

#def plotting(orbita, N, nombre):
def plotting(caption, fig, ax, y1, N, titulo):
	ax.plot(np.array(range(0, N*3, 3)), y1, label=caption)
	ax.set(xlabel="hours", ylabel="$x_i$",  title=titulo)
	ax.grid()
	
	#plt.yscale('log')
	
	"""
	x = np.array(range(N)).reshape(-1,1)
	plt.plot( np.array(range(N)), orbita) 
	
	plt.yscale('log')
	plt.savefig(nombre)
	"""
	#plt.show()
