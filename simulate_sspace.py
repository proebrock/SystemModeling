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
	return np.array([np.sin(np.sqrt(k / m) * t)])

# System
A = np.array([[ 0, 1 ], [ -k/m, -c/m ]])
B = np.array([[ 0 ], [ 1 ]])
C = np.array([ 1/m, 0 ])
D = np.array([ 0 ])
def sys(x, t):
	return np.dot(A, x) + np.dot(B, u(t))

# Initial condition
x0 = np.array([ 0.0, 0.0 ])

# Simulate system
x = odeint(sys, x0, t)
y = np.array([ np.dot(C, x[i]) + np.dot(D, u(t[i])) for i in range(n) ])

# Plot result
plt.plot(t, [ u(ti) for ti in t], label='Input $U(t)$')
plt.plot(t, y, label='Output $y(t)$')
plt.grid()
plt.xlabel('Time (s)')
plt.legend(loc='upper left')
plt.savefig(os.path.splitext(__file__)[0] + '.pdf')
plt.show()
