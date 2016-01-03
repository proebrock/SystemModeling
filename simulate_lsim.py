import os
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Parameters for mechanical oscillator
m = 1.0 # Mass [kg]
k = 0.8 # Spring constant [N/m]
c = 0.0 # Damping constant [Ns/m]
sys = signal.lti([ 1 ], [ m, c, k ])

# Time range
n = 500+1
t = np.linspace(0, 40, num=n)

# Input
U = np.sin(np.sqrt(k/m)*t)

# Simulate
T, yout, xout = signal.lsim(sys, U, t, X0=np.array([ 0, 0 ]))

# Plot result
plt.plot(T, U, label='Input $U(t)$')
plt.plot(T, yout, label='Output $y(t)$')
plt.grid()
plt.xlabel('Time (s)')
plt.legend(loc='upper left')
plt.savefig(os.path.splitext(__file__)[0] + '.pdf')
plt.show()
