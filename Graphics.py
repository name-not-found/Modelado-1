import numpy as np
import matplotlib.pyplot as plt

def graphic (orbitas, condiciones):
	x = np.array(range(7)).reshape(-1,1)
	
	for a, c in zip(orbitas,condiciones):
		plt.plot(x, a, label="x = {}".format(c))
	
	plt.yscale('log')
	plt.legend()
	plt.show()
