import numpy as np
import matplotlib.pyplot as plt

#def plotting(orbita, N, nombre):
def plotting(caption, fig, ax, y1, N, titulo, time):
	ax.plot(time, y1, label=caption)
	ax.set(xlabel="hours", ylabel="$g$",  title=titulo)
	ax.grid()
	
	#plt.yscale('log')
	
	"""
	x = np.array(range(N)).reshape(-1,1)
	plt.plot( np.array(range(N)), orbita) 
	
	plt.yscale('log')
	plt.savefig(nombre)
	"""
	#plt.show()
