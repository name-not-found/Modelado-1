import numpy as np
import matplotlib.pyplot as plt

#def plotting(orbita, N, nombre):
def plotting(caption, fig, ax, y1):
	ax.plot(y1, label=caption)
	#ax.set(xlabel="i", ylabel="$x_i$", title=titulo)
	ax.grid()
	
	plt.yscale('log')
	
	"""
	x = np.array(range(N)).reshape(-1,1)
	plt.plot( np.array(range(N)), orbita)
	
	plt.yscale('log')
	plt.savefig(nombre)
	"""
	#plt.show()
