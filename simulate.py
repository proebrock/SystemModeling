import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters for mechanical oscillator
m = 1.0 # Mass [kg]
k = 0.8 # Spring constant [N/m]
c = 0.3 # Damping constant [Ns/m]

# State space matrices
A = np.array([[ 0, 1 ], [ -k/m, -c/m ]])
B = np.array([[ 0 ], [ 1 ]])
C = np.array([ 1/m, 0 ])
D = np.array([ 0 ])

# Input function
def u(t):
	if t >= 30:
		return np.array([ 2 ])
	else:
		return np.array([ 0 ])

# Helper function for simulation
def func(x, t):
	result = np.dot(A, x) + np.dot(B, u(t))
	return result

# Start condition
x0 = np.array([ 1, 0 ])
# Time range
n = 100+1
t = np.linspace(0, 60, num=n)
# Simulate system
x = odeint(func, x0, t)
# Calculate output
y = np.array([ np.dot(C, x[i]) + np.dot(D, u(t[i])) for i in range(n) ])

# Plot result
plt.plot(t, y)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Output (m)')
plt.show()
