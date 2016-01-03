import os
import numpy as np
from scipy import signal
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Define system
def sys(y, t):
	sigma = 10.0
	beta = 8.0/3
	rho = 28.0
	return np.array([ \
		sigma * (y[1] - y[0]), \
		rho*y[0] - y[1] - y[0]*y[2], \
		y[0] * y[1] - beta * y[2] \
		])

# Time range
n = 10000+1
t = np.linspace(0, 100, num=n)

# Initial condition
x0 = np.array([ 1.0, 1.0, 1.0 ])

# Simulate system
y = odeint(sys, x0, t)

# Plot results
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(y[:,0], y[:,1], y[:,2])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.savefig(os.path.splitext(__file__)[0] + '.pdf')
plt.show()

