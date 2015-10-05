import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


m = 1 # Mass [kg]
k = 0.8 # Spring constant [N/m]
c = 0.3 # Damping constant [Ns/m]

A = np.array([[ 0, 1 ], [ -k/m, -c/m ]])
B = np.array([[ 0 ], [ 1/m ]])
C = np.array([ 1, 0 ])
D = np.array([ 0 ])

def u(t):
	if t >= 10:
		return np.array([ 2 ])
	else:
		return np.array([ 0 ])

def func(x, t):
	result = np.dot(A, x) + np.dot(B, u(t))
	return result

x0 = np.array([ 0, 0 ])
t = np.linspace(0, 60, num=1001)
x = odeint(func, x0, t)

plt.plot(t, x)
plt.grid()
plt.xlabel('Time (s)')
plt.legend(('$x$ (m)', '$\dot{x}$ (m/s)'))
plt.show()
