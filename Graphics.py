import numpy as np
import matplotlib.pyplot as plt

def plotting(orbita, N):
	x = np.array(range(N)).reshape(-1,1)
	
	plt.plot( np.array(range(N)), orbita)
	
	plt.yscale('log')
	plt.legend()
	plt.show()
