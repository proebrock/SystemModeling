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
n = 500+1
t = np.linspace(0, 40, num=n)

# Simulate
T, yout = signal.step(sys, T=t)

# Plot result
plt.plot(T, yout)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Output (m)')
plt.savefig(os.path.splitext(__file__)[0] + '.pdf')
plt.show()

