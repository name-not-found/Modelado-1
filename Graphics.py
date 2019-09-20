import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
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

def plot_histogram(fig_h, ax_h,f,g,bind):
	data_histo=[]
	for i, (v1,v2) in enumerate(zip(f,g)):
		data_histo.append(v1-v2)
	ax_h.hist(data_histo,bins=bind)
	#axs_histo.hist(g, bins=bind)
	
def plot_observations(fig, ax, obs_z, obs_d, obs_derr):
	ax.errorbar(obs_z, obs_d,  yerr=obs_derr, fmt='o')
