import os
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Define system
m = 1.0 # Mass [kg]
k = 0.8 # Spring constant [N/m]
c = 0.0 # Damping constant [Ns/m]
omega0sq = k / m
two_zeta_omega0 = c / m
beta = 1 / m
def u(t):
	return np.sin(np.sqrt(omega0sq)*t)
def sys(y,t):
	return np.array([ \
		y[1], \
		- two_zeta_omega0 * y[1] - omega0sq * y[0] + beta * u(t) \
	])

# Time range
n = 500+1
t = np.linspace(0, 40, num=n)

# Initial condition
x0 = np.array([ 0.0, 0.0 ])

# Simulate system
y = odeint(sys, x0, t)

# Plot result
plt.plot(t, [ u(ti) for ti in t], label='Input $U(t)$')
plt.plot(t, y[:,1], label='Output $y(t)$')
plt.grid()
plt.xlabel('Time (s)')
plt.legend(loc='upper left')
plt.savefig(os.path.splitext(__file__)[0] + '.pdf')
plt.show()
