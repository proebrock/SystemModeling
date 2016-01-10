import os
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Gravitational constant in m^3 / (kg * s^2)
G = 6.67408e-11

# Number of bodies: Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune
k = 9
# Number of DOF: 2d
l = 2

# Masses [kg]
m = np.array([ 1.9891e30, 3.302e23, 4.8690e24, 5.9742e24, 6.4191e23, 1.8987e27, 5.6851e26, 8.6849e25, 1.0244e26 ])
assert(m.size == k)

# Time range
n = 5000+1
t = np.linspace(0, 164.79132 * 365.25 * 24 * 3600, num=n)

def rotate(v, phi):
	return np.dot(np.array([ [ np.cos(phi), -np.sin(phi) ], [ np.sin(phi), np.cos(phi) ] ]), v)

# Initial conditions
x0 = np.array([ \
	# Positions [m]
	[ 0.0, 0.0 ], \
	[ 5.7909175e10, 0.0 ], \
	[ 1.0820893e11, 0.0 ], \
	[ 1.4959789e11, 0.0 ], \
	[ 2.2793664e11, 0.0 ], \
	[ 7.78412010e11, 0.0], \
	[ 1.426725400e12, 0.0 ], \
	[ 2.870972200e12, 0.0 ], \
	[ 4.498252900e12, 0.0 ], \
	# Speeds [m/s]
	[ 0.0, 0.0 ], \
	[ 4.78725e4, 0.0 ], \
	[ 3.50214e4, 0.0 ], \
	[ 2.97859e4, 0.0 ], \
	[ 2.41309e4, 0.0 ], \
	[ 1.30697e4, 0.0 ], \
	[ 9.6724e3, 0.0 ], \
	[ 6.8352e3, 0.0 ], \
	[ 5.4778e3, 0.0 ], \
	])
for i in range(k-1):
	# Rotate positions of planets to evenly distributed them over 360 degrees
	x0[i+1,:] = rotate(x0[i+1,:], (2 * np.pi * i) / k - 1)
for i in range(k-1):
	# Rotate speed vectors that they are orthogonal to line sun <-> planet
	x0[i+k+1,:] = rotate(x0[i+k+1,:], np.pi/2.0 + (2 * np.pi * i) / k - 1)
assert(x0.shape == ( 2 * k, l ))
x0 = x0.reshape(2 * k * l)

def sys(y,t):
	y = y.reshape(( 2 * k, l ))
	x = np.zeros(y.shape)
	for i in range(k):
		x[i,:] = y[i+k,:]
	for i in range(k):
		for j in range(l):
			if not i == j:
				x[i+k] -= (G * m[j] * (y[i,:] - y[j,:])) / np.power(np.linalg.norm(y[i,:] - y[j,:]), 3)
	return x.reshape(2 * k * l)

## Simulate system
sys(x0, 0)
y = odeint(sys, x0, t)

colors = [ 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'orange', 'violet', 'brown' ]
for i in range(k):
	# Plot simulated trajectory
	plt.plot(y[:,2*i+0], y[:,2*i+1], '-', color=colors[i])
for i in range(k):
	# Plot start marker
	plt.plot(y[0,2*i+0], y[0,2*i+1], '*', color=colors[i])
	# Show end marker
	plt.plot(y[-1,2*i+0], y[-1,2*i+1], 'o', color=colors[i])
plt.grid()
plt.axis('equal')
plt.show()
