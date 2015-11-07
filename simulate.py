import os
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Parameters for mechanical oscillator
m = 1.0 # Mass [kg]
k = 0.8 # Spring constant [N/m]
c = 0.3 # Damping constant [Ns/m]

sys = signal.lti([ 1 ], [ m, c, k ])

# Time range
n = 100+1
t = np.linspace(0, 60, num=n)

# Input
U = np.zeros(n)
U[np.where(t >= 30.0)] = 2.0

# Simulate
T, yout, xout = signal.lsim(sys, U, t, X0=np.array([ 1, 0 ]))

# Plot result
plt.plot(T, yout)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Output (m)')
plt.savefig(os.path.splitext(__file__)[0] + '.pdf')
plt.show()
