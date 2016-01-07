import os
import numpy as np
from scipy import signal
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
u = np.sin(np.sqrt(k / m) * t)

# System
sys = signal.lti([ 1 ], [ m, c, k ])

# Initial condition
x0 = np.array([ 0.0, 0.0 ])

# Simulate system
T, y, x = signal.lsim(sys, u, t, X0=x0)

# Plot result
plt.plot(T, u, '-k', label='Input $U(t)$')
plt.plot(T, y, '--b', label='Output $y(t)$')
plt.grid()
plt.xlabel('Time (s)')
plt.legend(loc='upper left')
plt.savefig(os.path.splitext(__file__)[0] + '.pdf')
plt.show()
