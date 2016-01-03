import os
import numpy as np
from scipy import signal
from scipy.integrate import odeint
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Define system
def sys(y, t):
	a = 0.2		# Prey growing rate without predators
	b = 0.02	# Prey dying rate due to predation (per predator)
	c = 0.4		# Predator dying rate without preys
	d = 0.02	# Predator growing rate per prey
	return np.array([ \
		y[0] * (a - b * y[1]), \
		- y[1] * (c - d * y[0]) \
	])

# Time range
n = 10000+1
t = np.linspace(0, 100, num=n)

# Initial condition
x0 = np.array([ 50.0, 10.0 ])

# Simulate system
y = odeint(sys, x0, t)

# Plot result
plt.plot(t, y[:,0], label='Prey count')
plt.plot(t, y[:,1], label='Predator count')
plt.grid()
plt.xlabel('Time')
plt.ylim(0, 60)
plt.legend(loc='upper left')
plt.savefig(os.path.splitext(__file__)[0] + '.pdf')
plt.show()
