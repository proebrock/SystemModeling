import os
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

m = 1.0 # Mass [kg]
k = 0.8 # Spring constant [N/m]
c = 0.0 # Damping constant [Ns/m]

# Time range
n = 500+1
t = np.linspace(0, 40, num=n)

# Input
def u(t):
	return np.sin(np.sqrt(k / m) * t)

# System
def sys(y,t):
	return np.array([ \
		y[1], \
		(- c * y[1] - k * y[0] + u(t)) / m \
	])

# Initial condition
x0 = np.array([ 0.0, 0.0 ])

# Simulate system
y = odeint(sys, x0, t)
y = y[:,0]

# Plot result
plt.plot(t, [ u(ti) for ti in t], '-k', label='Input $U(t)$')
plt.plot(t, y, '--b', label='Output $y(t)$')
plt.grid()
plt.xlabel('Time (s)')
plt.legend(loc='upper left')
plt.savefig(os.path.splitext(__file__)[0] + '.pdf')
plt.show()
